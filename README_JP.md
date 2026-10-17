**🌐 Available Versions:** [🇺🇸 English](./README.md) | [🇰🇷 한국어](./README_KR.md) | [🇯🇵 日本語](./README_JP.md)

---

# はじめまして！👋

**晴れの国・岡山**でソフトウェアエンジニアとして働いている**白知憲（ペク・ジホン）**です。

LLMアプリケーション、自然言語処理（NLP）、AIエンジニアリング、業務ワークフロー自動化に関心があり、
単なるデモにとどまらず、**LLM・機械学習システムを構築し、再現可能な評価によって現実の運用の中で価値を出し続けるAIエンジニア**を目指しています。

現在は**LLMベースのアプリケーション開発**、**業務プロセス・ドキュメントの自動化**、**実践的なAIソリューション設計**を中心にスキルを研鑽しています。

📧 **Email** : fairyofdata@gmail.com  
💼 **LinkedIn** : https://www.linkedin.com/in/hjbaek/

---

## 🎯 注力している領域

- 🤖 LLMアプリケーションとAIエンジニアリング
- 📏 機械学習・LLMシステムの再現可能な評価
- 💬 自然言語処理と文書からの情報抽出
- ⚙️ MLOpsと実運用に耐えるAIシステム

---

## 💻 技術スタック

**機械学習・音声**  
<img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"> <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white"> <img src="https://img.shields.io/badge/Transformers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black"> <img src="https://img.shields.io/badge/Whisper-412991?style=for-the-badge&logo=openai&logoColor=white"> <img src="https://img.shields.io/badge/Wav2Vec2-0467DF?style=for-the-badge&logo=meta&logoColor=white">

**LLM・検索**  
<img src="https://img.shields.io/badge/OpenAI_API-74AA9C?style=for-the-badge&logo=openai&logoColor=white"> <img src="https://img.shields.io/badge/Gemini_API-4285F4?style=for-the-badge&logo=google&logoColor=white"> <img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white"> <img src="https://img.shields.io/badge/FAISS-0467DF?style=for-the-badge&logo=meta&logoColor=white">

**Web・API**  
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"> <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">

**データベース**  
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white"> <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white">

**インフラ・開発環境**  
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"> <img src="https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazonwebservices&logoColor=white"> <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white"> <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white">

---

## 🗂️ プロジェクト

### ⭐ 主要プロジェクト

---

#### 🧑‍🏫 [PhonemeJP2KR — 日本語話者向け・音素レベルの韓国語発音コーチング](https://github.com/fairyofdata/PhonemeJP2KR)
> `Python` `Streamlit` `Whisper` `Wav2Vec2` `Gemini` `G2P`

