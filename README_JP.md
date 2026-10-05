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

### 🤖 LLM & AI エンジニアリング プロジェクト

---

#### 🧑‍🏫 [PhonemeJP2KR — 日本語話者向け・音素レベルの韓国語発音コーチング](https://github.com/fairyofdata/PhonemeJP2KR)
> `Python` `Streamlit` `Whisper` `Wav2Vec2` `Gemini` `G2P`

日本語を母語とする学習者が韓国語の発音を矯正できるよう設計されたCAPT（Computer-Assisted Pronunciation Training）Webアプリケーションです。優秀賞を受賞した音声認識検索プロジェクト（URFIT）で確立したASR（Whisper）および音声処理パイプライン技術を拡張し、より高度な音素レベルの発音診断システムとして設計しました。

- **デュアルASRアーキテクチャ**: 言語モデルを内蔵したWhisper（知的誤り補正）と、言語モデルのないWav2Vec2-CTC（物理的発声の捕捉）の差分を測定することで、学習者自身が気づけない発音エラーを数値化します。
- **決定論的G2Pエンジン**: 標準発音法（7終声・連音・鼻音化・激音化など）のルールを純粋なPythonで直接実装し、LLMの幻覚（ハルシネーション）を原천封じ、同一入力に対して常に同一スコアを保証します。
- **L1干渉エラー分類器**: 対照音韻論の研究（Jang 2016など）に学術的根拠を置いたルールベースのタガーで、日本語話者に体系的に現れる母音挿入・終声脱落・三項対立の崩壊など6種のエラーを診断します。LLM（Gemini）は構造化された証拠のみを受け取ってカタカナ可視化とコーチングフィードバックを担当します。
- **実証的検証**: 実際の日本語話者音声（AI-Hub L2コーパス、615発話・198名）で上位／下位評価の判別 AUC 0.818、人手評価との相関 ρ = 0.473 を示し、古典的な GOP ベースラインを全指標で上回りました。加えて Spearman ρ = −0.702（スコアと誤り重篤度の相関）、G2P精度100%（51/51・17/17、held-out）など、6つの再現可能な実験でシステムの有効性を検証しました。

---

#### 📊 [LLM_ESG_POS — LLMベースのESG重視ポートフォリオ最適化サービス](https://github.com/fairyofdata/LLM_ESG_POS)
> `Python` `Streamlit` `KoELECTRA` `GPT-3.5` `Black-Litterman` `KOSPI`

🏆 光云大学 第8回 産学協力SWプロジェクト **優秀賞** · 情報融合学科 卒業展示会 **優秀賞**

韓国上場企業のニューステキストをLLMおよびファインチューニング済みモデルで直接分析し、透明性の高いESGスコアを算出。これをBlack-Littermanモデルの投資家ビューとして反映し、パーソナライズされたポートフォリオを構成する研究/サービスシステムです。

- **データパイプライン**: KOSPI 68社のニュース**138万件**を収集し、GPT-3.5でラベルのブートストラッピングを行った後、KoELECTRAをファインチューニングして6段階の分類・回帰モデルのカスケードを構築しました。
- **ポートフォリオ最適化**: ユーザーアンケート（15問）がE/S/G選好をエージェンシー別手法の重みに変換され、Black-Littermanのビュー（P, Q）として注入後、Ledoit-Wolfシュリンケージ共分散に基づく最大シャープ比最適化を実施します。
- **バックテスト**: 2020〜2024年の年次リバランス基準で、KOSPI（Sharpe 0.190）・ESG ETF（0.251）対比、**LEPOS（0.503、最大ドローダウン 0.187）**が全指標で上回ることを実証しました。

---

#### 🎵 [LLM_STT_Songfinder — 音声認識ベース AI J-POPプレイリストコミュニティ](https://github.com/fairyofdata/LLM_STT_Songfinder)
> `Python` `FastAPI` `Angular` `Whisper` `FAISS` `SentenceTransformer` `Spotify API`

🏆 韓国貿易協会 SCIT Master 47期 プロジェクト発表会 **優秀賞**

「なんとなく覚えている歌詞」や鼻歌だけで聴きたいJ-POPを探し出し、AIが好みに合った類似曲を推薦してSpotifyプレイリストを自動生成するコミュニティサービスです。

- **マルチモーダル検索**: Whisper（STT）で音声をテキストに変換後、SentenceTransformerの埋め込みとFAISSインデックスで歌詞データセットをベクトル類似度検索します。
- **AIプレイリスト生成**: 検索結果をGPT-3.5が分析してクリエイティブなプレイリストタイトルと説明を自動生成し、Spotify OAuth APIでユーザーのアカウントに直接保存します。
- **アーキテクチャのリファクタリング**: Hugging Face Spaceベースのプロトタイプを、Angular 17+（フロントエンド）＋ FastAPI（バックエンド）のマイクロサービスアーキテクチャに完全分離し、Firebase・Cloud Runなど多様なクラウド環境へのデプロイに対応しました。

---

#### ✍️ [PragmaticsKR2JP — 韓国語話者のための日本語作文コーチ](https://github.com/fairyofdata/PragmaticsKR2JP)
> `Python` `Streamlit` `Structured Outputs` `LLM-as-annotator`

🚧 開発中（2026年9月 ～）・個人開発

日本語で書いた文章の誤りを、固定の誤り分類表に沿ってLLMにタグ付けさせる個人用の作文コーチです。LLMが付けるのは誤りの位置と種類だけで、引用が原文にあるかの照合、タグなしで直された箇所の検出、3回採点の多数決、集計はコードが行います。プロンプトで指示した規則が守られないことを実験で確かめ、その規則をコードの検査に移しました。

