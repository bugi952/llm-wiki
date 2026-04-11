import logging
import sqlite3
import time

import feedparser

logger = logging.getLogger(__name__)

# Domain mapping for known feed types (LLM skip per design)
DOMAIN_BY_TYPE = {
    "arxiv": "ai",
    "blog": "ai",       # Anthropic/OpenAI/DeepMind blogs
    "newsletter": "ai",  # Import AI
    "central_bank": "macro",
}


def collect_rss(conn, feeds, delay=3):
    """Collect RSS feeds and insert new entries into DB.

    Returns number of new entries inserted.
    """
    total_new = 0

    for i, feed_cfg in enumerate(feeds):
        if i > 0:
            time.sleep(delay)

        name = feed_cfg["name"]
        url = feed_cfg["url"]
        feed_type = feed_cfg.get("type", "blog")

        logger.info("Fetching feed: %s (%s)", name, url)

        parsed = feedparser.parse(url)
        if parsed.get("bozo") and not parsed.get("entries"):
            logger.warning("Bad feed %s: %s", name, parsed.get("bozo_exception"))
            continue

        domain = DOMAIN_BY_TYPE.get(feed_type)

        for entry in parsed.get("entries", []):
            entry_url = entry.get("link") or entry.get("id")
            if not entry_url:
                continue

            title = entry.get("title", "")
            content = entry.get("summary", "") or entry.get("description", "")
            published = entry.get("published")

            try:
                conn.execute(
                    """INSERT INTO sources
                       (source_type, feed_name, domain, title, url, content, published_at, status)
                       VALUES (?, ?, ?, ?, ?, ?, ?, 'collected')""",
                    ("rss", name, domain, title, entry_url, content, published),
                )
                total_new += 1
            except sqlite3.IntegrityError:
                # Duplicate URL, skip
                pass

        conn.commit()
        logger.info("Feed %s: %d entries processed", name, len(parsed.get("entries", [])))

    return total_new
