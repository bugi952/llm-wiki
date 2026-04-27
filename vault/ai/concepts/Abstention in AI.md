---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Abstention in AI

## 정의


## 주요 발전
- **2026-04-27**: KAIST 연구팀이 무작위 가중치 초기화 단계에서 발생하는 과도한 확신을 '노이즈 예열 학습'으로 해결 [(원문)](https://www.aitimes.com/news/articleView.html?idxno=209803)
- **2026-04-24**: scalar confidence 대신 evidence distribution으로 abstention 행동 개선, epistemic uncertainty와 data ambiguity 구분 [(원문)](https://arxiv.org/abs/2604.20854)
- **2026-04-21**: Dynamic mid-generation abstention: 각 token에서 value function이 reward parameter 이하면 조기 종료. RL 프레임워크로 형식화 [(원문)](https://arxiv.org/abs/2604.18419)
- **2026-04-21**: DeepSeek-R1: full coverage 85.3% accuracy → 10% coverage 11.3% (74%p 저하). confidence-based abstention의 극단적 성능 저하 사례 [(원문)](https://arxiv.org/abs/2604.17716)
- **2026-04-21**: Validity screening protocol (L, Fp, RBS 지수)로 LLM confidence signal을 Valid/Indeterminate/Invalid 3단계로 분류. 20개 frontier LLM 중 4개는 Invalid, 2개는 Indeterminate [(원문)](https://arxiv.org/abs/2604.17714)
- **2026-04-21**: LLM의 단순 거부('I don't know')는 두 불확실성을 구분 못함. downstream task(clarification 요청, 외부 도구 호출)에 장애 [(원문)](https://arxiv.org/abs/2604.17293)
- **2026-04-21**: RLVR 보상으로 훈련된 3B 모델, 불가능한 쿼리에 대해 명확화 기반 거부로 신뢰성 개선 [(원문)](https://arxiv.org/abs/2604.17073)
- **2026-04-21**: MCQ 기반 작업에서 abstention 불가능하면 안전 실패 위험. 중간 강도 제약에서 정책 위반 최고조 [(원문)](https://arxiv.org/abs/2604.16916)


## 핵심 주체
[[KAIST]] | [[Uncertainty Quantification]] | [[Self-Aware Difficulty Metrics]]


## 모순/논쟁

