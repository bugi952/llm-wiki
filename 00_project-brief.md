# LLM Wiki — 프로젝트 브리프

> 2026-04-09 설계 시작

## 개요
AI/Macro 분야 정보를 자동 수집 → 1차 필터링 → Wiki에 정리 → 건재가 Obsidian으로 열람 → 좋은 것만 Think Tank에 수동 intake.

## 왜 만드는가
- Think Tank에 지식 인풋이 적음 — 건재가 수동으로 소스를 찾아 넣어야 해서
- 좋은 인풋을 어디서 찾을지도 모름
- Think Tank을 깨끗한 사고 공간으로 유지하면서, 대량의 raw data는 별도 시스템에서 선별

## 핵심 설계 결정

### 역할 분리
```
LLM Wiki = 대량 수집 + 1차 선별 + 정리 (파이프라인)
Think Tank = 2차 필터 + 깊은 사고 + 의사결정 (사고 공간)
```
Wiki가 자체 지식 베이스로 비대해지면 안 됨. Think Tank과 중복 금지.

### 도메인
- **AI** — 논문, 블로그, 커뮤니티
- **Macro** — 미국/한국 경제지표, 연준/한국은행 동향

### Wiki 구조: 플랫 + 스마트 인덱스
entity/concept 페이지 없음. 깊은 축적은 Think Tank domains/가 함.

**왜 플랫인가 (검토한 대안과 기각 이유):**
- Karpathy 원문은 entities/concepts/sources 3분류 제안
- 3분류 검토 결과: entity/concept 페이지가 Think Tank의 domains/와 중복됨. 두 곳에서 같은 주제를 관리하면 어디가 맞는 정보인지 모호해짐
- 2분류(sources + wiki)도 같은 문제 발생
- **결론: Wiki는 "선별과 정렬"에 집중. 깊은 축적/연결은 Think Tank이 함. index.md가 entity/concept의 역할을 흡수 (주제별 그룹핑 + 2~3줄 종합)**
```
vault/
  ai/
    index.md              ← 중요도순 + 주제별 그룹 (건재가 여기를 봄)
    claude-5-발표.md       ← 개별 소스 요약 (1파일 = 1소스)
    arxiv-agent-survey.md
    ...
  macro/
    index.md
    fomc-april-2026.md
    ...
  raw/                    ← 원본 전문 (참고용, 불변)
  index.md                ← 전체 인덱스 (통합 뷰)
  log.md                  ← 활동 로그
```

### index.md 구조
```markdown
# AI 인덱스

## 긴급
- [Claude 5 발표](claude-5-발표.md) — 성능 2배, 가격 인하

## 주제별

### Agent Coding (5건, 최신 4/9)
핵심 흐름: 에이전틱 코딩이 IDE 기본 기능으로 자리잡는 중
- [Agent Survey 논문](arxiv-agent-survey.md) ⭐
- [Anthropic Tool Use](anthropic-tool-use-update.md)
- ...

## 배경 (급하지 않음)
- ...
```

### 중요도 태깅
- **긴급** — 시간에 민감 (새 모델 출시, 정책 변경, 지표 발표)
- **인사이트** — 기존 지식에 새 관점 추가
- **연결** — Wiki 내 다른 페이지와 교차점 많음
- **배경** — 알아두면 좋지만 당장 행동 불필요

## 수집 소스 (전부 무료)

### Phase 1

**AI:**
| 소스 | 방식 | 빈도 | 안정성 |
|------|------|------|--------|
| arXiv (cs.AI + cs.CL + cs.LG) | 공식 RSS | 평일 1회 | 높음 |
| Hacker News | 공식 Firebase API | 일 수회 | 높음 |
| Anthropic/OpenAI/DeepMind 블로그 | RSSHub (셀프호스팅) | 실시간 | 중간 |
| Import AI 뉴스레터 | RSS | 주 1회 | 높음 |

**Macro:**
| 소스 | 방식 | 빈도 | 안정성 |
|------|------|------|--------|
| FRED | 공식 API (120req/분, 무료) | 지표 발표 시 | 높음 |
| 한국은행 ECOS | 공식 API (무료) | 발표 시 | 높음 |
| St. Louis Fed | 공식 RSS | 실시간 | 높음 |
| Finnhub 경제 캘린더 | API (60req/분, 무료 tier) | 일 1회 | 높음 |

