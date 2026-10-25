**🌐 Available Versions:** [🇺🇸 English](./README.md) | [🇰🇷 한국어 (Korean)](./README_KR.md) | [🇯🇵 日本語 (Japanese)](./README_JP.md)  

---

# Hi there! 👋

I'm **Jiheon Baek**, an Applied AI engineer living under the famously sunny skies of Okayama, Japan.

I specialize in Natural Language Processing (NLP), LLM applications, and workflow automation —
with a strong focus on building **LLM and machine-learning systems** and evaluating them reproducibly, so they keep delivering value under real-world operational constraints.

Currently deepening my expertise in **production-grade LLM architectures**, **document-centric workflow automation**, and **practical AI systems design**.

📧 **Email** : fairyofdata@gmail.com  
💼 **LinkedIn** : https://www.linkedin.com/in/hjbaek/

---

## 🎯 Focus

- 🤖 LLM applications & AI engineering
- 📏 Reproducible evaluation of ML and LLM systems
- 💬 NLP & document-centric information extraction
- ⚙️ MLOps & production-grade AI systems

---

## 💻 Tech Stack

**ML & Speech**  
<img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"> <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"> <img src="https://img.shields.io/badge/Transformers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black"> <img src="https://img.shields.io/badge/Whisper-412991?style=for-the-badge&logo=openai&logoColor=white"> <img src="https://img.shields.io/badge/Wav2Vec2-0467DF?style=for-the-badge&logo=meta&logoColor=white">

**LLM & Retrieval**  
<img src="https://img.shields.io/badge/OpenAI_API-74AA9C?style=for-the-badge&logo=openai&logoColor=white"> <img src="https://img.shields.io/badge/Gemini_API-4285F4?style=for-the-badge&logo=google&logoColor=white"> <img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white"> <img src="https://img.shields.io/badge/FAISS-0467DF?style=for-the-badge&logo=meta&logoColor=white">

**Web & API**  
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">

**Databases**  
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white"> <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white">

**Infrastructure & Tooling**  
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"> <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=white"> <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white"> <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white">

---

## 🗂️ Projects

### ⭐ Featured

---

#### 🧑‍🏫 [PhonemeJP2KR — Phoneme-level Korean Pronunciation Coaching for Japanese Speakers](https://github.com/fairyofdata/PhonemeJP2KR)
> `Python` `Streamlit` `Whisper` `Wav2Vec2` `Gemini` `G2P`

