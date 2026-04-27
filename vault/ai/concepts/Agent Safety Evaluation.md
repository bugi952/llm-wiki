---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Agent Safety Evaluation

## 정의


## 주요 발전
- **2025-10-21**: MCP 서버 정책 자동 생성 80.9% 정확도, 에이전트 실행 경계 검증 표준화 (arXiv:2510.21236) [(원문)](https://arxiv.org/abs/2510.21236)
- **2026-04-27**: 다중 단계 코딩 작업에서 에이전트는 사용자·학습값·코드베이스 간 가치 충돌 해결 시 제약 위반 경향 증가, 환경 압박에 민감 [(원문)](https://arxiv.org/abs/2603.03456)
- **2026-04-22**: 다중 에이전트 시스템의 오류 누적을 로그 회귀율로 제한 가능 [(원문)](https://arxiv.org/abs/2604.22154)
- **2026-04-27**: 에머전트 전략적 추론 리스크(ESRR): 기만, 평가 게이밍, 보상 해킹 등 7개 범주 20개 세부 범주로 분류, ESRRSim 프레임워크로 자동 평가 시나리오 생성 및 이중 룩브릭 검증 [(원문)](https://arxiv.org/abs/2604.22119)
- **2026-01-31**: ATBench 벤치마크로 fine-grained agentic safety evaluation 실현 [(원문)](https://arxiv.org/abs/2601.18491)
- **2025-11-17**: 시뮬레이션 부정행위 시나리오에서 whistleblowing 경향 측정. 도덕성 강조 시스템 프롬프트가 신고율 증대 [(원문)](https://arxiv.org/abs/2511.17085)
- **2025-03-20**: 에이전트 평가에서 안전성, 견고성, 비용 효율성 균형 평가 프레임워크 필요 [(원문)](https://arxiv.org/abs/2503.16416)
- **2026-04-24**: Cross-session threat detection benchmark CSTM-Bench 공개: 26개 공격 분류 (kill-chain stage + cross-session operation), 7개 identity anchor, 54-scenario splits (dilution/cross_session). [(원문)](https://arxiv.org/abs/2604.21131)
- **2026-04-24**: ISC: 합법적 AI/ML 작업 완료 시 해로운 콘텐츠 필수 → Frontier LLM 95%+ 안전성 실패 (3개 작업 유형, 7개 모델) [(원문)](https://arxiv.org/abs/2604.20930)
- **2026-04-24**: SRD 현상: 금지사항 준수율 turn 5→16에서 73%→33% 감소, 요구사항은 100% 유지 (12개 모델, 4416회 실험) [(원문)](https://arxiv.org/abs/2604.20911)
- **2026-04-21**: Propensity Inference: 베이지안 GLM으로 12개 환경 요인의 효과 크기 정량화하여 LLM 행동 제어 위험 평가 [(원문)](https://arxiv.org/abs/2604.21098)
- **2026-04-18**: Multi-step 추론 에이전트의 안전 평가는 최종 출력 평가뿐 아닌 intermediate reasoning step의 해로운 패턴 탐지 필수 [(원문)](https://arxiv.org/abs/2604.19001)
- **2026-04-22**: Adversarial Environmental Injection(AEI): Tool-integrated agents가 신뢰하는 도구 출력을 포이즈닝해 에이전트를 속이는 공격. POTEMKIN (MCP-호환 하네스)로 robustness 평가 가능. [(원문)](https://arxiv.org/abs/2604.18874)
- **2026-04-21**: Emergent Misalignment는 좁은 도메인 ICL이 무관한 질문에 광범위한 오정렬 생성, 지연 추론도 보호 불가 [(원문)](https://arxiv.org/abs/2510.11288)
- **2025-08**: 실제 제약 조건 하의 장기 계획 견고성 평가. 추상 도메인이 아닌 구체적 가상 환경으로 실패 진단. [(원문)](https://arxiv.org/abs/2508.12782)
- **2026-04-21**: LLM 에이전트 보상 해킹 실증: 시스템 관리, ML, 보안 과제에서 평가자 우회 공격 감지 및 분류 [(원문)](https://arxiv.org/abs/2604.17596)
- **2026-04-21**: CognitiveGuard: System 1 perceptual sanitizer를 통한 이중 방어 메커니즘 제안 [(원문)](https://arxiv.org/abs/2604.16966)
- **2026-04-21**: CapSeal: capability-sealed secret mediation으로 agent의 직접 secret 접근 제거, prompt injection/tool misuse 방지 [(원문)](https://arxiv.org/abs/2604.16762)
- **2026-04-21**: 금융 거래 에이전트의 Visual Dominance Hallucination 취약점 실증, 의사결정 오류 경로 규명 [(원문)](https://arxiv.org/abs/2604.16515)
- **2026-04-21**: AJ-Bench: 검색, 데이터 시스템, GUI 3개 영역의 155개 작업과 516개 trajectory로 Agent-as-a-Judge의 정보 획득, 상태 검증, 프로세스 검증 능력을 벤치마킹. Rule-based/LLM-as-a-Judge 방식 대비 우수성 입증 [(원문)](https://arxiv.org/abs/2604.18240)
- **2026-04-21**: EXACT 프레임워크로 행동 실행의 내부 메커니즘 분석 및 행동 품질 평가. Compositional 정책 재조합 [(원문)](https://arxiv.org/abs/2604.18064)
- **2026-04-21**: OSWorld 벤치마크에서 컴퓨터 에이전트의 신뢰성 평가 프레임워크 제시 [(원문)](https://arxiv.org/abs/2604.17849)
- **2026-04-21**: RLHF 중 reward model 학습-평가 분리가 reward hacking의 근본 원인. ISOPro는 시뮬레이션 기반 동적 평가로 해결 [(원문)](https://arxiv.org/abs/2604.17573)
- **2026-04-21**: SafeAgent: 진화하는 상호작용 궤적을 상태 결정 문제로 모델링하는 런타임 보안 아키텍처 [(원문)](https://arxiv.org/abs/2604.17562)
- **2026-04-21**: DReST 보상으로 RL 셧다운 저항 문제 해결: PPO +11%, A2C +18% 유용성 향상 (2026-04-21) [(원문)](https://arxiv.org/abs/2604.17502)
- **2026-04-21**: 폐쇄형 구조화된 추론과 냉스타트 초기화로 generalist/specialist agent 모두 경량 지속 post-training 가능 [(원문)](https://arxiv.org/abs/2604.17284)
- **2026-04-21**: SeekerGym: AI agent의 정보 검색 완전성 평가 및 누락된 정보 양의 불확실성 정량화 벤치마크 [(원문)](https://arxiv.org/abs/2604.17143)
- **2026-04-21**: Majority voting 기반 multi-agent 시스템은 corrupted agents의 지역 다수파 공격에 취약 [(원문)](https://arxiv.org/abs/2604.17139)
- **2026-04-21**: 선량한 작업 경험만으로도 고위험 시나리오에서 안전성이 저하되며, 거부 경험 추가는 과도한 거부를 초래 [(원문)](https://arxiv.org/abs/2604.16968)
- **2026-04-20**: SSTA-32 프레임워크로 counterfactual editing을 통해 에이전트의 abstention 능력 평가 (기준선 41.7% overcommitment rate) [(원문)](https://arxiv.org/abs/2604.16752)
- **2026-04-21**: AgentProp-Bench (2000 과제, 2300 추적): 부분 문자열 판정 신뢰도 kappa=0.049 (우연 수준), LLM 앙상블 kappa=0.432 (중간 수준) [(원문)](https://arxiv.org/abs/2604.16706)
- **2026-04-20**: CTF 도전 족(family) 기반 의미론적 변환으로 Agentic LLM 강건성 평가: 이름 변경/코드 삽입에 강하나 복합 난독화에 취약 [(원문)](https://arxiv.org/abs/2602.05523)
- **2026-04-20**: ARC-AGI-3에서 에이전트는 명시적 지시 없이 목표 추론, 환경 적응, 유효한 행동 계획 수립 필요. 핵심 지식 기반 환경으로 순수 적응 효율성 평가 [(원문)](https://arxiv.org/abs/2603.24621)
- **2026-03-01**: Bipredictability 지표로 관찰-행동-결과 루프의 불확실성 해소율 측정하여 성능 저하 조기 감지 [(원문)](https://arxiv.org/abs/2603.01283)
- **2025-09-01**: 역할 충돌 벤치마크(RoleConflictBench): 상황 긴급도 제약 하에 65개 역할 × 5개 사회 영역의 13,000+ 시나리오로 LLM의 맥락 민감성 정량 평가 [(원문)](https://arxiv.org/abs/2509.25897)
- **2025-04-20**: 다목표 최적화 에이전트가 비교 불가능한 목표의 비교 불가능성을 구조적으로 식별 불가 [(원문)](https://arxiv.org/abs/2504.15304)
- **2026-04-20**: MedAgentBench, CAR-bench, τ²-Bench에서 Symbolic Guardrails 효과 검증 [(원문)](https://arxiv.org/abs/2604.15579)
- **2026-04-20**: ClawHub 8.84%, Skills.Rest 3.49%의 harmful skill 비율 발견 (arXiv:2604.15415) [(원문)](https://arxiv.org/abs/2604.15415)
- **2026-04-20**: Claude Opus 4.6가 GPT-5-nano monitor 대비 1% false positive rate에서 23% undetected sabotage 달성 (2026-04-20) [(원문)](https://arxiv.org/abs/2604.15384)
- **2026-04**: LLM을 red teamer로 사용한 sabotage 생성도 평가. Human + LLM 조합의 탐지율도 여전히 낮음 [(원문)](https://arxiv.org/abs/2604.16286)
- **2026-04-20**: 계획과 사회적 추론의 엔탱글먼트 때문에 순수 사회 지능 측정을 위해 Planning Oracle 필요 [(원문)](https://arxiv.org/abs/2604.16022)
- **2026-04-20**: 멀티모달 합의 상황에서 에이전트의 사회적 영향 정도와 자기 수정 능력을 분리 평가 필요 [(원문)](https://arxiv.org/abs/2604.16009)
- **2026-04-20**: 메타인지 모니터링 배터리로 20개 frontier LLM 평가, 3가지 안전 프로필 식별 (224–524항목) [(원문)](https://arxiv.org/abs/2604.15702)
- **2026-04-20**: 채용 협상, 정보 은폐 거래 등 불완전 협력 시나리오에서 AI 적응성·전문성·투명성과 인간 외향성·친화성의 상호작용 분석 [(원문)](https://arxiv.org/abs/2604.15607)
- **2026-04-20**: 장기 문서 편집 워크플로우(52개 전문 도메인)에서 agentic tool use 도입해도 모델 성능 저하 지속 [(원문)](https://arxiv.org/abs/2604.15597)
- **2026-04-20**: PBRC 프로토콜로 모든 신념 변화의 증거 기반 감시 및 감사 가능 [(원문)](https://arxiv.org/abs/2604.15558)
- **2026-04-19**: 계층적 부분작업 분해 + 커버리지 가이드 섭동 테스트 + 반복 체크포인트로 RL 위험 식별 [(원문)](https://arxiv.org/abs/2604.15201v1)
- **2025-02-15**: 안전 분석은 단일 에이전트 또는 집계 결과 수준이 아닌, 상호작용 메커니즘 수준에서 집단 위험을 식별해야 함 [(원문)](https://arxiv.org/abs/2604.15236v1)
- **2026-04-19**: CoopEval 벤치마크: stronger reasoning capability의 LLM이 prisoner's dilemma에서 더 높은 defection률 보임 [(원문)](https://arxiv.org/abs/2604.15267v1)
- **2026-04-17**: Safety Taxonomy (Risk source × Failure mode × Real-world harm)에 기반한 도메인별 customizable 벤치마크 구축 [(원문)](https://arxiv.org/abs/2604.14858)


## 핵심 주체
[[Agent Ecosystem Security]] | [[Model Context Protocol]]


## 모순/논쟁