### Phase 2 (안정화 후 추가)
- youtube-transcript-api (Karpathy 등 유튜브 자막)
- DBnomics (글로벌 경제 데이터)
- 추가 RSS (MIT Tech Review, MarkTechPost 등)
- 뉴스 봇 합류 (텔레그램 속보 알림 기능)

### 제외
- X (크롤링 불안정 + 비용. 나중에 재검토)

## 필터링

```
수집된 원문 (하루 수십~수백 건)
    ↓
[Filter A] 주제 분류 — "AI야? Macro야? 무관?"
    → 저비용 LLM. 무관한 거 80% 탈락
    ↓
[Filter B] 품질+신규성 — "이미 아는 내용? 새 인사이트?"
    → LLM이 Wiki 기존 지식 대조. 1~5점. 3점+ 통과
    ↓
Wiki 저장 + 중요도 태깅 + index.md 갱신
```

처음엔 필터 느슨하게 → 건재가 뭘 가져가는지 보며 조임.

## Obsidian 연동

```
VPS (봇) → GitHub push (자동)
    ↓
PC: Obsidian Git 플러그인 → 자동 pull
모바일: GitHub 앱/웹으로 읽기
```

## Think Tank 전달

건재가 수동. Obsidian에서 index.md 확인 → 좋은 소스 발견 → Think Tank에서 /intake로 가져옴.
Wiki가 직접 Think Tank에 쓰지 않음. 건재 판단이 항상 최종 게이트.

## 기술 스택
```
호스팅:      BUGIcodes 블로그와 같은 VPS (추가 비용 없음)
런타임:      Python
LLM:        Claude API (필터링용)
저장소:      마크다운 파일 (Obsidian vault)
동기화:      Git → GitHub
DB:         SQLite (소스 추적, 필터 결과, 통계)
```

## 시스템 아키텍처
```
llm-wiki/
├── config/
│   ├── settings.yaml
│   └── sources/
│       ├── ai.yaml           # AI 소스 목록 (RSS URL 등)
│       └── macro.yaml        # Macro 소스 목록
│
├── collector/                 # 자동 수집
│   ├── rss.py                # RSS 피드 (블로그, 뉴스, arXiv)
│   ├── hackernews.py         # HN API → AI 필터링
│   ├── fred.py               # FRED API (미국 경제지표)
│   ├── ecos.py               # 한국은행 ECOS API
│   ├── finnhub.py            # 경제 캘린더
│   └── manual.py             # 수동 인풋 처리
│
├── filter/
│   ├── topic.py              # Filter A: 주제 분류
│   └── quality.py            # Filter B: 품질+신규성 (Wiki 대조)
│
├── wiki/
│   ├── ingest.py             # 소스 → 요약 페이지 생성
│   ├── indexer.py            # index.md 중요도순 생성/갱신
│   └── linter.py             # 정합성 점검
│
├── vault/                     # Obsidian vault (마크다운 저장소)
│   ├── ai/
│   │   ├── index.md
│   │   └── (소스 요약 파일들)
│   ├── macro/
│   │   ├── index.md
│   │   └── (소스 요약 파일들)
│   ├── raw/                  # 원본 전문
│   ├── index.md              # 전체 인덱스
│   └── log.md
│
├── data/
│   ├── wiki.db               # SQLite
│   └── logs/
│
├── sync.py                    # Git commit + push (크론)
├── scheduler.py               # 메인 스케줄러
├── requirements.txt
└── CLAUDE.md
```

## 블로그(BUGIcodes)와의 관계
- 같은 VPS에서 구동, 인프라 비용 추가 없음
- 코드베이스는 별도 (llm-wiki/ vs bugicodes-bot/)
- 뉴스 봇은 장기적으로 Wiki에 합류 (텔레그램 속보 알림 레이어)

