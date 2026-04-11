import os
from datetime import date, timedelta
from unittest.mock import patch
import pytest
from db import get_db, init_db
from wiki.indexer import update_index, _classify_by_age


@pytest.fixture
def db():
    conn = get_db(":memory:")
    init_db(conn)
    yield conn
    conn.close()


@pytest.fixture
def vault_dir(tmp_path):
    (tmp_path / "ai").mkdir()
    (tmp_path / "macro").mkdir()
    # Create a summary file with frontmatter
    page = """---
title: Scaling Laws v2
source: arxiv-cs-ai-cl-lg
url: https://arxiv.org/abs/2401.00001
date: 2026-04-10
domain: ai
importance: insight
---

## 핵심
Scaling laws show predictable performance.

## 새로운 점
10T parameter scale validation.
"""
    (tmp_path / "ai" / "2026-04-10_scaling-laws-v2.md").write_text(page)
    return str(tmp_path)


def _insert_ingested(db, vault_path, title="Scaling Laws v2", domain="ai",
                     importance="insight", indexed=False):
    db.execute(
        """INSERT INTO sources (source_type, feed_name, domain, title, url, content,
           published_at, status, importance, vault_path, indexed)
           VALUES ('rss', 'arxiv-cs-ai-cl-lg', ?, ?, 'https://arxiv.org/abs/2401.00001',
           'content', '2026-04-10', 'ingested', ?, ?, ?)""",
        (domain, title, importance, vault_path, indexed),
    )
    db.commit()


def test_update_index_creates_index_md(db, vault_dir):
    vault_path = os.path.join(vault_dir, "ai", "2026-04-10_scaling-laws-v2.md")
    _insert_ingested(db, vault_path)
    update_index(db, vault_dir)

    index_path = os.path.join(vault_dir, "ai", "index.md")
    assert os.path.exists(index_path)
    content = open(index_path).read()
    assert "Scaling Laws v2" in content
    assert "2026-04-10_scaling-laws-v2.md" in content


def test_update_index_marks_indexed(db, vault_dir):
    vault_path = os.path.join(vault_dir, "ai", "2026-04-10_scaling-laws-v2.md")
    _insert_ingested(db, vault_path)
    update_index(db, vault_dir)

    cursor = db.execute("SELECT indexed FROM sources LIMIT 1")
    assert cursor.fetchone()[0] == 1


def test_update_index_idempotent(db, vault_dir):
    vault_path = os.path.join(vault_dir, "ai", "2026-04-10_scaling-laws-v2.md")
    _insert_ingested(db, vault_path)
    update_index(db, vault_dir)
    update_index(db, vault_dir)  # second run

    index_path = os.path.join(vault_dir, "ai", "index.md")
    content = open(index_path).read()
    # Should appear only once
    assert content.count("Scaling Laws v2") == 1


def test_update_index_importance_order(db, vault_dir):
    # Create urgent file
    urgent_page = """---
title: GPT-5 Released
source: openai-blog
url: https://openai.com/gpt5
date: 2026-04-11
domain: ai
importance: urgent
---

## 핵심
GPT-5 released.

## 새로운 점
New model.
"""
    (vault_dir_path := os.path.join(vault_dir, "ai"))
    with open(os.path.join(vault_dir_path, "2026-04-11_gpt-5-released.md"), "w") as f:
        f.write(urgent_page)

    # Insert both
    vault_path1 = os.path.join(vault_dir, "ai", "2026-04-10_scaling-laws-v2.md")
    _insert_ingested(db, vault_path1, title="Scaling Laws v2", importance="insight")
    db.execute(
        """INSERT INTO sources (source_type, feed_name, domain, title, url, content,
           published_at, status, importance, vault_path, indexed)
           VALUES ('rss', 'openai-blog', 'ai', 'GPT-5 Released', 'https://openai.com/gpt5',
           'content', '2026-04-11', 'ingested', 'urgent', ?, 0)""",
        (os.path.join(vault_dir, "ai", "2026-04-11_gpt-5-released.md"),),
    )
    db.commit()

    update_index(db, vault_dir)

    index_path = os.path.join(vault_dir, "ai", "index.md")
    content = open(index_path).read()
    # Urgent should appear before insight
    urgent_pos = content.index("GPT-5 Released")
    insight_pos = content.index("Scaling Laws v2")
    assert urgent_pos < insight_pos


def test_update_index_preserves_importance_on_rebuild(db, vault_dir):
    """After first index, adding new entries should preserve existing importance."""
    vault_path1 = os.path.join(vault_dir, "ai", "2026-04-10_scaling-laws-v2.md")
    _insert_ingested(db, vault_path1, title="Scaling Laws v2", importance="insight")
    update_index(db, vault_dir)

    # Add a new urgent file
    urgent_page = """---
title: Claude 6 Released
source: anthropic-blog
url: https://anthropic.com/claude6
date: 2026-04-12
domain: ai
importance: urgent
---

## 핵심
Claude 6 released.

## 새로운 점
Major upgrade.
"""
    with open(os.path.join(vault_dir, "ai", "2026-04-12_claude-6-released.md"), "w") as f:
        f.write(urgent_page)
    db.execute(
        """INSERT INTO sources (source_type, feed_name, domain, title, url, content,
           published_at, status, importance, vault_path, indexed)
           VALUES ('rss', 'anthropic-blog', 'ai', 'Claude 6 Released', 'https://anthropic.com/claude6',
           'content', '2026-04-12', 'ingested', 'urgent', ?, 0)""",
        (os.path.join(vault_dir, "ai", "2026-04-12_claude-6-released.md"),),
    )
    db.commit()

    update_index(db, vault_dir)

    index_path = os.path.join(vault_dir, "ai", "index.md")
    content = open(index_path).read()
    # Scaling Laws should still be in 주제별, not urgent
    assert "## 긴급" in content
    assert "Claude 6 Released" in content
    # insight entry should be under 주제별
    urgent_section = content.split("## 주제별")[0]
    assert "Scaling Laws v2" not in urgent_section


def test_update_index_creates_global_index(db, vault_dir):
    """update_index should also create vault/index.md."""
    vault_path = os.path.join(vault_dir, "ai", "2026-04-10_scaling-laws-v2.md")
    _insert_ingested(db, vault_path)
    update_index(db, vault_dir)

    global_index = os.path.join(vault_dir, "index.md")
    assert os.path.exists(global_index)
    content = open(global_index).read()
    assert "Scaling Laws v2" in content
    assert "ai/" in content  # relative path includes domain


def test_classify_by_age():
    today = date.today()
    entries = [
        {"title": "Fresh", "date": today.isoformat(), "importance": "insight"},
        {"title": "Old 45d", "date": (today - timedelta(days=45)).isoformat(), "importance": "background"},
        {"title": "Ancient 100d", "date": (today - timedelta(days=100)).isoformat(), "importance": "background"},
    ]
    active, archive = _classify_by_age(entries)
    assert len(active) == 1
    assert active[0]["title"] == "Fresh"
    assert len(archive) == 1
    assert archive[0]["title"] == "Old 45d"
    # Ancient (100d) should be removed entirely
