import json
import logging
import os

from config import get_config
from llm import claude_call

logger = logging.getLogger(__name__)


def _load_index_md(domain):
    """Load existing index.md for context."""
    path = f"vault/{domain}/index.md"
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return "(아직 인덱스 없음)"


def call_haiku_quality(title, content, index_context, conn):
    """Call Claude CLI to score quality + novelty. Returns dict."""
    cfg = get_config()
    max_len = cfg["filter"]["max_content_length_quality"]
    prompt = f"""품질 평가기. 기존 Wiki 지식 대비 새로운 가치가 있는지 판별.

기존 Wiki 인덱스:
{index_context}

새 소스:
제목: {title}
내용: {content[:max_len]}

평가 후 JSON만 출력:
{{"novelty": 1-5, "importance": 1-5, "reliability": 1-5, "average": float, "importance_tag": "urgent"|"insight"|"connection"|"background", "reason": "한줄"}}"""

    return claude_call(prompt, conn=conn, expect_json=True)


def filter_quality(conn, threshold=None):
    """Run Filter B on all topic_pass sources.

    Returns (passed_count, failed_count).
    """
    if threshold is None:
        threshold = get_config()["filter"]["quality_score_threshold"]

    cursor = conn.execute(
        "SELECT id, domain, title, content FROM sources WHERE status = 'topic_pass'"
    )
    rows = cursor.fetchall()

    passed = 0
    failed = 0

    # Cache index content per domain
    index_cache = {}

    for source_id, domain, title, content in rows:
        if domain not in index_cache:
            index_cache[domain] = _load_index_md(domain)

        try:
            result = call_haiku_quality(title, content or "", index_cache[domain], conn)
        except Exception as e:
            logger.error("Quality eval failed for source %d: %s", source_id, e)
            conn.execute("UPDATE sources SET status = 'quality_fail' WHERE id = ?", (source_id,))
            failed += 1
            continue

        average = result.get("average", 0.0)
        importance_tag = result.get("importance_tag", "background")

        if average >= threshold:
            conn.execute(
                "UPDATE sources SET status = 'quality_pass', importance = ?, filter_b_result = ? WHERE id = ?",
                (importance_tag, json.dumps(result), source_id),
            )
            passed += 1
            logger.info("Quality pass: %s [%.1f, %s]", title, average, importance_tag)
        else:
            conn.execute(
                "UPDATE sources SET status = 'quality_fail', filter_b_result = ? WHERE id = ?",
                (json.dumps(result), source_id),
            )
            failed += 1
            logger.info("Quality fail: %s [%.1f]", title, average)

    conn.commit()
    return passed, failed
