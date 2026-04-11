# LLM Wiki — 파이프라인 아키텍처

> 2026-04-09 확정. Evaluator 검증 11건 반영 (v2).

---

## 1. 시스템 아키텍처

```
llm-wiki/
├── config/
│   ├── settings.yaml              # 전체 설정
│   ├── sources/
│   │   ├── ai.yaml                # AI 소스 목록 (RSS URL, API 설정)
│   │   └── macro.yaml             # Macro 소스 목록
│   └── filter_rules.yaml          # 필터 키워드, 가중치, 임계값
│
├── collector/                     # 자동 수집
│   ├── rss.py                     # RSS 피드 (블로그, 뉴스, arXiv, Import AI)
│   ├── hackernews.py              # HN Firebase API → AI 필터링
│   ├── fred.py                    # FRED API (미국 경제지표)
│   ├── ecos.py                    # 한국은행 ECOS API
│   ├── finnhub.py                 # 경제 캘린더 (FOMC, CPI 등)
│   └── manual.py                  # 수동 인풋 처리 (텔레그램 + 파일)
│
├── filter/
│   ├── topic.py                   # Filter A: AI/Macro 주제 분류
│   └── quality.py                 # Filter B: 품질+신규성 (Wiki 대조)
│
├── wiki/
│   ├── ingest.py                  # 소스 → 요약 페이지 생성
│   ├── indexer.py                 # index.md 중요도순 생성/갱신
│   └── linter.py                  # 정합성 점검
│
├── vault/                         # Obsidian vault (GitHub 레포)
│   ├── ai/
│   │   ├── index.md
│   │   └── (소스 요약 파일들)
│   ├── macro/
│   │   ├── index.md
│   │   └── (소스 요약 파일들)
│   ├── raw/                       # 원본 전문 (VPS에만 보관, .gitignore)
│   ├── index.md                   # 전체 인덱스
│   └── log.md                     # 활동 로그
│
├── data/
│   ├── wiki.db                    # SQLite
│   └── logs/                      # 실행 로그
│
├── bot.py                         # 텔레그램 봇 (상시 가동, systemd)
│                                  #   수동 인풋 → 즉시 처리 (filter→ingest→sync)
│                                  #   알림 전송 (긴급, 주간 리포트)
├── sync.py                        # Git commit + push
├── scheduler.py                   # 메인 스케줄러 (크론, 6시간 간격)
│                                  #   bot.py와 별도 프로세스
├── requirements.txt
├── .env                           # API 키 (gitignore)
├── .gitignore                     # vault/raw/ 제외 (PDF 비대화 방지)
└── CLAUDE.md                      # VPS 코딩 세션용 지침
```

---

## 2. 모듈별 상세

### 2-0. scheduler.py — 메인 스케줄러

```
매 6시간 (크론):
  1. 락 파일 확인 → 있으면 중단 (1시간+ 스테일 → 삭제 + 알림)
  2. 락 파일 생성
  3. 일일 API 호출 카운터 확인 → 300회 초과 시 중단 + 알림
  4. collector 전체 실행 → 새 소스 수집
  5. filter/topic → 주제 분류 (혼합 소스만 LLM, 나머지는 config 고정)
  6. filter/quality → 품질 채점 (통과분만)
  7. wiki/ingest → 요약 생성
  8. wiki/indexer → index.md 증분 갱신 (새 파일만)
  9. sync → Git push
  10. 락 파일 삭제

매주 일요일:
  11. wiki/linter → 정합성 점검
  12. 통계 리포트 → 텔레그램 전송

실행 모드:
  python scheduler.py auto       # 전체 자동 (크론용)
  python scheduler.py collect    # 수집만
  python scheduler.py filter     # 필터만
  python scheduler.py ingest     # 요약+인덱스만
  python scheduler.py sync       # Git push만
  python scheduler.py status     # DB 상태 확인

프로세스 분리:
  scheduler.py — 크론으로 6시간마다 실행 후 종료
  bot.py       — systemd 서비스로 24시간 상시 가동 (별도 프로세스)
                 수동 인풋 수신 시 즉시 filter→ingest→sync 실행
                 크래시 시 systemd가 자동 재시작
```

### 2-1. collector/rss.py — RSS 수집

**입력:** config/sources/ai.yaml, macro.yaml의 RSS URL 목록
**출력:** DB sources 테이블에 새 항목

