"""One-time migration: convert old per-source pages into new wiki structure.

Reads existing vault/ai/*.md and vault/macro/*.md files,
groups by entity/concept, and creates persistent wiki pages.
"""

import json
import logging
import os
import re
import sqlite3
from datetime import datetime

from db import get_db, init_db
from wiki.pages import create_page, append_timeline_entry, update_indicator_row, page_exists
from wiki.indexer import update_index

logger = logging.getLogger(__name__)

# Map feed_name to entity
FEED_TO_ENTITY = {
    "anthropic-blog": "Anthropic",
    "deepmind-blog": "Google DeepMind",
    "openai-blog": "OpenAI",
    "meta-ai-blog": "Meta AI",
    "importai": "Import AI (Newsletter)",
    "arxiv-cs-ai": "arXiv",
    "arxiv-cs-cl": "arXiv",
    "arxiv-cs-lg": "arXiv",
}

# Seed concept pages for AI domain
AI_CONCEPTS = [
    "AI Safety",
    "Scaling Laws",
    "Open Source Models",
    "AI Infrastructure",
    "Agentic AI",
    "AGI",
    "Multimodal AI",
    "AI Regulation",
]

# Seed indicator pages for macro domain
MACRO_INDICATORS = {
    "US Interest Rates": ["연방기금금리", "10년 국채금리", "10Y-2Y 스프레드"],
    "US Inflation": ["미국 CPI"],
    "US Employment": ["미국 실업률"],
    "Korea Interest Rates": ["기준금리"],
    "Korea Inflation": ["소비자물가지수"],
}


def _parse_old_frontmatter(filepath):
    """Parse frontmatter from old-style vault files."""
    fields = {}
    try:
        with open(filepath) as f:
            lines = f.readlines()
    except FileNotFoundError:
        return fields, ""

    if not lines or lines[0].strip() != "---":
        return fields, "".join(lines)

    body_start = 1
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == "---":
            body_start = i + 1
            break
        if ":" in line:
            key, val = line.split(":", 1)
            fields[key.strip()] = val.strip()

    body = "".join(lines[body_start:])
    return fields, body


def _extract_summary(body):
    """Extract the summary from ## 핵심 section."""
    match = re.search(r"## 핵심\s*\n(.+?)(?=\n## |\Z)", body, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""


def migrate(conn, vault_dir="vault"):
    """Run the full migration."""
    init_db(conn)
    stats = {"entities": 0, "concepts": 0, "indicators": 0, "entries": 0}

    # Step 1: Create seed entity pages from existing sources
    logger.info("=== Step 1: Creating entity pages ===")
    entity_entries = {}  # entity_name -> list of (date, entry, url)

    # Scan existing AI files
    ai_dir = os.path.join(vault_dir, "ai")
    if os.path.isdir(ai_dir):
        for fname in sorted(os.listdir(ai_dir)):
            if fname == "index.md" or not fname.endswith(".md"):
                continue
            filepath = os.path.join(ai_dir, fname)
            fm, body = _parse_old_frontmatter(filepath)

            feed = fm.get("source", "")
            entity_name = FEED_TO_ENTITY.get(feed)
            if not entity_name:
                continue

            title = fm.get("title", fname)
            date_str = fm.get("date", "unknown")
            url = fm.get("url", "")
            summary = _extract_summary(body)
            entry = summary[:100] if summary else title

            if entity_name not in entity_entries:
                entity_entries[entity_name] = []
            entity_entries[entity_name].append((date_str, entry, url, title))

    # Create entity pages and populate timelines
    for entity_name, entries in entity_entries.items():
        slug = f"ai/entities/{entity_name}"
        if not page_exists(conn, slug):
            create_page(conn, slug, entity_name, "entity", "ai")
            stats["entities"] += 1

        entries.sort(key=lambda x: x[0], reverse=True)
        for date_str, entry, url, title in entries:
            if append_timeline_entry(slug, date_str, entry, url):
                stats["entries"] += 1

    logger.info("Created %d entity pages with %d entries", stats["entities"], stats["entries"])

    # Step 2: Create seed concept pages
    logger.info("=== Step 2: Creating concept pages ===")
    for concept in AI_CONCEPTS:
        slug = f"ai/concepts/{concept}"
        if not page_exists(conn, slug):
            create_page(conn, slug, concept, "concept", "ai")
            stats["concepts"] += 1

    logger.info("Created %d concept pages", stats["concepts"])

    # Step 3: Migrate macro data to indicator pages
    logger.info("=== Step 3: Creating indicator pages ===")

    # Create indicator pages
    for indicator_name in MACRO_INDICATORS:
        slug = f"macro/indicators/{indicator_name}"
        if not page_exists(conn, slug):
            create_page(conn, slug, indicator_name, "indicator", "macro")
            stats["indicators"] += 1

    # Populate from DB sources
    macro_rows = conn.execute(
        """SELECT title, content, published_at FROM sources
           WHERE domain = 'macro' AND status = 'ingested'"""
    ).fetchall()

    for title, content, published_at in macro_rows:
        date_str = published_at[:10] if published_at else "unknown"
        # Match title to indicator page
        for indicator_name, keywords in MACRO_INDICATORS.items():
            for kw in keywords:
                if kw in title:
                    slug = f"macro/indicators/{indicator_name}"
                    # Extract value from title (e.g., "미국 CPI: 330.3 (2026-03-01)")
                    val_match = re.search(r":\s*([\d.]+)", title)
                    value = val_match.group(1) if val_match else ""
                    if value:
                        update_indicator_row(slug, kw, value, date_str)
                    break

    logger.info("Created %d indicator pages", stats["indicators"])

    # Step 4: Update index
    logger.info("=== Step 4: Building index ===")
    update_index(conn, vault_dir)

    # Step 5: Archive old files
    logger.info("=== Step 5: Archiving old files ===")
    archive_dir = os.path.join(vault_dir, "archive")
    os.makedirs(archive_dir, exist_ok=True)

    for domain_dir_name in ["ai", "macro"]:
        domain_dir = os.path.join(vault_dir, domain_dir_name)
        if not os.path.isdir(domain_dir):
            continue
        for fname in os.listdir(domain_dir):
            if fname == "index.md" or not fname.endswith(".md"):
                continue
            # Old-style files have date prefix like 2026-04-06_...
            if re.match(r"\d{4}-\d{2}-\d{2}_", fname) or fname.startswith("unknown_"):
                src = os.path.join(domain_dir, fname)
                dst = os.path.join(archive_dir, f"{domain_dir_name}_{fname}")
                os.rename(src, dst)

    logger.info("Old files moved to vault/archive/")

    logger.info("=== Migration complete ===")
    logger.info("Entities: %d, Concepts: %d, Indicators: %d, Timeline entries: %d",
                stats["entities"], stats["concepts"], stats["indicators"], stats["entries"])
    return stats


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(name)s %(levelname)s %(message)s")
    conn = get_db()
    migrate(conn)
