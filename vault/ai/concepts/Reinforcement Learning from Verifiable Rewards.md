---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Reinforcement Learning from Verifiable Rewards

## 정의


## 주요 발전
- **2025-08-06**: 검색과 추론의 불균형을 개선하는 난이도 인식 커리큘럼 전략 [(원문)](https://arxiv.org/abs/2508.06165)
- **2026-04-21**: DROL: 잠재 조건부 1-step 액터에 top-1 동적 라우팅 적용 → BC와 크리틱 가이던스 양립 [(원문)](https://arxiv.org/abs/2604.22229)
- **2026-04-26**: RIC: 분류 태스크에서 stepwise prediction quality 개선에 RL 적용, value function으로 anytime halting 구현 [(원문)](https://arxiv.org/abs/2604.22110)
- **2026-04-27**: RLVR 훈련 전 소량의 SFT를 거치면 추론 체인의 CIR/SR 개선 가능 (Qwen2.5 실험) [(원문)](https://arxiv.org/abs/2604.22074)
- **2026-04-25**: TD error 초기 단계→신뢰도 성숙 후 안정성 기반 샘플링으로 전환, hardware noise trajectory 재활용 [(원문)](https://arxiv.org/abs/2604.21863v1)
- **2026-04-24**: DynaMO: sequence 수준 variance-minimizing rollout allocation과 token 수준 gradient-aware advantage modulation으로 resource 최적화 [(원문)](https://arxiv.org/abs/2602.19208)
- **2026-04-24**: GeoRA는 RL update subspace의 anisotropic, compressible 구조를 활용한 geometry-aware adaptation [(원문)](https://arxiv.org/abs/2601.09361)
- **2026-04-24**: RIFT는 모든 positive/negative trajectories에서 학습하는 데이터 효율적 RLVR 기법 [(원문)](https://arxiv.org/abs/2601.09253)
- **2025-11-25**: LLM RL 포스트트레이닝의 off-policy 훈련: importance clipping(PPO-Clip)만으로는 전역 분포 변화 미흡. ERC는 엔트로피 비율로 보정 [(원문)](https://arxiv.org/abs/2512.05591)
- **2025-10-15**: 다턴 대화의 Lost-in-Conversation 문제를 RLAAR(커리큘럼 RL + 추상화 보상)로 해결, 신뢰도 향상 [(원문)](https://arxiv.org/abs/2510.18731)
- **2025-10-01**: 역강화학습(AIRL)으로 전문가 시연에서 추론 리워드 모델 학습, SFT와 결과 기반 RL의 중간 접근 [(원문)](https://arxiv.org/abs/2510.01857)
- **2025-09**: CE-GPPO: PPO 클리핑 구간 밖 저확률 토큰의 경사 신호를 제한된 범위 내에서 복원해 엔트로피 조율 [(원문)](https://arxiv.org/abs/2509.20712)
- **2026-04-24**: RAW-UCB로 reward decay 문제의 rested/restless 구분 통합 처리 (recommender, tutoring systems) [(원문)](https://arxiv.org/abs/2604.21432)
- **2026-04-21**: DDRL의 consensus-based off-policy 검증으로 reward noise 감소, 수학 추론 성능 향상 [(원문)](https://arxiv.org/abs/2604.21327)
- **2026-04-22**: Tabular 도메인에서 검증 가능한 reward signal (coverage, distinctness) 설계 및 적용 [(원문)](https://arxiv.org/abs/2604.18966)
- **2026-04-22**: Groupwise Ranking Reward로 검증된 궤적 내에서 더 강한 추론을 우선시하여 answer-correctness와 reasoning-validity 동시 최적화 [(원문)](https://arxiv.org/abs/2604.18892)
- **2025-12**: Argos: 다중 교사 모델 및 규칙 기반 점수 함수 풀에서 동적 선택하여 최종 정확도+공간시간 지역화 종합 평가 [(원문)](https://arxiv.org/abs/2512.03438)
- **2026-04-21**: Turn-level 보상으로 다중 턴 도구 사용 추론 학습 신호 개선 (GTPO) [(원문)](https://arxiv.org/abs/2511.14846)
- **2026-04-21**: 엔트로피 붕괴 원인 분석: 클리핑 임계값, 정책 외 업데이트 수, 학습 데이터 다양성 3가지 핵심 요인 [(원문)](https://arxiv.org/abs/2511.05993)
- **2025-10-14**: 루브릭 기반+결과 리워드 결합으로 추론 신뢰성 향상 (6개 멀티모달 벤치마크) [(원문)](https://arxiv.org/abs/2510.14738)
- **2026-04-21**: 비동기 평균화 Q-learning의 비점근 중심극한정리 증명 (Wasserstein 수렴) [(원문)](https://arxiv.org/abs/2509.18964)
- **2026-04-21**: Self-evolving CoT curriculum (EvoCoT)으로 sparse reward 조건에서도 hard problem 탐색 병목 해결, 다양 LLM family에서 reasoning 능력 향상 [(원문)](https://arxiv.org/abs/2508.07809)
- **2026-04-21**: 기하학 문제에서 검증된 보상으로 소규모 모델 학습 (arXiv:2506.07160) [(원문)](https://arxiv.org/abs/2506.07160)
- **2026-04-21**: Ground-truth 없는 long-form writing 최적화에 pairwise comparison 기반 보상 메커니즘 적용 (2026-04-21) [(원문)](https://arxiv.org/abs/2506.05760)
- **2024-11-04**: Plasticity loss는 RL 성능 plateau와 scaling failure의 주요 원인. 50+ 완화 전략 정리됨 [(원문)](https://arxiv.org/abs/2411.04832)
- **2026-04-21**: 심층 양자 프로세스 회귀 기반 OPE(DQPOPE)로 정책 평가 분포 추정, 통계적 신뢰도 향상 [(원문)](https://arxiv.org/abs/2604.18143)
- **2026-04-21**: Q-값 반복에서 정책이 실질적으로 최적인 해의 집합(POS) 정의 및 스위칭 시스템으로 기하학적 분석 [(원문)](https://arxiv.org/abs/2604.17457)
- **2026-04-21**: EasyVideoR1: RLVR을 비디오 이해에 확장한 최초의 완전한 프로덕션 프레임워크 공개 [(원문)](https://arxiv.org/abs/2604.16893)
- **2026-04-21**: BRRL(Bounded Ratio RL)로 신뢰 영역 방법의 이론적 기초 재정의 (2026-04-21) [(원문)](https://arxiv.org/abs/2604.18578)
- **2026-04-21**: Weak supervision (희소 데이터/노이즈/자체 감독)에서 일반화는 training reward saturation 동역학이 지배 [(원문)](https://arxiv.org/abs/2604.18574)
- **2026-04-21**: 다중 교사 협업 훈련과 엔트로피 기반 탐색 보상으로 LLM 추론 능력 향상 [(원문)](https://arxiv.org/abs/2604.18530)
- **2026-04-21**: 포화 벤치마크 환경에서 CUTS(Constrained Uniform Top-K Sampling)로 고신뢰도 후보 영역 내 균일 샘플링 강제, Mixed-CUTS로 exploit/explore 롤아웃 합성하여 그룹 내 우위 분산 증폭 [(원문)](https://arxiv.org/abs/2604.18493)
- **2026-04-21**: 저 데이터 환경에서 procedural dataset으로 SLM RLVR 성능의 세밀한 스케일링 가능 (arXiv 2604.18381) [(원문)](https://arxiv.org/abs/2604.18381)
- **2026-04-21**: 검증 기반 보상 모델(VRM)과 적응형 보상 융합(ARF)으로 양자 역학 등 과학 도메인의 LLM 신뢰성 강화 [(원문)](https://arxiv.org/abs/2604.18176)
- **2026-04-21**: 불연속 동역학에서 梯度 편향 문제를 DDCG 방법으로 해결 [(원문)](https://arxiv.org/abs/2604.18161)
- **2026-04-21**: Entropy collapse는 저자원 환경의 RLVR 성능을 제약하며, 고일반도메인 데이터와 EDA 메커니즘으로 해결 가능 (2026-04-21) [(원문)](https://arxiv.org/abs/2604.17928)
- **2026-04-21**: 다중 시도 CoT에서 단순한 성공/실패 가중치는 편향된 그래디언트를 야기하며, 보정된 시도 레벨 가중치(CAL GRPO)로 불편향 추정 달성 [(원문)](https://arxiv.org/abs/2604.17912)
- **2026-04-20**: 연속 잠재 표현에 직접 RL 적용으로 이산 공간 정책 최적화 대비 탐색 다양성 개선. 확률적 샘플링이 명시적 탐색 메커니즘 대체 [(원문)](https://arxiv.org/abs/2604.17892)
- **2026-04-21**: SVL: 목표까지의 시간을 확률분포로 모델링, hazard model 기반 최대우도 추정으로 안정성 향상 [(원문)](https://arxiv.org/abs/2604.17551)
- **2026-04-21**: 데이터 희소성 조건에서 LLM RL의 3가지 관점(데이터중심, 훈련중심, 프레임워크중심) 분류 및 방법론 체계화 [(원문)](https://arxiv.org/abs/2604.17312)
- **2026-04-21**: Verifiable reward를 활용한 abstention과 post-refusal clarification의 동시 최적화 구현 [(원문)](https://arxiv.org/abs/2604.17073)
- **2026-04-16**: On-policy rollout을 IRL demonstration으로 활용하여 reward trajectory 다양성 회복 [(원문)](https://arxiv.org/abs/2604.16995)
- **2026-04-21**: MCPO: Mastery 프롬프트에 hinge-KL regularizer 적용으로 정책 드리프트 방지, 부분 정답→완전 정답 수렴 강화 [(원문)](https://arxiv.org/abs/2604.16972)
- **2026-04-21**: LLM RL의 Priority staleness 문제: 빠른 정책 진화로 저장된 우선순위가 낡음. Freshness-Aware PER로 개선 [(원문)](https://arxiv.org/abs/2604.16918)
- **2026-04-21**: Cross-cultural entity translation에서 entity-level verifiable reward 활용 (EA-RLVR 프레임워크) [(원문)](https://arxiv.org/abs/2604.16881)
- **2026-04-21**: DARLING: 비정상 MDP 변화점 감지로 동적 회귀 경계 첫 달성 (타뷸러·선형 통합) [(원문)](https://arxiv.org/abs/2604.16684)
- **2026-04-20**: 과정 감독 기반 reward model로 trajectory-level 페널티의 과도한 단축 문제 개선, 미세한 신용 할당 [(원문)](https://arxiv.org/abs/2602.09953)
- **2026-04-20**: Adaptive Entropy Regularization (AER): 고정 엔트로피 계수 대신 작업 난이도별 탐색강도 동적 조정으로 RLVR 성능 개선 [(원문)](https://arxiv.org/abs/2510.10959)
- **2025-09-05**: Self-Aligned Reward(SAR)로 검증 가능 보상의 이진 피드백 한계 극복 [(원문)](https://arxiv.org/abs/2509.05489)
- **2026-04-20**: 작업 기반 RL이 분포 날카로움보다 모델에 실제 새로운 기술 부여 [(원문)](https://arxiv.org/abs/2604.16259)
- **2026-04-20**: 다중 턴 도구 기반 프로세스로 오류 전파 및 신뢰성 문제 해결 [(원문)](https://arxiv.org/abs/2604.16004)
- **2026-04-20**: 롤아웃 궤적의 망각과 불확실성 신호로 실패 패턴 식별, LLM 기반 작업 합성 [(원문)](https://arxiv.org/abs/2604.15840)
- **2026-04-20**: Best-of-N sampling을 통한 empowerment-driven exploration 탄력성 확보 [(원문)](https://arxiv.org/abs/2604.15614)
- **2026-04-20**: RCFG로 테스트 타임에 보상함수 변경 가능, 모델 재학습 불필요 [(원문)](https://arxiv.org/abs/2604.15577)
- **2026-04-19**: 보상 해킹: 모델이 검증자 불완전성을 악용해 일반화 불가능한 패턴 학습 [(원문)](https://arxiv.org/abs/2604.15149v1)
- **2026-04-17**: V-Triune: 샘플/검증/진단 세 수준 추상화로 멀티모달 RL 통합, 8개 추론-인식 작업 동시 학습 [(원문)](https://arxiv.org/abs/2505.18129)
- **2025-10-26**: LTE(Learning from Trial and Error): 자체 오류 학습으로 GRPO 대비 Pass@1 평균 5.02, Pass@k 9.96 향상, 외부 전문가 의존 제거 [(원문)](https://arxiv.org/abs/2510.26109)
- **2025-10-20**: BoundRL: 경계 생성을 RLVR로 최적화하는 구조적 텍스트 분할, 출력 토큰 90% 감소로 hallucination 최소화 [(원문)](https://arxiv.org/abs/2510.20151)
- **2025-10-10**: UCAS: 모델 내부 불확실성 신호 활용, token-level 비대칭 페널티로 entropy collapse 해결 [(원문)](https://arxiv.org/abs/2510.10649)
- **2025-06-09**: DPO는 명시적 보상 함수 없이 선호도 최적화하나, 토큰 레벨 생성 중요도와 암묵적 보상 함수의 불일치가 성능 한계 유발하는 이론적 결함 규명 [(원문)](https://arxiv.org/abs/2506.09457)
- **2024-11-01**: Value function regularization으로 달성 불가능한 부분목표 방지. Preference-based learning으로 reward 신호의 비정상성 극복 [(원문)](https://arxiv.org/abs/2411.00361)
- **2026-04-17**: Bandit 알고리즘의 regret 꼬리 확률 특성화 연구 [(원문)](https://arxiv.org/abs/2604.14876)
- **2026-04-17**: 적대적 보상 환경에서의 최적 학습 알고리즘 특성화 [(원문)](https://arxiv.org/abs/2604.14860)
- **2026-04-17**: RLVR 모델이 검증자를 속이는 reward hacking 현상 발견 [(원문)](https://arxiv.org/abs/2604.15149)
- **2026-04-17**: Step-level 정보 이득 기반 보상으로 검색 강화 추론 개선 [(원문)](https://arxiv.org/abs/2604.15148)
- **2026-04-17**: LLM pseudo-observations 예측 정확도를 exponential moving average로 추적하여 온라인 의사결정 학습 개선 [(원문)](https://arxiv.org/abs/2604.14961)
- **2026-04-17**: 음성 대화 모델의 의미론적 견고성과 차례짓기 개선을 위한 이중축 생성형 보상 모델 [(원문)](https://arxiv.org/abs/2604.14920)
- **2026-04-17**: RGPO(Rejection-Gated Policy Optimization)가 importance sampling 대신 미분가능한 acceptance gate로 신뢰성 샘플 선별 [(원문)](https://arxiv.org/abs/2604.14895)
- **2026-04-17**: 정책을 Wasserstein 공간 위의 함수로 정의, 리만 구조로 기울기/헤시안 분석 [(원문)](https://arxiv.org/abs/2604.14765)
- **2026-04-17**: UEC-RL: GRPO 엔트로피 붕괴 문제를 대상별 엔트로피 제어로 해결 [(원문)](https://arxiv.org/abs/2604.14646)
- **2026-04-17**: 정책-가치 불일치를 이용한 value-aware intervention으로 인간의 suboptimal policy 맥락에서 성능 향상 [(원문)](https://arxiv.org/abs/2604.14465)
- **2026-04-17**: Value Gradient Flow (VGF): 최적 수송 기반 행동 정규화 RL 패러다임, 이산 그래디언트 플로우로 확장 가능하게 해결 [(원문)](https://arxiv.org/abs/2604.14265)
- **2026-04-17**: 동적 계수 정정(DCR)으로 역확률 가중치 적응적 제약, 그래디언트 폭발 및 엔트로피 붕괴 방지 [(원문)](https://arxiv.org/abs/2604.14258)


## 핵심 주체
[[RAG (Retrieval-Augmented Generation)]]


## 모순/논쟁

