---
description: Sync all Anthropic documentation sources (project)
allowed-tools: Bash(.venv/bin/python3 scripts/*:*), Bash(curl *), Read, Glob, Task
---

# Documentation Sync Task

Run all documentation fetchers **in parallel** to update the local mirror of Anthropic docs. The fetchers use HTTP conditional requests (ETag/If-Modified-Since) for efficient incremental updates.

## Steps to Execute

1. **Run all fetchers in parallel** using the Task tool to spawn 10 agents simultaneously:
   - `.venv/bin/python3 scripts/fetch_platform_docs.py --skip-indexes`
   - `.venv/bin/python3 scripts/fetch_code_claude_docs.py --skip-indexes`
   - `.venv/bin/python3 scripts/fetch_engineering_blog.py --skip-indexes`
   - `.venv/bin/python3 scripts/fetch_claude_blog.py --skip-indexes`
   - `.venv/bin/python3 scripts/fetch_support_docs.py --rediscover --skip-indexes`
   - `.venv/bin/python3 scripts/fetch_anthropic_research.py --skip-indexes`
   - `.venv/bin/python3 scripts/fetch_anthropic_news.py --skip-indexes`
   - `.venv/bin/python3 scripts/fetch_mcp_docs.py --skip-indexes`
   - `.venv/bin/python3 scripts/fetch_mcp_blog.py --skip-indexes`
   - `.venv/bin/python3 scripts/fetch_agentskills_docs.py --skip-indexes`

   Use `subagent_type: "general-purpose"` for each agent. Each agent should run its fetcher and report: total docs, new/updated/unchanged counts, and any failures.

2. **Wait for all agents** to complete and collect their results.

3. **Fetch Claude Code CHANGELOG** for tracking releases:
   ```bash
   curl -s https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md -o code-claude-docs/CHANGELOG.md
   ```

4. **Regenerate indexes once** after all fetchers complete:
   ```bash
   .venv/bin/python3 scripts/generate_indexes.py
   ```

5. **Summarize results** in a table showing:
   - Total documents per source
   - New/updated/unchanged counts
   - Any errors encountered

## CLI Options Available

- `--force` - Force full re-fetch, ignoring cache
- `--dry-run` - Show what would be fetched without downloading
- `--concurrency N` - Max concurrent requests (default: 5-10)
- `--rediscover` - (support docs only) Refresh article discovery cache
- `--skip-indexes` - Skip index regeneration (used for parallel fetching)

## Expected Sources

| Source | Fetcher | Typical Count |
|--------|---------|---------------|
| Platform Docs | fetch_platform_docs.py | ~527 |
| Claude Code Docs | fetch_code_claude_docs.py | ~48 |
| MCP Docs | fetch_mcp_docs.py | ~162 |
| MCP Blog | fetch_mcp_blog.py | ~15 |
| AgentSkills Docs | fetch_agentskills_docs.py | ~4 |
| Anthropic Research | fetch_anthropic_research.py | ~129 |
| Anthropic News | fetch_anthropic_news.py | ~171 |
| Engineering Blog | fetch_engineering_blog.py | ~16 |
| Claude.com Blog | fetch_claude_blog.py | ~77 |
| Support Articles | fetch_support_docs.py | ~295 |

Run all fetchers in parallel now and report the combined results.
