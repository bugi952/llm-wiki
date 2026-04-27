---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Scaling Laws

## 정의


## 주요 발전
- **2026-04-23**: Google DeepMind, 비동기 분산 학습 아키텍처(Decoupled DiLoCo) 공개로 GPU 동기화 제약 근본 해결 [(원문)](https://www.aitimes.com/news/articleView.html?idxno=209767)
- **2026-04-22**: 불확실성 인식 실험 설계로 스케일링 법칙 피팅 시 전체 예산의 ~10%만으로 전체 실험 대비 유사한 외삽 정확도 달성 (arXiv:2604.22753) [(원문)](https://arxiv.org/abs/2604.22753)
- **2026-04-26**: 구조화 의료 데이터는 제한 어휘·희소 관찰로 인해 NLP와 다른 스케일링 효과 가능성 제시 [(원문)](https://arxiv.org/abs/2604.22348)
- **2026-04-24**: 딥러닝 이론의 5가지 축(수해석적 설정, 추적가능 극한, 수학 법칙, 하이퍼파라미터, 보편 현상)의 통합 프레임워크 [(원문)](https://arxiv.org/abs/2604.21691)
- **2026-04-24**: 깊이 고정 시 추가 반복의 검증 손실을 새 스케일링 법칙으로 정량화: L = E + A(N_once + r^0.46·N_rec)^-α + B·D^-β (R²=0.997) [(원문)](https://arxiv.org/abs/2604.21106)
- **2026-04-24**: SGD는 배치 크기 감소에 따라 sharpness가 2/η 아래로 억제되는 현상 설명 (stochastic self-stabilization) [(원문)](https://arxiv.org/abs/2604.21016)
- **2026-04-21**: RLVR 훈련에서 엔트로피 유지 ↔ 응답 다양성, 캘리브레이션, 벤치마크 성능 간 상관관계 [(원문)](https://arxiv.org/abs/2511.05993)
- **2025-10-14**: 2025년 발견: 훈련 데이터의 intra-doc 반복, inconsistency, skewed distribution의 조합이 emergent knowledge arbitration 능력 촉발 [(원문)](https://arxiv.org/abs/2510.02370)
- **2026-04-21**: 신호 강도와 입력 공분산에 따른 학습 시간 창의 의존성. 과적합 전 신호 감지 가능 구간의 수학적 조건 [(원문)](https://arxiv.org/abs/2604.18450)
- **2026-04-21**: 생의학 데이터 성능을 제타 함수 기반 모델로 설명. 누적 신호-노이즈 에너지가 코버리언스 연산자의 스펙트럼 모드를 따라 축적 [(원문)](https://arxiv.org/abs/2604.17581)
- **2026-04-21**: Frontier supercomputer 32K GPU에서 63% strong scaling efficiency 달성—exascale 추론의 bottleneck 해소 [(원문)](https://arxiv.org/abs/2604.16590)
- **2026-04-21**: Test-time scaling: Best-of-N 선택에서 가벼운 calibration 기반 scorer로 expensive process reward model 대체 [(원문)](https://arxiv.org/abs/2604.16535)
- **2026-04-21**: Grokking 전이점이 TDU-OFC 오프라인 avalanche probe로 유한 크기 스케일링 D(t)로 정량화 가능 (modular addition, XOR) [(원문)](https://arxiv.org/abs/2604.16431)
- **2026-04-21**: Data Mixing: 샘플 선택이 아닌 도메인 가중치 최적화로 계산 예산 제약 하 효율성 극대화 [(원문)](https://arxiv.org/abs/2604.16380)
- **2025-09-01**: RL post-training의 스케일링 법칙: 모델 스케일(0.5B~72B), 데이터량, 컴퓨트 예산의 상호작용을 거듭제곱 함수로 모델링. 대형 모델의 학습 효율 우월성 실증 [(원문)](https://arxiv.org/abs/2509.25300)
- **2026-04-20**: 추론 스펙트럼이 모델 크기에 로그 스케일링 의존 (α_reasoning ∝ -0.074 ln N) [(원문)](https://arxiv.org/abs/2604.15350)
- **2026-04-19**: 훈련 데이터 커버리지가 성능 한계를 설정하며, RL은 안정성만 개선할 뿐 한계를 확장하지 못함 [(원문)](https://arxiv.org/abs/2604.15306v1)
- **2025-06-13**: 고차원 등가(High-dimensional Equivalent) 프레임워크: RMT를 비선형 DNN으로 확장, Proportional regime에서 데이터 차원·표본·파라미터 상호작용 분석 [(원문)](https://arxiv.org/abs/2506.13139)
- **2026-01-14**: LLMOrbit: 브루트포스 스케일링 한계(scaling wall) 정의 — 데이터 고갈 9-27T, 비용 $3M→$300M+/5년, 에너지 22배 증가 [(원문)](https://arxiv.org/abs/2601.14053)
- **2026-01-12**: Threshold Differential Attention (TDA)는 Row-wise extreme-value thresholding으로 소프트맥스의 sink 문제 해결 [(원문)](https://arxiv.org/abs/2601.12145)
- **2026-01-07**: ORBIT: 다단계 강화학습으로 각 reasoning budget 수준에서 Pareto-optimal 정책 발견 [(원문)](https://arxiv.org/abs/2601.08310)
- **2026-04-17**: LLM 일반화: 공간적 전이(unseen maps)는 강하나 길이 스케일링(longer horizons)에서 재귀적 불안정성으로 실패 [(원문)](https://arxiv.org/abs/2604.15306)
- **2026-04-17**: Looped transformers: 테스트 타임 반복으로 어려운 문제에 더 많은 계산 할당 가능. 재귀+정규화 조합으로 입력 의존성 확보 [(원문)](https://arxiv.org/abs/2604.15259)
- **2026-04-17**: Inference 단계 계산량 증가도 모델 성능의 주요 스케일링 축 [(원문)](https://arxiv.org/abs/2604.14853)
- **2026-04-17**: 사전학습 후 크기별 가중치 합성으로 스케일 적응, 배포 시점의 모델 크기 자유도 확보 [(원문)](https://arxiv.org/abs/2604.14769)
- **2026-04-17**: MoE 모델에서 expert routing의 specialization 동역학이 정보-기하학적 프레임워크로 분석 가능, 실패 예측(FSI) 정의 [(원문)](https://arxiv.org/abs/2604.14500)
- **2026-04-17**: Claude Opus 4.7은 향상된 스케일링 효율성 보유 [(원문)](https://news.ycombinator.com/item?id=47793546)
- **2026-04-17**: In-context operator learning: 단일 연산자 모델 대비 공간-시간 예측에서 우수한 성능 입증 (GICON, arXiv:2603.12725) [(원문)](https://arxiv.org/abs/2603.12725)
- **2026-04-17**: LLM 계산 밀도: 주로 밀집, 입력에 따라 희소-밀집 간 동적 전환 (입력별 패턴 상관도 높음) [(원문)](https://arxiv.org/abs/2601.22795)
- **2026-01-15**: TRIM: 위험 단계만 고성능 모델 라우팅 → 정확도 유지하며 inference 비용 절감 [(원문)](https://arxiv.org/abs/2601.10245)
- **2026-04-17**: 전문가 모델 없이 기존 데이터로 Large Reasoning Models 성능 향상 [(원문)](https://arxiv.org/abs/2510.26519)
- **2026-04-17**: 데이터 효율적 정책 학습으로 LLM 스케일링 최적화 [(원문)](https://arxiv.org/abs/2510.26491)
- **2026-04-17**: test-time compute 확장으로 오픈 가중치 모델 추론 능력 비약적 향상 [(원문)](https://arxiv.org/abs/2510.14232)
- **2025-10-12**: 평탄함/예각성은 학습 함수에 의존하는 상대적 개념; 동일 최적해도 다른 기하학적 특성 가능 [(원문)](https://arxiv.org/abs/2510.12451)
- **2025-10-05**: 3.8백만 프로그래밍 학습자 추적 데이터(Pencil Code)로 학생 코딩 행동 및 습득 과정 분석 모델 학습 [(원문)](https://arxiv.org/abs/2510.05056)
- **2025-10-03**: Reasoning distillation: 전체 trajectory 최적화 vs step-level 신호 → 학생 모델은 익숙한 step 조합으로 일반화, LALP로 전이 가능한 신호 추출 [(원문)](https://arxiv.org/abs/2510.03988)
- **2026-04-17**: Negative Sample Reinforcement (NSR): Pre-train Space RL의 효율적 기울기 정렬 메커니즘 [(원문)](https://arxiv.org/abs/2604.14142)
- **2026-04-17**: Momentum SGD는 batch size에 따라 2가지 sharpness 플래토로 수렴: 소형(2(1-β)/η) vs 대형(2(1+β)/η). Batch size에 따른 stochastic stability의 이중 구조 [(원문)](https://arxiv.org/abs/2604.14108)
- **2026-04-14**: Token importance 선택으로 50% 토큰만 사용해도 full-token 학습 성능 달성 (메모리 47% 절감) [(원문)](https://arxiv.org/abs/2604.14084)
- **2026-04-14**: 외부 데이터 없이 self-play로 sparse reward 문제 해결 [(원문)](https://arxiv.org/abs/2604.14054)
- **2026-04-14**: 토크나이저 정규화로 LLM 추론 효율성 및 안전성 동시 개선 [(원문)](https://arxiv.org/abs/2604.14053)
- **2026-04-14**: Shallow ReLU 네트워크의 완전한 대칭성 분류 제시 [(원문)](https://arxiv.org/abs/2604.14037)


## 핵심 주체
[[Google DeepMind]] | [[Model Efficiency]]


## 모순/논쟁

