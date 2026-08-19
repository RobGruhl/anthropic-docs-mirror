# Compliance API coverage extends to Claude Cowork and Claude Code
*August 11, 2026*
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

# Compliance API coverage extends to Claude Cowork and Claude Code

- CategoryEnterprise AIProduct announcements

- ProductClaude EnterpriseClaude appsClaude CodeClaude Cowork

- DateAugust 11, 2026

- Reading time5min

- ShareCopy linkhttps://claude.com/blog/compliance-api-cowork-and-claude-code

Claude's Compliance API now covers Cowork across the desktop app, web, and mobile, as well as Claude Code in the CLI and desktop app. Coverage is in beta for Claude Enterprise customers. Compliance and security teams can pull session content and metadata from both products through the same Compliance API interface they already use for Claude chats.

The new endpoints are additive: nothing changes about the data you already pull from the Compliance API today.

Security and compliance teams rely on the Compliance API to see how Claude is used across their organization — for audits and eDiscovery — without deploying separate logging infrastructure for each surface. Extending coverage to Cowork and Claude Code closes a gap: those sessions now show up alongside Claude chats.

## How it works

The new session endpoints return a consolidated, server-hosted transcript for each Cowork and Claude Code session, so prompts, responses, and tool activity come back together in a single session record.

Each session record carries two kinds of data:

- Session content:prompts and responses, tool calls content (web and MCP), and skills and artifacts content captured as transcript text.

- Session metadata:verified user ID and email address, organization ID, session and per-message IDs, and timestamps.

This beta doesn't include Claude Code on the web, Claude Code accessed through the Claude Platform, or sessions run on Amazon Bedrock, Google Cloud's Vertex AI, or Microsoft Foundry.

Organizations already exporting OpenTelemetry data can keep it running: the Compliance API can work alongside it with no infrastructure required on your side.

## Getting started

Coverage for Cowork and Claude Code is available today and included with the Compliance API using your existing Compliance Access Key – there’s no separate integration to build. If it's already enabled for your organization, query the new session endpoints directly. If not, review the Compliance API[documentation](https://platform.claude.com/docs/en/manage-claude/compliance-api)to enable it.

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225485fe31f1ed2d9a1_db28a79c9f4492b8471009d4c20e900f234ece48-1000x1000.svg)

### Securing the frontier: How JetBrains evaluates and deploys Claude Fable 5

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22bed4b18b6703cd710_e750c875fbd7f08ffb6495efa180a8ed60de3611-1000x1000.svg)

### New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22a7bb714a55b503cd7_cad034e66b44f7f017c0cb931c403a97d1763758-1000x1000.svg)

### Claude on call: How Claude Tag serves as Anthropic’s first responder for CI/CD failures

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f7365ae69f4d9f4f96fa2_Object-DoubleHelix.svg)

### The Claude Science product guide

## Transform how your organization operates with Claude

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

---
**Source:** https://claude.com/blog/compliance-api-cowork-and-claude-code
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
