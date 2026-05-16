# Creating Isolated Sub-Agents in Claude Code

This guide covers three approaches for creating isolated sub-agents with specific tools and restricted access.

## Three Approaches

| Approach | Best For | Tool Isolation | Custom Tools |
|----------|----------|----------------|--------------|
| Headless CLI | Scripts, CI/CD, quick tasks | `--allowedTools` flag | Via `--mcp-config` |
| Agent SDK | Production apps, complex workflows | `allowedTools` option | Via `mcpServers` |
| Filesystem agents | Persistent, shareable agents | `tools` field in YAML | Inherits from session |

---

## 1. Headless CLI Mode (Simplest)

Run Claude Code non-interactively with restricted tools:

```bash
# Basic isolated agent with specific tools
claude -p "Analyze the auth module for security issues" \
  --allowedTools "Read,Grep,Glob" \
  --permission-mode bypassPermissions

# With custom system prompt
claude -p "Review this code" \
  --allowedTools "Read,Grep,Glob,Bash" \
  --append-system-prompt "You are a security expert. Focus only on vulnerabilities."

# With MCP servers for custom tools
claude -p "Query the database" \
  --allowedTools "Read,mcp__database__query" \
  --mcp-config ./mcp-config.json

# Resume a previous session
claude -p --resume "session-id" "Continue the analysis"

# JSON output for programmatic parsing
claude -p "Analyze code" --output-format json --allowedTools "Read,Grep"
```

### Key CLI Flags

| Flag | Description |
|------|-------------|
| `-p`, `--print` | Non-interactive/headless mode |
| `--allowedTools` | Comma-separated list of permitted tools |
| `--permission-mode` | `default`, `acceptEdits`, `bypassPermissions` |
| `--append-system-prompt` | Add custom instructions to system prompt |
| `--mcp-config` | Path to MCP server configuration JSON |
| `--output-format` | `text`, `json`, or `stream-json` |
| `--resume`, `-r` | Resume a previous session by ID |
| `--continue`, `-c` | Continue most recent session |

### Example: SRE Incident Bot

```bash
investigate_incident() {
    local incident_description="$1"
    local severity="${2:-medium}"

    claude -p "Incident: $incident_description (Severity: $severity)" \
      --append-system-prompt "You are an SRE expert. Diagnose and suggest fixes." \
      --output-format json \
      --allowedTools "Bash,Read,Grep,WebSearch" \
      --mcp-config monitoring-tools.json
}
```

---

## 2. Claude Agent SDK (Most Flexible)

### TypeScript

```typescript
import { query } from '@anthropic-ai/claude-agent-sdk';

for await (const message of query({
  prompt: "Analyze auth.py for security issues",
  options: {
    // Isolate main agent to read-only tools
    allowedTools: ["Read", "Grep", "Glob"],
    permissionMode: "bypassPermissions",

    // Define specialized sub-agents with their own tool restrictions
    agents: {
      'security-scanner': {
        description: 'Security analysis specialist. Use for vulnerability scanning.',
        prompt: `You are a security expert specializing in code vulnerability analysis.

Focus on:
- SQL injection
- XSS vulnerabilities
- Authentication bypasses
- Sensitive data exposure

Report findings with severity levels and specific line references.`,
        tools: ['Read', 'Grep', 'Glob'],  // Read-only access
        model: 'sonnet'
      },
      'test-runner': {
        description: 'Test execution specialist. Use for running and analyzing tests.',
        prompt: 'You are a test automation expert...',
        tools: ['Bash', 'Read', 'Grep'],  // Can execute but not edit
        model: 'haiku'  // Faster model for simple tasks
      }
    }
  }
})) {
  if (message.type === "result" && message.subtype === "success") {
    console.log(message.result);
  }
}
```

### Python

```python
from claude_agent_sdk import query, ClaudeAgentOptions
import asyncio

async def main():
    async for message in query(
        prompt="Analyze auth.py for security issues",
        options=ClaudeAgentOptions(
            allowed_tools=["Read", "Grep", "Glob"],
            permission_mode="bypassPermissions",
            agents={
                'security-scanner': {
                    'description': 'Security analysis specialist',
                    'prompt': 'You are a security expert...',
                    'tools': ['Read', 'Grep', 'Glob'],
                    'model': 'sonnet'
                }
            }
        )
    ):
        print(message)

asyncio.run(main())
```

### AgentDefinition Configuration