```python
# 로직
1. 각 피드 URL에 대해 feedparser로 파싱
2. DB에서 guid/link 중복 체크
3. 새 항목만 sources 테이블에 INSERT:
   {
     "source_type": "rss",
     "feed_name": "anthropic-blog",
     "domain": "ai",
     "title": "Introducing Claude 5",
     "url": "https://anthropic.com/blog/...",
     "content": "본문 또는 description",
     "published_at": "2026-04-09T12:00:00Z",
     "status": "collected"
   }

# arXiv RSS 특수 처리
- arXiv RSS는 초록(abstract)만 포함
- status='collected' → Filter 통과 후 전문 다운로드 (ingest 단계)
- arXiv 전문 다운로드: arxiv 패키지 → PDF → PyMuPDF 텍스트 추출
- 추출 실패 시 (수식/이미지 기반 논문): 초록 기반 요약으로 폴백 + 로그 기록

# RSSHub 피드 (Anthropic/OpenAI/DeepMind)
- RSSHub 셀프호스팅 URL: http://localhost:1200/...
- 공식 RSS 없는 블로그를 RSS로 변환
- 같은 rss.py 코드로 처리 (URL만 다름)
- RSSHub 장애 시: 커뮤니티 RSS 폴백 URL로 전환
  - Anthropic: https://raw.githubusercontent.com/taobojlen/anthropic-rss-feed/main/anthropic_news_rss.xml
  - OpenAI: https://raw.githubusercontent.com/capjamesg/openai-blog-rss/main/feed.xml
  - 장애 지속 1일+ → 텔레그램 알림

# Rate limit
- 피드당 최소 3초 간격 (arXiv ToS 준수)
- 전체 수집 1회에 ~5분 소요
```

### 2-2. collector/hackernews.py — Hacker News 수집

**입력:** HN Firebase API
**출력:** DB sources 테이블에 AI 관련 항목

```python
# 로직
1. /v0/topstories.json → 상위 100개 스토리 ID
2. 각 스토리 /v0/item/{id}.json → 제목, URL, 점수
3. 빠른 필터 (API 호출 전 비용 절약):
   - 제목에 AI 키워드 포함? (config/filter_rules.yaml의 키워드 목록)
   - score >= 50? (노이즈 제거)
4. 통과한 것만 DB에 INSERT (story URL 기준 중복 체크, HN URL 아님)
5. 원본 URL이 있으면 본문도 스크래핑 시도 (requests + BeautifulSoup)

# 키워드 목록 (filter_rules.yaml에서 관리)
ai_keywords:
  - LLM, GPT, Claude, Anthropic, OpenAI, DeepMind
  - transformer, agent, reasoning, RLHF
  - AI coding, copilot, cursor, vibe coding
  ...

# Rate limit: 명시적 제한 없음, 15초 간격 권장
```

### 2-3. collector/fred.py — FRED API 수집

**입력:** FRED API (무료, 키 필요)
**출력:** DB sources 테이블에 경제지표 항목

```python
# 로직
1. 관심 시리즈 목록 (config/sources/macro.yaml):
   - GDP, CPI, UNRATE, FEDFUNDS, T10Y2Y, DGS10 등
2. fredapi 패키지로 최신 값 조회
3. DB에서 마지막 저장된 날짜 확인
4. 새 데이터 있으면 INSERT:
   {
     "source_type": "fred",
     "feed_name": "CPI",
     "domain": "macro",
     "title": "CPI March 2026: 3.2% YoY",
     "content": "지표값 + 전월 대비 + 전년 대비 계산",
     "status": "collected"
   }

# Rate limit: 120req/분, 충분
```

### 2-4. collector/ecos.py — 한국은행 ECOS API 수집

**입력:** ECOS API (무료, 키 필요)
**출력:** DB sources 테이블에 한국 경제지표 항목

```python
# 로직
1. 관심 통계표 (config/sources/macro.yaml):
   - 기준금리, 소비자물가지수, GDP, 환율 등
2. ECOS API 호출 → JSON 응답 파싱
3. 새 데이터 INSERT

# 특이사항: ECOS API는 통계표 코드 기반 조회
# 예: 722Y001 (기준금리), 901Y009 (소비자물가지수)
```

### 2-5. collector/finnhub.py — 경제 캘린더 수집

**입력:** Finnhub API (무료 tier)
**출력:** DB sources 테이블에 이벤트 항목

