import os
import time
from unittest.mock import patch, MagicMock
import pytest
from db import get_db, init_db
from scheduler import run_auto, acquire_lock, release_lock, LOCK_FILE


@pytest.fixture
def db():
    conn = get_db(":memory:")
    init_db(conn)
    yield conn
    conn.close()


@pytest.fixture
def clean_lock():
    """Ensure no stale lock file."""
    release_lock()
    if os.path.exists(LOCK_FILE):
        os.remove(LOCK_FILE)
    yield
    release_lock()
    if os.path.exists(LOCK_FILE):
        os.remove(LOCK_FILE)


def test_acquire_lock(clean_lock):
    assert acquire_lock() is True
    assert os.path.exists(LOCK_FILE)
    release_lock()
    assert not os.path.exists(LOCK_FILE)


def test_lock_blocks_concurrent(clean_lock):
    """Lock should block a second process (simulated via subprocess)."""
    import subprocess, sys
    assert acquire_lock() is True
    # Try to acquire from a child process
    code = "from scheduler import acquire_lock; import sys; sys.exit(0 if acquire_lock() else 1)"
    result = subprocess.run([sys.executable, "-c", code], capture_output=True, timeout=5)
    assert result.returncode == 1  # child should fail to acquire
    release_lock()


@patch("scheduler.sync_vault")
@patch("scheduler.update_index")
@patch("scheduler.ingest")
@patch("scheduler.filter_quality")
@patch("scheduler.filter_topic")
@patch("scheduler.collect_coingecko", return_value=3)
@patch("scheduler.collect_ecos", return_value=1)
@patch("scheduler.collect_fred", return_value=2)
@patch("scheduler.collect_hackernews", return_value=3)
@patch("scheduler.collect_rss")
def test_run_auto_full_pipeline(mock_rss, mock_hn, mock_fred, mock_ecos,
                                 mock_coingecko, mock_topic, mock_quality,
                                 mock_ingest, mock_index, mock_sync, db, clean_lock):
    mock_rss.return_value = 5
    mock_topic.return_value = (3, 2)
    mock_quality.return_value = (2, 1)
    mock_ingest.return_value = 2
    mock_sync.return_value = {"changed": True, "committed": True, "pushed": False}

    result = run_auto(db)
    assert result["collected"] == 14  # 5+3+2+1+3
    assert result["topic_passed"] == 3
    assert result["quality_passed"] == 2
    assert result["ingested"] == 2
    assert mock_rss.called
    assert mock_hn.called
    assert mock_fred.called
    assert mock_ecos.called


@patch("scheduler.send_alert")
@patch("scheduler.sync_vault")
@patch("scheduler.update_index")
@patch("scheduler.ingest")
@patch("scheduler.filter_quality")
@patch("scheduler.filter_topic")
@patch("scheduler.collect_ecos")
@patch("scheduler.collect_fred")
@patch("scheduler.collect_hackernews")
@patch("scheduler.collect_rss")
def test_run_auto_api_limit(mock_rss, mock_hn, mock_fred, mock_ecos,
                            mock_topic, mock_quality, mock_ingest, mock_index,
                            mock_sync, mock_alert, db, clean_lock):
    """Pipeline should stop if daily API count exceeds 300."""
    from datetime import datetime, timezone
    today_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    for _ in range(301):
        db.execute("INSERT INTO system_log (event, created_at) VALUES ('api_call', ?)",
                   (f"{today_utc} 12:00:00",))
    db.commit()

    result = run_auto(db)
    assert result.get("error") == "api_limit_exceeded"
    assert not mock_rss.called
    assert mock_alert.called
