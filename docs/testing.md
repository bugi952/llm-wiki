# LLM Wiki -- 테스트 전략 + Phase별 수락 조건

## 테스트 원칙
- 모든 모듈은 TDD (RED/GREEN/REFACTOR)
- 외부 API 호출은 mock. 실제 연결은 /test-connection으로 별도 확인
- DB 테스트는 인메모리 SQLite (실제 wiki.db 건드리지 않음)
- 멱등성 테스트 필수: 같은 입력 2회 실행 -> 중복 없음 확인

---

## Phase 1: MVP -- 첫 자동 수집 + Wiki 페이지 생성

### 수락 조건
1. `python -m pytest tests/` 전체 통과
2. DB 스키마 생성 -> sources, filter_stats, system_log 테이블 존재 확인
3. collector/rss.py: arXiv RSS 피드에서 최소 1건 수집 -> DB sources에 status='collected'로 저장
4. collector/rss.py: 같은 피드 2회 수집 -> 중복 INSERT 없음 (unique 제약)
5. filter/topic.py: arXiv 소스 -> LLM 스킵, domain='ai', status='topic_pass' 직접 설정
6. filter/quality.py: topic_pass 소스에 Haiku 호출 -> 3.0+ 통과, 3.0- 탈락. status 업데이트
7. wiki/ingest.py: quality_pass 소스 -> vault/ai/{date}_{slug}.md 파일 생성 (프론트매터 + 핵심 + 새로운 점)
8. wiki/indexer.py: 새 파일 -> vault/ai/index.md에 추가. 기존 항목 유지. 중요도순 정렬
9. sync.py: vault/ 변경 감지 -> git commit + push 성공 (테스트에서는 dry-run)
10. 전체 파이프라인: scheduler.py auto -> collect -> filter -> ingest -> index -> sync 순차 실행 완료
11. 일일 API 호출 카운터: 300회 초과 시 파이프라인 중단 확인

### 완료 기준
arXiv RSS에서 수집한 논문이 vault/ai/index.md에 요약과 함께 나타남.
Obsidian에서 index.md 열어서 링크 클릭하면 개별 요약 페이지로 이동.

---

## Phase 2: 소스 확장

### 수락 조건
1. collector/hackernews.py: HN top 100 -> AI 키워드 필터 -> score >= 50 -> DB 저장
2. collector/hackernews.py: HN 소스 -> Filter A에서 Haiku 호출로 분류 (혼합 소스)
3. RSSHub 셀프호스팅: http://localhost:1200/ 응답 확인
4. RSSHub 경유 Anthropic/OpenAI 블로그 -> rss.py로 수집 가능
5. RSSHub 장애 시 -> 커뮤니티 RSS 폴백 URL로 자동 전환
6. collector/fred.py: 지정 시리즈(GDP, CPI 등) 최신값 조회 -> DB 저장
7. collector/ecos.py: 한국은행 기준금리 등 조회 -> DB 저장
8. collector/finnhub.py: 이번 주 US/KR 경제 이벤트 조회 -> high impact 알림
9. 전체 소스 수집 1회 5분 이내 완료

### 완료 기준
AI + Macro 양쪽 index.md에 자동 수집된 콘텐츠 표시.

---

## Phase 3: 수동 인풋 + 알림

### 수락 조건
1. bot.py: systemd 서비스로 24시간 가동. 크래시 시 자동 재시작
2. /add URL -> 즉시 filter -> ingest -> sync (크론 대기 안 함)
3. /add X URL -> fxtwitter 자동 변환 -> 내용 추출 -> 파이프라인
4. /add 텍스트 -> 텍스트 기반 소스로 처리
5. /status, /recent, /stats -> 정확한 통계 반환
6. 긴급(urgent) 소스 -> 즉시 텔레그램 알림
7. scheduler.py와 bot.py 동시 실행 -> 락 파일로 충돌 방지
8. 스테일 락 (1시간+) -> 자동 삭제 + 알림

### 완료 기준
건재가 텔레그램에서 URL을 보내면 수분 내 vault에 요약 페이지 생성.

---

## Phase 4: 안정화

### 수락 조건
1. wiki/linter.py: 깨진 링크, 고아 파일, 중복 소스, 프론트매터 누락 탐지
2. 주간 리포트: 수집 N -> 필터 N -> Wiki N 텔레그램 전송
3. 크론 등록: 6시간 간격 자동 실행 + DB 백업 (매일)
4. 30일 지난 항목 -> index 아카이브 섹션 이동
5. 90일 지난 항목 -> index에서 제거 (파일 유지)
6. 7일간 무인 운영 -> 장애 없이 자동 수집+필터+Wiki 갱신

### 완료 기준
1주일 무인 운영 후 vault에 정상적인 콘텐츠 축적. 장애 알림 없음.

---

## Phase 5: 확장 (나중에)

### 수락 조건
1. YouTube 자막 수집기
2. 추가 RSS 소스 (MIT Tech Review, MarkTechPost 등)
3. 뉴스 봇 합류 검토

### 완료 기준
Phase 4 안정화 후 논의.
