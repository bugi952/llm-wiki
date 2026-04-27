---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Mixture of Experts

## 정의


## 주요 발전
- **2025-05-01**: 30B부터 718B까지 대규모 MoE 모델을 PreMoE로 최대 50% sparsity 달성하면서도 성능 손실 최소화 가능 (도메인 특화 전문가 모델 또는 다중 도메인 범용 모델) [(원문)](https://arxiv.org/abs/2505.17639)
- **2026-04-24**: MoE 모델 양자화에서 합성 데이터 활용으로 성능 유지 가능 입증 (Nvidia Nemotron 해커톤) [(원문)](https://www.aitimes.com/news/articleView.html?idxno=209720)
- **2025-02-20**: 신경망 활성화 패턴 분석으로 기존 FFN을 sparse MoE로 post-training 변환 가능 [(원문)](https://arxiv.org/abs/2502.04416)
- **2026-04-24**: 이중 데이터 플라이휠(추론+agentic): 선형 워크플로우를 다중분기 행동트리로 확장해 실제 의사결정 복잡도 반영 [(원문)](https://arxiv.org/abs/2604.21590)
- **2026-04-21**: 카테고리 임베딩 기반 동적 가중치 할당으로 유사 candidate-job 쌍 구별 (AUC +2.4%) [(원문)](https://arxiv.org/abs/2604.21264)
- **2026-04-21**: MoE sparse activation은 효율성 개선하나, expert routing 동적 형태 + 불규칙 연산(top-k, scatter/gather)이 NPU 제약과 충돌. NPUMoE는 dense computation NPU 오프로드로 해결. [(원문)](https://arxiv.org/abs/2604.18788)
- **2026-04-21**: PiERN (Physically-isolated Experts Routing Network): token-level routing으로 computational experts와 reasoning을 단일 chain-of-thought 내 내생적으로 통합, multi-agent overhead 제거 [(원문)](https://arxiv.org/abs/2509.18169)
- **2025-02-01**: 클러스터 분리 최적화를 통한 라우터 성능 개선 방법 제시 (arXiv:2502.15315) [(원문)](https://arxiv.org/abs/2502.15315)
- **2026-04-21**: 객체 탐지 도메인에서 MoE 모델 적용 시 YOLO 기반 전문가와 동적 게이팅 네트워크로 전문가 기여도 동적 가중치 조정 [(원문)](https://arxiv.org/abs/2604.18256)
- **2026-04-21**: Qwen3.5-35B (256 routed experts, top-8) shared-prefix code generation에서 동일 토큰 위치의 layer-wise 라우팅 Jaccard similarity 0.649 (40배 random), 서로 다른 토큰도 0.175 (11배 random)로 높은 routing locality 확인 [(원문)](https://arxiv.org/abs/2604.17182)
- **2026-04-21**: CoGR-MoE: 답변 선택지의 의미론을 활용한 개념 가이드 라우팅으로 시각 질문 답변의 전문가 선택 일관성 향상 [(원문)](https://arxiv.org/abs/2604.16930)
- **2026-04-21**: BAR: 도메인별 전문가를 독립 중간-SFT-RL 파이프라인으로 학습 후 MoE 라우터로 통합 [(원문)](https://arxiv.org/abs/2604.18473)
- **2026-04-21**: 각 MoE 계층의 hidden state는 라우팅을 구동하는 저대역폭 제어 신호와 내용 채널(언어/위치)로 분해 가능; 라우팅 단순성이 layer 간 구성적 전문화 강제 [(원문)](https://arxiv.org/abs/2604.17837)
- **2026-04-21**: 라우팅 메커니즘을 KV 캐시 압축 방식 선택에 적용. 전역 메모리 예산 제약 하 정확도 손실 최소화 [(원문)](https://arxiv.org/abs/2604.17695)
- **2026-04-19**: DeepSeek V4가 MoE로 미국 수출 규제 속 최고 성능 달성 [(원문)](https://www.aitimes.com/news/articleView.html?idxno=209507)
- **2025-11-01**: MoA 프레임워크로 하드웨어 설계(RTL/HDL) 자동화 달성 - 품질 기반 캐싱으로 노이즈 감소 [(원문)](https://arxiv.org/abs/2510.27617)
- **2026-04-20**: billion-parameter 물리 모델에서 1.2 EFLOPS 성능, 90% 병렬 효율 [(원문)](https://arxiv.org/abs/2604.15821)
- **2026-04-20**: Qwen3.5-Omni Thinker/Talker에 Hybrid Attention MoE 적용, 장문 추론 효율성 개선 [(원문)](https://arxiv.org/abs/2604.15804)
- **2026-04-17**: Expert specialization은 probability simplex의 Fisher Information metric으로 정량화 가능, specialization은 Riemannian geodesic flow로 형식화됨 [(원문)](https://arxiv.org/abs/2604.14500)


## 핵심 주체
[[Model Efficiency]] | [[Cost-Aware Model Selection]] | [[Runtime-Adaptive Model Compression]]


## 모순/논쟁

