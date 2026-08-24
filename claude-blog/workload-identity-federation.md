# Secure access to the Claude Platform with Workload Identity Federation
*June 17, 2026*
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

# Secure access to the Claude Platform with Workload Identity Federation

- CategoryProduct announcements

- ProductClaude Platform

- DateJune 17, 2026

- Reading time5min

- ShareCopy linkhttps://claude.com/blog/workload-identity-federation

Workload Identity Federation (WIF) is now generally available on the Claude Platform. WIF is compatible with any OIDC-compliant identity provider and covers all Claude API endpoints, including when accessing the endpoints through our first-party SDKs and Claude Code.

With WIF for workloads and[ant auth login](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/quickstart#authentication)for interactive sessions, developers never have to handle a static API key when building with the Claude Platform.

## How Workload Identity Federation works

WIF replaces static API keys with short-lived, scoped credentials issued at request time. Whether you're a two-person startup running GitHub Actions or an enterprise with detailed credential policies, you can now authenticate with the Claude Platform the same way you authenticate with the rest of your stack.

With WIF, there are no static Anthropic credentials to create, rotate, or leak. Workloads authenticate with the identity they already have: an AWS IAM role, a GCP or Kubernetes service account, an Azure managed identity, a GitHub Actions token, Okta, or other OIDC-compliant providers.

We're also introducing service accounts to the Claude Platform, so each workload can have its own identity, roles, and audit trail instead of a shared API key. First, a federation rule binds an external identity to a service account. Then, when a workload requests access, the Claude Platform verifies the workload's signed OIDC token, matches its claims against your federation rules, and issues a short-lived access token bounded by the service account's roles. Every exchange and request is recorded against that service account in your audit logs.

## Set up your first workload in minutes

The[Claude Console](https://platform.claude.com/)has a guided setup flow for configuring workload identities. The setup validates each step and finishes with a test command that confirms your workload can authenticate.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a2f08711ad72d3a0d542c25_Screenshot%202026-06-13%20at%209.20.12%E2%80%AFAM.png)

## Run your whole organization without static keys

WIF is compatible with the[Admin API](https://platform.claude.com/docs/en/build-with-claude/administration-api)for organization management. Federation rules can be configured for least-privilege access through fine-grained scopes.

Federation configuration is also fully programmatic for organizations operating at scale. New Admin API endpoints let you create and update issuers, service accounts, and federation rules.

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

## Getting started

API keys work alongside WIF, so you can migrate one workload at a time. Read the setup[guides](https://platform.claude.com/docs/en/build-with-claude/workload-identity-federation)for each identity provider, or open the[Claude Console](https://platform.claude.com/)to connect your first workload.

FAQ

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d23008bbc20c0ffaeb6f_43abe7e54b56a891e74a8542944dfbd33f07f49c-1000x1000.svg)

### Centrally manage authorization for MCP connectors

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

### Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenders

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2238ce207f9b2011d3f_e44a6b53398f189b9fd0d4f70516db614ac84db3-1000x1000.svg)

### Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad-hoc questions

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229061abf091318fc81_6905c83d0735e1bc430025fdd1748d1406079036-1000x1000.svg)

### Build production agents with computer use, the Skills API, and the Files API

## Transform how your organization operates with Claude

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

---
**Source:** https://claude.com/blog/workload-identity-federation
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
