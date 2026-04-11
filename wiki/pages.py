"""Wiki page CRUD operations."""

import logging
import os
import re
from datetime import datetime

from wiki.templates import TEMPLATES

logger = logging.getLogger(__name__)

VAULT_DIR = "vault"


def _slug_to_path(slug):
    """Convert page slug to filesystem path. e.g. 'ai/entities/Anthropic' -> 'vault/ai/entities/Anthropic.md'"""
    return os.path.join(VAULT_DIR, f"{slug}.md")


def list_pages(conn, domain=None):
    """Return list of (slug, title, page_type) from wiki_pages table."""
    if domain:
        rows = conn.execute(
            "SELECT slug, title, page_type, domain FROM wiki_pages WHERE domain = ?", (domain,)
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT slug, title, page_type, domain FROM wiki_pages"
        ).fetchall()
    return [{"slug": r[0], "title": r[1], "page_type": r[2], "domain": r[3]} for r in rows]


def page_exists(conn, slug):
    """Check if a wiki page exists in the DB."""
    row = conn.execute("SELECT id FROM wiki_pages WHERE slug = ?", (slug,)).fetchone()
    return row is not None


def read_page(slug):
    """Read a wiki page's content."""
    path = _slug_to_path(slug)
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return f.read()


def create_page(conn, slug, title, page_type, domain, content=None):
    """Create a new wiki page with template or custom content."""
    path = _slug_to_path(slug)
    os.makedirs(os.path.dirname(path), exist_ok=True)

    if content is None:
        template_fn = TEMPLATES.get(page_type)
        if page_type == "weekly":
            content = template_fn(domain, title)
        else:
            content = template_fn(title, domain)

    with open(path, "w") as f:
        f.write(content)

    conn.execute(
        """INSERT OR IGNORE INTO wiki_pages (slug, title, page_type, domain, last_updated)
           VALUES (?, ?, ?, ?, ?)""",
        (slug, title, page_type, domain, datetime.now().isoformat()),
    )
    conn.commit()
    logger.info("Created wiki page: %s (%s)", title, slug)
    return path


def append_timeline_entry(slug, date_str, entry, url=None):
    """Append an entry to the '최근 동향' or '주요 발전' or '이력' section."""
    path = _slug_to_path(slug)
    if not os.path.exists(path):
        return False

    with open(path) as f:
        content = f.read()

    # Find the right section to append to
    for section in ["## 최근 동향", "## 주요 발전", "## 이력"]:
        if section in content:
            link = f" [(원문)]({url})" if url else ""
            new_entry = f"- **{date_str}**: {entry}{link}\n"

            # Check for duplicate (same date + similar entry)
            if f"**{date_str}**" in content and entry[:30] in content:
                return False

            # Insert after section heading
            idx = content.index(section) + len(section)
            # Find end of heading line
            newline_idx = content.index("\n", idx)
            content = content[:newline_idx + 1] + new_entry + content[newline_idx + 1:]

            with open(path, "w") as f:
                f.write(content)

            _update_frontmatter_date(path)
            return True

    return False


def append_to_weekly(slug, source_title, summary, url=None):
    """Append a source entry to a weekly digest."""
    path = _slug_to_path(slug)
    if not os.path.exists(path):
        return False

    with open(path) as f:
        content = f.read()

    link = f" [(원문)]({url})" if url else ""
    new_entry = f"- **{source_title}**{link}\n  {summary}\n\n"

    # Check for duplicate
    if source_title in content:
        return False

    content = content.rstrip() + "\n" + new_entry

    with open(path, "w") as f:
        f.write(content)

    _update_frontmatter_date(path)
    return True


def update_indicator_row(slug, indicator, value, date_str, trend="─"):
    """Add or update a row in an indicator table."""
    path = _slug_to_path(slug)
    if not os.path.exists(path):
        return False

    with open(path) as f:
        content = f.read()

    table_row = f"| {indicator} | {value} | {date_str} | {trend} |"

    # Check if indicator already exists in table
    pattern = rf"\| {re.escape(indicator)} \|.*\|"
    if re.search(pattern, content):
        content = re.sub(pattern, table_row, content)
    else:
        # Append to table (after header row)
        table_end = content.find("|------|-----|------|------|")
        if table_end >= 0:
            insert_at = content.index("\n", table_end) + 1
            content = content[:insert_at] + table_row + "\n" + content[insert_at:]

    # Also append to history section
    history_entry = f"- {date_str}: {indicator} {value}\n"
    if "## 이력" in content and history_entry.strip() not in content:
        idx = content.index("## 이력") + len("## 이력")
        newline_idx = content.index("\n", idx)
        content = content[:newline_idx + 1] + history_entry + content[newline_idx + 1:]

    with open(path, "w") as f:
        f.write(content)

    _update_frontmatter_date(path)
    return True


def update_cross_references(slug, related_pages):
    """Update the '연관 페이지' or '핵심 주체' section with wiki links."""
    path = _slug_to_path(slug)
    if not os.path.exists(path):
        return False

    with open(path) as f:
        content = f.read()

    links = " | ".join(f"[[{p}]]" for p in related_pages)

    for section in ["## 연관 페이지", "## 핵심 주체"]:
        if section in content:
            idx = content.index(section) + len(section)
            next_section = content.find("\n##", idx + 1)
            if next_section < 0:
                next_section = len(content)
            content = content[:idx] + f"\n{links}\n\n" + content[next_section:]
            break

    with open(path, "w") as f:
        f.write(content)
    return True



def increment_source_count(conn, slug):
    """Increment source_count for a wiki page."""
    conn.execute(
        "UPDATE wiki_pages SET source_count = source_count + 1, last_updated = ? WHERE slug = ?",
        (datetime.now().isoformat(), slug),
    )
    conn.commit()


def record_update(conn, slug, source_id, update_type):
    """Record a page update in page_updates table."""
    page_row = conn.execute("SELECT id FROM wiki_pages WHERE slug = ?", (slug,)).fetchone()
    if page_row:
        conn.execute(
            "INSERT INTO page_updates (page_id, source_id, update_type) VALUES (?, ?, ?)",
            (page_row[0], source_id, update_type),
        )
        conn.commit()


def _update_frontmatter_date(path):
    """Update last_updated in frontmatter."""
    with open(path) as f:
        content = f.read()

    now = datetime.now().strftime("%Y-%m-%d")
    content = re.sub(r"last_updated: .+", f"last_updated: {now}", content)

    with open(path, "w") as f:
        f.write(content)
