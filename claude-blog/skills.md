# エージェントスキルの紹介
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2307f9555d7c1bc46cb_77dd9077412abc790bf2bc6fa3383b37724d6305-1000x1000.svg)

# エージェントスキルの紹介

- カテゴリ製品アップデート情報

- 製品Claude Platform

- 日付2025-10-16

- 所要時間5分

- 共有リンクをコピーhttps://claude.com/blog/skills

最新情報：[組織全体でのスキル管理機能](#)、パートナーが構築したスキルを紹介するディレクトリを追加しました。またエージェントスキルをプラットフォーム間で移植可能なオープンスタンダードとして公開しました。（2025年12月18日）

Claudeは、スキルを活用して特定のタスクの実行方法を改善できるようになりました。 スキルとは、Claudeが必要に応じて読み込むことができる、指示、スクリプト、リソースが格納されたフォルダーです。

Claudeは、目の前のタスクに関連するスキルのみ利用します。スキルを活用することで、Excelの操作や組織のブランドガイドラインに従うといった専門的なタスクにおいてClaudeがより効果的にパフォーマンスを発揮できるようになります。

すでにスキルは、Claudeのアプリで動作しています。Claudeはこれらを活用してスプレッドシートやプレゼンテーションなどのファイルを作成しています。今後は、独自のスキルを構築し、Claudeアプリ、Claude Code、API全体でそれらを活用できるようになります。

## スキルの仕組み

Claudeはタスクに取り組む際、利用可能なスキルをスキャンして関連性の高いものを見つけます。 条件が合致すると、必要な最小限の情報とファイルのみを読み込み、専門知識にアクセスしながらClaudeの動作を高速に維持します。

スキルの特長は以下の通りです。

- 組み合わせ可能：スキルを組み合わせることができます。 Claudeは必要なスキルを自動的に特定し、その使用を調整します。

- 移植可能：スキルはどこでも同じフォーマットを使用します。 一度構築すれば、Claudeアプリ、Claude Code、API全体で使用できます。

- 効率的：必要なときに必要なものだけを読み込みます。

- 強力：スキルには、従来のプログラミングがトークン生成よりも信頼性の高いタスク向けに、実行可能なコードを含めることができます。

スキルを、専門知識をパッケージ化できるカスタムオンボーディング教材とみなし、Claudeをユーザーにとって最も重要な分野の専門家に育成できます。エージェントスキルの設計パターン、アーキテクチャ、開発のベストプラクティスに関する技術的な詳細は、[エンジニアリングブログ](#)をご覧ください。

## スキルはすべてのClaude製品で機能

### Claudeのアプリ

Pro、Max、Team、Enterpriseのユーザーは、スキルを利用できます。文書作成、カスタマイズ可能なサンプル、独自のカスタムスキルを作成する機能など、一般的なタスク向けのスキルを提供します。

![Claude.aiのスキル機能インターフェイス（スキルが有効化されている状態の例）](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/696bc306edc0bf4d2a7f273a_69338018ff630211cebe56f2_690267e194f8fd4618cb330e_image.webp)

Claudeは、タスクに基づいて関連するスキルを自動的に呼び出します。手動で選択する必要はありません。 作業中にClaudeの思考プロセス内でスキルを確認することも可能です。スキルの作成は簡単です。 「スキル作成」スキルでは、インタラクティブなガイダンスを提供します。Claudeはワークフローについての質問、フォルダー構造を生成し、SKILL.mdファイルのフォーマットを行い、必要なリソースをまとめてパッケージ化します。手作業でファイル編集する必要はありません。

[設定](#)でスキルを有効にします。 TeamおよびEnterpriseユーザーの場合、管理者はまず組織全体でスキルを有効にする必要があります。

### Claude Developer Platform（API）

エージェントスキル（単にスキルと呼ぶことが多いです）を、Messages APIリクエストに追加できるようになりました。新たな/v1/skillsエンドポイントにより、開発者はカスタムスキルのバージョン管理や運用をプログラムで制御できるようになります。スキルには、[コード実行ツール](#)のベータ版が必要で、これはスキル実行に必要な安全な環境を提供します。

Anthropicが開発したスキルを活用してClaudeに、数式付きの専門的なExcelスプレッドシート、PowerPointプレゼンテーション、Word文書、入力可能なPDFファイルの読み取りおよび生成を行わせることができます。開発者は、カスタムスキルを作成して、特定のユースケース向けにClaudeの機能を拡張できます。

また、開発者はClaude Consoleを通じてスキルのバージョンを簡単に作成、表示、アップグレードできます。

詳細については、[ドキュメント](#)、スキルのクックブック、[Anthropic Academy](#)をご覧ください。

‍

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a8c287936531790c85c4_box_light.svg)

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a8bdc1ea299a1a768655_box_dark.svg)

「スキルは、ClaudeにBox上のコンテンツの扱い方を教えます。ユーザーは、保存されているファイルを、自社の標準に準拠したPowerPointプレゼンテーション、Excelスプレッドシート、Word文書へと変換でき、何時間分もの作業時間を節約できます。」

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a94f6f82b1f84f489887_Canva_light.svg)

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a94baddb6685c1e5410d_Canva_dark.svg)

「Canvaはスキルを活用してエージェントをカスタマイズし、できる範囲を拡大する予定です。これにより、Canvaをエージェントのワークフローに深く浸透させる新しい方法が開かれ、チームが独自のコンテキストを把握し、驚くほど高品質なデザインを簡単に作成できるようになります。」

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68ba17a186e44af7d97dae57_Frame.svg)

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68ba179c1c4432fa78b2f126_Frame-1.svg)

