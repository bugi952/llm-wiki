import json
from unittest.mock import patch
import pytest
from db import get_db, init_db
from filter.quality import filter_quality


@pytest.fixture
def db():
    conn = get_db(":memory:")
    init_db(conn)
    yield conn
    conn.close()


def _insert_topic_pass(db, title="Good Paper", url="https://arxiv.org/abs/1",
                       content="Novel findings about LLMs", domain="ai", importance=None):
    db.execute(
        """INSERT INTO sources (source_type, feed_name, domain, title, url, content, status, importance)
           VALUES ('rss', 'arxiv-cs-ai-cl-lg', ?, ?, ?, ?, 'topic_pass', ?)""",
        (domain, title, url, content, importance),
    )
    db.commit()


@patch("filter.quality.call_haiku_quality")
def test_quality_pass_above_threshold(mock_haiku, db):
    _insert_topic_pass(db)
    mock_haiku.return_value = {
        "novelty": 4, "importance": 4, "reliability": 5,
        "average": 4.3, "importance_tag": "insight",
        "reason": "New scaling law results"
    }
    passed, failed = filter_quality(db)
    assert passed == 1
    assert failed == 0
    cursor = db.execute("SELECT status, importance FROM sources LIMIT 1")
    row = cursor.fetchone()
    assert row[0] == "quality_pass"
    assert row[1] == "insight"


@patch("filter.quality.call_haiku_quality")
def test_quality_fail_below_threshold(mock_haiku, db):
    _insert_topic_pass(db, url="https://arxiv.org/abs/2")
    mock_haiku.return_value = {
        "novelty": 1, "importance": 2, "reliability": 3,
        "average": 2.0, "importance_tag": "background",
        "reason": "Already known information"
    }
    passed, failed = filter_quality(db)
    assert passed == 0
    assert failed == 1
    cursor = db.execute("SELECT status FROM sources LIMIT 1")
    assert cursor.fetchone()[0] == "quality_fail"


@patch("filter.quality.call_haiku_quality")
def test_quality_stores_filter_result(mock_haiku, db):
    _insert_topic_pass(db, url="https://arxiv.org/abs/3")
    result = {
        "novelty": 5, "importance": 4, "reliability": 4,
        "average": 4.3, "importance_tag": "urgent",
        "reason": "Major breakthrough"
    }
    mock_haiku.return_value = result
    filter_quality(db)
    cursor = db.execute("SELECT filter_b_result FROM sources LIMIT 1")
    stored = json.loads(cursor.fetchone()[0])
    assert stored["novelty"] == 5
    assert stored["importance_tag"] == "urgent"


@patch("filter.quality.call_haiku_quality")
def test_quality_exact_threshold_passes(mock_haiku, db):
    _insert_topic_pass(db, url="https://arxiv.org/abs/4")
    mock_haiku.return_value = {
        "novelty": 3, "importance": 3, "reliability": 3,
        "average": 3.0, "importance_tag": "background",
        "reason": "Borderline"
    }
    passed, failed = filter_quality(db)
    assert passed == 1
