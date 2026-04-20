---
type: concept
domain: ai
last_updated: 2026-04-20
source_count: 0
---

# LLM Safety Alignment

## 정의


## 주요 발전
- **2026-04-20**: 높은 유창성의 AI 인터페이스는 오토메이션 편향과 조기적 인지적 폐쇄를 유도, 사용자의 비판적 인식 능력 약화 [(원문)](https://arxiv.org/abs/2603.21735)
- **2025-10-15**: Web 검색 통합으로 무해한 쿼리로부터 유해 콘텐츠 인용 유도 가능 (CREST-Search) [(원문)](https://arxiv.org/abs/2510.09689)
- **2026-01-03**: RedBench: 37개 벤치마크 통합, 29,362 샘플, 22 위험 카테고리, 19 도메인 표준화 [(원문)](https://arxiv.org/abs/2601.03699)
- **2025-02-20**: GRPO 기반 강화학습으로 유사 프롬프트에 대한 답변 일관성 보장, RAG·온도 조절 이상의 근본적 해결 (arXiv:2512.12858) [(원문)](https://arxiv.org/abs/2512.12858)
- **2025-02-20**: 추론 능력 강화와 안전성(환각 감소) 간의 인과적 긴장 관계 [(원문)](https://arxiv.org/abs/2510.22977)
- **2025-10**: 언러닝 시 모델 신뢰성 확보: 지식 제거와 유틸리티 보존의 trade-off 해결 [(원문)](https://arxiv.org/abs/2510.17210)
- **2025-09-19**: Wasserstein/KL/χ² 모호도 기반 DRO-REBEL로 RLHF 과최적화 방지 및 수렴성 증명 [(원문)](https://arxiv.org/abs/2509.19104)
- **2025-09-05**: 상대적 곤혹도 차이로 응답 간결성과 정확성의 균형 달성 [(원문)](https://arxiv.org/abs/2509.05489)
- **2025-06-20**: LLM이 인간의 정치적/사회적 동기에 따라 추론 방향을 편향시킴 (8개 모델 실험) [(원문)](https://arxiv.org/abs/2506.20020)
- **2025-05-24**: TRIDENT - lexical diversity, malicious intent, jailbreak tactics 3차원 포괄 red-teaming 데이터 합성 [(원문)](https://arxiv.org/abs/2505.24672)
- **2025-04-20**: 중간 추론 단계 검증이 최종 답변 정확성만큼 중요함을 실증 [(원문)](https://arxiv.org/abs/2505.13792)
- **2026-04-20**: In-situ 대화 중 사용자 피드백을 자동 수집하여 선호도 데이터셋 생성(WildFeedback) [(원문)](https://arxiv.org/abs/2408.15549)
- **2026-04-20**: OpenAI, Anthropic, Google LLM은 콘텐츠 선별에서 polarization 증폭. 프롬프트 전략(general, popular, engaging 등)에 따라 편향 강도·방향 다름 (arXiv:2604.15937) [(원문)](https://arxiv.org/abs/2604.15937)
- **2026-04-20**: 분산 LLM 환경에서 라우팅 성능 최적화가 사용자 데이터 프라이버시와 충돌할 수 있음을 최초 실증 [(원문)](https://arxiv.org/abs/2604.15728)
- **2026-04-20**: 다중모달 프롬프트 엔지니어링 시스템에서 48시간 내 관찰 가능한 행동 변화 발생(의사결정 이양, 자율성 상실) [(원문)](https://arxiv.org/abs/2604.15343)
- **2026-04-20**: 능력감은 의인화를 제외한 모든 결과 예측. 감정적 공감은 관계 척도만 예측하고 epistemic 결과(신뢰, 유용성) 미예측 [(원문)](https://arxiv.org/abs/2604.15316)
- **2026-04-20**: Test-time alignment의 proxy 기반 rejection criterion: confidence의 언어학적 모호성(ambiguous phrasing) 한계 지적, 보수적 confidence bet으로 개선 [(원문)](https://arxiv.org/abs/2604.16146)
- **2026-04-20**: 확률적 토크나이제이션으로 적대적 공격과 무작위 섭동에 대한 견고성 향상 [(원문)](https://arxiv.org/abs/2604.16037)
- **2026-04-20**: 내부 상태 표현 기반 hallucination detection을 joint optimization으로 통합하는 안전성 강화 방식 [(원문)](https://arxiv.org/abs/2604.15945)
- **2026-04-20**: 훈련 없는 메서드(prompt-based, retrieval-based, input/output modification)로 신뢰성 향상 가능하나 utility degradation과 brittleness 주의 필요 [(원문)](https://arxiv.org/abs/2604.15789)
- **2026-04-20**: Pruning Unsafe Tickets: 그래디언트 프리 속성화로 안전하지 않은 서브네트워크 직접 제거하며 유틸리티 보존 [(원문)](https://arxiv.org/abs/2604.15780)
- **2026-04-20**: Healthcare/education 고위험 domain에서 reasoning step의 safety가 final answer만큼 critical [(원문)](https://arxiv.org/abs/2604.15725)
- **2026-04-20**: 자가 피드백을 통한 에이전트의 정책 해석 자동 정제로 alignment 실패 감소 [(원문)](https://arxiv.org/abs/2604.15505)
- **2026-04-20**: 파라미터 업데이트 없는 경량 추론 시간 스티어링으로 안전성 위반, 할루시네이션 완화. 일원형 설계 대신 조건부+전문가 메커니즘으로 유용성 보존 [(원문)](https://arxiv.org/abs/2604.15488)
- **2026-04-20**: 통합 데이터 표현과 양방향 로짓 증류(bidirectional logit distillation)로 언러닝 목표 간 간섭(task interference) 해결 [(원문)](https://arxiv.org/abs/2604.15482)
- **2026-04-19**: Aligned LLM도 게임이론 설정에서 기본값으로 defect하는 안전 문제 [(원문)](https://arxiv.org/abs/2604.15267v1)
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
[[AI Safety]] | [[Human-AI Cognitive Alignment]] | [[AI Regulation]]


## 모순/논쟁

