# Managing context on the Claude Developer Platform
*September 29, 2025*
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22930b7622d6096c33d_4d663bd87c391c144b9bca513b3849ccfa00a3b9-1000x1000.svg)

# Managing context on the Claude Developer Platform

Introducing context editing and the memory tool to help developers build more effective agents that handle long-running tasks.

- CategoryProduct announcements

- ProductClaude Platform

- DateSeptember 29, 2025

- Reading time5min

- ShareCopy linkhttps://claude.com/blog/context-management

Today, we’re introducing new capabilities for managing your agents’ context on the Claude Developer Platform: context editing and the memory tool.

With our latest model,[Claude Sonnet 4.5](https://www.anthropic.com/news/claude-sonnet-4-5), these capabilities enable developers to build AI agents capable of handling long-running tasks at higher performance and without hitting context limits or losing critical information.

## Context windows have limits, but real work doesn’t

As production agents handle more complex tasks and generate more tool results, they often exhaust their effective context windows—leaving developers stuck choosing between cutting agent transcripts or degrading performance. Context management solves this in two ways, helping developers ensure only relevant data stays in context and valuable insights get preserved across sessions.

Context editingautomatically clears stale tool calls and results from within the context window when approaching token limits. As your agent executes tasks and accumulates tool results, context editing removes stale content while preserving the conversation flow, effectively extending how long agents can run without manual intervention. This also increases the effective model performance as Claude focuses only on relevant context.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6909051d7a73a4b74ba8767a_8ad2952bc0513750088cdfd309ee83ba0fd15438-1920x800.webp)

The memory toolenables Claude to store and consult information outside the context window through a file-based system. Claude can create, read, update, and delete files in a dedicated memory directory stored in your infrastructure that persists across conversations. This allows agents to build up knowledge bases over time, maintain project state across sessions, and reference previous learnings without having to keep everything in context.

The memory tool operates entirely client-side through tool calls. Developers manage the storage backend, giving them complete control over where the data is stored and how it’s persisted.

Claude Sonnet 4.5 enhances both capabilities with built-in context awareness—tracking available tokens throughout conversations to manage context more effectively.

Together, these updates create a system that improves agent performance:

- Enable longer conversations by automatically removing stale tool results from context

- Boost accuracy by saving critical information to memory—and bring that learning across successive agentic sessions

## Building long-running agents

Claude Sonnet 4.5 is the best model in the world for building agents. These features unlock new possibilities for long-running agents—processing entire codebases, analyzing hundreds of documents, or maintaining extensive tool interaction histories. Context management builds on this foundation, ensuring agents can leverage this expanded capacity efficiently while still handling workflows that extend beyond any fixed limit. Use cases include:

- Coding:Context editing clears old file reads and test results while memory preserves debugging insights and architectural decisions, enabling agents to work on large codebases without losing progress.

- Research:Memory stores key findings while context editing removes old search results, building knowledge bases that improve performance over time.

- Data processing:Agents store intermediate results in memory while context editing clears raw data, handling workflows that would otherwise exceed token limits.

## Performance improvements with context management

On an internal evaluation set for agentic search, we tested how context management improves agent performance on complex, multi-step tasks. The results demonstrate significant gains: combining the memory tool with context editing improved performance by 39% over baseline. Context editing alone delivered a 29% improvement.

In a 100-turn web search evaluation, context editing enabled agents to complete workflows that would otherwise fail due to context exhaustion—while reducing token consumption by 84%.

## Getting started

These capabilities are available today in public beta on the Claude Developer Platform, natively and in Amazon Bedrock and Google Cloud’s Vertex AI. Explore the documentation for[context editing](https://docs.claude.com/en/docs/build-with-claude/context-editing)and the[memory tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/memory-tool), or visit our[cookbook](https://platform.claude.com/cookbook/tool-use-memory-cookbook)to learn more.

Anthropic is not affiliated with, endorsed by, or sponsored by CATAN GmbH or CATAN Studio. The CATAN trademark and game are the property of CATAN GmbH.

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22e6fa9211768bbce0b_6e00dbffcddc82df5e471c43453abfc74ca94e8d-1000x1000.svg)

### Bringing Claude Code and Claude Cowork to government

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22949f86cd1968deb9f_33dbe8f783d4835a838b4c4ae85d3c04e352fee1-1000x1000.svg)

### Claude Design now stays on brand for daily work

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22a7bb714a55b503cd7_cad034e66b44f7f017c0cb931c403a97d1763758-1000x1000.svg)

### New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22bed4b18b6703cd710_e750c875fbd7f08ffb6495efa180a8ed60de3611-1000x1000.svg)

### New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels

## Transform how your organization operates with Claude

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

---
**Source:** https://claude.com/blog/context-management
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
