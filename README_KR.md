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
- **L1 간섭 오류 분류기**: 일본어 모어 화자에게서 체계적으로 나타나는 모음 삽입, 받침 탈락, 3지대립 붕괴 등 6가지 오류 유형을 규칙 기반으로 태깅하고, LLM(Gemini)은 진단된 구조화된 증거만을 받아 카타카나 시각화와 코칭 피드백만 담당합니다.
- **실증 검증**: Spearman ρ = −0.702, G2P 정확도 100%(51/51, held-out) 등 4가지 재현 가능한 실험으로 시스템 유효성을 검증했습니다.

---

#### 📊 LEPOS — LLM 기반 ESG 중심 포트폴리오 최적화 서비스
> `Python` `Streamlit` `KoELECTRA` `GPT-3.5` `Black-Litterman` `KOSPI`

🏆 광운대학교 제8회 산학협력 SW 프로젝트 **우수상** · 정보융합학과 졸업전시회 **우수상**

한국 상장 기업의 뉴스 텍스트를 LLM 및 파인튜닝 모델로 직접 분석하여 투명한 ESG 점수를 산출하고, 이를 Black-Litterman 모델의 투자자 뷰로 반영해 맞춤형 포트폴리오를 구성하는 연구/서비스 시스템입니다.

- **데이터 파이프라인**: KOSPI 68개사의 뉴스 **138만 건**을 수집하고, GPT-3.5로 라벨 부트스트래핑 후 KoELECTRA를 파인튜닝해 6단계 분류/회귀 모델 캐스케이드를 구축했습니다.
- **포트폴리오 최적화**: 사용자 설문(15문항)이 E/S/G 선호를 에이전시별 방법론 가중치로 변환되며, 이를 Black-Litterman 뷰(P, Q)로 주입 후 Ledoit-Wolf shrinkage 공분산 기반 최대 샤프 비율 최적화를 수행합니다.
- **백테스팅**: 2020~2024년 연간 리밸런싱 기준으로 KOSPI(Sharpe 0.190), ESG ETF(0.251) 대비 **LEPOS(0.503, 최대 낙폭 0.187)**가 모든 지표에서 우세함을 증명했습니다.

---

#### 🔮 OmikuZ — 세계관 확장형 AI 오미쿠지(점괘) 서비스
> `Python` `FastAPI` `React` `Vite` `SQLAlchemy` `OpenAI` `PWA`

다양한 '세계관(Spot)'을 여행하며 해당 세계관의 캐릭터 AI에게 점괘 심층 해석을 받을 수 있는 모바일 최적화 웹앱입니다.

- **비용 최적화 아키텍처**: 점괘 원문은 DB 마스터 데이터에서 캐싱 반환하고, 20시간마다 충전되는 토큰(Lazy Evaluation)을 소모할 때에만 LLM 심층 해석 API를 호출하여 비용을 최소화합니다.
- **무한 확장 구조**: 신규 세계관 추가 시 백엔드 코드 배포 없이 DB의 `theme_metadata(JSON)` 필드에 시스템 프롬프트와 테마 색상만 주입하면 즉시 반영됩니다.
- **구조화된 LLM 응답**: Pydantic JSON 스키마로 LLM 응답을 강제 파싱하여 프론트엔드 렌더링 안정성을 확보했습니다.
- **몰입형 UX**: 타임록 기반 워프 게이지, 산통 흔들기 인터랙션, Typewriter 효과 등 PWA 환경에서 네이티브 수준의 마이크로 인터랙션을 구현했습니다.

---

#### 🎵 URFIT — 음성인식 기반 AI J-POP 플레이리스트 커뮤니티
> `Python` `FastAPI` `Angular` `Whisper` `FAISS` `SentenceTransformer` `Spotify API`

🏆 한국무역협회 SCIT Master 47기 프로젝트 발표회 **우수상**

"대충 아는 가사"나 흥얼거림만으로 원하는 J-POP을 찾고, AI가 취향 기반 유사 곡 추천 및 Spotify 플레이리스트를 자동 생성해주는 커뮤니티 서비스입니다.

- **멀티모달 검색**: Whisper(STT)로 음성을 텍스트로 변환 후, SentenceTransformer 임베딩과 FAISS 인덱스로 가사 데이터셋을 벡터 유사도 검색합니다.
- **AI 플레이리스트 생성**: 검색 결과를 GPT-3.5가 분석해 창의적인 플레이리스트 제목/설명을 자동 생성하고, Spotify OAuth API로 사용자 계정에 직접 저장합니다.
- **아키텍처 리팩토링**: Hugging Face Space 기반 프로토타입을 Angular 17+(Frontend) + FastAPI(Backend) 마이크로서비스 아키텍처로 완전 분리하여 Firebase, Cloud Run 등 다양한 클라우드 환경 배포에 대응했습니다.

---

### 🛠️ 개인 도구

---

#### 💰 Accountant — AI 기반 지능형 가계부 대시보드
> `Angular 21` `Firebase` `Firestore` `PWA` `OpenAI` `Signals`

단순 지출 기록을 넘어, 데이터 정제 · 다차원 교차 시각화 · AI 재무 컨설팅을 결합한 개인 재무 분석 대시보드입니다. (엔화 기준)

- **독자적 도메인 설계**: 지출을 '통제 가능성'에 따라 [정기 / 생활 / 문화 / 사회 / 인프라] 5대 분류로 나누고, AI 브리핑은 통제 가능 변동비(생활+문화+사회)만을 집중 분석합니다.
- **AI 영수증 스캐너**: `gpt-4o-mini` 비전 모델이 영수증 이미지에서 날짜·금액·지출처를 추출하며, 기존 분류 체계를 프롬프트에 동적 주입하여 환각을 방지합니다.
- **OLS 회귀 기반 지출 예측**: 완료된 과거 기간만을 사용한 단순 선형회귀로 다음 기간 지출을 예측하고, 비반복성 outlier(이사 초기비용 등)를 자동 제외합니다.
- **PWA + 오프라인 동기화**: Angular Service Worker + Dexie(IndexedDB) 로컬 캐시 + 오프라인 변경 큐로 네트워크 단절 시에도 조회·입력이 가능하고, 온라인 복귀 시 자동 동기화됩니다.

---

#### 🎵 Archetier — 음반 수집 관리 대시보드
> `Angular 17+` `Firebase Hosting` `ngx-charts` `Signals`

개인 음반 수집 내역을 체계적으로 관리하고 시각화하는 대시보드입니다.

- **지능형 교차 필터링**: 테이블 행 클릭 시 해당 조건으로 차트와 상세 내역이 즉시 필터링되며, 필터 상태에 따라 장르별 비중 파이 차트가 아티스트별 드릴다운 차트로 자동 전환됩니다.
- **반응형 UI**: 데스크탑에서는 강력한 테이블 그리드, 모바일에서는 터치 친화적 아코디언 뷰로 자동 전환되며 입수/발매일과 가격 프리미엄을 뱃지(Badge) 형태로 시각화합니다.

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
