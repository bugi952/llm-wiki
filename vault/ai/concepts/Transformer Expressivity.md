---
type: concept
domain: ai
last_updated: 2026-04-20
source_count: 0
---

# Transformer Expressivity

## 정의


## 주요 발전
- **2026-04-20**: Softmax Attention이 기본 상태(default state)를 구현하려면 content-agnostic position으로의 확률 질량 집중 필수 [(원문)](https://arxiv.org/abs/2603.11487)
- **2026-04-20**: Spiking self-attention의 스파이크 수 하한선: Ω(L_f² nd/ε²) (정보이론 기반, 유효 차원 d_eff=47-89) [(원문)](https://arxiv.org/abs/2604.15769)
- **2026-04-17**: Self-attention을 tropical rational map으로 모델링하면 Power Voronoi Diagram으로 수렴. Multi-head aggregation이 O(N) → O(N^H) 복잡도 확장, 깊이와 함께 Θ(N^{d_model}L) 선형 영역 생성 [(원문)](https://arxiv.org/abs/2604.14727)


## 핵심 주체
[[Mechanistic Interpretability]] | [[Sparse Attention]]


## 모순/논쟁