```python
# 로직
1. /calendar/economic 엔드포인트 → 이번 주 경제 이벤트
2. 관심 이벤트 필터:
   - country: US, KR
   - impact: high, medium
   - 예: FOMC, CPI, NFP, 한은 금통위
3. 이벤트 전 알림 (importance=high → 텔레그램 알림)
4. 결과 발표 후 → DB INSERT

# Rate limit: 60req/분, 충분
```

### 2-6. collector/manual.py — 수동 인풋 처리

**입력:** 텔레그램 메시지 또는 vault/raw/ 파일
**출력:** DB sources 테이블에 항목

```python
# 텔레그램 경로 (bot.py에서 호출)
def process_telegram_input(message):
    url = extract_url(message.text)

    if url:
        # X URL 처리
        if "x.com" in url or "twitter.com" in url:
            url = url.replace("x.com", "fxtwitter.com")
            url = url.replace("twitter.com", "fxtwitter.com")
            content = scrape_fxtwitter(url)
        else:
            content = scrape_url(url)

        insert_source(url=url, content=content, source_type="manual")
    else:
        # 텍스트만 온 경우
        insert_source(content=message.text, source_type="manual")

    # 즉시 처리 (크론 대기 안 함)
    run_pipeline_for_source(source_id)  # filter → ingest → sync
    reply("처리 완료. Wiki에 추가됨.")

# 파일 경로
- vault/raw/에 .md 파일이 새로 추가되면
- scheduler가 감지 → DB INSERT → 파이프라인 진입
```

### 2-7. filter/topic.py — Filter A: 주제 분류

**입력:** DB sources (status='collected')
**출력:** status='topic_pass' 또는 'topic_fail' + domain 태깅

```python
# 로직
1. DB에서 status='collected' 조회
2. domain이 이미 확정된 소스는 LLM 스킵:
   - arXiv (cs.AI/CL/LG) → domain='ai', 바로 topic_pass
   - FRED/ECOS/Finnhub/StLouis Fed → domain='macro', 바로 topic_pass
   - Anthropic/OpenAI/DeepMind 블로그 → domain='ai', 바로 topic_pass
   - 수동 인풋 (건재가 직접 넣은 것) → domain='ai' 또는 'macro' 건재에게 물음
3. 혼합 소스만 Claude Haiku 호출:
   - Hacker News (AI/기타 혼재)
   - 기타 일반 RSS
   System: "분류기. 주어진 텍스트가 AI, Macro, 또는 무관한지 판별."
   User: "제목: {title}\n내용: {content[:500]}"
   응답: {"domain": "ai" | "macro" | "irrelevant", "confidence": 0.0~1.0}
4. irrelevant → status='topic_fail'
5. ai/macro + confidence >= threshold → status='topic_pass'

# 비용 절약: 혼합 소스만 LLM 호출 → 하루 ~20건 (HN 위주)
# 나머지 ~130건은 config 기반 자동 분류 → LLM 비용 $0
```

### 2-8. filter/quality.py — Filter B: 품질+신규성 채점

**입력:** DB sources (status='topic_pass')
**출력:** status='quality_pass' 또는 'quality_fail' + importance 태깅

```python
# 로직
1. DB에서 status='topic_pass' 조회
2. 해당 domain의 index.md 로드 (기존 지식 맥락)
3. 각 소스에 대해 Claude Haiku 호출:
   System: "품질 평가기. 기존 Wiki 지식 대비 새로운 가치가 있는지 판별."
   User: """
     기존 Wiki 인덱스:
     {index_md_content}

     새 소스:
     제목: {title}
     내용: {content[:1000]}

     평가:
     1. 신규성 (1-5): 기존 지식에 없는 새 정보?
     2. 중요도 (1-5): 건재의 의사결정/사고에 영향?
     3. 신뢰도 (1-5): 출처 신뢰할 수 있는가?
   """
   응답: {
     "novelty": 4,
     "importance": 3,
     "reliability": 5,
     "average": 4.0,
     "importance_tag": "insight",
     "reason": "스케일링 법칙에 대한 새로운 실험 결과"
   }
4. average >= 3.0 → status='quality_pass'
5. average < 3.0 → status='quality_fail'

# importance_tag 자동 부여:
# - "urgent": 시간 민감 (모델 출시, 지표 발표, 정책 변경)
# - "insight": 새 관점/데이터
# - "connection": 기존 Wiki 주제와 교차
# - "background": 급하지 않지만 참고할 만함

# 하루 ~30건 (80% 탈락 후) × Haiku → 매우 저렴
```

