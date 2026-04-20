---
type: concept
domain: ai
last_updated: 2026-04-20
source_count: 0
---

# Fine-tuning

## 정의


## 주요 발전
- **2026-02-15**: 학생 모델이 교사 모델을 무단 증류할 때 성능 저하를 유도하는 anti-distillation 기법 적용 [(원문)](https://arxiv.org/abs/2602.15143)
- **2025-10**: 제한된 계산 예산 하에서 DP fine-tuning의 배치 크기 선택은 누적 DP 노이즈로 설명 가능 [(원문)](https://arxiv.org/abs/2510.20616)
- **2025-04-20**: SAI-DPO를 통한 자가 인식 동적 샘플링으로 수학 추론 효율성 개선 [(원문)](https://arxiv.org/abs/2505.16176)
- **2026-04-20**: UA-Net: ImageNet 사전학습 → TRISO 미세사진 도메인 파인튜닝 → 메타모델 기반 불확실성 예측 [(원문)](https://arxiv.org/abs/2604.15542)
- **2026-04-20**: Multi-agent 기반 고품질 테스트벤치 자동화로 파인튜닝 데이터 양 감소 가능 (2026-04-20) [(원문)](https://arxiv.org/abs/2604.15388)
- **2026-04-20**: DeepInsightTheorem 데이터셋: 증명 작성 → insightful thinking 진화 학습, human learning process 모방 [(원문)](https://arxiv.org/abs/2604.16278)
- **2026-04-20**: 크로스모달 그래디언트 비대칭 문제 해결을 위한 계층별 직교 그래디언트 투영 기법 [(원문)](https://arxiv.org/abs/2604.16067)
- **2026-04-20**: Chain-of-Thought 증류 계열에서 대부분의 의미론적 다양성 손실은 지도 학습 단계에서 발생 [(원문)](https://arxiv.org/abs/2604.16027)
- **2026-04-20**: MLLM 강화학습 미세조정 시 내생적 추론 드리프트 발견: 외생적 변화와 구별, 자동회귀 생성 중 예측 불가능한 분포 변화 [(원문)](https://arxiv.org/abs/2604.15705)
- **2026-04-20**: FFT는 LoRA/QLoRA 대비 통계적으로 다른 집중도 높은 귀속 패턴 생성 [(원문)](https://arxiv.org/abs/2604.15589)
- **2026-04-20**: 자체-증류 기반 fine-tuning으로 출력 분포 변화 제약하여 hallucination 억제 가능 [(원문)](https://arxiv.org/abs/2604.15574)
- **2026-04-20**: Layer selection probe로 task-relevant layer만 LoRA 적용 시 학습 속도 15-28% 향상 [(원문)](https://arxiv.org/abs/2604.15351)
- **2026-04-17**: SLM 리랭킹에 두 단계 학습(RL 프롬프트 + 세분화 점수)로 좁은 표현 공간 극복 [(원문)](https://arxiv.org/abs/2506.03487)
- **2026-04-17**: Post-training 분류: off-policy(외부 궤적) vs on-policy(모델 생성 롤아웃)로 체계화 (arXiv:2604.07941) [(원문)](https://arxiv.org/abs/2604.07941)
- **2026-04-17**: Llama 1.3B까지 hybrid 구조에서 SAGE 적용 시 메모리 효율성 개선 (arXiv:2604.07663) [(원문)](https://arxiv.org/abs/2604.07663)
- **2026-04-17**: 표준→방언 전이학습에서 음성 모델이 텍스트 모델보다 우월, 자동 음성인식 정규화 필수 [(원문)](https://arxiv.org/abs/2510.07890)
- **2026-04-17**: SPaCe: 자기 속도 커리큘럼 학습으로 LLM RL 훈련의 표본 효율성 극대화, 데이터 중복도 제거 [(원문)](https://arxiv.org/abs/2508.05015)
- **2025-02-01**: 2025-02: 공중 여론조사 데이터(SubPOP 3,362Q/70K 응답쌍) 파인튜닝으로 인간-LLM 응답 분포 격차 46% 축소 [(원문)](https://arxiv.org/abs/2502.16761)
- **2026-04-17**: Retention-prioritized gradient synthesis: target 지식 제거 시 일반 능력 보존 최적화 [(원문)](https://arxiv.org/abs/2604.14808)
- **2026-04-17**: Kronecker 제약으로 무게 템플릿과 크기별 스케일러 분리, 가변 크기 초기화 문제를 멀티태스크 적응으로 변환 [(원문)](https://arxiv.org/abs/2604.14769)
- **2026-04-17**: 불확실성 기반 CoT 자체 합성으로 강모델 증류 및 테스트타임 탐색의 계산 부담 완화 [(원문)](https://arxiv.org/abs/2604.14768)
- **2026-04-17**: 메모리 효율적 대규모 모델 미세조정 시 ZO 방법의 안정성 조건 수립 [(원문)](https://arxiv.org/abs/2604.14669)
- **2026-04-17**: BabyLM 데이터로 훈련한 LM도 wh-question과 topicalization 간 filler-gap 표현 이전 가능, 인간 수준 일반화엔 훨씬 더 많은 데이터 필요 [(원문)](https://arxiv.org/abs/2604.14459)
- **2026-04-17**: Group Fine-Tuning(GFT): SFT를 극도로 희소한 암시 보상을 가진 정책 그래디언트 특수 사례로 재해석. 그룹 어드밴티지 러닝으로 응답 그룹 구성 후 정규화된 대조 감독 적용 [(원문)](https://arxiv.org/abs/2604.14258)
- **2026-04-14**: QLoRA + Rank-Stabilized LoRA(r=32)로 8B 오픈소스 모델의 네팔어 이해도 향상 [(원문)](https://arxiv.org/abs/2604.14171)
- **2026-04-17**: 교사-학생 협력 데이터 합성(TESSY): 교사 모델의 추론 능력 보존하면서 합성 시퀀스의 스타일을 학생 모델 분포와 정렬하여 미세조정 성능 저하 문제 해결 [(원문)](https://arxiv.org/abs/2604.14164)


## 핵심 주체
[[LLM Watermarking]] | [[Private Inference]]


## 모순/논쟁

