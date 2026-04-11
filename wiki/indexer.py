import logging
import os
from datetime import datetime

logger = logging.getLogger(__name__)

IMPORTANCE_ORDER = {"urgent": 0, "insight": 1, "connection": 2, "background": 3}


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

    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            key, val = line.split(":", 1)
            fields[key.strip()] = val.strip()
    return fields


def _build_index_content(domain, entries):
    """Build index.md content from a list of entries sorted by importance."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    parts = [f"# {domain.upper()} 인덱스", f"최종 갱신: {now}", ""]

    urgent = [e for e in entries if e["importance"] == "urgent"]
    other = [e for e in entries if e["importance"] != "urgent"]

    # Sort each group by date descending
    urgent.sort(key=lambda e: e.get("date", ""), reverse=True)
    other.sort(key=lambda e: (IMPORTANCE_ORDER.get(e["importance"], 3), e.get("date", "")),
               reverse=False)
    # Re-sort: importance first, then date descending within same importance
    other.sort(key=lambda e: (IMPORTANCE_ORDER.get(e["importance"], 3), ""), reverse=False)

    if urgent:
        parts.append("## 긴급")
        for e in urgent:
            parts.append(f"- [{e['title']}]({e['filename']})")
        parts.append("")

    if other:
        parts.append("## 주제별")
        for e in other:
            parts.append(f"- [{e['title']}]({e['filename']})")
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

    # Build global vault/index.md
    global_entries = []
    for domain in sorted(all_domain_entries.keys()):
        for e in all_domain_entries[domain]:
            global_entries.append({
                **e,
                "filename": f"{domain}/{e['filename']}",
            })
    if global_entries:
        global_path = os.path.join(vault_dir, "index.md")
        global_content = _build_index_content("전체", global_entries)
        with open(global_path, "w") as f:
            f.write(global_content)
        logger.info("Updated vault/index.md (%d entries)", len(global_entries))

    # Mark as indexed
    for source_id, domain, vault_path in new_sources:
        conn.execute("UPDATE sources SET indexed = 1 WHERE id = ?", (source_id,))
    conn.commit()
