---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Token Pruning

## 정의


## 주요 발전
- **2026-04-18**: Temporally stable token을 조기 finalize하여 불필요한 remasking decoding step 제거 [(원문)](https://arxiv.org/abs/2604.18995)
- **2026-04-21**: 기존 아키텍처 의존 프루닝 문제를 계층별 특화 전략으로 해결 [(원문)](https://arxiv.org/abs/2604.16462)
- **2026-04-21**: 토큰 안정성 감지로 휴리스틱 기반 가지치기의 하드웨어 커널 비호환 문제 해결 [(원문)](https://arxiv.org/abs/2604.18103)
- **2026-04-21**: CRISP 방법: attention anchor를 활용한 CoT 압축으로 계산 오버헤드 감소 [(원문)](https://arxiv.org/abs/2604.17297)
- **2026-04-21**: Unary signals이 pairwise signals보다 perturbation에 안정적 (O(N_p) vs O(N_p^2)); CLT로 설명 가능 [(원문)](https://arxiv.org/abs/2604.16745)
- **2025-04-20**: 낮은 커토시스(kurtosis) 은닉 상태로 프루닝 최적화 가능 [(원문)](https://arxiv.org/abs/2504.20966)
- **2026-04-20**: 한국어 특화 LLM에서 토큰 가지치기로 생성 안정성 향상 및 번역 성능 개선 [(원문)](https://arxiv.org/abs/2604.16235)
- **2026-04-20**: LRM에서 체계적인 경로 수준 가지치기 방법론 (STOP) 제시 [(원문)](https://arxiv.org/abs/2604.16029)
- **2026-04-20**: ViT 토큰 프루닝 후 dispatch 오버헤드(60-90μs)가 병목. Triton 커널로 40μs까지 감소, 2.24x 처리량 개선 (arXiv:2604.15408) [(원문)](https://arxiv.org/abs/2604.15408)
- **2026-04-19**: K-Token Merging: 임베딩 공간에서 K개 토큰 병합으로 75% 입력 길이 감소 [(원문)](https://arxiv.org/abs/2604.15153v1)


## 핵심 주체
[[Early-Exit Networks]] | [[Model Efficiency]] | [[Speculative Decoding]]


## 모순/논쟁