日本語を母語とする学習者が韓国語の発音を矯正できるよう設計されたCAPT（Computer-Assisted Pronunciation Training）Webアプリケーションです。優秀賞を受賞したチームプロジェクトURFITで担当した音声検索モジュール（[Songfinder](https://github.com/fairyofdata/LLM_STT_Songfinder)）で確立したASR（Whisper）および音声処理パイプライン技術を拡張し、より高度な音素レベルの発音診断システムとして設計しました。

- **デュアルASRアーキテクチャ**: 言語モデルを内蔵したWhisper（知的誤り補正）と、言語モデルのないWav2Vec2-CTC（物理的発声の捕捉）の差分を測定することで、学習者自身が気づけない発音エラーを数値化します。
- **決定論的G2Pエンジン**: 標準発音法（7終声・連音・鼻音化・激音化など）のルールを純粋なPythonで直接実装し、LLMの幻覚（ハルシネーション）を根本から防ぎ、同一入力に対して常に同一スコアを保証します。
- **L1干渉エラー分類器**: 対照音韻論の研究（Jang 2016など）に学術的根拠を置いたルールベースのタガーで、日本語話者に体系的に現れる母音挿入・終声脱落・三項対立の崩壊など6種のエラーを診断します。LLM（Gemini）は構造化された証拠のみを受け取ってカタカナ可視化とコーチングフィードバックを担当します。
- **実証的検証**: 実際の日本語話者音声（AI-Hub L2コーパス、615発話・198名）で上位／下位評価の判別 AUC 0.818、人手評価との相関 ρ = 0.473 を示し、古典的な GOP ベースラインを全指標で上回りました。加えて Spearman ρ = −0.702（スコアと誤り重篤度の相関）、G2P精度100%（51/51・17/17、held-out）など、6つの再現可能な実験でシステムの有効性を検証しました。

---

#### 📊 [LLM_ESG_POS — LLMベースのESG重視ポートフォリオ最適化サービス](https://github.com/fairyofdata/LLM_ESG_POS)
> `Python` `Streamlit` `KoELECTRA` `GPT-3.5` `Black-Litterman` `KOSPI`

🏆 光云大学 第8回 産学協力SWプロジェクト **優秀賞** · 情報融合学科 卒業展示会 **優秀賞**  
📄 共著論文（第2著者）が *Computational Economics*（Springer, 2026）に掲載 — [doi:10.1007/s10614-026-11413-9](https://doi.org/10.1007/s10614-026-11413-9)

韓国上場企業のニューステキストをLLMおよびファインチューニング済みモデルで直接分析し、透明性の高いESGスコアを算出。これをBlack-Littermanモデルの投資家ビューとして反映し、パーソナライズされたポートフォリオを構成する研究/サービスシステムです。

- **データパイプライン**: KOSPI 68社のニュース**138万件**を収集し、GPT-3.5でラベルのブートストラッピングを行った後、KoELECTRAをファインチューニングして6段階の分類・回帰モデルのカスケードを構築しました。
- **ポートフォリオ最適化**: ユーザーアンケート（15問）がE/S/G選好をエージェンシー別手法の重みに変換され、Black-Littermanのビュー（P, Q）として注入後、Ledoit-Wolfシュリンケージ共分散に基づく最大シャープ比最適化を実施します。
- **バックテスト**: 2020〜2024年の年次リバランス基準で、KOSPI（Sharpe 0.190）・ESG ETF（0.251）対比、**最適化したESGポートフォリオ（0.499、最大ドローダウン 0.187）**が全指標で上回ることを実証しました。

---

#### 🎵 [Songfinder — 音声によるJ-POP検索とプレイリスト生成](https://github.com/fairyofdata/LLM_STT_Songfinder)
> `Python` `FastAPI` `Angular` `Whisper` `FAISS` `SentenceTransformer` `Spotify API`

🏆 韓国貿易協会 SCIT Master 47期 プロジェクト発表会 **優秀賞**（6名のチームプロジェクトURFITとして受賞）  
👤 URFITのうち、音声・音楽マッチングの部分（STT → FAISS検索 → 推薦 → Spotifyプレイリスト）を一人で実装し、2026年のリファクタリングも一人で行いました。

「なんとなく覚えている歌詞」や鼻歌だけで聴きたいJ-POPを探し出し、AIが好みに合った類似曲を推薦してSpotifyプレイリストを自動生成するコミュニティサービスです。

- **マルチモーダル検索**: Whisper（STT）で音声をテキストに変換後、SentenceTransformerの埋め込みとFAISSインデックスで歌詞データセットをベクトル類似度検索します。
- **AIプレイリスト生成**: 検索結果をGPT-3.5が分析してクリエイティブなプレイリストタイトルと説明を自動生成し、Spotify OAuth APIでユーザーのアカウントに直接保存します。
- **アーキテクチャのリファクタリング**: Hugging Face Spaceベースのプロトタイプを、Angular 17+（フロントエンド）＋ FastAPI（バックエンド）のマイクロサービスアーキテクチャに完全分離し、Firebase・Cloud Runなど多様なクラウド環境へのデプロイに対応しました。

---

### 🚧 開発中

- **[韓国語話者のための日本語作文コーチ](https://github.com/fairyofdata/PragmaticsKR2JP)** · `PragmaticsKR2JP` · 2026年9月 ～・個人  
  固定の誤り分類表に沿って、LLMは誤りの位置と種類だけを付けます。引用の原文照合、3回採点の多数決、集計はすべてコードが行います。
- **[ローカルモデルが関門に立つ、カスケード型DLPレイヤー](https://github.com/fairyofdata/CascadeDLP)** · `CascadeDLP` · 2026年9月 ～・個人  
  文書をクラウドのLLMに渡す前にローカルのモデルが読み、「通過・伏せて送信・利用者に確認・ローカルのみ・拒否」を判定します。韓国語・日本語・英語が混在する文書が対象で、MCPツールとして使います。

---

### 📁 その他のプロジェクト

- **[日韓の報道を比べて中立的な記事にまとめる](https://github.com/fairyofdata/LLM_NAKOJA)** · `LLM_NAKOJA` · 2024・個人  
  同じ事案を報じた中央日報と読売新聞の記事を対にし、共通の事実と強調点の違いを分けた一本の記事を日韓両言語で合成します（Pydanticで出力を検証）。誠信女子大学 SW021「ChatGPT for Business」課程の発展として制作しました。
- **[3モデルのアンサンブルによるスミッシング検出](https://github.com/fairyofdata/AntiPhishingNLP)** · `AntiPhishingNLP` · 2023・5名チーム · 🥇 KISA サイバーセキュリティAI・ビッグデータチャレンジ Track C 最優秀賞（1位）  
  SMS本文をKoBERT・KoELECTRA・Att-BiLSTMのソフトボーティングで判別します（ボイスフィッシングは別デモ）。担当：Att-BiLSTMの設計・実装、ソフトボーティング戦略、SMOTE、推論モジュール。韓国外国語大学 データ青年キャンパスのチームプロジェクトです。
- **[字母単位で回避型の悪口を検出する](https://github.com/fairyofdata/SepticFilterNLP)** · `SepticFilterNLP` · 2022・6名チーム · 🥇 サムスンSDS マルチキャンパス ビッグデータ活用コンテスト 最優秀賞（1位）  
  文字の分離や記号の挿入で隠された悪口を検出します。担当：クローリング（5万6000件以上のコメント）、MySQLスキーマ、データパイプライン、Django連携。

---

## 📚 学歴・研修

- **情報融合学科 データサイエンス専攻 学士** [@光云大学](https://ic.kw.ac.kr:501/program/process.php)  
- **K-デジタルトレーニング**: データサイエンスコース [@マルチキャンパス（サムスンSDS）](https://www.multicampus.com/em/enrolment/courseDetai?p_menu=NzUjU1VC&p_gubun=Qw==&corsCd=FA00NM)  
- **LG Aimers**: データインテリジェンスコース [@LG AI研究院](https://lgresearch.ai/news/view?seq=488)  
- **データ青年キャンパス**: 自然言語処理コース [@韓国外国語大学](https://ime.hufs.ac.kr/bbs/ime/509/71087/artclView.do)  
- **SW021**: ChatGPTビジネス活用コース [@誠信女子大学](https://m.dhnews.co.kr/news/view/1065594826213812)  
- **ACC Korea**: AWS公式大学生コミュニティ 第1期メンバー [@AWS Korea](https://www.awscloudclubs.kr/)  
- **SCIT Master**: 日本ITエンジニア就職連携プログラム [@韓国貿易協会](https://newtradecampus.kita.net/page/user_job_CloudIT_courseguide_outline)  

---

## 🏆 受賞歴

- 🥇 **サムスンSDS マルチキャンパス ビッグデータ活用コンテスト** (マルチキャンパス, 2022) - **最優秀賞 (1位)**  
- 🥇 **韓国インターネット振興院 サイバーセキュリティ AI・ビッグデータチャレンジ Track C** (KISA, 2023) - **最優秀賞 (1位)**  
- 🥈 **光云大学 第8回 産学協力SWプロジェクト** (光云大学, 2024) - **優秀賞 (2位)**  
- 🥈 **光云大学 情報融合学科 卒業作品展示会** (光云大学, 2024) - **優秀賞 (2位)**  
- 🥈 **韓国貿易協会 第47期 SCIT Master プロジェクト発表会** (KITA, 2025) - **優秀賞 (2位)**  
