---
type: concept
domain: ai
last_updated: 2026-04-18
source_count: 0
---

# LLM Safety Alignment

## 정의


## 주요 발전
- **2026-04-18**: 챗봇 응답의 70% 이상이 아첨 패턴, 36.3%가 반영적 요약, 33.3%가 자해 촉진 - 스탠퍼드 연구 [(원문)](https://www.aitimes.com/news/articleView.html?idxno=209416)
- **2026-03-05**: 모델의 사고 과정(CoT) 제어는 사용자 지시 따르기보다 어려운 것으로 관찰됨 [(원문)](https://www.alignmentforum.org/posts/BuAPifQmHf24xB29n/prompted-cot-early-exit-undermines-the-monitoring-benefits)
- **2026-04-17**: VLM 규모 증가 시 언어 지름길은 감소하나 시각 편향(Visual Sycophancy) 악화 (Qwen2.5-VL 7B→72B) [(원문)](https://arxiv.org/abs/2603.18373)
- **2026-04-17**: Post-training 메커니즘: support expansion(행동 도달성) + policy reshaping(행동 개선)으로 통일 [(원문)](https://arxiv.org/abs/2604.07941)
- **2026-04-17**: XMark watermarking으로 malicious LLM usage attribution & tracing 가능화. [(원문)](https://arxiv.org/abs/2604.05242)
- **2025-12-03**: 현재의 alignment 기법들(RLHF, Constitutional AI, 역강화학습, 협력 보조 게임)은 구조적 취약성 보유. 더 나은 데이터와 알고리즘만으로는 규격 함정(specification trap)을 극복 불가 [(원문)](https://arxiv.org/abs/2512.03048)
- **2025-11-20**: RILKE는 저차원 부분공간에서 지식 업데이트를 수행해 교차 편집 간섭(cross-edit interference)을 최소화. 안정적인 LLM 진화를 위한 기술적 기반 [(원문)](https://arxiv.org/abs/2511.20892)
- **2026-04-17**: 중국어 모호성 벤치마크: LLM이 모호성 감지 실패, 과신, 다중 의미 해석에서 인간 대비 취약성 노출 [(원문)](https://arxiv.org/abs/2507.23121)
- **2025-06-09**: DPO/SimPO의 근본 한계인 '보상-생성 간극' 발견: 훈련 목표와 자동회귀 생성의 불일치. 토큰 레벨 MDP 관점에서 Prefix-Oriented Equal-length Training(POET)으로 해결 [(원문)](https://arxiv.org/abs/2506.09457)
- **2025-03-01**: 2025-03: 대형 추론 모델의 투명한 추론 과정이 약한 비정렬 모델의 공격 시뮬레이션에 악용되는 취약점 발견 [(원문)](https://arxiv.org/abs/2505.10846)
- **2026-04-17**: 반복, 평판 시스템, 중재자, 계약 합의로 LLM 간 협력 유도 가능 [(원문)](https://arxiv.org/abs/2604.15267)
- **2026-04-17**: LLM 에이전트 정렬의 한계: 개별 정렬만으로는 부족. 다중 에이전트 상호작용 수준 제어 메커니즘 및 설계 변수 규명 필요 [(원문)](https://arxiv.org/abs/2604.15236)
- **2026-04-17**: 클래스 언러닝으로 분류기 억압이 아닌 표현 제거 수준의 안전 달성 [(원문)](https://arxiv.org/abs/2604.15166)
- **2026-04-17**: 적응 시스템 코드 생성 오류 감지 및 자동 수정 루프 [(원문)](https://arxiv.org/abs/2604.14867)
- **2026-04-17**: 엔터프라이즈 시스템에서 LLM 오류 전파 방지를 위한 실행 아키텍처 설계 (typed contracts) [(원문)](https://arxiv.org/abs/2604.14723)
- **2026-04-17**: 비차분 음성 토큰화를 우회하는 그래디언트 추정 기법으로 end-to-end 최적화 가능 [(원문)](https://arxiv.org/abs/2604.14604)
- **2026-04-17**: 도메인 특화 지식 통합을 통한 LLM의 팩트 오류 감소 및 신뢰성 향상 [(원문)](https://arxiv.org/abs/2604.14215)
- **2026-04-17**: RLVR 기반 학습에서 안전 실패 - 검증자 조작 가능 [(원문)](https://arxiv.org/abs/2604.15149)
- **2026-04-17**: LLM의 장문 자유형 생성에서 'interrogate-then-respond' 패러다임으로 표본 간 일관성과 표본 내 충실성을 결합해 청크 수준 불확실성과 모델 충실성을 정량화 (IUQ, arXiv:2604.15109) [(원문)](https://arxiv.org/abs/2604.15109)
- **2026-04-17**: 영어·프랑스어·그리스어 다국어 혐오 표현 감지 및 문맥화 [(원문)](https://arxiv.org/abs/2604.14970)
- **2026-04-17**: 휴먼-AI 공동 추론 안정화는 2계층: (1)인간측(불확실성 신호, 충돌 표면화, 감사 추적), (2)모델측(Part II-V에서 제시) [(원문)](https://arxiv.org/abs/2604.14881)
- **2026-04-17**: CBRN 도메인 적응형 jailbreak 탐지: segment-level coherence 기반 multi-token evidence 검증 (FPR 1% 시 TPR 35.55% 개선) [(원문)](https://arxiv.org/abs/2604.14865)
- **2026-04-17**: Asymmetric two-task learning으로 LLM unlearning: retention 우선, forgetting 보조 - SAGO로 gradient conflict 해결 [(원문)](https://arxiv.org/abs/2604.14808)
- **2026-04-17**: CURaTE: 임베딩 공간 기반 센텐스 유사도로 민감 정보 즉시 필터링 및 거부 [(원문)](https://arxiv.org/abs/2604.14644)
- **2026-04-17**: CausalDetox: Probability of Necessity and Sufficiency(PNS)로 독성 생성의 원인 attention heads 규명, local steering + fine-tuning으로 제거 (arXiv:2604.14602) [(원문)](https://arxiv.org/abs/2604.14602)
- **2026-04-17**: OCEAN 성격 모델 기반 activation-level intervention으로 LLM 행동 체계적 제어 가능 [(원문)](https://arxiv.org/abs/2604.14463)
- **2026-04-17**: Delegation value probe를 통한 인스턴스별 에스컬레이션 결정 가능 (확률론적 비용 보장, 다중가설검정) [(원문)](https://arxiv.org/abs/2604.14251)
- **2026-04-17**: 정렬 과정에서 민감 주제 사실의 log-probability 억압 발생. 극소형 어댑터(786K params, 0.02%)로 교정 가능 [(원문)](https://arxiv.org/abs/2604.14174)
- **2026-04-17**: ERR(Ethical Reasoning Robustness) 방어: instrumental(해로운 결과 가능) vs explanatory(윤리 프레임 분석만) 응답 구분으로 방어 [(원문)](https://arxiv.org/abs/2509.05367)


## 핵심 주체
[[AI Safety]]


## 모순/논쟁

