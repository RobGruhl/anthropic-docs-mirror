# The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry
*June 22, 2026*
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22c7f111435762ad994_1b398dbdfa4995ce5ce943aa87d8b78b2c2ba065-1000x1000.svg)

# The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry

- CategoryEnterprise AI

- ProductClaude Enterprise

- DateJune 22, 2026

- Reading time5min

- ShareCopy linkhttps://claude.com/blog/the-full-claude-desktop-experience-on-aws-google-cloud-and-microsoft-foundry

Organizations that use Claude Desktop through AWS, Google Cloud, and Microsoft Foundry now get the full Desktop experience — chat, Claude Cowork, and Claude Code, all in one app.

Now IT teams can keep inference inside their own environment across products, and deploy Claude Desktop organization-wide with per-user SSO, MDM policy templates, an offline installer option, and an M365 connector that can run entirely on the device.

Inference runs on your cloud in the regions you configure and conversation history is stored locally. You control the endpoints data connectors reach and the aggregated telemetry Anthropic receives.

### One surface for the entire organization

Until today, customers using Claude Desktop through AWS, Google Cloud, and Microsoft Foundry only had access to Claude Cowork and Claude Code. Now, one deployment covers every role, and each surface has its own policy key, so you decide who gets what, and when.Chat for quick answers and thinking through a problem. Claude Cowork for the work your people would rather hand off: Claude researches across approved sources, works with the files already on the device and builds the deliverable, surfacing results when it’s done. Claude Code for engineers who want agentic coding without living in a terminal.

### Deployment controls

Deploying Claude Desktop organization-wide means working within the systems you already have.

Sign in like any work app.Employees use the same work account they use for everything else: IAM Identity Center, Workforce Identity Federation, Microsoft Entra ID, or any OIDC provider like Okta. No shared keys to rotate, no cloud credentials on end-user machines.

Deploy like any app you already manage.Export policy templates from the setup UI and push them through Intune, GPO, or Jamf. An offline installer covers air-gapped environments.

Know it works before anyone sees it.Test every connector, confirm which Claude models your provider serves, and verify the connection, all before rollout. A model guard keeps routing on Claude, including in GovCloud, even if a setting is misconfigured.

Start small, expand as adoption grows.Chat, Claude Cowork, and Claude Code each have their own policy key, so you can give non-technical teams chat and Claude Cowork, engineering Claude Code, and then broaden access as teams adopt each surface. Your hard-deny rules apply across every tab.

Bring Claude to where the work lives.A Microsoft 365 connector gives Claude access to mail and documents through your own Entra app, with tenant allowlisting and beta support for GCC High/DoD endpoints. For the strictest residency requirements, use our local connector, and the connection stays between the device and Microsoft.

> "We rolled out Claude Desktop fast through our existing cloud environment — no separate vendor contract. Our own LLM Gateway let one team deploy it to hundreds of users worldwide, with no heavy infrastructure build-out." - Sarang Oh, Analytics/AI Team Leader, Hanwha Solutions

### Getting started

For admins, the[deployment guide](http://claude.com/docs/third-party/claude-desktop/installation)walks through SSO, policy templates, and pre-rollout validation. Or contact your account team and we'll help you plan the rollout.

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a0112e18cdd7f0b92d19e40_Hand-BuildingBricks.svg)

### Building effective human-agent teams

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22930b7622d6096c33d_4d663bd87c391c144b9bca513b3849ccfa00a3b9-1000x1000.svg)

### 1M context is now generally available for Opus 4.6 and Sonnet 4.6

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2319ef2161fcf9ba649_ddad92700787ec1bf1d80359c0c5e6ca305682b0-1000x1000.svg)

### Advancing finance with Claude Opus 4.6

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d223de65e7dcca8267d8_ea364001be6bf6d2e86b58109ead6a779d5771a7-1000x1000.svg)

### How Anthropic teams use Claude Code

## Transform how your organization operates with Claude

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

---
**Source:** https://claude.com/blog/the-full-claude-desktop-experience-on-aws-google-cloud-and-microsoft-foundry
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
