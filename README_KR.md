<!-- 원본: README_KR.md (한국어판이 원본, 영·일은 번역) · 동기화: 2026-10-26 -->

# 안녕하세요! 👋

[English](README.md) · [한국어](README_KR.md) · [日本語](README_JP.md)

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

일본어 모어 화자가 한국어 발음 오류를 음소 단위로 찾고 고치도록 돕는 CAPT(Computer-Assisted Pronunciation Training) 웹 애플리케이션입니다. 팀 프로젝트 URFIT 에서 맡은 음성 검색 모듈([RAGSTT4Lyrics](https://github.com/fairyofdata/RAGSTT4Lyrics))의 ASR(Whisper)·오디오 처리 파이프라인을 넓혀 만들었습니다.

- **듀얼 ASR**: 언어모델이 내장된 Whisper(원어민이 알아듣는 쪽)와 언어모델이 없는 Wav2Vec2-CTC(실제로 낸 소리 쪽)의 차이를 재서, 학습자가 스스로 듣지 못하는 오류를 드러냅니다.
- **결정적 G2P 엔진**: 표준발음법(7종성, 연음, 비음화, 격음화 등)을 순수 Python 규칙으로 구현해, 같은 입력에는 항상 같은 점수가 나옵니다.
- **L1 간섭 오류 분류기**: 대조음운론 연구(장향실 2016 등)에 근거한 규칙 기반 태거로, 모음 삽입·받침 탈락·평음/격음/경음 혼동 등 일본어 화자에게 체계적으로 나타나는 9가지 오류를 진단합니다. 가타카나 표기도 규칙표로 만들고, LLM(Gemini)은 구조화된 증거를 받아 코칭 문장만 씁니다.
- **실증 검증**: 실제 일본인 화자 음성(AI-Hub L2 코퍼스, 615개 발화·198명)에서 상/하 평가 판별 AUC 0.818, 사람 평가와의 상관 ρ = 0.473 으로 고전적 GOP 기준선을 모든 지표에서 앞섰습니다. 점수와 오류 심각도의 상관은 ρ = −0.702(음성을 다시 합성한 재실행에서는 −0.599, 둘 다 기록), G2P 정확도는 held-out 100%(51/51·17/17)입니다. 실험 6종을 실행했고, 모집 평정자와의 상관 연구는 설계만 마쳤습니다.

---

#### 📊 [PortfolioOpt4ESG — LLM 기반 ESG 중심 포트폴리오 최적화 (LEPOS)](https://github.com/fairyofdata/PortfolioOpt4ESG)
> `Python` `Streamlit` `KoELECTRA` `GPT-3.5` `Black-Litterman` `KOSPI`

🏆 광운대학교 제8회 산학협력 SW 프로젝트 **우수상** · 정보융합학과 졸업전시회 **우수상**  
📄 공저 논문(제2저자) *Computational Economics*(Springer, 2026) 게재 — [doi:10.1007/s10614-026-11413-9](https://doi.org/10.1007/s10614-026-11413-9)

한국 상장 기업의 뉴스 텍스트를 LLM 및 파인튜닝 모델로 직접 분석하여 투명한 ESG 점수를 산출하고, 이를 Black-Litterman 모델의 투자자 뷰로 반영해 맞춤형 포트폴리오를 구성하는 연구/서비스 시스템입니다.

- **데이터 파이프라인**: KOSPI 68개사의 뉴스 **138만 건**을 수집하고, GPT-3.5로 라벨 부트스트래핑 후 KoELECTRA를 파인튜닝해 6단계 분류/회귀 모델 캐스케이드를 구축했습니다.
- **포트폴리오 최적화**: 사용자 설문(15문항)을 E/S/G 선호와 평가기관별 방법론 가중치로 바꾸고, 이를 Black-Litterman 뷰(P, Q)로 넣은 뒤 Ledoit-Wolf shrinkage 공분산 기반 최대 샤프 비율 최적화를 합니다.
- **백테스팅**: 2020~2024년 연간 리밸런싱에서 **최적화한 ESG 포트폴리오(Sharpe 0.499, 최대 낙폭 0.187)**가 KOSPI(0.190)·ESG ETF(0.251)를 모든 지표에서 앞섰습니다 (저장소의 재현 결과. 생존 편향, 표본 안에서 고른 τ 등 한계는 저장소 README 에 적었습니다).

---

#### 🎵 [RAGSTT4Lyrics — 흐릿하게 기억나는 가사로 J-POP 찾기 (Songfinder)](https://github.com/fairyofdata/RAGSTT4Lyrics)
> `Python` `FastAPI` `Angular` `Whisper` `FAISS` `SentenceTransformer` `Spotify API`

🏆 한국무역협회 SCIT Master 47기 프로젝트 발표회 **우수상**(6인 팀 프로젝트 URFIT으로 수상)  
👤 URFIT 중 음성·음악 매칭 파트(STT → FAISS 검색 → 추천 → Spotify 플레이리스트)를 혼자 구현했고, 2026년 리팩토링과 성능 평가도 혼자 진행했습니다.

부정확하게 기억나는 가사를 말하거나 입력하면 J-POP 곡을 찾아 주고, 비슷한 곡을 추천해 Spotify 플레이리스트로 만들어 주는 서비스입니다. 가사 없는 콧노래로는 찾지 않습니다.

- **음성 검색**: Whisper(STT)로 받아 적은 가사를 SentenceTransformer 임베딩과 FAISS 로 검색합니다. 곡을 찾는 단계에는 LLM 을 쓰지 않습니다.
- **평가와 개선**: 곡 식별 단계만 떼어 합성 질의·TTS 음성으로 쟀습니다(실사용 정확도는 아님). 한국인 발음 음성은 Whisper 가 35% 를 한국어로 받아 적는 문제를 찾아, 일본어 재전사와 줄 단위 조각 투표를 넣은 뒤 **36% → 69%**, 원어민 5줄 음성은 47% → 74% 가 됐습니다.
- **플레이리스트 문구와 구조**: 검색된 곡의 요약·태그로 GPT-3.5 가 플레이리스트 제목·설명을 쓰고, Spotify OAuth 로 계정에 저장합니다. Hugging Face Space 프로토타입을 Angular 17 + FastAPI 로 나눠 다시 만들었습니다(배포는 다음 단계).

---

### 🚧 개발 중

- **[한국어 화자를 위한 일본어 작문 코치](https://github.com/fairyofdata/PragmaticsKR2JP)** · `PragmaticsKR2JP` · 2026.09 – · 개인  
  일본어 글이 어디가 틀렸고 그 장면·상대에게 무엇이 적절한지 알려주는 개인용 코치입니다. LLM은 고정된 오류 분류표 안에서 위치와 유형만 붙이고, 인용 원문 대조·3회 채점 다수결·집계는 코드가 하며, 그 주석의 재현성과 탐지율을 재서 공개합니다.
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
