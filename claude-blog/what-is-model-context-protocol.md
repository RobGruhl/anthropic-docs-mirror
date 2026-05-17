# モデルコンテキストプロトコルとは？AIをあなたの世界に接続
---
![](https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg)

# モデルコンテキストプロトコルとは？AIをあなたの世界に接続

モデルコンテキストプロトコルを使え​​ばカスタム統合なしで、AIアシスタントをツールに接続できます。

- カテゴリエージェント

- 製品Claudeのアプリ

- 日付2025-10-31

- 読了時間5分

- 共有リンクをコピーhttps://claude.com/blog/what-is-model-context-protocol

AI models are only as good as the context provided to them. AI assistants like[Claude](https://claude.ai)can answer questions and perform an impressive range of tasks, but if they can't access the data or tools they need, they're limited in what they can do for you. You typically solve this by copying and pasting context from one tab to another, whether it's editing a document in Google Drive, replying to a thread in Slack, or updating code in an IDE. This process is slow, manual, and risks leaving out important context.

TheModel Context Protocol (MCP)offers a solution that is open and widely available across all AI apps and assistants. In this article, you'll learn what MCP is, how it works and why it matters, and who it's for. You'll see examples of MCP in action and understand how you can start using or building with MCP today.

## What is the Model Context Protocol (MCP)?

TheModel Context Protocolis an open standard that defines how LLMs communicate with external systems.

Think of MCP asUSB-C for LLMs. Just as USB-C provides a universal connector for your phone, laptop, and other devices, MCP provides a universal format for LLMs to connect with external systems. Before USB-C, every electronic gadget had its own cable: Lightning for iPhone, micro-USB for Android, proprietary connectors for cameras. As more devices adopted USB-C, connectivity became seamless across the ecosystem.

MCP brings this same simplicity to AI integrations. Before MCP, every application and database required custom code to connect with LLMs. Google Drive needed its own integration, Slack needed another, Figma yet another. Now, MCP provides a single, standardized format for connecting these tools to Claude and other AI applications.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6920e9d8382558e1ff64db41_68f64b7d51a1d57549b3ad8e_What%2520is%2520MCP_%2520Final%25402x.png)

## Where did MCP come from?

MCP was created at Anthropic by David Sorria Para and Justin Spahr-Summers. The idea originated from David's frustration with constantly copying code between Claude Desktop and his Integrated Development Environment (IDE). Recognizing this as a classic M×N problem where multiple applications need multiple integrations, David pitched building a protocol to solve this to Justin. They designed MCP based on the popular Language Server Protocol and open-sourced it in November 2024 with Anthropic's support to ensure the entire AI ecosystem could benefit.

## How does MCP work?

MCP works through a two-sided approach. AI agents and chatbots like Claude createMCP Clients, so they can connect to applications like Notion, Canva, or Figma, who make their tools and data available throughMCP Servers.

By building anMCP Client, AI agents and chatbots can access thousands of MCP Servers built by the community, giving them a straightforward path to extend their capabilities. By building anMCP Server, companies and developers can make their products readily available to AI, creating a new avenue to provide value.

As MCP is open-source, anyone can build an MCP Server or Client.

## Why is MCP important?

MCP allows LLMs to go beyond chat and perform real-world tasks: reading an email thread and sending a reply, accessing a codebase and deploying an update, or reviewing a design brief and generating a first draft. The protocol creates a foundation for LLMs to connect with external systems, tools, and applications to access data and take actions. This provides:

### Universal compatibility for AI

AI assistants gain access to thousands of tools— Once an AI assistant implements MCP (via an MCP client), it can instantly connect to thousands of MCP-compatible applications, from specialized coding tools to enterprise workflow platforms, without building custom integrations for each one.

Tools and applications connect to every AI assistant at once— Companies like Notion, Figma, or Asana build a single MCP server that works with any AI assistant that’s compatible (i.e. has implemented an MCP client). Developers only need to build one integration for all AI connections.

### An Open, AI-native ecosystem

Anyone can build and share— As an open standard, MCP servers published by developers or companies are compatible with any MCP client. This openness has created a thriving ecosystem of thousands of community-built servers, accelerating the availability of tools and applications for AI assistants..

Makes software AI-accessible by design— Traditional software is built for humans using web interfaces. MCP provides a parallel interface designed for AI interaction, allowing applications to become truly AI-native. This means better, more reliable integrations between AI models and the tools people already use.

### A foundational protocol for agents

MCP creates the infrastructure for AI agents to access any number of services and tools, creating true end-to-end task automation. As more applications adopt the protocol, the vision of AI agents that can independently handle complex, multi-step workflows becomes increasingly practical.

## Who is MCP for?

Developers get a standardized way to build integrations once and have them work with any compatible AI. Enterprises gain secure, IT-controlled AI connectivity that scales across their organization. Consumers can connect their favorite tools to AI instantly, with no technical knowledge required.

### For developers: one standard for connecting AI to applications

Developers can follow a single standard to connect external products to your AI applications and agents. This simplifies the process of building integrations, grows the number of available products to connect to, and improves the overall quality and security of connectivity in the ecosystem.

Building an agent that will connect to many applications? Building an application that will connect to many agents? MCP provides you with access to an ecosystem of compatible tools with streamlined integration.

### For enterprises: secure, scalable AI connectivity across your organization

