"""Generate dashboard data.js from vault markdown + DB."""

import json
import logging
import os
import re
from collections import defaultdict
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

VAULT_DIR = "vault"
DOMAINS = ["ai", "macro", "crypto"]
SUBDIR_MAP = {"entity": "entities", "concept": "concepts", "indicator": "indicators"}


def _utcnow():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")


def _read_frontmatter(path):
    """Read YAML frontmatter from a markdown file."""
    with open(path) as f:
        content = f.read()
    if not content.startswith("---"):
        return {}, content
    end = content.find("---", 3)
    if end < 0:
        return {}, content
    fm = {}
    for line in content[3:end].strip().split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, content[end + 3:].strip()


def _extract_facts(content, limit=7):
    """Extract dated facts from markdown content."""
    facts = []
    for line in content.split("\n"):
        m = re.match(r"- \*\*(\d{4}-\d{2}-\d{2})\*\*:\s*(.+?)(?:\s*\[\(원문\)\]|\s*\[원문\]|\s*\[|\s*$)", line)
        if m:
            text = m.group(2).strip()
            # Extract URL if present
            url_m = re.search(r'\[(?:\(원문\)|원문)\]\((.+?)\)', line)
            url = url_m.group(1) if url_m else ""
            facts.append({"date": m.group(1), "text": text, "url": url})
    return facts[:limit]


def _extract_indicator_table(content):
    """Extract indicator values from markdown table."""
    rows = []
    for line in content.split("\n"):
        m = re.match(r"\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|", line)
        if m and m.group(1).strip() not in ("지표", "코인", "") and "---" not in m.group(1):
            rows.append({
                "k": m.group(1).strip(),
                "v": m.group(2).strip(),
                "date": m.group(3).strip(),
            })
    return rows


def _extract_wikilinks(content):
    """Extract [[wikilink]] targets from content."""
    return re.findall(r'\[\[([^\]|]+?)(?:\|[^\]]+?)?\]\]', content)


def _scan_vault(vault_dir):
    """Scan all vault pages, return structured data."""
    pages = []
    for domain in DOMAINS:
        for subdir_type, subdir_name in SUBDIR_MAP.items():
            dir_path = os.path.join(vault_dir, domain, subdir_name)
            if not os.path.isdir(dir_path):
                continue
            for fname in os.listdir(dir_path):
                if not fname.endswith(".md"):
                    continue
                fpath = os.path.join(dir_path, fname)
                fm, content = _read_frontmatter(fpath)
                title = fname[:-3]
                facts = _extract_facts(content)
                wikilinks = _extract_wikilinks(content)
                indicator_values = []
                if subdir_type == "indicator":
                    indicator_values = _extract_indicator_table(content)

                pages.append({
                    "title": title,
                    "domain": domain,
                    "type": subdir_type,
                    "last_updated": fm.get("last_updated", ""),
                    "facts": facts,
                    "wikilinks": wikilinks,
                    "indicator_values": indicator_values,
                    "slug": f"{domain}/{subdir_name}/{title}",
                })
    return pages


def _build_ticker(pages):
    """Build ticker data from indicator pages."""
    ticker = []
    # Crypto prices
    for p in pages:
        if p["type"] == "indicator" and p["domain"] == "crypto" and p["indicator_values"]:
            for iv in p["indicator_values"]:
                ticker.append({"k": p["title"].replace(" Price", ""), "v": iv["v"]})
    # Macro indicators
    for p in pages:
        if p["type"] == "indicator" and p["domain"] == "macro":
            for iv in p["indicator_values"]:
                ticker.append({"k": iv["k"], "v": iv["v"]})
    return ticker


