"""Generate daily digest pages per domain.

Collects today's ingested facts, groups by page, then calls LLM once
per domain for a 3-line summary at the top.
"""

import json
import logging
import os
from datetime import datetime, timezone

from llm import claude_call

logger = logging.getLogger(__name__)

VAULT_DIR = "vault"
DOMAINS = ["ai", "crypto", "macro"]


def _get_today_facts(conn, domain):
    """Get all sources ingested today (UTC) for a domain."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    cursor = conn.execute(
        """SELECT title, url, importance, filter_b_result
           FROM sources
           WHERE status = 'ingested' AND domain = ?
           AND date(collected_at) = ?
           ORDER BY importance DESC, id DESC""",
        (domain, today),
    )
    results = []
    for title, url, importance, fb_raw in cursor:
        fb = {}
        if fb_raw:
            try:
                fb = json.loads(fb_raw)
            except (json.JSONDecodeError, TypeError):
                pass
        results.append({
            "title": title,
            "url": url,
            "importance": importance or "background",
            "summary_ko": fb.get("summary_ko", ""),
            "facts": fb.get("facts", []),
            "entities": fb.get("entities", []),
        })
    return results


def _build_digest_body(items):
    """Build markdown body from today's ingested items, grouped by entity."""
    if not items:
        return ""

    # Group by first entity (or "기타")
    by_entity = {}
    for item in items:
        key = item["entities"][0] if item["entities"] else "기타"
        by_entity.setdefault(key, []).append(item)

    lines = []
    for entity, entity_items in sorted(by_entity.items()):
        lines.append(f"### {entity}")
        for item in entity_items:
            tag = f"[{item['importance']}]" if item["importance"] != "background" else ""
            summary = item["summary_ko"] or item["title"]
            url_link = f" [(원문)]({item['url']})" if item["url"] else ""
            lines.append(f"- {tag} {summary}{url_link}")
        lines.append("")

    return "\n".join(lines)


def _generate_summary(domain, items, conn):
    """Call LLM to generate 3-line summary of today's digest."""
    if not items:
        return "오늘 새로운 소식 없음."

    # Build context for LLM (compact)
    source_lines = []
    for item in items[:20]:  # Cap at 20 items for prompt size
        tag = item["importance"]
        source_lines.append(f"[{tag}] {item['title']}")
    sources_text = "\n".join(source_lines)

    domain_label = {"ai": "AI", "crypto": "Crypto", "macro": "매크로/경제"}[domain]

    prompt = f"""오늘의 {domain_label} 뉴스 요약. 아래 항목들을 읽고 핵심 3줄로 요약하라.
한국어로 작성. 각 줄은 독립적인 인사이트. 번호 매기지 마.

=== 오늘 항목 ({len(items)}건) ===
{sources_text}
=== 끝 ===

3줄 요약만 출력. 마크다운 서식 없이 평문으로:"""

    try:
        return claude_call(prompt, conn=conn, expect_json=False)
    except Exception as e:
        logger.warning("Daily summary LLM call failed for %s: %s", domain, e)
        return "요약 생성 실패."


def generate_daily_digest(conn):
    """Generate daily digest for each domain. Returns number of digests created."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    created = 0

    for domain in DOMAINS:
        items = _get_today_facts(conn, domain)
        if not items:
            logger.info("Daily digest: no items for %s", domain)
            continue

        # Generate summary
        summary = _generate_summary(domain, items, conn)

        # Build page
        body = _build_digest_body(items)
        domain_label = {"ai": "AI", "crypto": "Crypto", "macro": "Macro"}[domain]

        content = f"""---
type: daily
domain: {domain}
date: {today}
source_count: {len(items)}
---

# {today} {domain_label} Daily

## 핵심 요약
{summary}

## 상세 ({len(items)}건)
{body}"""

        # Write file
        daily_dir = os.path.join(VAULT_DIR, domain, "daily")
        os.makedirs(daily_dir, exist_ok=True)
        path = os.path.join(daily_dir, f"{today}.md")
        with open(path, "w") as f:
            f.write(content)

        logger.info("Daily digest created: %s (%d items)", path, len(items))
        created += 1

    return created