A CAPT (Computer-Assisted Pronunciation Training) web application designed to help Japanese native speakers identify and correct Korean pronunciation errors at the phoneme level. Developed by expanding the ASR (Whisper) and speech-processing pipelines refined during [Songfinder](https://github.com/fairyofdata/RAGSTT4Lyrics), the voice search module I built in the award-winning team project URFIT.

- **Dual-ASR Architecture**: Measures the divergence between Whisper (strong internal LM — approximates intelligibility) and Wav2Vec2-CTC (no LM — captures raw acoustics) to surface the precise pronunciation gap that learners cannot hear in themselves.
- **Deterministic G2P Engine**: Implements Standard Korean phonological rules (7-coda neutralization, liaison, nasalization, aspiration, etc.) as a pure-Python pipeline — no external dependencies, no hallucinations, and fully reproducible scores.
- **L1 Interference Classifier**: A rule-based tagger grounded in Contrastive Phonology research (Jang 2016, etc.) that systematically diagnoses 6 typical error types specific to Japanese speakers (vowel epenthesis, coda deletion, laryngeal confusion, etc.). The LLM (Gemini) receives only structured evidence tags — it never computes measurements.
- **Empirical Validation**: Validated through 6 reproducible experiments — including real Japanese-accented speech (AI-Hub L2 corpus, 615 clips / 198 speakers: AUC 0.818 separating high- vs low-rated speech, ρ = 0.473 vs human ratings, outperforming the classic GOP baseline on every axis), Spearman ρ = −0.702 (score-severity correlation), and 100% G2P accuracy on held-out rule sets (51/51 context-free, 17/17 morphology-conditioned).

---

#### 📊 [PortfolioOpt4ESG — LLM-based ESG-Focused Portfolio Optimization Service](https://github.com/fairyofdata/PortfolioOpt4ESG)
> `Python` `Streamlit` `KoELECTRA` `GPT-3.5` `Black-Litterman` `KOSPI`

🏆 Excellence Award — 8th Industry-Academia SW Project Exhibition, Kwangwoon University  
🏆 Excellence Award — 2024 Graduation Exhibition, Kwangwoon University  
📄 Co-authored paper (2nd author) published in *Computational Economics* (Springer, 2026) — [doi:10.1007/s10614-026-11413-9](https://doi.org/10.1007/s10614-026-11413-9)

A research-grade system that derives transparent ESG scores directly from news text using fine-tuned Korean NLP models, then feeds those scores into a Black-Litterman portfolio optimizer as investor views.

- **Data Pipeline**: Crawled **1.38M news articles** for 68 KOSPI companies (2019–2023), bootstrapped labels with GPT-3.5, and fine-tuned a cascade of 6 KoELECTRA classifiers (relevance filtering → sentiment → ESG scoring → pillar classification).
- **Portfolio Optimization**: A 15-question survey maps user values onto a pillar-by-agency preference matrix, which is injected into Black-Litterman as P/Q views. Final weights maximize the Sharpe ratio under Ledoit-Wolf shrinkage covariance.
- **Backtesting**: Annual rebalancing over 2020–2024 shows **the optimized ESG portfolio (Sharpe 0.499, max drawdown 0.187)** outperforming KOSPI (0.190) and ESG ETF (0.251) on every metric.

---

#### 🎵 [Songfinder — Speech-driven J-POP Search & Playlist Generation](https://github.com/fairyofdata/RAGSTT4Lyrics)
> `Python` `FastAPI` `Angular` `Whisper` `FAISS` `SentenceTransformer` `Spotify API`

🏆 Excellence Award (team) — KITA SCIT Master 47th Cohort Project Presentation, for the 6-person team project URFIT  
👤 My module in URFIT: I built the voice-and-music matching part — STT → FAISS retrieval → recommendation → Spotify playlist — on my own, and refactored it solo in 2026.

A service that finds J-POP songs from vague lyrics or humming, then builds a Spotify playlist with AI-generated title and description — targeting the gap between "I know this song" and being able to search for it.

- **Multimodal Search Pipeline**: Whisper (STT) converts voice input to text; SentenceTransformer embeddings + FAISS index run vector similarity search across a lyrics dataset to retrieve the best-matching tracks.
- **AI Playlist Generation**: GPT-3.5 analyzes the retrieved tracks and generates a creative playlist title and description, then saves it directly to the user's Spotify account via OAuth API.
- **Architecture Refactor**: Migrated from a Hugging Face Space monolith to a clean microservice architecture (Angular 17+ frontend / FastAPI backend), enabling flexible deployment to Firebase Hosting, Cloud Run, and beyond.

---

### 🚧 In Progress

- **[A Japanese writing coach for Korean speakers](https://github.com/fairyofdata/PragmaticsKR2JP)** · `PragmaticsKR2JP` · Sep 2026 –, solo  
  The LLM only tags where each error is and what type it is, against a fixed taxonomy; quote checks, majority voting over three gradings and the counting all run in code.
- **[A cascading DLP layer with a local model as the gate](https://github.com/fairyofdata/CascadeDLP)** · `CascadeDLP` · Sep 2026 –, solo  
  A local model reads each document before it reaches a cloud LLM and rules on it — pass, mask, ask the user, local only, or block. Built for documents mixing Korean, Japanese and English, and used as MCP tools.

---

### 📁 Earlier Projects

- **[Neutral article synthesis from Korean and Japanese coverage](https://github.com/fairyofdata/Neutralize4KRJP)** · `Neutralize4KRJP` · 2024, solo  
  Pairs JoongAng Ilbo and Yomiuri Shimbun reporting on the same issue and writes one bilingual article that separates shared facts from differences in emphasis, with Pydantic-validated structured outputs. Built on the SW021 *ChatGPT for Business* program at Sungshin Women's University.
- **[Smishing detection with a three-model ensemble](https://github.com/fairyofdata/AntiPhishingNLP)** · `AntiPhishingNLP` · 2023, team of 5 · 🥇 KISA Cybersecurity AI·Big Data Challenge Track C (1st)  
  KoBERT, KoELECTRA and Att-BiLSTM soft-voted on SMS text (voice phishing is a separate demo). My part: the Att-BiLSTM design and implementation, the soft-voting strategy, SMOTE and the inference module. A team project at the HUFS Data Youth Campus.
- **[Detecting disguised profanity at the jamo level](https://github.com/fairyofdata/SepticFilterNLP)** · `SepticFilterNLP` · 2022, team of 6 · 🥇 Samsung SDS Multicampus Big Data Contest (1st)  
  Catches profanity hidden by separated characters or inserted symbols. My part: crawling (56,000+ comments), the MySQL schema, the data pipeline and Django integration.

---

## 📚 Education & Training

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
