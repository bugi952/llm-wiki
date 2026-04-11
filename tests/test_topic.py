import json
from unittest.mock import patch, MagicMock
import pytest
from db import get_db, init_db
from filter.topic import filter_topic


@pytest.fixture
def db():
    conn = get_db(":memory:")
    init_db(conn)
    yield conn
    conn.close()


def _insert_source(db, source_type="rss", feed_name="arxiv-cs-ai-cl-lg", domain="ai",
                   title="Test Paper", url="https://arxiv.org/abs/1", content="About LLMs"):
    db.execute(
        """INSERT INTO sources (source_type, feed_name, domain, title, url, content, status)
           VALUES (?, ?, ?, ?, ?, ?, 'collected')""",
        (source_type, feed_name, domain, title, url, content),
    )
    db.commit()


def test_arxiv_skips_llm(db):
    """arXiv sources should skip LLM call and directly pass with domain='ai'."""
    _insert_source(db, feed_name="arxiv-cs-ai-cl-lg", domain="ai")
    passed, failed = filter_topic(db)
    assert passed == 1
    assert failed == 0
    cursor = db.execute("SELECT status, domain FROM sources WHERE url=?", ("https://arxiv.org/abs/1",))
    row = cursor.fetchone()
    assert row[0] == "topic_pass"
    assert row[1] == "ai"


def test_known_blog_skips_llm(db):
    """Anthropic/OpenAI/DeepMind blogs should skip LLM."""
    _insert_source(db, feed_name="anthropic-blog", domain="ai",
                   url="https://anthropic.com/blog/1", title="New Claude Feature")
    passed, failed = filter_topic(db)
    assert passed == 1
    assert failed == 0


def test_known_macro_skips_llm(db):
    """FRED/ECOS sources with domain='macro' should skip LLM."""
    _insert_source(db, source_type="fred", feed_name="CPI", domain="macro",
                   url="https://fred.com/cpi", title="CPI March 2026")
    passed, failed = filter_topic(db)
    assert passed == 1
    cursor = db.execute("SELECT status FROM sources LIMIT 1")
    assert cursor.fetchone()[0] == "topic_pass"


@patch("filter.topic.call_haiku")
def test_mixed_source_calls_llm(mock_haiku, db):
    """HN source without domain should call Haiku for classification."""
    _insert_source(db, source_type="hackernews", feed_name="hackernews", domain=None,
                   url="https://hn.com/1", title="New GPT-5 Released", content="OpenAI released GPT-5")
    mock_haiku.return_value = {"domain": "ai", "confidence": 0.9}
    passed, failed = filter_topic(db)
    assert passed == 1
    assert mock_haiku.called


@patch("filter.topic.call_haiku")
def test_irrelevant_source_fails(mock_haiku, db):
    """Irrelevant HN source should be marked topic_fail."""
    _insert_source(db, source_type="hackernews", feed_name="hackernews", domain=None,
                   url="https://hn.com/2", title="Best Pizza in NYC", content="Pizza review")
    mock_haiku.return_value = {"domain": "irrelevant", "confidence": 0.8}
    passed, failed = filter_topic(db)
    assert passed == 0
    assert failed == 1
    cursor = db.execute("SELECT status FROM sources LIMIT 1")
    assert cursor.fetchone()[0] == "topic_fail"


@patch("filter.topic.call_haiku")
def test_low_confidence_fails(mock_haiku, db):
    """Source with confidence below threshold should fail."""
    _insert_source(db, source_type="hackernews", feed_name="hackernews", domain=None,
                   url="https://hn.com/3", title="Maybe AI?", content="Ambiguous content")
    mock_haiku.return_value = {"domain": "ai", "confidence": 0.3}
    passed, failed = filter_topic(db)
    assert passed == 0
    assert failed == 1
