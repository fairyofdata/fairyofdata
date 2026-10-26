<!-- 原本: README_KR.md（韓国語版が原本、英語・日本語は翻訳） · 同期: 2026-10-26 -->

# はじめまして！👋

[English](README.md) · [한국어](README_KR.md) · [日本語](README_JP.md)

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

日本語母語話者が韓国語の発音の誤りを音素単位で見つけて直せるようにする CAPT（Computer-Assisted Pronunciation Training）Web アプリケーションです。チームプロジェクト URFIT で担当した音声検索モジュール（[RAGSTT4Lyrics](https://github.com/fairyofdata/RAGSTT4Lyrics)）の ASR（Whisper）・音声処理パイプラインを広げて作りました。

- **デュアル ASR**: 言語モデルを内蔵した Whisper（ネイティブが聞き取る側）と、言語モデルのない Wav2Vec2-CTC（実際に出した音の側）の差を測り、学習者が自分では聞き取れない誤りを見えるようにします。
- **決定論的 G2P エンジン**: 標準発音法（7終声、連音、鼻音化、激音化など）を純粋な Python のルールとして実装し、同じ入力には常に同じスコアが出ます。
- **L1 干渉エラー分類器**: 対照音韻論の研究（Jang 2016 など）に根拠を置くルールベースのタガーで、母音挿入・終声脱落・平音/激音/濃音の混同など、日本語話者に体系的に現れる 9 種の誤りを診断します。カタカナ表記もルール表で作り、LLM（Gemini）は構造化された証拠を受け取ってコーチング文だけを書きます。
- **実証的検証**: 実際の日本語話者の音声（AI-Hub L2 コーパス、615 発話・198 名）で、上位／下位評価の判別 AUC 0.818、人手評価との相関 ρ = 0.473 を示し、古典的な GOP ベースラインを全指標で上回りました。スコアと誤りの重さの相関は ρ = −0.702（音声を合成し直した再実行では −0.599、両方を記録）、G2P 精度は held-out で 100%（51/51・17/17）です。実験は 6 つを実施し、募集した評定者との相関研究は設計のみです。

---

#### 📊 [PortfolioOpt4ESG — LLMベースのESG重視ポートフォリオ最適化 (LEPOS)](https://github.com/fairyofdata/PortfolioOpt4ESG)
> `Python` `Streamlit` `KoELECTRA` `GPT-3.5` `Black-Litterman` `KOSPI`

🏆 光云大学 第8回 産学協力SWプロジェクト **優秀賞** · 情報融合学科 卒業展示会 **優秀賞**  
📄 共著論文（第2著者）が *Computational Economics*（Springer, 2026）に掲載 — [doi:10.1007/s10614-026-11413-9](https://doi.org/10.1007/s10614-026-11413-9)

韓国上場企業のニューステキストをLLMおよびファインチューニング済みモデルで直接分析し、透明性の高いESGスコアを算出。これをBlack-Littermanモデルの投資家ビューとして反映し、パーソナライズされたポートフォリオを構成する研究/サービスシステムです。

- **データパイプライン**: KOSPI 68社のニュース**138万件**を収集し、GPT-3.5でラベルのブートストラッピングを行った後、KoELECTRAをファインチューニングして6段階の分類・回帰モデルのカスケードを構築しました。
- **ポートフォリオ最適化**: ユーザーアンケート（15問）をE/S/G選好と評価機関別の手法の重みに変換し、Black-Littermanのビュー（P, Q）として入れた後、Ledoit-Wolfシュリンケージ共分散に基づく最大シャープ比最適化を行います。
- **バックテスト**: 2020〜2024年の年次リバランスで、**最適化したESGポートフォリオ（Sharpe 0.499、最大ドローダウン 0.187）**がKOSPI（0.190）・ESG ETF（0.251）を全指標で上回りました（リポジトリでの再現結果。生存者バイアス、サンプル内で選んだ τ などの限界はリポジトリの README に記載）。

---

#### 🎵 [RAGSTT4Lyrics — うろ覚えの歌詞から J-POP を探す (Songfinder)](https://github.com/fairyofdata/RAGSTT4Lyrics)
> `Python` `FastAPI` `Angular` `Whisper` `FAISS` `SentenceTransformer` `Spotify API`

🏆 韓国貿易協会 SCIT Master 47期 プロジェクト発表会 **優秀賞**（6名のチームプロジェクトURFITとして受賞）  
👤 URFITのうち、音声・音楽マッチングの部分（STT → FAISS検索 → 推薦 → Spotifyプレイリスト）を一人で実装し、2026年のリファクタリングと性能評価も一人で行いました。

うろ覚えの歌詞を話すか入力すると J-POP の曲を見つけ、似た曲を推薦して Spotify のプレイリストにするサービスです。歌詞のない鼻歌では探せません。

- **音声検索**: Whisper（STT）で書き起こした歌詞を、SentenceTransformer の埋め込みと FAISS で検索します。曲を特定する段階では LLM を使いません。
- **評価と改善**: 曲の特定の段階だけを切り出し、合成クエリと TTS 音声で測りました（実利用での精度ではありません）。韓国語なまりの日本語の 35% を Whisper が韓国語として書き起こす問題を見つけ、日本語での再書き起こしと行単位の断片の投票を入れた結果、韓国語なまりの音声は **36% → 69%**、ネイティブの 5 行の音声は 47% → 74% になりました。
- **プレイリスト文と構成**: 見つかった曲の要約・タグから GPT-3.5 がプレイリストのタイトルと説明を書き、Spotify OAuth でアカウントに保存します。Hugging Face Space のプロトタイプを Angular 17 + FastAPI に分けて作り直しました（デプロイは次の段階）。

---

### 🚧 開発中

- **[韓国語話者のための日本語作文コーチ](https://github.com/fairyofdata/PragmaticsKR2JP)** · `PragmaticsKR2JP` · 2026年9月 ～・個人  
  日本語の文章がどこで間違っていて、その場面・相手に何が適切かを教えてくれる個人用のコーチです。LLMは固定の誤り分類表に沿って位置と種類だけを付け、引用の原文照合・3回採点の多数決・集計はコードが行い、その注釈の再現性と検出率を測って公開します。
- **[ローカルモデルが関門に立つ、カスケード型DLPレイヤー](https://github.com/fairyofdata/CascadeDLP)** · `CascadeDLP` · 2026年9月 ～・個人  
  文書をクラウドのLLMに渡す前にローカルのモデルが読み、「通過・伏せて送信・利用者に確認・ローカルのみ・拒否」を判定します。韓国語・日本語・英語が混在する文書が対象で、MCPツールとして使います。

---

### 📁 その他のプロジェクト

- **[日韓の報道を比べて中立的な記事にまとめる](https://github.com/fairyofdata/Neutralize4KRJP)** · `Neutralize4KRJP` · 2024・個人  
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