---

#### 🚪 [CascadeDLP — ローカルモデルが関門に立つ、カスケード型DLPレイヤー](https://github.com/fairyofdata/CascadeDLP)
> `Python` `Local LLM` `MCP` `Pseudonymization`

🚧 開発中（2026年9月 ～）・個人開発

文書をクラウドのLLMに渡す前に、ローカルのモデルが先に読んで判定する、データ漏えい防止（DLP）のレイヤーです。機微な項目は、ルール、人が確定した用語集、ローカルLLMの順に探し（検出カスケード）、その結果から文書を「通過・伏せて送信・利用者に確認・ローカルのみ・拒否」のいずれかに判定します。伏せて送った文書の回答は、ローカルで元の値に戻します。クラウドに渡すかどうかは文書の機微度で決めます。韓国語・日本語・英語が混在する文書が対象で、MCPツールとして使います。

---

#### ⚖️ [LLM_NAKOJA — LLMベース日韓関係中立記事自動生成システム](https://github.com/fairyofdata/LLM_NAKOJA)
> `Python` `OpenAI (GPT-4o-mini)` `Pydantic Structured Outputs` `Selenium` `Streamlit` `Pytest`

韓国（中央日報）と日本（読売新聞）が同じ事案をどう報じたかを対にして比べ、**共通の事実と強調点の違いを分けた一本の記事を、日本語と韓国語の両方で合成するパイプライン**です。自国中心のフレーミングを減らすことを狙いとしています。

- **英語を中間言語として使う**: 最終の記事を書く前に、事実と主観的な主張を構造化した英語の要約にまとめます。この段階は、母語（L1）特有のフレーミングや感情的な言い回しを減らすことを狙いとしています。
- **スキーマによる出力の強制**: 改行分割や正規表現の代わりに、OpenAIの構造化出力と Pydantic v2 スキーマを採用し、両国の論点対照表（Perspective Contrast Matrix）を抽出します。実APIでのパース失敗率は未計測です。
- **層の分離と単体テスト**: スクレイパー、LLMパイプライン、UIを分離。単体テスト10件（Mock OpenAI クライアント使用）でスキーマの直列化とパイプラインの分岐を検証しています。

---

#### 🛡️ [AntiPhishingNLP — NLPベースのフィッシング検出サービス](https://github.com/fairyofdata/AntiPhishingNLP)
> `Python` `KoBERT` `KoELECTRA` `Att-BiLSTM` `Django` `STT`

🏆 2023 韓国インターネット振興院（KISA） サイバーセキュリティAI・Big Dataチャレンジ Track C — **最優秀賞 (1位)**

SMSフィッシング（スミッシング）と音声フィッシング（ボイスフィッシング）の両チャネルを同時に検出するNLPベースのフィッシング検知システムです。韓国外国語大学 データ青年キャンパス チームプロジェクト。

- **三重アンサンブル分類器**: KoBERT（双方向文脈理解）・KoELECTRA（トークン適切性判別）・Att-BiLSTM（MeCab形態素解析+Attention）のソフトボーティングで、汎化能力とドメイン特化能力を両立します。
- **2つのチャネル**: SMSテキストはアンサンブルで判別します。音声チャネルは別の Django デモで、ブラウザの Web Speech API で文字起こしした結果を、アンサンブルではなく専用の単一 LSTM モデルで判別します。
- **クラス不均衡対応**: KorCCViDデータセットにSMOTEオーバーサンプリングを適用し、フィッシング/正常クラスの不均衡を解消します。
- **担当パート（白知憲）**: Att-BiLSTM の構成（単純な LSTM の代わりに、双方向 LSTM に Attention 層を加える）を提案し、実装までを主導。クラス不均衡に対する SMOTE の適用も提案し、実装を主導しました。細部の一部はチームメンバーと共同で行いました。

---

#### 🛡️ [SepticFilterNLP — ディープラーニングアルゴリズムに基づく悪口検出フィルター](https://github.com/fairyofdata/SepticFilterNLP)
> `Python` `FastText` `CNN` `LSTM` `Django` `MySQL`

🏆 最優秀賞 (1位) — サムスンSDS マルチキャンパス ビッグデータ活用コンテスト

従来の形態素ベースのフィルターでは検出できない、巧妙に回避された悪口（文字の分離、特殊記号の挿入など）を検出するために開発されたディープラーニングフィルターです。

- **デュアルトークン化とアンサンブル（チーム）**: チームとして、文字レベルの子音・母音（字母）分離トークナイザーと3モデル（FastText LSTM、Jamo LSTM、Jamo CNN）のソフトボーティングアンサンブルを構築しました（単一モデル最高精度：Jamo CNN 93.7%）。
- **データエンジニアリング**: Selenium + BeautifulSoup によるマルチコミュニティ・クローラー（IPブロック回避を含む）を構築して5万6000件以上のコメントを収集し、MySQLスキーマと取り込みパイプラインを設計しました。
- **フルスタックデプロイ**: モデル推論APIをDjangoバックエンドとWebインターフェースに連携し、予測ログをMySQLに保存しました。
- **担当パート（白知憲）**: クローリング、MySQLスキーマ・データパイプライン設計、Djangoサービス連携、ラベリング。

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

## 🎯 現在注力している領域 (Current Focus)

- 機械学習システムと再現可能なモデル評価
- LLMベースのアプリケーションおよびワークフロー自動化
- 非構造化ドキュメントの情報抽出・実務NLPパイプライン
- 現場の制約条件に耐えうる堅牢な実用AIシステムの構築