def _build_domain_data(pages):
    """Build per-domain article list + entity chips + graph."""
    domain_titles = {"ai": "오늘의 AI", "crypto": "오늘의 Crypto", "macro": "오늘의 Macro"}
    data = {}

    for domain in DOMAINS:
        domain_pages = [p for p in pages if p["domain"] == domain]
        entities = [p for p in domain_pages if p["type"] == "entity"]
        concepts = [p for p in domain_pages if p["type"] == "concept"]
        indicators = [p for p in domain_pages if p["type"] == "indicator"]

        # Collect all recent facts with entity attribution
        all_facts = []
        for p in domain_pages:
            for f in p["facts"]:
                all_facts.append({
                    "date": f["date"],
                    "hl": f["text"],
                    "entity": p["title"],
                    "url": f.get("url", ""),
                    "page_type": p["type"],
                    "slug": p["slug"],
                })
        all_facts.sort(key=lambda x: x["date"], reverse=True)

        # Entity chips: sort by fact count
        entity_chips = sorted(
            [(p["title"], len(p["facts"])) for p in entities],
            key=lambda x: x[1], reverse=True,
        )[:10]

        # Graph: build from wikilinks between pages in this domain
        node_set = set()
        link_counts = defaultdict(int)
        for p in domain_pages:
            for wl in p["wikilinks"]:
                # Normalize wikilink target
                target = wl.split("/")[-1] if "/" in wl else wl
                if any(pp["title"] == target and pp["domain"] == domain for pp in pages):
                    node_set.add(p["title"])
                    node_set.add(target)
                    pair = tuple(sorted([p["title"], target]))
                    link_counts[pair] += 1

        # Build graph nodes (limit to top connected)
        node_links = defaultdict(int)
        for (a, b), w in link_counts.items():
            node_links[a] += w
            node_links[b] += w
        top_nodes = sorted(node_links.keys(), key=lambda n: node_links[n], reverse=True)[:15]
        top_set = set(top_nodes)

        nodes = []
        for i, n in enumerate(top_nodes):
            ptype = "ent"
            for p in domain_pages:
                if p["title"] == n:
                    ptype = {"entity": "ent", "concept": "con", "indicator": "ind"}.get(p["type"], "ent")
                    break
            # Simple circular layout
            import math
            angle = 2 * math.pi * i / max(len(top_nodes), 1)
            x = int(180 + 140 * math.cos(angle))
            y = int(130 + 100 * math.sin(angle))
            nodes.append({"id": n, "label": n, "type": ptype, "size": 10 + node_links[n], "x": x, "y": y})

        links = []
        for (a, b), w in link_counts.items():
            if a in top_set and b in top_set:
                links.append([a, b, min(w, 5)])

        data[domain] = {
            "title": domain_titles.get(domain, domain),
            "entity_count": len(entities),
            "concept_count": len(concepts),
            "indicator_count": len(indicators),
            "articles": all_facts[:7],
            "entities": entity_chips,
            "graph": {"nodes": nodes, "links": links},
        }

    return data


def _build_ledger(pages):
    """Build timeline ledger from recent facts across all domains."""
    all_entries = []
    for p in pages:
        for f in p["facts"]:
            all_entries.append({
                "date": f["date"],
                "k": p["domain"],
                "fact": f["text"],
                "entity": p["title"],
                "slug": p["slug"],
            })
    all_entries.sort(key=lambda x: x["date"], reverse=True)

    # Group by day, limit to 3 days
    ledger = []
    current_day = None
    day_count = 0
    for e in all_entries:
        day = e["date"]
        if day != current_day:
            if day_count >= 3:
                break
            day_count += 1
            current_day = day
            day_entries = [x for x in all_entries if x["date"] == day]
            ledger.append({"day": day, "subtotal": f"+{len(day_entries)} facts"})
        ledger.append({
            "k": e["k"],
            "fact": e["fact"],
            "entity": e["entity"],
            "slug": e["slug"],
        })

    return ledger[:50]


def _build_heatmap(conn):
    """Build 140-day heatmap from page_updates table."""
    rows = conn.execute(
        """SELECT date(created_at) as d, COUNT(*) as c
           FROM page_updates
           WHERE created_at >= date('now', '-140 days')
           GROUP BY d ORDER BY d"""
    ).fetchall()
    date_counts = dict(rows)

    heatmap = []
    today = datetime.now(timezone.utc).date()
    for i in range(140):
        from datetime import timedelta
        d = today - timedelta(days=139 - i)
        count = date_counts.get(d.isoformat(), 0)
        # Map count to level 0-5
        if count == 0:
            level = 0
        elif count <= 5:
            level = 1
        elif count <= 15:
            level = 2
        elif count <= 30:
            level = 3
        elif count <= 60:
            level = 4
        else:
            level = 5
        heatmap.append(level)

    return heatmap


