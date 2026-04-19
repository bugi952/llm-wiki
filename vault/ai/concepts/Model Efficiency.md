---
type: concept
domain: ai
last_updated: 2026-04-19
source_count: 0
---

# Model Efficiency

## 정의


## 주요 발전
- **2026-04-14**: Parcae: 루프형 트랜스포머로 동일 데이터·연산에서 기존 모델 능가 [(원문)](https://www.aitimes.com/news/articleView.html?idxno=209435)
- **2026-04-19**: Post-training INT4 양자화에서 FP32 수렴 후 갑작스러운 성능 붕괴 발견 (INT4 gap 11% → 517%, Pythia-160m 154개 체크포인트 분석) [(원문)](https://arxiv.org/abs/2604.15167v1)
- **2026-04-19**: 8개 시각 벤치마크에서 pruning 방법·VLM 아키텍처 간 일반화 가능한 최적 설정 도출 [(원문)](https://arxiv.org/abs/2604.15188v1)
- **2026-04-19**: e-graph 재작성과 기호 추론으로 하드웨어 제약 하에서 증명된 부최적 영역 제거 [(원문)](https://arxiv.org/abs/2604.15272v1)
- **2026-04-19**: 표형 데이터 DL에서 Muon 최적화기가 AdamW 대비 일관되게 우수한 성능을 보이며, 모델 가중치의 지수 이동 평균(EMA)이 추가 개선 효과 [(원문)](https://arxiv.org/abs/2604.15297v1)
- **2026-04-16**: MoE 구조로 연산량 77% 절감하면서 성능 향상 달성 (Qwen 3.5 대비) [(원문)](https://www.aitimes.com/news/articleView.html?idxno=209406)
- **2026-04-17**: 베이지안 최적화 + 가우시안 프로세스로 전자 구조 계산 약 10배 가속화 가능 (정확도 유지) [(원문)](https://arxiv.org/abs/2603.10992)
- **2026-01-01**: KV 캐시 재사용으로 스트리밍 비디오 GPU 메모리 오버헤드 감소 [(원문)](https://arxiv.org/abs/2601.14724)
- **2025-12**: Few-Shot Architecture Prompting: n=3 support examples에서 vision task architecture 다양성과 정확도 최적 [(원문)](https://arxiv.org/abs/2512.24120)
- **2026-04-17**: ProRank: RL 기반 프롬프트 학습과 세분화 점수 학습으로 SLM 리랭킹 성능 향상, 대규모 LLM 대비 계산 효율화 [(원문)](https://arxiv.org/abs/2506.03487)
- **2026-04-17**: LWD는 구조 수정 없이 추론 비용 추가 없이 기존 디퓨전 모델의 고해상도 성능 확장 가능 [(원문)](https://arxiv.org/abs/2506.00433)
- **2026-04-17**: SAGE optimizer: AdamW의 메모리 오버헤드를 Lion 스타일 업데이트와 O(d) 적응형 스케일로 해결 [(원문)](https://arxiv.org/abs/2604.07663)
- **2026-04-17**: AgentOpt: client-side model selection & API budget management for agentic workloads. [(원문)](https://arxiv.org/abs/2604.06296)
- **2026-04-17**: 콘텐츠 기반 라우팅의 역설: 높은 정밀도(99.5%)는 이분 맥락 + 쌍 토큰 비교로만 달성 가능. 회피 시도(메모리뱅크, 대조 학습 등)는 모두 1-29% 실패 [(원문)](https://arxiv.org/abs/2603.20997)
- **2026-02-22**: DYSCO: retrieval heads로 생성 단계별 관련 토큰 재가중, fine-tuning 불필요 [(원문)](https://arxiv.org/abs/2602.22175)
- **2026-04-17**: Dense neural networks는 무제한 가중치 조건에서만 universal approximator (자연스러운 제약 하에선 불가능) [(원문)](https://arxiv.org/abs/2602.07618)
- **2026-04-17**: Large models의 prefill(context encoding) stage에서 deep layers가 decode(next-token prediction) 대비 덜 중요하므로 stage-aware pruning으로 accuracy 유지하며 효율화 가능 [(원문)](https://arxiv.org/abs/2602.03295)
- **2026-04-17**: Iterative margin loss 기반 contrastive training으로 compact multimodal representation 학습, storage overhead 극소화 [(원문)](https://arxiv.org/abs/2601.21262)
- **2026-01-14**: LLMOrbit: 스케일링 벽 돌파 패러다임 6가지 — (1)test-time compute(o1/DeepSeek-R1), (2)architecture innovation, (3)training optimization, (4)data efficiency, (5)hardware advances, (6)reasoning methods [(원문)](https://arxiv.org/abs/2601.14053)
- **2026-01-07**: ASL: attention score 기반 token rank 분산으로 pruning 레이어를 동적 선택, 성능 저하 최소화 [(원문)](https://arxiv.org/abs/2601.07667)
- **2026-01-01**: 언어 학습 작업(L2T)을 텍스트 다음 토큰 예측과 혼합 학습. 언어 능력 벤치마크 성능 향상 및 습득 가속 [(원문)](https://arxiv.org/abs/2601.03448)
- **2025-12-14**: Cornfigurator: 처리량-지연 trade-off로 goodput 극대화 [(원문)](https://arxiv.org/abs/2512.14098)
- **2026-04-17**: GEMS: Human simulation (설문/시험)에서 GNN이 LLM 동등 성능 + 3자리 수 파라미터 절감 [(원문)](https://arxiv.org/abs/2511.02135)
- **2025-10-25**: Balanced Forman Curvature 기반 그래프 액티브 러닝으로 라벨 부족 환경에서 효율성 향상 [(원문)](https://arxiv.org/abs/2510.25892)
- **2026-04-17**: 병렬 Chain-of-Thought 추론에서 답이 동일한 트레이스 80% 이상, DeepPrune으로 동적 중복 제거하여 계산 효율성 극대화 [(원문)](https://arxiv.org/abs/2510.08483)
- **2026-04-17**: Chunked prefill 기반 MoE 추론에서 메모리 트래픽 39% 증가, 레이어 기반 스케줄링(Layered Prefill)으로 개선 [(원문)](https://arxiv.org/abs/2510.08055)
- **2026-04-17**: 온라인 알고리즘 설계: LLM 기반 생성이 기존 휴리스틱의 한계 극복 [(원문)](https://arxiv.org/abs/2510.03851)
- **2026-04-17**: MoE 추론: PreScope로 141% 처리량 향상, 74.6% PCIe 지연 감소 [(원문)](https://arxiv.org/abs/2509.23638)
- **2025-09**: SRA: 코사인 유사도 기반 MoE 라우팅으로 sparse activation 유지하면서 라우팅 결정의 직접 해석가능성 확보 [(원문)](https://arxiv.org/abs/2509.14255)
- **2026-04-17**: SPaCe 프레임워크: 의미론적 클러스터링과 다중 암드 밴딧으로 훈련 데이터 할당 최적화 [(원문)](https://arxiv.org/abs/2508.05015)
- **2025-03-01**: 2025-03: Logo-LLM - 사전훈련 LLM의 다층 계층 활용으로 시계열 지역-전역 패턴 동시 모델링 (얕은층→지역, 깊은층→전역) [(원문)](https://arxiv.org/abs/2505.11017)
- **2026-04-17**: 커널 신경 연산자(KNO)는 불규칙 기하학과 고차원 데이터에서 메모리 효율 및 수렴성 제공 (arXiv:2407.00809) [(원문)](https://arxiv.org/abs/2407.00809)
- **2026-04-17**: DA-Cramming: 의존성 계약을 사전학습에 통합하여 GPU 1대로 BERT 수준 모델 하루 내 학습 가능 (arXiv:2311.04799) [(원문)](https://arxiv.org/abs/2311.04799)
- **2026-04-17**: 양자 ML의 가중합 계산 효율성: 개별 샘플링 O(N||α||²/ε²) vs. QAE 기반 최적화 경로 [(원문)](https://arxiv.org/abs/2604.15214)
- **2026-04-17**: 그리드 서치 대비 경사 기반 탐색으로 VLM 성능-연산 최적 구성 검색 [(원문)](https://arxiv.org/abs/2604.15188)
- **2026-04-17**: 확산 모델에서 FP 정규화 오버헤드 대비 효율적인 경량 페널티 항 분석 [(원문)](https://arxiv.org/abs/2604.15171)
- **2026-04-17**: 단 85개 뉴런(5000 세포 중 1.7%)으로 MNIST 90% 달성 (단일 에포크) [(원문)](https://arxiv.org/abs/2604.15143)
- **2026-04-15**: Atropos: GCN으로 추론 경로의 성공 확률 예측 후 조기 종료. SLM 에이전트의 비용-성능 최적화. [(원문)](https://arxiv.org/abs/2604.15075)
- **2026-04-15**: Cost-aware 라우팅 시스템의 보안 취약점: 적대적 쿼리로 고비용 모델 선택 강제 가능. [(원문)](https://arxiv.org/abs/2604.15022)
- **2026-04-17**: NAS 기반 의료 모델 경량화 연구 진행 [(원문)](https://arxiv.org/abs/2604.14849)
- **2026-04-17**: Nautilus: 자동 스케줄링으로 복잡한 GPU 커널 최적화 완전 자동화 [(원문)](https://arxiv.org/abs/2604.14825)
- **2026-04-17**: Vision SSM을 spectral domain에서 처리하여 O(L log L) 복잡도 달성 (HAMSA) [(원문)](https://arxiv.org/abs/2604.14724)
- **2026-04-17**: Rate-Distortion-Perception 프레임워크로 압축과 인식 품질의 거래 관계 분석 [(원문)](https://arxiv.org/abs/2604.14603)
- **2026-04-17**: 적응형 시각 추론(AVR): 추론 경로 중복 제거. 시각 인식/논리 추론/답변 적용 3단계로 분해하고 Full/Perception-Only/Direct Answer 중 동적 선택 [(원문)](https://arxiv.org/abs/2604.14568)
- **2026-04-17**: DPO를 OCR에 첫 적용한 소형 언어 모델로 transcription 품질·생성 안정성·inference cost 동시 최적화 [(원문)](https://arxiv.org/abs/2604.14314)
- **2026-04-17**: HARNESS: 아랍어-영어 이중언어 교사에서 학생 모델로 점진적 증류 통해 경량화 및 성능 유지 [(원문)](https://arxiv.org/abs/2604.14186)
- **2026-04-17**: 표형 데이터 MLP 학습에서 Muon 옵티마이저가 AdamW를 일관되게 초과 성능. 가중치 EMA(지수 이동평균)가 AdamW 개선 기법으로 확인 [(원문)](https://arxiv.org/abs/2604.15297)
- **2026-04-17**: SpecGuard: Attention grounding + log-probability로 speculative decoding의 스텝 검증 정확도 향상 [(원문)](https://arxiv.org/abs/2604.15244)
- **2026-04-17**: 미분 가능한 희소 어텐션으로 당 단계(per-step) 훈련 시간 개선, softmax 대비 입력 의존형 희소성 유지 [(원문)](https://arxiv.org/abs/2604.15180)
- **2026-04-17**: 양자화 붕괴: FP32 수렴 후에도 가중치 업데이트로 INT4 성능 급격히 악화 (11%→517% INT4 갭) [(원문)](https://arxiv.org/abs/2604.15167)
- **2026-04-17**: K-Token Merging으로 토큰 75% 압축 가능, Pareto-optimal 성능 [(원문)](https://arxiv.org/abs/2604.15153)
- **2026-04-17**: GNN의 O(n³) 복잡도 문제를 truncated Neumann series와 mass compensation으로 해결 (DsmNet, arXiv:2604.15069) [(원문)](https://arxiv.org/abs/2604.15069)
- **2026-04-17**: DLink: layer-wise 지식 증류로 EEG FM을 임베디드 BCI 시스템에 배포 가능 (MiC 파이프라인) [(원문)](https://arxiv.org/abs/2604.15016)
- **2026-04-17**: Mixture-of-Experts flow matching으로 3 스텝 샘플링에서 자동회귀 모델 수준 품질 달성, 추론 40배 고속화 [(원문)](https://arxiv.org/abs/2604.15009)
- **2026-04-17**: AC/DC: 모델 머징과 합성 데이터로 더 큰 모델보다 적은 메모리에서 우수한 성능 [(원문)](https://arxiv.org/abs/2604.14969)
- **2026-04-17**: MemoSight: 컨텍스트 압축과 다중 토큰 예측을 특수 토큰/위치 레이아웃으로 통합해 KV 캐시 66% 감소, 추론 1.56배 가속 [(원문)](https://arxiv.org/abs/2604.14889)
- **2026-04-17**: RACER: 검색 기반 정확 패턴과 로짓 기반 미래 단서를 통합해 추측적 디코딩 성능 2배 향상 [(원문)](https://arxiv.org/abs/2604.14885)
- **2026-04-17**: 곡률 정렬 프로빙으로 신경망 손실 함수 지형의 안정성을 경계 차원 기반으로 측정 가능 (상위 D 고유벡터 공간) [(원문)](https://arxiv.org/abs/2604.14870)
- **2026-04-17**: Test-time compute 동적 할당: 제한된 추론 예산 내 최적 성능 달성 [(원문)](https://arxiv.org/abs/2604.14853)
- **2026-04-17**: Pangu-ACE: 1B 튜터 라우터가 19.7% 요청을 직접 처리하며 cascade로 compute 최적화 [(원문)](https://arxiv.org/abs/2604.14828)
- **2026-04-14**: 조기 종료 메커니즘: 동적 계산 비용 조정으로 엣지 배포 효율성 향상. 정적 기법과 상호 보완. [(원문)](https://arxiv.org/abs/2604.14789)
- **2026-04-17**: 어텐션 싱크: 학습된 쿼리 바이어스 + 위치 인코딩의 1층 MLP 변환 + 키 프로젝션의 상호작용. 각 요소 제거해도 발생하므로 서로 다른 회로 존재 가능 [(원문)](https://arxiv.org/abs/2604.14722)
- **2026-04-17**: Multiplicative gating이 attention의 Fisher-Rao 기하학적 표현성을 확대하여 positively curved manifold 생성 가능 [(원문)](https://arxiv.org/abs/2604.14702)
- **2026-04-17**: Speculative decoding: 코드생성(높은 수용률) vs 자유 채팅(낮은 수용률) 도메인별 편차 실측 [(원문)](https://arxiv.org/abs/2604.14682)
- **2026-04-17**: Zeroth-order 방법의 선형 안정성은 전체 Hessian 스펙트럼에 의존 (1차 방법과 대조) [(원문)](https://arxiv.org/abs/2604.14669)
- **2026-04-17**: 탐색-안정화 밸런싱으로 학습 수렴 속도 및 신뢰성 개선 [(원문)](https://arxiv.org/abs/2604.14646)
- **2026-04-17**: MoE 모델 on-premises serving의 메모리 병목을 speculative decoding으로 해결 (ELMoE-3D) [(원문)](https://arxiv.org/abs/2604.14626)
- **2026-04-17**: Self-speculative decoding에서 confidence-based adaptive layer skipping으로 추론 속도 개선 [(원문)](https://arxiv.org/abs/2604.14612)
- **2026-04-17**: Claude Haiku/Amazon Nova 프롬프트 최적화 성공률 ~50% 이하, 18,000회 그리드 평가로 agent 간 상호작용 무의미 확인 [(원문)](https://arxiv.org/abs/2604.14585)
- **2026-04-17**: 에이전트 특화 SFT/RL로 30B 모델에서 대규모 시스템 수준 성능 달성. 비용 대비 성능 최적화 [(원문)](https://arxiv.org/abs/2604.14518)
- **2026-04-17**: Spiking Neural Network의 quantization에서 정확도 동등 조건의 firing behavior 차이 분석 [(원문)](https://arxiv.org/abs/2604.14487)
- **2026-04-17**: PINN에서 finite-difference 보조 항으로 residual field 정규화, 3D heat-conduction에서 경계층 오차 감소 [(원문)](https://arxiv.org/abs/2604.14472)
- **2026-04-17**: 공유 가중치 재귀 구조(HRM-LM)는 독립 레이어 쌓기보다 표현력에서 격차 발생 [(원문)](https://arxiv.org/abs/2604.14442)
- **2026-04-14**: Geometric routing으로 MoE expert의 monosemantic 특성 입증. 15% experts가 temporal, geographic, cardinal, discourse, emotional, financial, military, scientific 등 10개 카테고리에 특화 [(원문)](https://arxiv.org/abs/2604.14434)
- **2026-04-14**: MoE 라우팅 토폴로지는 언어 모델 품질 결정 무관. 5가지 라우팅 변형이 76-84M 파라미터 규모에서 통계적으로 동등 (33.93-34.72 PPL) [(원문)](https://arxiv.org/abs/2604.14419)
- **2026-04-17**: 텐서 네트워크 분해를 통한 신경망 압축으로 계산 효율성과 설명가능성 동시 달성 가능 [(원문)](https://arxiv.org/abs/2604.14287)
- **2026-04-17**: 메트릭-인식 PCA (MAPCA): 일반 메트릭으로 스케일 불변 표현 학습, beta-family 스펙트럼 편향 연속 제어 [(원문)](https://arxiv.org/abs/2604.14249)
- **2026-04-17**: 회로 레이아웃 최적화를 LLM 생성 작업으로 재정의 (라우팅 가능성 향상) [(원문)](https://arxiv.org/abs/2604.14237)
- **2026-04-17**: 토큰 길이 정규화를 통한 자동 프롬프트 최적화(CROP)로 80.6% 토큰 감소, 성능 유지 [(원문)](https://arxiv.org/abs/2604.14214)
- **2026-04-17**: 중국어 프롬프트 토큰 효율성은 모델에 따라 다르며, 코딩 작업 성공률은 영어가 더 높음 [(원문)](https://arxiv.org/abs/2604.14210)
- **2026-04-17**: Cross-architecture distillation: Transformer→SSM(Mamba) 증류 시 초기화 전략으로 성능 보존 가능성 입증 [(원문)](https://arxiv.org/abs/2604.14191)
- **2026-04-17**: Gradient entanglement 분석: 다중 목적 최적화 시 감독 gradient 왜곡 및 표현 겹침 발생 [(원문)](https://arxiv.org/abs/2604.14176)
- **2026-04-17**: 계층적 메모리 메커니즘으로 모바일 입력기에서 사용자 개인화 LLM 실시간 구현 [(원문)](https://arxiv.org/abs/2604.14159)
- **2026-04-17**: 프롬프트 및 디코딩 스텝 적응형 동적 압축 감지 프레임워크로 메모리와 지연시간 감소 [(원문)](https://arxiv.org/abs/2604.14156)


## 핵심 주체
[[Looped Transformers]] | [[Transformer Expressivity]]


## 모순/논쟁

