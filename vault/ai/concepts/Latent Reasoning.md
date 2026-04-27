---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Latent Reasoning

## 정의


## 주요 발전
- **2026-04-27**: Abstract CoT: reserved token vocabulary로 자연언어 CoT 대체, 추론 길이 단축 + 성능 유지 [(원문)](https://arxiv.org/abs/2604.22709)
- **2025-12**: ThinkARM: 추론 트레이스를 Analysis, Explore, Implement, Verify 등 함수적 단계로 추상화, 탐색 단계가 정확성의 핵심 분기점 [(원문)](https://arxiv.org/abs/2512.19995)
- **2026-04-24**: 다국어 제약 없을 때 모델 추론 공간 확장 (Polyglot Thinking Experiment) [(원문)](https://arxiv.org/abs/2604.21593)
- **2026-04-21**: Progressive alignment objective로 반복 갱신 중 잠재 표현 안정화 (SpiralThinker) [(원문)](https://arxiv.org/abs/2511.08983)
- **2025-10-07**: Monte Carlo Dropout/Additive Gaussian Noise로 연속 벡터 샘플링 후 Latent Reward Model (contrastive objective)로 trajectory aggregation [(원문)](https://arxiv.org/abs/2510.07745)
- **2025-10**: Overthinking 현상: LRM이 정답 중간해 도달 후 계속 추론해 오답으로 덮어씀. 오라클 조기 중단으로 8% 정확도 개선+72% 사고 토큰 감소 가능 [(원문)](https://arxiv.org/abs/2510.00546)
- **2026-04-21**: 추론 단계 수 증가 시 성능 급락, test-time compute와 아키텍처 깊이로 극복 가능하나 근본 한계 존재 [(원문)](https://arxiv.org/abs/2508.16745)
- **2026-04-21**: 자율주행 제어에서 명시적 CoT 대신 latent 공간 추론으로 실시간성 확보 [(원문)](https://arxiv.org/abs/2604.18486)
- **2026-04-21**: Phase-Shift Rollback (LPSR): MATH-500에서 8B 모델 44% (표준 28.8% 대비 +15.2pp, p<1e-15) [(원문)](https://arxiv.org/abs/2604.18567)
- **2026-04-21**: 의미론적 스텝 경계 샘플링(STP)으로 ProcessBench 다단계 예측 정확도 168배 향상 vs random-token STP(4배) [(원문)](https://arxiv.org/abs/2604.18464)
- **2026-04-20**: LEPO: Gumbel-Softmax로 잠재 공간에 제어 가능한 확률성 주입. 롤아웃 단계에서는 확률성 유지 → 다양한 궤적 샘플링. 최적화 단계에서는 통합 그래디언트 추정으로 RL 호환성 강화 [(원문)](https://arxiv.org/abs/2604.17892)
- **2026-04-16**: SPS (Steering Probability Squeezing): RL + IRL 교대 학습으로 Pass@k 성능 향상, trajectory distribution 명시적 reshape [(원문)](https://arxiv.org/abs/2604.16995)
- **2026-04-21**: Thought tree의 구조(내용 아님)가 코딩 작업 정확도의 강력한 예측 신호. Frontier reasoning models의 실세계 코딩 벤치마크 성능 분석 [(원문)](https://arxiv.org/abs/2604.16931)


## 핵심 주체
[[Chain-of-Thought Controllability]] | [[System-2 Learning]] | [[In-Context Learning]]


## 모순/논쟁

