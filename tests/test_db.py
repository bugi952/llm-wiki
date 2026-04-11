import sqlite3
import pytest
from db import get_db, init_db, log_event, get_daily_api_count, increment_api_count


@pytest.fixture
def db():
    """In-memory SQLite for testing."""
    conn = get_db(":memory:")
    init_db(conn)
    yield conn
    conn.close()


def test_init_db_creates_tables(db):
    cursor = db.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
    )
    tables = [row[0] for row in cursor.fetchall()]
    assert "sources" in tables
    assert "filter_stats" in tables
    assert "system_log" in tables


def test_init_db_idempotent(db):
    # calling init_db again should not raise
    init_db(db)
    cursor = db.execute(
        "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
    )
    tables = [row[0] for row in cursor.fetchall()]
    assert "sources" in tables


def test_sources_unique_url(db):
    db.execute(
        "INSERT INTO sources (source_type, title, url) VALUES (?, ?, ?)",
        ("rss", "Test", "https://example.com/1"),
    )
    db.commit()
    with pytest.raises(sqlite3.IntegrityError):
        db.execute(
            "INSERT INTO sources (source_type, title, url) VALUES (?, ?, ?)",
            ("rss", "Test Dup", "https://example.com/1"),
        )


def test_sources_unique_story_url(db):
    db.execute(
        "INSERT INTO sources (source_type, title, url, story_url) VALUES (?, ?, ?, ?)",
        ("hackernews", "HN1", "https://hn.com/1", "https://example.com/story"),
    )
    db.commit()
    with pytest.raises(sqlite3.IntegrityError):
        db.execute(
            "INSERT INTO sources (source_type, title, url, story_url) VALUES (?, ?, ?, ?)",
            ("hackernews", "HN2", "https://hn.com/2", "https://example.com/story"),
        )


def test_log_event(db):
    log_event(db, "collect", '{"source": "arxiv", "count": 5}')
    cursor = db.execute("SELECT event, details FROM system_log")
    row = cursor.fetchone()
    assert row[0] == "collect"
    assert "arxiv" in row[1]


def test_api_count_starts_zero(db):
    assert get_daily_api_count(db) == 0


def test_increment_api_count(db):
    increment_api_count(db)
    increment_api_count(db)
    # Verify events were inserted
    count = db.execute("SELECT COUNT(*) FROM system_log WHERE event = 'api_call'").fetchone()[0]
    assert count == 2


def test_filter_stats_unique_date(db):
    db.execute(
        "INSERT INTO filter_stats (date, total_collected) VALUES ('2026-04-11', 10)"
    )
    db.commit()
    with pytest.raises(sqlite3.IntegrityError):
        db.execute(
            "INSERT INTO filter_stats (date, total_collected) VALUES ('2026-04-11', 20)"
        )
