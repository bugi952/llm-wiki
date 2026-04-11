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
    if os.path.exists(LOCK_FILE):
        os.remove(LOCK_FILE)
    yield
    if os.path.exists(LOCK_FILE):
        os.remove(LOCK_FILE)


def test_acquire_lock(clean_lock):
    assert acquire_lock() is True
    assert os.path.exists(LOCK_FILE)
    release_lock()
    assert not os.path.exists(LOCK_FILE)


def test_lock_blocks_second_run(clean_lock):
    assert acquire_lock() is True
    assert acquire_lock() is False
    release_lock()


def test_stale_lock_auto_removed(clean_lock):
    """Lock older than 1 hour should be auto-removed."""
    acquire_lock()
    # Backdate the lock file
    old_time = time.time() - 3700  # 1h+ ago
    os.utime(LOCK_FILE, (old_time, old_time))
    assert acquire_lock() is True  # stale lock removed
    release_lock()


@patch("scheduler.sync_vault")
@patch("scheduler.update_index")
@patch("scheduler.ingest")
@patch("scheduler.filter_quality")
@patch("scheduler.filter_topic")
@patch("scheduler.collect_rss")
def test_run_auto_full_pipeline(mock_collect, mock_topic, mock_quality,
                                 mock_ingest, mock_index, mock_sync, db, clean_lock):
    mock_collect.return_value = 5
    mock_topic.return_value = (3, 2)
    mock_quality.return_value = (2, 1)
    mock_ingest.return_value = 2
    mock_sync.return_value = {"changed": True, "committed": True, "pushed": False}

    result = run_auto(db)
    assert result["collected"] == 5
    assert result["topic_passed"] == 3
    assert result["quality_passed"] == 2
    assert result["ingested"] == 2
    assert mock_collect.called
    assert mock_topic.called
    assert mock_quality.called
    assert mock_ingest.called
    assert mock_index.called
    assert mock_sync.called


@patch("scheduler.collect_rss")
def test_run_auto_api_limit(mock_collect, db, clean_lock):
    """Pipeline should stop if daily API count exceeds 300."""
    # Insert 301 api_call events
    for _ in range(301):
        db.execute("INSERT INTO system_log (event) VALUES ('api_call')")
    db.commit()

    result = run_auto(db)
    assert result.get("error") == "api_limit_exceeded"
    assert not mock_collect.called
