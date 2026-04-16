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
    return db.execute("SELECT last_insert_rowid()").fetchone()[0]


@patch("filter.quality._call_batch")
def test_quality_pass_above_threshold(mock_batch, db):
    sid = _insert_topic_pass(db)
    mock_batch.return_value = [{
        "id": sid, "novelty": 4, "importance": 4, "reliability": 5,
        "average": 4.3, "importance_tag": "insight", "reason": "New scaling law results",
        "entities": [], "concepts": [], "new_pages": [], "facts": [],
        "summary_ko": "", "whats_new": "",
    }]
    passed, failed = filter_quality(db)
    assert passed == 1
    assert failed == 0
    cursor = db.execute("SELECT status, importance FROM sources LIMIT 1")
    row = cursor.fetchone()
    assert row[0] == "quality_pass"
    assert row[1] == "insight"


@patch("filter.quality._call_batch")
def test_quality_fail_below_threshold(mock_batch, db):
    sid = _insert_topic_pass(db, url="https://arxiv.org/abs/2")
    mock_batch.return_value = [{
        "id": sid, "novelty": 1, "importance": 2, "reliability": 3,
        "average": 2.0, "importance_tag": "background", "reason": "Already known",
        "entities": [], "concepts": [], "new_pages": [], "facts": [],
        "summary_ko": "", "whats_new": "",
    }]
    passed, failed = filter_quality(db)
    assert passed == 0
    assert failed == 1
    cursor = db.execute("SELECT status FROM sources LIMIT 1")
    assert cursor.fetchone()[0] == "quality_fail"


@patch("filter.quality._call_batch")
def test_quality_stores_routing_in_filter_result(mock_batch, db):
    sid = _insert_topic_pass(db, url="https://arxiv.org/abs/3")
    result = {
        "id": sid, "novelty": 5, "importance": 4, "reliability": 4,
        "average": 4.3, "importance_tag": "urgent", "reason": "Major breakthrough",
        "entities": ["OpenAI"], "concepts": ["Scaling Laws"],
        "new_pages": [], "facts": [{"page": "OpenAI", "entry": "신규 발표", "date": "2026-04-10"}],
        "summary_ko": "요약", "whats_new": "새로운 점",
    }
    mock_batch.return_value = [result]
    filter_quality(db)
    cursor = db.execute("SELECT filter_b_result FROM sources LIMIT 1")
    stored = json.loads(cursor.fetchone()[0])
    assert stored["novelty"] == 5
    assert stored["importance_tag"] == "urgent"
    # Routing info also stored
    assert stored["entities"] == ["OpenAI"]
    assert len(stored["facts"]) == 1


@patch("filter.quality._call_batch")
def test_quality_exact_threshold_passes(mock_batch, db):
    sid = _insert_topic_pass(db, url="https://arxiv.org/abs/4")
    mock_batch.return_value = [{
        "id": sid, "novelty": 3, "importance": 3, "reliability": 3,
        "average": 3.0, "importance_tag": "background", "reason": "Borderline",
        "entities": [], "concepts": [], "new_pages": [], "facts": [],
        "summary_ko": "", "whats_new": "",
    }]
    passed, failed = filter_quality(db)
    assert passed == 1


@patch("filter.quality._call_batch")
def test_quality_batch_groups_by_domain(mock_batch, db):
    """Sources from same domain should be batched together."""
    sid1 = _insert_topic_pass(db, title="AI Paper 1", url="https://a.com/1", domain="ai")
    sid2 = _insert_topic_pass(db, title="AI Paper 2", url="https://a.com/2", domain="ai")
    sid3 = _insert_topic_pass(db, title="Macro Data", url="https://b.com/1", domain="macro")

    def fake_batch(sources, *args):
        return [{"id": s[0], "novelty": 4, "importance": 4, "reliability": 4,
                 "average": 4.0, "importance_tag": "insight", "reason": "ok",
                 "entities": [], "concepts": [], "new_pages": [], "facts": [],
                 "summary_ko": "", "whats_new": ""} for s in sources]

    mock_batch.side_effect = fake_batch
    passed, failed = filter_quality(db)
    assert passed == 3
    # Should have been called twice: once for ai (2 sources), once for macro (1 source)
    assert mock_batch.call_count == 2


@patch("filter.quality._call_batch")
def test_quality_batch_failure_marks_all_failed(mock_batch, db):
    """If a batch CLI call fails, all sources in that batch should be quality_fail."""
    _insert_topic_pass(db, title="P1", url="https://c.com/1")
    _insert_topic_pass(db, title="P2", url="https://c.com/2")
    mock_batch.side_effect = RuntimeError("CLI crashed")
    passed, failed = filter_quality(db)
    assert passed == 0
    assert failed == 2
