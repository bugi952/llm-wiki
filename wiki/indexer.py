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


def update_index(conn, vault_dir="vault"):
    """Incrementally update index.md for each domain.

    Only processes sources with status='ingested' and indexed=false.
    """
    cursor = conn.execute(
        """SELECT id, domain, title, importance, vault_path
           FROM sources WHERE status = 'ingested' AND indexed = 0"""
    )
    new_sources = cursor.fetchall()

    if not new_sources:
        logger.info("No new sources to index")
        return

    # Group by domain
    by_domain = {}
    for source_id, domain, title, importance, vault_path in new_sources:
        by_domain.setdefault(domain, []).append({
            "id": source_id,
            "title": title,
            "importance": importance or "background",
            "vault_path": vault_path,
            "filename": os.path.basename(vault_path) if vault_path else "",
        })

    for domain, sources in by_domain.items():
        index_path = os.path.join(vault_dir, domain, "index.md")

        # Load existing entries from index
        existing_entries = []
        if os.path.exists(index_path):
            with open(index_path) as f:
                existing_content = f.read()
            # Parse existing entries (lines starting with "- [")
            for line in existing_content.split("\n"):
                stripped = line.strip()
                if stripped.startswith("- ["):
                    existing_entries.append(stripped)

        # Build new entries
        new_entries = []
        for src in sources:
            filename = src["filename"]
            entry_line = f"- [{src['title']}]({filename})"
            # Avoid duplicates
            if not any(filename in e for e in existing_entries):
                new_entries.append({
                    "line": entry_line,
                    "importance": src["importance"],
                    "filename": filename,
                })

        # Merge all entries
        all_entries = []
        for line in existing_entries:
            # Try to determine importance from existing content
            imp = "background"
            all_entries.append({"line": line, "importance": imp, "existing": True})
        all_entries.extend(new_entries)

        # Separate by importance
        urgent = []
        other = []
        for entry in all_entries:
            if entry.get("importance") == "urgent":
                urgent.append(entry["line"])
            else:
                other.append(entry["line"])

        # Also add existing entries that were under ## 긴급
        if os.path.exists(index_path):
            with open(index_path) as f:
                lines = f.readlines()
            in_urgent = False
            for line in lines:
                stripped = line.strip()
                if stripped == "## 긴급":
                    in_urgent = True
                    continue
                elif stripped.startswith("## "):
                    in_urgent = False
                    continue
                if in_urgent and stripped.startswith("- ["):
                    if stripped not in urgent:
                        urgent.append(stripped)
                        # Remove from other if present
                        other = [e for e in other if e != stripped]

        # For new urgent entries, move from other to urgent
        for entry in new_entries:
            if entry["importance"] == "urgent" and entry["line"] in other:
                other.remove(entry["line"])

        # Build index content
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        parts = [f"# {domain.upper()} 인덱스", f"최종 갱신: {now}", ""]

        if urgent:
            parts.append("## 긴급")
            parts.extend(urgent)
            parts.append("")

        if other:
            parts.append("## 주제별")
            parts.extend(other)
            parts.append("")

        index_content = "\n".join(parts)

        with open(index_path, "w") as f:
            f.write(index_content)

        # Mark as indexed
        for src in sources:
            conn.execute("UPDATE sources SET indexed = 1 WHERE id = ?", (src["id"],))

        conn.commit()
        logger.info("Updated %s/index.md (+%d entries)", domain, len(new_entries))