### 2-9. wiki/ingest.py — 요약 생성

**입력:** DB sources (status='quality_pass')
**출력:** vault/{domain}/에 요약 마크다운 파일

```python
# 로직
1. DB에서 status='quality_pass' 조회
2. arXiv 논문이면 전문 다운로드:
   - arxiv 패키지 → PDF 다운로드 → vault/raw/에 저장 (VPS만, .gitignore)
   - PyMuPDF로 텍스트 추출
   - 추출 실패 시: 초록 기반 요약으로 폴백 + 로그 "pdf_extract_failed"
3. Claude Haiku 호출:
   System: "지식 요약기. 핵심 내용을 간결하게 정리."
   User: """
     출처: {source_type} / {feed_name}
     제목: {title}
     URL: {url}
     내용:
     {content}

     요약 형식:
     ---
     title: (제목)
     source: (출처 이름)
     url: (원본 URL)
     date: (발행일)
     domain: (ai/macro)
     importance: (urgent/insight/connection/background)
     ---

     ## 핵심
     (3~5줄 요약)

     ## 새로운 점
     (기존 지식 대비 뭐가 새로운지)
   """
4. vault/{domain}/{slug}.md로 저장
5. DB status='ingested' + 파일 경로 기록

# 파일명 규칙: {date}_{slug}.md
# 예: 2026-04-09_claude-5-announcement.md
```

### 2-10. wiki/indexer.py — 인덱스 생성/갱신

**입력:** vault/{domain}/ 내 모든 요약 파일
**출력:** 갱신된 index.md

```python
# 로직 — 증분 업데이트 (매번 전체 스캔하지 않음)
1. DB에서 status='ingested' AND indexed=false인 파일만 조회
2. 기존 index.md 로드
3. 새 파일 각각에 대해:
   a. 프론트매터에서 importance, date 추출
   b. 기존 그룹 중 매칭되는 주제 있으면 → 해당 그룹에 추가
   c. 매칭 안 되면 → Claude Haiku 호출: "이 소스의 주제 그룹 제안"
      → 새 그룹 생성 또는 기존 그룹에 매칭
4. importance 기준 정렬:
   - 1차: importance (urgent > insight > connection > background)
   - 2차: date (최신순)
5. 그룹별 "핵심 흐름" 한 줄: 새 소스 추가된 그룹만 재생성
6. index.md 덮어쓰기:

   # {Domain} 인덱스
   최종 갱신: {now}

   ## 긴급
   - [제목](파일.md) — 한줄 요약

   ## 주제별

   ### {주제} ({N}건, 최신 {date})
   핵심 흐름: ...
   - [제목](파일.md) ⭐ — 한줄 요약
   - [제목](파일.md) — 한줄 요약

   ## 배경
   - ...

7. 전체 인덱스 (vault/index.md)도 동일하게 갱신
8. DB에서 indexed=true로 업데이트

# 오래된 항목 처리:
# - 30일 지난 항목 → "아카이브" 섹션으로 이동
# - 90일 지난 항목 → index에서 제거 (파일은 유지)

# LLM 호출 최소화:
# - 기존 그룹 매칭은 키워드 기반 (LLM 불필요)
# - 새 그룹 생성 시만 Haiku 호출
# - 핵심 흐름 재생성은 변경된 그룹만
```

### 2-11. wiki/linter.py — 정합성 점검

**입력:** vault/ 전체
**출력:** 점검 리포트

```python
# 주간 점검 항목
1. 깨진 링크: index.md에 링크된 파일이 실제 존재하는지
2. 고아 파일: index.md에 없는 요약 파일
3. 중복 소스: 같은 URL이 여러 요약 파일에 있는지
4. 프론트매터 누락: title, date, importance 빠진 파일
5. index.md 정렬 확인: importance 순서 맞는지

# 결과 → 텔레그램 알림 + log.md 기록
```

### 2-12. bot.py — 텔레그램 봇

