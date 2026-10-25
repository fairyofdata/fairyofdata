**🌐 Available Versions:** [🇺🇸 English](./README.md) | [🇰🇷 한국어](./README_KR.md) | [🇯🇵 日本語](./README_JP.md)

---

# 안녕하세요! 👋

맑은 하늘의 오카야마에서 소프트웨어 엔지니어로 근무하고 있는 **백지헌**입니다.

LLM Application, Natural Language Processing(NLP), AI Engineering, 워크플로우 자동화에 깊은 관심을 두고 있으며,
단순 데모를 넘어 **LLM·머신러닝 시스템을 만들고, 재현 가능한 평가로 실제 운영 환경에서 계속 가치를 내는 AI 엔지니어**를 지향합니다.

현재는 **LLM 기반 애플리케이션**, **업무 프로세스 및 문서 자동화**, **실용적 AI 솔루션 아키텍처**를 중심으로 역량을 고도화하고 있습니다.

📧 **Email** : fairyofdata@gmail.com  
💼 **LinkedIn** : https://www.linkedin.com/in/hjbaek/

---

## 🎯 Focus

- 🤖 LLM 애플리케이션과 AI 엔지니어링
- 📏 머신러닝·LLM 시스템의 재현 가능한 평가
- 💬 자연어 처리와 문서 정보 추출
- ⚙️ MLOps와 실운영에 견디는 AI 시스템

---

## 💻 Tech Stack

**머신러닝·음성**  
<img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"> <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"> <img src="https://img.shields.io/badge/Transformers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black"> <img src="https://img.shields.io/badge/Whisper-412991?style=for-the-badge&logo=openai&logoColor=white"> <img src="https://img.shields.io/badge/Wav2Vec2-0467DF?style=for-the-badge&logo=meta&logoColor=white">

**LLM·검색**  
<img src="https://img.shields.io/badge/OpenAI_API-74AA9C?style=for-the-badge&logo=openai&logoColor=white"> <img src="https://img.shields.io/badge/Gemini_API-4285F4?style=for-the-badge&logo=google&logoColor=white"> <img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white"> <img src="https://img.shields.io/badge/FAISS-0467DF?style=for-the-badge&logo=meta&logoColor=white">

**Web·API**  
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">

**데이터베이스**  
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white"> <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white">

**인프라·개발 환경**  
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"> <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=white"> <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white"> <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white">

---

## 🗂️ Projects

### ⭐ 주요 프로젝트

---

#### 🧑‍🏫 [PhonemeJP2KR — 일본인 학습자를 위한 음소 단위 한국어 발음 코칭](https://github.com/fairyofdata/PhonemeJP2KR)
> `Python` `Streamlit` `Whisper` `Wav2Vec2` `Gemini` `G2P`

