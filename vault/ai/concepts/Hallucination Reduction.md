---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Hallucination Reduction

## 정의


## 주요 발전
- **2026-01-12**: System modality에서 image/text로 attention 재분배하여 VLM yes-bias 완화 (기존 image-centric 접근 초과) [(원문)](https://arxiv.org/abs/2601.12430)
- **2026-04-22**: Context-Fidelity Boosting: 로짓 수준 적응형 가중치로 맥락 지원 토큰의 생성 확률 증가 [(원문)](https://arxiv.org/abs/2604.22335)
- **2026-04-25**: LVLM hallucination의 주요 원인은 vision backbone 제약이 아니라 textual instruction prior의 과도한 영향; preference optimization (HalluVL-DPO)로 시각 기반성 향상 [(원문)](https://arxiv.org/abs/2604.21911v1)
- **2026-04-24**: Counterfactual Segmentation Reasoning으로 세그멘테이션 VLM의 공간적 환각 심각도 측정. HalluSegBench 벤치마크 첫 제시 (arXiv:2506.21546) [(원문)](https://arxiv.org/abs/2506.21546)
- **2025-09-25**: 과학 confabulation 오류의 61%가 의미론적 무관한 분석기(salient distractor), 모든 스케일에서 근본적 결함 [(원문)](https://arxiv.org/abs/2509.25868)
- **2026-04-24**: HalluScope 벤치마크: LVLM hallucination의 주요 원인은 텍스트 지시문의 과도한 언어 선행 지식 [(원문)](https://arxiv.org/abs/2604.21911)
- **2026-04-24**: 카메라 ISP의 capture-time hallucination은 저조도 향상이나 AI 줌에서 의미론적 변화 유발 [(원문)](https://arxiv.org/abs/2604.21879)
- **2026-04-24**: SRICL: 의미 검색(SR) + 문맥 학습(ICL) + 미세조정(SFT) + 결정적 검증기로 구조화 출력 강제 (BIO 유효성, 경계 드리프트 해결) [(원문)](https://arxiv.org/abs/2604.21525)
- **2026-04-24**: DAVinCI: Claim을 내부/외부 소스에 귀속 → entailment+confidence calibration으로 검증. FEVER/CLIMATE-FEVER에서 baseline 대비 정확도 향상 (arXiv:2604.21193) [(원문)](https://arxiv.org/abs/2604.21193)
- **2025-12**: Faithfulness hallucination 검출에 설명 생성을 함께 제공하는 FaithLens 모델 (8B 파라미터) [(원문)](https://arxiv.org/abs/2512.20182)
- **2026-04-21**: Knowledge-driven hallucination: 모델의 사전학습 지식이 명시적 source evidence를 override하는 현상 (BPM 도메인에서 실증) [(원문)](https://arxiv.org/abs/2509.15336)
- **2025-05**: fs1 방법은 3.9K 팩트 기반 추론 추적으로 8개 instruction-tuned LLM을 미세조정하여 pass@16에서 6-14 포인트 개선하며, 특히 3홉 이상 KG 경로 질문과 숫자 답변 유형에서 효과적 [(원문)](https://arxiv.org/abs/2505.11140)
- **2024-12-02**: 불확실성 인식 인과 언어 모델링 손실함수로 모델이 신뢰할 수 있는 불확실성 추정 능력 확보 [(원문)](https://arxiv.org/abs/2412.02904)
- **2026-04-21**: 단계별 자기 보상 신호를 통한 추론 시점 동적 환각 완화 기법 (PSRD) [(원문)](https://arxiv.org/abs/2604.17982)
- **2026-04-21**: World Bank 큐레이션 데이터셋으로 hallucination 근본 감소 + 2,200명 평가에서 주당 2.4-3.9시간 업무 시간 절감 [(원문)](https://arxiv.org/abs/2604.17843)
- **2026-04-21**: 다중 프롬프트 투표(majority voting)로 LLM 인용 재현성 및 분산 크게 개선, 검증 없는 인용은 팩트 회상보다 학습 패턴 재구성 [(원문)](https://arxiv.org/abs/2604.16407)
- **2026-04-21**: 생성 전 증거 수준의 갈등 해결로 신뢰 불가 주장 사전 억제 [(원문)](https://arxiv.org/abs/2604.18362)
- **2026-04-21**: DoRA SFT 모델이 Llama3.1-8B 대비 QA 성공률 26% 개선, hallucination 47% 감소 [(원문)](https://arxiv.org/abs/2604.17943)
- **2026-04-20**: SPREG: 실시간 엔트로피 쌍중 임계값으로 논리적 할루시네이션 감지. 엔트로피 스파이크를 오류 신호로 활용하여 동적 가이던스 트리거 [(원문)](https://arxiv.org/abs/2604.17884)
- **2026-04-21**: 잠재 공간 기반 RAG로 텍스트 쿼리 단계 제거, 검증된 증거 기반 생성 강화 [(원문)](https://arxiv.org/abs/2604.17866)
- **2026-04-21**: 문체 재작성(style-controlled rewriting)을 통해 LLM이 factual evidence를 더 잘 활용하도록 유도 [(원문)](https://arxiv.org/abs/2604.17325)
- **2026-04-21**: GUI 에이전트의 hallucination은 cascading failures 유발; 3단계 캘리브레이션 평가 워크플로우로 VLM-as-a-judge 신뢰도 향상 [(원문)](https://arxiv.org/abs/2604.17284)
- **2026-04-21**: MeasHalu: 과학 문헌의 측정값 추출 시 hallucination을 quantities, units, modifiers, relations의 세분화된 분류로 정리. Process-based supervision과 progressive reward curriculum으로 특정 hallucination 타입 페널티 [(원문)](https://arxiv.org/abs/2604.16929)
- **2026-04-21**: PRISM 프레임: memory/instruction/reasoning/knowledge 4개 차원의 hallucination 원인 진단 (9,448 instances, 24 LLMs) [(원문)](https://arxiv.org/abs/2604.16909)
- **2026-04-21**: 검색 컨텍스트가 이미 정답인 출력까지 덮어쓰는 중립 회귀 현상 형식화 및 대응 [(원문)](https://arxiv.org/abs/2604.16686)
- **2026-04-21**: SAE 기반 위상 전이 모델로 잠재 동역학(latent dynamics)의 임계점 탐지 → 인수분해 가능한 오류 귀인 가능 [(원문)](https://arxiv.org/abs/2604.16430)
- **2026-01-27**: VIB 이론으로 VLM의 attention head 출력에서 환각 신호 추출 가능; 의미론적 노이즈 필터링으로 내부 메커니즘 기반 탐지/완화 [(원문)](https://arxiv.org/abs/2601.05547)
- **2026-01-26**: VLM의 prompt-induced hallucination은 특정 attention head의 prompt copying으로 발생; 해당 head ablation으로 최소 40% 감소 가능 [(원문)](https://arxiv.org/abs/2601.05201)
- **2025-02-20**: TPA로 다음 토큰 확률을 Query/Context/FFN/LayerNorm 등 7개 출처로 분해, 품사별 hallucination 기여도 정량화 (arXiv:2512.07515) [(원문)](https://arxiv.org/abs/2512.07515)
- **2025-12**: Lossless Encoder-Decoder: LCT→HDL→LCT 역변환으로 Hallucination 및 Omission 자동 탐지 [(원문)](https://arxiv.org/abs/2512.03053)
- **2025-11-01**: 미세조정 시 새 지식은 기존 지식 관련 할루시네이션을 전파하는 경향 발생 [(원문)](https://arxiv.org/abs/2511.02626)
- **2025-02-20**: 강화학습으로 추론을 강화하면 도구 환각이 비례적으로 증가하는 역설 발견 (SimpleToolHalluBench) [(원문)](https://arxiv.org/abs/2510.22977)
- **2025-10**: AS는 사실 베어링 토큰 주의 감소 시 언어 구조 손상 없이 할루시네이션 방지 [(원문)](https://arxiv.org/abs/2510.17210)
- **2026-04-20**: arXiv:2510.09033 - Hallucination을 Unassociated(매개변수 근거 없음) vs Associated(허위 통계 기반) 분류. 후자는 정상 회상과 내부 패턴 동일 [(원문)](https://arxiv.org/abs/2510.09033)
- **2025-05-21**: RAG output의 factuality vs faithfulness 구분으로 context-unsupported but factually correct 답변의 오판 제거 [(원문)](https://arxiv.org/abs/2505.21072)
- **2026-04-20**: LLM 훈련 시 hallucination detection head를 직접 신호로 사용하는 RAGognizer 방식 제안 [(원문)](https://arxiv.org/abs/2604.15945)
- **2026-04-20**: 청크 서명 기반 의미 충돌 감소, 검색기 판별력 강화 [(원문)](https://arxiv.org/abs/2604.15802)
- **2026-04-20**: prompt 엔지니어링과 retrieval 기반 메서드로 거짓 주장 감소 가능하나 trade-off 존재 [(원문)](https://arxiv.org/abs/2604.15789)
- **2026-04-20**: Token-wise, layer-wise 불확실성 추정으로 factual error 탐지 [(원문)](https://arxiv.org/abs/2604.15741)
- **2026-04-20**: Fine-tuning 중 매개변수 고정으로 사전학습 지식 보존 및 hallucination 감소 [(원문)](https://arxiv.org/abs/2604.15574)
- **2026-04-20**: SSAS의 bounded attention + 고신호 감정 중심 프롬프트로 환각 감소 및 엔터프라이즈 수준 신뢰도 달성 [(원문)](https://arxiv.org/abs/2604.15547)
- **2026-04-20**: LLM 환각은 초기 단계에서 asymmetric attractor dynamics로 인한 궤적 커밋. 첫 토큰부터 분기 가능성 44.3% (arXiv:2604.15400) [(원문)](https://arxiv.org/abs/2604.15400)
- **2026-04-19**: LLM 기계번역에서 오버제네레이션의 3가지 유형: 자기설명(자연스러움), 거짓 생성(위험), 적절한 설명(번역가 역할) — 상용 환경 탐지 전략 개발 [(원문)](https://arxiv.org/abs/2604.15165v1)
- **2026-04-17**: V-Reflection: Box-Guided Compression Module로 MLLMs의 미세한 인식 환각 감소 (arXiv:2604.03307) [(원문)](https://arxiv.org/abs/2604.03307)
- **2026-04-17**: VLM 69.6%가 시각 이상 감지 후에도 사용자 기대 만족을 위해 환각 반복 (Visual Sycophancy) [(원문)](https://arxiv.org/abs/2603.18373)
- **2025-10-14**: Hallucination은 기술적 버그가 아닌 통계적 패턴 예측과 인간 직관의 결합으로 인한 체계적 오해 [(원문)](https://arxiv.org/abs/2510.14665)
- **2026-04-17**: KnowRL: 지식 검증 기반 팩트성 보상을 RL 훈련에 통합하여 느린 사고 중 환각 감소 [(원문)](https://arxiv.org/abs/2506.19807)
- **2025-05-20**: 느린 추론(System II) 모델이 불완전하거나 오도된 시각 입력에 대해 깊이 우선 탐색으로 잘못된 전제를 지속 탐색하며 더 자주 거짓 상세정보를 구성하는 역스케일링 법칙 발견 [(원문)](https://arxiv.org/abs/2505.20214)
- **2026-04-17**: LLM CoT 추론이 생물의료 데이터 분석에서 모델 saliency 결과의 confounders 검증에 효과적 [(원문)](https://arxiv.org/abs/2604.14334)
- **2026-04-17**: 의미론적으로 일관되나 사실상 부정확한 LLM 응답의 불확실성을 claim-level에서 측정 가능 (arXiv:2604.15109) [(원문)](https://arxiv.org/abs/2604.15109)
- **2026-04-17**: 환각은 시맨틱 드리프트의 증상. 해석 가능한 추론 추적이 구조적 해결책으로, 표현 불일치 조기 감지 가능 [(원문)](https://arxiv.org/abs/2604.14881)
- **2026-04-17**: 의료 문서화에서 hallucination 정의를 lexical faithfulness에서 clinical grounding 기반으로 재정의 필요 [(원문)](https://arxiv.org/abs/2604.14829)
- **2026-04-17**: 스펙트럼 필터링: semantic signals는 topologically smooth, noise는 high-frequency. SCR로 신호 부분공간만 consistency 강제하여 LLM hallucination 제거 및 over-smoothing 방지 [(원문)](https://arxiv.org/abs/2604.14746)
- **2026-04-17**: 같은 중간 상태에서의 대체 연속으로 정답 도달 가능. 초기 전환점 재지정으로 망각(hallucination) 감소 [(원문)](https://arxiv.org/abs/2604.14528)
- **2026-04-17**: 글로벌 만족도 제약으로 개별 쿼리 정확도 유지하면서 다중 쿼리 모순 감소 [(원문)](https://arxiv.org/abs/2604.14525)
- **2026-04-17**: GeoDe 프레임워크: 결정 초평면 근처의 '회색지대'(내부 신념 불확실성)를 기하 거리 신뢰 신호로 정제하여 추상화 미세조정에서 경계 레이블 노이즈 제거 [(원문)](https://arxiv.org/abs/2604.14324)
- **2026-04-17**: MoE 모델의 반사실적 라우팅 (CoR): long-tail 지식 expert 활성화로 할루시네이션 완화 (비훈련 추론) [(원문)](https://arxiv.org/abs/2604.14246)
- **2026-04-17**: 취약점 분석 도메인에서 RAG 기반 지식 재검증으로 hallucination 감소 [(원문)](https://arxiv.org/abs/2604.14172)
- **2026-04-14**: Stateful Evidence-Driven RAG: 증거 누적을 명시적으로 추적하고 반복 추론으로 노이즈 강건성 개선 [(원문)](https://arxiv.org/abs/2604.14170)
- **2026-04-14**: Inverse Reasoning 파이프라인으로 복잡한 추론 작업에서 hallucination 최소화 [(원문)](https://arxiv.org/abs/2604.14168)


## 핵심 주체
[[Vision-Language Models]] | [[Modality Dominance in Vision-Language Models]]


## 모순/논쟁

