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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d222061abf091318fb82_423062049d4676b41d52b16068cbb5e21603190e-1000x1000.svg)

### The AI-Native SDLC playbook

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22562f020146c9ec973_f8f4644253bde2f901550431b871b6dcf91e5d9d-1000x1000.svg)

### Claude's memory works everywhere, and you decide what's in it

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22727482c9ba6a02e71_1576ae23eaf481f33bd36ab468171cc69d12361a-1000x1000.svg)

### Bain & Company joins the Claude Partner Network as a Global Premier partner

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

### Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenders

## Transform how your organization operates with Claude

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

---
**Source:** https://claude.com/blog/compliance-api-cowork-and-claude-code
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
