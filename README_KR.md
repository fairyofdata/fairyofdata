# 안녕하세요! 👋

맑은 하늘의 오카야마에서 소프트웨어 엔지니어로 근무하고 있는 **백지헌**입니다.

LLM Application, Machine Learning, NLP, AI Engineering에 관심이 있으며,
AI를 실제 서비스와 업무에 적용하는 개발을 지향합니다.

현재는 **LLM 기반 애플리케이션**, **AI 자동화**, **MLOps**, **Machine Learning**을 중심으로 역량을 쌓으며 ML Engineer를 목표로 성장하고 있습니다.

📧 **Email** : fairyofdata@gmail.com  
💼 **LinkedIn** : https://www.linkedin.com/in/hjbaek/

---

## 🚀 Interests

- 🤖 LLM Applications
- 🧠 Machine Learning & Deep Learning
- 💬 Natural Language Processing (NLP)
- ⚙️ AI Engineering
- ☁️ MLOps
- 📝 Prompt Engineering

---

## 💻 Tech Stack

### AI / Machine Learning
<p>
  <img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white">
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white">
  <img src="https://img.shields.io/badge/HuggingFace-FDEE21?style=for-the-badge&logo=HuggingFace&logoColor=black">
  <img src="https://img.shields.io/badge/OpenAI_API-74AA9C?style=for-the-badge&logo=openai&logoColor=white">
  <img src="https://img.shields.io/badge/Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white">
</p>

### Frontend
<p>
  <img src="https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white">
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
</p>

### Backend / Database
<p>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white">
  <img src="https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black">
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white">
  <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white">
</p>

### Data Science
<p>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white">
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge">
  <img src="https://img.shields.io/badge/FAISS-0467DF?style=for-the-badge&logo=meta&logoColor=white">
</p>

### Tools
<p>
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white">
  <img src="https://img.shields.io/badge/Google_Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=black">
  <img src="https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white">
</p>

---

## 🗂️ Projects

### 🔬 개인 연구 / 서비스 프로젝트

---

#### 🧑‍🏫 Phomene — 일본인 학습자를 위한 음소 단위 한국어 발음 코칭
> `Python` `Streamlit` `Whisper` `Wav2Vec2` `Gemini` `G2P`

일본어 모어 화자가 한국어 발음을 교정할 수 있도록 설계된 CAPT(Computer-Assisted Pronunciation Training) 웹 애플리케이션입니다.

- **듀얼 ASR 아키텍처**: 언어모델이 내장된 Whisper(지능적 오류 보정)와 언어모델이 없는 Wav2Vec2-CTC(물리적 발성 포착)의 차이를 측정하여 학습자 스스로 인지하지 못하는 발음 오류를 수치화합니다.
- **결정론적 G2P 엔진**: 표준발음법(7종성, 연음, 비음화, 격음화 등) 규칙을 순수 Python으로 직접 구현하여 LLM 환각을 원천 차단하고 동일 입력에 대해 항상 동일한 점수를 보장합니다.
- **L1 간섭 오류 분류기**: 대조음운론 연구(장향실 2016 등)에 학술적 근거를 둔 규칙 기반 태거로, 일본어 모어 화자에게서 체계적으로 나타나는 모음 삽입, 받침 탈락, 3지대립 붕괴 등 6가지 오류 유형을 진단합니다. LLM(Gemini)은 진단된 구조화된 증거만을 받아 카타카나 시각화와 코칭 피드백만 담당합니다.
- **실증 검증**: Spearman ρ = −0.702, G2P 정확도 100%(51/51, held-out) 등 4가지 재현 가능한 실험으로 시스템 유효성을 검증했습니다.

---

#### 🎵 URFIT — 음성인식 기반 AI J-POP 플레이리스트 커뮤니티
> `Python` `FastAPI` `Angular` `Whisper` `FAISS` `SentenceTransformer` `Spotify API`

🏆 한국무역협회 SCIT Master 47기 프로젝트 발표회 **우수상**

"대충 아는 가사"나 흥얼거림만으로 원하는 J-POP을 찾고, AI가 취향 기반 유사 곡 추천 및 Spotify 플레이리스트를 자동 생성해주는 커뮤니티 서비스입니다.

- **멀티모달 검색**: Whisper(STT)로 음성을 텍스트로 변환 후, SentenceTransformer 임베딩과 FAISS 인덱스로 가사 데이터셋을 벡터 유사도 검색합니다.
- **AI 플레이리스트 생성**: 검색 결과를 GPT-3.5가 분석해 창의적인 플레이리스트 제목/설명을 자동 생성하고, Spotify OAuth API로 사용자 계정에 직접 저장합니다.
- **아키텍처 리팩토링**: Hugging Face Space 기반 프로토타입을 Angular 17+(Frontend) + FastAPI(Backend) 마이크로서비스 아키텍처로 완전 분리하여 Firebase, Cloud Run 등 다양한 클라우드 환경 배포에 대응했습니다.

