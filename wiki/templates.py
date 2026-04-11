"""Page templates for wiki page types."""

from datetime import datetime


def entity_template(title, domain):
    """Template for entity pages (organizations, products)."""
    now = datetime.now().strftime("%Y-%m-%d")
    return f"""---
type: entity
domain: {domain}
last_updated: {now}
source_count: 0
---

# {title}

## 개요


## 최근 동향


## 연관 페이지

"""


def concept_template(title, domain):
    """Template for concept pages (topics, themes)."""
    now = datetime.now().strftime("%Y-%m-%d")
    return f"""---
type: concept
domain: {domain}
last_updated: {now}
source_count: 0
---

# {title}

## 정의


## 주요 발전


## 핵심 주체


## 모순/논쟁

"""


def indicator_template(title, domain):
    """Template for macro indicator pages."""
    now = datetime.now().strftime("%Y-%m-%d")
    return f"""---
type: indicator
domain: {domain}
last_updated: {now}
---

# {title}

## 현재 수치
| 지표 | 값 | 날짜 | 추이 |
|------|-----|------|------|

## 분석


## 이력

"""


def weekly_template(domain, week_label):
    """Template for weekly digest pages."""
    now = datetime.now().strftime("%Y-%m-%d")
    return f"""---
type: weekly
domain: {domain}
last_updated: {now}
---

# {week_label} 주간 다이제스트

"""


TEMPLATES = {
    "entity": entity_template,
    "concept": concept_template,
    "indicator": indicator_template,
    "weekly": weekly_template,
}
