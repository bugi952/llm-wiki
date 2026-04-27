---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Mechanistic Interpretability

## 정의


## 주요 발전
- **2026-04-21**: LLM hidden state에서 digit-count 경계(10, 100)에 기하학적 왜곡 발생 (log-distance + boundary boost 모델) [(원문)](https://arxiv.org/abs/2603.28258)
- **2025-02-01**: CCG: sparse autoencoders + DAGMA 구조 학습으로 LLM 개념 간 인과 의존성 추출, Causal Fidelity Score로 검증 [(원문)](https://arxiv.org/abs/2603.10377)
- **2026-04-27**: Retrieval head 최적화(RetMask)는 mechanistic insight를 성능 개선으로 직접 전환. 일반 작업 성능을 보존하면서 장문맥 능력 강화. [(원문)](https://arxiv.org/abs/2601.11020)
- **2025-12-05**: TopK SAE는 생물학적 개념 매핑에 효과적이나, Ordered SAE는 생성 제어 신뢰도에서 우수 (트레이드오프) [(원문)](https://arxiv.org/abs/2512.05794)
- **2024-10**: 라벨된 Concept Atlas에 새 모델을 정렬하여 sparse autoencoder 학습 비용 제거 가능 [(원문)](https://arxiv.org/abs/2510.27413)
- **2025-05-01**: LLM 내부 표현의 고차원 기하학을 persistent homology로 정량화하여 선형/특징 중심 해석성의 한계 극복 [(원문)](https://arxiv.org/abs/2505.20435)
- **2026-04-27**: Contrastive Semantic Projection (CSP): Vision Language Model 기반 뉴런 라벨링. 활성화 예시 + 대조적 예시로 더 정확하고 충실한 뉴런 설명 생성 [(원문)](https://arxiv.org/abs/2604.22477)
- **2026-04-22**: Hessian을 통한 feature-level interaction 감지 방법 등장 [(원문)](https://arxiv.org/abs/2604.22045)
- **2026-04-27**: ego 속성, 동네 smoothing, 고주파 그래프 차이, 클래스 기하를 분리하여 message passing의 entangled 표현 해제 [(원문)](https://arxiv.org/abs/2604.22676)
- **2026-04-26**: Differential Preference Steering(DPS): 인과 마스킹으로 선호도 헤드 식별·선호도 기여도 점수(PCS) 계산 [(원문)](https://arxiv.org/abs/2604.22345)
- **2026-04-27**: Activation patching으로 filler-gap dependency의 localized shared mechanism 발견 (early-middle layers) [(원문)](https://arxiv.org/abs/2604.22166)
- **2026-04-27**: Dyck 언어 학습 트랜스포머: 어텐션 패턴은 스택 LIFO를 인과적으로 사용하지만 residual stream 신호는 표현만 가능함을 프로빙 및 개입으로 실증 [(원문)](https://arxiv.org/abs/2604.22128)
- **2025-04-24**: 인과적 개입은 자연 분포에서 벗어난 표현(harmless/pernicious divergences) 야기 → 해석 신뢰성 위협 [(원문)](https://arxiv.org/abs/2511.04638)
- **2025-10-15**: 문맥인식 뉴런 마스킹으로 동적·가역적 편향 제거, 배포 후 대화 문맥에 따라 실시간 적응형 조정 가능 [(원문)](https://arxiv.org/abs/2510.18914)
- **2026-04-24**: 미학습 토큰의 unembedding 붕괴가 구별 불가능성 야기, 'active forgetting' 개입으로 완화 [(원문)](https://arxiv.org/abs/2604.21632)
- **2026-04-24**: 추론을 recall과 state-tracking이라는 원시 연산으로 분해 가능 → hybrid 아키텍처 우월성 실증 [(원문)](https://arxiv.org/abs/2604.21454)
- **2026-04-24**: VLM과 LLM의 성능 격차 분석으로 시각 표현의 메커니스틱 한계 파악 가능 [(원문)](https://arxiv.org/abs/2604.21346)
- **2026-04-22**: Functional attribution (influence functions)으로 정상 vs 이상 메커니즘 구분. Parameter-space sampling으로 모델 내부 결합도 측정 [(원문)](https://arxiv.org/abs/2604.18970)
- **2026-04-22**: Harmful intent는 12개 모델(Qwen, Llama, Gemma 계열) residual streams의 선형 방향으로 기하학적 복원 가능. 소프트-AUC 최적화로 AUROC 0.98, TPR@1%FPR 0.80 달성 [(원문)](https://arxiv.org/abs/2604.18901)
- **2026-04-22**: Citation hallucination은 필드별 독립적 신경 회로 사용. 인과 개입으로 특정 뉴런 억제시 할루시네이션 감소 증명하여 신경 수준의 targeted intervention 가능성 제시. [(원문)](https://arxiv.org/abs/2604.18880)
- **2026-04-22**: 64D 임베딩의 유효 차원성 13.3 (참여율), 개념 벡터 84% 회전(60°+ 각도), 국소-전역 정렬 0.17 측정 [(원문)](https://arxiv.org/abs/2604.18715)
- **2025-10-06**: LLM에서 validity와 plausibility가 representational geometry에서 강하게 정렬되어 혼동 발생 [(원문)](https://arxiv.org/abs/2510.06700)
- **2026-04-21**: 기존 LLM 반사실적 생성 방법의 문제점 비판 및 더 간단한 대안 제시 [(원문)](https://arxiv.org/abs/2509.22297)
- **2026-04-21**: 희소 오토인코더(SAE) 기반 특성 공동활성화로 개념(국가, 단어)과 관계(수도, 번역언어) 모듈 추출 가능. 첫 레이어에 개념, 후반 레이어에 추상 관계 집중 [(원문)](https://arxiv.org/abs/2506.18141)
- **2026-04-21**: LLM 해로움 순응: 행동적 패턴 분석만으로는 내부 실패 모드 파악 불가. 안전 평가 방식의 재검토 필요. [(원문)](https://arxiv.org/abs/2604.18510)
- **2026-04-21**: Sparse Autoencoder 피처 트레이스의 commit-open 프로토콜로 호스팅 LLM의 몰래 모델 치환 탐지 (Qwen, Gemma 검증) [(원문)](https://arxiv.org/abs/2604.18179)
- **2026-04-21**: 표현 정렬의 보편성이 아닌 생태적 제약 겹침에서 비롯된다는 Umwelt Representation Hypothesis 제시 [(원문)](https://arxiv.org/abs/2604.17960)
- **2026-04-21**: VLM의 FFN 뉴런을 작업별 어텐션 헤드에 조건화해 인과적 기여도 순위화. HONES 프레임워크로 신경 다중의미성 감소 (arXiv:2604.17941) [(원문)](https://arxiv.org/abs/2604.17941)
- **2026-04-21**: 보안 표현이 초기 레이어에서 인코딩되나 계산 비활성화 → 학습 결함 아닌 구조적 문제임을 입증 [(원문)](https://arxiv.org/abs/2604.16697)
- **2026-04-21**: Amortized visual attribution streaming achieves causal faithfulness comparable to exhaustive perturbation methods while enabling real-time streaming [(원문)](https://arxiv.org/abs/2604.16587)
- **2026-04-21**: surprisal과 인지 노력의 정렬이 층에 따라 역전. 구문적 도전 과제에서 후기 층의 높은 예측력 [(원문)](https://arxiv.org/abs/2604.18563)
- **2026-04-21**: 언어 모델의 활성화가 추론 단계의 중요도를 내재적으로 인코딩하며, 이는 생성 이전부터 존재하고 모델 간 일반화 가능 [(원문)](https://arxiv.org/abs/2604.18307)
- **2026-04-21**: LLM의 중간-후기 레이어들은 추상성을 일관된 1D 방향으로 압축하여, 이를 통해 비유 언어 분류와 훈련-없는 조종 가능 [(원문)](https://arxiv.org/abs/2604.18296)
- **2026-04-21**: GPT-2/Qwen에서 prompt 개입의 고정 인터페이스 상태 전이로 라우팅 재사용 [(원문)](https://arxiv.org/abs/2604.18158)
- **2026-04-21**: Logic-to-Topology 변환으로 latent space의 구조적 불변성 노출 가능. 표층 인코딩 vs. structural understanding 구분 [(원문)](https://arxiv.org/abs/2604.18050)
- **2026-04-21**: BNN 뉴런의 활성화 임계값을 Sugeno integral로 표현하여 if-then 규칙 집합으로 명시적 해석 가능 [(원문)](https://arxiv.org/abs/2604.17967)
- **2026-04-21**: 신경 셀룰러 오토마타(NCA)가 문법 학습 후 자발적으로 CKY 알고리즘과 유사한 Proto-CKY 표현 구성 [(원문)](https://arxiv.org/abs/2604.17857)
- **2026-04-21**: 개별 expert는 polysemantic이지만 expert paths는 의미 함수별로 monosemantic clustering (언어/형식 무관) [(원문)](https://arxiv.org/abs/2604.17837)
- **2026-04-21**: Contrastive LRP-based attribution으로 realistic benchmark의 LLM 실패 패턴 분석 [(원문)](https://arxiv.org/abs/2604.17761)
- **2026-04-21**: Diffusion grokking: flow-matching 확산 모델에서도 지연된 일반화 발생. 반복 샘플링을 산술 계산과 시각 디노이징 페이즈로 분해 가능 [(원문)](https://arxiv.org/abs/2604.17673)
- **2026-04-21**: ATLAS 프레임워크: 모델 숨겨진 상태의 representational geometry를 constitution-conditioned 차트로 분해. Gemma에서 source 행 포착율 97%, score-flip 100% [(원문)](https://arxiv.org/abs/2604.17663)
- **2026-04-21**: Model-native 특성화: human taxonomy 없이 sequence-level activation 기반 orthogonal basis에서 model의 행동 조직화 축 회수 [(원문)](https://arxiv.org/abs/2604.17614)
- **2026-04-21**: Llama, Olmo, Qwen (8B~32B) 모델이 activation에 적용된 dropout/Gaussian noise를 거의 완벽하게 감지·지역화·구분 가능. In-context 학습으로 perturbation 유형도 학습 가능 [(원문)](https://arxiv.org/abs/2604.17465)
- **2026-04-21**: 6개 감정 카테고리와 4개 수사적 장치의 neuron representation mechanism 체계적 조사로 내재 연관성 규명 [(원문)](https://arxiv.org/abs/2604.17255)
- **2026-04-21**: Persona space와 emergent misalignment의 mechanistic 구조 분석으로 LLM individuation 문제 접근 [(원문)](https://arxiv.org/abs/2604.17031)
- **2026-04-21**: Cross-layer transcoder (CLT)에서 Feature Attribution Patching (FAP)로 행동 충실도·해석 품질 측정 (PIE 프레임워크) [(원문)](https://arxiv.org/abs/2604.16889)
- **2026-04-21**: VLM 해석가능성 연구에서 정보 유출 보안 이슈 제기 [(원문)](https://machinelearning.apple.com/research/what-do-your-logits-know)
- **2026-01-26**: VLM의 attention head를 통한 hallucination 메커니즘 분석 및 모델별 차이점 규명 [(원문)](https://arxiv.org/abs/2601.05201)
- **2026-04-20**: 특성 재구성 오류로 uMLIP 모델 간 정보 내용 정량 평가 가능 [(원문)](https://arxiv.org/abs/2512.05717)
- **2026-04-20**: Attention Sinks는 최적화 부작용 아닌 필수 기능: trigger 토큰 조건부 작업에서 필연적 증명 [(원문)](https://arxiv.org/abs/2603.11487)
- **2026-04-20**: Truncation 기반 분석으로 다국어 숨은 추론 형성의 언어별 편차 측정 (자원 풍부 언어에서 강함) [(원문)](https://arxiv.org/abs/2601.02996)
- **2025-02-20**: 화학 반응 메커니즘의 arrow-pushing 형식으로 LLM 해석가능성 강화, CASP 제안 post-hoc 검증 가능 (arXiv:2512.05722) [(원문)](https://arxiv.org/abs/2512.05722)
- **2025-04-20**: 정류된(rectified) 소프트맥스의 주의 패턴 해석 가능성 향상 [(원문)](https://arxiv.org/abs/2504.20966)
- **2026-04-20**: 헤비안 학습을 Wasserstein 최소화 이동으로 모델링하면 내부 메모리 상태와 관찰 가능 시냅스 가중치의 이중 구조 드러남 [(원문)](https://arxiv.org/abs/2604.16052)
- **2026-04-20**: 복잡한 양자 데이터에서 해석 가능한 표현을 학습하고 order parameter로 변환하는 파이프라인으로 물리적 통찰 도출 가능 [(원문)](https://arxiv.org/abs/2604.16015)
- **2026-04-20**: RISE: 출력층 영향 집중도(influence hotspots)를 통한 스케일러블 데이터 기여도 추정 (arXiv:2604.16197) [(원문)](https://arxiv.org/abs/2604.16197)
- **2026-04-20**: 기능적 투명성, 개념 정렬, 표현 분해, 명시적 모듈화, 잠재 희소성 유도 등 내재적 해석 방법 종합 정리 [(원문)](https://arxiv.org/abs/2604.16042)
- **2026-04-20**: 특성 귀인의 엄격한 기호적 방법 필요. 비기호적 도구의 신뢰성 부족 인식 [(원문)](https://arxiv.org/abs/2604.15898)
- **2026-04-20**: 숙련된 LLM은 attention이 입력 정보 전파, MLP가 결과 집계하는 명확한 분업 구조 보유; 미숙한 모델은 이 분업 부재 [(원문)](https://arxiv.org/abs/2604.15842)
- **2026-04-20**: Latent-state trajectory가 LLM reasoning의 primary object일 가능성; surface CoT의 faithfulness 재검토 필요 [(원문)](https://arxiv.org/abs/2604.15726)
- **2026-04-20**: 신경원 활성화 그래프 랭킹(NAG): 타겟 입력의 고영향도 신경원을 compact 그래프로 특성화, 데이터 선택 시 평균 4.9% 성능 개선 [(원문)](https://arxiv.org/abs/2604.15706)
- **2026-04-20**: 모델 규모 증가 시 LLM은 수치 제약과 규칙 식별자 우선순위화 전략 발달 [(원문)](https://arxiv.org/abs/2604.15589)
- **2026-04-20**: 완전 보드 맥락을 CNN 자동인코더로 인코딩하면 개별 기물 기여도 예측 정확도 16% 향상 [(원문)](https://arxiv.org/abs/2604.15585)
- **2026-04-20**: 로짓 렌즈의 선형 접근성으로 계층별 모델 행동 예측 가능 [(원문)](https://arxiv.org/abs/2604.15557)
- **2026-04-20**: Activation patching으로 환각 활성화의 인과 비대칭성 검증: 주입 87.5% 손상율 vs. 역복구 33.3% [(원문)](https://arxiv.org/abs/2604.15400)
- **2026-04-20**: Transformer 내부에서 추론 시 spectral compression 발생 (9/11 모델, p<0.05) [(원문)](https://arxiv.org/abs/2604.15350)
- **2026-03-05**: 스타일 제약(소문자, 단어 회피 등) 준수 시 CoT 제어성 평가 가능 [(원문)](https://www.alignmentforum.org/posts/BuAPifQmHf24xB29n/prompted-cot-early-exit-undermines-the-monitoring-benefits)


## 핵심 주체
[[In-Context Learning]]


## 모순/논쟁

