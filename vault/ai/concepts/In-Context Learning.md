---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# In-Context Learning

## 정의


## 주요 발전
- **2026-04-27**: LLMs는 prompt 내 HMM 예제로부터 pattern을 inferring하여 이론적 최적값에 근접한 예측 성능 달성 가능; 동물 의사결정 같은 현실 시계열 데이터에서도 expert 모델과 경쟁 가능 [(원문)](https://arxiv.org/abs/2506.07298)
- **2025-10-01**: 저랭크 회귀 작업에서 통계 요동이 암묵적 정규화 유발, 과제 구조에 따라 일반화 오류의 급격한 위상 전이 발생 [(원문)](https://arxiv.org/abs/2510.04548)
- **2026-04-24**: Embedding 자체의 성능을 downstream classifier 영향 제거하고 직접 평가하는 classifier-independent 방법론 [(원문)](https://arxiv.org/abs/2604.21555)
- **2026-04-22**: 그래프의 homophily, community structure를 in-context에서 학습하는 foundation model 접근 [(원문)](https://arxiv.org/abs/2604.19028)
- **2026-04-21**: 16개 ICL 예제로 Gemini, Kimi-K2, Grok, Qwen 전 모델에서 1-24% 이상정렬률 발생, 2개 예제로도 나타남 [(원문)](https://arxiv.org/abs/2510.11288)
- **2025-10-14**: 2025년 controlled experiment: parametric/in-context 지식의 robust 균형 활용은 intra-document inconsistency(moderate level)와 반복성의 co-occurrence 필요 [(원문)](https://arxiv.org/abs/2510.02370)
- **2026-04-21**: Context-memory 충돌 상황에서 context reiteration이 context-only task는 개선하지만 parametric knowledge 필요 task는 성능 저하 (2026-04-21) [(원문)](https://arxiv.org/abs/2506.06485)
- **2026-04-21**: 쌍 비교 추론이 오디오 도메인의 할루시네이션 필터링에 효과적 [(원문)](https://arxiv.org/abs/2604.16749)
- **2026-04-21**: 시계열의 맥락 동역학을 자연언어 설명으로 변환하여 LLM의 체인오브싱크 추론 패턴 활용 [(원문)](https://arxiv.org/abs/2604.18305)
- **2026-04-21**: 컨텍스트 메모리의 동적 활용 시점 결정이 성능 향상의 핵심, 증거 기반 메모리 은행 관리로 장기 효율성 보장 [(원문)](https://arxiv.org/abs/2604.18206)
- **2026-04-21**: ICL과 LoRA는 저차원 대응(low-rank correspondence) 원리로 동일한 기하학적 구조 탐색 [(원문)](https://arxiv.org/abs/2604.17384)
- **2026-04-16**: Non-stationary sequences에서 transformer는 unknown change-point 감지 후 동적 적응 가능 (형식적 증명), model complexity는 change-point 정보 수준에 따라 결정 [(원문)](https://arxiv.org/abs/2604.16988)
- **2026-04-21**: SemanticQA: 다중어 표현(MwE), 관용구, 명사 복합어에서 LLM의 의미 추론 성능 편차 분석 [(원문)](https://arxiv.org/abs/2604.16593)
- **2026-04-21**: LiFT: 시간적 난이도 증가 커리큘럼과 few-shot 구조화로 역사 컨텍스트 통합 개선 [(원문)](https://arxiv.org/abs/2604.16382)
- **2026-04-20**: 다중 심리 패턴의 강화·갈등·조절 상호작용이 in-context 성능에 영향 [(원문)](https://arxiv.org/abs/2601.10198)
- **2025-12**: In-Context Distillation: Teacher의 시범 학습 후 저비용 Student에 In-Context 예제로 배포 [(원문)](https://arxiv.org/abs/2512.02543)
- **2026-04-20**: ICL을 활용한 개인화 보상 모델링으로 재훈련 없이 사용자 적응 가능 [(원문)](https://arxiv.org/abs/2502.19312)
- **2026-04-20**: ACSESS: 23개 샘플 선택 전략 자동 조합으로 개별 전략 대비 일관된 성능 개선(5개 모델, 14개 데이터셋 검증) [(원문)](https://arxiv.org/abs/2402.03038)
- **2026-04-20**: 음성/음악 신호의 transient 특성을 정확히 포착하는 contrastive 기반 디코딩 방식 (2026-04-20) [(원문)](https://arxiv.org/abs/2604.15383)
- **2026-04-20**: SemEval-2026 Task 5: narrative 텍스트에서 few-shot prompting으로 human-like plausibility 판단 달성 [(원문)](https://arxiv.org/abs/2604.16262)
- **2026-04-20**: 18개 NER 벤치마크에서 모델간 불일치 분석을 통한 지시 개선 효과 검증 [(원문)](https://arxiv.org/abs/2604.15866)
- **2026-04-20**: Brain Score로 측정한 LM의 구조 추출 능력은 자연언어뿐만 아니라 DNA, Python 등 비언어 시퀀스에도 일관됨 [(원문)](https://arxiv.org/abs/2604.15503)
- **2026-04-20**: 언어 혼용(code-switching)이 맥락 학습 성능 개선에 기여 [(원문)](https://arxiv.org/abs/2604.15490)
- **2026-04-19**: 최단경로 계획에서 LLM은 공간 이동(spatial transfer)에는 강하나 길이 확장(length scaling)에서 재귀적 불안정으로 실패 [(원문)](https://arxiv.org/abs/2604.15306v1)
- **2026-02-22**: 장문맥 입력에서 attention이 관련 context와 정렬 유지 어려움, 동적 조정으로 개선 [(원문)](https://arxiv.org/abs/2602.22175)
- **2026-02-20**: RAG에서 검색 문서의 관련성이 LLM 숨겨진 상태를 동적 변화시킴 (4 QA 데이터셋, 3개 LLM 실증) [(원문)](https://arxiv.org/abs/2602.20091)
- **2026-01-07**: multilingual thinking의 Single-Language vs Mixed-Language Sampling으로 output 다양성 체계적 제어 [(원문)](https://arxiv.org/abs/2601.11227)
- **2026-01-01**: LLM이 22회 파인튜닝 사이클을 통해 신경망 아키텍처 설계 역량 점진적 습득. MinHash-Jaccard로 중복 구조 필터링 [(원문)](https://arxiv.org/abs/2601.02997)
- **2024-10-01**: GPT-4/4o를 이용한 symbolic regression 성공. Chain-of-thought prompting으로 데이터 분석 후 수학 표현식 유도 [(원문)](https://arxiv.org/abs/2410.17448)
- **2026-04-17**: 실시간 시장 신호(주문서)와 뉴스의 동시 맥락화로 예측 수행, 시간 규칙이 엄격한 예측 시장에 적용 [(원문)](https://arxiv.org/abs/2604.14199)
- **2026-04-17**: 장문맥 추론의 sparse 구조를 활용한 선택적 가중치 업데이트 전략 [(원문)](https://arxiv.org/abs/2604.14922)
- **2026-04-17**: 유전 알고리즘으로 Chain-of-Thought 궤적 진화, 전역 교배+국소 돌연변이로 다양성 확보 [(원문)](https://arxiv.org/abs/2604.14768)
- **2026-04-17**: Narrative reformulation으로 코드 생성 성능 18.7% 향상 (HumanEval, 11개 모델 zero-shot) [(원문)](https://arxiv.org/abs/2604.14631)
- **2026-04-17**: 정보론적 기초로 메모리 선택 시 응답 불확실성 감소 및 예측 정밀도 향상 [(원문)](https://arxiv.org/abs/2604.14473)
- **2026-04-17**: RoPE perturbation + 자기 증류로 컨텍스트 위치 강건성 개선, RAG·다중 문서 추론 정확도 향상 [(원문)](https://arxiv.org/abs/2604.14339)
- **2026-04-14**: 중국 에세이 수사학 인식에 LoRA와 ICL을 결합하여 CCL 2025 평가 1위 [(원문)](https://arxiv.org/abs/2604.14167)


## 핵심 주체
[[Latent Reasoning]] | [[Time Series Reasoning]]


## 모순/논쟁

