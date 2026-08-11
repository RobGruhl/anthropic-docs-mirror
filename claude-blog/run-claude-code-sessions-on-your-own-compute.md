# Run Claude Code sessions on your own compute
*August 6, 2026*
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22651dd05046d0fdb0b_39c40393e610cc0a5e65f50ad12ff5ada273f792-1000x1000.svg)

# Run Claude Code sessions on your own compute

- CategoryProduct announcements

- ProductClaude Code

- DateAugust 6, 2026

- Reading time5min

- ShareCopy linkhttps://claude.com/blog/run-claude-code-sessions-on-your-own-compute

Now in public beta, self-hosted environments let you run Claude Code sessions on your own infrastructure. Start a session from the web, mobile, desktop, or a routine, and it runs inside your network, next to your internal services, toolchains, and security controls, rather than on Anthropic-hosted infrastructure.

For most enterprises, we strongly recommend our hosted offering for operational simplicity with no infrastructure to run or maintain. Self-hosted environments are for teams whose network, tooling, or compliance requirements call for keeping agent execution on infrastructure they control. If you go this route, plan to staff engineering to own setup and ongoing maintenance.

### Why self-host

We saw organizations in our preview program adopt self-hosted environments for a few key reasons:

- Network access:sessions run inside your network and can reach internal services, databases, and registries without exposing them to the public internet

- Customizability:pre-install compilers, SDKs, and internal CLIs in your environment so every session starts ready to build

- Compliance:source code and build artifacts stay on infrastructure you control

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a71ea92125f54b13041e5b9_6a71ea6c8fc8ac632732466a_logo_faire-light.svg)

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a71ea92125f54b13041e5bd_6a71ea6c2122143c0b574194_logo_faire-dark.svg)

“Self-hosted environments let us integrate Claude Code into our existing development workflows while maintaining our security and operational controls. This setup means Claude can generate PRs, help fix CI issues, and respond to developer workflow events, with compute that can scale based on demand. Claude understands our codebase, making it a strong fit for how our engineering teams build.”

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

### Data stays on your infrastructure

Repository checkouts, build artifacts, secrets, and any files a session creates or modifies all stay on infrastructure you provision.

The conversation itself, including prompts, responses, and tool results (which can include code that Claude reads), is sent to Anthropic for inference, and the session transcript is stored so a session can be picked up from any surface.

### How it works

When using self-hosted environments, you deploy a set of[runners](https://code.claude.com/docs/en/self-hosted-environments#key-concepts). These long-lived processes pick up [session](https://code.claude.com/docs/en/self-hosted-environments#session-lifecycle)s and start a Claude Code process for each[session](https://code.claude.com/docs/en/self-hosted-environments#session-lifecycle). Runners come in two modes.

- Fixed:you keep a set number running and sessions are distributed across them.

- On-demand:an orchestrator watches for queued sessions, starts a runner as sessions arrive, and stops them when work finishes so capacity tracks demand.

Runners can serve more than one session, but each session runs in its own checkout, so work stays isolated between developers and accounts. Sessions from every supported surface route to the same environment, so you set it up once and it works wherever your team starts a session.

Note: Self-hosted environments differ from[Remote Control](https://code.claude.com/docs/en/remote-control), which lets developers continue sessions running on their own machines from a phone or browser. Sessions using [Remote Control](https://code.claude.com/docs/en/remote-control) end when that machine stops running the session and are tied to the user who ranclaude, whereas self-hosted environments run sessions on shared infrastructure your platform team operates and can be used by any user.

### Getting started

Self-hosted environments are available in public beta to organizations on Claude Team and Enterprise plans. They are off by default and not available for organizations using ZDR.

Plan on a platform, developer experience, or developer productivity team owning setup and ongoing operation, including building and maintaining the runner image, updating runners, and running the orchestrator if you use on-demand mode.

See the[documentation](https://code.claude.com/docs/en/self-hosted-environments)to learn more. Share feedback via[GitHub](https://github.com/anthropics/claude-code/issues)or through your Anthropic account team.

FAQ

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

### Compliance API coverage extends to Claude Cowork and Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22753311132c8c37b39_d3dd09ad16c68461dc3fb01df5e84cf7ccafda6c-1000x1000.svg)

### Inference hooks: inline data loss prevention for Claude Enterprise

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229b7f170bab528846d_0df729ce74e4c9dd62c3342c9549ce6c7cef1202-1000x1000.svg)

### Bringing MCP 2026-07-28 to Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22349f86cd1968deab7_f06ca06f9d08ca4a85f26357eb896c3730274507-1000x1000.svg)

### Giving admins more visibility and control over Claude spend

## Transform how your organization operates with Claude

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

---
**Source:** https://claude.com/blog/run-claude-code-sessions-on-your-own-compute
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
