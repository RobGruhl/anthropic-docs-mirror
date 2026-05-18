# Claude Developer Platform の構造化出力
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d223de65e7dcca8267d8_ea364001be6bf6d2e86b58109ead6a779d5771a7-1000x1000.svg)

# Claude Developer Platform の構造化出力

構造化出力により、応答が JSON スキーマおよびツール定義と一致することを保証。

- カテゴリ製品発表

- 製品Claude Platform

- 日付2025-11-14

- 所要時間5分

- 共有リンクをコピーhttps://claude.com/blog/structured-outputs-on-the-claude-developer-platform

最新情報：Claude Haiku 4.5で利用可能になりました。Claude Developer Platform（Claude Developer Platform）上でネイティブおよび Microsoft Foundry でサポートされています。 （2025年12月4日）

Claude Developer Platform は、Claude Sonnet 4.5 と Opus 4.1 の構造化出力をサポートするようになりました。この機能は公開ベータ版として利用可能で、API レスポンスが常に指定された JSON スキーマまたはツール定義と一致するようにします。

構造化された出力により Claude の応答が定義されたスキーマに準拠していることが保証され、開発者はスキーマ関連の解析エラーやツール呼び出しの失敗を排除できます。画像からのデータ抽出、エージェントのオーケストレーション、外部APIとの統合など、あらゆる場面で有効です。

### 信頼性の高いアプリケーションの構築

本番環境でアプリケーションやエージェントを構築する開発者にとって、データ形式の単一エラーが連鎖的な障害を引き起こす可能性があります。構造化出力は、モデルの性能に影響を与えることなく、定義した構造と完全に一致する応答を保証することでこの問題を解決します。これにより、正確性が極めて重要なアプリケーションやエージェントにおいて、Claude は信頼性の高い選択肢となります。具体的には下記の例が挙げられます。

- データ抽出：下流システムがエラーのない一貫したフォーマットに依存する場合。

- マルチエージェントアーキテクチャ：エージェント間の安定した通信が、パフォーマンスと安定性に不可欠な場合。

- 複雑な検索ツール：複数の検索フィールドを正確に入力し、特定のパターンに準拠する必要がある場合。

構造化出力は、JSON またはツールの 2 つの方法で利用できます。JSON と併用する場合、API リクエスト内にスキーマ定義を提供していただく必要があります。ツールに関しては、ツール仕様の定義を提供してくだだくと、Claude の出力は自動的にこれらのツール定義に準拠します。

その結果、信頼性の高い出力が得られ、再試行回数が削減され、フェイルオーバーロジックや複雑なエラー処理が不要となる簡素化されたコードベースが実現します。

### お客様の事例：OpenRouter

OpenRouter は 400 万以上の開発者に、単一の統合ンターフェイスを通じて主要 AI モデルすべてへのアクセスを提供しています。

「構造化出力はエージェント AI スタックにおいて非常に価値ある構成要素になりました。エージェントは常に構造化データを取り込み生成するため、Anthropic の構造化出力は開発者にとって真の課題を解決します。エージェントワークフローは常に安定して実行され、チームはツール呼び出しのデバッグを行うよりもお客様に集中できます」と OpenRouter の COO である Chris Clark 氏は述べています。

### 開始方法

構造化出力はパブリックベータ版として、Claude Developer Platform において Sonnet 4.5 および Opus 4.1 で利用できるようになりました。Haiku 4.5 のサポートもまもなく開始される予定です。サポートされる JSON スキーマタイプ、実装例、ベストプラクティスの詳細は[ドキュメント](#)をご覧ください。

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

よくある質問

## 関連する投稿

Claude を活用して構築を行うチーム向けの、その他の製品ニュースとベストプラクティスをご覧ください。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22e13864f88ea55c2d8_b5c98d26c46edc43193e7f7e28a00633a538bb9c-1000x1000.svg)

### Code w/ Claude SF 2026 recap: Building on the AI exponential

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a025cf25f0694905405e054_Object-Scale.svg)

### Claude for the legal industry

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

### Claude Security is now in public beta

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225e31f7aa22c1f28cb_46e4aa7ea208ed440d5bd9e9e3a0ee66bc336ff1-1000x1000.svg)

### Built-in memory for Claude Managed Agents

## Claude を活用して組織運営の方法を変革

開発者向けニュースレターを入手

製品の最新情報、操作方法、コミュニティスポットライトなどを掲載しています。毎月受信トレイに配信されます。

毎月の開発者向けニュースレターを受け取りたい場合は、メールアドレスを入力してください。購読はいつでも解除できます。

---
**Source:** https://claude.com/ja/blog/structured-outputs-on-the-claude-developer-platform
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
