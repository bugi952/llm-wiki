import json
import os
import pytest
from db import get_db, init_db
from wiki.ingest import ingest, _make_slug, _parse_date


@pytest.fixture
def db():
    conn = get_db(":memory:")
    init_db(conn)
    yield conn
    conn.close()


@pytest.fixture
def vault_dir(tmp_path):
    for d in ["ai/entities", "ai/concepts", "ai/weekly", "macro/indicators", "macro/weekly"]:
        (tmp_path / d).mkdir(parents=True)
    return str(tmp_path)


def _insert_quality_pass(db, title="Scaling Laws v2", url="https://arxiv.org/abs/2401.00001",
                         domain="ai", importance="insight", content="Novel scaling results",
                         routing=None):
    """Insert a quality_pass source with pre-computed routing in filter_b_result."""
    if routing is None:
        routing = {
            "entities": [], "concepts": [], "new_pages": [],
            "facts": [], "summary_ko": "요약", "whats_new": "",
        }
    db.execute(
        """INSERT INTO sources (source_type, feed_name, domain, title, url, content,
           published_at, status, importance, filter_b_result)
           VALUES ('rss', 'arxiv-cs-ai-cl-lg', ?, ?, ?, ?, '2026-04-10', 'quality_pass', ?, ?)""",
        (domain, title, url, content, importance, json.dumps(routing)),
    )
    db.commit()


def test_parse_date_iso():
    assert _parse_date("2026-04-10") == "2026-04-10"
    assert _parse_date("2026-04-10T12:00:00Z") == "2026-04-10"


def test_parse_date_rfc2822():
    assert _parse_date("Thu, 02 Apr 2026 12:00:00 GMT") == "2026-04-02"
    assert _parse_date("Mon, 09 Mar 2026 00:00:00 +0000") == "2026-03-09"


def test_parse_date_empty():
    from datetime import date
    today = date.today().isoformat()
    assert _parse_date(None) == today
    assert _parse_date("") == today


def test_make_slug():
    assert _make_slug("Scaling Laws for Neural LMs") == "scaling-laws-for-neural-lms"
    assert _make_slug("GPT-5: A New Era!") == "gpt-5-a-new-era"
    assert _make_slug("한글 제목 Test") == "test"


def test_ingest_uses_routing_from_filter_b(db, vault_dir, monkeypatch):
    monkeypatch.setattr("wiki.pages.VAULT_DIR", vault_dir)

    routing = {
        "entities": ["arXiv"],
        "concepts": ["Scaling Laws"],
        "new_pages": [],
        "facts": [
            {"page": "Scaling Laws", "entry": "10T 파라미터 스케일 검증 완료", "date": "2026-04-10"}
        ],
        "summary_ko": "스케일링 법칙의 10T 파라미터 규모 검증.",
        "whats_new": "최초 10T 규모 실증",
    }
    _insert_quality_pass(db, routing=routing)

    # Pre-create target pages
    from wiki.pages import create_page
    create_page(db, "ai/concepts/Scaling Laws", "Scaling Laws", "concept", "ai")

    count = ingest(db, vault_dir)
    assert count == 1

    # Check page was updated
    concept_path = os.path.join(vault_dir, "ai", "concepts", "Scaling Laws.md")
    content = open(concept_path).read()
    assert "10T 파라미터" in content


def test_ingest_updates_db_status(db, vault_dir, monkeypatch):
    monkeypatch.setattr("wiki.pages.VAULT_DIR", vault_dir)
    _insert_quality_pass(db)
    ingest(db, vault_dir)
    cursor = db.execute("SELECT status FROM sources LIMIT 1")
    assert cursor.fetchone()[0] == "ingested"


def test_ingest_idempotent(db, vault_dir, monkeypatch):
    monkeypatch.setattr("wiki.pages.VAULT_DIR", vault_dir)
    _insert_quality_pass(db)
    ingest(db, vault_dir)
    count = ingest(db, vault_dir)
    assert count == 0  # nothing new


def test_ingest_creates_weekly_digest(db, vault_dir, monkeypatch):
    monkeypatch.setattr("wiki.pages.VAULT_DIR", vault_dir)
    _insert_quality_pass(db)
    ingest(db, vault_dir)

    # Weekly digest should exist
    weekly_files = os.listdir(os.path.join(vault_dir, "ai", "weekly"))
    assert len(weekly_files) >= 1


def test_ingest_handles_missing_filter_b_result(db, vault_dir, monkeypatch):
    """Sources with NULL filter_b_result should still be ingested (empty routing)."""
    monkeypatch.setattr("wiki.pages.VAULT_DIR", vault_dir)
    db.execute(
        """INSERT INTO sources (source_type, feed_name, domain, title, url, content,
           published_at, status, importance, filter_b_result)
           VALUES ('rss', 'test', 'ai', 'Test', 'https://x.com/1', 'content',
           '2026-04-10', 'quality_pass', 'background', NULL)""",
    )
    db.commit()
    count = ingest(db, vault_dir)
    assert count == 1
    cursor = db.execute("SELECT status FROM sources LIMIT 1")
    assert cursor.fetchone()[0] == "ingested"
