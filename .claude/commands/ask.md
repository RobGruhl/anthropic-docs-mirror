---
description: Search Anthropic docs to answer a question
argument-hint: [--slack] <question>
allowed-tools: Read, Grep, Glob, AskUserQuestion, Write
---

# Documentation Search Task

Answer the following question using the local Anthropic documentation mirror:

**Question:** $ARGUMENTS

## Slack Formatting Option

If the question starts with `--slack`, format the response for direct pasting into Slack:

**Formatting rules:**
- Use `*bold*` instead of `**bold**` (Slack doesn't support double asterisks)
- Use `_italic_` instead of `*italic*`
- NO markdown headers (`#`, `##`) - use `*Bold Text:*` for section titles
- NO markdown tables - use structured lists with `→` arrows instead
- Use `[text](url)` for links
- Use bullet points `•` or `- ` for lists
- Use backticks for `code` and file paths

**File output (for clean copy/paste):**
When `--slack` is used, ALSO write the complete Slack-formatted response to `slack-updates/ask-response.md` using the Write tool. This gives the user a clean file to copy from without terminal rendering issues.

After writing the file, end your response with:
```
📋 Slack-ready version saved to: slack-updates/ask-response.md
```

## Clarifying Questions (If Needed)

If the question is unclear or ambiguous, you may ask ONE round of clarifying questions using the AskUserQuestion tool before searching. Only do this if genuinely needed - if the question is clear enough to research, proceed directly to searching.

## Important: Use Local Documentation Only

This repository contains a comprehensive mirror of ~1,400 Anthropic documents. **Do NOT use WebFetch** - the local docs are complete and searching them is faster and more thorough than web fetching.

## Documentation Structure

There are 10 doc sources. Each covers different material — knowing what's in each one helps you search the right places.

### Primary technical references (search first for "how do I" questions)

| Directory | Content | Count | What's in it |
|-----------|---------|-------|--------------|
| `code-claude-docs/` | Claude Code docs from code.claude.com | ~50 | Claude Code features: CLAUDE.md, skills, rules, plugins, subagents, hooks, settings, MCP, permissions, CLI reference. The canonical source for Claude Code configuration. |
| `platform-docs/` | Developer docs from platform.claude.com | ~484 | API reference (all SDKs), prompt engineering, tool use, agent patterns, Agent Skills (API-side), structured outputs, vision, embeddings. Also covers enterprise Agent Skills governance and the Skills API. |
| `mcp-docs/` | MCP docs from modelcontextprotocol.io | ~162 | MCP protocol specification, SDK docs (TypeScript, Python), tutorials, server development guides, registry. |

### Blog posts and announcements (search for context, examples, and "why")

| Directory | Content | Count | What's in it |
|-----------|---------|-------|--------------|
| `claude-blog/` | Product blog from claude.com/blog | ~84 | Product announcements, practical guides (CLAUDE.md best practices, skills creation walkthroughs, plugin system), how Anthropic teams use Claude, agentic coding guides. Rich with real-world examples and use cases. |
| `engineering-blog/` | Engineering blog from anthropic.com/engineering | ~18 | Deep technical posts: building effective agents, context engineering, prompt engineering overview, MCP best practices. High signal-to-noise. |
| `anthropic-news/` | News from anthropic.com/news | ~171 | Model launches, partnership announcements, safety reports, policy updates. Good for "when was X released" or "what's new in Y model." |
| `mcp-blog/` | MCP blog from blog.modelcontextprotocol.io | ~13 | MCP ecosystem updates, new transport protocols, community highlights. |

### Support and specialized content (search for troubleshooting and org management)

| Directory | Content | Count | What's in it |
|-----------|---------|-------|--------------|
| `docs-support/` | Support articles from support.anthropic.com | ~315 | How-to guides, troubleshooting, org administration (provisioning skills, managing teams), Claude.ai features (Projects, Styles, Artifacts), billing, account management. Covers the Claude.ai web app, NOT Claude Code. |
| `anthropic-research/` | Research papers from anthropic.com/research | ~96 | Interpretability, alignment, safety evaluations, economic impact studies, red teaming. For deep technical/research questions. |
| `agentskills-docs/` | Agent Skills standard from agentskills.io | ~4 | The open Agent Skills specification. What skills are, how to integrate them, the formal spec. |

### When to search beyond the primary reference

- **Claude Code questions** → Start with `code-claude-docs/`, then check `claude-blog/` for practical guides and examples.
- **API/SDK questions** → Start with `platform-docs/`, then `engineering-blog/` for patterns.
- **"How do I manage X for my org/team"** → Check `docs-support/` (org admin), `platform-docs/` (enterprise Skills), and `code-claude-docs/` (managed settings, plugins).
- **Skills/plugins questions** → Search ALL of: `code-claude-docs/` (Claude Code skills), `platform-docs/` (API Skills), `claude-blog/` (guides and announcements), `docs-support/` (org provisioning), `agentskills-docs/` (open standard). Note: "Skills" means different things in different contexts — Claude Code skills (`.claude/skills/`), Claude.ai Skills (web app), and API Skills (`/v1/skills`) are related but have different distribution mechanisms.
- **Best practices / patterns** → Check `engineering-blog/` and `claude-blog/` — these have the richest practical guidance.
- **"What changed" / "What's new"** → Check `anthropic-news/` and `claude-blog/`.
- **MCP questions** → Start with `mcp-docs/`, then `code-claude-docs/` for Claude Code MCP config, then `engineering-blog/` for best practices.

**Index System:**
- Master index: `indexes/README.md`
- Topic indexes: `indexes/topics/*.md` (77+ topics covering API, MCP, hooks, tools, agents, etc.)

## Search Strategy

### Step 1: Understand the Scope
Read `indexes/README.md` to see all available topics and document counts.

### Step 2: Find Relevant Topic Indexes
Search topic index filenames and content for keywords from the question:
```
Grep pattern="<keyword>" path="indexes/topics/" output_mode="files_with_matches"
```

Topic indexes group documents by subject across all sources, making them excellent starting points.

### Step 3: Read Topic Indexes
Read the relevant topic index files (e.g., `indexes/topics/mcp.md`, `indexes/topics/hooks.md`). Each lists documents from all 7 sources with file paths.

### Step 4: Search Documentation Content
Search within documentation directories for specific terms. Always search the primary references, and add supplemental sources based on the question type (see "When to search beyond the primary reference" above):

**Always search (primary references):**
```
Grep pattern="<term>" path="code-claude-docs/" output_mode="files_with_matches"
Grep pattern="<term>" path="platform-docs/" output_mode="files_with_matches"
Grep pattern="<term>" path="mcp-docs/" output_mode="files_with_matches"
```

**Search for practical guidance, examples, and announcements:**
```
Grep pattern="<term>" path="claude-blog/" output_mode="files_with_matches"
Grep pattern="<term>" path="engineering-blog/" output_mode="files_with_matches"
Grep pattern="<term>" path="docs-support/" output_mode="files_with_matches"
```

**Search for news, research, and specialized content (when relevant):**
```
Grep pattern="<term>" path="anthropic-news/" output_mode="files_with_matches"
Grep pattern="<term>" path="anthropic-research/" output_mode="files_with_matches"
Grep pattern="<term>" path="mcp-blog/" output_mode="files_with_matches"
Grep pattern="<term>" path="agentskills-docs/" output_mode="files_with_matches"
```

Run searches in parallel. Aim to source from at least 2-3 different doc categories when possible — the primary references give you the "what", and the blogs/support docs give you the "why" and "how others use it."

### Step 5: Read and Synthesize
Read as many documents as needed to fully answer the question. Don't artificially limit yourself - if the question requires reading 10 or 30 or 50 documents, read all of those documents.

## Response Format

Provide:
1. **Direct answer** to the question
2. **Supporting details** from the documentation
3. **Source references** with both local file paths AND online URLs

Each document contains a `**Source:**` line at the bottom with its original URL. Include both the local path and online URL for each source.

**URL patterns by directory:**
| Directory | Online URL Pattern |
|-----------|-------------------|
| `platform-docs/` | `https://platform.claude.com/docs/en/{path}` (replace `__` with `/`) |
| `code-claude-docs/` | `https://code.claude.com/docs/en/{filename}` |
| `mcp-docs/` | `https://modelcontextprotocol.io/{path}` |
| `mcp-blog/` | `https://blog.modelcontextprotocol.io/{filename}` |
| `anthropic-research/` | `https://www.anthropic.com/research/{filename}` |
| `anthropic-news/` | `https://www.anthropic.com/news/{filename}` |
| `engineering-blog/` | `https://www.anthropic.com/engineering/{filename}` |
| `claude-blog/` | `https://www.anthropic.com/news/{filename}` |
| `docs-support/` | Check the `**Source:**` line in the document |
| `agentskills-docs/` | `https://agentskills.io/{filename}` |

### Standard Format Example:
```
[Comprehensive answer to the question...]

**Sources:**
- `code-claude-docs/mcp.md` → [MCP](https://code.claude.com/docs/en/mcp) - MCP configuration details
- `platform-docs/developer-guide/agents-and-tools__tool-use__overview.md` → [Tool Use Overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
- `engineering-blog/building-effective-agents.md` → [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
```

### Slack Format Example (when --slack flag is used):
```
[Comprehensive answer to the question...]

*Sources:*
• `code-claude-docs/mcp.md` → [MCP](https://code.claude.com/docs/en/mcp) - MCP configuration details
• `platform-docs/developer-guide/agents-and-tools__tool-use__overview.md` → [Tool Use Overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
• `engineering-blog/building-effective-agents.md` → [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)

---
💡 *Want answers like this from all 1,400+ Anthropic docs?*
`git clone https://github.com/robgruhl/anthropic-docs-mirror.git` → open in Claude Code → `/ask --slack your question` → copy from `slack-updates/ask-response.md` → paste into Slack (⌘⇧F to apply formatting). Run `/refresh` weekly to stay current.

📋 Slack-ready version saved to: slack-updates/ask-response.md
```

### Slack Promo Footer

When `--slack` is used, ALWAYS append the following footer after the Sources section in both the terminal output and the `slack-updates/ask-response.md` file. Include it exactly as shown (with the `---` separator):

```
---
💡 *Want answers like this from all 1,400+ Anthropic docs?*
`git clone https://github.com/robgruhl/anthropic-docs-mirror.git` → open in Claude Code → `/ask --slack your question` → copy from `slack-updates/ask-response.md` → paste into Slack (⌘⇧F to apply formatting). Run `/refresh` weekly to stay current.
```

Answer the question now by searching the local documentation.