---

#### 📊 LEPOS — LLM 기반 ESG 중심 포트폴리오 최적화 서비스
> `Python` `Streamlit` `KoELECTRA` `GPT-3.5` `Black-Litterman` `KOSPI`

🏆 광운대학교 제8회 산학협력 SW 프로젝트 **우수상** · 정보융합학과 졸업전시회 **우수상**

한국 상장 기업의 뉴스 텍스트를 LLM 및 파인튜닝 모델로 직접 분석하여 투명한 ESG 점수를 산출하고, 이를 Black-Litterman 모델의 투자자 뷰로 반영해 맞춤형 포트폴리오를 구성하는 연구/서비스 시스템입니다.

- **데이터 파이프라인**: KOSPI 68개사의 뉴스 **138만 건**을 수집하고, GPT-3.5로 라벨 부트스트래핑 후 KoELECTRA를 파인튜닝해 6단계 분류/회귀 모델 캐스케이드를 구축했습니다.
- **포트폴리오 최적화**: 사용자 설문(15문항)이 E/S/G 선호를 에이전시별 방법론 가중치로 변환되며, 이를 Black-Litterman 뷰(P, Q)로 주입 후 Ledoit-Wolf shrinkage 공분산 기반 최대 샤프 비율 최적화를 수행합니다.
- **백테스팅**: 2020~2024년 연간 리밸런싱 기준으로 KOSPI(Sharpe 0.190), ESG ETF(0.251) 대비 **LEPOS(0.503, 최대 낙폭 0.187)**가 모든 지표에서 우세함을 증명했습니다.

---

#### 🛡️ AntiPhishingNLP — NLP 기반 피싱 탐지 서비스
> `Python` `KoBERT` `KoELECTRA` `Att-BiLSTM` `Django` `STT`

🏆 2023 한국인터넷진흥원(KISA) 사이버보안 AI·빅데이터 챌린지 Track C — **최우수상 (1위)**

스미싱 문자 텍스트와 보이스피싱 음성 탐지를 이중으로 처리하는 NLP 기반 피싱 감지 시스템입니다. 한국외국어대학교 데이터청년캠퍼스 팀 프로젝트입니다.

- **3중 앙상블 분류기**: KoBERT(양방향 문맥 이해) + KoELECTRA(토큰 적합성 판별) + Att-BiLSTM(MeCab 형태소 분석 + Attention) 세 모델의 소프트보팅으로 일반화와 도메인 특화 능력을 모두 확보합니다.
- **이중 입력 채널**: 스미싱 문자는 직접 텍스트로 투입하고, 보이스피싱 음성은 Django Web Speech API로 실시간 STT 변환 후 동일 파이프라인에 투입합니다.
- **클래스 불균형 대응**: KorCCViD 데이터셋에 SMOTE 오버샘플링을 적용하여 피싱/정상 클래스 불균형을 해소합니다.
- **담당 파트 (백지헌)**: Att-BiLSTM 아키텍처 설계, 앙상블 보팅 전략, KorCCViD 데이터셋 정제 및 SMOTE 파이프라인, 텍스트 분류 추론 모듈 개발.

---

#### 🛡️ SepticFilterNLP — 딥러닝 알고리즘 기반 욕설 감지 필터
> `Python` `FastText` `CNN` `LSTM` `Django` `MySQL`

🏆 삼성SDS 멀티캠퍼스 빅데이터 활용 공모전 — **최우수상 (1위)**

기존 형태소 기반 필터가 잡아내지 못하는 교묘하게 우회된 욕설(자모 분리, 특수문자 삽입 등)을 감지하기 위해 개발된 딥러닝 필터입니다.

- **듀얼 토큰화 및 앙상블**: 자모 단위 분리 토크나이저를 직접 설계하고, 3개의 모델(FastText LSTM, Jamo LSTM, Jamo CNN)을 소프트 보팅으로 앙상블하여 93.7%의 정확도를 달성했습니다.
- **데이터 엔지니어링**: 봇 차단(IP 밴, User-Agent 필터링)을 우회하는 랜덤 페이싱 스크래핑 파이프라인을 구축하여 56,000개 이상의 실제 커뮤니티 댓글 데이터를 수집했습니다.
- **풀스택 배포**: Django 기반 REST API와 웹 인터페이스를 개발하여 실시간 추론 결과를 제공하고, MySQL 데이터베이스에 예측 로그를 영구 저장했습니다.

---

## 📚 Experience

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

---

## 🎯 Current Focus

- LLM Application Development
- AI Automation
- Machine Learning
- MLOps
- Building practical AI services
