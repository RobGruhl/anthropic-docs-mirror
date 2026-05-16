# Anthropic Documentation Hub - One Pager

## Problem Statement

Developers working with Claude need to frequently reference Anthropic's documentation across multiple sources (platform docs, API reference, support articles, blogs). Searching the web is slow, results are scattered, and context switching between browser and IDE breaks flow. When using Claude Code for development, there's no fast way to get authoritative answers about Claude's capabilities without leaving the terminal.

## Solution

A local mirror of all Anthropic documentation (~1,400 documents from 10 sources) that integrates directly with Claude Code. Developers can ask natural language questions and get instant, accurate answers sourced from official documentation. The `/ask` slash command provides a dedicated interface for documentation queries.

## How It Works

1. **Documentation Fetchers**: Python scripts crawl and download documentation from 10 Anthropic sources:
   - Platform docs (platform.claude.com) - 486 docs
   - Claude Code docs (code.claude.com) - 51 docs
   - MCP docs (modelcontextprotocol.io) - 164 docs
   - MCP blog (blog.modelcontextprotocol.io) - 13 posts
   - AgentSkills docs (agentskills.io) - 4 docs
   - Anthropic Research (anthropic.com/research) - 96 papers
   - Anthropic News (anthropic.com/news) - 171 articles
   - Engineering blog (anthropic.com/engineering) - 16 posts
   - Product blog (claude.com/blog) - 84 posts
   - Support articles (support.claude.com) - 312 articles

2. **Index System**: Auto-generated two-tier index organizes documents by content type and 81 topics for efficient navigation.

3. **Slash Commands**: Custom Claude Code commands enable:
   - `/ask <question>` - Search docs to answer questions
   - `/ask --slack <question>` - Same with Slack-formatted output
   - `/sync-docs` - Update all documentation (runs 10 fetchers in parallel)
   - `/slack-update` - Generate update summaries

4. **Incremental Updates**: Fetchers use HTTP conditional requests (ETag/If-Modified-Since) for efficient syncing.

## Key Features

- **~1,400 documents** from 10 official Anthropic sources
- **Natural language Q&A** via `/ask` command (with optional `--slack` output)
- **81 topic indexes** for organized browsing
- **Parallel fetching** - all 10 fetchers run concurrently for fast syncs
- **Incremental sync** with efficient HTTP conditional requests
- **Slack integration** for sharing documentation updates with the team

## Results / Impact

- Eliminates context switching between IDE and browser for documentation lookups
- Provides authoritative answers from official sources only
- Weekly sync keeps documentation current
- Enables team sharing of documentation updates via Slack

## What's Next

- Automated weekly sync via scheduled jobs
- Integration with additional documentation sources as they become available
