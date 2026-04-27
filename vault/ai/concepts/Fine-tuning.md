---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Fine-tuning

## 정의


## 주요 발전
- **2025-11-18**: 커리큘럼 학습은 상수 학습률에서만 효과적이며, 표준 감소 스케줄 하에서는 이점이 사라지는 현상 발견 [(원문)](https://arxiv.org/abs/2511.18903)
- **2026-04-27**: 하이브리드 언어모델(Attention+SSM)에서 어텐션 경로 LoRA만으로 전체 모델 대비 5-10배 효율 달성, 순차 vs 병렬 구조에 따라 SSM 적응 효과 상이 (Qwen3.5, Falcon-H1) [(원문)](https://arxiv.org/abs/2604.22127)
- **2026-04-25**: GiVA (Gradient-Informed Bases for Vector-based Adaptation)로 벡터 기반 적응의 rank를 8배 감소시켜 LoRA 성능 달성 [(원문)](https://arxiv.org/abs/2604.21901v1)
- **2026-04-25**: 신호처리 원리(저랭크 모델링, 역문제)로 LoRA 및 어댑터 설계 원칙 설명 [(원문)](https://arxiv.org/abs/2604.21905v1)
- **2026-02-03**: sensorimotor norms 예측을 위한 projection model 기반 learned mapping 방식 적용 [(원문)](https://arxiv.org/abs/2602.00469)
- **2026-04-24**: GeoRA는 RLVR의 distinct optimization dynamics를 반영하여 LoRA의 RLVR 적응성 향상 [(원문)](https://arxiv.org/abs/2601.09361)
- **2026-04-24**: RIFT는 RFT의 hard thresholding 대신 모든 self-generated samples을 reward로 재가중치화하여 활용 [(원문)](https://arxiv.org/abs/2601.09253)
- **2025-09**: HyperAdapt: 대각 행렬의 행·열 스케일링으로 n×m 행렬에 대해 n+m개 파라미터만으로 고차원 업데이트 달성 [(원문)](https://arxiv.org/abs/2509.18629)
- **2025-05-01**: Fine-tuning 중 무해 데이터에서도 safety 저하 위험. Safety/task-performance 손실 지형이 부분적 decoupling으로 unsafe 영역으로의 이동 발생 [(원문)](https://arxiv.org/abs/2505.16737)
- **2025-05-01**: Post-training 단계에서 MLP adapter를 latent space 부착으로 augmentation 불변성 추가. 원본 입력 분포 성능 유지 [(원문)](https://arxiv.org/abs/2505.11702)
- **2025-03-20**: 도메인 특화 파인튜닝이 안전성 정렬 훼손 문제, 선택적 머징으로 해결 가능 [(원문)](https://arxiv.org/abs/2503.17239)
- **2024-11-11**: 연합 시나리오에서 파라미터 효율적 어댑터 기반 파인튜닝으로 SLM 강화 [(원문)](https://arxiv.org/abs/2411.11707)
- **2024-10-16**: 다국어 순차 파인튜닝 시 Phase 간 작업 유사성이 모델 적응성 결정 [(원문)](https://arxiv.org/abs/2410.16006)
- **2026-04-21**: 도메인 특화 미세조정 시 생성된 합성 데이터 혼합 사용으로 언어 벤치마크 성능 저하 완화, 멀티모달 LLM에서 효과 두드러짐 [(원문)](https://arxiv.org/abs/2406.11354)
- **2026-04-24**: Projected optimization 관점: trainable subspace 깊이 변화가 update signal을 변경, CL 평가 결과 영향 [(원문)](https://arxiv.org/abs/2604.21927)
- **2026-04-24**: 신호처리 이론 관점의 LoRA 재해석: 저랭크 모델링과 역문제로 아키텍처 선택 원칙화 [(원문)](https://arxiv.org/abs/2604.21905)
- **2026-04-21**: Gradient 기반 초기화로 파라미터 효율적 미세조정 순위 최소화, NLU/NLG/이미지 분류 검증 [(원문)](https://arxiv.org/abs/2604.21901)
- **2026-04-21**: 음악과 시가 모델의 내부 계산과 임베딩을 직교적으로 개선하며 수렴 속도 가속화 [(원문)](https://arxiv.org/abs/2604.21265)
- **2026-04-24**: 도메인 특화 파인튜닝으로 온라인 리뷰 관리 자동화 가능, preference alignment로 할루시네이션과 보수주의 문제 해결 [(원문)](https://arxiv.org/abs/2604.21209)
- **2026-04-20**: Rényi divergence 기반 자기대조 학습(IRIS)으로 학습 단계별 최적 divergence 자동 조정 [(원문)](https://arxiv.org/abs/2604.20933)
- **2026-04-22**: 경량 어댑터 대신 압축 SLM으로 분산 학습 성능 격차 해소 [(원문)](https://arxiv.org/abs/2604.19015)
- **2026-04-21**: LoRA on the Go (LoGo): 라벨링/추가 훈련 없이 단일 순전파로 인스턴스별 LoRA 동적 선택/병합 [(원문)](https://arxiv.org/abs/2511.07129)
- **2026-04-21**: ConMeZO: 콘 중심 샘플링으로 0차 최적화 수렴 속도 2배 가속 [(원문)](https://arxiv.org/abs/2511.02757)
- **2025-10-14**: 2025년 합성 코퍼스 분석: 기존 '해로운' 것으로 여겨진 데이터 특성들(반복, inconsistency)이 robust knowledge utilization의 필수조건 [(원문)](https://arxiv.org/abs/2510.02370)
- **2026-04-21**: LLM-as-judge 패러다임에서 fine-tuned 판사가 더 작은 모델로 높은 성능과 편향 강건성 제공 [(원문)](https://arxiv.org/abs/2509.23542)
- **2026-04-21**: BEFT (Bias-Efficient Fine-tuning): value projection bias (b_v)의 직접 fine-tuning이 query/key bias보다 저자원 레짐에서 우수, 6.7B까지 검증 [(원문)](https://arxiv.org/abs/2509.15974)
- **2025-08-01**: Bi-LoRA: auxiliary LoRA로 SAM weight perturbation 분리, sharpness 최적화 개선 (2025-08 arXiv) [(원문)](https://arxiv.org/abs/2508.19564)
- **2025-06-15**: PrefixMemory-Tuning으로 Attention 헤드에서 Prefix 분리, 현대 LLM 적응 효율 개선 (arXiv:2506.13674) [(원문)](https://arxiv.org/abs/2506.13674)
- **2026-04-21**: LIFT: 추론 능력 향상 SFT에서 저자원 환경 미세조정 시 rank reduction 전처리 후 주요 가중치 선택이 magnitude-based baseline 대비 크게 효과적 [(원문)](https://arxiv.org/abs/2506.00772)
- **2026-04-21**: SEFT: 미세조정 중 가중치 드롭-성장으로 희소 토폴로지를 동적 진화시켜 전체 희소성 유지 [(원문)](https://arxiv.org/abs/2505.24037)
- **2024-12-02**: 파인튜닝 단계에서 불확실성 보정을 통해 정확도 유지하며 신뢰도 동시 향상 가능 [(원문)](https://arxiv.org/abs/2412.02904)
- **2024-10-05**: SFTMix: 훈련 동역학으로 confidence 레벨 기반 샘플 구분, 데이터 필터링 불필요 [(원문)](https://arxiv.org/abs/2410.05248)
- **2026-04-21**: Edge replica 간 co-execution으로 federated PEFT 효율 증진 (CoLLM) [(원문)](https://arxiv.org/abs/2604.16400)
- **2026-04-21**: Zeroth-order optimization으로 forward pass만 사용. Multi-Armed Bandit 기반 계층별 적응 샘플링으로 섭동·업데이트 지연 40% 감소 [(원문)](https://arxiv.org/abs/2604.18264)
- **2026-04-21**: SVD 기반 태스크 인식 초기화로 LoRA A 행렬을 입력 활성화 공분산 부분공간에 정렬 (TLoRA) [(원문)](https://arxiv.org/abs/2604.18124)
- **2026-04-21**: 저순위 적응의 가지(branch)를 양자화하여 매개변수 효율성 극대화 [(원문)](https://arxiv.org/abs/2604.18117)
- **2026-04-21**: HiP-LoRA: SVD 기반 spectral plasticity로 pretrained 능력 보존 및 catastrophic forgetting 방지 [(원문)](https://arxiv.org/abs/2604.17751)
- **2026-04-21**: 도메인 특화 파인튜닝이 이전 도메인의 안전 가드레일을 침식. LoRA 직교 보수 제약으로 안전성 유지 [(원문)](https://arxiv.org/abs/2604.17691)
- **2026-04-21**: Data-Parameter Correspondence: 데이터 가지치기와 파라미터 희소화는 Fisher-Rao metric에서 쌍대 연산 [(원문)](https://arxiv.org/abs/2604.17384)
- **2026-04-21**: REALM: 어노테이터별 scalar expertise를 unsupervised 학습으로 습득; identity 정보만으로 신뢰도 추출 (다중 QA 벤치마크 검증) [(원문)](https://arxiv.org/abs/2604.17289)
- **2026-04-21**: Contrastive pre-finetuning에서 representation regularization으로 task bias 제어 및 embedding geometry 보존 가능 [(원문)](https://arxiv.org/abs/2604.17257)
- **2026-04-21**: 240개 fine-tuning 실험(125M~6.9B, 4개 아키텍처)으로 표현 변화 깊이 프로필의 아키텍처-작업 의존성 규명, 그래디언트 흐름 vs 모델 내재 특성의 구분 [(원문)](https://arxiv.org/abs/2604.17177)
- **2026-04-21**: 핵심/비핵심 매개변수 구분으로 도메인 적응 중 일반 능력 보존 [(원문)](https://arxiv.org/abs/2604.17051)
- **2026-04-21**: 다중 작업 LoRA 어댑터 머징 시 task-specific 정보 보존을 위한 B-space 캘리브레이션 필요 [(원문)](https://arxiv.org/abs/2604.16826)
- **2026-04-21**: CALIBER: 컨텍스트 인식 저자원 Bayesian LoRA로 예측 신뢰도 및 크로스모달 신뢰성 동시 달성 [(원문)](https://arxiv.org/abs/2604.16657)
- **2026-04-21**: 어휘 확장(vocab expansion)은 추가할 토큰 항목 선택과 임베딩 초기화 전략이 효과 결정 [(원문)](https://arxiv.org/abs/2604.16656)
- **2026-04-21**: CoCo-LoRA: 저랭크 어댑터에 오디오 컨텍스트 조건화로 음성(배경음, 채널, 톤)의 불확실성 정량화 [(원문)](https://arxiv.org/abs/2604.16615)
- **2026-04-21**: Matched learning rate 비교: Full FT vs LoRA, 동일 LR에서 Full FT는 entropy 수렴/확장 극단, LoRA는 전체 범위서 양수 유지 [(원문)](https://arxiv.org/abs/2604.16410)
- **2026-04-21**: LoRA 파인튜닝에서 높은 주석 엔트로피 예제는 훈련 중 손실 증가하는 역학습 패턴, 전체 파인튜닝에서 거의 없음. 디코더 모델이 더 강한 상관 [(원문)](https://arxiv.org/abs/2604.16332)
- **2026-02-15**: 학생 모델이 교사 모델을 무단 증류할 때 성능 저하를 유도하는 anti-distillation 기법 적용 [(원문)](https://arxiv.org/abs/2602.15143)
- **2025-10**: 제한된 계산 예산 하에서 DP fine-tuning의 배치 크기 선택은 누적 DP 노이즈로 설명 가능 [(원문)](https://arxiv.org/abs/2510.20616)
- **2025-04-20**: SAI-DPO를 통한 자가 인식 동적 샘플링으로 수학 추론 효율성 개선 [(원문)](https://arxiv.org/abs/2505.16176)
- **2026-04-20**: UA-Net: ImageNet 사전학습 → TRISO 미세사진 도메인 파인튜닝 → 메타모델 기반 불확실성 예측 [(원문)](https://arxiv.org/abs/2604.15542)
- **2026-04-20**: Multi-agent 기반 고품질 테스트벤치 자동화로 파인튜닝 데이터 양 감소 가능 (2026-04-20) [(원문)](https://arxiv.org/abs/2604.15388)
- **2026-04-20**: DeepInsightTheorem 데이터셋: 증명 작성 → insightful thinking 진화 학습, human learning process 모방 [(원문)](https://arxiv.org/abs/2604.16278)
- **2026-04-20**: 크로스모달 그래디언트 비대칭 문제 해결을 위한 계층별 직교 그래디언트 투영 기법 [(원문)](https://arxiv.org/abs/2604.16067)
- **2026-04-20**: Chain-of-Thought 증류 계열에서 대부분의 의미론적 다양성 손실은 지도 학습 단계에서 발생 [(원문)](https://arxiv.org/abs/2604.16027)
- **2026-04-20**: MLLM 강화학습 미세조정 시 내생적 추론 드리프트 발견: 외생적 변화와 구별, 자동회귀 생성 중 예측 불가능한 분포 변화 [(원문)](https://arxiv.org/abs/2604.15705)
- **2026-04-20**: FFT는 LoRA/QLoRA 대비 통계적으로 다른 집중도 높은 귀속 패턴 생성 [(원문)](https://arxiv.org/abs/2604.15589)
- **2026-04-20**: 자체-증류 기반 fine-tuning으로 출력 분포 변화 제약하여 hallucination 억제 가능 [(원문)](https://arxiv.org/abs/2604.15574)
- **2026-04-20**: Layer selection probe로 task-relevant layer만 LoRA 적용 시 학습 속도 15-28% 향상 [(원문)](https://arxiv.org/abs/2604.15351)
- **2026-04-17**: SLM 리랭킹에 두 단계 학습(RL 프롬프트 + 세분화 점수)로 좁은 표현 공간 극복 [(원문)](https://arxiv.org/abs/2506.03487)
- **2026-04-17**: Post-training 분류: off-policy(외부 궤적) vs on-policy(모델 생성 롤아웃)로 체계화 (arXiv:2604.07941) [(원문)](https://arxiv.org/abs/2604.07941)
- **2026-04-17**: Llama 1.3B까지 hybrid 구조에서 SAGE 적용 시 메모리 효율성 개선 (arXiv:2604.07663) [(원문)](https://arxiv.org/abs/2604.07663)
- **2026-04-17**: 표준→방언 전이학습에서 음성 모델이 텍스트 모델보다 우월, 자동 음성인식 정규화 필수 [(원문)](https://arxiv.org/abs/2510.07890)
- **2026-04-17**: SPaCe: 자기 속도 커리큘럼 학습으로 LLM RL 훈련의 표본 효율성 극대화, 데이터 중복도 제거 [(원문)](https://arxiv.org/abs/2508.05015)
- **2025-02-01**: 2025-02: 공중 여론조사 데이터(SubPOP 3,362Q/70K 응답쌍) 파인튜닝으로 인간-LLM 응답 분포 격차 46% 축소 [(원문)](https://arxiv.org/abs/2502.16761)
- **2026-04-17**: Retention-prioritized gradient synthesis: target 지식 제거 시 일반 능력 보존 최적화 [(원문)](https://arxiv.org/abs/2604.14808)
- **2026-04-17**: Kronecker 제약으로 무게 템플릿과 크기별 스케일러 분리, 가변 크기 초기화 문제를 멀티태스크 적응으로 변환 [(원문)](https://arxiv.org/abs/2604.14769)
- **2026-04-17**: 불확실성 기반 CoT 자체 합성으로 강모델 증류 및 테스트타임 탐색의 계산 부담 완화 [(원문)](https://arxiv.org/abs/2604.14768)
- **2026-04-17**: 메모리 효율적 대규모 모델 미세조정 시 ZO 방법의 안정성 조건 수립 [(원문)](https://arxiv.org/abs/2604.14669)
- **2026-04-17**: BabyLM 데이터로 훈련한 LM도 wh-question과 topicalization 간 filler-gap 표현 이전 가능, 인간 수준 일반화엔 훨씬 더 많은 데이터 필요 [(원문)](https://arxiv.org/abs/2604.14459)
- **2026-04-17**: Group Fine-Tuning(GFT): SFT를 극도로 희소한 암시 보상을 가진 정책 그래디언트 특수 사례로 재해석. 그룹 어드밴티지 러닝으로 응답 그룹 구성 후 정규화된 대조 감독 적용 [(원문)](https://arxiv.org/abs/2604.14258)
- **2026-04-14**: QLoRA + Rank-Stabilized LoRA(r=32)로 8B 오픈소스 모델의 네팔어 이해도 향상 [(원문)](https://arxiv.org/abs/2604.14171)
- **2026-04-17**: 교사-학생 협력 데이터 합성(TESSY): 교사 모델의 추론 능력 보존하면서 합성 시퀀스의 스타일을 학생 모델 분포와 정렬하여 미세조정 성능 저하 문제 해결 [(원문)](https://arxiv.org/abs/2604.14164)


## 핵심 주체
[[Dynamic Data Selection for Training]]


## 모순/논쟁