## 전체 흐름
```
[크론 — VPS]
  collector → 소스 수집 (RSS/API/수동)
       ↓
  filter → 주제 분류 → 품질 채점
       ↓ (통과분만)
  wiki/ingest → 요약 작성 + index.md 갱신
       ↓
  sync → Git push → GitHub
       ↓
[건재]
  PC: Obsidian → 자동 pull → index.md 열람
  모바일: GitHub 앱/웹으로 읽기
       ↓ (좋은 거 발견)
  Think Tank → /intake → domains/ 저장
```

## 진행 단계
```
Phase 1: 설계 (Think Tank에서) ✅
  [x] 프로젝트 브리프 (00_project-brief.md)
  [x] 파이프라인 아키텍처 (01_pipeline-architecture.md, Evaluator 검증 11건 반영)
  [x] CLAUDE.md (02_claude-md.md)

Phase 2: 인프라 (VPS에서)
  [ ] llm-wiki/ 폴더 생성
  [ ] GitHub 레포 생성 + Obsidian Git 설정
  [ ] RSSHub 셀프호스팅 설치

Phase 3: MVP (VPS에서 코딩)
  [ ] collector — RSS + HN 수집
  [ ] filter — 주제 분류 + 품질 필터
  [ ] wiki/ingest — 요약 생성
  [ ] wiki/indexer — index.md 생성
  [ ] sync — Git push 자동화
  → 첫 자동 수집 + Wiki 페이지 생성 테스트

Phase 4: 확장
  [ ] FRED/ECOS/Finnhub 수집기 추가
  [ ] wiki/linter 추가
  [ ] 필터 튜닝 (건재 사용 패턴 기반)

Phase 5: 안정화
  [ ] Phase 2 소스 추가 (YouTube 등)
  [ ] 뉴스 봇 합류 검토
```

## 비용
```
인프라:      $0 (기존 VPS 공유)
API:        $0 (전부 무료 tier)
LLM 필터링:  Claude API 비용 (소량, 하루 수십 호출)
동기화:      $0 (GitHub 무료)
---
총:         Claude API 비용만 (월 몇 달러 수준)
```

## Karpathy 원문과의 차이
| | Karpathy Wiki | 이 프로젝트 |
|---|---|---|
| 소스 수집 | 수동 | **자동** (크롤러+API) |
| 필터링 | 없음 (전부 수용) | **2단계 필터** |
| Wiki 구조 | entities/concepts/sources | **플랫 + 스마트 인덱스** |
| 깊은 축적 | Wiki 자체에서 | **Think Tank에서** (Wiki는 선별 역할) |
| 열람 | 로컬 | **Obsidian + GitHub 모바일** |

## 설계 과정에서 버린 대안들 (코딩 시 임의 변경 금지)

| 검토한 대안 | 기각 이유 |
|---|---|
| entity/concept 페이지 | Think Tank domains/와 중복. 두 곳에서 같은 지식 관리 불가 |
| Think Tank 관련성 필드 (ingest 요약에 포함) | Wiki는 Think Tank 파일에 접근 불가. 항상 빈 칸 또는 헛소리 |
| 전부 LLM으로 주제 분류 (Filter A) | arXiv/FRED 등 도메인 고정 소스에 LLM 불필요. 돈 낭비 |
| indexer 전체 스캔 | 파일 100개+ 시 매번 전체를 LLM에 넘기면 비용+불안정. 증분만 |
| vault/raw/ Git에 포함 | arXiv PDF 쌓이면 레포 수백MB. Obsidian 동기화 느려짐 |
| 수동 인풋 크론 대기 | 건재가 텔레그램으로 던졌는데 6시간 대기는 UX 문제 |
| Sonnet으로 필터/요약 | 건재가 최종 게이트. Haiku로 충분. 비용 우선 |
| 자동 Think Tank 전달 | Wiki가 직접 Think Tank에 쓰면 건재 판단 게이트 소실 |
| X 자동 수집 | API $200/월, 크롤링 불안정. 텔레그램 수동 인풋 + fxtwitter로 대체 |

## 관련 파일
- [[01_pipeline-architecture]] — 파이프라인 아키텍처 (모듈별 스펙, DB 스키마, 설정, 크론)
- [[02_claude-md]] — VPS 코딩 세션용 CLAUDE.md
