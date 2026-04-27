---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Agent Memory

## 정의


## 주요 발전
- **2026-03-24**: 로봇의 불변 서브네트워크가 장기 기억 보존 메커니즘으로 기능하며 학습 안정성 제공 [(원문)](https://arxiv.org/abs/2603.24350)
- **2026-01-14**: Chain-of-Memory (CoM): lightweight construction + dynamic evolution으로 retrieved fragments를 coherent inference paths로 조직화 [(원문)](https://arxiv.org/abs/2601.14287)
- **2026-04-26**: Memanto: typed schema + temporal versioning으로 knowledge graph 오버헤드 제거 가능 [(원문)](https://arxiv.org/abs/2604.22085)
- **2026-04-25**: Claude/ChatGPT 스타일의 persistent memory를 제공하는 오픈소스 메모리 계층 솔루션 등장 [(원문)](https://news.ycombinator.com/item?id=47897790)
- **2026-04-25**: LLM 에이전트가 Markdown+Git 버전 관리되는 Wiki를 실시간 갱신하는 시스템 구현 [(원문)](https://news.ycombinator.com/item?id=47899844)
- **2025-09-22**: 분산 환경에서 라우팅 트리상 통신으로 로컬 AM 최적화, sublinear regret 달성 [(원문)](https://arxiv.org/abs/2509.22321)
- **2026-04-21**: Hierarchical structure + event-level bindings + periodic semantic consolidation으로 flat memory의 효율성과 graph memory의 reasoning 능력을 결합 [(원문)](https://arxiv.org/abs/2604.21748)
- **2026-04-21**: Thompson Sampling 기반 memory retrieval 정책 선택 및 failure pattern 진단을 통한 long-horizon learning [(원문)](https://arxiv.org/abs/2604.21725)
- **2026-04-21**: MemPalace는 2026년 4월 공개된 spatial metaphor 기반 LLM 메모리 시스템으로, ChromaDB 활용 시 96.6% Recall@5 달성 [(원문)](https://arxiv.org/abs/2604.21284)
- **2026-04-24**: EngramaBench: 5개 페르소나, 100개 다중 세션 대화, 150개 쿼리로 장기 메모리 평가, cross-space reasoning 0.6532 달성 [(원문)](https://arxiv.org/abs/2604.21229)
- **2026-04-24**: LLM의 다중 엔티티 추적: 현재 슬롯은 직접 추론, 이전 슬롯은 관계적 추론(귀납, 충돌 감지)에 활용되는 기능적 분업 [(원문)](https://arxiv.org/abs/2604.21139)
- **2026-04-24**: 에이전트가 에피소드 간 구조화된 스킬 검색으로 장시간 의사결정 일관성 향상 [(원문)](https://arxiv.org/abs/2604.20987)
- **2026-04-20**: SCM은 신경과학 기반 메모리 아키텍처로 working memory, multi-dimensional importance tagging, sleep consolidation(NREM/REM), value-based forgetting, self-model introspection 구현. 10턴 대화에서 완벽한 recall + 메모리 잡음 90.9% 감소 [(원문)](https://arxiv.org/abs/2604.20943)
- **2026-04-20**: OpenAI Codex, Chronicle 메모리 기능 공개 (화면 정보 기반 자동 맥락 저장, 반복 설명 제거) [(원문)](https://www.aitimes.com/news/articleView.html?idxno=209540)
- **2026-04-21**: Task 유형에 따라 parametric memory와 context 의존도가 상이. 설명/재반복 전략은 context 의존 task에만 효과적 (2026-04-21) [(원문)](https://arxiv.org/abs/2506.06485)
- **2026-04-21**: MIRROR: reconstructive episodic memory로 매 턴 완전히 재구성되는 기억 메커니즘 (누적 저장 제거) [(원문)](https://arxiv.org/abs/2506.00430)
- **2026-04-21**: Vision-Language Navigation에서 상태 드리프트: (1) 완료된 부분목표 미식별(Progress Drift), (2) 방문 장소 이력 표현 열화(Memory Drift) [(원문)](https://arxiv.org/abs/2604.17473)
- **2026-04-21**: Long-term memory는 이미지 내 은폐 트리거(sleeper agent)에 의한 포이즈닝에 취약 [(원문)](https://arxiv.org/abs/2604.16966)
- **2026-04-21**: Self-evolving memory + 200+ import-to-package 매핑으로 신뢰도 계층화 구현, in-session 학습 최적화 [(원문)](https://arxiv.org/abs/2604.16941)
- **2026-04-21**: Memory lifecycle security: Write, Store, Retrieve, Execute, Share, Forget/Rollback 각 단계의 integrity/confidentiality/availability/governance [(원문)](https://arxiv.org/abs/2604.16548)
- **2026-04-21**: BrainMem은 working, episodic, semantic memory 계층을 통해 에이전트 플래너의 장기 의존성 처리 및 경험 재사용 개선 [(원문)](https://arxiv.org/abs/2604.16331)
- **2026-04-21**: 자연언어 증거 요약으로 context 효율화, 계층적 shrinkage로 극값 예측 보정 [(원문)](https://arxiv.org/abs/2604.18576)
- **2026-04-21**: WorldDB: 내용 주소 기반 불변 노드와 쓰기 시간 프로그램으로 영속 메모리 실현 [(원문)](https://arxiv.org/abs/2604.18478)
- **2026-04-21**: HiGMem: 2계층 event-turn 메모리로 LLM-guided retrieval 수행, 컨텍스트 비용 감소 및 정확도 향상 [(원문)](https://arxiv.org/abs/2604.18349)
- **2026-04-21**: Training-free 메모리 제어: 불확실성 기반 라우팅 + 신뢰도 선택으로 SVAMP +7.0, ASDiv +7.67 개선 [(원문)](https://arxiv.org/abs/2604.18206)
- **2026-04-20**: 도구 호출 맥락화: 선택 자체보다는 선택의 이유(왜)를 메모리에 저장. 명확한 선호도 역사가 에이전트 개인화의 필수 조건 [(원문)](https://arxiv.org/abs/2604.17886)
- **2026-04-21**: 2026-04: PDDL 기반 신념 추론으로 state tracking 신뢰성 강화, implicit 상태 추적의 한계 극복 [(원문)](https://arxiv.org/abs/2604.17819)
- **2026-04-21**: AnchorMem: 원본 컨텍스트 보존하며 atomic fact 앵커로 검색 효율성 개선 [(원문)](https://arxiv.org/abs/2604.17377)
- **2026-04-21**: Knows: YAML 기반 사이드카로 연구 논문의 주장, 증거, 출처를 구조화하여 LLM 에이전트 직접 처리 가능 [(원문)](https://arxiv.org/abs/2604.17309)
- **2026-04-21**: 구조화된 정신 상태 그래프로 360명의 모의 사용자 선호도 변화의 근거(provenance) 제공하여 모델 실패 진단 가능 [(원문)](https://arxiv.org/abs/2604.17283)
- **2026-04-21**: Continuity Layer 개념 제안: 세션 종료 시 메모리 손실 문제를 해결하는 아키텍처 필수 요소 [(원문)](https://arxiv.org/abs/2604.17273)
- **2026-04-21**: EVU(Estimate-Verify-Update) 메커니즘으로 관찰-기존 신념 간 불일치 능동 관리 가능 [(원문)](https://arxiv.org/abs/2604.17252)
- **2026-04-21**: Hierarchical on-demand memory로 기본값은 high-level view만 표시, 필요시 상세 정보 조회. Context 내 의사결정 관련 정보 밀도 최대화 (arXiv:2604.17091) [(원문)](https://arxiv.org/abs/2604.17091)
- **2026-04-21**: Hebbian 학습으로 co-activation 패턴 기반 메모리 그래프 진화 [(원문)](https://arxiv.org/abs/2604.16839)
- **2026-04-21**: 메모리 항목의 신뢰도(confidence)·강도(strength)를 명시적으로 모델링하여 불확실한 정보 과다 보유 문제 해결 [(원문)](https://arxiv.org/abs/2604.16774)
- **2026-04-21**: LLM 메모리를 생명주기 기반으로 관리: transient(일시) → working(작업) → durable(영구) 3단계 [(원문)](https://arxiv.org/abs/2604.16774)
- **2026-04-21**: 음성 에이전트는 사용자 중단 중 작업 상태 업데이트에 실패하는 경향 (EchoChain 벤치마크) [(원문)](https://arxiv.org/abs/2604.16456)
- **2026-04-20**: Non-linear dialogue의 topic shift 추적을 위한 tree 기반 context 메모리 (arXiv:2604.05552) [(원문)](https://arxiv.org/abs/2604.05552)
- **2026-04-20**: 파일시스템 기반 hierarchical knowledge base로 context window 초과 메모리 지속 가능, 다중 세션 협력 [(원문)](https://arxiv.org/abs/2602.01566)
- **2026-04-20**: 도구 의존성을 function calling 시연으로부터 모델링하여 계획 전개 시 적응적 검색 실현 [(원문)](https://arxiv.org/abs/2512.17052)
- **2026-04-20**: 경험 압축 스펙트럼: 에피소딕(5-20배) → 절차적 기술(50-500배) → 선언적 규칙(1000배+). 장기 배포에서 컨텍스트 소비와 검색 지연 감소 [(원문)](https://arxiv.org/abs/2604.15877)
- **2026-04-20**: MemEvoBench: 에이전트 메모리의 장기 안전성 평가 (7개 도메인, 36가지 위험 유형) [(원문)](https://arxiv.org/abs/2604.15774)
- **2026-04-20**: 장기/단기 대화 메모리 + 프로젝트 제안으로 과학 협업 맥락 유지 [(원문)](https://arxiv.org/abs/2604.15588)
- **2026-04-20**: 구조화된 tool-level 정책 통찰을 메모리에 유지하고 반복 개선하는 메커니즘(PolicyBank) [(원문)](https://arxiv.org/abs/2604.15505)
- **2026-01-01**: 분산형 multi-agent 시스템의 토폴로지 최적화로 지연 시간 감소 [(원문)](https://arxiv.org/abs/2601.10120)
- **2026-04-17**: Rashomon Memory: 다중 목표 에이전트가 관점별 독립 온톨로지 유지 + 검색 시 논증 이론으로 조율하는 메모리 아키텍처 [(원문)](https://arxiv.org/abs/2604.03588)
- **2026-04-17**: Skill activation/execution/termination 조건으로 정의된 executable skills를 semantic gradients 기반 PPO Gate로 검증, score-based maintenance로 고품질 procedural memory 유지 [(원문)](https://arxiv.org/abs/2602.01869)
- **2026-01-01**: 멀티 그래프 메모리(의미/시간/인과/엔티티 그래프)로 장문맥 추론 정확도 향상. LoCoMo/LongMemEval 벤치마크 통과 [(원문)](https://arxiv.org/abs/2601.03236)
- **2026-04-17**: Interlat: 압축된 latent space 통신으로 에이전트 내부 표현의 뉘앙스 전달 가능 [(원문)](https://arxiv.org/abs/2511.09149)
- **2026-04-17**: NEMORI 프레임워크: 예측 오류 기반 적응형 메모리 증류로 정보 보유 여부 자동 결정 [(원문)](https://arxiv.org/abs/2508.03341)
- **2026-04-17**: 경험의 표현 형식이 재사용 가능성과 적응력에 미치는 1차 영향 요소, compact gene 방식이 documentation-oriented보다 우수함 실증 [(원문)](https://arxiv.org/abs/2604.15097)
- **2026-04-17**: 에이전트가 코퍼스 구조를 명시적으로 인식하고 탐색 경로 추적, 비생산적 경로 백트래킹, 분산된 증거 조합 가능 [(원문)](https://arxiv.org/abs/2604.14572)
- **2026-04-17**: LLM 에이전트의 제한된 합리성(epsilon-rational preferences) 특성화 [(원문)](https://arxiv.org/abs/2604.14386)
- **2026-04-17**: 결정 정책을 메모리로 저장하여 과도한 합리화 방지, 암묵적 통계 정규성 흡수 [(원문)](https://arxiv.org/abs/2604.15190)
- **2026-04-17**: 메모리 리소스의 명시적 생명주기와 상태 추적으로 장기 에이전트 학습의 일관성 보장 [(원문)](https://arxiv.org/abs/2604.15034)
- **2026-04-17**: 계층적 메모리 구조로 IE 결과 유지하여 reasoning 정확도 향상 [(원문)](https://arxiv.org/abs/2604.14930)
- **2026-04-17**: SGA 원자를 메모리에 저장해 재사용 가능한 인과 로직 보존, 도메인 특이성은 제거 [(원문)](https://arxiv.org/abs/2604.14712)
- **2026-04-17**: 부모 아카이브를 통한 자율 에이전트 간 지식 상속 및 재사용 메커니즘 [(원문)](https://arxiv.org/abs/2604.14655)
- **2026-04-17**: 자기 진화하는 메모리로 의료 진단 에이전트의 inter-case learning 구현 [(원문)](https://arxiv.org/abs/2604.14475)
- **2026-04-17**: RUMS: 상호정보량 기반 메모리 선택이 의미 유사도 기반보다 인간 판단과 더 일치, 400배 큰 모델과도 경쟁 [(원문)](https://arxiv.org/abs/2604.14473)
- **2026-04-17**: APEX-MEM: 시간적 구조화 메모리로 LOCOMO QA 88.88% 정확도 [(원문)](https://arxiv.org/abs/2604.14362)
- **2026-04-17**: MemGround 벤치마크: Surface State Memory, Temporal Associative Memory, Reasoning-Based Memory 3계층 평가 프레임워크 [(원문)](https://arxiv.org/abs/2604.14158)


## 핵심 주체
[[Continual Learning]] | [[Metacognition in AI]] | [[Self-Evolving Agent Systems]]


## 모순/논쟁

