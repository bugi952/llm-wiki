---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# LLM Output Consistency Control

## 정의


## 주요 발전
- **2026-04-27**: Background temperature: 배치 크기, 커널 비불변성, 부동소수점 비결합성으로 인한 T=0 설정에서의 발산 [(원문)](https://arxiv.org/abs/2604.22411)
- **2026-04-22**: 정적/맥락 인식/토큰 인식 부스팅 전략으로 생성 단계에 충실도 제어 (디코딩 시간 경량 방식) [(원문)](https://arxiv.org/abs/2604.22335)
- **2025-06-09**: VRS 기법 — 자연언어 추론으로 샘플 거부 제어, 확률 편향 감소 [(원문)](https://arxiv.org/abs/2506.09998)
- **2026-04-21**: FUSE: 라벨 없는 검증기 앙상블로 조건부 의존성 제어하여 검증 품질 향상 (arXiv:2604.18547) [(원문)](https://arxiv.org/abs/2604.18547)
- **2026-04-21**: 의미 보존 prompt 변형 시 LLM은 입력을 cluster하지 않고 disperse, log prob 차이 과도 (arXiv 2604.18389) [(원문)](https://arxiv.org/abs/2604.18389)
- **2026-04-21**: LLM protocol의 각 단계를 correction rate c=Pr(E₁=1|E₀=0)과 corruption rate γ=Pr(E₁=0|E₀=1)의 이분 측정으로 분석. 분포 변화와 파이프라인 조합 하에서 protocol 안정성 평가 가능 [(원문)](https://arxiv.org/abs/2604.18245)
- **2026-04-20**: SSAS (Syntactic & Semantic Context Assessment Summarization): 계층적 분류(Theme→Story→Cluster) + Summary-of-Summaries로 bounded attention 구현, 감정분석 일관성 강화 [(원문)](https://arxiv.org/abs/2604.15547)


## 핵심 주체
[[Hallucination Reduction]]


## 모순/논쟁

