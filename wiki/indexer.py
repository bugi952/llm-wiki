import logging
import os
from datetime import datetime, date, timedelta

from config import get_config

logger = logging.getLogger(__name__)

IMPORTANCE_ORDER = {"urgent": 0, "insight": 1, "connection": 2, "background": 3}
IMPORTANCE_EMOJI = {"urgent": "🔴", "insight": "🟡", "connection": "🔗", "background": "⚪"}
IMPORTANCE_HEADING = {"urgent": "Urgent", "insight": "Insight", "connection": "Connection", "background": "Background"}


def _parse_frontmatter(filepath):
    """Extract frontmatter fields from a markdown file."""
    fields = {}
    try:
        with open(filepath) as f:
            lines = f.readlines()
    except FileNotFoundError:
        return fields

    if not lines or lines[0].strip() != "---":
        return fields

    in_frontmatter = True
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            key, val = line.split(":", 1)
            fields[key.strip()] = val.strip()

    # Extract first sentence of ## 핵심 section as one-line summary
    in_summary = False
    for line in lines:
        if line.strip() == "## 핵심":
            in_summary = True
            continue
        if in_summary and line.startswith("##"):
            break  # Hit next section, no content found
        if in_summary and line.strip():
            fields["one_liner"] = line.strip().split("。")[0].split(". ")[0].rstrip(".")
            break

    return fields


def _classify_by_age(entries):
    """Split entries into active, archive, and expired based on date."""
    cfg = get_config()
    archive_days = cfg["wiki"]["archive_after_days"]
    remove_days = cfg["wiki"]["remove_from_index_after_days"]

    today = date.today()
    archive_cutoff = (today - timedelta(days=archive_days)).isoformat()
    remove_cutoff = (today - timedelta(days=remove_days)).isoformat()

    active = []
    archive = []
    for e in entries:
        entry_date = e.get("date", "")
        if not entry_date or entry_date < remove_cutoff:
            continue  # 90+ days: remove from index (file kept)
        elif entry_date < archive_cutoff:
            archive.append(e)  # 30-90 days: archive section
        else:
            active.append(e)
    return active, archive


def _format_entry(e):
    """Format a single index entry with emoji, score, summary, and source link."""
    emoji = IMPORTANCE_EMOJI.get(e["importance"], "⚪")
    score = e.get("score", "")
    score_str = f" ★{score}" if score else ""
    one_liner = e.get("one_liner", "")
    url = e.get("url", "")
    summary_str = f" — {one_liner}" if one_liner else ""
    source_str = f" [(원문)]({url})" if url else ""
    return f"- {emoji} **[[{e['filename']}|{e['title']}]]**{score_str}{summary_str}{source_str}"


def _build_index_content(domain, entries):
    """Build index.md content with importance grouping and inline summaries."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    parts = [f"# {domain.upper()} Daily", f"최종 갱신: {now}", ""]

    active, archive = _classify_by_age(entries)

    # Group by importance
    for imp in ["urgent", "insight", "connection", "background"]:
        group = [e for e in active if e["importance"] == imp]
        if not group:
            continue
        group.sort(key=lambda e: e.get("date", ""), reverse=True)
        heading = IMPORTANCE_HEADING[imp]
        emoji = IMPORTANCE_EMOJI[imp]
        parts.append(f"### {emoji} {heading}")
        for e in group:
            parts.append(_format_entry(e))
        parts.append("")

    if archive:
        archive.sort(key=lambda e: e.get("date", ""), reverse=True)
        parts.append("### 📦 아카이브")
        for e in archive:
            parts.append(_format_entry(e))
        parts.append("")

    return "\n".join(parts)


def _collect_all_entries(domain, vault_dir):
    """Scan all .md files in vault/{domain}/ and extract entry info from frontmatter."""
    domain_dir = os.path.join(vault_dir, domain)
    entries = []

    if not os.path.isdir(domain_dir):
        return entries

    for fname in os.listdir(domain_dir):
        if fname == "index.md" or not fname.endswith(".md"):
            continue
        filepath = os.path.join(domain_dir, fname)
        fm = _parse_frontmatter(filepath)
        entries.append({
            "title": fm.get("title", fname),
            "importance": fm.get("importance", "background"),
            "date": fm.get("date", ""),
            "score": fm.get("score", ""),
            "url": fm.get("url", ""),
            "one_liner": fm.get("one_liner", ""),
            "filename": fname,
            "domain": domain,
        })

    return entries


def update_index(conn, vault_dir="vault"):
    """Incrementally update index.md for each domain + global index.

    Only processes sources with status='ingested' and indexed=false.
    Rebuilds index from frontmatter to preserve importance.
    """
    cursor = conn.execute(
        """SELECT id, domain, vault_path
           FROM sources WHERE status = 'ingested' AND indexed = 0"""
    )
    new_sources = cursor.fetchall()

    if not new_sources:
        logger.info("No new sources to index")
        return

    # Collect affected domains
    affected_domains = set()
    for source_id, domain, vault_path in new_sources:
        affected_domains.add(domain)

    # Rebuild index for each affected domain from frontmatter
    all_domain_entries = {}
    for domain in affected_domains:
        entries = _collect_all_entries(domain, vault_dir)
        all_domain_entries[domain] = entries

        index_path = os.path.join(vault_dir, domain, "index.md")
        content = _build_index_content(domain, entries)
        with open(index_path, "w") as f:
            f.write(content)
        logger.info("Updated %s/index.md (%d entries)", domain, len(entries))

    # Build global vault/index.md with domain sections
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    global_parts = [f"# Wiki Daily", f"최종 갱신: {now}", ""]

    for domain in sorted(all_domain_entries.keys()):
        domain_entries = all_domain_entries[domain]
        if not domain_entries:
            continue
        # Add domain-relative paths for global index
        adjusted = [{**e, "filename": f"{domain}/{e['filename']}"} for e in domain_entries]
        active, archive = _classify_by_age(adjusted)

        global_parts.append(f"## {domain.upper()}")
        global_parts.append("")
        for imp in ["urgent", "insight", "connection", "background"]:
            group = [e for e in active if e["importance"] == imp]
            if not group:
                continue
            group.sort(key=lambda e: e.get("date", ""), reverse=True)
            heading = IMPORTANCE_HEADING[imp]
            emoji = IMPORTANCE_EMOJI[imp]
            global_parts.append(f"### {emoji} {heading}")
            for e in group:
                global_parts.append(_format_entry(e))
            global_parts.append("")

        if archive:
            archive.sort(key=lambda e: e.get("date", ""), reverse=True)
            global_parts.append("### 📦 아카이브")
            for e in archive:
                global_parts.append(_format_entry(e))
            global_parts.append("")

    if len(global_parts) > 3:
        global_path = os.path.join(vault_dir, "index.md")
        with open(global_path, "w") as f:
            f.write("\n".join(global_parts))
        logger.info("Updated vault/index.md")

    # Mark as indexed
    for source_id, domain, vault_path in new_sources:
        conn.execute("UPDATE sources SET indexed = 1 WHERE id = ?", (source_id,))
    conn.commit()
