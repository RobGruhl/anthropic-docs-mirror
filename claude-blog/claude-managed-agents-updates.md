# New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22bed4b18b6703cd710_e750c875fbd7f08ffb6495efa180a8ed60de3611-1000x1000.svg)

# New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels

- KategorieProduktankündigungen

- ProduktClaude Platform

- Datum19.5.2026

- Lesezeit5Min

- TeilenLink kopierenhttps://claude.com/blog/claude-managed-agents-updates

Starting today, Claude Managed Agents can operate in a sandbox you control and connect to your private Model Context Protocol (MCP) servers. Both the sandbox where an agent executes tools and the services it reaches run within the established boundaries of your enterprise, under your security and runtime controls.

The sandbox runs on your own infrastructure, or with managed providers like[Cloudflare](https://developers.cloudflare.com/sandbox/claude-managed-agents/),[Daytona](https://www.daytona.io/docs/en/guides/claude/claude-managed-agents),[Modal](https://github.com/modal-labs/claude-managed-agents-modal-sandbox/tree/main), or[Vercel](https://vercel.com/kb/guide/run-claude-managed-agent-tools-with-vercel-sandbox)to handle the compute and isolation for you.

On the Claude Platform,[self-hosted sandboxes](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)is available in public beta and MCP tunnels in research preview ([request access](https://claude.com/form/claude-managed-agents)).

## Keep agent execution within your perimeter

With self-hosted sandboxes, you keep sensitive files, packages, and services in your own infrastructure or with a managed sandbox provider. The[agent loop](https://www.anthropic.com/engineering/managed-agents)that handles orchestration, context management, and error recovery stays on Anthropic’s infrastructure, while tool execution moves to your own configured environment.

Inside your perimeter, network policies, audit logging, and security tooling are already in place, and files and repositories don't leave. You also control the compute: resource sizing and the runtime image are set on your side, so agents running compute-heavy work such as long builds or image generation get the CPU, memory, and capacity the task needs.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0c965b35dd4ce814b00c56_Sandboxes_3%20(1).png)

## Choose your sandbox client

Bring any sandbox client you want, or start with one of our supported providers:

- Cloudflareruns sandboxes at scale using microVMs and lighter weight isolates. Outbound network requests are in your control with zero-trust secrets injection, customizable proxies to audit, reroute, or modify egress, and the ability to connect to internal services over Cloudflare's network.Amplitudeis building Design Agent, an internal tool for on-brand production UI and marketing design, on Managed Agents and Cloudflare for tighter observability and control.

- Daytonasandboxes are full composable computers, long-running and stateful. The same primitive runs a quick burst or an agent that works for hours. The sandbox stays accessible while a session runs over SSH or an authenticated preview URL, or can be paused and restored with full state preserved.Clay’sGTM engineering agent, Sculptor, builds, tests, and monitors workflows autonomously on Managed Agents and Daytona.

- Modalis a cloud platform built for AI workloads, where sandboxes share the same foundation as Modal's functions, storage, and networking primitives, giving you everything you need to build production AI systems. Modal's custom container runtime delivers sub-second startup on any image, scales to hundreds of thousands of concurrent sandboxes, and gives you CPU and GPU resources on demand.

- Vercelsandboxes combine VM security, VPC peering, and bring your own cloud with millisecond startup time. Managed Agents handles the model, tools, and session state, while the Vercel Sandbox firewall injects credentials at the network boundary so they never enter the sandbox.Rogo, an AI platform for institutional finance, is building an analyst agent on Managed Agents and Vercel Sandbox to handle their proprietary data securely.

## Connect to services within your private network

With[MCP tunnels](http://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview), your agents reach MCP servers inside your private network without exposing them to the public internet. Internal databases, private APIs, knowledge bases, and ticketing systems become tools your agents can call. A lightweight gateway you deploy makes a single outbound connection, no inbound firewall rules, no public endpoints, and traffic encrypted end to end.

MCP tunnels is supported in Managed Agents and the Messages API. MCP tunnels is managed from workspace settings within the[Claude Console](https://platform.claude.com/)by organization admins.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0b4fdc9749bb31acafa95b_MCP%20tunnel%20(1).png)

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a277c3714419cc7f58a9342_logo_rogo-light.svg)

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a277c483b67dd0f46bcdb09_logo_rogo-dark.svg)

Claude Managed Agents handles the agent loop, Vercel's sandboxes give us an environment we can configure for our workloads. This gives us the option to leverage best-in-class infrastructure while we focus on what compounds for a financial AI platform: depth and breadth of tools and data, and a product surface built for how investors and bankers actually work.

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0c15dc2d99d53c20667cf5_mason-light.svg)

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0c15e9d43b72bc8726b778_mason-dark.svg)

Our use cases require secure orchestration of internal tools across a complex product surface. Modal's sandbox gives us the security boundary our enterprise customers need, and combining it with Claude Managed Agents gives us a powerful harness without hand-rolling extra complexity. We had a working version up in under a week, raising reliability for our customers.

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5aa585b66f744445eaec7_Doordash_light.svg)

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5aa5e900d8af5fd782dd2_Doordash_dark.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## Getting started

Both self-hosted sandboxes and MCP tunnels work within the same core primitives supported by Managed Agents. Self-hosted sandboxes is available in public beta and MCP tunnels in research preview. To get started with MCP tunnels,[request access](https://claude.com/form/claude-managed-agents).

Explore our[docs](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)to learn more, follow our[cookbooks](https://github.com/anthropics/claude-cookbooks/tree/main/managed_agents/self_hosted_sandboxes)to set up your sandbox provider, or deploy your first agent in the[Claude Console](https://platform.claude.com/).

Häufig gestellte Fragen

## Ähnliche Beiträge

Weitere Produktneuheiten und Best Practices für Teams, die mit Claude arbeiten.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22d7d4c10df6024f7bc_ee580919acaba2ddc07425f7a7390c8962cadc94-1000x1000.svg)

### Steering Claude Code: CLAUDE.md files, skills, hooks, rules, subagents and more

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2238ce207f9b2011d3f_e44a6b53398f189b9fd0d4f70516db614ac84db3-1000x1000.svg)

### Observability for developers building connectors

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a025cf25f0694905405e054_Object-Scale.svg)

### Claude für die Rechtsbranche

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22e13864f88ea55c2d8_b5c98d26c46edc43193e7f7e28a00633a538bb9c-1000x1000.svg)

### Skills erklärt: Vergleich von Skills mit Prompts, Projekten, MCP und Subagenten

## Transformieren Sie mit Claude die Arbeitsweise Ihres Unternehmens

Entwickler-Newsletter abonnieren

Neues zu Produkten, Anleitungen, Community-Spotlights und mehr. Monatlich in Ihrem Posteingang.

Bitte geben Sie Ihre E-Mail-Adresse an, wenn Sie unseren monatlichen Entwickler-Newsletter erhalten möchten. Sie können sich jederzeit wieder abmelden.

---
**Source:** https://claude.com/de/blog/claude-managed-agents-updates
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
