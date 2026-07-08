# はじめまして！👋

**晴れの国・岡山**でソフトウェアエンジニアとして働いている**白知憲（ペク・ジホン）**です。

LLMアプリケーション、機械学習、NLP、AIエンジニアリングに興味があり、
AIを実際のサービスや業務に活かす開発を目指しています。

現在は**LLMベースのアプリケーション**・**AI自動化**・**MLOps**・**機械学習**を中心にスキルを磨き、MLエンジニアを目標に成長し続けています。

📧 **Email** : fairyofdata@gmail.com  
💼 **LinkedIn** : https://www.linkedin.com/in/hjbaek/

---

## 🚀 興味・関心

- 🤖 LLMアプリケーション
- 🧠 機械学習・深層学習
- 💬 自然言語処理（NLP）
- ⚙️ AIエンジニアリング
- ☁️ MLOps
- 📝 プロンプトエンジニアリング

---

## 💻 技術スタック

### AI / 機械学習
<p>
  <img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=white">
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white">
  <img src="https://img.shields.io/badge/HuggingFace-FDEE21?style=for-the-badge&logo=HuggingFace&logoColor=black">
  <img src="https://img.shields.io/badge/OpenAI_API-74AA9C?style=for-the-badge&logo=openai&logoColor=white">
  <img src="https://img.shields.io/badge/Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white">
</p>

### フロントエンド
<p>
  <img src="https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white">
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
</p>

### バックエンド / データベース
<p>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white">
  <img src="https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white">
  <img src="https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black">
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white">
  <img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white">
</p>

### データサイエンス
<p>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white">
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge">
  <img src="https://img.shields.io/badge/FAISS-0467DF?style=for-the-badge&logo=meta&logoColor=white">
</p>

### ツール
<p>
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white">
  <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white">
  <img src="https://img.shields.io/badge/Google_Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=black">
  <img src="https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white">
</p>

---

## 🗂️ プロジェクト

### 🔬 個人研究 / サービスプロジェクト

---

#### 🧑‍🏫 Phomene — 日本語話者向け・音素レベルの韓国語発音コーチング
> `Python` `Streamlit` `Whisper` `Wav2Vec2` `Gemini` `G2P`

日本語を母語とする学習者が韓国語の発音を矯正できるよう設計されたCAPT（Computer-Assisted Pronunciation Training）Webアプリケーションです。

- **デュアルASRアーキテクチャ**: 言語モデルを内蔵したWhisper（知的誤り補正）と、言語モデルのないWav2Vec2-CTC（物理的発声の捕捉）の差分を測定することで、学習者自身が気づけない発音エラーを数値化します。
- **決定論的G2Pエンジン**: 標準発音法（7終声・連音・鼻音化・激音化など）のルールを純粋なPythonで直接実装し、LLMの幻覚（ハルシネーション）を原천封じ、同一入力に対して常に同一スコアを保証します。
- **L1干渉エラー分類器**: 日本語話者に体系的に現れる母音挿入・終声脱落・三項対立の崩壊など6種のエラーをルールベースでタグ付けし、LLM（Gemini）は構造化された証拠のみを受け取ってカタカナ可視化とコーチングフィードバックを担当します。
- **実証的検証**: Spearman ρ = −0.702、G2P精度100%（51/51、held-outセット）など、4つの再現可能な実験でシステムの有効性を検証しました。

---

#### 📊 LEPOS — LLMベースのESG重視ポートフォリオ最適化サービス
> `Python` `Streamlit` `KoELECTRA` `GPT-3.5` `Black-Litterman` `KOSPI`

🏆 光云大学 第8回 産学協力SWプロジェクト **優秀賞** · 情報融合学科 卒業展示会 **優秀賞**

韓国上場企業のニューステキストをLLMおよびファインチューニング済みモデルで直接分析し、透明性の高いESGスコアを算出。これをBlack-Littermanモデルの投資家ビューとして反映し、パーソナライズされたポートフォリオを構成する研究/サービスシステムです。

- **データパイプライン**: KOSPI 68社のニュース**138万件**を収集し、GPT-3.5でラベルのブートストラッピングを行った後、KoELECTRAをファインチューニングして6段階の分類・回帰モデルのカスケードを構築しました。
- **ポートフォリオ最適化**: ユーザーアンケート（15問）がE/S/G選好をエージェンシー別手法の重みに変換され、Black-Littermanのビュー（P, Q）として注入後、Ledoit-Wolfシュリンケージ共分散に基づく最大シャープ比最適化を実施します。
- **バックテスト**: 2020〜2024年の年次リバランス基準で、KOSPI（Sharpe 0.190）・ESG ETF（0.251）対比、**LEPOS（0.503、最大ドローダウン 0.187）**が全指標で上回ることを実証しました。

---

#### 🛡️ AntiPhishingNLP — NLPベースのフィッシング検出サービス
> `Python` `KoBERT` `KoELECTRA` `Att-BiLSTM` `Django` `STT`

🏆 2023 韓国インターネット振興院（KISA） サイバーセキュリティAI・Big Dataチャレンジ Track C — **最優秀賞 (1位)**

SMSフィッシング（スミッシング）と音声フィッシング（ボイスフィッシング）の両チャネルを同時に検出するNLPベースのフィッシング検知システムです。韓国外国語大学 データ青年キャンパス チームプロジェクト。

