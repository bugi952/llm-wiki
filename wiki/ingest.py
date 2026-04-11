"""Ingest sources into the wiki using the router + mechanical update pattern."""

import logging
import re
from datetime import date
from email.utils import parsedate_to_datetime

from wiki.router import route_source
from wiki.pages import (
    page_exists, create_page, append_timeline_entry, append_to_weekly,
    update_indicator_row, update_cross_references, increment_source_count,
    record_update,
)

logger = logging.getLogger(__name__)


def _parse_date(published_at):
    """Extract YYYY-MM-DD from various date formats."""
    if not published_at:
        return date.today().isoformat()
    if re.match(r"\d{4}-\d{2}-\d{2}", published_at):
        return published_at[:10]
    try:
        dt = parsedate_to_datetime(published_at)
        return dt.strftime("%Y-%m-%d")
    except Exception:
        return date.today().isoformat()


def _make_slug(title):
    """Convert title to URL-friendly slug."""
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"[\s]+", "-", slug).strip("-")
    slug = re.sub(r"-+", "-", slug)
    return slug[:60] or "untitled"


def _page_slug(title, page_type, domain):
    """Generate a wiki page slug from title, type, and domain."""
    subdir = {
        "entity": "entities",
        "concept": "concepts",
        "indicator": "indicators",
        "weekly": "weekly",
    }.get(page_type, "entities")
    safe_title = re.sub(r"[/\\:*?\"<>|]", "", title)
    return f"{domain}/{subdir}/{safe_title}"


def _week_slug(domain):
    """Get current week's digest slug."""
    today = date.today()
    week_num = today.isocalendar()[1]
    year = today.isocalendar()[0]
    return f"{domain}/weekly/{year}-W{week_num:02d}"


def _ensure_page(conn, title, page_type, domain):
    """Ensure a wiki page exists, create if not."""
    slug = _page_slug(title, page_type, domain)
    if not page_exists(conn, slug):
        create_page(conn, slug, title, page_type, domain)
    return slug


def ingest(conn, vault_dir="vault"):
    """Ingest quality_pass sources into the wiki.

    For each source:
    1. Route: determine target pages (1 LLM call)
    2. Mechanical updates: append facts to pages (0 LLM calls)
    3. Create new pages if needed (0 LLM calls, template-based)
    4. Add to weekly digest (0 LLM calls)

    Returns number of sources ingested.
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

        source = {
            "id": source_id,
            "source_type": source_type,
            "feed_name": feed_name,
            "domain": domain,
            "title": title,
            "url": url,
            "content": content,
            "published_at": date_str,
            "importance": importance,
        }

        # Step 1: Route (1 LLM call)
        try:
            routing = route_source(source, conn)
        except Exception as e:
            logger.error("Route failed for source %d: %s", source_id, e)
            continue

        # Step 2: Create new pages if needed (template-based, 0 LLM calls)
        for new_page in routing.get("new_pages", []):
            ptype = new_page.get("type", "entity")
            _ensure_page(conn, new_page["title"], ptype, domain)

        # Step 3: Mechanical updates - append facts to timeline (0 LLM calls)
        updated_slugs = set()
        for fact in routing.get("facts", []):
            page_title = fact["page"]
            # Try to find this page in entities or concepts
            for ptype in ["entity", "concept", "indicator"]:
                slug = _page_slug(page_title, ptype, domain)
                if page_exists(conn, slug):
                    success = append_timeline_entry(
                        slug, fact.get("date", date_str),
                        fact["entry"], url
                    )
                    if success:
                        increment_source_count(conn, slug)
                        record_update(conn, slug, source_id, "append")
                        updated_slugs.add(slug)
                    break
            else:
                # Page doesn't exist yet - create as entity by default
                slug = _ensure_page(conn, page_title, "entity", domain)
                append_timeline_entry(slug, fact.get("date", date_str), fact["entry"], url)
                increment_source_count(conn, slug)
                record_update(conn, slug, source_id, "create")
                updated_slugs.add(slug)

        # Step 4: Update cross-references (0 LLM calls)
        all_mentioned = routing.get("entities", []) + routing.get("concepts", [])
        for slug in updated_slugs:
            related = [p for p in all_mentioned if _page_slug(p, "entity", domain) != slug
                       and _page_slug(p, "concept", domain) != slug]
            if related:
                update_cross_references(slug, related[:5])

        # Step 5: Add to weekly digest (0 LLM calls)
        week_slug = _week_slug(domain)
        if not page_exists(conn, week_slug):
            today = date.today()
            week_label = f"{today.isocalendar()[0]}-W{today.isocalendar()[1]:02d}"
            create_page(conn, week_slug, week_label, "weekly", domain)
        append_to_weekly(week_slug, title, routing.get("summary_ko", ""), url)

        # Mark as ingested
        conn.execute(
            "UPDATE sources SET status = 'ingested' WHERE id = ?", (source_id,)
        )
        conn.commit()
        count += 1
        pages_str = ", ".join(updated_slugs) if updated_slugs else "(no pages)"
        logger.info("Ingested source %d: %s -> %s", source_id, title, pages_str)

    return count
