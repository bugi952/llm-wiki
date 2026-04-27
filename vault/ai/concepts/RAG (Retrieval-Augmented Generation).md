---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# RAG (Retrieval-Augmented Generation)

## 정의


## 주요 발전
- **2026-01-14**: CoM의 adaptive truncation으로 retrieval recall vs reasoning accuracy 간극 해소 [(원문)](https://arxiv.org/abs/2601.14287)
- **2025-08-10**: 개인 맥락 검색 후 자연언어 피드백으로 응답 품질 및 관련성 향상 [(원문)](https://arxiv.org/abs/2508.10695)
- **2025-08-06**: UR² 프레임워크: 어려운 인스턴스만 선택적으로 검색 호출, 도메인 코퍼스와 LLM 생성 요약 하이브리드 활용 [(원문)](https://arxiv.org/abs/2508.06165)
- **2026-04-27**: UAE 방법으로 QASPER 벤치마크에서 Recall@1 30.59%, MAP 30.16% 향상 (arXiv:2604.22722) [(원문)](https://arxiv.org/abs/2604.22722)
- **2026-04-27**: Query variant selection에 Query Performance Prediction(QPP) 활용 → downstream retrieval/generation 비용 선제적 감소 가능 [(원문)](https://arxiv.org/abs/2604.22661)
- **2026-04-27**: ResRank: passage를 compact token으로 압축 → 'lost in the middle' 현상 완화 및 inference latency 선형화 [(원문)](https://arxiv.org/abs/2604.22180)
- **2026-04-27**: BERAG: Bayesian ensemble 방식으로 lost-in-the-middle 문제 해결, 시각 데이터 확장성 개선 [(원문)](https://arxiv.org/abs/2604.22678)
- **2026-04-22**: 다단계 패러프레이즈를 검색·요약·생성에 통합하면 long-tail 관계 완성에서 최대 40.6 EM 점수 향상, 모델 미세조정 불필요 [(원문)](https://arxiv.org/abs/2604.22261)
- **2026-04-22**: 2026년 MuDABench 벤치마크 제안, 80,000+ 페이지 금융 문서에서 332개 분석 QA 인스턴스로 표준 RAG의 다문서 종합 능력 한계 지적 [(원문)](https://arxiv.org/abs/2604.22239)
- **2026-04-21**: 27개 LLM 평가: 대부분 문서 정보를 사용자 정보보다 우선하며, post-training으로 강화됨 [(원문)](https://arxiv.org/abs/2604.22193)
- **2026-04-26**: 우크라이나어: 2-stage hybrid search + synthetic fine-tuning으로 저자원 로컬 배포 가능 (UNLP 2026 2위) [(원문)](https://arxiv.org/abs/2604.22095)
- **2026-04-27**: 임상 EHR 처리에서 RAG로 관련 세그먼트 추출 후 LLM 인코딩하여 입력 복잡도 감소 [(원문)](https://arxiv.org/abs/2604.22061)
- **2026-04-24**: Organize의 RARE 논문이 ACL 2026 메인 채택, 금융·법률 분야 RAG 성능 5% 하락 지적 [(원문)](https://www.aitimes.com/news/articleView.html?idxno=209713)
- **2026-04-24**: Sentinel-Strategist 아키텍처로 다중 벡터 공격 방어. 선택적 방어 배포로 검색 성능 저하 40% 이상 감소 [(원문)](https://arxiv.org/abs/2604.20932)
- **2026-04-24**: Iterative, feedback-driven GraphRAG 아키텍처: 응답 품질 평가로 반복적 정제 → HotPotQA 기준 의미론적 품질 향상 [(원문)](https://arxiv.org/abs/2604.20859)
- **2026-04-24**: 내부 파라미터와 검색 정보 간 knowledge conflict를 Dempster-Shafer Theory로 측정해 신뢰성 향상 (ERA) [(원문)](https://arxiv.org/abs/2604.20854)
- **2026-04-21**: Atom-Entity Graph: 텍스트 청크 대신 자기포함적 원자 팩트 단위로 지식 표현하여 유연성과 정확성 향상 [(원문)](https://arxiv.org/abs/2604.20844)
- **2025-10-01**: 2025년 ERL 프레임워크로 search-augmented LLM의 decomposition/retrieval/reasoning 오류 식별 및 재생성 메커니즘 도입 [(원문)](https://arxiv.org/abs/2510.00861)
- **2026-04-21**: LTRR: 쿼리 유형별 최적 retriever 동적 선택으로 단일 retriever 대비 일관되게 우수 성능 달성 [(원문)](https://arxiv.org/abs/2506.13743)
- **2025-05-16**: LC-RAG: 환경 로그를 컨텍스트로 추가해 약한 의미 링크 강화. 학생 대화 기반 협업 peer agent Copa 구현 [(원문)](https://arxiv.org/abs/2505.17238)
- **2026-04-21**: 이미지 기반 문서 임베딩이 표/수식/차트 등 구조화 요소 처리에 부족. LaTeX 원본 소스 접근 시 검색 성능 향상. [(원문)](https://arxiv.org/abs/2604.18508)
- **2026-04-21**: Multi-hop 검색 평가 CARE 기법 제안, HotPotQA/MuSiQue 벤치 사용 [(원문)](https://arxiv.org/abs/2604.18234)
- **2026-04-21**: LLM agents를 활용한 취약점 분석 자동화 및 보고서 생성 (RAVEN) [(원문)](https://arxiv.org/abs/2604.17948)
- **2026-04-21**: Bayesian Active Learning + Gaussian Process로 LLM 관련성 신호를 임베딩 공간 전체에 전파하는 BAGEL 프레임워크 (arXiv:2604.17906) [(원문)](https://arxiv.org/abs/2604.17906)
- **2026-04-21**: AVA: 인용 검증 가능성으로 RAG의 신뢰성 문제 해결 (World Bank 4,000+ 보고서) [(원문)](https://arxiv.org/abs/2604.17843)
- **2026-04-21**: HeadRank: 엔트로피 정규화된 attention head 선택으로 무디코딩 reranking 구현 [(원문)](https://arxiv.org/abs/2604.17237)
- **2026-04-21**: RLM-on-KG: 증거가 산재된 상황에서만 LLM 제어가 규칙 기반 탐색보다 우월 (GraphRAG 대비 +0.16pp F1, 비유의) [(원문)](https://arxiv.org/abs/2604.17056)
- **2026-04-21**: LLM 기반 dense retriever는 명령어 튜닝 모델이 강력하나, 복잡 추론 최적화 모델은 일반화 성능 저하(specialization tax) 발생 [(원문)](https://arxiv.org/abs/2604.16576)
- **2026-04-21**: GraphRAG-Router: 강화학습 기반 hierarchical routing으로 heterogeneous GraphRAG/LLM 조정 [(원문)](https://arxiv.org/abs/2604.16401)
- **2026-04-21**: 2026-04 AgriIR: 1B 파라미터 모델 + 적응형 리트리버로 인도 농업 정보 접근 최적화 (모듈식, 결정론적 인용) [(원문)](https://arxiv.org/abs/2604.16353)
- **2026-04-21**: 구성성 기반 부정(negation), 역할 교환(role swap) 같은 최소 편집이 임베딩 유사도는 높으나 의미 뒤집음. 코사인 공간의 기하학적 한계 (2026-04) [(원문)](https://arxiv.org/abs/2604.16351)
- **2026-04-21**: LiteSemRAG: 인덱싱·쿼리 단계에서 LLM 호출 제거. 컨텍스트 토큰 임베딩 + 동적 의미 노드 구성으로 다의성(polysemy) 모델링 (2026-04) [(원문)](https://arxiv.org/abs/2604.16350)
- **2026-04-21**: RT-QA: 실행 가능한 코드 워크플로우로 검색 기반 에이전트를 평가. 12개 도메인, 320개 중국어 질문, 웹 구조 변화 적응 메커니즘 (2026-04) [(원문)](https://arxiv.org/abs/2604.16349)
- **2026-04-21**: X선 회절 실험 영상 분석에 RAG 적용하여 사이트별 안전 규칙 추출 [(원문)](https://arxiv.org/abs/2604.16345)
- **2026-04-21**: 멀티모달 문서 QA를 위한 적응형 RAG 프레임워크(MARA): 쿼리-영역 정렬 및 동적 증거 선택 [(원문)](https://arxiv.org/abs/2604.16313)
- **2026-04-21**: FlexStructRAG: 지식 그래프(이진), 하이퍼그래프(n-ary), 의미 클러스터를 통합하는 쿼리 적응형 다중 구조 검색 [(원문)](https://arxiv.org/abs/2604.16312)
- **2026-04-21**: RAG-DIVE: Multi-turn 대화를 동적으로 생성·검증·평가하는 RAG 시스템 평가 프레임워크 [(원문)](https://arxiv.org/abs/2604.16310)
- **2026-04-21**: 증거 요약/추출/추론 전담 역할 에이전트들의 다중 중간 증거 관점을 비교·통합하는 합성 단계로 노이즈/불완전/이질적 검색 맥락 처리 개선 [(원문)](https://arxiv.org/abs/2604.18509)
- **2026-04-21**: ArbGraph: 증거 그래프 기반 갈등 해소로 장문 RAG 신뢰성 개선 (arXiv:2604.18362v1) [(원문)](https://arxiv.org/abs/2604.18362)
- **2026-04-21**: Context-aware 블랙박스 최적화에 RAG 적용: 과거 문맥 검색으로 레짐 대리 프록시 식별 후 soft prompt 기반 손실 예측 [(원문)](https://arxiv.org/abs/2604.18026)
- **2026-04-21**: DoRA: 방어 문서 기반 6.5K 인스턴스로 contamination-aware RAG 평가, hallucination 47% 감소 [(원문)](https://arxiv.org/abs/2604.17943)
- **2026-04-21**: LAnR: 텍스트 쿼리 대신 LLM 숨겨진층에서 직접 검색 벡터 생성, 텍스트 모듈 제거로 일체형 프레임워크 구현 [(원문)](https://arxiv.org/abs/2604.17866)
- **2026-04-21**: O-RAN, 3GPP, srsRAN 기술 문서의 dense, acronym-heavy 특성을 반영한 embedding 벤치마크 (9,000 QA pairs, 3 chunk sizes) [(원문)](https://arxiv.org/abs/2604.17778)
- **2026-04-21**: 문서 내 다중 주제 인터리빙으로 인한 임베딩 공간의 '의미적 겹침(Semantic Entanglement)' 현상. Entanglement Index로 정량화, Semantic Disentanglement Pipeline으로 해결 [(원문)](https://arxiv.org/abs/2604.17677)
- **2026-04-21**: 고정 검색 대비 함께 학습 시 +26.8% F1 개선 (7개 QA 벤치), 검색이 주요 병목 [(원문)](https://arxiv.org/abs/2604.17555)
- **2026-04-21**: EHRAG 프레임워크는 structural hyperedge (문장 co-occurrence)와 semantic hyperedge (embedding clustering)를 결합하여 disjoint entity 간 의미 연결 포착. Hybrid structural-semantic diffusion으로 검색 성능 향상 [(원문)](https://arxiv.org/abs/2604.17458)
- **2026-04-21**: 메타 플래너가 엔티티 그라운딩을 미뤄두고 먼저 추상적 추론 골격 수립으로 어휘적 모호성에 대한 취약성 완화 (arXiv:2604.17405) [(원문)](https://arxiv.org/abs/2604.17405)
- **2026-04-21**: RoTRAG: 인간 작성 도덕 규범(Rules of Thumb)을 외부 corpus로 활용한 harm assessment [(원문)](https://arxiv.org/abs/2604.17301)
- **2026-04-21**: NWCAD: 비신뢰 컨텍스트 시 폴백으로 중립 회귀 방지 (2단계 게이트 방식) [(원문)](https://arxiv.org/abs/2604.16686)
- **2026-04-20**: Spectral Tempering: 임베딩 차원 축소 시 SNR 기반 적응적 스펙트럼 스케일링으로 PCA(분산 보존) vs 화이트닝(등방성) 절충 [(원문)](https://arxiv.org/abs/2603.19339)
- **2026-02-01**: 임상시험 프로토콜 추출에 domain-specific RAG 적용 시 독립 LLM(62.6%)보다 높은 정확도(89.0%) 달성 [(원문)](https://arxiv.org/abs/2602.00052)
- **2025-03-02**: Quantum 프로그래밍 도메인에 RAG 적용하여 LLM 기반 코드 생성 성능 개선 [(원문)](https://arxiv.org/abs/2503.02497)
- **2026-01-03**: LLM은 정부/신문 같은 제도권 출처를 선호하나, 정보 반복으로 선호도 역전 가능 (13개 모델 검증) [(원문)](https://arxiv.org/abs/2601.03746)
- **2025-02-20**: Retrieved context의 이진 갈등 분석 한계 극복, Self-attention·LayerNorm의 hallucination 역할 실증 [(원문)](https://arxiv.org/abs/2512.07515)
- **2025-07-16**: 다단계 reflection과 검증으로 신뢰성 기반 RL 최적화 (Deliberative Searcher) [(원문)](https://arxiv.org/abs/2507.16727)
- **2025-05-21**: FRANQ - faithfulness-aware uncertainty quantification으로 hallucination 탐지 개선 [(원문)](https://arxiv.org/abs/2505.21072)
- **2026-04-20**: RAG 파이프라인에서 익명화 적용 위치(데이터셋 vs 생성 답변)가 개인정보-유틸리티 트레이드오프에 영향 [(원문)](https://arxiv.org/abs/2604.15958)
- **2026-04-20**: LLM 기반 코딩에서 멀티모달 검색으로 신뢰성 향상 [(원문)](https://arxiv.org/abs/2604.15663)
- **2026-04-20**: AdaRankLLM: zero-shot prompt + passage dropout 기반 적응형 listwise reranking. LLM 성능 향상에 따라 고정 깊이 검색의 필요성 재평가 [(원문)](https://arxiv.org/abs/2604.15621)
- **2026-04-20**: Closed-domain hallucination 문제에 대해 토큰 레벨 detection 기반 파인튜닝 방법 제시 [(원문)](https://arxiv.org/abs/2604.15945)
- **2026-04-20**: Skill-RAG 프레임워크: hidden-state probe로 검색 실패 진단 후 query rewriting/decomposition/focusing 중 선택 [(원문)](https://arxiv.org/abs/2604.15771)
- **2026-04-19**: IG-Search: 정보 이득 기반 단계별 보상으로 검색 쿼리 효율성 개선 [(원문)](https://arxiv.org/abs/2604.15148v1)


## 핵심 주체
[[Agent Memory]] | [[Long-Context Processing]] | [[Agentic AI]]


## 모순/논쟁

