# New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration
*May 19, 2026*
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d224ef32980bc807847d_a683fdcfe3e2c7c6532342a0fa4ff789c3fd4852-1000x1000.svg)

# New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration

- CategoryProduct announcements

- ProductClaude Platform

- DateMay 19, 2026

- Reading time5min

- ShareCopy linkhttps://claude.com/blog/new-in-claude-managed-agents

Today we're launching dreaming in[Claude Managed Agents](https://claude.com/blog/claude-managed-agents)as a research preview. Dreaming extends[memory](https://claude.com/blog/claude-managed-agents-memory)by reviewing past sessions to find patterns and help agents self-improve. We're also making outcomes, multiagent orchestration, and webhooks available to developers building with Managed Agents. Together, these updates make agents more capable at handling complex tasks with minimal steering.

## Build self-improving agents with dreaming

[Dreaming](https://platform.claude.com/docs/en/managed-agents/dreams)is a scheduled process in Claude Managed Agents that reviews agent sessions and memory stores, extracts patterns, and curates memories so agents improve over time. You decide how much control you want: dreaming can update memory automatically, or you can review changes before they land.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f8e9ad765c7eed52dcf468_Claude-Managed-Agents-Blog-Followup-Dreaming.png)

Dreaming surfaces patterns that a single agent can’t see on its own, including recurring mistakes, workflows that agents converge on, and preferences shared across a team. It also restructures memory so it stays high-signal as it evolves. This is especially useful for long-running work and multiagent orchestration.

Together, memory and dreaming form a robust memory system for self-improving agents. Memory lets each agent capture what it learnsas it works. Dreaming refines that memorybetween sessions, pulling shared learnings across agents and keeping it up-to-date.

Dreaming is available in Managed Agents on the Claude Platform; developers can[request access here](https://claude.com/form/claude-managed-agents).

## Outcomes: define the quality bar for agent work

With[outcomes](https://platform.claude.com/docs/en/managed-agents/define-outcomes), you write a rubric describing what success looks like and the agent works toward it. A separate grader evaluates the output against your criteria in its own context window, so it isn't influenced by the agent's reasoning. When something isn't right, the grader pinpoints what needs to change and the agent takes another pass.

Agents do their best work when they know what "good" looks like. For example, a structural framework, a presentation standard, or a set of requirements that need to be met. With outcomes, agents can check their work against that bar and self-correct until the output is good enough, without a human needing to review each attempt.

Outcomes is particularly useful for tasks that require attention to detail and exhaustive coverage. It also works for subjective quality, like whether copy matches a brand voice or a design follows visual guidelines. In testing, outcomes improved task success by up to 10 points over a standard prompting loop, with the largest gains on the hardest problems. Outcomes also improved file generation quality, with +8.4% task success on docx and +10.1% on pptx in our internal benchmarks.

You can also now define an outcome, let the agent run, and get notified by a[webhook](http://platform.claude.com/docs/en/managed-agents/webhooks)when it's done.

## Multiagent orchestration: Handle complex tasks with multiple agents

When there is too much work for a single agent to do well,[multiagent orchestration](https://platform.claude.com/docs/en/managed-agents/multi-agent)lets a lead agent break the job into pieces and delegate each one to a specialist with its own model, prompt, and tools. For example, a lead agent can run an investigation while subagents fan out through deploy history, error logs, metrics, and support tickets.

These specialists work in parallel on a shared filesystem and contribute to the lead agent's overall context. The lead agent can check back in with other agents mid-workflow because events are persistent and every agent remembers what it's done. You can also trace every step in the[Claude Console](https://platform.claude.com/): which agent did what, in what order, and why, giving you full visibility into how your task was delegated and executed.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f8ea208aefcf18345ee3ef_Claude-Managed-Agents-Blog-Followup-Sessions-UI.png)

## What teams are building

Teams are using dreaming, outcomes, and multiagent orchestration to ship agents that verify their own work, learn across sessions, and parallelize complex jobs:

- Harveyuses Managed Agents to coordinate complex legal work like long-form drafting and document creation. With dreaming, their agents remember what they learned between sessions, including filetype workarounds and tool-specific patterns. Completion rates went up ~6x in their tests.

- Netflix's platform team built an analysis agent that processes logs from hundreds of builds across different sources. With changes that affect thousands of applications, what matters is finding the issues that recur across many of them. Multiagent orchestration lets the agent analyze batches in parallel and surface only the patterns worth acting on.

- Spiralby Every is using multiagent orchestration and outcomes to power the writing agent behind their new API and CLI. The lead agent runs onHaiku: it fields incoming requests, poses quick follow-up questions when needed, then delegates the drafting to subagents running onOpus. When a user asks for multiple drafts, the subagents run in parallel. Writing quality is Spiral's core value, so they use outcomes to enforce it. Each draft is scored against a rubric of Every's editorial principles and the user's voice, both pulled from memory. Only drafts that clear the bar are returned.

- Wisedocsbuilt a document quality check agent on Managed Agents, using outcomes to grade each review against their internal guidelines. Reviews now run 50% faster, while staying aligned with their team's standards.

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## Getting started

Dreaming is available in research preview, outcomes, multiagent orchestration, and memory are available in public beta as part of Managed Agents. To get started with dreaming, request access[here](https://claude.com/form/claude-managed-agents). Explore our[documentation](https://platform.claude.com/docs/en/managed-agents/overview)to learn more or visit the[Claude Console](https://platform.claude.com/)to deploy your first agent.

FAQ

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225c16d1b0cc3b1ded5_6457c34fbcb012acf0f27f15a6006f700d0f50de-1000x1000.svg)

### Auto mode for Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2238ce207f9b2011d3f_e44a6b53398f189b9fd0d4f70516db614ac84db3-1000x1000.svg)

### Making Claude Cowork ready for enterprise

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3f14a08cb97bf1b16d40ef_ObjectClouds.svg)

### Claude Cowork is coming to mobile and web

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22e6fa9211768bbce0b_6e00dbffcddc82df5e471c43453abfc74ca94e8d-1000x1000.svg)

### Bringing Claude Code and Claude Cowork to government

## Transform how your organization operates with Claude

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

---
**Source:** https://claude.com/blog/new-in-claude-managed-agents
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
