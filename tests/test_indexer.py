import os
import pytest
from db import get_db, init_db
from wiki.indexer import update_index
from wiki.pages import create_page, list_pages


@pytest.fixture
def db():
    conn = get_db(":memory:")
    init_db(conn)
    yield conn
    conn.close()


@pytest.fixture
def vault_dir(tmp_path):
    (tmp_path / "ai" / "entities").mkdir(parents=True)
    (tmp_path / "ai" / "concepts").mkdir(parents=True)
    (tmp_path / "macro" / "indicators").mkdir(parents=True)
    return str(tmp_path)


def test_update_index_creates_index_md(db, vault_dir, monkeypatch):
    monkeypatch.setattr("wiki.pages.VAULT_DIR", vault_dir)
    monkeypatch.setattr("wiki.indexer.VAULT_DIR", vault_dir)

    create_page(db, "ai/entities/Anthropic", "Anthropic", "entity", "ai")
    update_index(db, vault_dir)

    index_path = os.path.join(vault_dir, "ai", "index.md")
    assert os.path.exists(index_path)
    content = open(index_path).read()
    assert "Anthropic" in content


def test_update_index_groups_by_type(db, vault_dir, monkeypatch):
    monkeypatch.setattr("wiki.pages.VAULT_DIR", vault_dir)
    monkeypatch.setattr("wiki.indexer.VAULT_DIR", vault_dir)

    create_page(db, "ai/entities/Anthropic", "Anthropic", "entity", "ai")
    create_page(db, "ai/concepts/AI Safety", "AI Safety", "concept", "ai")
    update_index(db, vault_dir)

    index_path = os.path.join(vault_dir, "ai", "index.md")
    content = open(index_path).read()
    assert "🏢 엔티티" in content
    assert "💡 개념" in content
    # Entity before concept
    assert content.index("엔티티") < content.index("개념")


def test_update_index_creates_global_index(db, vault_dir, monkeypatch):
    monkeypatch.setattr("wiki.pages.VAULT_DIR", vault_dir)
    monkeypatch.setattr("wiki.indexer.VAULT_DIR", vault_dir)

    create_page(db, "ai/entities/Anthropic", "Anthropic", "entity", "ai")
    create_page(db, "macro/indicators/US Interest Rates", "US Interest Rates", "indicator", "macro")
    update_index(db, vault_dir)

    global_path = os.path.join(vault_dir, "index.md")
    assert os.path.exists(global_path)
    content = open(global_path).read()
    assert "AI" in content
    assert "Anthropic" in content
    assert "US Interest Rates" in content


def test_update_index_builds_log(db, vault_dir, monkeypatch):
    monkeypatch.setattr("wiki.pages.VAULT_DIR", vault_dir)
    monkeypatch.setattr("wiki.indexer.VAULT_DIR", vault_dir)

    create_page(db, "ai/entities/Anthropic", "Anthropic", "entity", "ai")
    # Simulate a page update
    page_id = db.execute("SELECT id FROM wiki_pages WHERE slug = 'ai/entities/Anthropic'").fetchone()[0]
    db.execute("INSERT INTO page_updates (page_id, update_type) VALUES (?, 'create')", (page_id,))
    db.commit()

    update_index(db, vault_dir)

    log_path = os.path.join(vault_dir, "log.md")
    assert os.path.exists(log_path)
    content = open(log_path).read()
    assert "Anthropic" in content


def test_update_index_idempotent(db, vault_dir, monkeypatch):
    monkeypatch.setattr("wiki.pages.VAULT_DIR", vault_dir)
    monkeypatch.setattr("wiki.indexer.VAULT_DIR", vault_dir)

    create_page(db, "ai/entities/Anthropic", "Anthropic", "entity", "ai")
    update_index(db, vault_dir)
    update_index(db, vault_dir)

    index_path = os.path.join(vault_dir, "ai", "index.md")
    content = open(index_path).read()
    # Wiki link format: [[entities/Anthropic|Anthropic]] - count the link entries
    assert content.count("[[entities/Anthropic|Anthropic]]") == 1