| Field | Type | Required | Description |
|:------|:-----|:---------|:------------|
| `description` | `string` | Yes | When to use this agent (include "PROACTIVELY" for auto-invocation) |
| `prompt` | `string` | Yes | System prompt defining role and behavior |
| `tools` | `string[]` | No | Allowed tools. Omit to inherit all tools |
| `model` | `'sonnet' \| 'opus' \| 'haiku' \| 'inherit'` | No | Model override |

### Common Tool Combinations

```typescript
// Read-only analysis agent
tools: ['Read', 'Grep', 'Glob']

// Test execution agent
tools: ['Bash', 'Read', 'Grep']

// Code modification agent
tools: ['Read', 'Edit', 'Write', 'Grep', 'Glob']

// Full access (or omit tools field)
tools: ['Read', 'Edit', 'Write', 'Bash', 'Grep', 'Glob', 'WebSearch', 'WebFetch']
```

---

## 3. Filesystem-Based Agents (Persistent/Shareable)

### File Locations

| Type | Location | Scope | Priority |
|:-----|:---------|:------|:---------|
| Project agents | `.claude/agents/*.md` | Current project only | Highest |
| User agents | `~/.claude/agents/*.md` | All projects | Lower |

### Agent File Format

Create `.claude/agents/security-scanner.md`:

```markdown
---
name: security-scanner
description: Security analysis specialist. Use PROACTIVELY for vulnerability scanning.
tools: Read, Grep, Glob
model: sonnet
permissionMode: bypassPermissions
---

You are a security expert specializing in code vulnerability analysis.

## Focus Areas
- SQL injection
- XSS vulnerabilities
- Authentication bypasses
- Sensitive data exposure
- Hardcoded secrets

## Output Format
Report findings with:
1. Severity level (Critical/High/Medium/Low)
2. File path and line number
3. Description of the vulnerability
4. Recommended fix
```

### Configuration Fields

| Field | Required | Description |
|:------|:---------|:------------|
| `name` | Yes | Unique identifier (lowercase, hyphens) |
| `description` | Yes | When to invoke this agent |
| `tools` | No | Comma-separated tool list. Omit to inherit all |
| `model` | No | `sonnet`, `opus`, `haiku`, or `inherit` |
| `permissionMode` | No | `default`, `acceptEdits`, `bypassPermissions` |
| `skills` | No | Comma-separated skills to auto-load |

### CLI-Based Dynamic Agents

```bash
claude --agents '{
  "code-reviewer": {
    "description": "Expert code reviewer. Use proactively after code changes.",
    "prompt": "You are a senior code reviewer. Focus on quality and security.",
    "tools": ["Read", "Grep", "Glob", "Bash"],
    "model": "sonnet"
  }
}'
```

---

## 4. Adding Custom Tools via MCP

### TypeScript Example

```typescript
import { query, tool, createSdkMcpServer } from "@anthropic-ai/claude-agent-sdk";
import { z } from "zod";

// Define custom tools
const customTools = createSdkMcpServer({
  name: "my-tools",
  version: "1.0.0",
  tools: [
    tool(
      "query_database",
      "Execute a read-only SQL query",
      {
        sql: z.string().describe("SQL SELECT query to execute")
      },
      async (args) => {
        const result = await db.query(args.sql);
        return {
          content: [{ type: "text", text: JSON.stringify(result, null, 2) }]
        };
      }
    ),
    tool(
      "get_metrics",
      "Fetch application metrics",
      {
        metric_name: z.string(),
        time_range: z.enum(["1h", "24h", "7d", "30d"])
      },
      async (args) => {
        const metrics = await fetchMetrics(args.metric_name, args.time_range);
        return {
          content: [{ type: "text", text: `${args.metric_name}: ${metrics}` }]
        };
      }
    )
  ]
});

// Use with tool isolation
async function* generateMessages() {
  yield {
    type: "user" as const,
    message: {
      role: "user" as const,
      content: "Get the user signup metrics for the last 24 hours"
    }
  };
}

for await (const msg of query({
  prompt: generateMessages(),
  options: {
    mcpServers: { "my-tools": customTools },
    // Only allow specific custom tools - no file access
    allowedTools: [
      "mcp__my-tools__query_database",
      "mcp__my-tools__get_metrics"
    ]
  }
})) {
  console.log(msg);
}
```

### Python Example

