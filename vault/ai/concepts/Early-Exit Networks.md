---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Early-Exit Networks

## 정의


## 주요 발전
- **2026-04-18**: 2D 조기 종료(센텐스+레이어 결합)로 곱셈적 계산 절감, 최적 레이어별 조기 종료 대비 1.4-2.3배 속도 향상 (arXiv 2604.18592) [(원문)](https://arxiv.org/abs/2604.18592)
- **2026-04-21**: River-LLM: KV cache 공유로 token-level early exit 구현, training-free, 지연 오버헤드 제거 (arXiv 2604.18396) [(원문)](https://arxiv.org/abs/2604.18396)
- **2026-04-21**: answer consistency + confidence trajectory 조합으로 정확한 종료 시점 결정 [(원문)](https://arxiv.org/abs/2604.17304)
- **2026-04-21**: Gate training 그래디언트 약화 문제를 auxiliary loss 조합으로 해결 (predictive + score supervision) [(원문)](https://arxiv.org/abs/2604.17228)
- **2026-04-21**: Linguistic markers로 추론 구조화하여 모델 내 early-exit 능력 내재화, 시스템 오버헤드 제거 [(원문)](https://arxiv.org/abs/2604.16890)


## 핵심 주체
[[Model Efficiency]]


## 모순/논쟁

