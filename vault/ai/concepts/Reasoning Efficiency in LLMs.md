---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Reasoning Efficiency in LLMs

## 정의


## 주요 발전
- **2026-04-22**: 추론 토큰의 32% 이상이 post-decision 설명이므로 종료 조기화·적응형 깊이 조정으로 계산 비용 대폭 절감 가능 [(원문)](https://arxiv.org/abs/2604.22266)
- **2026-04-25**: 스킬 기반 추론은 장문의 CoT를 압축 저장하고 추론 시점에 검색해 중복 경로 회피 [(원문)](https://arxiv.org/abs/2604.21764v1)
- **2025-10-13**: Test-time scaling 신호 최적화 — PRM 신호와 LLM 신호의 복잡한 상호작용 분석 [(원문)](https://arxiv.org/abs/2510.13918)
- **2025-09-24**: ChessArena: 13개 모델 800+ 게임 평가, 인간 아마추어(Maia-1100) 수준 미달, 일부는 랜덤 미만 [(원문)](https://arxiv.org/abs/2509.24239)
- **2025-07-04**: 기본 수학 문제에서도 LLM의 과도한 생각(overthinking)으로 인한 토큰 낭비 및 정확도 역설 실증 [(원문)](https://arxiv.org/abs/2507.04023)
- **2026-04-24**: TRACES: 각 추론 단계를 실시간 태깅하여 비용-효율적 조기 종료 구현 [(원문)](https://arxiv.org/abs/2604.21057)
- **2026-04-21**: 텍스트-잠재 인터리빙으로 수학/논리/상식 추론에서 SOTA 달성 [(원문)](https://arxiv.org/abs/2511.08983)
- **2026-04-21**: VCORE가 CoT 감독을 제약 최적화 문제로 재정의하여 토큰별 감독 할당 최적화 [(원문)](https://arxiv.org/abs/2510.27462)
- **2026-04-21**: ThinkLogit 기법으로 작은 추론 가이더 모델에서 큰 비추론 모델로 추론 능력을 디코딩 시점에서 전이 [(원문)](https://arxiv.org/abs/2510.09354)
- **2025-10**: ThinkBrake: 로그 확률 마진 모니터링으로 문장 경계의 동적 추론 종료, 수학/QA 정확도 유지하며 토큰 30-50% 감소 (arXiv:2510.00546) [(원문)](https://arxiv.org/abs/2510.00546)
- **2026-04-21**: 다단계 추론 성능은 모델 깊이, recurrence/메모리를 통한 effective depth 확장이 핵심 [(원문)](https://arxiv.org/abs/2508.16745)
- **2026-04-21**: 음성 언어 모델에서 강화학습 기반 progressive reasoning으로 명시적 추론 프로세스 생성 [(원문)](https://arxiv.org/abs/2604.18187)
- **2026-04-21**: 자체 수정(19.8%)보다 LPSR(44%)이 +24.2pp 높음 (McNemar χ²=89.4, p≈0) [(원문)](https://arxiv.org/abs/2604.18567)
- **2026-04-21**: LLM 추론 궤적이 직선이 아닌 부드러운 곡선(smooth manifold) - 3-layer MLP로 추가 오차 38% 감소 [(원문)](https://arxiv.org/abs/2604.18464)
- **2026-04-17**: Poly-EPO: 집합 강화학습으로 탐색과 활용의 시너지를 명시적으로 학습, 테스트 타임 계산 확장으로 성능 및 일반화 개선 [(원문)](https://arxiv.org/abs/2604.17654)
- **2026-04-21**: TRACE: 단일 step 신뢰도 대신 다중 step 증거의 시간적 aggregation으로 수렴 감지 [(원문)](https://arxiv.org/abs/2604.17304)
- **2026-04-21**: intrinsic saliency 기반 조기 종료로 token 효율성 개선 [(원문)](https://arxiv.org/abs/2604.17297)
- **2026-04-21**: RankGuide로 추론 모델 협력의 성능-지연 트레이드오프 최적화 [(원문)](https://arxiv.org/abs/2604.16694)


## 핵심 주체
[[Early Decision Commitment in Transformers]] | [[Chain-of-Thought Controllability]]


## 모순/논쟁

