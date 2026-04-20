---
type: concept
domain: ai
last_updated: 2026-04-20
source_count: 0
---

# Long-Context Processing

## 정의


## 주요 발전
- **2026-04-20**: CoMeT의 FIFO 임시메모리(최근)+gated global 메모리(장거리)로 constant memory O(1)+linear time O(n) 달성 [(원문)](https://arxiv.org/abs/2602.01766)
- **2026-04-20**: 외부 파일시스템 workspace로 token budget 압축 문제 우회, iterative refinement 가능 [(원문)](https://arxiv.org/abs/2602.01566)
- **2025-09-01**: 온라인 서브스페이스 적응을 통한 저랭크 KV 캐시 압축(OjaKV): 첫/최근 토큰 보존 + 하이브리드 저장 정책으로 메모리 병목 해결 [(원문)](https://arxiv.org/abs/2509.21623)
- **2026-04-20**: KV-cache: FP16에서 시스템적 수치 오류 발생. FP32에서만 안정적 [(원문)](https://arxiv.org/abs/2604.15409)
- **2026-04-20**: Probabilistic prefix deduplication으로 context 길이 확장 시 KV cache 압축 효율 증가 [(원문)](https://arxiv.org/abs/2604.15356)


## 핵심 주체
[[Model Efficiency]] | [[State Space Models]] | [[Sparse Attention]]


## 모순/논쟁

