import logging
import os
import subprocess
from datetime import date

logger = logging.getLogger(__name__)


def _run_git(args, cwd):
    """Run a git command, return (returncode, stdout, stderr)."""
    result = subprocess.run(
        ["git"] + args, cwd=cwd,
        capture_output=True, text=True
    )
    return result.returncode, result.stdout.strip(), result.stderr.strip()


def sync_vault(repo_dir=".", dry_run=False):
    """Detect vault/ changes, commit and push.

    Returns dict with changed, committed, pushed status.
    """
    result = {"changed": False, "committed": False, "pushed": False}

    # Check for changes in vault/ and site/
    track_dirs = ["vault/"]
    if os.path.isdir(os.path.join(repo_dir, "site")):
        track_dirs.append("site/")
    rc, stdout, _ = _run_git(["status", "--porcelain"] + track_dirs, repo_dir)
    if not stdout:
        logger.info("No vault changes to sync")
        return result

    result["changed"] = True

    # Count new and modified files
    lines = [l for l in stdout.split("\n") if l.strip()]
    new = sum(1 for l in lines if l.startswith("?") or l.startswith("A"))
    modified = sum(1 for l in lines if l.startswith("M") or l.startswith(" M"))

    if dry_run:
        logger.info("Dry run: %d new, %d modified files", new, modified)
        return result

    # Stage vault + site changes
    _run_git(["add"] + track_dirs, repo_dir)

    # Commit
    today = date.today().isoformat()
    msg = f"wiki: {today} 업데이트 (+{new}건, ~{modified}건)"
    rc, _, stderr = _run_git(["commit", "-m", msg], repo_dir)
    if rc == 0:
        result["committed"] = True
        logger.info("Committed: %s", msg)
    else:
        logger.warning("Commit failed: %s", stderr)
        return result

    # Push (may fail if no remote)
    rc, _, stderr = _run_git(["push", "origin", "main"], repo_dir)
    if rc == 0:
        result["pushed"] = True
        logger.info("Pushed to origin/main")
    else:
        logger.warning("Push failed (will retry next cycle): %s", stderr)

    return result
