---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Sparse Attention

## 정의


## 주요 발전
- **2026-04-22**: BudgetFormer: 입력별 동적 헤드 예산 할당으로 불필요한 계산 비용 제거 [(원문)](https://arxiv.org/abs/2604.22583)
- **2026-04-27**: Hub 토큰 기반 routing으로 sub-quadratic 희소 어텐션 구현 - encode-decode-score-council 파이프라인 [(원문)](https://arxiv.org/abs/2604.22442)
- **2026-04-27**: 계층 민감도에 따라 softmax·linear sliding window·주의 제거를 선택적 적용 (LayerBoost) [(원문)](https://arxiv.org/abs/2604.22050)
- **2026-04-24**: 블록 단위 희소 어텐션이 슬라이딩 윈도우 내 동적 이웃 선택으로 메모리 업데이트 효율화 [(원문)](https://arxiv.org/abs/2604.21221)
- **2026-04-24**: Gist tokens를 routing signal로 활용한 selective unfolding 및 targeted fine-grained attention [(원문)](https://arxiv.org/abs/2604.20920)
- **2024-10-14**: RACE Attention: Repeated Arrays-of-Count Estimators. 각도 유사도 기반 선형 시간 어텐션 (2024) [(원문)](https://arxiv.org/abs/2510.04008)
- **2026-04-21**: TriangleMix는 decoding-time contribution sparsity 활용, prefilling의 quadratic attention 복잡도 감소, layer별 dense+triangle attention 혼합으로 가속화 [(원문)](https://arxiv.org/abs/2507.21526)
- **2026-04-18**: AdaCluster: 각도 유사성 보존 클러스터링으로 비디오 확산 트랜스포머 1.67-4.31배 가속화 [(원문)](https://arxiv.org/abs/2604.18348)
- **2026-04-21**: Sessa가 희소 어텐션을 피드백 경로에 배치해 장거리 의존성 처리 개선 (2026-04-21) [(원문)](https://arxiv.org/abs/2604.18580)
- **2026-04-21**: Layer-wise reduction의 신호 무관한 에러 증폭기 존재: Pareto curve convexity, critical compression ratio r_crit ∝ 1/L [(원문)](https://arxiv.org/abs/2604.16745)
- **2026-04-21**: 블록 희소 주의로 기상 예측의 장거리 의존성을 선형 비용에 캡처하며 스펙트럼 충실도 보존 [(원문)](https://arxiv.org/abs/2604.16429)
- **2025-04-20**: Softpick을 통한 주의 싱크(attention sink) 0% 달성, 희소한 주의 맵 생성 [(원문)](https://arxiv.org/abs/2504.20966)
- **2026-04-19**: AdaSplash-2: α-entmax 정규화(τ) 계산을 히스토그램 기반 초기화로 1-2회로 단축. 중간~고도 희소성에서 FlashAttention-2와 동등 per-step 학습 시간 [(원문)](https://arxiv.org/abs/2604.15180v1)


## 핵심 주체
[[Transformer Expressivity]] | [[Early-Exit Networks]] | [[KV Cache Compression]]


## 모순/논쟁

