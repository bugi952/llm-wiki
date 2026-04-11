import sqlite3
from unittest.mock import patch, MagicMock
import pytest
from db import get_db, init_db
from collector.rss import collect_rss


FAKE_FEED = {
    "bozo": False,
    "entries": [
        {
            "title": "Scaling Laws for Neural LMs",
            "link": "https://arxiv.org/abs/2401.00001",
            "id": "https://arxiv.org/abs/2401.00001",
            "summary": "We study scaling laws for large language models.",
            "published": "2026-04-10T00:00:00Z",
        },
        {
            "title": "Attention Is All You Need v2",
            "link": "https://arxiv.org/abs/2401.00002",
            "id": "https://arxiv.org/abs/2401.00002",
            "summary": "Revisiting transformers with new architecture.",
            "published": "2026-04-10T00:00:00Z",
        },
    ],
}


@pytest.fixture
def db():
    conn = get_db(":memory:")
    init_db(conn)
    yield conn
    conn.close()


@patch("collector.rss.feedparser.parse")
def test_collect_rss_inserts_entries(mock_parse, db):
    mock_parse.return_value = FAKE_FEED
    feeds = [{"name": "arxiv-cs-ai-cl-lg", "url": "https://rss.arxiv.org/rss/cs.AI", "type": "arxiv"}]
    count = collect_rss(db, feeds)
    assert count == 2
    cursor = db.execute("SELECT COUNT(*) FROM sources WHERE source_type='rss'")
    assert cursor.fetchone()[0] == 2


@patch("collector.rss.feedparser.parse")
def test_collect_rss_no_duplicates(mock_parse, db):
    mock_parse.return_value = FAKE_FEED
    feeds = [{"name": "arxiv-cs-ai-cl-lg", "url": "https://rss.arxiv.org/rss/cs.AI", "type": "arxiv"}]
    collect_rss(db, feeds)
    count = collect_rss(db, feeds)
    assert count == 0
    cursor = db.execute("SELECT COUNT(*) FROM sources")
    assert cursor.fetchone()[0] == 2


@patch("collector.rss.feedparser.parse")
def test_collect_rss_sets_domain_for_arxiv(mock_parse, db):
    mock_parse.return_value = FAKE_FEED
    feeds = [{"name": "arxiv-cs-ai-cl-lg", "url": "https://rss.arxiv.org/rss/cs.AI", "type": "arxiv"}]
    collect_rss(db, feeds)
    cursor = db.execute("SELECT domain FROM sources WHERE url=?", ("https://arxiv.org/abs/2401.00001",))
    assert cursor.fetchone()[0] == "ai"


@patch("collector.rss.feedparser.parse")
def test_collect_rss_sets_status_collected(mock_parse, db):
    mock_parse.return_value = FAKE_FEED
    feeds = [{"name": "arxiv-cs-ai-cl-lg", "url": "https://rss.arxiv.org/rss/cs.AI", "type": "arxiv"}]
    collect_rss(db, feeds)
    cursor = db.execute("SELECT status FROM sources LIMIT 1")
    assert cursor.fetchone()[0] == "collected"


@patch("collector.rss.feedparser.parse")
def test_collect_rss_handles_bozo_feed(mock_parse, db):
    mock_parse.return_value = {"bozo": True, "bozo_exception": Exception("bad feed"), "entries": []}
    feeds = [{"name": "bad-feed", "url": "https://example.com/bad", "type": "blog"}]
    count = collect_rss(db, feeds)
    assert count == 0


@patch("collector.rss.feedparser.parse")
def test_collect_rss_fallback_on_rsshub_failure(mock_parse, db):
    """When RSSHub feed fails, should try community fallback URL."""
    fallback_entries = [
        {"title": "Anthropic Update", "link": "https://anthropic.com/update/1",
         "summary": "New feature", "published": "2026-04-10"},
    ]
    # First call (RSSHub) fails, second call (fallback) succeeds
    mock_parse.side_effect = [
        {"bozo": True, "bozo_exception": Exception("connection refused"), "entries": []},
        {"bozo": False, "entries": fallback_entries},
    ]
    feeds = [{"name": "anthropic-blog", "url": "http://localhost:1200/anthropic/blog", "type": "blog"}]
    count = collect_rss(db, feeds)
    assert count == 1
    assert mock_parse.call_count == 2
