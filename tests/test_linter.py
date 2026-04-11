import os
import pytest
from wiki.linter import lint_vault


@pytest.fixture
def vault_dir(tmp_path):
    ai = tmp_path / "ai"
    ai.mkdir()

    # Valid file with proper frontmatter
    (ai / "2026-04-10_good-article.md").write_text("""---
title: Good Article
source: deepmind-blog
url: https://example.com/good
date: 2026-04-10
domain: ai
importance: insight
---

## 핵심
Content here.

## 새로운 점
New stuff.
""")

    # Index that links to good-article and a missing file
    (ai / "index.md").write_text("""# AI 인덱스
최종 갱신: 2026-04-11

## 주제별
- [Good Article](2026-04-10_good-article.md)
- [Missing Article](2026-04-10_missing-article.md)
""")

    # Orphan file (not in index)
    (ai / "2026-04-09_orphan.md").write_text("""---
title: Orphan Article
source: test
url: https://example.com/orphan
date: 2026-04-09
domain: ai
importance: background
---

## 핵심
Orphan.
""")

    # File with missing frontmatter fields
    (ai / "2026-04-08_bad-frontmatter.md").write_text("""---
title: Bad Frontmatter
---

## 핵심
Missing fields.
""")

    return str(tmp_path)


def test_lint_detects_broken_links(vault_dir):
    report = lint_vault(vault_dir)
    assert len(report["broken_links"]) == 1
    assert "missing-article" in report["broken_links"][0]


def test_lint_detects_orphan_files(vault_dir):
    report = lint_vault(vault_dir)
    assert len(report["orphan_files"]) >= 1
    orphan_names = [os.path.basename(f) for f in report["orphan_files"]]
    assert "2026-04-09_orphan.md" in orphan_names


def test_lint_detects_missing_frontmatter(vault_dir):
    report = lint_vault(vault_dir)
    assert len(report["missing_frontmatter"]) >= 1
    # bad-frontmatter.md is missing date, importance, etc.
    bad = [f for f in report["missing_frontmatter"] if "bad-frontmatter" in f["file"]]
    assert len(bad) == 1
    assert len(bad[0]["missing"]) > 0


def test_lint_clean_vault(tmp_path):
    """Empty vault should produce clean report."""
    (tmp_path / "ai").mkdir()
    (tmp_path / "ai" / "index.md").write_text("# AI 인덱스\n")
    report = lint_vault(str(tmp_path))
    assert len(report["broken_links"]) == 0
    assert len(report["orphan_files"]) == 0
    assert len(report["missing_frontmatter"]) == 0
