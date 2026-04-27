---
type: concept
domain: ai
last_updated: 2026-04-27
source_count: 0
---

# Audio-Language Models

## 정의


## 주요 발전
- **2026-04-22**: Unified model for speech/music/SFX via natural language instructions with dynamic token injection [(원문)](https://arxiv.org/abs/2604.22209)
- **2026-04-21**: 지시 튜닝으로 명시적 채점 기준과 추론을 임베딩 → 1,600샘플에서 인간 정렬성 개선 [(원문)](https://arxiv.org/abs/2604.22225)
- **2026-04-25**: AUDITA는 음성 질답의 진정한 추론을 평가하기 위해 도메인 편향과 지름길 전략을 배제한 대규모 벤치마크 [(원문)](https://arxiv.org/abs/2604.21766v1)
- **2026-04-25**: 디코더 기반 LLM이 ASR 평가의 효과적인 도구로 사용 가능 [(원문)](https://arxiv.org/abs/2604.21928v1)
- **2026-04-21**: 음성 개별 단어만으로 학습한 CNN 기반 신경망이 다중 단어 연결을 자발적으로 생성 [(원문)](https://arxiv.org/abs/2305.01626)
- **2026-04-24**: AUDITA 벤치마크: 실제 오디오 추론 능력 평가 (인간 기준선 32.13%, 산만하는 요소 포함 장시간 시간 의존성) [(원문)](https://arxiv.org/abs/2604.21766)
- **2026-04-24**: 인도 10개 언어 기반 120K+ 페어와이즈 TTS 비교 평가 (Bradley-Terry 모델링) [(원문)](https://arxiv.org/abs/2604.21481)
- **2026-04-21**: LLM 기반 디코더가 반드시 인구통계 편향을 증가시키지는 않음 (Granite-8B 민족성 WER max/min=2.28) [(원문)](https://arxiv.org/abs/2604.21276)
- **2026-04-21**: LLM이 동시 음성 번역(SST) 품질을 크게 개선하나 계산 오버헤드 증가로 실시간 처리 어려움 [(원문)](https://arxiv.org/abs/2604.21045)
- **2026-04-20**: 샤오미 OmniVoice, 600+ 언어 확산 언어 모델 기반 비자기회귀 TTS 오픈소스 공개 [(원문)](https://www.aitimes.com/news/articleView.html?idxno=209553)
- **2025-12**: SpidR-Adapt의 FOBLO 최적화로 수백 시간 데이터 없이도 새 언어 음성 표현 습득 가능 [(원문)](https://arxiv.org/abs/2512.21204)
- **2025-06-15**: Mamba 기반 HuBERT, SUPERB 벤치마크 인과 설정에서 경쟁력 있는 성능 [(원문)](https://arxiv.org/abs/2506.12606)
- **2025-06-15**: 음성 인식 후 LLM으로 고유명사 복원, 음성-의미 문맥 활용 [(원문)](https://arxiv.org/abs/2506.10779)
- **2026-04-21**: PodSarc: 음성 전용(멀티모드 불필요) 사항 검출에서 LLM 자동 라벨링 + 인간 검증 협업으로 F1 73.63% 달성 [(원문)](https://arxiv.org/abs/2506.00955)
- **2026-04-18**: Omni-Embed-Audio: 자연 검색 행동 모의(질문, 명령, 태그, 바꿔 표현, 제외) 기반 오디오-텍스트 검색 견고성 향상 [(원문)](https://arxiv.org/abs/2604.18360)
- **2026-04-21**: 하이브리드 보상(LLM 평가 + 임베딩 유사도)으로 음성 reasoning의 논리적 깊이와 음향 접지성 동시 강화 [(원문)](https://arxiv.org/abs/2604.18187)
- **2026-04-21**: LLM 기반 음성 인식(ASR) 프레임워크 NIM4 제안: 다중 단계 학습으로 강건성 및 효율화 달성 [(원문)](https://arxiv.org/abs/2604.18105)
- **2026-04-21**: VIBE 프레임워크로 실제 인간 음성 데이터 기반 생성적 편향 평가 [(원문)](https://arxiv.org/abs/2604.17248)
- **2026-04-21**: 비교 유도 ICL로 미학습 딥페이크에 대한 training-free 일반화 달성 [(원문)](https://arxiv.org/abs/2604.16749)
- **2026-04-21**: TokenChain이 ASR-TTS 피드백을 의미 토큰으로 통합해 인간 지각-산출 루프 모사 (2026-04-21) [(원문)](https://arxiv.org/abs/2510.06201)
- **2026-04-21**: Qwen2-Audio가 저자원 언어 ASR에서 상당한 성능 기여, 다중 모달 학습의 저자원 환경 효율성 입증 [(원문)](https://arxiv.org/abs/2604.18204)
- **2026-04-21**: 음성 instruction data + SER 데이터로 감정적 음성 대화 시스템 구축 [(원문)](https://arxiv.org/abs/2604.18159)
- **2026-04-21**: 사전학습 AudioLLM으로 30분 큐레이션 데이터만으로 높은 감정 전달 성능 달성 [(원문)](https://arxiv.org/abs/2604.17435)
- **2026-04-21**: TPI-Train (88K 샘플)로 제3자 개입 시 주 사용자 음성 구분 능력 강화, acoustic signal 우선순위 학습 [(원문)](https://arxiv.org/abs/2604.17358)
- **2026-04-21**: 팟캐스트·라디오·음성 메모 등 증가하는 채널에서 미정보 검증의 중요성 대두 [(원문)](https://arxiv.org/abs/2604.16767)
- **2026-04-21**: 오디오-텍스트 크로스 어텐션 기반 Bayesian 어댑터로 저자원 멀티모달 학습에서 불확실성 정량화 [(원문)](https://arxiv.org/abs/2604.16657)


## 핵심 주체
[[Voice Synthesis]] | [[Diffusion Models]] | [[Multimodal AI]] | [[Text-to-Speech]]


## 모순/논쟁

