# LLM Wiki Bot

AI/Macro 분야 정보를 자동 수집 -> 필터링 -> Wiki 정리하는 봇.
Obsidian vault로 건재에게 전달, 건재가 선별해 Think Tank에 수동 intake.

## 환경
- 작업 디렉토리: /home/bugi/llm-wiki/
- Python venv: .venv/
- 시크릿: .env (FRED_API_KEY, ECOS_API_KEY, FINNHUB_API_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID)
- Claude: API 키 불필요. Claude Code CLI + Max 구독 (VPS에서 `claude login` 완료)
- GitHub: SSH 키 또는 PAT (vault 레포 push용)

## Owner Profile
- 오버엔지니어링 극도로 싫어함. 요구한 것만 구현
- 코드를 직접 읽지 않음 -> 동작 명세로 확인
- Think Tank에서 설계 완료 후 넘어온 프로젝트 -> docs/ 설계를 절대적으로 따를 것
- Wiki는 중간 저장소. Think Tank과 중복되는 지식 축적 금지

## Tech Stack
Python 3.12+ / Claude Code CLI (Haiku, Max 구독) / SQLite / feedparser / Telegram Bot API / GitPython / crontab + systemd

## Hard Rules

### Tier 0 -- 절대 불변 (어떤 상황에서도 위반 금지)
- **설계 문서가 진리.** docs/의 설계가 모든 구현 결정의 근거. 임의 변경/확장 금지
- **CLI 호출 최소화.** domain 고정 소스는 Filter A CLI 스킵. indexer는 증분만. 모든 LLM 호출은 `claude -p --model haiku` subprocess
- **vault/raw/는 Git에 안 올림.** .gitignore 필수. PDF는 VPS에만 보관
- **수동 인풋은 즉시 처리.** 건재가 텔레그램으로 던지면 크론 대기 없이 즉시 파이프라인
- **추가 비용 $0.** 무료 API만 사용. Claude는 Max 구독 CLI로 $0
- **일일 CLI 300회 한도.** 초과 시 파이프라인 중단 + 텔레그램 알림. rate limit 시 60초 대기 후 재시도
- **no hardcoded secrets.** 모든 credential은 환경변수
- **idempotent.** 같은 소스 두 번 수집해도 중복 생성 안 됨

### Tier 1 -- 필수 워크플로우
- 코드 변경 후 검증 필수
- 테스트 통과 전 완료 선언 금지

### Tier 2 -- 프로세스
- 멀티파일 구현 전 방향 제안

충돌 시: 낮은 숫자 Tier가 항상 우선. 같은 Tier 충돌 -> 보수적 옵션 선택.

## 실행 원칙

### 착수 전
- docs/00, 01 먼저 읽는다
- 구현 방향을 번호 목록으로 제안 (각 단계 1줄) -> 건재 컨펌 후 착수

### 착수 후
- 수락 조건 충족까지 한 번에 완성. 중간 확인 금지
- 에러 -> 자체 진단 -> 자체 수정 -> 3회 실패 시 건재에게 보고
- 기능 완성 시 code-gotchas.md 퀵체크 5항목 셀프 점검. 미달 시 전달 없이 수정

### 완료 시
- Phase 완료 시 /review-code 실행 (fork 격리 채점)
- 3.5+ -> 동작 명세 전달 (모듈명, 입출력, 핵심 로직, 제약 -- 10줄 이내 한국어)
- 3.5- -> 자체 수정 후 재평가 (최대 2회 재시도)
- 3회 미달 -> 채점표 추이 + 미달 원인 + 제안을 건재에게 텔레그램 알림

### 예외 -- 멈추고 건재에게 확인
- 설계 문서 간 모순 발견
- API 인증 변경 (FRED, ECOS, Finnhub, Telegram)
- DB 스키마 변경 (기존 데이터 영향)
- 새 외부 의존성 추가 필요
- RSSHub 라우트 변경 필요

### 역류
설계와 다르게 구현했거나 빠진 엣지 케이스 -> FINDINGS.md에 기록

## File Map
```
docs/                     # 설계 문서 (00 brief, 01 architecture)
config/                   # settings.yaml, sources/, filter_rules.yaml
collector/                # 수집 모듈 (rss, hackernews, fred, ecos, finnhub, manual)
filter/                   # topic.py (Filter A), quality.py (Filter B)
wiki/                     # ingest.py, indexer.py, linter.py
vault/                    # Obsidian vault (ai/, macro/, raw/)
data/wiki.db              # SQLite
data/logs/                # 실행 로그
bot.py                    # 텔레그램 봇 (systemd)
scheduler.py              # 메인 스케줄러 (크론 6시간)
sync.py                   # Git push 자동화
code-gotchas.md           # 코딩 채점 기준 (/review-code 참조)
FINDINGS.md               # 역류 피드백 (개발->Think Tank)
reviews/                  # 코드 리뷰 기록
.claude/commands/         # build-phase, review-code, pre-push, test-connection
.env                      # 시크릿 (gitignore)
```

## Current Phase
Phase 1: MVP -> /build-phase 참조

## Compact Instructions
압축 시 반드시 포함: 현재 모듈명+함수명 / 마지막 코드 스니펫 / 에러 전문 / 해결한 버그 / 남은 체크리스트 / 미반영 피드백

## Context 관리
- 긴 Bash 출력은 파일로 리다이렉트 후 필요 부분만 Read
- 큰 로그는 grep으로 필터 (터미널에 전체 출력 금지)
- 이전에 읽은 파일 재참조 시 Read로 재확인

## 공통 규칙
- 파괴적 명령 실행 전 반드시 확인
- 전략/로직 변경은 Plan 모드로 계획 먼저
- 동의보다 비판적 피드백 먼저. 모르면 모른다고 말하기
- 추론은 영어, 설명은 한글, 주석은 영어
- 알림은 전부 한국어
