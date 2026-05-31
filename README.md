# LLM Wiki

LLM Wiki is an open-source automation pipeline for collecting AI and macroeconomic sources, filtering them with LLMs, summarizing important updates, and syncing structured notes into an Obsidian/GitHub-based wiki.

It is designed for researchers, builders, and maintainers who need to reduce information overload and turn raw sources into reusable knowledge.

## Features

- RSS/API source collection for AI and macroeconomic updates
- LLM-based relevance and quality filtering
- Novelty detection against existing notes
- Markdown/Obsidian-compatible wiki generation
- SQLite-based tracking
- GitHub/Obsidian sync workflow
- Scheduled automation support

## Why this matters

Researchers and maintainers often spend too much time manually scanning news, papers, releases, and market updates. LLM Wiki turns that workflow into a reusable open-source pipeline that collects raw sources, filters noise, summarizes useful information, and organizes it into a long-term knowledge base.

## Project status

Early-stage MVP. Actively maintained.

The current repository includes the core project structure, collectors, filters, documentation drafts, wiki/vault structure, and automation experiments.

## Use cases

- Personal AI research wiki
- Macro and market intelligence archive
- Obsidian-based knowledge management
- Automated daily digest generation
- LLM-assisted source filtering and summarization
- Reusable maintainer workflow for open-source knowledge projects

## Roadmap

- Improve setup documentation
- Add example configuration files
- Add sample generated wiki output
- Add clearer contributor guidelines
- Add GitHub Actions workflow examples
- Add tests for collector, filter, and sync modules
- Improve LLM prompt evaluation and quality scoring

## Repository structure

```text
collector/      Source collection modules
filter/         LLM filtering and quality scoring
config/         Configuration examples
docs/           Project documentation
vault/          Obsidian-compatible knowledge vault
wiki/           Generated wiki content
site/           GitHub Pages / site output
tests/          Test files
