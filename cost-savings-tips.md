# Cost Savings Features & Patterns for the Claude Agent SDK

A comprehensive guide to reducing the cost of agents built with the Anthropic Agent SDK.

---

## 1. Model Selection per Task (Subagent Model Override)

The Agent SDK lets you assign different models to subagents based on task complexity. Use cheaper models for simpler subtasks and reserve expensive models for complex reasoning.

```python
agents={
    "code-reviewer": AgentDefinition(
        description="Expert code reviewer",
        tools=["Read", "Grep", "Glob"],
        model="sonnet",  # Cheaper model for review tasks
    ),
    "security-reviewer": AgentDefinition(
        description="Security code reviewer",
        tools=["Read", "Grep", "Glob"],
        model="opus" if is_strict else "sonnet",  # Opus only when needed
    ),
}
```

The model options are `"sonnet"`, `"opus"`, `"haiku"`, and `"inherit"`. The "Building Effective Agents" blog post explicitly recommends routing easy/common questions to **Haiku** and hard/unusual questions to **Sonnet** or **Opus**.

**Pricing reference (per million tokens):**

| Model | Input | Output |
|-------|-------|--------|
| Haiku 4.5 | $1 | $5 |
| Sonnet 4.6 | $3 | $15 |
| Opus 4.6 | $5 | $25 |