일본어 모어 화자가 한국어 발음을 교정할 수 있도록 설계된 CAPT(Computer-Assisted Pronunciation Training) 웹 애플리케이션입니다. 우수상을 받은 팀 프로젝트 URFIT에서 맡은 음성 검색 모듈([Songfinder](https://github.com/fairyofdata/RAGSTT4Lyrics))에서 정립한 ASR(Whisper) 및 오디오 처리 파이프라인 기술을 확장하여, 한층 고도화된 음소 수준의 발음 진단 시스템으로 설계했습니다.

- **듀얼 ASR 아키텍처**: 언어모델이 내장된 Whisper(지능적 오류 보정)와 언어모델이 없는 Wav2Vec2-CTC(물리적 발성 포착)의 차이를 측정하여 학습자 스스로 인지하지 못하는 발음 오류를 수치화합니다.
- **결정론적 G2P 엔진**: 표준발음법(7종성, 연음, 비음화, 격음화 등) 규칙을 순수 Python으로 직접 구현하여 LLM 환각을 원천 차단하고 동일 입력에 대해 항상 동일한 점수를 보장합니다.
- **L1 간섭 오류 분류기**: 대조음운론 연구(장향실 2016 등)에 학술적 근거를 둔 규칙 기반 태거로, 일본어 모어 화자에게서 체계적으로 나타나는 모음 삽입, 받침 탈락, 3지대립 붕괴 등 6가지 오류 유형을 진단합니다. LLM(Gemini)은 진단된 구조화된 증거만을 받아 카타카나 시각화와 코칭 피드백만 담당합니다.
- **실증 검증**: 실제 일본인 화자 음성(AI-Hub L2 코퍼스, 615개 발화·198명)에서 상/하 평가 판별 AUC 0.818, 사람 평가와의 상관 ρ = 0.473을 보이며 고전적 GOP 기준선을 모든 지표에서 앞섰습니다. 이 밖에 Spearman ρ = −0.702(점수-오류 심각도 상관), G2P 정확도 100%(51/51·17/17, held-out) 등 6가지 재현 가능한 실험으로 시스템 유효성을 검증했습니다.

---

#### 📊 [PortfolioOpt4ESG — LLM 기반 ESG 중심 포트폴리오 최적화 서비스](https://github.com/fairyofdata/PortfolioOpt4ESG)
> `Python` `Streamlit` `KoELECTRA` `GPT-3.5` `Black-Litterman` `KOSPI`

🏆 광운대학교 제8회 산학협력 SW 프로젝트 **우수상** · 정보융합학과 졸업전시회 **우수상**  
📄 공저 논문(제2저자) *Computational Economics*(Springer, 2026) 게재 — [doi:10.1007/s10614-026-11413-9](https://doi.org/10.1007/s10614-026-11413-9)

한국 상장 기업의 뉴스 텍스트를 LLM 및 파인튜닝 모델로 직접 분석하여 투명한 ESG 점수를 산출하고, 이를 Black-Litterman 모델의 투자자 뷰로 반영해 맞춤형 포트폴리오를 구성하는 연구/서비스 시스템입니다.

- **데이터 파이프라인**: KOSPI 68개사의 뉴스 **138만 건**을 수집하고, GPT-3.5로 라벨 부트스트래핑 후 KoELECTRA를 파인튜닝해 6단계 분류/회귀 모델 캐스케이드를 구축했습니다.
- **포트폴리오 최적화**: 사용자 설문(15문항)이 E/S/G 선호를 에이전시별 방법론 가중치로 변환되며, 이를 Black-Litterman 뷰(P, Q)로 주입 후 Ledoit-Wolf shrinkage 공분산 기반 최대 샤프 비율 최적화를 수행합니다.
- **백테스팅**: 2020~2024년 연간 리밸런싱 기준으로 KOSPI(Sharpe 0.190), ESG ETF(0.251) 대비 **최적화한 ESG 포트폴리오(0.499, 최대 낙폭 0.187)**가 모든 지표에서 우세함을 증명했습니다.

---

#### 🎵 [Songfinder — 음성으로 찾는 J-POP 검색과 플레이리스트 생성](https://github.com/fairyofdata/RAGSTT4Lyrics)
> `Python` `FastAPI` `Angular` `Whisper` `FAISS` `SentenceTransformer` `Spotify API`

🏆 한국무역협회 SCIT Master 47기 프로젝트 발표회 **우수상**(6인 팀 프로젝트 URFIT으로 수상)  
👤 URFIT 중 음성·음악 매칭 파트(STT → FAISS 검색 → 추천 → Spotify 플레이리스트)를 혼자 구현했고, 2026년 리팩토링도 혼자 진행했습니다.

"대충 아는 가사"나 흥얼거림만으로 원하는 J-POP을 찾고, AI가 취향 기반 유사 곡 추천 및 Spotify 플레이리스트를 자동 생성해주는 커뮤니티 서비스입니다.

- **멀티모달 검색**: Whisper(STT)로 음성을 텍스트로 변환 후, SentenceTransformer 임베딩과 FAISS 인덱스로 가사 데이터셋을 벡터 유사도 검색합니다.
- **AI 플레이리스트 생성**: 검색 결과를 GPT-3.5가 분석해 창의적인 플레이리스트 제목/설명을 자동 생성하고, Spotify OAuth API로 사용자 계정에 직접 저장합니다.
- **아키텍처 리팩토링**: Hugging Face Space 기반 프로토타입을 Angular 17+(Frontend) + FastAPI(Backend) 마이크로서비스 아키텍처로 완전 분리하여 Firebase, Cloud Run 등 다양한 클라우드 환경 배포에 대응했습니다.

---

### 🚧 개발 중

- **[한국어 화자를 위한 일본어 작문 코치](https://github.com/fairyofdata/PragmaticsKR2JP)** · `PragmaticsKR2JP` · 2026.09 – · 개인  
  고정된 오류 분류표 안에서 LLM은 오류의 위치와 유형만 붙이고, 인용 원문 대조·3회 채점 다수결·집계는 모두 코드가 합니다.
- **[로컬 모델이 관문을 서는 캐스케이딩 DLP 레이어](https://github.com/fairyofdata/CascadeDLP)** · `CascadeDLP` · 2026.09 – · 개인  
  문서를 클라우드 LLM에 넘기기 전에 로컬 모델이 먼저 읽고 「통과·가려서 전송·사용자 확인·로컬 전용·차단」 중 하나로 판정합니다. 한·일·영 혼용 문서가 대상이며 MCP 도구로 씁니다.

---

### 📁 그 밖의 프로젝트

- **[한일 보도를 비교해 중립 기사로 합성](https://github.com/fairyofdata/Neutralize4KRJP)** · `Neutralize4KRJP` · 2024 · 개인  
  같은 사안을 다룬 중앙일보·요미우리신문 기사를 짝지어, 공통 사실과 강조점의 차이를 나눈 기사 한 편을 한·일 두 언어로 합성합니다(Pydantic으로 출력 검증). 성신여자대학교 SW021 「ChatGPT for Business」 과정의 연장선에서 만든 개인 프로젝트입니다.
- **[세 모델 앙상블로 스미싱 탐지](https://github.com/fairyofdata/AntiPhishingNLP)** · `AntiPhishingNLP` · 2023 · 5인 팀 · 🥇 KISA 사이버보안 AI·빅데이터 챌린지 Track C 최우수상(1위)  
  문자 메시지를 KoBERT·KoELECTRA·Att-BiLSTM 소프트 보팅으로 분류합니다(보이스피싱은 별도 데모). 담당: Att-BiLSTM 설계·구현, 소프트 보팅 전략, SMOTE, 추론 모듈. 한국외국어대학교 데이터청년캠퍼스 팀 프로젝트입니다.
- **[자모 단위로 우회 욕설 탐지](https://github.com/fairyofdata/SepticFilterNLP)** · `SepticFilterNLP` · 2022 · 6인 팀 · 🥇 삼성SDS 멀티캠퍼스 빅데이터 활용 공모전 최우수상(1위)  
  글자 분리나 기호 삽입으로 숨긴 욕설을 잡아냅니다. 담당: 크롤링(커뮤니티 댓글 5만 6천 건 이상), MySQL 스키마, 데이터 파이프라인, Django 연동.

---

## 📚 Education & Training

- **정보융합학과 데이터사이언스전공 학사** [@광운대학교](https://ic.kw.ac.kr:501/program/process.php)  
- **K-디지털 트레이닝**: 데이터 사이언스 과정 [@멀티캠퍼스 (삼성 SDS)](https://www.multicampus.com/em/enrolment/courseDetai?p_menu=NzUjU1VC&p_gubun=Qw==&corsCd=FA00NM)  
- **LG Aimers**: 데이터 인텔리전스 과정 [@LG AI 연구원](https://lgresearch.ai/news/view?seq=488)  
- **데이터 청년 캠퍼스**: 자연어 처리 과정 [@한국외국어대학교](https://ime.hufs.ac.kr/bbs/ime/509/71087/artclView.do)  
- **SW021**: ChatGPT 비즈니스 활용 과정 [@성신여자대학교](https://m.dhnews.co.kr/news/view/1065594826213812)  
- **ACC Korea**: AWS 공식 대학생 커뮤니티 1기 멤버 [@AWS Korea](https://www.awscloudclubs.kr/)  
- **SCIT Master**: 일본 IT직무 취업연계 프로그램 [@한국무역협회](https://newtradecampus.kita.net/page/user_job_CloudIT_courseguide_outline)  

---

## 🏆 Awards

- 🥇 **삼성SDS 멀티캠퍼스 빅데이터 활용 공모전** (멀티캠퍼스, 2022) - **최우수상 (1위)**  
- 🥇 **한국인터넷진흥원 사이버보안 AI-빅데이터 챌린지 Track C** (KISA, 2023) - **최우수상 (1위)**  
- 🥈 **광운대학교 제8회 산학협력 SW 프로젝트** (광운대, 2024) - **우수상 (2위)**  
- 🥈 **광운대학교 정보융합학과 졸업작품 전시회** (광운대, 2024) - **우수상 (2위)**  
- 🥈 **한국무역협회 제47기 SCIT Master 프로젝트 발표회** (KITA, 2025) - **우수상 (2위)**  
