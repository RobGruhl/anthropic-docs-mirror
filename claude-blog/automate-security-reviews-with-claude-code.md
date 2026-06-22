# Claude Codeでセキュリティレビューを自動化
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2260bfc90348429f9c3_cd9cf56a7f049285b7c1c8786c0a600cf3d7f317-1000x1000.svg)

# Claude Codeでセキュリティレビューを自動化

- カテゴリ製品発表

- 製品Claude Code

- 日付2025-08-06

- 所要時間5分

- 共有リンクをコピーhttps://claude.com/blog/automate-security-reviews-with-claude-code

本日は、Claude Code の自動セキュリティレビューについて説明します。GitHub Actions 統合と新しい /security-review コマンドを使用して、開発者は容易に Claude にセキュリティ上の懸念事項を特定するよう指示でき、その後それらを修正をしてもらえます。

開発者がより迅速なリリースと複雑なシステム構築のために AI への依存度を高めるにつれ、コードのセキュリティ確保はこれまで以上に重要となります。今回の新機能により、セキュリティレビューを既存のワークフローに統合することが可能になり、本番環境に到達する前に脆弱性を検出するのに役立ちます。

### ターミナルからコードの脆弱性を確認

新しい /security-review コマンドを使用すると、コードをコミットする前にターミナルからアドホックなセキュリティ分析を実行できます。Claude Code でコマンドを実行すると、Claude はコードベース内の潜在的な脆弱性を検索し、発見した問題について詳細な説明を提供します。

このコマンドは、セキュリティに特化した専用のプロンプトを使用し、以下を含む一般的な脆弱性パターンをチェックします。

- SQL インジェクションリスク

- クロスサイトスクリプティング（XSS）脆弱性

- 認証と承認の欠陥

- 安全でないデータ処理

- 依存関係の脆弱性

また、各問題が特定された後、Claude Code に各問題の修正を指示することもできます。これにより、セキュリティレビューを継続的に内部の開発プロセスに組み込むことができ、修正が最も容易な早い段階で問題を発見することが可能となります。

### 新しいプルリクエストに対するセキュリティレビューを自動化

Claude Code 用の新しい GitHub Action は、プルリクエストが作成されるたびに自動的に解析を行うことで、セキュリティレビューをさらに上のレベルに引き上げます。設定後、GitHub Action は以下を実行します。

- 新しいプルリクエストが開かれたときに自動的にトリガー

- セキュリティ脆弱性についてコード変更をレビュー

- カスタマイズ可能なルールを適用し、誤検知や既知の問題を除外

- 特定された懸念事項と推奨される修正について PR にインラインコメントを投稿

これによりチーム全体で一貫したセキュリティレビュープロセスが確立され、最低限の基礎水準のセキュリティレビューなしにコードが本番環境に到達することがないよう保証されます。このアクションは既存の CI/CD パイプラインと連帯しチームのセキュリティポリシーに合わせてカスタマイズ可能です。

![2 つのスクリーンショット、Claude Code が検出した脆弱性を示し、GitHub にコメントを残す。](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e95d9257ab1dfc1937fcbe_37aa77df52f1a4e8d81f398f48dbb98a5ba1d5ec-1920x1080.png)

### Anthropic における製品セキュリティの向上

当社では、Claude Code 自体を含む、チームが本番環境にリリースするコードのセキュリティ確保に、これらの機能を自ら活用しています。GitHub Action の導入以来、これまでに自社コード内のセキュリティ脆弱性を検出・特定し、リリースする前に防止することができました。

例えば先週、チームが内部ツール向けに開発した新機能では、ローカル接続を受け付けるローカル HTTP サーバーの起動が必要でした。GitHub Action は、DNS リバインディングを通じて悪用可能なリモートコード実行の脆弱性を特定し、PR がマージされる前に修正されました。

![リモートコード実行の脆弱性を示す GitHub のコメント](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e95d9257ab1dfc1937fcc2_a370dba2f6e5095cdbcb23ef878dda4befd61d95-1920x1080.png)

別の事例では、エンジニアがプロキシシステムを構築して社内認証情報を安全に管理できるようにしました。 GitHub Action は、自動的にこのプロキシが SSRF 攻撃に対して脆弱であるとフラグを立て、直ちにこの問題を修正しました。

![SSRF 攻撃の脆弱性を示す GitHub のコメント](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68e95d9257ab1dfc1937fcb8_23dd3b5404c6f7dc812df83a7de95babab286865-1920x1080.png)

### 開始方法

両方の機能は現在、すべての Claude Code ユーザーに提供されます。自動セキュリティレビューの使用を開始する方法。

- /security-review　コマンドの場：Claude Code を最新バージョンに更新し、プロジェクトディレクトリで　/security-review を実行します。コマンドをカスタマイズする方法については、ドキュメントを参照ください。

- GitHub Action の場合：ステップバイステップのインストールおよび構成の手順についてはドキュメントを参照ください。

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

よくある質問

## 関連する投稿

Claude を活用して構築を行うチーム向けの、その他の製品

ニュースとベストプラクティスをご覧ください。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a025cf25f0694905405e054_Object-Scale.svg)

### 法務業界向けの Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690937bee860a953417a8eee_Object-CodeBrowserGlobe.svg)

### ウェブ上のClaude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22cf0b73a86025c5ba9_2174acb37a84767550abfe2588eb5648f941a897-1000x1000.svg)

### Max planの紹介

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22d0099a66d72e05699_33ddc751e21fb4b116b3f57dd553f0bc55ea09d1-1000x1000.svg)

### Claude in Chrome のパイロット試験

## Claude を活用して組織運営の方法を変革

開発者向けニュースレターを入手

製品の最新情報、操作方法、コミュニティスポットライトなどを掲載しています。毎月受信トレイに配信されます。

毎月の開発者向けニュースレターを受け取りたい場合は、メールアドレスを入力してください。購読はいつでも解除できます。

---
**Source:** https://claude.com/ja/blog/automate-security-reviews-with-claude-code
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
