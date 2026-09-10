**🌐 Available Versions:** [🇺🇸 English](./README.md) | [🇰🇷 한국어 (Korean)](./README_KR.md) | [🇯🇵 日本語 (Japanese)](./README_JP.md)  

---

# Hi there! 👋

I'm **Jiheon Baek**, a software engineer living under the famously sunny skies of Okayama, Japan.

I specialize in Natural Language Processing (NLP), LLM applications, and workflow automation —
with a strong focus on engineering **Applied AI and Forward-Deployed AI solutions** that create measurable business impact under real-world operational constraints.

Currently deepening my expertise in **production-grade LLM architectures**, **document-centric workflow automation**, and **practical AI systems design**.

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

### 🤖 LLM & AI Engineering Projects

---

#### 🧑‍🏫 [PhonemeJP2KR — Phoneme-level Korean Pronunciation Coaching for Japanese Speakers](https://github.com/fairyofdata/PhonemeJP2KR)
> `Python` `Streamlit` `Whisper` `Wav2Vec2` `Gemini` `G2P`

A CAPT (Computer-Assisted Pronunciation Training) web application designed to help Japanese native speakers identify and correct Korean pronunciation errors at the phoneme level. Developed by expanding the ASR (Whisper) and speech-processing pipelines refined during the award-winning project (URFIT - SCIT Master Excellence Award).

- **Dual-ASR Architecture**: Measures the divergence between Whisper (strong internal LM — approximates intelligibility) and Wav2Vec2-CTC (no LM — captures raw acoustics) to surface the precise pronunciation gap that learners cannot hear in themselves.
- **Deterministic G2P Engine**: Implements Standard Korean phonological rules (7-coda neutralization, liaison, nasalization, aspiration, etc.) as a pure-Python pipeline — no external dependencies, no hallucinations, and fully reproducible scores.
- **L1 Interference Classifier**: A rule-based tagger grounded in Contrastive Phonology research (Jang 2016, etc.) that systematically diagnoses 6 typical error types specific to Japanese speakers (vowel epenthesis, coda deletion, laryngeal confusion, etc.). The LLM (Gemini) receives only structured evidence tags — it never computes measurements.
- **Empirical Validation**: Validated through 6 reproducible experiments — including real Japanese-accented speech (AI-Hub L2 corpus, 615 clips / 198 speakers: AUC 0.818 separating high- vs low-rated speech, ρ = 0.473 vs human ratings, outperforming the classic GOP baseline on every axis), Spearman ρ = −0.702 (score-severity correlation), and 100% G2P accuracy on held-out rule sets (51/51 context-free, 17/17 morphology-conditioned).

---

#### 📊 [LLM_ESG_POS — LLM-based ESG-Focused Portfolio Optimization Service](https://github.com/fairyofdata/LLM_ESG_POS)
> `Python` `Streamlit` `KoELECTRA` `GPT-3.5` `Black-Litterman` `KOSPI`

🏆 Excellence Award — 8th Industry-Academia SW Project Exhibition, Kwangwoon University  
🏆 Excellence Award — 2024 Graduation Exhibition, Kwangwoon University

A research-grade system that derives transparent ESG scores directly from news text using fine-tuned Korean NLP models, then feeds those scores into a Black-Litterman portfolio optimizer as investor views.

- **Data Pipeline**: Crawled **1.38M news articles** for 68 KOSPI companies (2019–2023), bootstrapped labels with GPT-3.5, and fine-tuned a cascade of 6 KoELECTRA classifiers (relevance filtering → sentiment → ESG scoring → pillar classification).
- **Portfolio Optimization**: A 15-question survey maps user values onto a pillar-by-agency preference matrix, which is injected into Black-Litterman as P/Q views. Final weights maximize the Sharpe ratio under Ledoit-Wolf shrinkage covariance.
- **Backtesting**: Annual rebalancing over 2020–2024 shows **LEPOS (Sharpe 0.503, max drawdown 0.187)** outperforming KOSPI (0.190) and ESG ETF (0.251) on every metric, with the ESG signal's contribution isolated to risk reduction via ablation.

---

#### 🎵 [LLM_STT_Songfinder — STT-Based AI J-POP Playlist Community](https://github.com/fairyofdata/LLM_STT_Songfinder)
> `Python` `FastAPI` `Angular` `Whisper` `FAISS` `SentenceTransformer` `Spotify API`

🏆 Excellence Award — KITA SCIT Master 47th Cohort Project Presentation

A service that finds J-POP songs from vague lyrics or humming, then builds a Spotify playlist with AI-generated title and description — targeting the gap between "I know this song" and being able to search for it.

- **Multimodal Search Pipeline**: Whisper (STT) converts voice input to text; SentenceTransformer embeddings + FAISS index run vector similarity search across a lyrics dataset to retrieve the best-matching tracks.
- **AI Playlist Generation**: GPT-3.5 analyzes the retrieved tracks and generates a creative playlist title and description, then saves it directly to the user's Spotify account via OAuth API.
- **Architecture Refactor**: Migrated from a Hugging Face Space monolith to a clean microservice architecture (Angular 17+ frontend / FastAPI backend), enabling flexible deployment to Firebase Hosting, Cloud Run, and beyond.

---

#### ⚖️ [LLM_NAKOJA — LLM-based Korea-Japan Relations Neutral Article Generator](https://github.com/fairyofdata/LLM_NAKOJA)
> `Python` `OpenAI (GPT-4o-mini)` `Pydantic Structured Outputs` `Selenium` `Streamlit` `Pytest`

