import json
import logging

from config import get_config
from llm import claude_call

logger = logging.getLogger(__name__)

# Feed names where domain is already known (no CLI needed)
KNOWN_DOMAIN_FEEDS = {
    "arxiv-cs-ai-cl-lg", "anthropic-blog", "openai-blog", "deepmind-blog", "import-ai",
}
KNOWN_MACRO_TYPES = {"fred", "ecos", "finnhub"}


def call_haiku(title, content, conn):
    """Call Claude CLI to classify topic. Returns dict with domain + confidence."""
    cfg = get_config()
    max_len = cfg["filter"]["max_content_length_topic"]
    prompt = (
        "분류기. 주어진 텍스트가 AI, Macro, 또는 무관한지 판별.\n\n"
        f"제목: {title}\n내용: {content[:max_len]}\n\n"
        'JSON만 출력: {"domain": "ai"|"macro"|"irrelevant", "confidence": 0.0~1.0}'
    )
    return claude_call(prompt, conn=conn, expect_json=True)


def filter_topic(conn, confidence_threshold=None):
    """Run Filter A on all collected sources.

    Returns (passed_count, failed_count).
    """
    if confidence_threshold is None:
        confidence_threshold = get_config()["filter"]["topic_confidence_threshold"]

    cursor = conn.execute(
        "SELECT id, source_type, feed_name, domain, title, content FROM sources WHERE status = 'collected'"
    )
    rows = cursor.fetchall()

    passed = 0
    failed = 0

    for row in rows:
        source_id, source_type, feed_name, domain, title, content = row

        # Known domain sources: skip CLI
        if feed_name in KNOWN_DOMAIN_FEEDS or source_type in KNOWN_MACRO_TYPES:
            if not domain:
                domain = "macro" if source_type in KNOWN_MACRO_TYPES else "ai"
            conn.execute(
                "UPDATE sources SET status = 'topic_pass', domain = ?, filter_a_result = ? WHERE id = ?",
                (domain, json.dumps({"domain": domain, "confidence": 1.0, "method": "config"}), source_id),
            )
            passed += 1
            logger.info("Topic pass (config): %s [%s]", title, domain)
            continue

        # Mixed sources: call CLI
        try:
            result = call_haiku(title, content or "", conn)
        except Exception as e:
            logger.error("CLI call failed for source %d: %s", source_id, e)
            failed += 1
            conn.execute("UPDATE sources SET status = 'topic_fail' WHERE id = ?", (source_id,))
            continue

        result_domain = result.get("domain", "irrelevant")
        confidence = result.get("confidence", 0.0)

        if result_domain in ("ai", "macro") and confidence >= confidence_threshold:
            conn.execute(
                "UPDATE sources SET status = 'topic_pass', domain = ?, filter_a_result = ? WHERE id = ?",
                (result_domain, json.dumps(result), source_id),
            )
            passed += 1
            logger.info("Topic pass (CLI): %s [%s, %.2f]", title, result_domain, confidence)
        else:
            conn.execute(
                "UPDATE sources SET status = 'topic_fail', filter_a_result = ? WHERE id = ?",
                (json.dumps(result), source_id),
            )
            failed += 1
            logger.info("Topic fail: %s [%s, %.2f]", title, result_domain, confidence)

    conn.commit()
    return passed, failed
