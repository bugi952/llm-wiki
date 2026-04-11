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
