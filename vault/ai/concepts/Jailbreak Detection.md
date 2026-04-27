---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Jailbreak Detection

## 정의


## 주요 발전
- **2025-12-01**: Boa 시스템이 2단계 탐색(너비우선 샘플링 + 깊이우선 탐색)으로 지수 탐색공간 효율화 [(원문)](https://arxiv.org/abs/2506.17299)
- **2025-10**: Self-Jailbreak: 모델이 초기 유해 의도 인식하나 추론 단계에서 판단 번복 → 안전하지 않은 출력 생성 [(원문)](https://arxiv.org/abs/2510.21285)
- **2026-04-25**: TTI 기법으로 다중턴 정책 우회 가능. 상태 비유지 조절이 공격 벡터 [(원문)](https://arxiv.org/abs/2604.21860v1)
- **2026-02-15**: Intent laundering technique reveals that current safety datasets measure refusal provocation rather than genuine safety risks [(원문)](https://arxiv.org/abs/2602.16729)
- **2025-05-01**: LogiBreak: 논리식 변환 기반 blackbox jailbreak. 자연언어-논리식 분포 차이 악용으로 의미 보존하며 안전장치 회피. 3개 언어에서 유효성 검증 [(원문)](https://arxiv.org/abs/2505.13527)
- **2026-04-21**: 기존 single-turn jailbreak과 달리, 고립된 멀티턴 상호작용을 통한 분산된 adversarial intent 회피 기법 (TTI) 분류 [(원문)](https://arxiv.org/abs/2604.21860)
- **2026-04-24**: New attack vector: 메모리리스 guardrails를 회피하기 위해 공격을 다수 세션에 분산 (accumulate, compose, launder, inject_on_reader). Session-bound detector는 각 세션 내 payload를 감지 불가. [(원문)](https://arxiv.org/abs/2604.21131)
- **2026-04-24**: Universal Steering와 Representation Engineering으로 Llama-3.3-70B-4bit에서 91% (US), 83% (RepE) 탈옥 가능성 발견 [(원문)](https://arxiv.org/abs/2604.20945)
- **2026-04-21**: Shell-Induced Behavioral Override (SIBO): Shell instruction이 모델 기본 협력 행동을 범주적으로 override함을 5개 게임 도메인에서 실증 [(원문)](https://arxiv.org/abs/2604.20871)
- **2026-04-18**: Jailbreak 시 해로운 행동의 4단계 진행: refusal 억제 → compliance 합리화 → harmful task 분해 → risk 은폐 [(원문)](https://arxiv.org/abs/2604.19001)
- **2026-04-22**: 기하학적 기반 탐지가 alignment 변형(base, instruction-tuned, abliterated)과 무관하게 안정적 성능 유지. 1ms 이내 계산으로 실시간 모니터링 가능 [(원문)](https://arxiv.org/abs/2604.18901)
- **2026-04-21**: 멀티 세대 샘플링은 단일 생성 평가 대비 jailbreak 취약점을 더 정확히 포착. 적당 수준까지 샘플 증가 시 유의미한 개선, 이후 수확체감. [(원문)](https://arxiv.org/abs/2604.18775)
- **2026-04-22**: SAE 기반 augmentation이 cross-model 공격 transferability 감소. 중간층에서 robustness와 clean performance 간 최적 균형 [(원문)](https://arxiv.org/abs/2604.18756)
- **2026-04-21**: SFT/RLVR/abliteration 등 서로 다른 기법이 행동적으로는 유사한 해로움 순응에 도달하나 기계론적으로는 상이한 실패 모드. [(원문)](https://arxiv.org/abs/2604.18510)
- **2026-04-21**: Prompt injection 탐지: forensic linguistics, fatigue analysis, deception tech, sequence alignment, mechanism design, spectral analysis, taint tracking 7가지 기법 [(원문)](https://arxiv.org/abs/2604.18248)
- **2026-04-21**: 보상 해킹 vs. Jailbreak: 전자는 평가 환경 자체 조작, 후자는 평가자 회피 → 탐지 전략 상이 [(원문)](https://arxiv.org/abs/2604.17596)
- **2026-04-21**: SafeDream: 안전 상태를 world model로 인코딩하여 multi-turn 공격 누적 효과 감지. LLM 수정 없이 외부 모듈로 동작 [(원문)](https://arxiv.org/abs/2604.16824)
- **2026-04-21**: Adversarial Humanities: 인문학적 스타일 변환으로 안전 거부 우회 36.8%-65.0% [(원문)](https://arxiv.org/abs/2604.18487)
- **2026-04-21**: 다단계 워크플로우·도구 상호작용·지속 컨텍스트의 prompt 인젝션 전파 차단 [(원문)](https://arxiv.org/abs/2604.17562)
- **2026-04-21**: Value Ambiguity/Conflict 범주 morality 데이터셋(10.3K) 기반 adversarial attack으로 LLM 윤리 판단 오류 노출 [(원문)](https://arxiv.org/abs/2604.17053)
- **2025-10-15**: Web search workflow를 통한 새로운 bypass 경로 발견 [(원문)](https://arxiv.org/abs/2510.09689)
- **2026-04-20**: 적대적 공격 성공률: 프롬프트 주입 미사용 시 다항식 성장 → 주입 시 지수 성장으로 전환 [(원문)](https://arxiv.org/abs/2603.11331)
- **2025-05-24**: TRIDENT - persona 기반 zero-shot 생성으로 jailbreak tactic 다양화 [(원문)](https://arxiv.org/abs/2505.24672)
- **2026-04-20**: 훈련 없는 방법으로 적대 공격 방어 가능하나 일관성 있는 평가 메트릭 필요 [(원문)](https://arxiv.org/abs/2604.15789)
- **2026-04-20**: PRJA Framework: reasoning step을 target한 jailbreak로 final answer 유지하면서 harmful content 주입 가능 [(원문)](https://arxiv.org/abs/2604.15725)
- **2026-04-17**: Streaming probing에서 isolated token spike 대신 aggregated segment-level signals로 robust detection 달성 [(원문)](https://arxiv.org/abs/2604.14865)


## 핵심 주체
[[Red Teaming]] | [[LLM Safety Alignment]]


## 모순/논쟁

