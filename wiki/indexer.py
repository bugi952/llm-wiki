"""Build wiki index pages and changelog from wiki_pages table."""

import logging
import os
from datetime import datetime

from wiki.pages import list_pages

logger = logging.getLogger(__name__)

VAULT_DIR = "vault"

TYPE_EMOJI = {
    "entity": "🏢",
    "concept": "💡",
    "indicator": "📊",
    "weekly": "📅",
}

TYPE_LABEL = {
    "entity": "엔티티",
    "concept": "개념",
    "indicator": "지표",
    "weekly": "주간",
}


def update_index(conn, vault_dir=VAULT_DIR):
    """Rebuild index.md for each domain and the global index."""
    pages = list_pages(conn)
    if not pages:
        logger.info("No wiki pages to index")
        return

    # Group by domain
    domains = {}
    for p in pages:
        d = p.get("domain", "ai")
        if d not in domains:
            domains[d] = []
        domains[d].append(p)

    # Build per-domain index
    for domain, domain_pages in domains.items():
        _build_domain_index(domain, domain_pages, vault_dir)

    # Build global index
    _build_global_index(domains, vault_dir)

    # Build log
    _build_log(conn, vault_dir)


def _build_domain_index(domain, pages, vault_dir):
    """Build vault/{domain}/index.md"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    parts = [f"# {domain.upper()} Wiki", f"최종 갱신: {now}", ""]

    # Group by type (excluding weekly)
    for ptype in ["entity", "concept", "indicator"]:
        group = [p for p in pages if p["page_type"] == ptype]
        if not group:
            continue
        group.sort(key=lambda p: p["title"])
        emoji = TYPE_EMOJI[ptype]
        label = TYPE_LABEL[ptype]
        parts.append(f"## {emoji} {label}")
        for p in group:
            # Link to page file
            subdir = {"entity": "entities", "concept": "concepts", "indicator": "indicators"}[ptype]
            parts.append(f"- [[{subdir}/{p['title']}|{p['title']}]]")
        parts.append("")

    # Weekly digests
    weeklies = [p for p in pages if p["page_type"] == "weekly"]
    if weeklies:
        weeklies.sort(key=lambda p: p["title"], reverse=True)
        parts.append("## 📅 주간 다이제스트")
        for p in weeklies[:8]:  # Last 8 weeks
            parts.append(f"- [[weekly/{p['title']}|{p['title']}]]")
        parts.append("")

    index_path = os.path.join(vault_dir, domain, "index.md")
    os.makedirs(os.path.dirname(index_path), exist_ok=True)
    with open(index_path, "w") as f:
        f.write("\n".join(parts))
    logger.info("Updated %s/index.md (%d pages)", domain, len(pages))


def _build_global_index(domains, vault_dir):
    """Build vault/index.md with all domains."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    parts = [f"# Wiki Daily", f"최종 갱신: {now}", ""]

    for domain in sorted(domains.keys()):
        pages = domains[domain]
        parts.append(f"## {domain.upper()}")
        parts.append("")

        for ptype in ["entity", "concept", "indicator"]:
            group = [p for p in pages if p["page_type"] == ptype]
            if not group:
                continue
            group.sort(key=lambda p: p["title"])
            emoji = TYPE_EMOJI[ptype]
            label = TYPE_LABEL[ptype]
            parts.append(f"### {emoji} {label}")
            for p in group:
                subdir = {"entity": "entities", "concept": "concepts", "indicator": "indicators"}[ptype]
                parts.append(f"- [[{domain}/{subdir}/{p['title']}|{p['title']}]]")
            parts.append("")

    global_path = os.path.join(vault_dir, "index.md")
    with open(global_path, "w") as f:
        f.write("\n".join(parts))
    logger.info("Updated vault/index.md")


def _build_log(conn, vault_dir):
    """Build vault/log.md from recent page_updates."""
    rows = conn.execute(
        """SELECT pu.created_at, wp.title, wp.page_type, pu.update_type, s.title
           FROM page_updates pu
           JOIN wiki_pages wp ON pu.page_id = wp.id
           LEFT JOIN sources s ON pu.source_id = s.id
           ORDER BY pu.created_at DESC
           LIMIT 100"""
    ).fetchall()

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    parts = [f"# 변경 이력", f"최종 갱신: {now}", ""]

    current_date = None
    for created_at, page_title, page_type, update_type, source_title in rows:
        entry_date = created_at[:10] if created_at else "unknown"
        if entry_date != current_date:
            current_date = entry_date
            parts.append(f"## [{entry_date}]")
            parts.append("")

        source_info = f" ← {source_title}" if source_title else ""
        parts.append(f"- {update_type}: **{page_title}**{source_info}")

    parts.append("")

    log_path = os.path.join(vault_dir, "log.md")
    with open(log_path, "w") as f:
        f.write("\n".join(parts))