```python
# 명령어
/add [URL 또는 텍스트]  → manual.py → 즉시 filter→ingest→sync (크론 대기 안 함)
/status                → 오늘 수집/필터/인제스트 건수
/recent                → 최근 Wiki 추가 5건
/stats                 → 주간 통계

# 자동 알림
- 긴급(urgent) 소스 발견 시 즉시 알림
- 주간 리포트: 수집 N건 → 필터 통과 N건 → Wiki 추가 N건
- RSSHub 장애 1일+ 지속 시 알림
- 일일 API 호출 한도 초과 시 알림
- 스테일 락 (1시간+) 감지 시 알림

# 수동 인풋 처리
텍스트/URL 수신 → manual.process_telegram_input() → 즉시 파이프라인 실행
X URL → fxtwitter 자동 변환 → 내용 추출

# 프로세스 관리
- systemd 서비스로 24시간 상시 가동
- 크래시 시 자동 재시작 (RestartSec=10)
- scheduler.py(크론)와 별도 프로세스
```

### 2-13. sync.py — Git 동기화

```python
# 로직
1. vault/ 디렉토리에서 변경 감지 (git status)
2. 변경 있으면:
   git add vault/
   git commit -m "wiki: {date} 업데이트 (+{new}건, ~{updated}건)"
   git push origin main

# scheduler.py 마지막 단계에서 호출
# 변경 없으면 commit/push 스킵
```

---

## 3. 데이터베이스 스키마 (SQLite)

```sql
-- 수집된 소스 추적
CREATE TABLE sources (
  id INTEGER PRIMARY KEY,
  source_type TEXT NOT NULL,          -- rss / hackernews / fred / ecos / finnhub / manual
  feed_name TEXT,                     -- 피드 이름 (anthropic-blog, CPI, ...)
  domain TEXT,                        -- ai / macro / null (분류 전)
  title TEXT NOT NULL,
  url TEXT,
  story_url TEXT,                     -- HN의 경우 원본 URL (중복 체크용)
  content TEXT,                       -- 본문 또는 초록
  published_at DATETIME,
  collected_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  status TEXT DEFAULT 'collected',    -- collected → topic_pass/fail → quality_pass/fail → ingested
  importance TEXT,                    -- urgent / insight / connection / background
  filter_a_result TEXT,               -- JSON (domain, confidence)
  filter_b_result TEXT,               -- JSON (novelty, importance, reliability, average, reason)
  vault_path TEXT,                    -- 생성된 요약 파일 경로
  indexed BOOLEAN DEFAULT false,      -- indexer.py 처리 완료 여부
  UNIQUE(url),                        -- 같은 URL 중복 수집 방지
  UNIQUE(story_url)                   -- HN 원본 URL 기준 중복 방지
);

-- 필터 통계 (튜닝용)
CREATE TABLE filter_stats (
  id INTEGER PRIMARY KEY,
  date DATE NOT NULL,
  total_collected INTEGER DEFAULT 0,
  topic_passed INTEGER DEFAULT 0,
  topic_failed INTEGER DEFAULT 0,
  quality_passed INTEGER DEFAULT 0,
  quality_failed INTEGER DEFAULT 0,
  ingested INTEGER DEFAULT 0,
  UNIQUE(date)
);

-- 시스템 로그
CREATE TABLE system_log (
  id INTEGER PRIMARY KEY,
  event TEXT NOT NULL,                -- collect / filter / ingest / sync / lint / error
  details TEXT,                       -- JSON
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## 3.5. 안전장치

### 비용/한도
```
일일 Haiku 호출 한도:  300회 (Filter A ~20 + Filter B ~30 + Ingest ~15 + Indexer ~5 = 여유 있음)
초과 시:             파이프라인 중단 + 텔레그램 알림
카운터:              DB system_log에서 당일 LLM 호출 건수 집계
```

### 장애 대응
```
Claude API 실패:     지수 백오프 (1s → 2s → 4s → 8s), 최대 5회 재시도
RSS 피드 실패:       해당 피드 스킵, 다음 크론에서 재시도
RSSHub 장애:        커뮤니티 RSS 폴백 URL로 전환. 1일+ 지속 시 알림
FRED/ECOS API 실패:  스킵 + 로그. 경제지표는 지연돼도 소실 안 됨
arXiv PDF 추출 실패: 초록 기반 요약으로 폴백
Git push 실패:      로컬 commit은 유지, 다음 크론에서 재push
```

### 동시 실행 방지
```
파일 기반 락: 파이프라인 시작 시 락 파일 생성
락 존재하면 실행 안 함 (이전 실행 미완료)
락이 1시간+ 유지 → 스테일 락으로 판단 → 삭제 + 텔레그램 알림
bot.py의 즉시 처리도 동일한 락 사용 (scheduler와 충돌 방지)
```

### 알림 (텔레그램 — 한국어)
```
📥 수동 인풋 처리 완료: "Wiki 추가: {title}\n{importance_tag}"
🔴 긴급 소스 발견:     "긴급: {title}\n{한줄 요약}"
📊 주간 리포트:        "수집 {N}건 → 필터 {N}건 → Wiki {N}건"
⚠️ 장애:              "RSSHub 장애 / API 한도 초과 / 스테일 락"
```

---

## 4. 설정 파일

```yaml
# config/settings.yaml

