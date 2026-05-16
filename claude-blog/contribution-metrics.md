# Understand Claude Code’s impact with contribution metrics
*January 29, 2026*
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22349f86cd1968deab7_f06ca06f9d08ca4a85f26357eb896c3730274507-1000x1000.svg)

# Understand Claude Code’s impact with contribution metrics

- CategoryClaude CodeProduct announcements

- ProductClaude Code

- DateJanuary 29, 2026

- Reading time5min

- ShareCopy linkhttps://claude.com/blog/contribution-metrics

Today, we're introducing contribution metrics in Claude Code, available in public beta. Engineering teams can now measure how Claude Code impacts their team’s velocity, tracking PRs shipped and code committed with Claude's help.

## How we're shipping at Anthropic

Engineering teams at Anthropic use Claude Code extensively, and contribution data has helped us quantify its impact. As Claude Code adoption has increased internally, we've seen a 67% increase in PRs merged per engineer per day. Across teams, 70–90% of code is now being written with Claude Code assistance.

While pull requests alone are an incomplete measure of developer velocity, we’ve found them to be a close proxy for what engineering teams care about: shipping features, fixing bugs, and delighting users faster.

The new contribution metrics in Claude Code help you measure this impact in your own organization.

## Measure velocity with Claude Code

By integrating with GitHub, contribution metrics surface the following data points:

- Pull requests merged: Track PRs created with and without Claude Code assistance

- Code committed: See lines of code committed to your repositories with and without Claude Code assistance

- Per-user contribution data: Identify adoption patterns across your team

Contribution data is calculated by matching Claude Code session activity with GitHub commits and PRs. We calculate this conservatively, and only code where we have high confidence in Claude Code's involvement is counted as assisted.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/697aba6d44c54e6710747e68_contribution-metrics-2.png)

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/697aba633790d097ad08c6fc_contribution-metrics-1.png)

The metrics appear in your existing Claude Code analytics dashboard, accessible to workspace admins and owners. No external tools or data pipelines are required. Simply install our GitHub App and authenticate to your organization’s GitHub account, and metrics will automatically populate on the dashboard.

Contribution metrics are designed to complement your existing engineering KPIs. Use them alongside DORA metrics, sprint velocity, or other measures to understand directional changes from bringing Claude Code to your team.

## Getting started

Code contribution metrics are available now in beta for Claude Team and Enterprise customers. To enable them:

- Install theClaude GitHub Appfor your organization

- Navigate toAdmin settings > Claude Codeand toggle on GitHub Analytics

- Authenticate to your GitHub organization

Metrics begin populating automatically as your team uses Claude Code. View the[documentation](https://code.claude.com/docs/en/analytics)for detailed setup instructions and guidance on interpreting your metrics.

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f76874e94e489958af8ba_Object-CodeMagnifier.svg)

### How AI helps break the cost barrier to COBOL modernization

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22a9e09b6cfb6289430_c9d8dd2af6d065e1ace8bd4bb29c716eb53ffffb-1000x1000.svg)

### Bringing automated preview, review, and merge to Claude Code on desktop

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229a7aa26ac1b6e96c2_a62b6eb169818f14c35b7a192af269e283f8fa93-1000x1000.svg)

### Increase web search accuracy and efficiency with dynamic filtering

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22a44550f2799b41ba4_c4a48972044d45df475f1dd84df3b74d221b6580-1000x1000.svg)

### Cowork: Claude Code for the rest of your work

## Transform how your organization operates with Claude

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

---
**Source:** https://claude.com/blog/contribution-metrics
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
