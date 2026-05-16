# Anthropic Documentation Hub

A comprehensive local mirror of all Anthropic documentation (~1,400 documents from 10 sources), optimized for fast searching and reference with Claude Code. Ask natural language questions about Claude features, APIs, and best practices without waiting for web searches. Essential for developers building with Claude who need instant access to official documentation.

## Quick Start

1. Clone: `git clone https://github.com/robgruhl/anthropic-docs-mirror.git`
2. Install: `pip3 install -r scripts/requirements.txt`
3. Use: Ask Claude Code questions or run `/ask How do I configure MCP servers?`

## What It Does

This repository provides fast local access to Claude documentation for:
- **Q&A** - Ask Claude Code questions about Claude features, APIs, and best practices
- **Development** - Reference official docs when implementing new features with Claude
- **Searchability** - Use Claude Code's grep/search tools across 1,400+ documents

## Documentation Coverage

| Source | Count | Description |
|--------|-------|-------------|
| Platform Docs | 486 | Developer guides, API reference, and resources from platform.claude.com |
| Claude Code Docs | 51 | Official Claude Code documentation from code.claude.com |
| MCP Docs | 164 | Model Context Protocol documentation from modelcontextprotocol.io |
| MCP Blog | 13 | MCP announcements from blog.modelcontextprotocol.io |
| AgentSkills Docs | 4 | AgentSkills documentation from agentskills.io |
| Anthropic Research | 96 | Research papers from anthropic.com/research |
| Anthropic News | 171 | News articles from anthropic.com/news |
| Engineering Blog | 16 | Technical deep-dives from anthropic.com/engineering |
| Claude.com Blog | 84 | Product announcements from claude.com/blog |
| Support Articles | 312 | Help documentation from support.claude.com |

**Total: ~1,400 documents** from 10 sources, organized through a two-tier index system with 81 topic indexes.

## Quick Start

### Browse Documentation

Start with the master index:
```
indexes/README.md
```

Or jump to specific topics:
```
indexes/topics/claude-code.md
indexes/topics/agent-sdk.md
indexes/topics/mcp.md
indexes/topics/hooks.md
indexes/topics/api.md
```

### Search with Claude Code

Ask Claude Code to search the documentation:
```
Find all mentions of hooks in the Claude Code docs
What does the API documentation say about streaming?
Show me examples of MCP server configuration
```

## Workflow

### Sync Documentation

Run the `/sync-docs` slash command to fetch the latest documentation:
```
/sync-docs
```

This runs all 10 fetchers in parallel:
- `scripts/fetch_platform_docs.py`
- `scripts/fetch_code_claude_docs.py`
- `scripts/fetch_mcp_docs.py`
- `scripts/fetch_mcp_blog.py`
- `scripts/fetch_agentskills_docs.py`
- `scripts/fetch_anthropic_research.py`
- `scripts/fetch_anthropic_news.py`
- `scripts/fetch_engineering_blog.py`
- `scripts/fetch_claude_blog.py`
- `scripts/fetch_support_docs.py`

### Create Slack Update

After syncing, generate a Slack-formatted summary:
```
/slack-update
```

This creates a file in `slack-updates/` ready to post to Slack.

### Manual Sync

You can also run fetchers directly:
```bash
python3 scripts/fetch_platform_docs.py
python3 scripts/fetch_code_claude_docs.py
python3 scripts/fetch_mcp_docs.py
python3 scripts/fetch_mcp_blog.py
python3 scripts/fetch_agentskills_docs.py
python3 scripts/fetch_anthropic_research.py
python3 scripts/fetch_anthropic_news.py
python3 scripts/fetch_engineering_blog.py
python3 scripts/fetch_claude_blog.py
python3 scripts/fetch_support_docs.py
```

CLI options:
- `--force` - Force full re-fetch, ignoring cache
- `--dry-run` - Show what would be fetched without downloading
- `--concurrency N` - Max concurrent requests (default: 5-10)

## Repository Structure

```
anthropic-docs/
├── platform-docs/          # Platform documentation (486 files)
│   ├── developer-guide/    # Main docs (models, features, tools)
│   ├── api-reference/      # API endpoint documentation
│   └── resources/          # Prompt library, use cases
├── code-claude-docs/       # Claude Code documentation (51 files)
├── mcp-docs/               # MCP documentation (164 files)
│   ├── docs/               # Getting started, tutorials, SDK docs
│   ├── specification/      # Protocol spec (multiple versions)
│   └── community/          # Governance, SEPs
├── mcp-blog/               # MCP blog posts (13 files)
├── agentskills-docs/       # AgentSkills documentation (4 files)
├── anthropic-research/     # Research papers (96 files)
├── anthropic-news/         # News articles (171 files)
├── engineering-blog/       # Engineering blog posts (16 files)
├── claude-blog/            # Product blog posts (84 files)
├── docs-support/           # Support articles (312 files)
├── indexes/                # Generated index system
│   ├── README.md           # Master index
│   └── topics/             # 81 topic-based indexes
├── scripts/                # Fetcher scripts (10 fetchers)
├── slack-updates/          # Slack update summaries
└── .claude/commands/       # Slash commands
```

## Slash Commands

| Command | Description |
|---------|-------------|
| `/ask <question>` | Search local docs to answer a question |
| `/ask --slack <question>` | Same as above, but outputs Slack-formatted response |
| `/sync-docs` | Sync all 10 documentation sources in parallel |
| `/slack-update` | Generate Slack-formatted update summary |

## Requirements

- Python 3.10+
- Dependencies: `pip3 install -r scripts/requirements.txt`

## License

Documentation content belongs to Anthropic. This repository mirrors publicly available documentation for local reference.
