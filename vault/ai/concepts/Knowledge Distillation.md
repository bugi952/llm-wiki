---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Knowledge Distillation

## 정의


## 주요 발전
- **2026-04-27**: 교사 LLM → 학생 트랜스포머 감각 임베딩 증류로 고정 차원 표현 생성, Amazon 다중 도메인 순차 추천 성능 향상 [(원문)](https://arxiv.org/abs/2603.02709)
- **2026-02-05**: 극좌표 표현의 방향-방사 분해로 각도 일관성과 크기 일관성을 분리하는 비대조적 증류 기법 (arXiv:2602.05639) [(원문)](https://arxiv.org/abs/2602.05639)
- **2026-04-27**: Utility-Modulated InfoNCE로 LLM 재랭킹 신호를 bi-encoder 임베딩에 주입 시 테스트 시점 LLM 추론 제거 가능 [(원문)](https://arxiv.org/abs/2604.22722)
- **2026-04-25**: RedirectQA 벤치마크로 entity name 로버스트니스 측정 가능, 모델별 편차 명확 [(원문)](https://arxiv.org/abs/2604.21882v1)
- **2026-01**: 추론 증류의 함수적 정렬 붕괴: 교사(r=0.64)는 인간 난이도와 일치하나 학생(r=0.34)은 저하, 리소스 할당 정책 미전달로 Cargo Cult 효과 [(원문)](https://arxiv.org/abs/2601.05019)
- **2024-11-11**: 서버 LLM → 클라이언트 SLM 지식 증류, 동시에 클라이언트 도메인 지식 → 서버 LLM 역전이 [(원문)](https://arxiv.org/abs/2411.11707)
- **2026-04-24**: LLM 생성 user profile을 sequential recommender로 inference-time LLM 호출 없이 증류 [(원문)](https://arxiv.org/abs/2604.21536)
- **2026-04-24**: 에이전트 증류의 부작용: 같은 교사 출신 모델 쌍이 교차 쌍 대비 Action Graph Similarity 5.9pp 높음 [(원문)](https://arxiv.org/abs/2604.21255)
- **2026-04-22**: Federated 설정에서 LLM→SLM 압축으로 프라이버시 보호 전략 [(원문)](https://arxiv.org/abs/2604.19015)
- **2026-04-22**: Distillation gradient를 reward signal로 활용해 적응적 가중치 최적화 [(원문)](https://arxiv.org/abs/2604.19009)
- **2026-04-22**: 증류 함정: 꼬리 노이즈·정책 불안정성·교사-학생 간극이 훈련 신호 왜곡. 과신감 환각·자기수정 붕괴·국소 디코딩 저하 유발 [(원문)](https://arxiv.org/abs/2604.18963)
- **2026-04-21**: Privileged information 주입 방식 대신 모델의 내재적 단기 능력 활용 self-distillation [(원문)](https://arxiv.org/abs/2604.17535)
- **2026-04-21**: Reasoning-aware summarizer 초기화: teacher 모델의 structured reasoning 증류 [(원문)](https://arxiv.org/abs/2604.17188)
- **2026-04-21**: 온정책 증류(OPD)는 accuracy 개선하나 심각한 과신(miscalibration) 발생. 학습 시 특권 정보와 배포 시 정보 불일치가 근본 원인 [(원문)](https://arxiv.org/abs/2604.16830)


## 핵심 주체
[[LLM Data Augmentation]] | [[Synthetic Data Generation]] | [[Semantic Document Retrieval]]


## 모순/논쟁

