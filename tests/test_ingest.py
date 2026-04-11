import json
import os
import tempfile
from unittest.mock import patch
import pytest
from db import get_db, init_db
from wiki.ingest import ingest, _make_slug


@pytest.fixture
def db():
    conn = get_db(":memory:")
    init_db(conn)
    yield conn
    conn.close()


@pytest.fixture
def vault_dir(tmp_path):
    (tmp_path / "ai").mkdir()
    (tmp_path / "macro").mkdir()
    return str(tmp_path)


def _insert_quality_pass(db, title="Scaling Laws v2", url="https://arxiv.org/abs/2401.00001",
                         domain="ai", importance="insight", content="Novel scaling results"):
    db.execute(
        """INSERT INTO sources (source_type, feed_name, domain, title, url, content,
           published_at, status, importance)
           VALUES ('rss', 'arxiv-cs-ai-cl-lg', ?, ?, ?, ?, '2026-04-10', 'quality_pass', ?)""",
        (domain, title, url, content, importance),
    )
    db.commit()


def test_make_slug():
    assert _make_slug("Scaling Laws for Neural LMs") == "scaling-laws-for-neural-lms"
    assert _make_slug("GPT-5: A New Era!") == "gpt-5-a-new-era"
    assert _make_slug("한글 제목 Test") == "test"


@patch("wiki.ingest.call_haiku_ingest")
def test_ingest_creates_file(mock_haiku, db, vault_dir):
    _insert_quality_pass(db)
    mock_haiku.return_value = {
        "summary": "Scaling laws show predictable performance gains.",
        "whats_new": "First empirical validation at 10T parameter scale."
    }
    count = ingest(db, vault_dir)
    assert count == 1

    # Check file exists
    files = os.listdir(os.path.join(vault_dir, "ai"))
    assert len(files) == 1
    assert files[0].endswith(".md")
    assert "scaling-laws" in files[0]


@patch("wiki.ingest.call_haiku_ingest")
def test_ingest_file_has_frontmatter(mock_haiku, db, vault_dir):
    _insert_quality_pass(db)
    mock_haiku.return_value = {
        "summary": "Summary text.",
        "whats_new": "New findings."
    }
    ingest(db, vault_dir)

    files = os.listdir(os.path.join(vault_dir, "ai"))
    with open(os.path.join(vault_dir, "ai", files[0])) as f:
        content = f.read()
    assert "---" in content
    assert "title:" in content
    assert "importance: insight" in content
    assert "## 핵심" in content
    assert "## 새로운 점" in content


@patch("wiki.ingest.call_haiku_ingest")
def test_ingest_updates_db_status(mock_haiku, db, vault_dir):
    _insert_quality_pass(db)
    mock_haiku.return_value = {"summary": "S", "whats_new": "N"}
    ingest(db, vault_dir)
    cursor = db.execute("SELECT status, vault_path FROM sources LIMIT 1")
    row = cursor.fetchone()
    assert row[0] == "ingested"
    assert row[1] is not None


@patch("wiki.ingest.call_haiku_ingest")
def test_ingest_idempotent(mock_haiku, db, vault_dir):
    _insert_quality_pass(db)
    mock_haiku.return_value = {"summary": "S", "whats_new": "N"}
    ingest(db, vault_dir)
    count = ingest(db, vault_dir)  # second run
    assert count == 0  # nothing new to ingest
