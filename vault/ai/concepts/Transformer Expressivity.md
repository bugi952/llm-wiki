---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Transformer Expressivity

## 정의


## 주요 발전
- **2025-02-01**: 쿼리 프로젝션을 비선형 residual Q(X)=X+f_θ(X) (bottleneck MLP)로 대체하면 val loss 2.4%, perplexity 6.81% 개선 [(원문)](https://arxiv.org/abs/2603.13381)
- **2026-04-24**: 신경망의 학습 역학, 숨겨진 표현, 최종 가중치의 통계적 특성을 설명하는 통합 이론 기초 [(원문)](https://arxiv.org/abs/2604.21691)
- **2026-04-21**: 각 입력 단계마다 상태 표현이 깊은 층으로 이동하며 얕은 층에서 정보 접근 불가능 (arXiv:2604.17121) [(원문)](https://arxiv.org/abs/2604.17121)
- **2026-04-20**: Softmax Attention이 기본 상태(default state)를 구현하려면 content-agnostic position으로의 확률 질량 집중 필수 [(원문)](https://arxiv.org/abs/2603.11487)
- **2026-04-20**: Spiking self-attention의 스파이크 수 하한선: Ω(L_f² nd/ε²) (정보이론 기반, 유효 차원 d_eff=47-89) [(원문)](https://arxiv.org/abs/2604.15769)
- **2026-04-17**: Self-attention을 tropical rational map으로 모델링하면 Power Voronoi Diagram으로 수렴. Multi-head aggregation이 O(N) → O(N^H) 복잡도 확장, 깊이와 함께 Θ(N^{d_model}L) 선형 영역 생성 [(원문)](https://arxiv.org/abs/2604.14727)


## 핵심 주체
[[Attention Sinks]]


## 모순/논쟁

