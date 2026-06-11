# Bringing automated preview, review, and merge to Claude Code on desktop
*February 20, 2026*
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22a9e09b6cfb6289430_c9d8dd2af6d065e1ace8bd4bb29c716eb53ffffb-1000x1000.svg)

# Bringing automated preview, review, and merge to Claude Code on desktop

Updates to Claude Code on desktop help you close the development loop, so you can go from writing code to merging PRs in one place.

- CategoryClaude CodeProduct announcements

- ProductClaude Code

- DateFebruary 20, 2026

- Reading time5min

- ShareCopy linkhttps://claude.com/blog/preview-review-and-merge-with-claude-code

Today, we're shipping Claude Code improvements that let you preview running apps, auto-review code, auto-fix and merge PRs, and seamlessly switch between desktop, mobile, and CLI. Together these updates help you spend less time on the toil around code and more time on the parts you enjoy.

## Write code and see it run

Claude Code on desktop can now start dev servers and preview your running app directly in the desktop interface. Claude views the webapp UI, reads console logs, catches errors, and keeps iterating, so you don’t have to switch to a browser and manually describe what you’re seeing to Claude. You can also select visual elements in the preview and pass feedback directly to Claude to iterate.

## Review code before you push

Once your changes look right, ask Claude to review them using the new “Review code” button. Claude examines your local diffs and leaves comments directly in the desktop diff view, highlighting bugs, making suggestions, and spotting potential issues inline.

You immediately get a second set of eyes to catch obvious issues before anything leaves your machine, and you can ask Claude to address the inline comments and make changes.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6998ab6c581b7e1365118a98_Code%20Review.png)

## Monitor PRs without leaving the app

For code hosted on GitHub, you can also monitor pull request status directly in the desktop app. After you open a PR, Claude Code will track its status, including CI check passes and failures, using the GitHub CLI under the hood.

You can also enable auto-fix so Claude automatically attempts to fix any CI failures it detects. If you enable auto-merge, Claude will also attempt to merge PRs once all checks pass.

You can work on one task in a Claude Code session and open a PR, then move on to a new task. In the background, Claude Code will be monitoring the PR for the original task, and will attempt to fix CI failures so that the PR is ready to merge (or is automatically merged) by the time you switch back to that task.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6998ab7b361d36cb996e0cc8_CI%20Monitoring.png)

## Pick up where you left off

Sessions now move with you. When you start a session from Claude Code in the CLI, run /desktop to bring your full session context into the desktop app.

You can also move local desktop app sessions to the cloud using the “Continue with Claude Code on the web” button. Start a task on the desktop app, then pick it up from the web or your phone with the Claude mobile app.

## Getting started

These updates are available now to all users. Update or download[Claude Code on desktop](https://claude.com/download)to get started. Explore the[documentation](https://code.claude.com/docs/en/desktop)to learn more.

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f783c784823d48ad84175_Object-CodeChatText.svg)

### Introducing routines in Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d223de65e7dcca8267d8_ea364001be6bf6d2e86b58109ead6a779d5771a7-1000x1000.svg)

### Introducing dynamic workflows in Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22a7bb714a55b503cd7_cad034e66b44f7f017c0cb931c403a97d1763758-1000x1000.svg)

### New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229b7f170bab528846d_0df729ce74e4c9dd62c3342c9549ce6c7cef1202-1000x1000.svg)

### Building intelligent apps for Apple platforms with Claude in the Foundation Models framework

## Transform how your organization operates with Claude

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

---
**Source:** https://claude.com/blog/preview-review-and-merge-with-claude-code
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
