import logging
import sqlite3

import requests
import yaml

from config import get_config

logger = logging.getLogger(__name__)

HN_API = "https://hacker-news.firebaseio.com/v0"


def _load_ai_keywords():
    """Load AI keywords from filter_rules.yaml."""
    try:
        with open("config/filter_rules.yaml") as f:
            rules = yaml.safe_load(f)
        keywords = []
        for level in rules.get("ai_keywords", {}).values():
            keywords.extend([k.lower() for k in level])
        return keywords
    except Exception:
        return ["llm", "gpt", "claude", "anthropic", "openai", "ai", "transformer"]


def _title_matches_keywords(title, keywords):
    """Check if title contains any AI keyword."""
    title_lower = title.lower()
    return any(kw in title_lower for kw in keywords)


def collect_hackernews(conn):
    """Collect AI-related stories from Hacker News.

    Returns number of new entries inserted.
    """
    cfg = get_config()
    min_score = cfg["hackernews"]["min_score"]
    top_n = cfg["hackernews"]["top_n"]

    keywords = _load_ai_keywords()

    # Fetch top story IDs
    resp = requests.get(f"{HN_API}/topstories.json", timeout=15)
    resp.raise_for_status()
    story_ids = resp.json()[:top_n]

    total_new = 0

    for story_id in story_ids:
        try:
            resp = requests.get(f"{HN_API}/item/{story_id}.json", timeout=10)
            resp.raise_for_status()
            item = resp.json()
        except Exception as e:
            logger.warning("Failed to fetch HN item %d: %s", story_id, e)
            continue

        if not item or item.get("type") != "story":
            continue

        title = item.get("title", "")
        score = item.get("score", 0)
        story_url = item.get("url", "")

        # Score filter
        if score < min_score:
            continue

        # Keyword filter
        if not _title_matches_keywords(title, keywords):
            continue

        hn_url = f"https://news.ycombinator.com/item?id={story_id}"

        try:
            conn.execute(
                """INSERT INTO sources
                   (source_type, feed_name, title, url, story_url, content, status)
                   VALUES ('hackernews', 'hackernews', ?, ?, ?, ?, 'collected')""",
                (title, hn_url, story_url or hn_url, f"HN score: {score}"),
            )
            total_new += 1
        except sqlite3.IntegrityError:
            pass

    conn.commit()
    logger.info("HN: %d new AI stories (from top %d, min score %d)", total_new, top_n, min_score)
    return total_new
