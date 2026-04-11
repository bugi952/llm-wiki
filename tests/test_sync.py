import os
import subprocess
import pytest
from sync import sync_vault


@pytest.fixture
def git_vault(tmp_path):
    """Create a temp git repo with vault structure."""
    vault = tmp_path / "vault"
    (vault / "ai").mkdir(parents=True)
    # Init git
    subprocess.run(["git", "init"], cwd=tmp_path, capture_output=True)
    subprocess.run(["git", "config", "user.name", "test"], cwd=tmp_path, capture_output=True)
    subprocess.run(["git", "config", "user.email", "test@test.com"], cwd=tmp_path, capture_output=True)
    # Initial commit
    (tmp_path / ".gitkeep").write_text("")
    subprocess.run(["git", "add", "."], cwd=tmp_path, capture_output=True)
    subprocess.run(["git", "commit", "-m", "init"], cwd=tmp_path, capture_output=True)
    return tmp_path


def test_sync_no_changes(git_vault):
    result = sync_vault(str(git_vault), dry_run=True)
    assert result["changed"] is False
    assert result["committed"] is False


def test_sync_detects_changes(git_vault):
    # Add a file to vault
    (git_vault / "vault" / "ai" / "test.md").write_text("# Test")
    result = sync_vault(str(git_vault), dry_run=True)
    assert result["changed"] is True
    assert result["committed"] is False  # dry-run


def test_sync_commits_changes(git_vault):
    (git_vault / "vault" / "ai" / "test.md").write_text("# Test")
    result = sync_vault(str(git_vault), dry_run=False)
    assert result["changed"] is True
    assert result["committed"] is True
    assert result["pushed"] is False  # no remote

    # Verify commit exists
    log = subprocess.run(
        ["git", "log", "--oneline", "-1"],
        cwd=git_vault, capture_output=True, text=True
    )
    assert "wiki:" in log.stdout


def test_sync_idempotent(git_vault):
    (git_vault / "vault" / "ai" / "test.md").write_text("# Test")
    sync_vault(str(git_vault), dry_run=False)
    result = sync_vault(str(git_vault), dry_run=False)
    assert result["changed"] is False
