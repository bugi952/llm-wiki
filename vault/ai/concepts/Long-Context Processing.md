---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Long-Context Processing

## 정의


## 주요 발전
- **2025-10**: 문장·EDU 경계 외의 새로운 주기 발견: 정보 인코딩의 주기성이 전통적 텍스트 구조 단위와 무관 [(원문)](https://arxiv.org/abs/2510.27241)
- **2025-02-15**: Recurrent state 크기가 장맥락 정보 회상 능력과 양의 상관관계, direct training 비용 회피 가능 [(원문)](https://arxiv.org/abs/2509.22630)
- **2026-04-27**: Event-driven sparse computation과 INT8-Spiking/FP8 dual quantization으로 context scaling 효율화 [(원문)](https://arxiv.org/abs/2604.22575)
- **2026-04-27**: Lightweight evidence highlighting으로 context noise에서 핵심 정보 강조 [(원문)](https://arxiv.org/abs/2604.22565)
- **2026-04-22**: SLIDERS 프레임워크로 문서를 관계형 DB로 추출하고 SQL 추론으로 컨텍스트 윈도우 한계 극복 [(원문)](https://arxiv.org/abs/2604.22294)
- **2026-04-27**: Linear window attention이 sequence length의 quadratic 복잡도를 선형화 [(원문)](https://arxiv.org/abs/2604.22050)
- **2026-04-24**: Elastic Pipeline Parallelism (EPP): 토큰 레벨/배치 레벨 PP를 워크로드에 적응시켜 장문맥 학습 중 메모리와 계산 효율성 동시 개선 [(원문)](https://arxiv.org/abs/2509.21275)
- **2025-09**: 최대 효율적 컨텍스트 윈도우(MECW)가 보고된 최대값(MCW)과 크게 차이나며, 문제 유형별로 변동 (수십 토큰~수천 토큰 범위) [(원문)](https://arxiv.org/abs/2509.21361)
- **2026-04-21**: Root Theorem: finite context + 정보 품질 저하는 axiom. signal-to-token ratio 최대화가 유일 원칙. homeostatic persistence (accumulate-compress-rewrite-shed) 필수 [(원문)](https://arxiv.org/abs/2604.20874)
- **2026-04-24**: 그래프 구조 메모리(Engrama)가 벡터 검색(Mem0)보다 cross-space 추론에서 0.625 vs 0.481로 우수 [(원문)](https://arxiv.org/abs/2604.21229)
- **2026-04-24**: 자동회귀 디코딩 비용 유지하며 unbounded temporal depth 달성, RNN 최적화 불안정성 제거 [(원문)](https://arxiv.org/abs/2604.21215)
- **2026-04-24**: Gist Sparse Attention: learnable gist tokens로 context 압축 후 coarse-to-fine sparse attention [(원문)](https://arxiv.org/abs/2604.20920)
- **2026-04-24**: Absorber LLM: causal synchronization으로 constant-memory에서 long-tail dependencies 보존 [(원문)](https://arxiv.org/abs/2604.20915)
- **2026-04-22**: FG²-GDN: channel-wise learning rate로 delta rule 적응화, context window 확장 [(원문)](https://arxiv.org/abs/2604.19021)
- **2025-12-07**: CoT 추론에서 KV cache 선택적 스킵으로 메모리-처리량 trade-off 개선 [(원문)](https://arxiv.org/abs/2512.07993)
- **2025-11-08**: FlexiCache 방식으로 긴 생성 시에도 GPU 메모리/연산 오버헤드 감소 가능 [(원문)](https://arxiv.org/abs/2511.00868)
- **2024-10-14**: RACE Attention으로 4백만 토큰 이상 장문맥 학습 가능 (FlashAttention-2/3 불가능 범위) (2024) [(원문)](https://arxiv.org/abs/2510.04008)
- **2026-04-21**: TriangleMix (training-free static attention pattern)로 입력 길이 증가에 따른 prefilling 병목 해결, 거의 무손실 성능 유지 [(원문)](https://arxiv.org/abs/2507.21526)
- **2026-04-21**: KV cache 성장 제어 + 하드웨어 인식 수치 안정화로 long-sequence 추론 메모리 병목 해결 [(원문)](https://arxiv.org/abs/2507.09025)
- **2026-04-21**: ExtAgents: 다중 에이전트 협력으로 LLM context 한계를 근본적으로 극복, 추론 시점 지식 통합 확장 (∞Bench+ 벤치마크) [(원문)](https://arxiv.org/abs/2505.21471)
- **2025-05-13**: LLM의 코드 의미론적 회상은 컨텍스트 중앙 위치에서 심각하게 저하되며, 패턴 매칭 지름길에 의존함 (arXiv:2505.13353) [(원문)](https://arxiv.org/abs/2505.13353)
- **2026-04-21**: 비디오 생성에서 서사적 풍요성과 글로벌 인과관계 등 장문 특성 평가의 필수성 (Long-CODE) [(원문)](https://arxiv.org/abs/2604.17428)
- **2026-04-21**: DASH가 self-attention의 layer-wise update 동역학을 모니터링하여 의미 고정점 도달 토큰을 선택적 중단, prefill 속도 향상 동시에 정확도 및 FlashAttention 호환성 유지 [(원문)](https://arxiv.org/abs/2604.18103)
- **2026-04-21**: KV 캐시 증가가 long-context 처리의 주요 병목 → NGC는 모델이 추론 과정에서 동적으로 캐시 정리 학습 [(원문)](https://arxiv.org/abs/2604.18002)
- **2026-04-21**: KV 캐시 압축의 공격적 적용은 다단계 추론 능력 저하를 야기하며, 캐시-깊이 트레이드오프를 고려한 설계 필요 (2026-04-21) [(원문)](https://arxiv.org/abs/2604.17935)
- **2026-04-21**: 계층별 이질적 KV 캐시 압축으로 메모리 병목 완화. LongBench 장문맥 작업에서 효율성 검증 [(원문)](https://arxiv.org/abs/2604.17695)
- **2026-04-21**: 역방향 KL divergence 기반 per-token 감독으로 long-context 생성 안정화 [(원문)](https://arxiv.org/abs/2604.17535)
- **2026-04-21**: 대규모 IoT/운영 데이터의 직렬화 효율화로 long-context 처리 비용 절감 [(원문)](https://arxiv.org/abs/2604.17512)
- **2026-04-21**: ATANT 벤치마크(250-스토리 코퍼스): 연속성 평가 프레임워크로 기존 메모리/긴컨텍스트/에이전트 메모리 벤치마크와 비교 [(원문)](https://arxiv.org/abs/2604.17273)
- **2026-04-21**: 장기 에이전트 성능은 context length가 아닌 context budget 내의 의사결정 관련 정보 유지량으로 결정됨 (arXiv:2604.17091) [(원문)](https://arxiv.org/abs/2604.17091)
- **2026-04-21**: Apple Silicon (64GB Mac)에서 Llama 3.1 70B의 128K 컨텍스트 추론 실현 [(원문)](https://arxiv.org/abs/2604.16957)
- **2026-04-21**: Training-free sink detection으로 KV-cache 메모리 부하 감소, 정확도-효율성 트레이드오프 개선 [(원문)](https://arxiv.org/abs/2604.16883)
- **2026-04-21**: Deferred template rendering이 모든 포맷(overhead multiplier μf > 1)에 대해 direct generation보다 token-efficient [(원문)](https://arxiv.org/abs/2604.16736)
- **2026-04-21**: STORM: 선형 복잡도 global attention으로 20B spatiotemporal token 처리 가능 [(원문)](https://arxiv.org/abs/2604.16590)
- **2026-04-21**: 시간 순서 텍스트에서 희귀 변화 이벤트 감지를 위한 temporal conditioning 프레임워크 [(원문)](https://arxiv.org/abs/2604.16382)
- **2026-04-20**: CoMeT의 FIFO 임시메모리(최근)+gated global 메모리(장거리)로 constant memory O(1)+linear time O(n) 달성 [(원문)](https://arxiv.org/abs/2602.01766)
- **2026-04-20**: 외부 파일시스템 workspace로 token budget 압축 문제 우회, iterative refinement 가능 [(원문)](https://arxiv.org/abs/2602.01566)
- **2025-09-01**: 온라인 서브스페이스 적응을 통한 저랭크 KV 캐시 압축(OjaKV): 첫/최근 토큰 보존 + 하이브리드 저장 정책으로 메모리 병목 해결 [(원문)](https://arxiv.org/abs/2509.21623)
- **2026-04-20**: KV-cache: FP16에서 시스템적 수치 오류 발생. FP32에서만 안정적 [(원문)](https://arxiv.org/abs/2604.15409)
- **2026-04-20**: Probabilistic prefix deduplication으로 context 길이 확장 시 KV cache 압축 효율 증가 [(원문)](https://arxiv.org/abs/2604.15356)


## 핵심 주체
[[Information Theory]]


## 모순/논쟁

