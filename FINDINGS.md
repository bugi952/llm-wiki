# FINDINGS — 역류 피드백

설계와 다르게 구현했거나 빠진 엣지 케이스를 기록한다.

## Phase 1 (2026-04-11)

### arXiv RSS 주말 비어있음
- arXiv RSS는 평일에만 업데이트. 토/일에 수집하면 0건
- arXiv Atom API(`export.arxiv.org/api/query`)는 항상 동작하므로 폴백 가능
- Phase 2에서 검토

### CLI JSON 파싱 실패 빈번
- `claude -p --model haiku`가 JSON 대신 마크다운/텍스트로 응답하는 경우 있음
- 재시도(최대 5회)로 대부분 복구되지만, 120건 처리 시 전체 시간이 크게 늘어남
- 프롬프트에 "JSON만 출력" 강조 + 재시도로 현재 대응 중

### RSSHub 미설치
- Anthropic/OpenAI 블로그 피드(localhost:1200)는 RSSHub 셀프호스팅 필요
- Phase 1에서는 DeepMind(공식 RSS) + Import AI로 검증
- Phase 2에서 RSSHub 설치 예정

### St. Louis Fed RSS 파싱 실패
- `stlouisfed.org/rss` 응답이 malformed XML
- Phase 2 macro 소스 작업 시 대안 URL 확인 필요

## Phase 2 (2026-04-11)

### RSSHub 미설치 — Docker 패키지 충돌
- VPS에서 `apt install docker.io` 실패 (held packages 충돌)
- `curl -fsSL https://get.docker.com | sh`도 실패
- Anthropic/OpenAI 블로그는 폴백 URL로 수집 가능하므로 당장 영향 없음
- VPS apt 문제 해결 또는 재설치 시 Docker + RSSHub 설치 예정

## Wiki 구조 전환 (2026-04-12)

### LLM Wiki 패턴으로 전환
- 기존: 소스 1개 → 요약 페이지 1개 (나열 방식)
- 변경: 소스 1개 → 기존 wiki 페이지 N개 업데이트 (축적 방식)
- 건재가 LLM Wiki 패턴 문서를 공유하고 방향 승인
- 기존 117개 파일은 vault/archive/로 이동

### 설계 문서(docs/00, 01) 부재
- CLAUDE.md에서 참조하는 docs/00_project-brief.md, docs/01_pipeline-architecture.md가 존재하지 않음
- docs/testing.md만 존재
- LLM Wiki 전환으로 설계 문서 업데이트 필요

### Finnhub economic calendar API 접근 불가
- 무료 플랜에서 403 Forbidden
- 프리미엄 전용 엔드포인트로 추정
- $0 원칙에 따라 Finnhub 수집 스킵 처리 (에러 핸들링 추가)
- FRED + ECOS로 macro 데이터 수집 중

### 개념 페이지 내용 비어있음
- 마이그레이션 시 entity 페이지는 타임라인 엔트리로 채워졌으나
- concept 페이지(AI Safety, Scaling Laws 등)는 빈 껍데기 상태
- 새 소스 인제스트 시 라우터가 관련 concept 페이지에 팩트를 추가하면서 채워질 예정

### UTC/KST 타임존 불일치
- SQLite CURRENT_TIMESTAMP는 UTC, Python date.today()는 KST
- get_daily_api_count()가 날짜 경계에서 잘못 카운트할 수 있음
- 일일 API 한도 체크에 영향 가능 (UTC 0시~9시 사이)
