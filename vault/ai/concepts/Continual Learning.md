---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Continual Learning

## 정의


## 주요 발전
- **2026-03-24**: 연속 학습 로봇이 고정된 내부 서브네트워크(자아)를 발달 (p<0.001), 적응 촉진 및 손상 시 방지 효과 확인 [(원문)](https://arxiv.org/abs/2603.24350)
- **2024-11-04**: DP-CL 공식화: 시간-변화 레이블 공간에서 출력 부채널을 통한 프라이버시 누출 분석 및 완화 방법 [(원문)](https://arxiv.org/abs/2411.04680)
- **2026-04-27**: Task-specific 모델을 재학습 없이 통합하는 적응형 continual merging - expert 다양성과 효율성 조화 [(원문)](https://arxiv.org/abs/2604.22464)
- **2026-04-27**: Adam + gradient modification 조합에서 shared routing 실패 발견. Adaptive decoupled moment routing으로 고중복 도메인에서 3.8-4.8 units 개선 [(원문)](https://arxiv.org/abs/2604.22407)
- **2026-04-25**: Fine-tuning regime (trainable depth)의 선택이 catastrophic forgetting과 현재 작업 학습의 tradeoff를 결정; 방법 비교는 regime을 고정해야 의미있음 [(원문)](https://arxiv.org/abs/2604.21927v1)
- **2026-04-25**: 시간 기반 작업 분할 방식이 평가 결과에 유의미한 영향 [(원문)](https://arxiv.org/abs/2604.21930v1)
- **2025-04-24**: RETROFIT: 저차원+희소 부분공간 제약과 신뢰도 기반 망각 제어로 데이터 재생 없이 연속학습 개선 [(원문)](https://arxiv.org/abs/2511.11439)
- **2024-10-16**: 영어 능력 기반 LLM이 다국어 데이터로 CFT 시 유사한 작업에서만 성능 유지 [(원문)](https://arxiv.org/abs/2410.16006)
- **2026-04-24**: Trainable depth regime이 CL 방법 비교 결과를 변경: 5개 벤치마크(MNIST, CIFAR-100 등)에서 실증 [(원문)](https://arxiv.org/abs/2604.21927)
- **2026-04-20**: LLM의 메모리 누적으로 인한 context window 폭발 문제를 offline consolidation과 선택적 망각으로 해결 [(원문)](https://arxiv.org/abs/2604.20943)
- **2026-04-22**: Proximal decoupling: learning step과 stability step을 분리하여 forward transfer 개선 및 capacity 효율화 [(원문)](https://arxiv.org/abs/2604.18857)
- **2026-04-18**: Divide-and-conquer 의사 라벨링(일관성 기반 선택 + 반영)으로 비라벨 데이터 효율적 처리 [(원문)](https://arxiv.org/abs/2604.18639)
- **2025-11-27**: In Situ Training: 스케칭 데이터 정규화로 장시간 시뮬레이션 중 재앙적 망각 방지. Johnson-Lindenstrauss 기반 이론적 근거 [(원문)](https://arxiv.org/abs/2511.02659)
- **2026-04-21**: ISI-CV: 신경형 칩 네이티브 gradient-free 연속학습 메트릭 [(원문)](https://arxiv.org/abs/2604.16496)
- **2026-04-21**: 다중 도메인 순차 학습에서 안전성 누적 침식. 임계값 기반 수정 재생으로 대응 [(원문)](https://arxiv.org/abs/2604.17691)
- **2026-04-17**: 1.7B 다국어 모델에서 기초 언어 능력과 번역 능력이 병렬로 개발되는 패턴 확인 [(원문)](https://arxiv.org/abs/2604.17633)
- **2026-04-21**: 비선형 회귀 과제에서 과제 의존성(현재 데이터 = 이전 데이터의 비선형 변환)을 가정하면 experience replay + 정규화의 복구 보장(recovery guarantee) 증명 가능 [(원문)](https://arxiv.org/abs/2604.17578)
- **2026-04-21**: 지속적 도메인 적응 중 고-기울기 샘플 필터링으로 정렬 보존 가능 (곡선 안전 데이터나 아키텍처 수정 불필요) [(원문)](https://arxiv.org/abs/2604.17215)
- **2026-04-21**: Decision tree 기반 개념 인터페이스로 설명 가능성 유지하면서 continual update 수행. Stability-plasticity tradeoff를 표형 의료 데이터 벤치마크에서 개선 (arXiv:2604.17089) [(원문)](https://arxiv.org/abs/2604.17089)
- **2026-04-20**: SLE-FNO: FNO 기반 단일층 확장으로 분포 시프트 적응 시 재앙적 망각 방지 [(원문)](https://arxiv.org/abs/2603.20410)
- **2026-04-20**: 증분 학습 기반 얼굴 위변조 탐지: 새로운 위변조 유형 출현 시에도 기존 성능 유지 [(원문)](https://arxiv.org/abs/2604.16207)
- **2026-04-20**: JumpLoRA: JumpReLU 게이팅을 통해 LoRA에 동적 희소성을 유도하여 작업 간섭 방지 (arXiv:2604.16171) [(원문)](https://arxiv.org/abs/2604.16171)
- **2026-04-20**: 지속학습의 정규화 기법을 적용하여 fine-tuning 유도 hallucination 완화 [(원문)](https://arxiv.org/abs/2604.15574)
- **2026-04-20**: TeLAPA: 행동적 다양성 아카이브로 작업별 정책 저장. 비정상 드리프트 하에서 안정적 재사용 [(원문)](https://arxiv.org/abs/2604.15414)
- **2026-04-17**: Vision-Language Model의 asymmetric architecture로 인한 catastrophic forgetting. Asymmetric Information Masking으로 해결 [(원문)](https://arxiv.org/abs/2604.14779)
- **2026-04-17**: Multi-site fMRI 신경 질환 진단에서 generative replay 기반 VAE로 catastrophic forgetting 완화 [(원문)](https://arxiv.org/abs/2604.14259)
- **2026-04-17**: CI-CBM(Class-Incremental CBM): 개념 병목 모델로 클래스 증분 학습 중 해석 가능성 유지, 이전 방법 대비 36% 정확도 향상 [(원문)](https://arxiv.org/abs/2604.14519)
- **2026-04-17**: Incremental concept formation으로 catastrophic forgetting 극복한 hierarchical topic modeling [(원문)](https://arxiv.org/abs/2604.14489)
- **2026-04-17**: Mistake-gated learning으로 학습 업데이트 50-80% 감소 (생물학적 negativity bias 영감) [(원문)](https://arxiv.org/abs/2604.14336)


## 핵심 주체
[[Metacognition in AI]] | [[Agent Memory]] | [[Self-Evolving Agent Systems]]


## 모순/논쟁

