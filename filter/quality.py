import json
import logging
import os

import anthropic
from db import increment_api_count

logger = logging.getLogger(__name__)

QUALITY_SCORE_THRESHOLD = 3.0


def _load_index_md(domain):
    """Load existing index.md for context."""
    path = f"vault/{domain}/index.md"
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return "(아직 인덱스 없음)"


def call_haiku_quality(title, content, index_context, conn):
    """Call Claude Haiku to score quality + novelty. Returns dict."""
    client = anthropic.Anthropic()
    increment_api_count(conn)

    resp = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=300,
        system="품질 평가기. 기존 Wiki 지식 대비 새로운 가치가 있는지 판별. JSON으로 응답.",
        messages=[{"role": "user", "content": f"""기존 Wiki 인덱스:
{index_context}

새 소스:
제목: {title}
내용: {content[:1000]}

평가 (JSON):
{{"novelty": 1-5, "importance": 1-5, "reliability": 1-5, "average": float, "importance_tag": "urgent"|"insight"|"connection"|"background", "reason": "한줄"}}"""}],
    )

    text = resp.content[0].text.strip()
    if "{" in text:
        text = text[text.index("{"):text.rindex("}") + 1]
    return json.loads(text)


def filter_quality(conn, threshold=QUALITY_SCORE_THRESHOLD):
    """Run Filter B on all topic_pass sources.

    Returns (passed_count, failed_count).
    """
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
