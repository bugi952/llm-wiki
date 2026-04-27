---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Physics-Informed Neural Networks

## 정의


## 주요 발전
- **2025-02-15**: Neural operator의 multimodal fusion 전략(field projection, branch decomposition) 임상 비교 [(원문)](https://arxiv.org/abs/2510.03248)
- **2026-04-25**: Pi-PINN은 폐형식 헤드 적응과 의사역행렬을 이용해 미지의 PDE에 빠른 일반화 달성 [(원문)](https://arxiv.org/abs/2604.21761v1)
- **2026-01-31**: Importance Density Functions(IDF)를 통한 KAN 격자 적응의 일반화 프레임워크 [(원문)](https://arxiv.org/abs/2601.18672)
- **2026-04-24**: LLM 생성 + 물리 계산 검증 루프로 실현 가능성 높은 신물질 후보 도출 [(원문)](https://arxiv.org/abs/2604.21068)
- **2026-04-24**: Transfer learning을 통한 미지 PDE 문제의 일반화 능력 개선 (Pi-PINN framework: Pseudoinverse 기반 폐쇄형 적응) [(원문)](https://arxiv.org/abs/2604.21761)
- **2026-04-24**: Green 적분 제약 기반 신경망 해석기로 고진동 Helmholtz 해 정확도 향상 [(원문)](https://arxiv.org/abs/2604.21411)
- **2026-04-24**: PI-LNO: 라플라스 적분 변환을 학습 기반으로 물리정보화한 신경망, 액체 방울 확산 예측에 적용 [(원문)](https://arxiv.org/abs/2604.20993)
- **2026-04-22**: FlowForge: 국소 문맥 기반 staged rollout으로 CFD 예측 안정성·노이즈 견고성 향상. 다단계 공간 업데이트로 오차 증폭 제어 [(원문)](https://arxiv.org/abs/2604.18953)
- **2026-04-22**: AC-SINDy는 arithmetic circuits로 동적으로 구성된 feature library를 사용하여 확장성 향상 [(원문)](https://arxiv.org/abs/2604.18889)
- **2025-10-21**: XRePIT은 OpenFOAM과 neural surrogate를 residual 기반으로 결합해 유체역학 장시간 시뮬레이션의 안정성 개선 [(원문)](https://arxiv.org/abs/2510.21804)
- **2023-01-20**: 신경 연산자는 편미분방정식 풀이에서 이산화 불변성·해상도 불변성 제공, FEM·FDM 대비 속도·정확성 향상 [(원문)](https://arxiv.org/abs/2301.13331)
- **2026-04-21**: 상 분야 모델 시뮬레이션에서 에너지 분할 변분 공식으로 신경 연산자 훈련 시 기저 모델의 에너지 소산 특성 강제 [(원문)](https://arxiv.org/abs/2604.18261)
- **2026-04-21**: 고차원 동역학의 롤아웃 오류에서 확산 기반 확률적 추론이 고전적 방법보다 견고성 증대 (arXiv:2604.17566) [(원문)](https://arxiv.org/abs/2604.17566)
- **2026-04-21**: Neural PDE 솔버의 누적 오차 문제를 ODE 기반 반복 정제로 해결 [(원문)](https://arxiv.org/abs/2604.17149)
- **2026-04-21**: PIT: 비디오 입자 추적에 미분 가능한 물리 모듈 통합, PILL 손실함수로 라벨 없이 물리 일관성 강제 [(원문)](https://arxiv.org/abs/2604.16895)
- **2026-04-21**: 희소 관측에서 시간 의존 PDE의 시공간 궤적 복원 달성 [(원문)](https://arxiv.org/abs/2604.16461)
- **2026-04-21**: BINN은 폐암 세포 2D+t 반응-확산 방정식 학습에 응용. 데이터 전처리-BINN-심볼릭 회귀 파이프라인 [(원문)](https://arxiv.org/abs/2604.18548)
- **2026-04-21**: Dallara 협력 고충실도 RANS 데이터셋으로 motorsport CAD 공기역학 CFD 신경망 서로게이트 학습, 기존 공개 데이터셋(단순화 승용차)의 한계 극복 [(원문)](https://arxiv.org/abs/2604.18491)
- **2026-04-21**: HVAC 시스템 응용: implicit PINODE로 냉매 질량·내부에너지 보존 제약을 자동미분으로 학습 [(원문)](https://arxiv.org/abs/2604.18438)
- **2026-04-21**: BG-SINDy: 우세 균형 원리로 다중규모 시스템의 작은 계수 항 보존 [(원문)](https://arxiv.org/abs/2604.18414)
- **2026-04-21**: DiLaR-PINN: 잔차 네트워크를 unmeasurable state에만 적용하고 skew-dissipative 형태로 매개변수화하여 에너지 감소 보장 [(원문)](https://arxiv.org/abs/2604.18277)
- **2026-04-21**: 신경망 연산자 대리 모델의 수렴율 경계 증명: affine-parametric shape encoding을 통한 parametric PDE의 holomorphic 성질 활용 [(원문)](https://arxiv.org/abs/2604.18012)
- **2026-04-21**: Adaptable Symplectic RNN (ASRNN)은 희소·잡음 데이터에서 nonlinear Hamiltonian 동역학계를 안정적으로 학습. 시간 미분 추정 불필요하고 symplectic 구조 보존으로 장기 안정성 보장 [(원문)](https://arxiv.org/abs/2604.17470)
- **2026-04-21**: Fourier Neural Operators를 메타옵틱스 역설계에 적용하여 Maxwell 방정식 풀이 가속화 [(원문)](https://arxiv.org/abs/2604.17425)
- **2026-04-21**: Bayesian PINN + 앙상블 다양성 제어로 난류 역문제 불확도 정량화, 앙상블 다양성과 우도 조정의 역할 규명 [(원문)](https://arxiv.org/abs/2604.17156)
- **2026-04-21**: Late Fusion 아키텍처로 학습된 parameter range 외에서도 PDE 예측 정확도 향상, distribution shift 극복 [(원문)](https://arxiv.org/abs/2604.16721)
- **2025-06-15**: HiPreNets - 순차적 잔차 정제(residual refinement)로 고정밀 신경망 학습 [(원문)](https://arxiv.org/abs/2506.15064)
- **2026-04-20**: 미분 가능 ODE 솔버로 물리 일관성을 강제하면서 SNN 루프와 분리하여 학습 안정성 향상 [(원문)](https://arxiv.org/abs/2604.15714)
- **2026-04-20**: 구조 보존 GNN: 재구성-플럭스 연산자로 설계하여 쌍곡선 보존법칙의 국소 보존성과 shock 구조를 명시적으로 보존 [(원문)](https://arxiv.org/abs/2604.15617)
- **2026-04-20**: PINNACLE: Fourier embedding, 적응 손실 균형, 다중 GPU 병렬화, 양자-고전 하이브리드 아키텍처 통합 지원 [(원문)](https://arxiv.org/abs/2604.15645)
- **2026-04-20**: 아핀 동형 제약을 만족하는 학습 프록시말 네트워크(AE-LPN) 개발 가능 [(원문)](https://arxiv.org/abs/2604.15556)
- **2026-04-20**: secant 정보 기반 적응형 예측 보정으로 첫 번째 최적화기 개선, 수렴 속도와 안정성 향상 (arXiv:2604.15392) [(원문)](https://arxiv.org/abs/2604.15392)
- **2026-04-19**: MEv-SINDy: 한 번의 강제 응답 시간 이력으로부터 비선형 동역학 방정식 추론. MEMS 빔 공진기, 미로 거울에서 소프트닝/경화 및 점프 현상 예측 [(원문)](https://arxiv.org/abs/2604.15181v1)
- **2026-04-17**: PINNs는 물리 제약을 신경망에 통합하여 표현력과 해석 가능성의 균형 달성. 시스템 동정과 매개변수 추정의 분리로 신뢰성 향상 [(원문)](https://arxiv.org/abs/2604.14879)


## 핵심 주체
[[Medical AI]] | [[Clinical AI]]


## 모순/논쟁