scheduler:
  interval_hours: 6                    # 수집 주기
  timezone: "Asia/Seoul"

filter:
  topic_confidence_threshold: 0.5      # Filter A 최소 confidence
  quality_score_threshold: 3.0         # Filter B 최소 average
  max_content_length_topic: 500        # Filter A에 보낼 content 길이
  max_content_length_quality: 1000     # Filter B에 보낼 content 길이

wiki:
  archive_after_days: 30               # index에서 아카이브로 이동
  remove_from_index_after_days: 90     # index에서 제거
  max_index_items: 50                  # index.md 최대 항목 수

claude:
  model: "claude-haiku-4-5-20251001"   # 전부 Haiku
  # ANTHROPIC_API_KEY는 환경 변수

hackernews:
  min_score: 50                        # 최소 점수
  top_n: 100                           # 상위 N개만 확인

arxiv:
  categories: ["cs.AI", "cs.CL", "cs.LG"]
  full_text_on_pass: true              # Filter 통과 후 전문 다운로드

sync:
  auto_push: true
  remote: "origin"
  branch: "main"

telegram:
  # BOT_TOKEN, CHAT_ID는 환경 변수
  notify_on_urgent: true
  weekly_report: true
```

```yaml
# config/sources/ai.yaml

rss_feeds:
  - name: "arxiv-cs-ai-cl-lg"
    url: "https://rss.arxiv.org/rss/cs.AI+cs.CL+cs.LG"
    type: "arxiv"

  - name: "anthropic-blog"
    url: "http://localhost:1200/anthropic/blog"    # RSSHub
    type: "blog"

  - name: "openai-blog"
    url: "http://localhost:1200/openai/blog"       # RSSHub
    type: "blog"

  - name: "deepmind-blog"
    url: "https://deepmind.google/blog/rss.xml"    # 공식
    type: "blog"

  - name: "import-ai"
    url: "https://importai.substack.com/feed"
    type: "newsletter"

hackernews:
  enabled: true
  keywords_file: "config/filter_rules.yaml"
```

```yaml
# config/sources/macro.yaml

fred:
  series:
    - id: "GDP"
      name: "미국 GDP"
    - id: "CPIAUCSL"
      name: "미국 CPI"
    - id: "UNRATE"
      name: "미국 실업률"
    - id: "FEDFUNDS"
      name: "연방기금금리"
    - id: "T10Y2Y"
      name: "10Y-2Y 스프레드"
    - id: "DGS10"
      name: "10년 국채금리"

ecos:
  series:
    - code: "722Y001"
      name: "기준금리"
    - code: "901Y009"
      name: "소비자물가지수"

finnhub:
  countries: ["US", "KR"]
  min_impact: "medium"

rss_feeds:
  - name: "stlouis-fed"
    url: "https://www.stlouisfed.org/rss"
    type: "central_bank"
```

```yaml
# config/filter_rules.yaml

ai_keywords:
  high:    # 거의 확실히 AI
    - LLM, GPT, Claude, Anthropic, OpenAI, DeepMind, Google AI
    - transformer, attention mechanism, RLHF, DPO, RLAIF
    - AI agent, agentic, tool use, function calling
    - AI coding, copilot, cursor, windsurf, aider, claude code
    - scaling law, emergent, reasoning, chain of thought
    - diffusion model, multimodal, vision language model
  medium:  # 맥락 따라 다름
    - neural network, deep learning, machine learning
    - fine-tuning, training, inference, benchmark
    - AI safety, alignment, interpretability
    - robotics, autonomous, self-driving
  low:     # 키워드만으로 판단 어려움 → Filter A에서 판별
    - model, architecture, optimization, performance

macro_keywords:
  high:
    - FOMC, Fed, 연준, 한국은행, 금통위
    - CPI, GDP, NFP, unemployment, inflation
    - interest rate, 기준금리, 국채, yield curve
    - recession, quantitative easing, tightening
  medium:
    - fiscal policy, monetary policy, 재정정책, 통화정책
    - trade deficit, current account, 무역수지, 경상수지
    - housing market, real estate, 부동산
