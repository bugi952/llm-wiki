---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Speculative Decoding

## 정의


## 주요 발전
- **2026-02-06**: 보조 추론기 모델 없이 자기증류로 단일 모델을 다중토큰 예측으로 변환하는 경량 대안 (arXiv:2602.06019) [(원문)](https://arxiv.org/abs/2602.06019)
- **2025-12-01**: 시각 자동회귀 생성에서 검증 스킵을 통한 speculative decoding 가속화 VVS (arXiv:2511.13587) [(원문)](https://arxiv.org/abs/2511.13587)
- **2025-10-15**: 온라인 드래프트 모델 선택의 무후회 알고리즘으로 각 질의마다 최적 모델 동적 선택, 토큰 수락률 최대화 [(원문)](https://arxiv.org/abs/2510.20064)
- **2026-04-18**: 병렬 token prediction 최적화 관점에서 diffusion LLM의 redundancy-aware decoding과 유사한 원리 [(원문)](https://arxiv.org/abs/2604.18995)
- **2025-10-06**: Trace Credit 기법으로 예측 신뢰도 낮지만 정답인 토큰의 신뢰도를 높여 병렬 디코딩 가속화 가능 [(원문)](https://arxiv.org/abs/2510.06133)
- **2025-09**: Speculative Verification: companion model 기반 draft-target 정렬도 측정, 정보 게인 최대화로 검증 길이 동적 조정 (arXiv:2509.24328) [(원문)](https://arxiv.org/abs/2509.24328)
- **2026-04-21**: WISV는 채널 상태 정보를 의사결정에 통합하여 무선 환경에서 추측 복호화 성능 향상 [(원문)](https://arxiv.org/abs/2604.17701)
- **2026-04-21**: 비디오 블록 생성에 도입되며, 이미지 품질 라우터를 통한 검증 메커니즘 적용 (SDVG, 최악 프레임 집계) [(원문)](https://arxiv.org/abs/2604.17397)
- **2026-04-21**: B-PASTE: 빔 기반 추측 실행으로 리소스 제약 환경에서 LLM 에이전트 레이턴시 최소화 (2026-04) [(원문)](https://arxiv.org/abs/2604.16469)
- **2026-04-21**: 토큰 순서 최적화(NI Sampling)로 샘플링 반복 횟수를 한 자릿수 감소 가능 [(원문)](https://arxiv.org/abs/2604.18471)
- **2026-04-21**: Copy-as-Decode 방식으로 병렬 프리필 활용 시 토큰 복사를 6.8~303배 가속화 [(원문)](https://arxiv.org/abs/2604.18170)
- **2026-04-21**: SMC/Metropolis-Hastings로 시퀀스 레벨 품질 최적화, 훈련 불필요(weights frozen) + prefix lookahead 변형으로 주변화 정확성 보장 [(원문)](https://arxiv.org/abs/2604.16453)
- **2026-04-21**: Cross-tokenizer 스펙데코딩 기법으로 문맥 인식 토큰 번역 시 수용률 향상 (Apple Silicon) [(원문)](https://arxiv.org/abs/2604.16368)
- **2026-04-20**: ConFu: Contemplate 토큰과 소프트 프롬프트로 드래프트 모델의 생성 방향 예측, 에러 누적 77% 감소 [(원문)](https://arxiv.org/abs/2603.08899)
- **2026-04-20**: SMC-SD: token-level rejection 대신 draft particle의 importance-weighted resampling; memory bandwidth 유휴 계산으로 벡터화 가속화 [(원문)](https://arxiv.org/abs/2604.15672)
- **2026-04-19**: SpecGuard: 단계별 검증을 위해 주의력 기반 귀속점수 + 로그확률 신뢰도 앙상블로 오류 전파 방지 [(원문)](https://arxiv.org/abs/2604.15244v1)


## 핵심 주체
[[Model Efficiency]] | [[Knowledge Distillation]]


## 모순/논쟁

