import logging
import os
import re

logger = logging.getLogger(__name__)


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

REQUIRED_FRONTMATTER = {"title", "date", "domain", "importance"}
LINK_PATTERN = re.compile(r'\[.*?\]\(([^)]+\.md)\)')


def _find_domains(vault_dir):
    """Find domain subdirectories in vault."""
    domains = []
    for name in os.listdir(vault_dir):
        path = os.path.join(vault_dir, name)
        if os.path.isdir(path) and name not in ("raw",):
            domains.append(name)
    return domains


def lint_vault(vault_dir="vault"):
    """Run integrity checks on vault.

    Returns dict with broken_links, orphan_files, duplicate_urls, missing_frontmatter.
    """
    report = {
        "broken_links": [],
        "orphan_files": [],
        "duplicate_urls": [],
        "missing_frontmatter": [],
    }

    domains = _find_domains(vault_dir)

    for domain in domains:
        domain_dir = os.path.join(vault_dir, domain)
        index_path = os.path.join(domain_dir, "index.md")

        # Collect all .md files (excluding index.md)
        all_files = set()
        for fname in os.listdir(domain_dir):
            if fname.endswith(".md") and fname != "index.md":
                all_files.add(fname)

        # Parse index.md for links
        linked_files = set()
        if os.path.exists(index_path):
            with open(index_path) as f:
                content = f.read()
            for match in LINK_PATTERN.finditer(content):
                linked = match.group(1)
                linked_files.add(linked)
                # Check broken link
                if not os.path.exists(os.path.join(domain_dir, linked)):
                    report["broken_links"].append(f"{domain}/{linked}")

        # Orphan files (in directory but not in index)
        for fname in all_files:
            if fname not in linked_files:
                report["orphan_files"].append(f"{domain}/{fname}")

        # Frontmatter check
        for fname in all_files:
            filepath = os.path.join(domain_dir, fname)
            fm = _parse_frontmatter(filepath)
            missing = REQUIRED_FRONTMATTER - set(fm.keys())
            if missing:
                report["missing_frontmatter"].append({
                    "file": f"{domain}/{fname}",
                    "missing": sorted(missing),
                })

    # Duplicate URL check across all sources
    seen_urls = {}
    for domain in domains:
        domain_dir = os.path.join(vault_dir, domain)
        for fname in os.listdir(domain_dir):
            if not fname.endswith(".md") or fname == "index.md":
                continue
            filepath = os.path.join(domain_dir, fname)
            fm = _parse_frontmatter(filepath)
            url = fm.get("url", "")
            if url:
                if url in seen_urls:
                    report["duplicate_urls"].append({
                        "url": url,
                        "files": [seen_urls[url], f"{domain}/{fname}"],
                    })
                else:
                    seen_urls[url] = f"{domain}/{fname}"

    # Summary log
    total_issues = (len(report["broken_links"]) + len(report["orphan_files"])
                    + len(report["duplicate_urls"]) + len(report["missing_frontmatter"]))
    if total_issues:
        logger.warning("Lint: %d issues found", total_issues)
    else:
        logger.info("Lint: clean")

    return report


def format_report(report):
    """Format lint report as human-readable text (Korean)."""
    lines = ["🔍 Wiki 정합성 점검 결과"]

    if report["broken_links"]:
        lines.append(f"\n❌ 깨진 링크 ({len(report['broken_links'])}건):")
        for link in report["broken_links"]:
            lines.append(f"  • {link}")

    if report["orphan_files"]:
        lines.append(f"\n📄 고아 파일 ({len(report['orphan_files'])}건):")
        for f in report["orphan_files"]:
            lines.append(f"  • {f}")

    if report["duplicate_urls"]:
        lines.append(f"\n🔗 중복 URL ({len(report['duplicate_urls'])}건):")
        for dup in report["duplicate_urls"]:
            lines.append(f"  • {dup['url']}")

    if report["missing_frontmatter"]:
        lines.append(f"\n⚠️ 프론트매터 누락 ({len(report['missing_frontmatter'])}건):")
        for item in report["missing_frontmatter"]:
            lines.append(f"  • {item['file']}: {', '.join(item['missing'])}")

    total = (len(report["broken_links"]) + len(report["orphan_files"])
             + len(report["duplicate_urls"]) + len(report["missing_frontmatter"]))
    if total == 0:
        lines.append("\n✅ 이상 없음")

    return "\n".join(lines)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    report = lint_vault()
    print(format_report(report))
