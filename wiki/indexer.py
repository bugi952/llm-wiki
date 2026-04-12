"""Build wiki dashboard, domain indexes, and changelog."""

import logging
import os
import re
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

DOMAIN_EMOJI = {
    "ai": "🤖",
    "macro": "🌍",
    "crypto": "💰",
}

SUBDIR_MAP = {"entity": "entities", "concept": "concepts", "indicator": "indicators"}


def update_index(conn, vault_dir=VAULT_DIR):
    """Rebuild dashboard, domain indexes, and changelog."""
    pages = list_pages(conn)
    if not pages:
        logger.info("No wiki pages to index")
        return

    domains = {}
    for p in pages:
        d = p.get("domain", "ai")
        if d not in domains:
            domains[d] = []
        domains[d].append(p)

    for domain, domain_pages in domains.items():
        _build_domain_index(domain, domain_pages, vault_dir)

    _build_dashboard(conn, domains, vault_dir)
    _build_log(conn, vault_dir)


def _build_domain_index(domain, pages, vault_dir):
    """Build vault/{domain}/index.md"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    parts = [f"# {domain.upper()} Wiki", f"최종 갱신: {now}", ""]

    for ptype in ["entity", "concept", "indicator"]:
        group = [p for p in pages if p["page_type"] == ptype]
        if not group:
            continue
        group.sort(key=lambda p: p["title"])
        parts.append(f"## {TYPE_EMOJI[ptype]} {TYPE_LABEL[ptype]}")
        for p in group:
            parts.append(f"- [[{SUBDIR_MAP[ptype]}/{p['title']}|{p['title']}]]")
        parts.append("")

    weeklies = [p for p in pages if p["page_type"] == "weekly"]
    if weeklies:
        weeklies.sort(key=lambda p: p["title"], reverse=True)
        parts.append("## 📅 주간 다이제스트")
        for p in weeklies[:8]:
            parts.append(f"- [[weekly/{p['title']}|{p['title']}]]")
        parts.append("")

    index_path = os.path.join(vault_dir, domain, "index.md")
    os.makedirs(os.path.dirname(index_path), exist_ok=True)
    with open(index_path, "w") as f:
        f.write("\n".join(parts))
    logger.info("Updated %s/index.md (%d pages)", domain, len(pages))


def _read_indicator_table(vault_dir, slug):
    """Read current values from an indicator page's table."""
    path = os.path.join(vault_dir, f"{slug}.md")
    if not os.path.exists(path):
        return []
    with open(path) as f:
        content = f.read()
    rows = []
    for line in content.split("\n"):
        # Match table rows: | indicator | value | date | trend |
        m = re.match(r"\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|", line)
        if m and m.group(1).strip() not in ("지표", "") and "---" not in m.group(1):
            rows.append({
                "name": m.group(1).strip(),
                "value": m.group(2).strip(),
                "date": m.group(3).strip(),
                "trend": m.group(4).strip(),
            })
    return rows


def _read_recent_entries(vault_dir, slug, limit=3):
    """Read the most recent timeline entries from a page."""
    path = os.path.join(vault_dir, f"{slug}.md")
    if not os.path.exists(path):
        return []
    with open(path) as f:
        content = f.read()
    entries = []
    for line in content.split("\n"):
        m = re.match(r"- \*\*(.+?)\*\*:\s*(.+?)(?:\s*\[|\s*$)", line)
        if m:
            entries.append({"date": m.group(1), "text": m.group(2).strip()})
    # Return most recent N
    return entries[:limit]