- **三重アンサンブル分類器**: KoBERT（双方向文脈理解）・KoELECTRA（トークン適切性判別）・Att-BiLSTM（MeCab形態素解析+Attention）のソフトボーティングで、汎化能力とドメイン特化能力を両立します。
- **二重入力チャネル**: SMSテキストはそのまま投入し、音声データはDjango Web Speech APIでリアルタイムSTT変換後に同じパイプラインに投入します。
- **クラス不均衡対応**: KorCCViDデータセットにSMOTEオーバーサンプリングを適用し、フィッシング/正常クラスの不均衡を解消します。
- **担当パート（白知憲）**: Att-BiLSTMアーキテクチャ設計、アンサンブル投票戦略、KorCCViDデータセット整備・SMOTEパイプライン、テキスト分類推論モジュール開発。

---

#### 🔮 OmikuZ — 世界観拡張型 AI おみくじサービス
> `Python` `FastAPI` `React` `Vite` `SQLAlchemy` `OpenAI` `PWA`

多彩な「世界観（スポット）」を旅しながら、そのキャラクターAIから運勢の深層解釈を受け取れるモバイル最適化Webアプリです。

- **コスト最適化アーキテクチャ**: おみくじ本文はDBマスターデータからキャッシュ返却し、20時間ごとに補充されるトークン（遅延評価）を消費するときだけLLM解釈APIを呼び出し、コストを最小化します。
- **無限拡張構造**: 新規世界観の追加時もバックエンドのコード再デプロイ不要。DBの`theme_metadata（JSON）`フィールドにシステムプロンプトとテーマカラーを注入するだけで即時反映されます。
- **構造化LLMレスポンス**: PydanticのJSONスキーマでLLMの出力を強制パースし、フロントエンドのレンダリング安定性を確保しています。
- **没入感のあるUX**: タイムロック式のワープゲージ、筒を振るインタラクション、タイプライターエフェクトなど、PWA環境でネイティブアプリ水準のマイクロインタラクションを実装しました。

---

#### 🎵 URFIT — 音声認識ベース AI J-POPプレイリストコミュニティ
> `Python` `FastAPI` `Angular` `Whisper` `FAISS` `SentenceTransformer` `Spotify API`

🏆 韓国貿易協会 SCIT Master 47期 プロジェクト発表会 **優秀賞**

「なんとなく覚えている歌詞」や鼻歌だけで聴きたいJ-POPを探し出し、AIが好みに合った類似曲を推薦してSpotifyプレイリストを自動生成するコミュニティサービスです。

- **マルチモーダル検索**: Whisper（STT）で音声をテキストに変換後、SentenceTransformerの埋め込みとFAISSインデックスで歌詞データセットをベクトル類似度検索します。
- **AIプレイリスト生成**: 検索結果をGPT-3.5が分析してクリエイティブなプレイリストタイトルと説明を自動生成し、Spotify OAuth APIでユーザーのアカウントに直接保存します。
- **アーキテクチャのリファクタリング**: Hugging Face Spaceベースのプロトタイプを、Angular 17+（フロントエンド）＋ FastAPI（バックエンド）のマイクロサービスアーキテクチャに完全分離し、Firebase・Cloud Runなど多様なクラウド環境へのデプロイに対応しました。

---

### 🛠️ 個人ツール

---

#### 💰 Accountant — AIベース 家計簿ダッシュボード
> `Angular 21` `Firebase` `Firestore` `PWA` `OpenAI` `Signals`

単なる支出記録を超えた、データクレンジング・多次元クロス可視化・AI財務コンサルティングを統合した個人財務分析ダッシュボードです。（円建て）

- **独自ドメイン設計**: 支出を「管理可能性」に応じて【固定費 / 生活費 / 文化費 / 交際費 / インフラ】の5分類で管理し、AIブリーフィングは管理可能な変動費（生活費＋文化費＋交際費）のみを集中分析します。
- **AIレシートスキャナー**: `gpt-4o-mini`ビジョンモデルがレシート画像から日付・金額・店舗名を抽出し、既存の分類体系をプロンプトに動的注入することでハルシネーションを防止します。
- **OLS回帰による支出予測**: 完了済み過去期間のみを使ったシンプルな線形回帰で次期の支出を予測し、非反復性のアウトライヤー（引越し初期費用など）を自動除外します。
- **PWA＋オフライン同期**: Angular Service Worker＋Dexie（IndexedDB）ローカルキャッシュ＋オフライン変更キューにより、ネットワーク切断中も閲覧・入力が可能で、オンライン復帰時に自動同期されます。

---

#### 🎵 Archetier — レコードコレクション管理ダッシュボード
> `Angular 17+` `Firebase Hosting` `ngx-charts` `Signals`

個人のレコードコレクションを体系的に管理・可視化するダッシュボードです。

- **インテリジェントクロスフィルタリング**: テーブル行をクリックすると、その条件でチャートと詳細一覧が即時フィルタリングされ、フィルター状態に応じてジャンル別比率のパイチャートがアーティスト別のドリルダウンチャートへ自動切替します。
- **レスポンシブUI**: デスクトップでは高機能テーブルグリッド、モバイルではタッチ操作向けのアコーディオンビューへ自動切替し、入手日・発売日や価格プレミアムをバッジ形式で視覚化します。

---

## 📚 経歴

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

---

## 🎯 現在の取り組み

- LLMアプリケーション開発
- AI自動化
- 機械学習
- MLOps
- 実用的なAIサービスの構築
