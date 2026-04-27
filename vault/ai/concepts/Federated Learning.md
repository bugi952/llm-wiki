---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Federated Learning

## 정의


## 주요 발전
- **2025-08-15**: 비선형 시스템 식별에 연합학습 적용 시 클라이언트 증가에 따라 수렴 속도 개선, 중앙화 접근과 동등 이상 성능 [(원문)](https://arxiv.org/abs/2508.15025)
- **2026-04-27**: FedSPDnet: SPD 매트릭스 기반 federated learning 프레임워크. Stiefel manifold 구조 보존으로 신호처리 응용 정확도 향상 [(원문)](https://arxiv.org/abs/2604.22494)
- **2026-04-22**: GradsSharding: gradient를 M개 샤드로 분할하여 각 serverless 함수에서 독립 평균화, 메모리 O(|θ|/M)로 축소 [(원문)](https://arxiv.org/abs/2604.22072)
- **2026-04-27**: Spectral entropy 기반 privacy-preserving 클라이언트 기여도 평가 (SpectralFed, SpectralFuse) [(원문)](https://arxiv.org/abs/2604.22562)
- **2025-10-01**: 수술 영상(복강경 충수절제술)에 FL 적용: 중앙화 학습 기준 26.31% F1, 분리화 학습의 추가 성능 저하로 다중심 일반화 문제 제시 [(원문)](https://arxiv.org/abs/2510.04772)
- **2024-11-11**: 경량 어댑터를 통한 LLM-SLM 양방향 지식 교환으로 프라이버시 보존 + 오버헤드 최소화 [(원문)](https://arxiv.org/abs/2411.11707)
- **2026-04-22**: Proxy SLM 기반 페더레이션 LLM 파인튜닝으로 성능-프라이버시 트레이드오프 개선 (FedProxy, arXiv:2604.19015) [(원문)](https://arxiv.org/abs/2604.19015)
- **2025-12-01**: 분산 연합 학습에서 목표 지향적 가중치 재조정으로 fairness와 Byzantine robustness 동시 달성하는 DFedReweighting 프레임워크 제안. [(원문)](https://arxiv.org/abs/2512.12022)
- **2026-04-21**: IoT 엣지 환경에서 federated learning은 privacy 향상, single point of failure 제거, adaptive threat response 개선을 제공하나, 리소스 제약과 heterogeneous devices에서 확장성 문제 잔존 [(원문)](https://arxiv.org/abs/2604.17179)
- **2025-02-01**: SafeLM: gradient smartification + Paillier 암호화로 privacy 보존하며 gradient inversion PSNR 31.7dB → 15.1dB 감소 [(원문)](https://arxiv.org/abs/2604.16606)
- **2026-04-21**: 위성 constellation에서의 federated learning: 동적 위성간 연결, SWaP-C 제약, 방사선 장애 고려 [(원문)](https://arxiv.org/abs/2604.16518)
- **2026-04-21**: Non-iid 데이터 분포에서 diverse/discriminative representation을 동시에 확보하는 distributed optimization framework 제시. 표현 분산 제약을 통한 전역 최적화 함수 개선 [(원문)](https://arxiv.org/abs/2604.18237)
- **2026-04-21**: RuleFit 기반 연합 학습으로 해석 가능한 글로벌 모델 구축, differentially private histograms로 클라이언트 간 규칙 동기화 [(원문)](https://arxiv.org/abs/2604.17956)
- **2026-04-21**: Zeroth-order 최적화 기반 federated RLHF로 엣지 디바이스 효율성 개선 (Par-S²ZPO) [(원문)](https://arxiv.org/abs/2604.17747)
- **2026-04-21**: FedLLM: 교통 흐름 예측에서 지역별 데이터 중앙화 없이 분산 학습 + 설명 가능성 결합 [(원문)](https://arxiv.org/abs/2604.16612)
- **2026-04-21**: Element-wise importance scoring (OBD 기반)으로 최적 parameter 선택 (FedOBP 알고리즘) [(원문)](https://arxiv.org/abs/2604.16574)
- **2025-02-20**: 독재자 클라이언트가 다른 모든 클라이언트 기여를 말소하며 자신의 기여만 보존하는 공격 전략의 분석적 분류 [(원문)](https://arxiv.org/abs/2510.22149)
- **2026-04-20**: Random Walk 기반 다중 스트림(Multi-Walk) 알고리즘은 큰 지름의 그래프 토폴로지에서 Asynchronous Gossip보다 반복 수렴에서 우수 [(원문)](https://arxiv.org/abs/2504.09792)
- **2026-04-20**: FedPL 프로토타입이 거리만 최대화할 때 클래스 간 의미 관계 손상; 텍스트 시멘틱 가이드로 해결 [(원문)](https://arxiv.org/abs/2503.13543)
- **2026-04-20**: PSP 동기화에서 장애 있는 장치로 인한 특정 클래스 과소대표. 노드 가용성과 데이터 분포 상관관계 문제 연구 [(원문)](https://arxiv.org/abs/2604.16090)
- **2026-04-20**: QLSTM: 양자-고전 하이브리드 LSTM으로 고에너지 물리학 데이터의 분산 학습 구현 [(원문)](https://arxiv.org/abs/2604.15775)
- **2026-04-20**: SGP (Stochastic Gradient Push) for 무선 DFL: 비대칭 믹싱 행렬 허용으로 directed communication graph 지원, D-PSGD의 symmetric/doubly stochastic 제약 극복 [(원문)](https://arxiv.org/abs/2604.15549)
- **2026-04-19**: FedIDM: 분포 매칭 기반 condensed data로 Byzantine 공격 탐지/필터링, 악의적 클라이언트 다수 환경에서도 안정적 수렴과 모델 유효성 유지 [(원문)](https://arxiv.org/abs/2604.15115v1)
- **2025-06-23**: Federated Learning의 의료 응용: 민감한 환자 데이터 중앙화 회피, 합성 데이터 증강으로 비균등 분포 문제 해결, 단 과도한 합성 데이터는 성능 저하 위험 [(원문)](https://arxiv.org/abs/2506.23334)


## 핵심 주체
[[AI in Systems Engineering]]


## 모순/논쟁

