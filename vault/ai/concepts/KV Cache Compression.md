---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# KV Cache Compression

## 정의


## 주요 발전
- **2025-09-20**: GPU 캐시 예측기 기반 동적 정책, 엄격한 시간·공간 제약 만족하며 배포 오버헤드 최소화 [(원문)](https://arxiv.org/abs/2509.20979)
- **2026-04-24**: QuantumAI가 극좌표 무작위 회전 한계를 극복한 QuantumQuant 기술 공개 [(원문)](https://www.aitimes.com/news/articleView.html?idxno=209728)
- **2026-04-24**: 서브토큰 레벨 라우팅으로 토큰 내 불균형한 값 그룹 분포를 차등적으로 활용 가능 [(원문)](https://arxiv.org/abs/2604.21335)
- **2025-12-07**: SkipKV: 다중 배치 환경에서 token-wise scoring 불안정성 제거, semantic-aware selective eviction [(원문)](https://arxiv.org/abs/2512.07993)
- **2025-11-08**: FlexiCache: 안정적 vs 불안정 어텐션 헤드를 구분하여 계층적 캐시 관리. 생성 길이에서도 정확도 손상 최소화 [(원문)](https://arxiv.org/abs/2511.00868)
- **2024-10-14**: Flash Attention의 저정밀도 학습 실패: 저차원 표현 + 반올림 오차의 악순환 규명 (2024) [(원문)](https://arxiv.org/abs/2510.04212)
- **2026-04-21**: 순차 입력 압축으로 추론 전 과정의 메모리 성장 제어 메커니즘 [(원문)](https://arxiv.org/abs/2604.16734)
- **2026-04-21**: Neural Garbage Collection (NGC): 언어모델이 chain-of-thought 추론 중 어떤 KV 캐시 항목을 버릴지 학습. Task reward 기반 end-to-end RL로 훈련. [(원문)](https://arxiv.org/abs/2604.18002)
- **2026-04-21**: K-hop 포인터 추적 문제에서 KV 캐시 크기 s, 토큰 n에 대해 필요 깊이는 Ω(⌈k/s⌉ · ⌈log₂ n/(Hmp)⌉) 형태의 하한을 가짐 (2026-04-21) [(원문)](https://arxiv.org/abs/2604.17935)
- **2026-04-21**: MoE-nD: 토큰 제거·양자화·저랭크 투영·계층 공유를 조합. 각 계층이 최적 (제거율, K비트, V비트) 튜플을 선택. 오프라인 보정 탐욕 솔버로 최적화 [(원문)](https://arxiv.org/abs/2604.17695)
- **2026-04-21**: Open-TQ-Metal: int4 압축으로 48배 attention 속도 향상, 3.2x 메모리 감소 [(원문)](https://arxiv.org/abs/2604.16957)


## 핵심 주체
[[Model Efficiency]] | [[LLM-Based Hardware Optimization]]


## 모순/논쟁

