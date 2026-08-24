# Claude Tag now reads even more of the room
*August 13, 2026*
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2260bfc90348429f9c3_cd9cf56a7f049285b7c1c8786c0a600cf3d7f317-1000x1000.svg)

# Claude Tag now reads even more of the room

Claude has more context to decide when to proactively collaborate in Slack (and when not to)

- CategoryProduct announcements

- ProductClaude Tag

- DateAugust 13, 2026

- Reading time5min

- ShareCopy linkhttps://claude.com/blog/claude-tag-now-reads-even-more-of-the-room

Claude Tag lets you add Claude to a Slack channel, where it works alongside your team. Claude responds when you @-mention it, or proactively when it thinks it can be helpful.

Before, Claude only sawone message at a time, so it made decisions to act proactively based on what was in front of it, but not the wider context of what was around it.

Now, Claude usescontextfrom across the channel, as well as its memory and the standing instructions you have given it, to determine when to contribute to the conversation.

As a result, Claude is now roughly 30% better at determining when, and when not, to proactively respond.

This update comes at no additional cost today. While holding more context does increase Claude Tag’s usage, the additional context Claude Tag holds does not count toward usage or spend limits on any plan.

## From passive responder to active participant

Previously a lightweight classifier decided when Claude should act. It looked at each new message on its own and made one yes-or-no call.

For example, here are two engineers chasing the same bug from opposite ends. Neither has a free hour to run it down, and neither message asks for anything.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7dc1a48865d9839cc4fea6_9120db7b.png)

Read one at a time, neither message is for Claude, so the classifier correctly does nothing, twice. Read together, there's an obvious piece of work sitting there. One engineer has a theory, the other has the evidence for it, and nobody has time to check.

With the classifier removed, Claude uses context across the channel to make one of four moves:

- Reply inline, when the answer is short, verifiable, and something the channel doesn't already know.

- Start deeper work in a thread, when a message deserves real time.

- Route the message to work it has in flight, when it adds to a workstream Claude already has open.

- Say nothing, when nothing is called for.

Here's the same conversation with Claude Tag using additional context. Claude picks the second move, even without being @-mentioned. It sees Priya's hypothesis and Devon's evidence, opens a thread with the investigation already running, and pulls both engineers in. It acts within the boundaries of the permissions, tools, and scope you have configured.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7dc1a48865d9839cc4fead_96b287d1.png)

Same thread, two minutes later. Claude reads the two messages together and starts the work. No @-mention.

The conversations aren't walled off from each other. So when Devon posts an update, it lands in the right workstream. When two investigations turn out to be the same bug, that connection gets made.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a7dc1a48865d9839cc4fea9_dcb183e0.png)

Claude now looks at all messages to understand the full context of the channel, to more accurately determine if it should participate in a conversation unprompted.

## How Claude decides when not to speak

An annoying agent is worse than an unhelpful one. We built Claude Tag to speak up only when it's useful, and in most channels, on most messages, that means saying nothing.

We do this by grading Claude’s channel-by-channel choices against a rubric based on principles like how useful the comment is, how confident Claude is in the response, and whether there is a person better suited to respond.

Claude also knows when to stop paying attention, similar to how people navigate Slack. It follows a few channels closely while paying less attention to others until someone tags it in. In a channel where, message after message, Claude keeps concluding it has nothing to add, it goes to sleep. A @-mention wakes it instantly.

You can also steer its response behavior in plain language: "Never respond here unless someone tags you," or "Feel free to jump in on anything about the deploy pipeline."

And if you'd rather Claude only spoke in a channel when someone tags it,[any member can switch ‘Respond automatically’off](https://claude.com/docs/claude-tag/users/when-claude-responds#turn-automatic-replies-on-or-off).

## The first reply is faster

The additional context also allows Claude to respond more quickly. It acknowledges you in seconds instead of operating silently while it starts up. The work itself takes as long as it always did; what's gone is the silent first minute when you couldn't tell whether it heard you.

## Live today

This update is now available across Claude Tag, available for Claude Teams and Enterprise customers. You can get started[here](https://claude.ai/admin-settings/claude-tag). Claude now acts as a more effective collaborator, one that can follow the conversation, decide for itself when to act, and when to stay out of the way.

Add Claude to one channel and watch what it adds to your conversations. Learn more about[Claude Tag](https://claude.com/product/tag).

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

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
**Source:** https://claude.com/blog/claude-tag-now-reads-even-more-of-the-room
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
