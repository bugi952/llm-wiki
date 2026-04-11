"""Route sources to wiki pages. 1 LLM call per source."""

import logging

from llm import claude_call
from wiki.pages import list_pages

logger = logging.getLogger(__name__)


def route_source(source, conn):
    """Determine which wiki pages to update for a given source.

    Args:
        source: dict with title, content, url, domain, importance, published_at
        conn: DB connection

    Returns:
        dict with entities, concepts, new_pages, facts, summary_ko, whats_new
    """
    existing = list_pages(conn, domain=source["domain"])
    page_list = "\n".join(f"- {p['title']} ({p['page_type']})" for p in existing)
    if not page_list:
        page_list = "(아직 페이지 없음)"

    content_preview = (source.get("content") or "")[:1500]

    prompt = f"""위키 라우터. 새 소스를 분석하고 업데이트할 페이지를 결정하라.

기존 위키 페이지 목록:
{page_list}

새 소스:
제목: {source['title']}
도메인: {source['domain']}
중요도: {source.get('importance', 'background')}
URL: {source.get('url', '')}
날짜: {source.get('published_at', '')}
내용:
{content_preview}

아래 JSON만 출력. 설명 없이 JSON만:
{{
  "entities": ["기존 또는 새 엔티티명"],
  "concepts": ["기존 또는 새 개념명"],
  "new_pages": [{{"title": "페이지명", "type": "entity 또는 concept", "reason": "생성 이유"}}],
  "facts": [
    {{"page": "대상 페이지명", "entry": "한줄 팩트 (한국어)", "date": "YYYY-MM-DD"}}
  ],
  "summary_ko": "3줄 이내 한국어 요약",
  "whats_new": "기존 지식 대비 새로운 점 (한국어)"
}}

규칙:
- entities: 이 소스에 언급된 조직/제품명. 기존 페이지와 정확히 같은 이름 사용
- concepts: 이 소스와 관련된 개념/주제. 기존 페이지와 정확히 같은 이름 사용
- new_pages: 기존에 없는 중요한 엔티티/개념만. 사소한 것은 만들지 마
- facts: 각 대상 페이지에 추가할 타임라인 항목. 간결하게
- 매크로 지표 데이터인 경우 entities/concepts 대신 indicator 페이지에 매핑"""

    result = claude_call(prompt, conn=conn, expect_json=True)

    # Validate structure
    for key in ["entities", "concepts", "facts", "summary_ko", "whats_new"]:
        if key not in result:
            result[key] = [] if key in ["entities", "concepts", "facts"] else ""
    if "new_pages" not in result:
        result["new_pages"] = []

    return result
