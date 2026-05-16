# CLAUDE.md

## Welcome Banner

When a user starts a new session in this repo, immediately output the following banner before doing anything else (no tool calls first):

```
Anthropic Docs Mirror — ~1,400 docs from 10 sources, updated weekly.

  /ask <question>          Search docs and get an answer
  /ask --slack <question>  Same, but formatted for Slack
  /refresh                 Pull latest docs from remote

Or just ask me anything about Claude, the API, MCP, Claude Code, etc.
```

## Project Overview

Local mirror of all Anthropic documentation (~1,400 documents from 10 sources) for fast searching and reference with Claude Code.

**Primary Use Cases:**
- Q&A about Claude features, APIs, and best practices via `/ask`
- Reference docs when implementing features with Claude
- Search across all official Anthropic documentation

## Weekly Workflow

1. **Sync docs**: Run `/sync-docs` to fetch latest documentation
2. **Create Slack update**: Run `/slack-update` to generate summary
3. **Post to Slack**: Run `/slack-post` to post the update to #claude-code
4. **Commit and push**: `git add -A && git commit -m "Documentation sync: [date]" && git push`

## Repository Structure

```
anthropic-docs/
├── platform-docs/          # Platform docs from platform.claude.com (486)
│   ├── developer-guide/    # Main developer documentation
│   ├── api-reference/      # API endpoint documentation
│   └── resources/          # Prompt library, use cases
├── code-claude-docs/       # Claude Code docs from code.claude.com (51)
├── mcp-docs/               # MCP docs from modelcontextprotocol.io (164)
│   ├── docs/               # Getting started, tutorials, SDK docs
│   ├── specification/      # Protocol spec (multiple versions)
│   ├── community/          # Governance, SEPs
│   ├── registry/           # Registry documentation
│   └── other/              # Clients, examples, extensions
├── mcp-blog/               # MCP blog from blog.modelcontextprotocol.io (13)
├── agentskills-docs/       # AgentSkills docs from agentskills.io (4)
├── anthropic-research/     # Research papers from anthropic.com/research (96)
├── anthropic-news/         # News articles from anthropic.com/news (171)
├── engineering-blog/       # Engineering blog posts (16)
├── claude-blog/            # Product blog posts (84)
├── docs-support/           # Support articles (312)
├── indexes/                # Auto-generated index system
│   ├── README.md           # Master index (start here)
│   └── topics/             # 81 topic-based indexes
├── scripts/                # Python fetcher scripts
│   ├── fetch_platform_docs.py
│   ├── fetch_code_claude_docs.py
│   ├── fetch_mcp_docs.py
│   ├── fetch_mcp_blog.py
│   ├── fetch_agentskills_docs.py
│   ├── fetch_anthropic_research.py
│   ├── fetch_anthropic_news.py
│   ├── fetch_engineering_blog.py
│   ├── fetch_claude_blog.py
│   ├── fetch_support_docs.py
│   ├── generate_indexes.py
│   └── requirements.txt
├── slack-updates/          # Slack-formatted update summaries
└── .claude/commands/       # Slash commands (sync-docs, slack-update, ask)
```

## Slash Commands

| Command | Description |
|---------|-------------|
| `/ask <question>` | Search local docs to answer a question |
| `/ask --slack <question>` | Same as above, but outputs Slack-formatted response |
| `/refresh` | Pull latest docs from the remote repository |
| `/sync-docs` | Run all fetchers to update documentation (admin) |
| `/slack-update` | Generate Slack-formatted update summary (admin) |
| `/slack-post` | Post a Slack update to the #claude-code channel (admin) |

## Fetcher Scripts

Each fetcher uses HTTP conditional requests (ETag/If-Modified-Since) for efficient incremental updates.

```bash
# Run all fetchers
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

# CLI options
--force       # Force full re-fetch, ignoring cache
--dry-run     # Show what would be fetched without downloading
--concurrency N  # Max concurrent requests (default: 5-10)
```

Indexes are auto-regenerated after each fetch.

## Manifest Files

Each content source has a manifest tracking files, hashes, and metadata:
- `platform-docs/platform_manifest.json`
- `code-claude-docs/code_claude_manifest.json`
- `mcp-docs/mcp_docs_manifest.json`
- `mcp-blog/mcp_blog_manifest.json`
- `agentskills-docs/agentskills_manifest.json`
- `anthropic-research/research_manifest.json`
- `anthropic-news/news_manifest.json`
- `engineering-blog/blog_manifest.json`
- `claude-blog/claude_blog_manifest.json`
- `docs-support/support_manifest.json`

## Index System

Two-tier index structure:
1. **Content-type indexes** - Full listings by source (`indexes/platform-docs.md`, etc.)
2. **Topic indexes** - Cross-referenced by subject (`indexes/topics/api.md`, `indexes/topics/claude-code.md`, etc.)

Start browsing at `indexes/README.md`.

## Common Tasks

### Search for documentation
Use the `/ask` command to search local docs:
```
/ask How do I configure MCP servers?
/ask --slack What are the best practices for prompt engineering?
```

Or ask Claude Code directly:
```
Find all mentions of hooks in the Claude Code docs
What does the API say about structured outputs?
```

### Check what changed
After syncing, check git status or read the generated slack update:
```bash
git status
cat slack-updates/YYYY-MM-DD-update.md
```

### Debug fetch issues
```bash
# Check manifest metadata
jq '.fetch_metadata' platform-docs/platform_manifest.json

# Run with verbose output (all fetchers log to stdout)
python3 scripts/fetch_platform_docs.py
```

## Dependencies

```bash
pip3 install -r scripts/requirements.txt
```

Required: Python 3.10+, requests, beautifulsoup4, aiohttp