def _build_index(pages):
    """Build A-Z index from all pages."""
    index = defaultdict(list)
    for p in pages:
        if p["type"] == "weekly":
            continue
        first = p["title"][0].upper()
        # Korean consonant grouping
        if '\uAC00' <= first <= '\uD7A3':
            # Get Korean initial consonant
            code = ord(first) - 0xAC00
            initial = code // (21 * 28)
            consonants = "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"
            first = consonants[initial] if initial < len(consonants) else first
        index[first].append({
            "n": p["title"],
            "k": p["domain"],
            "kind": {"entity": "엔티티", "concept": "개념", "indicator": "지표"}.get(p["type"], ""),
            "s": p["slug"],
        })
    # Sort items within each letter
    for letter in index:
        index[letter].sort(key=lambda x: x["n"])
    return dict(index)


def _build_backlinks(pages):
    """Build backlink rankings and orphan list."""
    # Count incoming links
    incoming = defaultdict(int)
    all_titles = {p["title"] for p in pages}
    for p in pages:
        for wl in p["wikilinks"]:
            target = wl.split("/")[-1] if "/" in wl else wl
            if target in all_titles and target != p["title"]:
                incoming[target] += 1

    # Rank by backlinks
    ranked = sorted(
        [(t, incoming[t]) for t in incoming],
        key=lambda x: x[1], reverse=True,
    )[:20]
    rank_data = []
    for title, count in ranked:
        p = next((pp for pp in pages if pp["title"] == title), None)
        if p:
            rank_data.append([title, p["domain"], {"entity": "엔티티", "concept": "개념", "indicator": "지표"}.get(p["type"], ""), count, p["slug"]])

    # Orphans: pages with 0 incoming links
    orphans = []
    for p in pages:
        if p["title"] not in incoming and p["type"] != "weekly":
            orphans.append([p["title"], p["domain"]])

    # Stubs: pages with 0 or 1 facts and empty sections
    stubs = []
    for p in pages:
        if len(p["facts"]) <= 1 and p["type"] != "weekly" and p["type"] != "indicator":
            stubs.append([p["title"], p["domain"]])

    return rank_data, orphans[:15], stubs[:15]


def generate_dashboard_data(vault_dir=VAULT_DIR, conn=None, output_path="site/data.js"):
    """Main entry point: scan vault + DB, write data.js."""
    pages = _scan_vault(vault_dir)
    logger.info("Scanned %d vault pages", len(pages))

    ticker = _build_ticker(pages)
    domain_data = _build_domain_data(pages)
    ledger = _build_ledger(pages)
    heatmap = _build_heatmap(conn) if conn else [0] * 140
    index = _build_index(pages)
    backlinks_rank, orphans, stubs = _build_backlinks(pages)

    # Today's update count
    update_count = 0
    if conn:
        row = conn.execute(
            "SELECT COUNT(*) FROM page_updates WHERE date(created_at) = date('now')"
        ).fetchone()
        update_count = row[0] if row else 0

    total_pages = len(pages)
    now = datetime.now(timezone.utc).strftime("%H:%M:%S")

    data = {
        "meta": {
            "total_pages": total_pages,
            "update_count": update_count,
            "last_sync": now,
        },
        "ticker": ticker,
        "domains": domain_data,
        "ledger": ledger,
        "heatmap": heatmap,
        "index": index,
        "backlinks_rank": backlinks_rank,
        "orphans": orphans,
        "stubs": stubs,
    }

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write("// Auto-generated by wiki/dashboard_data.py\n")
        f.write(f"window.WIKI_DATA = {json.dumps(data, ensure_ascii=False, indent=None)};\n")

    logger.info("Generated dashboard data: %s (%d pages, %d ticker items)", output_path, total_pages, len(ticker))
    return data
