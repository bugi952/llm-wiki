---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Looped Transformers

## 정의


## 주요 발전
- **2026-04-24**: Hyperloop: Begin-Middle-End 3단계 블록 구조로 중간 블록만 반복 적용, 파라미터 공유율 증대 [(원문)](https://arxiv.org/abs/2604.21254)
- **2026-04-24**: Recurrent Transformer: 각 레이어가 자신의 활성화로부터 KV 쌍 계산, 레이어 수 제약 없이 시간 깊이 증가 [(원문)](https://arxiv.org/abs/2604.21215)
- **2026-04-24**: 반복 횟수 r에 대한 반복-동치 지수 φ=0.46 발견 (R²=0.997). r=4일 때 410M 루프 모델 성능이 580M 비루프 모델과 동등. 루프가 단순 용량 증가가 아닌 중간 효율성 제공 [(원문)](https://arxiv.org/abs/2604.21106)
- **2026-04-24**: 반복 연산자의 최적 설계에서 손실 함수의 곡률 정보 활용 중요성 제시. 기존 일차 근사 대신 고차 최적화 가능 [(원문)](https://arxiv.org/abs/2604.21100)
- **2026-04-22**: Denoising Recursion은 루프 트랜스포머에 diffusion 패러다임 적용하여 긴 정제 궤적 학습 가능 [(원문)](https://arxiv.org/abs/2604.18839)
- **2025-10-07**: 재귀 트랜스포머의 성능 병목: undifferentiated computation(매 반복 유사 패턴)과 information overload(혼재된 정보) [(원문)](https://arxiv.org/abs/2510.07739)
- **2026-04-21**: 피드포워드 아키텍처는 진화하는 상태의 반복적 업데이트를 유지할 수 없음 (arXiv:2604.17121) [(원문)](https://arxiv.org/abs/2604.17121)
- **2026-04-14**: Parcae 아키텍처: UC 샌디에고 & Together AI, 루프 구조로 2배 크기 모델 성능을 절반 매개변수로 달성 [(원문)](https://www.aitimes.com/news/articleView.html?idxno=209435)
- **2026-04-19**: 고정점 안정성 프레임워크: recall + outer normalization이 도달 가능성, 국소 매끄러움, 역전파 안정성 동시 달성 [(원문)](https://arxiv.org/abs/2604.15259v1)


## 핵심 주체
[[Model Efficiency]] | [[On-Device LLM Inference]]


## 모순/논쟁

