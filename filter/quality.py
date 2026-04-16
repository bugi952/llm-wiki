"""Filter B: batch quality + routing evaluation.

Groups sources by domain, evaluates up to BATCH_SIZE per CLI call.
Each call returns quality scores AND routing info, eliminating
the separate router.py CLI call during ingest.
"""

import json
import logging
import os

from config import get_config
from llm import claude_call
from wiki.pages import list_pages

logger = logging.getLogger(__name__)

BATCH_SIZE = 5


def _load_index_md(domain):
    """Load existing index.md for context."""
    path = f"vault/{domain}/index.md"
    if os.path.exists(path):
        with open(path) as f:
            return f.read()
    return "(아직 인덱스 없음)"


def _build_batch_prompt(sources, index_context, page_list, max_len):
    """Build a single prompt that evaluates multiple sources at once."""
    source_block = []
    for i, (sid, domain, title, content) in enumerate(sources):
        source_block.append(
            f"[{i}] id={sid}\n제목: {title}\n내용: {(content or '')[:max_len]}"
        )
    sources_text = "\n---\n".join(source_block)

    return f"""품질 평가 + 위키 라우터 (배치 모드). 아래 소스들을 각각 평가하라.

기존 Wiki 인덱스:
{index_context}

기존 위키 페이지 목록:
{page_list}

=== 소스 목록 ===
{sources_text}
=== 끝 ===

각 소스에 대해:
1. 기존 Wiki 대비 새로운 가치 평가 (novelty, importance, reliability 각 1-5)
2. 통과 시 (average >= 3.0) 위키 라우팅 정보도 함께 제공

JSON 배열만 출력. 설명 없이 JSON만:
[
  {{
    "id": 소스id,
    "novelty": 1-5,
    "importance": 1-5,
    "reliability": 1-5,
    "average": float,
    "importance_tag": "urgent"|"insight"|"connection"|"background",
    "reason": "한줄 평가",
    "entities": ["조직/제품명"],
    "concepts": ["관련 개념"],
    "new_pages": [{{"title": "페이지명", "type": "entity 또는 concept", "reason": "생성 이유"}}],
    "facts": [{{"page": "대상 페이지명", "entry": "한줄 팩트 (한국어)", "date": "YYYY-MM-DD"}}],
    "summary_ko": "3줄 이내 한국어 요약",
    "whats_new": "기존 지식 대비 새로운 점"
  }}
]

규칙:
- entities/concepts: 기존 페이지와 정확히 같은 이름 사용
- new_pages: 기존에 없는 중요한 엔티티/개념만. 사소한 것은 만들지 마
- facts: 각 대상 페이지에 추가할 타임라인 항목. 간결하게
- average < 3.0이면 라우팅 필드(entities~whats_new)는 빈 값으로"""


def _call_batch(sources, index_context, page_list, max_len, conn):
    """Call CLI once for a batch of sources. Returns list of result dicts."""
    prompt = _build_batch_prompt(sources, index_context, page_list, max_len)
    result = claude_call(prompt, conn=conn, expect_json="array")

    # Validate: must be a list
    if isinstance(result, dict):
        result = [result]
    if not isinstance(result, list):
        raise ValueError(f"Expected list, got {type(result)}")

    return result


def filter_quality(conn, threshold=None):
    """Run Filter B on all topic_pass sources using batch evaluation.

    Quality scores AND routing info are stored in filter_b_result.
    Ingest phase reads routing from there — no separate CLI call needed.

    Returns (passed_count, failed_count).
    """
    if threshold is None:
        threshold = get_config()["filter"]["quality_score_threshold"]
    max_len = get_config()["filter"]["max_content_length_quality"]

    cursor = conn.execute(
        "SELECT id, domain, title, content FROM sources WHERE status = 'topic_pass'"
    )
    rows = cursor.fetchall()

    if not rows:
        return 0, 0

    # Group by domain for shared index context
    by_domain = {}
    for sid, domain, title, content in rows:
        by_domain.setdefault(domain, []).append((sid, domain, title, content))

    passed = 0
    failed = 0

    for domain, domain_sources in by_domain.items():
        index_context = _load_index_md(domain)

        # Load existing page list for routing context
        existing = list_pages(conn, domain=domain)
        page_list = "\n".join(f"- {p['title']} ({p['page_type']})" for p in existing)
        if not page_list:
            page_list = "(아직 페이지 없음)"

        # Process in batches
        for i in range(0, len(domain_sources), BATCH_SIZE):
            batch = domain_sources[i:i + BATCH_SIZE]

            try:
                results = _call_batch(batch, index_context, page_list, max_len, conn)
            except Exception as e:
                logger.error("Batch quality eval failed for %s[%d:%d]: %s",
                             domain, i, i + len(batch), e)
                # Mark entire batch as failed
                for sid, _, title, _ in batch:
                    conn.execute(
                        "UPDATE sources SET status = 'quality_fail' WHERE id = ?",
                        (sid,),
                    )
                    failed += 1
                continue

            # Build lookup by source id
            result_by_id = {}
            for r in results:
                rid = r.get("id")
                if rid is not None:
                    result_by_id[int(rid)] = r

            for sid, _, title, _ in batch:
                result = result_by_id.get(sid)
                if not result:
                    logger.warning("No result for source %d in batch response", sid)
                    conn.execute(
                        "UPDATE sources SET status = 'quality_fail' WHERE id = ?",
                        (sid,),
                    )
                    failed += 1
                    continue

                try:
                    average = float(result.get("average", 0))
                except (TypeError, ValueError):
                    average = 0.0
                importance_tag = result.get("importance_tag", "background")

                if average >= threshold:
                    conn.execute(
                        "UPDATE sources SET status = 'quality_pass', importance = ?, "
                        "filter_b_result = ? WHERE id = ?",
                        (importance_tag, json.dumps(result), sid),
                    )
                    passed += 1
                    logger.info("Quality pass: %s [%.1f, %s]", title, average, importance_tag)
                else:
                    conn.execute(
                        "UPDATE sources SET status = 'quality_fail', filter_b_result = ? WHERE id = ?",
                        (json.dumps(result), sid),
                    )
                    failed += 1
                    logger.info("Quality fail: %s [%.1f]", title, average)

    conn.commit()
    return passed, failed
