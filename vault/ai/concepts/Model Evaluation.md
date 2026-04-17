---
type: concept
domain: ai
last_updated: 2026-04-17
source_count: 0
---

# Model Evaluation

## 정의


## 주요 발전
- **2025-12**: Simulator fidelity 정량화: confidence set 기반 sim-to-real gap 평가 (quantile curve) [(원문)](https://arxiv.org/abs/2512.05024)
- **2026-04-17**: E2EDev: BDD 원칙 기반 엔드투엔드 소프트웨어 개발 작업 벤치마크, Behave 프레임워크 자동 평가 파이프라인 [(원문)](https://arxiv.org/abs/2510.14509)
- **2025-06-11**: Kuiper 통계 기반 Multi-calibration 메트릭: 확률 예측이 다중 부분군에서 동시에 보정되는 정도를 신호대잡음비(SNR) 가중치로 측정 [(원문)](https://arxiv.org/abs/2506.11251)
- **2026-04-17**: Feedback metrics: correction lag (feedback→behavior 지연), post-feedback performance (semantic variant queries). [(원문)](https://arxiv.org/abs/2604.06647)
- **2026-04-17**: 메타인지 능력 측정: meta-d' 프레임워크로 AI의 불확실성 자체 평가 능력(신뢰도 판단 정확성) 정량화 [(원문)](https://arxiv.org/abs/2603.29693)
- **2026-04-17**: AIMO 3 Diverse Prompt Mixer 실험: 8점 능력 격차에서 모든 프롬프트 개입 무효, 모델 능력이 지배적 (pass@8 42/50 vs pass@20 ~45.5) [(원문)](https://arxiv.org/abs/2603.27844)
- **2026-04-17**: ReasonScaffold: LLM 설명(예측 레이블 제외) 노출 후 인간 재평가 시 동의도·개정 행동 변화 측정 (Delphi 방식) [(원문)](https://arxiv.org/abs/2603.21094)
- **2026-04-17**: 벤치마크 내 객관적 데이터 42% 참조 중 웰니스 신호 17.7%로 편중, 진단 입력·검사값 부재 [(원문)](https://arxiv.org/abs/2603.18294)
- **2026-04-17**: Instruction-following 평가용 메타-벤치마크 IF-RewardBench 제안 (listwise evaluation paradigm) [(원문)](https://arxiv.org/abs/2603.04738)
- **2026-04-17**: LLM의 수학 추론 능력은 저자원 언어(Sinhala, Tamil)에서 영어 대비 현저히 저하 [(원문)](https://arxiv.org/abs/2602.14517)
- **2026-01-07**: reasoning budget을 deployment-time 하이퍼파라미터로 취급, 환경 제약에 맞춘 cost-accuracy 조절 [(원문)](https://arxiv.org/abs/2601.08310)
- **2026-01-07**: MENT 데이터셋으로 LLM-as-Judge의 knowledge cutoff 및 score inconsistency 문제 체계화 [(원문)](https://arxiv.org/abs/2601.07338)
- **2025-12-13**: Finch: 데이터 입력/구조화/검증/시각화/보고 통합 평가 [(원문)](https://arxiv.org/abs/2512.13168)
- **2025-12-04**: LexGenius 벤치마크: 법률 지능 7차원 11과제 20능력 평가 체계 [(원문)](https://arxiv.org/abs/2512.04578)
- **2026-04-17**: IF-CRITIC: 제약 체크리스트 기반 instruction-following 세밀 평가 및 constraint-level 선호도 최적화 [(원문)](https://arxiv.org/abs/2511.01014)
- **2026-04-17**: Time-RA: 시계열 이상 탐지를 판별식에서 생성식 추론 과제로 재정의, 멀티모달 벤치마크 제시(40K 샘플) [(원문)](https://arxiv.org/abs/2507.15066)
- **2025-06-13**: 확산 모델에서 손실이 0이 아닌 최적값을 가지는 특성을 이용하여, 모델 수용력 부족과 큰 최적 손실을 구분 가능하게 하는 진단 메트릭 제시 [(원문)](https://arxiv.org/abs/2506.13763)
- **2025-05-20**: Soft labels를 이용한 베이즈 오류 추정에서 편향 감소율이 클래스 조건부 분포 분리도에 적응적으로 작동함을 이론적으로 증명. 인스턴스당 하드 라벨 수 증가 시 이전 결과보다 현저히 빠른 수렴 [(원문)](https://arxiv.org/abs/2505.20761)
- **2026-04-17**: 밀집 다중 보상 스킴으로 Vision-Language 모델의 end-to-end 강화학습 가능 [(원문)](https://arxiv.org/abs/2604.14967)
- **2026-04-17**: LLM은 test generation 태스크에서 genuine reasoning보다 shallow heuristics와 memorization에 의존 [(원문)](https://arxiv.org/abs/2604.14437)
- **2026-04-17**: Zero-ablation 메서드가 레지스터 중요성을 과대평가. 대체 제어(평균/노이즈/크로스이미지 셔플)로 실제 의존도 측정 [(원문)](https://arxiv.org/abs/2604.14433)
- **2026-04-14**: 정적 벤치마크의 한계를 넘어 마켓플레이스 시뮬레이션으로 시스템 간 경쟁 효과(early adoption, market dominance) 평가 가능 [(원문)](https://arxiv.org/abs/2604.14256)
- **2026-04-17**: FRESCO 벤치마크: Wikipedia 버전 기록으로 시간 경과에 따른 정보 변화 시뮬레이션. 재순위 모델이 최신 정보와 의미 연관성 충돌에서 일관된 실패 모드 노출 [(원문)](https://arxiv.org/abs/2604.14227)
- **2026-04-17**: PolyBench: 4997개 이벤트, 38,666개 이진 시장에서 7개 LLM을 방향성 정확도, CWR, APY, Sharpe ratio로 평가 (2026-02-06~12) [(원문)](https://arxiv.org/abs/2604.14199)
- **2026-04-17**: QFT/String Theory에서 명시적 정확성, 핵심 개념, 추론 연쇄, 암묵적 단계, 심화도를 분리한 5단계 평가 척도 개발 [(원문)](https://arxiv.org/abs/2604.14188)
- **2026-04-17**: LLM 판사의 신뢰성 진단: conformal prediction sets를 이용해 예측 구간 생성, 폭이 문서별 어려움을 포착 (Spearman rho=+0.576) [(원문)](https://arxiv.org/abs/2604.15302)
- **2026-04-17**: LLM judge는 평가 대상의 의미가 아닌 '평가 결과의 downstream 영향' 신호에 의존해 판정 왜곡 (18,240개 통제 실험) [(원문)](https://arxiv.org/abs/2604.15224)
- **2026-04-17**: 20+ 모델(인코더/디코더)의 fine-tuning·few-shot 성능을 엄격한 시간 분리로 평가 [(원문)](https://arxiv.org/abs/2604.15203)
- **2026-04-17**: 단일층 Mamba(MambaSL)가 30개 UEA 시계열 분류 데이터셋에서 유의한 SOTA 성능 달성 [(원문)](https://arxiv.org/abs/2604.15174)
- **2026-04-17**: Backtrader 프레임워크용 알고리즘 거래 전략 코드 생성 벤치마크 [(원문)](https://arxiv.org/abs/2604.15151)
- **2026-04-17**: 얼굴 인식 같은 고위험 시스템 평가 시 다중 공정성 메트릭의 동시 검토 필수 (단수 메트릭 의존 위험) [(원문)](https://arxiv.org/abs/2604.15038)
- **2026-04-17**: ProVoice-Bench: 1,182개 샘플로 프로액티브 음성 에이전트의 상황 인식(context-aware) 성능 한계 발견 [(원문)](https://arxiv.org/abs/2604.15037)
- **2026-04-17**: XQ-MEval: 9개 언어 쌍 parallel quality 벤치마크로 번역 메트릭의 cross-lingual bias 문제 체계적 평가 [(원문)](https://arxiv.org/abs/2604.14934)
- **2026-04-17**: 의료 진단 정확도, 감별진단, 임상추론, 치료위험 4개 차원별로 LLM vs 전문가 평가 비교 [(원문)](https://arxiv.org/abs/2604.14892)
- **2026-04-17**: Foundation model 최적 표현 추출 레이어가 task(trajectory vs perturbation)와 cellular context에 따라 다름. 최종 레이어 고정 가정 도전. [(원문)](https://arxiv.org/abs/2604.14838)
- **2026-04-17**: Multimodal 시스템의 답변 거부 메트릭: visual modality dependency 및 evidence sufficiency 축 [(원문)](https://arxiv.org/abs/2604.14799)
- **2026-04-17**: 1,985 사용자 프로필 기반 개인화 QA 벤치마크 CoPA, 6가지 인지 요인으로 세밀한 평가 제공 [(원문)](https://arxiv.org/abs/2604.14773)
- **2026-04-17**: Transformer 표현력의 tight asymptotic bounds: 시퀀스 길이, 임베딩 차원, 깊이의 조합으로 지수적 복잡도 증가 증명 [(원문)](https://arxiv.org/abs/2604.14727)
- **2026-04-17**: LLM 에이전트의 하드웨어 버그 수정 벤치마크 417개 인스턴스 (Verilog/Chisel, RISC-V 코어, SoC) [(원문)](https://arxiv.org/abs/2604.14709)
- **2026-04-17**: 정보 회상, 인용 정확도, 지시 준수도, 깊이 품질 5차원 평가 프레임워크 [(원문)](https://arxiv.org/abs/2604.14683)
- **2026-04-17**: 임상 LM의 캘리브레이션 평가를 위한 개별-집단 이중 목적 함수 [(원문)](https://arxiv.org/abs/2604.14651)
- **2026-04-17**: Text2Space 데이터셋으로 공간 표현 구성 능력과 추론 능력 분리 평가 가능 [(원문)](https://arxiv.org/abs/2604.14641)
- **2026-04-17**: 다지선다 옵션을 100개로 확장한 robust 평가 프로토콜, 저옵션 설정의 과평가 현상 적발 [(원문)](https://arxiv.org/abs/2604.14634)
- **2026-04-17**: StoryCoder: 태스크 개요-제약-테스트 케이스 narrative 구조화로 일관적 성능 개선 [(원문)](https://arxiv.org/abs/2604.14631)
- **2026-04-17**: 생성 AI 출력과 인간 라벨의 복잡한 관계를 비모수적으로 모델링하는 GAI 프레임워크 [(원문)](https://arxiv.org/abs/2604.14575)
- **2026-04-17**: 추론 실패는 균등 분포 아님. 초기 수 토큰에서 국소 오류 후 국소적으로는 일관되나 전체적으로 틀림. 여러 벤치마크에서 성능 향상 검증 [(원문)](https://arxiv.org/abs/2604.14528)
- **2026-04-17**: 390개 멀티 쿼리 인스턴스 벤치마크. Case Satisfiability Rate, Contradiction Density, Revision Cost 지표. 반례 기반 수정으로 성능 향상 [(원문)](https://arxiv.org/abs/2604.14525)
- **2026-04-17**: MARCA: 웹 검색 기반 정보 추구 평가를 위한 영어/포르투갈어 이중언어 벤치마크 (52문항) [(원문)](https://arxiv.org/abs/2604.14448)
- **2026-04-17**: 다중 턴 LLM 대화 분석에서 연속 턴의 비독립성 무시로 표준 검정 결과의 42%가 spurious (cluster-robust correction 미적용 시) [(원문)](https://arxiv.org/abs/2604.14414)
- **2026-04-17**: Path-Sampled Integrated Gradients: 특성 귀속 분산 1/3 감소, 수렴 속도 O(m^-1) [(원문)](https://arxiv.org/abs/2604.14338)
- **2026-04-17**: GPT-4.1 기반 경험도 예측: 약 10k MLB 팬 응답에서 67% 정확도(±1 포인트), 36% 정확 일치. 반복 평가 간 87% 정확 일치로 결정적 성능 입증 [(원문)](https://arxiv.org/abs/2604.14321)
- **2026-04-17**: Zero-shot, 엄격한 제약 프롬프팅으로 LLM의 언어간 전이 능력과 시각 추론 능력을 평가하는 새로운 벤치마크 [(원문)](https://arxiv.org/abs/2604.14306)
- **2026-04-17**: 최대 엔트로피 추정으로 FDIC Call Reports 재구성, 14년×58분기 동적 가중 방향 그래프로 평가 [(원문)](https://arxiv.org/abs/2604.14232)
- **2026-04-17**: Fun-TSG: 다변량 시계열 이상 탐지 자동 생성/평가 도구, 함수 기반 의존성 구조 지원 [(원문)](https://arxiv.org/abs/2604.14221)
- **2026-04-14**: 네팔어 적응 평가: PPL, BERTScore, chrF++, ROUGE, BLEU로 유창성/음성 일관성/의미 무결성 측정 [(원문)](https://arxiv.org/abs/2604.14171)
- **2026-04-17**: ICLR 2021-2025 논문 30,000+건 분석: 수용 예측 시 점수 기반 91% vs 텍스트 기반 81% 정확도. 개별 낮은 점수가 평균 부근에서도 거부 결정 주도 [(원문)](https://arxiv.org/abs/2604.14162)
- **2026-04-17**: 6개 SOTA LLM이 주제 수준 데이터 누수 등 방법론적 결함을 일관되게 독립 식별 가능 [(원문)](https://arxiv.org/abs/2604.14161)
- **2026-04-17**: 게임화 상호작용 시나리오에서 메모리 활용도와 행동 궤적을 다차원으로 평가하는 메트릭 스위트 [(원문)](https://arxiv.org/abs/2604.14158)


## 핵심 주체
[[Agentic AI]]


## 모순/논쟁