A cross-border AI journalism pipeline that cross-analyzes news reporting on identical bilateral issues from both Korean (JoongAng Ilbo) and Japanese (Yomiuri Shimbun) media, stripping nationalistic framing bias to **automatically synthesize balanced, neutral articles in both Korean and Japanese**.

- **L1 Framing Bias Elimination Architecture**: To eliminate implicit nationalistic framing and emotional undertones, the system employs **English as an intermediate lingua franca** to distill verifiable facts and subjective claims before synthesizing the final bilingual article.
- **Pydantic Structured Outputs**: Employs OpenAI's latest structured parsing to eliminate regex parsing errors completely and systematically extract a 'Perspective Contrast Matrix' (shared facts, Korean emphasis, Japanese emphasis, framing divergence).
- **Clean Architecture & Full Verification**: Decoupled crawler, pure LLM pipeline, and Streamlit presentation layers backed by a comprehensive unit test suite (10/10 Passed with pytest and mock clients).

---

#### 🛡️ [AntiPhishingNLP — NLP-based Phishing Detection Service](https://github.com/fairyofdata/AntiPhishingNLP)
> `Python` `KoBERT` `KoELECTRA` `Att-BiLSTM` `Django` `STT`

🏆 Grand Prize (1st) — 2023 KISA Cybersecurity AI·Big Data Challenge Track C

A dual-channel phishing detection system combining SMS phishing (smishing) text classification and real-time voice phishing (vishing) detection via STT — built as a team project at Hankuk University of Foreign Studies Data Youth Campus.

- **Triple Ensemble Classifier**: KoBERT (bidirectional context), KoELECTRA (token replacement detection), and Att-BiLSTM with MeCab tokenizer are soft-voted to cover both generalized and domain-specific phishing patterns.
- **Dual Input Channels**: Text messages are fed directly; voice calls are transcribed to text in real-time via the browser's Web Speech API and sent to the Django backend to route through the same classification pipeline.
- **Class Imbalance Handling**: SMOTE oversampling applied on the KorCCViD dataset to address severe phishing/normal class skew.
- **Contribution (Jiheon Baek)**: Att-BiLSTM architecture design, ensemble voting strategy, KorCCViD dataset cleansing and SMOTE pipeline, text classification inference module.

---

#### 🛡️ [SepticFilterNLP — Deep Learning Algorithm-based Profanity Detection Filter](https://github.com/fairyofdata/SepticFilterNLP)
> `Python` `FastText` `CNN` `LSTM` `Django` `MySQL`

🏆 Grand Prize (1st) — Samsung SDS Multi-Campus Big Data Challenge

A deep learning filter developed to detect circumvented profanity (e.g., character separation, special symbol insertion) that traditional morpheme-based detectors fail to identify.

- **Dual-Tokenization & Ensemble (team)**: The team built a character-level Jamo decomposition tokenizer and a Soft-Voting Ensemble of FastText LSTM, Jamo LSTM, and Jamo CNN (best single model: Jamo CNN, 93.7% accuracy).
- **Data Engineering**: Built a multi-community crawler (Selenium + BeautifulSoup, with IP-ban evasion) that collected 56,000+ community comments, and designed the MySQL schema and ingestion pipeline.
- **Full-stack Deployment**: Integrated the model-serving API with the Django backend and web interface, persisting prediction logs to MySQL.
- **Contribution (Jiheon Baek)**: Crawling, MySQL schema & data pipeline, Django service integration, labeling.

---

## 📚 Experience

- **B.S. in Information Convergence (Data Science)** [@Kwangwoon University](https://ic.kw.ac.kr:501/program/process.php)  
- **K-Digital Training**: Data Science Track [@Multicampus (Samsung SDS)](https://www.multicampus.com/em/enrolment/courseDetai?p_menu=NzUjU1VC&p_gubun=Qw==&corsCd=FA00NM)  
- **LG Aimers**: Data Intelligence Program [@LG AI Research](https://lgresearch.ai/news/view?seq=488)  
- **Data Youth Campus**: Natural Language Processing Track [@Hankuk University of Foreign Studies](https://ime.hufs.ac.kr/bbs/ime/509/71087/artclView.do)  
- **SW021**: ChatGPT for Business [@Sungshin Women's University](https://m.dhnews.co.kr/news/view/1065594826213812)  
- **ACC Korea**: AWS Official University Community — 1st Cohort Member [@AWS Korea](https://www.awscloudclubs.kr/)  
- **SCIT Master**: Japan IT Career Placement Program [@Korea International Trade Association](https://newtradecampus.kita.net/page/user_job_CloudIT_courseguide_outline)  

---

## 🏆 Awards

- 🥇 **Samsung SDS Multicampus Big Data Utilization Contest** (Multicampus, 2022) — **Grand Prize (1st)**  
- 🥇 **KISA Cybersecurity AI·Big Data Challenge Track C** (KISA, 2023) — **Grand Prize (1st)**  
- 🥈 **Kwangwoon University 8th Industry-Academia SW Project Exhibition** (KWU, 2024) — **Excellence Award (2nd)**  
- 🥈 **Kwangwoon University Dept. of Information Convergence Graduation Exhibition** (KWU, 2024) — **Excellence Award (2nd)**  
- 🥈 **KITA SCIT Master 47th Cohort Project Presentation** (KITA, 2025) — **Excellence Award (2nd)**  

---

## 🎯 Current Focus

- Applied AI & Forward-Deployed AI Engineering
- LLM Application & Workflow Automation
- Document-centric Information Extraction & NLP
- Building robust, production-grade AI systems
