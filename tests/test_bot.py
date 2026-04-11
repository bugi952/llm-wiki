from unittest.mock import patch, MagicMock, AsyncMock
import pytest
from db import get_db, init_db


@pytest.fixture
def db():
    conn = get_db(":memory:")
    init_db(conn)
    yield conn
    conn.close()


def test_bot_imports():
    """Verify bot module imports without errors."""
    import bot
    assert hasattr(bot, "main")


def test_bot_has_command_handlers():
    """Verify bot defines expected command handlers."""
    import bot
    assert hasattr(bot, "cmd_add")
    assert hasattr(bot, "cmd_status")
    assert hasattr(bot, "cmd_recent")
    assert hasattr(bot, "cmd_stats")


@patch("bot.get_db")
def test_cmd_status_returns_counts(mock_get_db, db):
    mock_get_db.return_value = db
    # Insert some test data
    db.execute("INSERT INTO sources (source_type, title, status) VALUES ('rss', 'test1', 'collected')")
    db.execute("INSERT INTO sources (source_type, title, status) VALUES ('rss', 'test2', 'ingested')")
    db.commit()

    import bot
    # Test the status query logic directly
    counts = bot._get_status_counts(db)
    assert counts["collected"] == 1
    assert counts["ingested"] == 1


@patch("bot.get_db")
def test_cmd_recent_returns_items(mock_get_db, db):
    mock_get_db.return_value = db
    db.execute(
        "INSERT INTO sources (source_type, title, url, status, importance) VALUES ('rss', 'Test Article', 'https://example.com', 'ingested', 'insight')")
    db.commit()

    import bot
    items = bot._get_recent_items(db, limit=5)
    assert len(items) == 1
    assert items[0]["title"] == "Test Article"