def _build_dashboard(conn, domains, vault_dir):
    """Build vault/index.md as a rich dashboard."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    parts = ["# 📡 Wiki Dashboard", f"최종 갱신: {now}", ""]

    # === Prices section (crypto + macro indicators) ===
    crypto_prices = []
    for slug_suffix in ["BTC Price", "ETH Price", "HYPE Price"]:
        rows = _read_indicator_table(vault_dir, f"crypto/indicators/{slug_suffix}")
        for r in rows:
            crypto_prices.append(r)

    macro_prices = []
    for slug_suffix in ["Oil (WTI)", "EUR-USD", "JPY-USD", "CNY-USD"]:
        rows = _read_indicator_table(vault_dir, f"macro/indicators/{slug_suffix}")
        for r in rows:
            macro_prices.append(r)

    us_rates = _read_indicator_table(vault_dir, "macro/indicators/US Interest Rates")

    if crypto_prices or macro_prices or us_rates:
        parts.append("## 💹 시세")
        parts.append("")

        if crypto_prices:
            parts.append("**Crypto**")
            parts.append("")
            parts.append("| 코인 | 가격 | 날짜 |")
            parts.append("|------|------|------|")
            for r in crypto_prices:
                parts.append(f"| {r['name']} | {r['value']} | {r['date']} |")
            parts.append("")

        if us_rates or macro_prices:
            parts.append("**Macro**")
            parts.append("")
            parts.append("| 지표 | 값 | 날짜 |")
            parts.append("|------|-----|------|")
            for r in us_rates:
                parts.append(f"| {r['name']} | {r['value']} | {r['date']} |")
            for r in macro_prices:
                parts.append(f"| {r['name']} | {r['value']} | {r['date']} |")
            parts.append("")

    # === Recent updates section ===
    recent_rows = conn.execute(
        """SELECT pu.created_at, wp.title, wp.slug, wp.domain, pu.update_type, s.title
           FROM page_updates pu
           JOIN wiki_pages wp ON pu.page_id = wp.id
           LEFT JOIN sources s ON pu.source_id = s.id
           ORDER BY pu.created_at DESC
           LIMIT 15"""
    ).fetchall()

    if recent_rows:
        parts.append("## 🔔 최근 업데이트")
        parts.append("")
        seen = set()
        for created_at, page_title, slug, domain, update_type, source_title in recent_rows:
            if page_title in seen:
                continue
            seen.add(page_title)
            date_str = created_at[:10] if created_at else ""
            emoji = DOMAIN_EMOJI.get(domain, "")
            source_info = f" — {source_title}" if source_title else ""
            subdir = SUBDIR_MAP.get(
                conn.execute("SELECT page_type FROM wiki_pages WHERE slug = ?", (slug,)).fetchone()[0],
                "entities"
            )
            parts.append(f"- {emoji} **[[{slug}|{page_title}]]** ({date_str}){source_info}")
        parts.append("")

    # === Recent timeline entries from key entities ===
    key_entities = [
        ("ai", "ai/entities/Anthropic"),
        ("ai", "ai/entities/OpenAI"),
        ("ai", "ai/entities/Google DeepMind"),
        ("crypto", "crypto/entities/Bitcoin"),
        ("crypto", "crypto/entities/Ethereum"),
        ("crypto", "crypto/entities/Hyperliquid"),
    ]

    has_timeline = False
    for domain, slug in key_entities:
        entries = _read_recent_entries(vault_dir, slug, limit=2)
        if entries:
            if not has_timeline:
                parts.append("## 📰 주요 엔티티 최신")
                parts.append("")
                has_timeline = True
            emoji = DOMAIN_EMOJI.get(domain, "")
            title = slug.split("/")[-1]
            parts.append(f"**{emoji} [[{slug}|{title}]]**")
            for e in entries:
                parts.append(f"- ({e['date']}) {e['text']}")
            parts.append("")

    # === Domain overview ===
    parts.append("## 📂 도메인")
    parts.append("")

    for domain in ["ai", "crypto", "macro"]:
        if domain not in domains:
            continue
        pages = domains[domain]
        emoji = DOMAIN_EMOJI.get(domain, "")
        entity_count = sum(1 for p in pages if p["page_type"] == "entity")
        concept_count = sum(1 for p in pages if p["page_type"] == "concept")
        indicator_count = sum(1 for p in pages if p["page_type"] == "indicator")

        counts = []
        if entity_count:
            counts.append(f"{entity_count} 엔티티")
        if concept_count:
            counts.append(f"{concept_count} 개념")
        if indicator_count:
            counts.append(f"{indicator_count} 지표")

        parts.append(f"### {emoji} [[{domain}/index|{domain.upper()}]] ({' · '.join(counts)})")
        parts.append("")

        for ptype in ["entity", "concept", "indicator"]:
            group = [p for p in pages if p["page_type"] == ptype]
            if not group:
                continue
            group.sort(key=lambda p: p["title"])
            links = " · ".join(f"[[{domain}/{SUBDIR_MAP[ptype]}/{p['title']}|{p['title']}]]" for p in group)
            parts.append(f"{TYPE_EMOJI[ptype]} {links}")
        parts.append("")

    global_path = os.path.join(vault_dir, "index.md")
    with open(global_path, "w") as f:
        f.write("\n".join(parts))
    logger.info("Updated vault/index.md (dashboard)")


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
