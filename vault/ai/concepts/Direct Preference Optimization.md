---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Direct Preference Optimization

## 정의


## 주요 발전
- **2026-04-27**: SFT(weak demonstrations) + RL 조합으로만 sandbagging 제거 가능, 단독 사용 불가 (2026-04-22) [(원문)](https://arxiv.org/abs/2604.22082)
- **2026-02-01**: Continuous Utility DPO (CU-DPO)는 binary preference 대신 continuous scores로 K strategies 학습 시 Θ(K log K) sample complexity 개선; entropy-regularized utility-maximizing policy 수렴성 입증 [(원문)](https://arxiv.org/abs/2602.00931)
- **2026-04-22**: Discrete Tilt Matching(DTM): masked diffusion LM의 sequence-level likelihood intractability를 state-level local unmasking posterior matching으로 해결 [(원문)](https://arxiv.org/abs/2604.18739)
- **2024-10-05**: 고품질 SFT 데이터셋 없이도 instruction tuning 성능 향상 가능한 Mixup 기반 방법론 [(원문)](https://arxiv.org/abs/2410.05248)
- **2026-04-21**: 규칙 기반 음악 제약을 자동 생성된 선호도 데이터로 변환해 DPO 적용 [(원문)](https://arxiv.org/abs/2604.18489)
- **2026-04-21**: 파이프라인 특화 데이터와 DPO를 결합하여 다단계 LLM 응용에서 보상 모델 예측과 실제 성과 간의 불일치 해소 [(원문)](https://arxiv.org/abs/2604.18327)
- **2026-04-21**: Margin-based objective가 거부된 응답과 함께 선택된 응답의 우도도 억제하는 likelihood displacement 현상 규명. Disentanglement band 조건으로 문제 회피 가능성 제시 [(원문)](https://arxiv.org/abs/2604.18239)
- **2026-04-21**: 수어 번역에서 spatial-temporal-linguistic 다층 DPO로 semantic drift 극복 가능 [(원문)](https://arxiv.org/abs/2604.18034)
- **2026-04-21**: 생성 모델 정렬 시 값-지도 추정기 설계와 타임스텝별 최적화 강도 간 트레이드오프 분석 [(원문)](https://arxiv.org/abs/2604.17415)
- **2026-04-21**: EqLen: 부등길이 응답 비교 문제를 비교 단위 구성으로 접근, equal-length paired training framework 제안 [(원문)](https://arxiv.org/abs/2604.17328)
- **2026-04-21**: Cat-DPO: 각 harm category마다 별도 adaptive safety margin으로 per-category 최적화 [(원문)](https://arxiv.org/abs/2604.17299)
- **2026-04-21**: PODPO는 부정 샘플 페널티 없이 positive samples만 활용하여 정책 업데이트. Drifting model의 local smoothness로 사전 오류 방지 [(원문)](https://arxiv.org/abs/2604.16519)
- **2025-09-19**: 상대 보상 회귀로 DPO 확장성 유지하면서 샘플 효율성 개선 [(원문)](https://arxiv.org/abs/2509.19104)
- **2025-04-20**: 진화하는 모델 역량에 맞춰 훈련 데이터 분포 반복적으로 재조정 [(원문)](https://arxiv.org/abs/2505.16176)
- **2026-04-20**: DPO의 다양성 감소 효과가 데이터 구성에 따라 차등 발생(광범위 다중소스 > CoT 단일 증류) [(원문)](https://arxiv.org/abs/2604.16027)
- **2026-04-20**: 그룹별 선호도 최적화(GroupDPO)로 메모리 오버헤드 제거하며 다중 응답 동시 학습 가능 [(원문)](https://arxiv.org/abs/2604.15602)


## 핵심 주체
[[LLM Safety Alignment]]


## 모순/논쟁

