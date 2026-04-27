---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# State Space Models

## 정의


## 주요 발전
- **2025-11-17**: SSM과 선형 변환기에서 실수부는 망각, 허수부는 위치 인코딩 회전을 담당 [(원문)](https://arxiv.org/abs/2511.17388)
- **2024-11**: HMM을 differentiable forward filter로 구현하면 interpretability 확보 가능 (Belief Net) [(원문)](https://arxiv.org/abs/2511.10571)
- **2025-02-15**: StateX: post-training state expansion으로 parameter 증가 최소화하며 recall 능력 향상 (arXiv:2509.22630) [(원문)](https://arxiv.org/abs/2509.22630)
- **2026-04-21**: CSI(채널 상태 정보) 예측에서 SSM 기반 MambaCSP는 트랜스포머 대비 선형 시간 복잡도로 메모리/지연시간 대폭 절감 [(원문)](https://arxiv.org/abs/2604.21957)
- **2026-04-27**: Sparse softmax와 sparse linear attention 조합으로 5B 모델의 long-context 효율성 달성 [(원문)](https://arxiv.org/abs/2604.22575)
- **2026-04-27**: 곤충 신경계의 modular decomposition(sensory encoding, heading representation, memory, command generation, motor control)이 distributed control 구현 (2026-04-22) [(원문)](https://arxiv.org/abs/2604.22081)
- **2026-04-24**: MMAF-guided learning: 시간-공간 상관성을 enforced constraint로 인코딩한 확률론적 Bayesian 신경망 앙상블 [(원문)](https://arxiv.org/abs/2603.15055)
- **2026-04-24**: Linear RNN이 permutation composition 및 code state-tracking에서 Transformer보다 우수한 성능 입증 [(원문)](https://arxiv.org/abs/2602.14814)
- **2025-07-01**: 경량 엣지 디바이스용 멀티스케일 시퀀스 모델링 (mGRADE: 게이트 순환+지연 임베딩 하이브리드) [(원문)](https://arxiv.org/abs/2507.01829)
- **2026-04-24**: OLS 기반 LDS 파라미터 추정에서 state-dimension 과다 계산 오류 시정 [(원문)](https://arxiv.org/abs/2604.21270)
- **2026-04-24**: 하이브리드(attention+recurrent state) 아키텍처가 순차 의존성 높은 작업에서 순수 attention 모델보다 견고 [(원문)](https://arxiv.org/abs/2604.21454)
- **2026-04-24**: Preconditioned DeltaNet이 온라인 최소제곱 프레임워크에서 선형 리커런스의 사전처리로 성능 향상. 정확 사전처리 시 선형 어텐션-델타 규칙 동치성 증명 [(원문)](https://arxiv.org/abs/2604.21100)
- **2026-04-24**: Apple ParaRNN: RNN 병렬 학습으로 대규모 모델 학습 가능 [(원문)](https://machinelearning.apple.com/research/large-scale-rnns)
- **2026-04-21**: Semi-CRF는 segment 특징과 경계 불확실성 추정 가능. Flash-SemiCRF의 prefix-sum lookup으로 메모리를 시퀀스 길이×라벨수 비례에서 상수로 감소 [(원문)](https://arxiv.org/abs/2604.18780)
- **2025-12**: 신경 진동자의 균등 점근 증분 안정성을 갖는 2차 동적 시스템 근사 능력 이론적 정량화 [(원문)](https://arxiv.org/abs/2512.01015)
- **2025-10-07**: MeSH 스키마로 상태 관리를 명시적 메모리 버퍼로 외부화, 동적 라우터로 반복 간 계산 다양화 [(원문)](https://arxiv.org/abs/2510.07739)
- **2025-06-15**: 음성 처리에서 SSM의 streaming, long-context 성능 및 화자 특성 포착 능력 우수 [(원문)](https://arxiv.org/abs/2506.12606)
- **2026-04-21**: 대각 상태 전이의 한계(낮은 메모리 유지, 제한된 이중선형 계산)를 bilinear input modulation으로 극복 [(원문)](https://arxiv.org/abs/2604.17221)
- **2026-04-21**: S4, S4D, DSS, S5, Mamba, Mamba-2, Jamba 등 SSM 아키텍처에 대한 첫 체계적 보안 분석. 스펙트럼 공격(전달함수 이득 악용), 지연 트리거 상태 백도어(주입 후 수천 스텝 후 활성화), 상태 용량 공격 3가지 신규 위협 확인 [(원문)](https://arxiv.org/abs/2604.16424)
- **2026-04-21**: Sessa로 SSM에 선택적 어텐션 통합, 다중 읽기-쓰기 경로 실현 (2026-04-21) [(원문)](https://arxiv.org/abs/2604.18580)
- **2026-04-18**: 수직 청크 기반 추론으로 메모리 복잡도를 입력길이 이상에서 상수로 축소 가능 [(원문)](https://arxiv.org/abs/2604.18199)
- **2026-04-21**: UniMamba로 효율적 상태공간 동역학과 Attention 의존성 학습 통합, 다변량 시계열의 변수 간 상호작용 명시화 [(원문)](https://arxiv.org/abs/2604.16325)
- **2026-04-20**: OLMo Hybrid 7B: Gated DeltaNet 사용, pure transformer 대비 성능 향상 (arXiv:2604.03444) [(원문)](https://arxiv.org/abs/2604.03444)
- **2026-04-20**: Mamba, S5, Jamba 등 최신 SSM 변형이 선형 계산 복잡도 유지하면서 긴 문맥 처리 능력 향상 [(원문)](https://arxiv.org/abs/2503.18970)
- **2026-04-20**: Mamba는 WSI(병리 이미지) 분석에서 Transformers보다 효율적이면서 글로벌 컨텍스트 모델링 [(원문)](https://arxiv.org/abs/2604.15729)
- **2026-04-20**: Vision Transformer 대비 계산 오버헤드 감소와 세밀한 병리 특징 추출 [(원문)](https://arxiv.org/abs/2604.15711)
- **2026-04-19**: MambaSL: 선택적 SSM과 projection 레이어를 TSC 최적화해 30개 UEA 데이터셋에서 SOTA. 20개 베이스라인을 통일 프로토콜로 재평가 [(원문)](https://arxiv.org/abs/2604.15174v1)
- **2026-04-17**: 멀티레이어 SSM은 compositional task에서 근본적 한계 존재, online Chain-of-Thought 적용 시 streaming 알고리즘과 동등 expressive power 달성 [(원문)](https://arxiv.org/abs/2604.14501)


## 핵심 주체
[[Attention mechanisms]]


## 모순/논쟁