Enterprises can drive internal adoption of AI tools and applications more effectively, as MCP simplifies the process of connecting your systems to AI. This helps make AI more connected within your organization, expanding its capabilities and usefulness for your staff.

### For consumers: instant access to your favorite tools

MCP provides end-users with seamless connectivity between their favorite AI assistants and work tools. It makes it easier to automate tasks and avoid copying and pasting across tabs. In short, MCP gives AI greater access and connectivity to your world.

In[Claude](https://claude.ai), you can instantly connect to MCP Servers, known as[Connectors](https://claude.com/partners/mcp). This provides you with a straightforward way to connect [Claude](https://claude.ai) to your favorite work apps.

## Connectors (MCP) in action

The real value of MCP becomes clear when you see it in action with the tools you already use. Here are some examples of MCP being used to power integrations in Claude, known asConnectors:

### Canva in Claude

The Canva Connector allows Claude to generate new designs directly within Canva. Using MCP, Claude can connect to the tools Canva provides to generate designs on the canvas.

### Notion and Linear in Claude

Using the Notion and Linear Connectors, Claude can access your pages in Notion and use them to update tickets in Linear. Here MCP creates a seamless transfer of unstructured context into organized tickets in a separate project management system.

### Figma in Claude Code

The Figma Connector allows Claude to access designs within Figma. This lets Claude Code create working prototypes of websites, applications, or user interfaces based on designs created in Figma.

### Available Claude Connectors

Claude Connectors include integrations for:

- Notionfor workspace documentation

- Linearfor issue tracking

- Stripefor payment data

- CanvaandFigmafor design assistance

- Hubspotfor automating CRM tasks

- Sentryfor error tracking

- ...and many more

Each connector takes just a few seconds to configure to become part of Claude's working context. Outside of Claude, there is an ecosystem of MCP servers on the[open-source MCP Registry](https://modelcontextprotocol.io).

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6920e9d8382558e1ff64db3e_68e948c50eec666207cdd811_2.png)

## Start exploring MCP

Two paths exist based on your needs.

### Connectors in Claude

[Connectors](https://claude.com/partners/mcp)are pre-built, giving [Claude](https://claude.ai/directory) instant access to tools, databases, and applications, and providing you with a new set of capabilities. Open[Claude](https://claude.ai/directory), browse available connectors, and click to add them.

### Build custom MCP connections

MCP is open-source, meaning that anyone can adopt MCP to connect AI to applications. The[Model Context Protocol documentation](https://modelcontextprotocol.io)walks through how to build with MCP.

## Getting started

If you want to try MCP, start by browsing for a Claude Connector you can immediately start using with Claude.

If an existing MCP server doesn't already exist, creating your own takes some work, but isn't too complex if you know TypeScript or Python. The[Model Context Protocol quickstart](https://modelcontextprotocol.io/quickstart)has working examples you can modify for your needs.

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

### MCP は Claude 専用ですか？

いいえ。MCP はオープンソースのプロトコルです。Claude が MCP 採用の先駆けですが、現在では他の AI プロバイダーも同じプロトコルを採用しているため、誰でも MCP サーバーの同じエコシステムに接続できます。

### MCP を使用するにはプログラミングスキルが必要ですか？

[コネクタ](https://claude.com/partners/mcp)を使用する場合は不要です。参照、インストール、認証を行います。以上です。カスタム MCP サーバーを構築するには TypeScript または Python の知識が必要ですが、拡大中の[コネクタ](https://claude.com/partners/mcp)ライブラリはほとんどの主要なツールに対応しています。

### MCP のセキュリティはどのように機能しますか？

各サーバーは、Claude にアクセスを許可する特定の権限を要求します。アクセスの承認または拒否が可能で、また、許可はいつでも取り消すことができます。

### MCP でのパフォーマンスはどのようなものですか？

MCP は効率的なプロトコルを使用しています。ローカルサーバー用の stdio トランスポートにより、オーバーヘッドが最小化できます。リモートサーバー用のサーバー送信イベント (SSE) と Streamable HTTP により、永続的な接続が維持されます。レスポンスストリーミングにより、大量のデータ操作でのタイムアウトを防止します。このプロトコルにより、ページネーション、フィルタリング、パーシャルレスポンスをサポートし、大規模なデータセットを効率的に処理します。

関連投稿

Claudeを活用した構築チーム向けの製品ニュースやベストプラクティスに関するその他の情報を提供します。

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d226da492fb9f7f815ba_1c3d1af62032009538b8bf5864139ca124b06741-1000x1000.svg)

### 企業全体のチームに向けた Cowork とプラグイン

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22bed4b18b6703cd710_e750c875fbd7f08ffb6495efa180a8ed60de3611-1000x1000.svg)

### Building agents that reach production systems with MCP

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225588ad176f7c4aafd_abc884c723daea810d2e986455358281a2f94102-1000x1000.svg)

### Harnessing Claude’s intelligence

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22e13864f88ea55c2d8_b5c98d26c46edc43193e7f7e28a00633a538bb9c-1000x1000.svg)

### スキル解説：スキルとプロンプト、プロジェクト、MCP、サブエージェントとの比較

## 開発を始める

開発者向けニュースレターを入手

製品の最新情報、操作方法、コミュニティスポットライトなどを掲載しています。毎月受信トレイにお届けします。

毎月の開発者向けニュースレターを受け取りたい場合は、メールアドレスを入力してください。購読はいつでも解除できます。

---
**Source:** https://claude.com/ja/blog/what-is-model-context-protocol
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
