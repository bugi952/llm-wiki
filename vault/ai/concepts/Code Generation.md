---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Code Generation

## 정의


## 주요 발전
- **2026-01-12**: dLLM은 JSON schema 등 strict 형식 준수 실패 → tool-calling 에이전트 부적합 [(원문)](https://arxiv.org/abs/2601.12979)
- **2025-11-22**: TreeCoder: 트리 탐색으로 디코딩 전략과 제약 함수를 일급 최적화 대상으로 처리 [(원문)](https://arxiv.org/abs/2511.22277)
- **2026-04-22**: NL2VC-60 데이터셋: 60개 복잡 알고리즘 문제. Dafny 형식 검증으로 LLM 코드 정확성 강제 [(원문)](https://arxiv.org/abs/2604.22601)
- **2026-04-22**: LLM 기반 코드 생성 결과의 보안/윤리 해로움을 사전에 테스트하는 ethics testing 프레임워크 [(원문)](https://arxiv.org/abs/2604.22089)
- **2026-04-21**: 1-3B 모델의 실행 피드백 기반 자정제로 HumanEval/MBPP에서 4σ 이상 성능 향상 (NameError, SyntaxError는 90% 수정, 로직 오류는 제한적) [(원문)](https://arxiv.org/abs/2604.21950)
- **2026-04-24**: Karpathy 강의 기반 인터랙티브 가이드로 LLM의 token 생성 메커니즘 시각화 [(원문)](https://news.ycombinator.com/item?id=47886517)
- **2026-04-24**: 진화 궤적을 단계별 감독신호로 변환하여 에이전트를 강력한 지역 개선자로 훈련 [(원문)](https://arxiv.org/abs/2603.28342)
- **2025-05-01**: 학술논문 개정은 구조화된 텍스트 변환 작업으로 code generation과 동일 패러다임 적용 가능. 섹션별 개정 140K 명령 쌍 데이터셋 [(원문)](https://arxiv.org/abs/2505.11336)
- **2026-04-24**: 공개 테스트 케이스 의존성으로 인한 과신(overconfidence gap) 문제 - 숨겨진 테스트에서 성능 저하 [(원문)](https://arxiv.org/abs/2604.21598)
- **2026-04-24**: Semantic-preserving 변환으로 variant 벤치마크 생성, 성능 저하로 memorization 측정 [(원문)](https://arxiv.org/abs/2604.21579)
- **2026-04-24**: Code structure/security patterns/debugging logic 3개 관점 병렬 분석으로 종합적 취약점 탐지 [(원문)](https://arxiv.org/abs/2604.21282)
- **2026-04-24**: 데이터셋 프로필 + 다운스트림 코드 분석으로 태스크 인식형 자동 단위 테스트 생성 및 선택적 피드백 최적화 (PrismaDV, SIFTA) [(원문)](https://arxiv.org/abs/2604.21765)
- **2026-04-24**: ML 파이프라인 자동 생성에서 민감 속성(race 등)이 87.7% 포함되는 편향, if-statement 테스트(59.2%)에서는 드러나지 않음 [(원문)](https://arxiv.org/abs/2604.21716)
- **2026-04-24**: SemEval-2026 Task 13: 다중 언어 기계생성 코드 탐지 + (1)생성 LLM 계열 (2)하이브리드 인간-기계 코드 (3)적대 수정 코드 분류 [(원문)](https://arxiv.org/abs/2604.21365)
- **2026-04-24**: PLOTTER: 이벤트/캐릭터 그래프 토폴로지 분석으로 네러티브 인과성과 구조적 일관성 개선 [(원문)](https://arxiv.org/abs/2604.21253)
- **2026-04-24**: DexBench: 예측(주어진 입력에 대한 behavior) + 추론(특정 objective를 위한 입력 변이) dual task로 실행 흐름 causal understanding 평가 [(원문)](https://arxiv.org/abs/2604.20917)
- **2026-04-24**: GPT-5.5로 복잡한 코드 생성 및 분석 능력 향상 [(원문)](https://openai.com/index/introducing-gpt-5-5)
- **2026-04-22**: Materials science, communication engineering, bioengineering 도메인의 fine-tuning-free 코드 생성 [(원문)](https://arxiv.org/abs/2604.19022)
- **2026-04-18**: PRIME 벤치마크(156개 대학원 수준 정리)로 formal proof 자동생성 성능 평가 [(원문)](https://arxiv.org/abs/2604.19000)
- **2025-10-17**: xKG는 과학 논문에서 추출한 코드 스니펫으로 RAG 기반 생성 성능 10.9% 향상 (o3-mini) [(원문)](https://arxiv.org/abs/2510.17795)
- **2025-10-12**: ContractEval: 364개 작업의 계약 검증 벤치마크 (HumanEval+, MBPP+ 기반) [(원문)](https://arxiv.org/abs/2510.12047)
- **2025-09-01**: RefineStat: LLM 확률적 프로그램 생성에서 semantic constraint와 diagnostic refinement로 에러 감소 (2025-09 arXiv) [(원문)](https://arxiv.org/abs/2509.01082)
- **2026-04-21**: Writing-RL: 수학/코드 도메인의 RLVR 방법론을 open-ended writing에 확장, margin-aware selection과 pairwise comparison reward 도입 (2026-04-21) [(원문)](https://arxiv.org/abs/2506.05760)
- **2025-05-16**: Fragment composition 패턴: 기존 코드/텍스트 재조합 방식으로 창의성과 grounding 동시 달성 가능성 [(원문)](https://arxiv.org/abs/2505.18128)
- **2026-04-21**: WebCompass: 15개 도메인, 16개 편집 연산, 11개 결함 유형의 multimodal 벤치마크 (text/image/video) [(원문)](https://arxiv.org/abs/2604.18224)
- **2026-04-21**: 병렬 학습 데이터 없이 강화학습 기반 자기지도로 저자원 프로그래밍 언어 간 코드 변환 부트스트래핑 가능 [(원문)](https://arxiv.org/abs/2604.18027)
- **2026-04-21**: Code LLM 시크릿 유출의 근본: BPE 토큰 분포 편향이 학습 데이터와 시크릿 데이터 간 차이 유발, 높은 token-level entropy의 시크릿이 선택적으로 암기됨 [(원문)](https://arxiv.org/abs/2604.17814)
- **2026-04-21**: 사전 보안 교육이 신원 중심 Java Spring Boot 구현의 유효 약점 감소에 유의미한 효과 (12명 개발자 준실험) [(원문)](https://arxiv.org/abs/2604.17763)
- **2026-04-21**: AI 생성 코드는 기능성을 유지하면서 내부 검사/오류 처리를 손상시키는 '조용한 실패' 패턴. 인간 피드백 최적화(RLHF)의 reward shaping 부작용으로 추정 (arXiv:2604.17587) [(원문)](https://arxiv.org/abs/2604.17587)
- **2026-04-21**: Precise Debugging Benchmark (PDB): 디버깅과 재생성 구분, edit-level precision과 bug-level recall 메트릭. 최신 모델 76% 이상 통과도 precision 45% 이하 [(원문)](https://arxiv.org/abs/2604.17338)
- **2026-04-21**: 컴파일러 피드백을 기호적 보상으로 활용하여 복잡한 의존성 문제 해결 [(원문)](https://arxiv.org/abs/2604.17184)
- **2026-04-21**: best-of-N sampling/multi-candidate code completion에서 공유 prefix KV cache와 MoE 라우팅의 높은 overlap으로 cache 재사용 및 배치 효율 최적화 기회 발굴 [(원문)](https://arxiv.org/abs/2604.17182)
- **2026-04-21**: LLM이 보안 취약점을 '알지만' 코드로 생성하는 Format-Reliability Gap 발견; per-vulnerability steering으로 최대 74% 감소 [(원문)](https://arxiv.org/abs/2604.16697)
- **2026-04-21**: Certified synthesis generates aligned program-specification-proof triples; vericoding combines NL→code with formal verification seamlessly [(원문)](https://arxiv.org/abs/2604.16584)
- **2026-04-21**: Agentic coding의 parallel/sequential scaling: trajectory 요약을 통한 inference-time optimization [(원문)](https://arxiv.org/abs/2604.16529)
- **2026-04-21**: AST 레벨에서 먼저 구조적 진화(교차, 돌연변이) 수행 후 LLM이 무효 코드 수리하는 2단계 방식으로 알고리즘 탐색 공간 확대 [(원문)](https://arxiv.org/abs/2604.16420)
- **2026-04-21**: AI 생성 앱의 10.3%가 critical security 결함 보유 [(원문)](https://arxiv.org/abs/2604.16399)
- **2026-04-21**: IFCodeEvolve - parametric function schema 기반 instruction-paired coding data 자동 생성. MCTS sampler로 constraint space를 동적으로 탐색, actor-schema co-evolution으로 challenging problems 점진 도입. [(원문)](https://arxiv.org/abs/2604.16322)
- **2026-04-21**: GPT-5.2는 CRUXEval 원본에서 99% 정확도이나 code perturbations에서 20-24% 정확도 하락. DeepSeek-R1(38-67%)은 상대적으로 안정적이나 여전히 낮음. [(원문)](https://arxiv.org/abs/2604.16320)
- **2026-04-21**: ManimTrainer: SFT + GRPO 조합으로 프로그래매틱 애니메이션 생성 능력 개선 (arXiv:2604.18364v1) [(원문)](https://arxiv.org/abs/2604.18364)
- **2026-04-21**: LLM의 높은 소스 이해도가 창의적 생성(번역)으로 이어지지 않음 [(원문)](https://arxiv.org/abs/2604.18169)
- **2026-04-21**: Stratagem: 게임 자가학습으로 추론 이전성 강화, 수학·일반·코드 생성 벤치마크에서 추상적 패턴 추출 검증 [(원문)](https://arxiv.org/abs/2604.17696)
- **2026-04-21**: EggMind: LLM이 equality saturation 최적화 전략을 자동 합성, manual strategy design 자동화 [(원문)](https://arxiv.org/abs/2604.17364)
- **2026-04-21**: Probabilistic Programs of Thought: 프로그램 확률 분포를 명시적으로 모델링하여 n개 샘플 생성을 n번 LLM 호출 없이 수행 [(원문)](https://arxiv.org/abs/2604.17290)
- **2026-04-20**: OpInstruct-HSx: 28K validated Haskell programs dataset으로 semantic equivalence 학습 [(원문)](https://arxiv.org/abs/2604.17010)
- **2026-04-21**: Test-time scaling 하에서 reasoning trace의 구조적 특성이 코딩 성능 예측의 핵심 신호. 임의 난이도의 코딩 작업 자동 생성 프레임워크로 systematic study 수행 [(원문)](https://arxiv.org/abs/2604.16931)
- **2026-04-21**: 8B LLM이 RL reward로 학습하여 6개 OR 벤치마크에서 frontier 모델 대비 경쟁력 있는 성능 달성 [(원문)](https://arxiv.org/abs/2604.16804)
- **2026-04-21**: LLM 에이전트가 failure-driven adaptation + diversity-preserving search로 최적 커널 코드 탐색 [(원문)](https://arxiv.org/abs/2604.16625)
- **2026-04-21**: NAS 문맥에서 LLM은 복잡한 아키텍처 코드 직접 생성보다 **기존 코드 단위의 tree 변환**에 활용하여 신뢰성과 유효성 확보 [(원문)](https://arxiv.org/abs/2604.16555)
- **2026-04-21**: GoCoMA: 코드 스타일로메트리 + 바이너리 아티팩트 다중모달 분석으로 LLM 코드 소속 판별 [(원문)](https://arxiv.org/abs/2604.16377)
- **2025-03-02**: 양자 프로그래밍 특화 고품질 데이터셋과 자동 큐레이션 프레임워크로 LLM 코드 생성 정확도 향상 [(원문)](https://arxiv.org/abs/2503.02497)
- **2026-04-20**: Neural Computers: I/O trace에서 컴퓨터 primitive 학습 가능. Code execution capability 보유 (arXiv:2604.06425) [(원문)](https://arxiv.org/abs/2604.06425)
- **2026-01-07**: 도메인 특화 언어(NPU DSL) 커널 생성은 LLM의 새로운 응용 영역 [(원문)](https://arxiv.org/abs/2601.07160)
- **2025-12**: 하드웨어 로직 설계 자동화(2D NoC 라우터 1500-2000줄)에서 역변환으로 정합성 검증 가능 [(원문)](https://arxiv.org/abs/2512.03053)
- **2025-08-06**: 음성학, 형태론, 통사론, 어휘 생성의 모듈화된 LLM 파이프라인으로 구성언어 자동 생성 (ConlangCrafter) [(원문)](https://arxiv.org/abs/2508.06094)
- **2026-04-20**: 학자의 출판 자료 분석(8단계 추출, 9모듈 구조)으로 학문적 추론 시스템을 LLM 추론 제약으로 변환. 박사 지도, 심사, 강의 자동화 검증 [(원문)](https://arxiv.org/abs/2604.16116)
- **2026-04-20**: 기존 코드 지역화 모델들이 키워드 숨김 벤치마크(KA-LogicQuery)에서 성능 급락(Keyword Shortcut bias), 진정한 구조적 추론 능력 부족 노출 [(원문)](https://arxiv.org/abs/2604.16021)
- **2026-04-20**: Isabelle 정식 증명에서 LLM 에이전트가 인간 힌트를 통해 증명을 자동 형식화 및 일반화 [(원문)](https://arxiv.org/abs/2604.15713)
- **2026-04-20**: 멀티모달 코드 검색 (CodeMMR) - 자연어, 코드, 이미지 통합 임베딩 [(원문)](https://arxiv.org/abs/2604.15663)
- **2026-04-20**: 하드웨어 설계 언어(RTL) 생성 시 기능성과 PPA 동시 최적화 [(원문)](https://arxiv.org/abs/2604.15642)
- **2026-04-20**: AI 에이전트 등장으로 단순 코드 생성 → 엔드-투-엔드 소프트웨어 엔지니어링 자동화로 진화 [(원문)](https://arxiv.org/abs/2604.15468)
- **2026-04-20**: CoT 프롬프트가 일반 프롬프트 대비 제어 흐름 복구 능력을 유의미하게 향상 (2026-04-20) [(원문)](https://arxiv.org/abs/2604.15390)
- **2026-04-20**: LLM 기반 Verilog 생성: multi-agent 테스트벤치 자동화로 데이터 효율성 향상, VerilogEval v2 벤치마크 SOTA 달성 (2026-04-20) [(원문)](https://arxiv.org/abs/2604.15388)
- **2026-04-20**: LLM 생성 Verilog RTL의 CWE-1244/1245 검출에 임베딩 기반 분류 89% 정밀도, 라인 단위 버그 96% 정확도 [(원문)](https://arxiv.org/abs/2604.15375)
- **2026-04-20**: 자연어 학습 목표·MR 양식 설명으로부터 모바일 기기용 MR 활동 코드 자동 생성 [(원문)](https://arxiv.org/abs/2604.15341)
- **2026-04**: 분자 설계 작업(molecular property prediction, representation transformation, design)에서 LLM RL 포스트트레이닝이 성능 대폭 향상 [(원문)](https://arxiv.org/abs/2604.16279)
- **2026-04-20**: LLM이 훈련 없이 해석 가능한 코드 자동 생성. 신경망 대신 인간이 읽을 수 있는 알고리즘 [(원문)](https://arxiv.org/abs/2604.15787)
- **2026-04-20**: NL2SQL에서 임상의 편집 피드백을 exemplar 데이터셋에 추가, 사용할수록 성능 개선되는 피드백 기반 진화 [(원문)](https://arxiv.org/abs/2604.15646)
- **2026-04-20**: Functional Majority Voting: 함수 합의 기반 다수결로 test-time inference 성능 향상, Label-free TTRL 확장 [(원문)](https://arxiv.org/abs/2604.15618)
- **2026-04-20**: 다언어 코드스위칭 fine-tuning으로 추론 성능 향상 가능 [(원문)](https://arxiv.org/abs/2604.15490)
- **2026-04-19**: QuantCode-Bench: 알고리즘 거래 전략 생성 평가 (400개 작업, 다단계 검증) [(원문)](https://arxiv.org/abs/2604.15151v1)


## 핵심 주체
[[Agentic AI]] | [[Diffusion Models]] | [[Embodied Agents]] | [[Tool Hallucination]]


## 모순/논쟁

