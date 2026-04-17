import logging
import re
import sqlite3

import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

URL_PATTERN = re.compile(r'https?://[^\s<>"]+')
FETCH_TIMEOUT = 15
USER_AGENT = "Mozilla/5.0 (compatible; llm-wiki/1.0)"
# fxtwitter serves OG metadata only to bot-like User-Agents
BOT_USER_AGENT = "TelegramBot (like TwitterBot)"
SOCIAL_DOMAINS = ("fxtwitter.com", "x.com", "twitter.com")


def _convert_x_url(url):
    """Convert X/Twitter URLs to fxtwitter for content extraction."""
    url = url.replace("twitter.com", "fxtwitter.com")
    url = url.replace("x.com", "fxtwitter.com")
    return url


def _extract_url(text):
    """Extract first URL from text."""
    match = URL_PATTERN.search(text)
    return match.group(0) if match else None


def _fetch_url_content(url):
    """Fetch URL and extract title + readable text.

    Uses bot UA for social media sites (fxtwitter needs it for OG metadata).

    Returns (title, text) tuple. Both empty strings on failure.
    """
    ua = BOT_USER_AGENT if any(d in url for d in SOCIAL_DOMAINS) else USER_AGENT
    try:
        resp = requests.get(
            url, timeout=FETCH_TIMEOUT,
            headers={"User-Agent": ua},
            allow_redirects=True,
        )
        resp.raise_for_status()
    except Exception as e:
        logger.warning("Fetch failed for %s: %s", url, e)
        return "", ""

    try:
        soup = BeautifulSoup(resp.text, "html.parser")

        # Title: og:title > <title> > first h1
        title = ""
        og_title = soup.find("meta", property="og:title")
        if og_title and og_title.get("content"):
            title = og_title["content"].strip()
        elif soup.title and soup.title.string:
            title = soup.title.string.strip()
        elif soup.find("h1"):
            title = soup.find("h1").get_text(strip=True)

        # Content: og:description + main text
        parts = []
        og_desc = soup.find("meta", property="og:description")
        if og_desc and og_desc.get("content"):
            parts.append(og_desc["content"].strip())

        # Strip scripts/styles then get body text
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()
        body_text = soup.get_text(separator=" ", strip=True)
        if body_text:
            parts.append(body_text[:3000])

        return title[:300], "\n\n".join(parts)[:4000]
    except Exception as e:
        logger.warning("Parse failed for %s: %s", url, e)
        return "", ""


def process_input(conn, text):
    """Process manual input (URL or text).

    Returns source_id if inserted, None if duplicate.
    """
    url = _extract_url(text)

    if url:
        # URL-based input — fetch actual content for filtering
        fetch_url = url
        # For X URLs, fxtwitter returns cleaner OG metadata
        if "x.com" in url or "twitter.com" in url:
            fetch_url = _convert_x_url(url)

        fetched_title, fetched_text = _fetch_url_content(fetch_url)

        # Title priority: user text (if more than just URL) > fetched > URL tail
        user_text = text.replace(url, "").strip()
        if user_text:
            title = user_text[:200]
        elif fetched_title:
            title = fetched_title[:200]
        else:
            title = (url.split("/")[-1] or url)[:200]

        # Content: combine user note + fetched body
        content_parts = []
        if user_text:
            content_parts.append(f"[사용자 메모] {user_text}")
        if fetched_title:
            content_parts.append(f"[제목] {fetched_title}")
        if fetched_text:
            content_parts.append(fetched_text)
        if not content_parts:
            content_parts.append(url)
        content = "\n\n".join(content_parts)

        try:
            cursor = conn.execute(
                """INSERT INTO sources
                   (source_type, feed_name, title, url, content, status)
                   VALUES ('manual', 'manual', ?, ?, ?, 'collected')""",
                (title, url, content),
            )
            conn.commit()
            logger.info("Manual input (URL): %s [fetched=%s]", url, bool(fetched_text))
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            logger.info("Duplicate URL: %s", url)
            return None
    else:
        # Text-only input
        title = text[:100]
        try:
            cursor = conn.execute(
                """INSERT INTO sources
                   (source_type, feed_name, title, content, status)
                   VALUES ('manual', 'manual', ?, ?, 'collected')""",
                (title, text),
            )
            conn.commit()
            logger.info("Manual input (text): %s", title[:50])
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            return None


def run_pipeline_for_source(conn, source_id):
    """Run filter → ingest → sync for a single source.

    Used by bot.py for immediate processing.
    """
    from filter.topic import filter_topic
    from filter.quality import filter_quality
    from wiki.ingest import ingest
    from wiki.indexer import update_index
    from sync import sync_vault

    filter_topic(conn)
    filter_quality(conn)
    ingest(conn)
    update_index(conn)
    sync_vault()
