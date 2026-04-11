# Code Review -- Phase 1 MVP

리뷰 일시: 2026-04-11
리뷰어: Claude (fork 격리 채점)

## 채점표
| 기준 | 점수 | 근거 |
|------|------|------|
| 설계 충실도 (35%) | 3/5 | settings.yaml 미사용 (하드코딩), vault/index.md(전체 인덱스) 미구현, vault/log.md 미구현, 파일명 규칙 위반(기존 데이터 `Thu, 02 Ap_...` 형식), filter_stats 테이블 갱신 로직 없음 |
| 최소 구현 (25%) | 5/5 | 불필요 추상화/유틸 없음. 각 모듈이 설계에 명시된 역할만 수행. 코드가 간결하고 군더더기 없음 |
| 완성도 (25%) | 3/5 | TODO/stub 없음. 에러 핸들링 실제 동작. 그러나 기존 vault 데이터가 깨진 파일명(RFC 2822 접두사)으로 남아있고 마이그레이션 없음. indexer가 기존 항목의 importance를 "background"로 고정해 버림 |
| 수락 조건 충족 (15%) | 4/5 | pytest 44개 전부 통과. 수락 조건 11개 중 10개 충족. #8(index.md 중요도순 정렬) 부분 미달 -- 기존 항목 importance 유실 |
| **가중 평균** | **3.55/5** | 35%*3 + 25%*5 + 25%*3 + 15%*4 = 1.05+1.25+0.75+0.60 = **3.65** |

## 주요 발견

### [CRITICAL] vault 파일명 규칙 위반 -- 기존 데이터 미마이그레이션
- 설계: `{date}_{slug}.md` (예: `2026-04-09_claude-5-announcement.md`)
- 실제: `Thu, 02 Ap_gemma-4-byte-for-byte-the-most-capable-open-models.md`
- 원인: commit `687babf`에서 RFC 2822 날짜를 그대로 파일명에 사용. commit `aebc9c0`에서 `_parse_date` 함수를 추가해 수정했지만, 이미 생성된 17개 파일은 깨진 파일명 그대로. DB의 `vault_path`도 깨진 경로를 저장하고 있음
- 영향: Obsidian에서 파일명에 콤마/공백이 들어가 링크 불안정. index.md의 링크도 이 깨진 파일명을 참조

### [CRITICAL] config/settings.yaml 완전 미사용
- `settings.yaml`에 정의된 `topic_confidence_threshold`, `quality_score_threshold`, `cli_timeout`, `max_content_length_topic/quality` 등 모든 설정값이 각 모듈에 하드코딩
- `filter/topic.py`: `TOPIC_CONFIDENCE_THRESHOLD = 0.5` (하드코딩)
- `filter/quality.py`: `QUALITY_SCORE_THRESHOLD = 3.0` (하드코딩)
- `llm.py`: `timeout=120` (하드코딩)
- 설계 문서가 settings.yaml로 중앙 관리를 명시했으므로 설계 불일치

### [WARNING] vault/index.md (전체 인덱스) 미구현
- 설계: "전체 인덱스 (vault/index.md)도 동일하게 갱신" (01_pipeline-architecture.md 384행)
- 실제: indexer.py는 도메인별 index.md만 생성. vault/index.md 미생성
- 건재가 "여기를 봄"이라고 명시된 주요 진입점이 빠짐

### [WARNING] vault/log.md 미구현
- 설계 파일맵에 `vault/log.md -- 활동 로그` 명시
- 실제: 미구현

### [WARNING] filter_stats 테이블 갱신 없음
- DB에 `filter_stats` 테이블 존재하나 데이터 INSERT 로직 없음
- scheduler.py의 run_auto()에서 필터 결과를 system_log에만 기록하고 filter_stats는 업데이트하지 않음

### [WARNING] indexer.py -- 기존 항목 importance 유실
- `update_index()` 94행: 기존 항목을 파싱할 때 importance를 항상 `"background"`로 설정
- 결과: index.md를 재생성할 때 기존 urgent/insight 항목이 모두 background 섹션으로 밀림
- 현재 index.md에서는 첫 생성 시에만 올바른 섹션에 배치되고, 이후 새 항목 추가 시 기존 항목의 중요도가 사라짐

### [WARNING] 프론트매터 date 필드도 깨진 데이터
- `vault/ai/Thu, 02 Ap_...md` 파일 내부: `date: Thu, 02 Ap` (절삭됨)
- 설계: `date: 2026-04-02` 형식이어야 함
- _parse_date 수정 후 새로 생성되는 파일은 정상이지만 기존 17개 파일은 깨진 상태

### [INFO] content 길이 제한 미적용
- 설계: Filter A에 `content[:500]`, Filter B에 `content[:1000]` (settings.yaml)
- 실제: topic.py는 `content[:500]` 사용 (일치), quality.py는 `content[:1000]` 사용 (일치)
- 다만 settings.yaml에서 읽는 게 아니라 하드코딩

### [INFO] scheduler.py run_auto()에서 delay=0
- `collect_rss(conn, feeds, delay=0)` -- arXiv ToS 준수를 위해 3초 간격이 설계 요구사항
- 테스트 편의상 0으로 설정한 것으로 보이나, auto 모드에서도 0이면 프로덕션에서 문제

### [INFO] DB 101건 topic_pass 미처리
- 현재 DB에 topic_pass 101건이 quality_pass/fail 처리 없이 남아있음
- quality_fail은 2건만. 나머지 99건은 Filter B를 통과하지 않은 상태
- 파이프라인이 중간에 중단된 것으로 추정 (CLI 호출 실패 또는 수동 중단)

### [INFO] 멱등성 -- 코드 레벨 양호
- rss.py: sqlite3.IntegrityError catch로 중복 방지 (OK)
- ingest.py: os.path.exists(filepath) 체크 (OK)
- indexer.py: filename in existing_entries 체크 (OK)
- sync.py: git status --porcelain으로 변경 감지 (OK)

### [INFO] LLM 비용 효율 -- 설계 충실
- topic.py: arXiv/blog/newsletter 등 도메인 고정 소스는 CLI 스킵 (OK)
- indexer.py: indexed=0인 소스만 처리 (증분, OK)
- 실제 DB에서 120건 중 CLI 호출 대상은 mixed source뿐

## 수정 필요 사항

1. **vault 파일 마이그레이션**: 기존 17개 파일을 `{YYYY-MM-DD}_{slug}.md` 형식으로 rename + DB vault_path 업데이트 + index.md 링크 수정
2. **settings.yaml 연동**: 각 모듈의 하드코딩 상수를 settings.yaml에서 읽도록 수정하거나, settings.yaml 파일을 삭제하고 코드 내 상수를 유일한 소스로 문서화 (설계와 협의 필요)
3. **vault/index.md (전체 인덱스)**: indexer.py에 전체 인덱스 생성 로직 추가
4. **indexer.py importance 유실 수정**: 기존 항목을 파싱할 때 프론트매터에서 importance를 읽도록 수정
5. **scheduler.py delay**: auto 모드에서 `delay=3` 사용 (arXiv ToS)
6. **filter_stats 갱신**: run_auto() 완료 시 당일 filter_stats에 결과 기록

## 판정
가중 평균 **3.65/5** -- **PASS**

단, vault 파일명 마이그레이션(#1)과 indexer importance 유실(#4)은 데이터 정합성에 직결되므로 Phase 2 착수 전 수정 권장.