```

---

## 5. 환경 변수 (.env, gitignore)

```bash
# Claude API
ANTHROPIC_API_KEY=sk-ant-...

# FRED
FRED_API_KEY=...

# 한국은행 ECOS
ECOS_API_KEY=...

# Finnhub
FINNHUB_API_KEY=...

# Telegram
TELEGRAM_BOT_TOKEN=123456:ABC-...
TELEGRAM_CHAT_ID=123456789

# GitHub (sync용)
# SSH 키 또는 Personal Access Token으로 인증
```

---

## 6. 의존성

```txt
# requirements.txt

# Claude API
anthropic>=0.40

# RSS
feedparser>=6.0

# HTTP
requests>=2.31
beautifulsoup4>=4.12       # 웹 스크래핑 (HN 원문, fxtwitter)

# arXiv
arxiv>=2.1                 # arXiv API 래퍼
PyMuPDF>=1.24              # PDF → 텍스트 추출

# 경제 데이터
fredapi>=0.5               # FRED API

# 텔레그램
python-telegram-bot>=21.0

# 설정
pyyaml>=6.0
python-dotenv>=1.0

# Git (sync)
gitpython>=3.1             # Git 자동화

# 시스템
schedule>=1.2              # 인프로세스 스케줄러 (크론 보조)
```

---

## 7. 크론 설정 (VPS)

```bash
# SQLite 백업 (매일 05:50 UTC)
50 5 * * * cp /home/bugi/llm-wiki/data/wiki.db /home/bugi/llm-wiki/data/wiki.db.bak

# 메인 수집+필터+인제스트+동기화 (6시간 간격: 00, 06, 12, 18 UTC)
0 0,6,12,18 * * * cd /home/bugi/llm-wiki && python scheduler.py auto >> data/logs/cron.log 2>&1

# 주간 점검 (일요일 04:00 UTC)
0 4 * * 0 cd /home/bugi/llm-wiki && python -m wiki.linter >> data/logs/lint.log 2>&1
```

```ini
# /etc/systemd/system/llm-wiki-bot.service
[Unit]
Description=LLM Wiki Telegram Bot
After=network.target

[Service]
User=bugi
WorkingDirectory=/home/bugi/llm-wiki
ExecStart=/usr/bin/python3 bot.py
Restart=always
RestartSec=10
EnvironmentFile=/home/bugi/llm-wiki/.env

[Install]
WantedBy=multi-user.target
```

```gitignore
# .gitignore (vault 레포)
vault/raw/          # PDF 원본 — VPS에만 보관, Git에 안 올림
data/
.env
__pycache__/
*.pyc
```

---

## 8. 개발 순서

```
Phase 1: MVP — 첫 자동 수집 + Wiki 페이지
  1. DB 스키마 생성 (SQLite)
  2. collector/rss.py — arXiv + DeepMind RSS 수집
  3. filter/topic.py — 주제 분류 (Haiku)
  4. filter/quality.py — 품질 채점 (Haiku)
  5. wiki/ingest.py — 요약 생성
  6. wiki/indexer.py — index.md 생성
  7. sync.py — Git push
  → 첫 자동 수집 + Wiki 페이지 생성 + Obsidian 확인

Phase 2: 소스 확장
  8. collector/hackernews.py — HN 수집
  9. RSSHub 셀프호스팅 설치 + Anthropic/OpenAI 피드 추가
  10. collector/fred.py — FRED 수집
  11. collector/ecos.py — ECOS 수집
  12. collector/finnhub.py — 경제 캘린더
  → 전체 소스 가동

Phase 3: 수동 인풋 + 알림
  13. bot.py — 텔레그램 봇
  14. collector/manual.py — 수동 인풋 (X URL fxtwitter 포함)
  → 건재 수동 인풋 가능

Phase 4: 안정화
  15. wiki/linter.py — 정합성 점검
  16. 주간 리포트 (텔레그램)
  17. 필터 튜닝 (건재 사용 패턴 기반)
  18. scheduler.py 크론 등록
  → 자동 운영

Phase 5: 확장 (나중에)
  19. YouTube 자막 수집기
  20. Phase 2 소스 추가
  21. 뉴스 봇 합류
```

---

## 관련 파일
- [[00_project-brief]] — 프로젝트 브리프