「スキルを使えば、ClaudeはNotionとシームレスに連携し、ユーザーを“質問”から“実行”へとより迅速に導きます。複雑なタスクにおけるプロンプト調整の手間を減らし、より予測可能な結果を実現します。」

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d5faa6352b26bf7542cb9b_logo_rakuten-light.svg)

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68d5fab610bf0d091b541153_logo_rakuten-dark.svg)

Skills により、管理会計と財務のワークフローが効率化されます。Claude が複数のスプレッドシートを処理し、重大な異常を検出し、当社の業務プロセスに従ってレポートを生成します。以前は 1 日を要していた作業が、現在では 1 時間で完了します。

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

### Claude Code

スキルは、チームの専門知識とワークフローでClaude Codeを強化します。 anthropics/skillsマーケットプレイスのプラグインを介してスキルをインストールできます。Claudeは関連性の高いスキルを自動的に読み込みます。 バージョン管理を通じてチーム内でスキルを共有できます。 また、~/.claude/skillsにスキルを追加することで、手動でインストールすることもできます。 Claude Agent SDKは、カスタムエージェントの構築においても、同様のエージェントスキルサポートを提供します。

## 開始方法

- Claudeアプリ：ユーザーガイドとヘルプセンター

- API開発者：ドキュメント

- Claude Code：ドキュメント

- カスタマイズするスキル例：GitHubリポジトリ

## 今後の予定

当社は、スキル作成ワークフローの簡素化と全社的な導入機能の実現に向けた取り組みを進めており、これにより組織がチーム間でスキルを分配しやすくなります。

なお、この機能によりClaudeはコードを実行する権限を得ることに留意してください。強力な機能ではありますが、どのスキルを使用するかには十分ご注意ください。お客様のデータの安全性を保つために信頼できるソースに限定してご利用ください。[詳細はこちら](https://support.claude.com/en/articles/12512180-using-skills-in-claude#h_2746475e70)。

よくある質問

## 関連する投稿

Claude を活用して構築を行うチーム向けの、その他の製品

ニュースとベストプラクティスをご覧ください。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3f14a08cb97bf1b16d40ef_ObjectClouds.svg)

### Claude in Microsoft Foundry is now generally available

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a025cf25f0694905405e054_Object-Scale.svg)

### 法務業界向けの Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690937bee860a953417a8eee_Object-CodeBrowserGlobe.svg)

### ウェブ上のClaude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22cf0b73a86025c5ba9_2174acb37a84767550abfe2588eb5648f941a897-1000x1000.svg)

### Max planの紹介

## Claude を活用して組織運営の方法を変革

開発者向けニュースレターを入手

製品の最新情報、操作方法、コミュニティスポットライトなどを掲載しています。毎月受信トレイに配信されます。

毎月の開発者向けニュースレターを受け取りたい場合は、メールアドレスを入力してください。購読はいつでも解除できます。

---
**Source:** https://claude.com/ja/blog/skills
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
