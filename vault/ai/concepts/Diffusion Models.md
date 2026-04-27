---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Diffusion Models

## 정의


## 주요 발전
- **2025-09-20**: 비디오 복원에서 저순위 모델과 확산 후진 샘플링 결합, 배경 제거 성능 향상 [(원문)](https://arxiv.org/abs/2509.20886)
- **2025-02-01**: EAD(Equivariant Asynchronous Diffusion): 비동기 노이징 제거로 분자 계층적 관계 포착 및 SOTA 성능 달성 [(원문)](https://arxiv.org/abs/2603.10093)
- **2026-01-12**: dLLM의 실시간 효율성 이점이 agentic 신뢰성 부족으로 상쇄 → autoregressive 대체 불가능 [(원문)](https://arxiv.org/abs/2601.12979)
- **2025-02-15**: Denoiser output의 norm이 훈련 집합과의 근접도를 인코딩해 프라이버시 취약점 드러냄 [(원문)](https://arxiv.org/abs/2509.25003)
- **2026-04-25**: SE(3) 대칭성을 활용한 Quotient-Space 확산 모델로 분자 구조 생성 시 학습 복잡도 감소 [(원문)](https://arxiv.org/abs/2604.21809v1)
- **2026-04-25**: 조건부 확산 + 질량 보존 제약으로 비디오 초해상도에서 물리 법칙 준수 [(원문)](https://arxiv.org/abs/2604.21903v1)
- **2026-03-03**: Score-matching diffusion models show finite-sample error bounds for intrinsically low-dimensional distributions (Wasserstein distance) without manifold/smooth-density assumptions (arXiv:2603.03700, 2026-03) [(원문)](https://arxiv.org/abs/2603.03700)
- **2025-10-01**: Vision Foundation Models의 frozen representation을 VAE 토크나이저로 직접 활용하면 distillation 대비 표현 강건성 향상 [(원문)](https://arxiv.org/abs/2510.18457)
- **2026-04-24**: 역설계의 one-to-many 매핑 문제를 확산 모델로 해결. 다양한 메타물질 설계안 동시 생성 [(원문)](https://arxiv.org/abs/2507.15753)
- **2026-04-24**: Adaptive moment estimation으로 guided diffusion 샘플링 시 gradient noise 안정화 — 이미지 복원/조건부 생성 SOTA 달성 [(원문)](https://arxiv.org/abs/2603.16797)
- **2026-01**: BackPlay: frozen backbone에서 경량 correction head만 학습, Look-back Correction으로 선택적 리마스킹을 통해 이전 토큰 재검증 [(원문)](https://arxiv.org/abs/2601.06428)
- **2026-04-24**: Appearance/motion의 fine-grained control을 diffusion framework로 구현하여 합성 데이터 검증 가능화 [(원문)](https://arxiv.org/abs/2604.21291)
- **2026-04-24**: 양자 시스템의 궤적 역전 문제를 diffusion score-based framework로 해석 가능함을 증명 [(원문)](https://arxiv.org/abs/2604.21210)
- **2026-04-24**: 제품-of-전문가 프라이어와 베이지안 증거 최대화로 단일 관찰에서 프라이어 튜닝 [(원문)](https://arxiv.org/abs/2604.21066)
- **2026-04-21**: 분자 생성: physics-based docking gradient를 denoising loop에 직접 주입. 4가지 guidance 전략(Vina-Direct, HNN-Denovo, multi-objective, unguided) 중 real-time docking이 최고 성능 [(원문)](https://arxiv.org/abs/2604.20886)
- **2026-04-24**: 확산 모델을 학습-투-랭크 문제에 처음 적용한 생성적 접근 (DenoiseRank) [(원문)](https://arxiv.org/abs/2604.20852)
- **2026-04-21**: 스케일 적응형 spatiotemporal 초해상도로 기후 데이터 업샘플링, 동일 아키텍처 다중 비율 지원 [(원문)](https://arxiv.org/abs/2604.21903)
- **2026-04-21**: Quotient-space 기반 접근으로 SE(3) 대칭성의 학습 효율성 향상 (arXiv:2604.21809) [(원문)](https://arxiv.org/abs/2604.21809)
- **2026-04-24**: Frequency-Forcing은 저주파 구조를 먼저 생성한 뒤 세부 정보를 추가해 이미지 합성 성능 향상 [(원문)](https://arxiv.org/abs/2604.20902)
- **2026-04-22**: Sobolev 메트릭으로 diffusion policy robustness 강화, 궤적 최적화 수렴 가속 (arXiv:2604.19011) [(원문)](https://arxiv.org/abs/2604.19011)
- **2026-04-22**: Gradient-based RL로 Distribution Matching Distillation 성능 개선 (GDMD, arXiv:2604.19009) [(원문)](https://arxiv.org/abs/2604.19009)
- **2026-04-22**: LLM 추론에서 diffusion 역과정으로 다단계 정제 과정 감독 (중간 경로 annotation 없음) [(원문)](https://arxiv.org/abs/2604.18839)
- **2026-04-22**: Masked diffusion LM의 token error correction을 Token-to-Mask(T2M) 방식으로 개선: 의심 토큰을 교체 대신 mask 상태로 reset하여 다음 step에서 올바른 context에서 재예측 [(원문)](https://arxiv.org/abs/2604.18738)
- **2025-12-01**: Discrete/Gaussian/Simplex diffusion을 통일된 수학 프레임워크로 재구성. 각 방식의 장단점(도메인 자연성 vs 알고리즘 성숙도 vs 수치 안정성)을 매개변수화로 해결. [(원문)](https://arxiv.org/abs/2512.15923)
- **2025-08**: Projected Coupled Diffusion (PCD) - test-time 제약조건 강제를 위한 coupled guidance 및 projection step 도입. 재학습 불필요. [(원문)](https://arxiv.org/abs/2508.10531)
- **2025-02-01**: 신경망이 학습하는 평활화된 스코어 함수가 데이터 보간을 유도 (arXiv:2502.19499) [(원문)](https://arxiv.org/abs/2502.19499)
- **2024-01-20**: Denoising score matching으로 추정한 score 함수를 비볼록 신경망+경사강하로 학습할 때도 최적화·일반화 수렴성 보증 가능 [(원문)](https://arxiv.org/abs/2401.15604)
- **2026-04-21**: Uniform Discrete Diffusion Model에 GRPO 적용으로 T2I 성능 획기적 향상. GenEval 정확도 69%→96%, PickScore 상승. [(원문)](https://arxiv.org/abs/2604.18518)
- **2026-04-21**: Zero-shot object grounding in remote sensing via diffusion-guided localization + SAM3 (14% accuracy gain) [(원문)](https://arxiv.org/abs/2604.18201)
- **2026-04-21**: FLUX.1 텍스트-이미지 모델을 LoRA로 미세조정하여 저데이터(클래스당 8-24개) 환경에서 15개 카테고리 군사 차량 감지 성능 향상 [(원문)](https://arxiv.org/abs/2604.18076)
- **2026-04-21**: 음악 생성을 위한 latent-space Fourier transform 활용 (LatentFT, 주파수 기반 제어) [(원문)](https://arxiv.org/abs/2604.17986)
- **2026-04-21**: 정규화 흐름과 Kähler-Ricci flow의 수학적 연결 규명 (미분기하학 기반) [(원문)](https://arxiv.org/abs/2604.17954)
- **2026-04-21**: 비선형 시공간 동역학 시스템 식별에서 noise prediction 대비 clean-space parameterization이 난류 영역에서 더 안정적 (arXiv:2604.17566) [(원문)](https://arxiv.org/abs/2604.17566)
- **2026-04-21**: 조건부 diffusion에서 training-inference input alignment가 프레임워크 선택보다 성능에 큰 영향 (Δ SSIM +0.082, p<0.001) [(원문)](https://arxiv.org/abs/2604.16955)
- **2026-04-21**: Autoregressive VLM을 Diffusion VLM으로 변환(BARD)해 token-by-token 병목 해소, 병렬 디코딩 실현 [(원문)](https://arxiv.org/abs/2604.16514)
- **2026-04-21**: Sensitive Semantic Boundary Modeling으로 자동 발견한 앵커를 기반으로 cross-attention에서 폐곡선 해로 정확 제어 [(원문)](https://arxiv.org/abs/2604.16483)
- **2026-04-21**: Student's t-distribution Mixture Model과 MoE로 기존 수백 개에서 수천 개 개념 삭제 확장 가능 [(원문)](https://arxiv.org/abs/2604.16481)
- **2026-04-21**: 과도한 latent channel은 diffusion 수렴을 방해하므로 고주파 제거로 해결 가능 [(원문)](https://arxiv.org/abs/2604.16479)
- **2026-04-21**: 기체상 반응 동역학 PDE 해결에 물리 기반 확산 샘플링 적용 (arXiv:2604.16461) [(원문)](https://arxiv.org/abs/2604.16461)
- **2026-04-18**: 드리프팅 모델(DMF): 커널 기반 드리프트장으로 원스텝 생성기 학습, 추론 시 ODE 적분 불필요 [(원문)](https://arxiv.org/abs/2604.18194)
- **2026-04-21**: 비볼록 등식/부등식 제약 하에서 diffusion process 수행 가능; landing mechanism으로 projection 제거하여 계산 효율성 증대 (분자/재료 생성) [(원문)](https://arxiv.org/abs/2604.17838)
- **2026-04-21**: Grokking 현상 발견: 과적합 후 타임스텝 임계값을 기준으로 지연된 일반화 발생. 반복 샘플링이 단계적 문제 분해의 메커니즘으로 작동 [(원문)](https://arxiv.org/abs/2604.17673)
- **2026-04-21**: Reward Score Matching: Soft RL, GFlowNets 등 보상 기반 파인튜닝 방법을 점수 매칭 프레임워크로 통합 [(원문)](https://arxiv.org/abs/2604.17415)
- **2026-04-21**: IDDM: Discrete diffusion에서 제어 가능한 재샘플링으로 중간 상태 의존성 감소, 텍스트/그래프 생성 품질 개선 [(원문)](https://arxiv.org/abs/2604.17310)
- **2026-04-21**: 연속 예측 분포의 KL 발산으로 토큰 시간적 불안정성 정량화, Stability-Weighted Decoding으로 병렬 텍스트 생성 정확도 개선 [(원문)](https://arxiv.org/abs/2604.17068)
- **2026-04-21**: 역문제 해결에서 noise-space Hamiltonian MC (N-HMC): local optima 회피 및 다양한 해탐색 가능. manifold infeasibility 해결 [(원문)](https://arxiv.org/abs/2604.16919)
- **2026-04-21**: FRIGID: 질량 분석 스펙트럼→분자 구조 생성에 확산 모델 적용, 추론 시간 스케일링으로 로그선형 정확도 향상 [(원문)](https://arxiv.org/abs/2604.16648)
- **2026-04-21**: RF 신호의 cross-modal generation으로 데이터 희소성 문제 해결 (WiFi→mmWave/RFID) [(원문)](https://arxiv.org/abs/2604.16558)
- **2026-02-02**: 기하학적 변형 + diffusion 프로세스로 단일 이미지에서 다양한 변형 생성하여 few-shot classification 정확도 최대 20% 향상 (training-free, model-agnostic) [(원문)](https://arxiv.org/abs/2602.00114)
- **2025-10-15**: 노이즈 aggregation 분석으로 membership inference 공격에 취약함 확인 [(원문)](https://arxiv.org/abs/2510.21783)
- **2026-04-20**: CRoCoDiL: 마스크 확산을 연속 잠재 표현 공간으로 확장, 토큰 의존성 및 의미 불일치 문제 해결 [(원문)](https://arxiv.org/abs/2603.20210)
- **2026-04-20**: 맥락 인코더와 복합된 비지도 확산 오토인코더로 의료 영상의 미구조적 인공물 제거 가능 [(원문)](https://arxiv.org/abs/2604.15723)
- **2026-04-20**: Block-wise parallel diffusion language model decoding으로 sequence 전체의 global refinement 가능 [(원문)](https://arxiv.org/abs/2604.15750)
- **2026-04-20**: 연속시간 마르코프 체인을 exit rate(언제 점프)와 jump distribution(어디로 점프)으로 분리 매개변수화 (arXiv:2604.15694) [(원문)](https://arxiv.org/abs/2604.15694)
- **2026-04-19**: FP 방정식 편차 페널티 적용 시 계산 비용 대비 효과 미미 (경량 정규화 기법으로 유사 효과 달성 가능) [(원문)](https://arxiv.org/abs/2604.15171v1)
- **2026-02-01**: Bird-SR: 보상 피드백 학습으로 실제 저해상도 이미지의 분포 시프트 문제 해결 [(원문)](https://arxiv.org/abs/2602.07069)
- **2025-09-14**: RFM-Editing: 확산 모델 기반 텍스트 유도 오디오 편집. 복잡한 멀티이벤트 오디오에서 선택적 수정 가능 [(원문)](https://arxiv.org/abs/2509.14003)
- **2025-06-23**: 의료 합성 데이터: 조건부 확산 모델(class-conditioned DDPM)로 초음파 이미지 생성, 연합학습 시 데이터 불균형(non-IID) 완화 [(원문)](https://arxiv.org/abs/2506.23334)
- **2026-04-17**: LWD: 웨이블릿 에너지 맵 기반 주파수 인식 마스킹으로 2K-4K 고해상도 합성의 세부 품질과 텍스처 충실도 개선 [(원문)](https://arxiv.org/abs/2506.00433)
- **2026-04-17**: 표준모형 확장(Type I Seesaw)에서 중성미자 질량 행렬 생성에 확산 모델 적용, Transfer learning으로 중성미자 물리 제약 충족 솔루션 104개 도출 [(원문)](https://arxiv.org/abs/2503.21432)
- **2026-04-17**: Edge-preserving diffusion: 가우시안에서 구조 인식 하이브리드 노이즈로 전환. stroke-to-image 등에서 robustness 개선 (arXiv:2410.01540) [(원문)](https://arxiv.org/abs/2410.01540)
- **2025-06-13**: 확산 모델의 최적 손실값을 폐쇄형으로 도출하고, 대규모 데이터셋에 적용 가능한 확률론적 추정기 개발. 이를 통해 훈련 품질 진단 및 스케줄 최적화로 120M~1.5B 모델 성능 개선 [(원문)](https://arxiv.org/abs/2506.13763)
- **2024-11-01**: DiffGap: 3D 분자 생성에서 exposure bias와 error accumulation 해결. Adaptive alignment와 temperature annealing으로 중간 denoising step을 현실적 궤적에 정렬 [(원문)](https://arxiv.org/abs/2411.05472)
- **2026-04-17**: 경량 정규화로 Fokker-Planck 위반 최소화, 생성 품질 유지하며 계산 비용 감소 [(원문)](https://arxiv.org/abs/2604.15171)
- **2026-04-17**: 비디오 아웃페인팅에서 flow-based 전파와 generation 통합 프레임워크 (Seen-to-Scene) [(원문)](https://arxiv.org/abs/2604.14648)
- **2026-04-17**: 생성 확산 모델을 이용한 개인화 학습 경로 추천(U-GLAD): 불확실성 인식 + 인지 적응 [(원문)](https://arxiv.org/abs/2604.14613)
- **2026-04-14**: Diffusion Crossover: 노이즈 시퀀스 구면선형보간(Slerp)으로 확산 모델의 의미론적 교배 연산 정의. 대화형 진화 계산의 고차원 표현 문제 해결. [(원문)](https://arxiv.org/abs/2604.14790)
- **2026-04-17**: 스텝 레벨 RL과 다중 목표 최적화를 결합한 디노이징 정렬 방법 [(원문)](https://arxiv.org/abs/2604.14379)
- **2026-04-17**: Thermodynamic diffusion inference로 에너지 10,000배 감소 [(원문)](https://arxiv.org/abs/2604.14332)


## 핵심 주체
[[Medical AI]]


## 모순/논쟁

