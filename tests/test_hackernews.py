from unittest.mock import patch, MagicMock
import pytest
from db import get_db, init_db
from collector.hackernews import collect_hackernews


@pytest.fixture
def db():
    conn = get_db(":memory:")
    init_db(conn)
    yield conn
    conn.close()


FAKE_TOP_IDS = [1, 2, 3, 4, 5]

FAKE_ITEMS = {
    1: {"id": 1, "title": "New GPT-5 model released by OpenAI", "url": "https://openai.com/gpt5",
        "score": 200, "type": "story", "time": 1712800000},
    2: {"id": 2, "title": "Best pizza in NYC 2026", "url": "https://pizza.com/best",
        "score": 150, "type": "story", "time": 1712800000},
    3: {"id": 3, "title": "Claude agent framework update", "url": "https://anthropic.com/agents",
        "score": 80, "type": "story", "time": 1712800000},
    4: {"id": 4, "title": "Show HN: My side project", "url": "https://example.com/side",
        "score": 30, "type": "story", "time": 1712800000},  # score < 50
    5: {"id": 5, "title": "Transformer architecture breakthrough", "url": "https://arxiv.org/new",
        "score": 300, "type": "story", "time": 1712800000},
}


def _mock_get(url, **kwargs):
    resp = MagicMock()
    resp.raise_for_status = MagicMock()
    if "topstories" in url:
        resp.json.return_value = FAKE_TOP_IDS
    else:
        item_id = int(url.split("/")[-1].replace(".json", ""))
        resp.json.return_value = FAKE_ITEMS.get(item_id, {})
    return resp


@patch("collector.hackernews.requests.get", side_effect=_mock_get)
def test_collect_hn_filters_ai_keywords(mock_get, db):
    count = collect_hackernews(db)
    # GPT-5 (score 200, AI keyword) + Claude agent (score 80, AI keyword) + Transformer (score 300, AI keyword) = 3
    # Pizza (no AI keyword) skipped, side project (score < 50) skipped
    assert count == 3


@patch("collector.hackernews.requests.get", side_effect=_mock_get)
def test_collect_hn_no_duplicates(mock_get, db):
    collect_hackernews(db)
    count = collect_hackernews(db)
    assert count == 0


@patch("collector.hackernews.requests.get", side_effect=_mock_get)
def test_collect_hn_sets_status(mock_get, db):
    collect_hackernews(db)
    cursor = db.execute("SELECT status, source_type FROM sources LIMIT 1")
    row = cursor.fetchone()
    assert row[0] == "collected"
    assert row[1] == "hackernews"


@patch("collector.hackernews.requests.get", side_effect=_mock_get)
def test_collect_hn_uses_story_url_for_dedup(mock_get, db):
    collect_hackernews(db)
    cursor = db.execute("SELECT story_url FROM sources WHERE title LIKE '%GPT-5%'")
    row = cursor.fetchone()
    assert row[0] == "https://openai.com/gpt5"


@patch("collector.hackernews.requests.get", side_effect=_mock_get)
def test_collect_hn_score_threshold(mock_get, db):
    collect_hackernews(db)
    cursor = db.execute("SELECT title FROM sources")
    titles = [r[0] for r in cursor.fetchall()]
    assert "Show HN: My side project" not in titles  # score 30 < 50
