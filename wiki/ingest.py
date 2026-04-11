import logging
import os
import re
from email.utils import parsedate_to_datetime

from llm import claude_call

logger = logging.getLogger(__name__)


def _make_slug(title):
    """Convert title to URL-friendly slug (ASCII only)."""
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug).strip("-")
    slug = re.sub(r"-+", "-", slug)
    return slug or "untitled"


def _parse_date(published_at):
    """Extract YYYY-MM-DD from various date formats."""
    if not published_at:
        return "unknown"
    # Already ISO format (2026-04-10 or 2026-04-10T...)
    if re.match(r"\d{4}-\d{2}-\d{2}", published_at):
        return published_at[:10]
    # RFC 2822 format (Thu, 02 Apr 2026 12:00:00 GMT)
    try:
        dt = parsedate_to_datetime(published_at)
        return dt.strftime("%Y-%m-%d")
    except Exception:
        pass
    return "unknown"


def call_haiku_ingest(title, content, source_type, feed_name, conn):
    """Call Claude CLI to generate summary. Returns dict with summary + whats_new."""
    prompt = (
        "지식 요약기. 핵심 내용을 간결하게 정리.\n\n"
        f"출처: {source_type} / {feed_name}\n제목: {title}\n내용:\n{content}\n\n"
        'JSON만 출력: {"summary": "3~5줄 요약", "whats_new": "기존 지식 대비 새로운 점"}'
    )
    return claude_call(prompt, conn=conn, expect_json=True)


def ingest(conn, vault_dir="vault"):
    """Generate wiki pages for quality_pass sources.

    Returns number of pages created.
    """
    cursor = conn.execute(
        """SELECT id, source_type, feed_name, domain, title, url, content,
                  published_at, importance
           FROM sources WHERE status = 'quality_pass'"""
    )
    rows = cursor.fetchall()
    count = 0

    for row in rows:
        source_id, source_type, feed_name, domain, title, url, content, published_at, importance = row

        date_str = _parse_date(published_at)
        slug = _make_slug(title)
        filename = f"{date_str}_{slug}.md"
        filepath = os.path.join(vault_dir, domain, filename)

        if os.path.exists(filepath):
            conn.execute("UPDATE sources SET status = 'ingested', vault_path = ? WHERE id = ?",
                         (filepath, source_id))
            conn.commit()
            continue

        try:
            result = call_haiku_ingest(title, content or "", source_type, feed_name, conn)
        except Exception as e:
            logger.error("Ingest failed for source %d: %s", source_id, e)
            continue

        summary = result.get("summary", "")
        whats_new = result.get("whats_new", "")

        # Get score from filter_b_result
        score_row = conn.execute(
            "SELECT filter_b_result FROM sources WHERE id = ?", (source_id,)
        ).fetchone()
        score = ""
        if score_row and score_row[0]:
            try:
                import json
                fb = json.loads(score_row[0])
                score = fb.get("average", "")
            except Exception:
                pass

        page = f"""---
title: {title}
source: {feed_name}
url: {url}
date: {date_str}
domain: {domain}
importance: {importance}
score: {score}
---

## 핵심
{summary}

## 새로운 점
{whats_new}
"""

        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w") as f:
            f.write(page)

        conn.execute(
            "UPDATE sources SET status = 'ingested', vault_path = ? WHERE id = ?",
            (filepath, source_id),
        )
        conn.commit()
        count += 1
        logger.info("Ingested: %s -> %s", title, filepath)

    return count
