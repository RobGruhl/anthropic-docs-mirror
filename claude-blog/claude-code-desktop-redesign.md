# Redesigning Claude Code on desktop for parallel agents
*April 14, 2026*
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22d0099a66d72e05699_33ddc751e21fb4b116b3f57dd553f0bc55ea09d1-1000x1000.svg)

# Redesigning Claude Code on desktop for parallel agents

Today, we're releasing a redesign of the Claude Code desktop app, built to help you run more Claude Code tasks at once.

- CategoryClaude CodeProduct announcements

- ProductClaude Code

- DateApril 14, 2026

- Reading time5min

- ShareCopy linkhttps://claude.com/blog/claude-code-desktop-redesign

It includes a new sidebar for managing multiple sessions, a drag-and-drop layout for arranging your workspace, an integrated terminal and file editor, plus performance and quality-of-life improvements.

## The new desktop experience

For many developers, the shape of agentic work has changed. You're not typing one prompt and waiting. You're kicking off a refactor in one repo, a bug fix in another, and a test-writing pass in a third, checking on each as results come in, steering when something drifts, and reviewing diffs before you ship.

The new app is built for how agentic coding actually feels now: many things in flight, and you in the orchestrator seat.

## Run sessions in parallel

The new sidebar puts every active and recent session in one place. Kick off work across multiple repos and move between them as results arrive.

You can filter by status, project, or environment, or group the sidebar by project to find and resume sessions faster. When a session's PR merges or closes, it archives itself so the sidebar stays focused on what's live.

When you need to ask a question mid-task, you can open a side chat (⌘ + ; or Ctrl + ;) to branch off a conversation. Side chats pull context from the main thread, but don’t add anything back to the thread, to avoid misdirecting your tasks.

## Review and ship without leaving the app

The redesign brings more commonly-used tools into the app, so you can review, tweak, and ship Claude's work without bouncing to your editor:

- Integrated terminal: Run tests or builds alongside your session.

- In-app file editor: Open files, make spot edits directly, and save changes.

- Faster diff viewer: Rebuilt for performance on large changesets.

- Expanded preview: Open HTML files or PDFs in-app, in addition to running local app servers in the preview pane.

Every pane is drag-and-drop. Arrange the terminal, preview, diff viewer, and chat in whatever grid matches how you work.

## Fits your stack

The desktop app now has parity with CLI plugins. If your org manages Claude Code plugins centrally, or you've installed your own locally, they work in the desktop app exactly the way they do in your terminal.

You can still run sessions locally or in the cloud. SSH support now extends to Mac alongside Linux, so you can point sessions at remote machines from either platform.

## Customize for how you work

Three view modes—Verbose, Normal, and Summary—let you dial the interface from full transparency into Claude's tool calls to just the results. New keyboard shortcuts cover session switching, spawning, and navigation; press⌘ + /(orCtrl + /) to see the full list. A new usage button shows both your context window and session usage at a glance.

Under the hood, the app has been rebuilt for reliability and speed, and now streams responses as Claude generates them.

## Getting started

The redesigned desktop app is available now for all Claude Code users on Pro, Max, Team, and Enterprise plans, and via the Claude API.

[Download the app](https://claude.com/download), or update and restart if you already have it. Explore the[documentation](https://docs.claude.com/claude-code)to learn more.

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22bed4b18b6703cd710_e750c875fbd7f08ffb6495efa180a8ed60de3611-1000x1000.svg)

### New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22e13864f88ea55c2d8_b5c98d26c46edc43193e7f7e28a00633a538bb9c-1000x1000.svg)

### Code w/ Claude SF 2026 recap: Building on the AI exponential

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690937bee860a953417a8eee_Object-CodeBrowserGlobe.svg)

### How a non-technical project manager built and shipped a stress management app with Claude Code in six weeks

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22d6ec42bcf1c632f75_52f59749d1e033ff2675c6686a07bcce83fb5046-1000x1000.svg)

### The founder's playbook: Building an AI-native startup

## Transform how your organization operates with Claude

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

---
**Source:** https://claude.com/blog/claude-code-desktop-redesign
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
