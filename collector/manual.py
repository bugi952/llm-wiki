import logging
import re
import sqlite3

logger = logging.getLogger(__name__)

URL_PATTERN = re.compile(r'https?://[^\s<>"]+')


def _convert_x_url(url):
    """Convert X/Twitter URLs to fxtwitter for content extraction."""
    url = url.replace("twitter.com", "fxtwitter.com")
    url = url.replace("x.com", "fxtwitter.com")
    return url


def _extract_url(text):
    """Extract first URL from text."""
    match = URL_PATTERN.search(text)
    return match.group(0) if match else None


def process_input(conn, text):
    """Process manual input (URL or text).

    Returns source_id if inserted, None if duplicate.
    """
    url = _extract_url(text)

    if url:
        # URL-based input
        title = text if text != url else url.split("/")[-1] or url
        content = text

        # For X URLs, fetch via fxtwitter
        if "x.com" in url or "twitter.com" in url:
            fx_url = _convert_x_url(url)
            content = f"원본: {url}\nfxtwitter: {fx_url}\n{text}"

        try:
            cursor = conn.execute(
                """INSERT INTO sources
                   (source_type, feed_name, title, url, content, status)
                   VALUES ('manual', 'manual', ?, ?, ?, 'collected')""",
                (title[:200], url, content),
            )
            conn.commit()
            logger.info("Manual input (URL): %s", url)
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
