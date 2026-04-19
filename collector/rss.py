import logging
import sqlite3
import time

import feedparser

logger = logging.getLogger(__name__)

# Domain mapping for known feed types (CLI skip per design)
DOMAIN_BY_TYPE = {
    "arxiv": "ai",
    "blog": "ai",       # Anthropic/OpenAI/DeepMind blogs
    "newsletter": "ai",  # Import AI
    "central_bank": "macro",
}

# Fallback URLs for RSSHub feeds (per 01_pipeline-architecture.md)
FALLBACK_URLS = {
    "anthropic-blog": "https://raw.githubusercontent.com/taobojlen/anthropic-rss-feed/main/anthropic_news_rss.xml",
    "openai-blog": "https://raw.githubusercontent.com/capjamesg/openai-blog-rss/main/feed.xml",
    # arXiv RSS is empty on weekends; Atom API always works
    "arxiv-cs-ai-cl-lg": "https://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.CL+OR+cat:cs.LG&start=0&max_results=50&sortBy=submittedDate&sortOrder=descending",
}


def _fetch_feed(name, url):
    """Fetch and parse a feed. Falls back to community RSS if RSSHub fails."""
    parsed = feedparser.parse(url)

    # Check if feed failed and fallback exists
    is_failed = (parsed.get("bozo") and not parsed.get("entries")) or len(parsed.get("entries", [])) == 0
    if is_failed and name in FALLBACK_URLS:
        fallback_url = FALLBACK_URLS[name]
        logger.warning("Feed %s failed, trying fallback: %s", name, fallback_url)
        parsed = feedparser.parse(fallback_url)
        if parsed.get("bozo") and not parsed.get("entries"):
            logger.warning("Fallback also failed for %s", name)
            return None
        logger.info("Fallback succeeded for %s (%d entries)", name, len(parsed.get("entries", [])))
        return parsed

    if is_failed:
        logger.warning("Bad feed %s: %s", name, parsed.get("bozo_exception", "no entries"))
        return None

    return parsed


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

        parsed = _fetch_feed(name, url)
        if not parsed:
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
                pass

        conn.commit()
        logger.info("Feed %s: %d entries processed", name, len(parsed.get("entries", [])))

    return total_new