**Sources:**
- [Subagents](https://platform.claude.com/docs/en/agent-sdk/subagents) - Model override per subagent
- [Pricing](https://platform.claude.com/docs/en/about-claude/pricing) - Full model pricing table
- [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) - Routing patterns

---

## 2. Budget Controls (`maxBudgetUsd`, `maxTurns`)

The SDK provides hard limits to cap spending per query:

- **`maxBudgetUsd`**: Sets a maximum dollar budget for the entire query. The agent stops when this limit is reached (result subtype: `error_max_budget_usd`).
- **`maxTurns`**: Limits the number of conversation turns (API round-trips) the agent can take (result subtype: `error_max_turns`).

```typescript
const result = query({
  prompt: "Fix the bug",
  options: {
    maxBudgetUsd: 2.00,
    maxTurns: 20,
  }
});
```

```python
async for message in query(
    prompt="Fix the bug",
    options=ClaudeAgentOptions(
        max_budget_usd=2.00,
        max_turns=20,
    ),
):
    print(message)
```

**Source:**
- [TypeScript SDK Reference](https://platform.claude.com/docs/en/agent-sdk/typescript) - `maxBudgetUsd`, `maxTurns` options

---

## 3. Compaction for Long-Running Agents

For agents that run many tool-use iterations, context grows and you pay for increasingly large input tokens on every turn. **Compaction** (server-side, via the Messages API) automatically summarizes older context when approaching the context window limit, dramatically reducing input tokens on subsequent turns.

```python
response = client.beta.messages.create(
    betas=["compact-2026-01-12"],
    model="claude-opus-4-6",
    max_tokens=4096,
    messages=messages,
    context_management={
        "edits": [
            {
                "type": "compact_20260112",
                "trigger": {"type": "input_tokens", "value": 100000},
            }
        ]
    },
)
```

### Enforcing a total token budget with compaction

Combine compaction with a counter to estimate cumulative usage and gracefully wrap up the task once a budget is reached:

```python
TRIGGER_THRESHOLD = 100_000
TOTAL_TOKEN_BUDGET = 3_000_000
n_compactions = 0

# ... in your agent loop:
if response.stop_reason == "compaction":
    n_compactions += 1
    messages.append({"role": "assistant", "content": response.content})

    # Estimate total tokens consumed; prompt wrap-up if over budget
    if n_compactions * TRIGGER_THRESHOLD >= TOTAL_TOKEN_BUDGET:
        messages.append({
            "role": "user",
            "content": "Please wrap up your current work and summarize the final state.",
        })
```

### Maximizing cache hits with compaction

Add a `cache_control` breakpoint at the end of your system prompt so the system prompt remains cached even when compaction rewrites the conversation:

```python
system=[
    {
        "type": "text",
        "text": "You are a helpful coding assistant...",
        "cache_control": {"type": "ephemeral"},  # Cache separately from conversation
    }
],
```

**Source:**
- [Compaction](https://platform.claude.com/docs/en/build-with-claude/compaction) - Server-side context summarization

---

## 4. Prompt Caching

Cache hits cost **90% less** than regular input tokens (0.1x base price). This is particularly important for agents because every turn resends the full conversation history plus tool definitions.

**Caching pricing multipliers:**
- Cache writes (5m TTL): 1.25x base input price
- Cache writes (1h TTL): 2x base input price
- **Cache reads: 0.1x base input price** (the big savings)

### Key agent-specific caching patterns

**Cache tool definitions** — Place `cache_control` on the last tool so all definitions are cached across turns:

```python
tools=[
    {"name": "search", "description": "...", "input_schema": {...}},
    {
        "name": "get_document",
        "description": "...",
        "input_schema": {...},
        "cache_control": {"type": "ephemeral"},  # Caches ALL tools above
    },
],
```

**Cache system prompts** — Especially valuable for agents with large instruction sets:

```python
system=[
    {
        "type": "text",
        "text": "Your detailed system prompt here...",
        "cache_control": {"type": "ephemeral"},
    }
],
```

**Cache conversation incrementally** — Mark the final block of each turn with `cache_control` so the growing conversation is incrementally cached. The system automatically finds the longest matching cached sequence.

**Use 1-hour cache TTL** — When agent steps take longer than 5 minutes between API calls (common for complex agentic workflows):

```python
"cache_control": {"type": "ephemeral", "ttl": "1h"}
```

### Cache token tracking in the Agent SDK

The SDK provides per-model usage breakdowns including cache metrics:

```typescript
for (const [modelName, usage] of Object.entries(result.modelUsage)) {
  console.log(`${modelName}: $${usage.costUSD.toFixed(4)}`);
  console.log(`  Input tokens: ${usage.inputTokens}`);
  console.log(`  Cache reads: ${usage.cacheReadInputTokens}`);
  console.log(`  Cache writes: ${usage.cacheCreationInputTokens}`);
}
```

**Source:**
- [Prompt Caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) - Full caching documentation and examples

---

## 5. Context Editing (Tool Result & Thinking Block Clearing)

For agentic workflows with heavy tool use, old tool results (file contents, search results) consume tokens on every subsequent turn but are no longer needed.

### Tool result clearing

The `clear_tool_uses_20250919` strategy automatically clears the oldest tool results when context grows beyond a threshold. Each cleared result is replaced with placeholder text.

```bash
curl https://api.anthropic.com/v1/messages \
    --header "anthropic-beta: context-management-2025-06-27" \
    --data '{
        "model": "claude-opus-4-6",
        "context_management": {
            "edits": [
                {"type": "clear_tool_uses_20250919"}
            ]
        },
        ...
    }'
```

### Thinking block clearing

The `clear_thinking_20251015` strategy manages extended thinking blocks to prevent them from consuming context space. You can choose how many thinking turns to preserve:

- `keep: "all"` — Maximize cache hits (preserves all thinking)
- `keep: {type: "thinking_turns", value: 1}` — Default, keeps only the last turn's thinking
- More aggressive clearing saves more tokens but invalidates caches

**Source:**
- [Context Editing](https://platform.claude.com/docs/en/build-with-claude/context-editing) - Tool result clearing and thinking block clearing

---

## 6. Adaptive Thinking with Effort Control

For Opus 4.6 and Sonnet 4.6, **adaptive thinking** with the `effort` parameter lets Claude dynamically decide how much thinking to do. Lower effort levels reduce output token consumption significantly on simple intermediate agent steps.

| Effort | Behavior |
|--------|----------|
| `low` | Skips thinking for simple tasks — saves output tokens |
| `medium` | Moderate thinking, skips for very simple queries |
| `high` | Always thinks (default) |
| `max` | No constraints on thinking depth (Opus 4.6 only) |

```python
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=16000,
    thinking={"type": "adaptive"},
    output_config={"effort": "medium"},  # or "low" for simple agent steps
    messages=[...],
)
```

In the Agent SDK, you can also control thinking tokens with `maxThinkingTokens`:

```typescript
options: {
  maxThinkingTokens: 4000,  // Cap thinking token usage
}
```

**Source:**
- [Adaptive Thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking) - Effort parameter documentation

---

## 7. Subagent Context Isolation

Subagents maintain **separate context** from the main agent. A research subagent can explore dozens of files without adding all those intermediate results to the main conversation's token count. Only the summarized result returns to the parent agent.

This is a significant cost advantage over doing everything in one agent loop, where every file read, search result, and intermediate reasoning step accumulates in the context and gets re-sent on every subsequent API call.

```python
agents={
    "research-assistant": AgentDefinition(
        description="Explores files and docs, returns only relevant findings",
        prompt="Research the codebase and return a concise summary of findings.",
        tools=["Read", "Grep", "Glob"],
        model="haiku",  # Cheap model for exploration
    ),
}
```

**Source:**
- [Subagents](https://platform.claude.com/docs/en/agent-sdk/subagents) - Context management benefits

---

## 8. Batch API (50% Discount)

For non-time-sensitive agent workloads (batch evaluations, bulk processing), the Batch API provides a **50% discount** on all tokens. Can be combined with prompt caching for additional savings.

| Model | Batch Input | Batch Output |
|-------|-------------|-------------|
| Opus 4.6 | $2.50/MTok | $12.50/MTok |
| Sonnet 4.6 | $1.50/MTok | $7.50/MTok |
| Haiku 4.5 | $0.50/MTok | $2.50/MTok |

Use the 1-hour cache TTL when combining batch processing with prompt caching, since batch requests can take longer than 5 minutes to process.

**Source:**
- [Batch Processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing) - 50% discount for async workloads

---

## 9. Tool Restrictions

Restricting subagent tools to only what's needed prevents unnecessary tool calls that consume tokens. Fewer available tools also means fewer tool definitions sent as input tokens on every API call.

Each tool definition adds tokens to every request. The tool use system prompt alone adds ~346 tokens when at least one tool is provided. Removing unnecessary tools eliminates both the definition overhead and the risk of unnecessary tool invocations.

| Use case | Recommended tools |
|----------|-------------------|
| Read-only analysis | `Read`, `Grep`, `Glob` |
| Test execution | `Bash`, `Read`, `Grep` |
| Code modification | `Read`, `Edit`, `Write`, `Grep`, `Glob` |

**Source:**
- [Subagents](https://platform.claude.com/docs/en/agent-sdk/subagents) - Tool restriction patterns
- [Pricing](https://platform.claude.com/docs/en/about-claude/pricing) - Tool use token overhead

---

## 10. Architectural Patterns from "Building Effective Agents"

The Anthropic engineering blog recommends these cost-conscious patterns:

**Start simple:**
> "Find the simplest solution possible, and only increase complexity when needed. Agentic systems often trade latency and cost for better task performance, and you should consider when this tradeoff makes sense."

**Use routing to match cost to complexity:**
> "Routing easy/common questions to smaller, cost-efficient models like Claude Haiku 4.5 and hard/unusual questions to more capable models like Claude Sonnet 4.5 to optimize for best performance."

**Avoid unnecessary agentic loops:**
> "For many applications, optimizing single LLM calls with retrieval and in-context examples is usually enough."

**Be aware of compounding costs in autonomous agents:**
> "The autonomous nature of agents means higher costs, and the potential for compounding errors. We recommend extensive testing in sandboxed environments, along with the appropriate guardrails."

**Source:**
- [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)

---

## 11. Cost Tracking for Optimization

You can't optimize what you don't measure. The SDK provides `total_cost_usd` and per-model `modelUsage` breakdowns to identify where costs are concentrated:

```typescript
import { query } from "@anthropic-ai/claude-agent-sdk";

const result = await query({
  prompt: "Analyze and refactor this code",
  options: { /* ... */ }
});

// Total cost for the entire query
console.log(`Total cost: $${result.usage.total_cost_usd}`);

// Per-model breakdown (useful when using different models for subagents)
for (const [modelName, usage] of Object.entries(result.modelUsage)) {
  console.log(`${modelName}: $${usage.costUSD.toFixed(4)}`);
  console.log(`  Input tokens: ${usage.inputTokens}`);
  console.log(`  Output tokens: ${usage.outputTokens}`);
  console.log(`  Cache reads: ${usage.cacheReadInputTokens}`);
  console.log(`  Cache writes: ${usage.cacheCreationInputTokens}`);
}
```

```python
from claude_agent_sdk import query, ResultMessage

async for message in query(prompt="Analyze and refactor this code"):
    if isinstance(message, ResultMessage):
        print(f"Total cost: ${message.total_cost_usd}")
```

Key metrics to monitor:
- **Cache hit rate**: High `cacheReadInputTokens` relative to total input means caching is working
- **Per-model costs**: Identify if expensive models are being used for simple tasks
- **Output vs input ratio**: High output token counts may indicate over-verbose responses or excessive thinking

**Source:**
- [Cost Tracking](https://platform.claude.com/docs/en/agent-sdk/cost-tracking) - SDK cost tracking and billing

---

## Quick Reference: Stacking Discounts

Multiple cost-saving mechanisms can be combined:

| Technique | Savings | Combinable With |
|-----------|---------|-----------------|
| Prompt caching (reads) | 90% off input | Batch, compaction, context editing |
| Batch API | 50% off all tokens | Caching, 1h cache TTL |
| Haiku instead of Opus | ~80% cheaper | All techniques |
| Sonnet instead of Opus | ~40% cheaper | All techniques |
| Context editing | Reduces input tokens | Caching (with caveats) |
| Compaction | Reduces input tokens | Caching |
| Adaptive thinking (low effort) | Reduces output tokens | All techniques |
| Tool restrictions | Reduces input tokens | All techniques |

For example, using Haiku with batch processing and prompt caching:
- Base Haiku input: $1/MTok
- With batch discount: $0.50/MTok
- Cache reads with batch: $0.05/MTok (0.1x of $0.50)

---

## All Sources

- [Agent SDK Cost Tracking](https://platform.claude.com/docs/en/agent-sdk/cost-tracking)
- [Agent SDK Subagents](https://platform.claude.com/docs/en/agent-sdk/subagents)
- [Agent SDK TypeScript Reference](https://platform.claude.com/docs/en/agent-sdk/typescript)
- [Pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- [Prompt Caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- [Compaction](https://platform.claude.com/docs/en/build-with-claude/compaction)
- [Context Editing](https://platform.claude.com/docs/en/build-with-claude/context-editing)
- [Adaptive Thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)
- [Batch Processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing)
- [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)