```python
from claude_agent_sdk import query, tool, create_sdk_mcp_server, ClaudeAgentOptions
from typing import Any
import json

@tool("query_database", "Execute a read-only SQL query", {"sql": str})
async def query_database(args: dict[str, Any]) -> dict[str, Any]:
    result = await db.query(args["sql"])
    return {
        "content": [{"type": "text", "text": json.dumps(result, indent=2)}]
    }

@tool("get_metrics", "Fetch application metrics", {"metric_name": str, "time_range": str})
async def get_metrics(args: dict[str, Any]) -> dict[str, Any]:
    metrics = await fetch_metrics(args["metric_name"], args["time_range"])
    return {
        "content": [{"type": "text", "text": f"{args['metric_name']}: {metrics}"}]
    }

custom_server = create_sdk_mcp_server(
    name="my-tools",
    version="1.0.0",
    tools=[query_database, get_metrics]
)

async for message in query(
    prompt="Get user signup metrics for 24h",
    options=ClaudeAgentOptions(
        mcp_servers={"my-tools": custom_server},
        allowed_tools=[
            "mcp__my-tools__query_database",
            "mcp__my-tools__get_metrics"
        ]
    )
):
    print(message)
```

### MCP Tool Naming Convention

Tools from MCP servers follow this pattern:
```
mcp__{server_name}__{tool_name}
```

Example: A tool named `query_database` in server `my-tools` becomes:
```
mcp__my-tools__query_database
```

---

## 5. Example Use Cases

### CI/CD Security Scanner

```bash
#!/bin/bash
# .github/scripts/security-scan.sh

claude -p "Scan the codebase for security vulnerabilities. Focus on:
- Hardcoded secrets
- SQL injection risks
- XSS vulnerabilities
- Insecure dependencies

Output a JSON report." \
  --allowedTools "Read,Grep,Glob" \
  --permission-mode bypassPermissions \
  --output-format json > security-report.json
```

### Multi-Agent Code Review Pipeline

```typescript
import { query } from '@anthropic-ai/claude-agent-sdk';

const reviewPipeline = query({
  prompt: "Review PR #123 comprehensively",
  options: {
    agents: {
      'style-checker': {
        description: 'Code style and formatting reviewer',
        prompt: 'Check for style guide violations...',
        tools: ['Read', 'Grep', 'Glob'],
        model: 'haiku'  // Fast for simple checks
      },
      'security-scanner': {
        description: 'Security vulnerability scanner',
        prompt: 'Identify security issues...',
        tools: ['Read', 'Grep', 'Glob'],
        model: 'sonnet'
      },
      'test-analyzer': {
        description: 'Test coverage analyzer',
        prompt: 'Analyze test coverage...',
        tools: ['Bash', 'Read', 'Grep'],
        model: 'sonnet'
      }
    }
  }
});
```

### Database Analysis Agent (Read-Only)

```typescript
const dbAnalyzer = query({
  prompt: "Analyze query performance and suggest optimizations",
  options: {
    mcpServers: { "postgres": postgresServer },
    allowedTools: [
      "mcp__postgres__explain_query",  // EXPLAIN only
      "mcp__postgres__list_indexes",
      "mcp__postgres__table_stats"
      // No INSERT/UPDATE/DELETE tools
    ],
    agents: {
      'query-optimizer': {
        description: 'SQL query optimization specialist',
        prompt: 'Analyze queries and suggest index improvements...',
        tools: ['mcp__postgres__explain_query', 'mcp__postgres__list_indexes']
      }
    }
  }
});
```

---

## Reference Documentation

| Topic | File |
|-------|------|
| Sub-agents overview | `code-claude-docs/sub-agents.md` |
| Headless mode | `code-claude-docs/headless.md` |
| CLI reference | `code-claude-docs/cli-reference.md` |
| SDK sub-agents | `platform-docs/developer-guide/agent-sdk__subagents.md` |
| Custom MCP tools | `platform-docs/developer-guide/agent-sdk__custom-tools.md` |
| Settings & tools list | `code-claude-docs/settings.md` |

---

## Available Built-in Tools

| Tool | Description |
|------|-------------|
| `Read` | Read files |
| `Write` | Create new files |
| `Edit` | Modify existing files |
| `Bash` | Run shell commands |
| `Glob` | Find files by pattern |
| `Grep` | Search file contents |
| `WebSearch` | Search the web |
| `WebFetch` | Fetch and parse URLs |
| `Task` | Spawn sub-agents |
| `TodoWrite` | Manage task lists |
| `NotebookEdit` | Edit Jupyter notebooks |
