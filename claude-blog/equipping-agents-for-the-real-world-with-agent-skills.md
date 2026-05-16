# Equipping agents for the real world with Agent Skills
*October 16, 2025*
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690937bee860a953417a8eee_Object-CodeBrowserGlobe.svg)

# Equipping agents for the real world with Agent Skills

Claude is powerful, but real work requires procedural knowledge and organizational context. Introducing Agent Skills, a new way to build specialized agents using files and folders.

- CategoryClaude CodeAgents

- ProductClaude CodeClaude Developer Platform

- DateOctober 16, 2025

- Reading time5min

- ShareCopy linkhttps://claude.com/blog/equipping-agents-for-the-real-world-with-agent-skills

Update: We've published[Agent Skills](https://agentskills.io/)as an open standard for cross-platform portability. (December 18, 2025)

As model capabilities improve, we can now build general-purpose agents that interact with full-fledged computing environments.[Claude Code](https://claude.com/product/claude-code), for example, can accomplish complex tasks across domains using local code execution and filesystems. But as these agents become more powerful, we need more composable, scalable, and portable ways to equip them with domain-specific expertise.

This led us to create[Agent Skills](https://www.anthropic.com/news/skills): organized folders of instructions, scripts, and resources that agents can discover and load dynamically to perform better at specific tasks.Skills extend Claude’s capabilities by packaging your expertise into composable resources for Claude, transforming general-purpose agents into specialized agents that fit your needs.

Building a skill for an agent is like putting together an onboarding guide for a new hire. Instead of building fragmented, custom-designed agents for each use case, anyone can now specialize their agents with composable capabilities by capturing and sharing their procedural knowledge. In this article, we explain what Skills are, show how they work, and share best practices for building your own.

![To activate skills, all you need to do is write a SKILL.md file with custom guidance for your agent.](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/697a4bc12d27779c3e377962_image.webp)

## The anatomy of a skill

To see Skills in action, let’s walk through a real example: one of the skills that powers[Claude’s recently launched document editing abilities](https://www.anthropic.com/news/create-files). Claude already knows a lot about understanding PDFs, but is limited in its ability to manipulate them directly (e.g. to fill out a form). This[PDF skill](https://github.com/anthropics/skills/tree/main/document-skills/pdf)lets us give Claude these new abilities.

At its simplest, a skill is a directory that contains aSKILL.md file. This file must start with YAML frontmatter that contains some required metadata:nameanddescription. At startup, the agent pre-loads thenameanddescriptionof every installed skill into its system prompt.

This metadata is thefirst levelofprogressive disclosure: it provides just enough information for Claude to know when each skill should be used without loading all of it into context. The actual body of this file is thesecond levelof detail. If Claude thinks the skill is relevant to the current task, it will load the skill by reading its fullSKILL.mdinto context.

![Anatomy of a SKILL.md file including the relevant metadata: name, description, and context related to the specific actions the skill should take.](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/697a4bc12d27779c3e37795c_image.webp)

As skills grow in complexity, they may contain too much context to fit into a singleSKILL.md, or context that’s relevant only in specific scenarios. In these cases, skills can bundle additional files within the skill directory and reference them by name fromSKILL.md. These additional linked files are thethird level(and beyond) of detail, which Claude can choose to navigate and discover only as needed.

In the PDF skill shown below, theSKILL.mdrefers to two additional files (reference.mdandforms.md) that the skill author chooses to bundle alongside the coreSKILL.md. By moving the form-filling instructions to a separate file (forms.md), the skill author is able to keep the core of the skill lean, trusting that Claude will readforms.mdonly when filling out a form.

![How to bundle additional content into a SKILL.md file.](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/697a4bc12d27779c3e377966_image.webp)

Progressive disclosure is the core design principle that makes Agent Skills flexible and scalable. Like a well-organized manual that starts with a table of contents, then specific chapters, and finally a detailed appendix, skills let Claude load information only as needed:

![This image depicts how progressive disclosure of context in Skills.](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/697a4bc12d27779c3e37795f_image.webp)

Agents with a filesystem and code execution tools don’t need to read the entirety of a skill into their context window when working on a particular task. This means that the amount of context that can be bundled into a skill is effectively unbounded.

### Skills and the context window

The following diagram shows how the context window changes when a skill is triggered by a user’s message.

![This image depicts how skills are triggered in your context window.](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/697a4bc12d27779c3e377956_image.webp)

The sequence of operations shown:

- To start, the context window has the core system prompt and the metadata for each of the installed skills, along with the user’s initial message;

- Claude triggers the PDF skill by invoking a Bash tool to read the contents ofpdf/SKILL.md;

- Claude chooses to read theforms.mdfile bundled with the skill;

- Finally, Claude proceeds with the user’s task now that it has loaded relevant instructions from the PDF skill.

### Skills and code execution

Skills can also include code for Claude to execute as tools at its discretion.

Large language models excel at many tasks, but certain operations are better suited for traditional code execution. For example, sorting a list via token generation is far more expensive than simply running a sorting algorithm. Beyond efficiency concerns, many applications require the deterministic reliability that only code can provide.

In our example, the PDF skill includes a pre-written Python script that reads a PDF and extracts all form fields. Claude can run this script without loading either the script or the PDF into context. And because code is deterministic, this workflow is consistent and repeatable.

![This image depicts how code is executed via Skills.](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/697a4bc12d27779c3e377959_image.webp)

## Developing and evaluating skills

Here are some helpful guidelines for getting started with authoring and testing skills:

- Start with evaluation:Identify specific gaps in your agents’ capabilities by running them on representative tasks and observing where they struggle or require additional context. Then build skills incrementally to address these shortcomings.

- Structure for scale:When theSKILL.mdfile becomes unwieldy, split its content into separate files and reference them. If certain contexts are mutually exclusive or rarely used together, keeping the paths separate will reduce the token usage. Finally, code can serve as both executable tools and as documentation. It should be clear whether Claude should run scripts directly or read them into context as reference.

- Think from Claude’s perspective:Monitor how Claude uses your skill in real scenarios and iterate based on observations: watch for unexpected trajectories or overreliance on certain contexts. Pay special attention to thenameanddescriptionof your skill. Claude will use these when deciding whether to trigger the skill in response to its current task.

- Iterate with Claude:As you work on a task with Claude, ask Claude to capture its successful approaches and common mistakes into reusable context and code within a skill. If it goes off track when using a skill to complete a task, ask it to self-reflect on what went wrong. This process will help you discover what context Claude actually needs, instead of trying to anticipate it upfront.

### Security considerations when using Skills

Skills provide Claude with new capabilities through instructions and code. While this makes them powerful, it also means that malicious skills may introduce vulnerabilities in the environment where they’re used or direct Claude to exfiltrate data and take unintended actions.

We recommend installing skills only from trusted sources. When installing a skill from a less-trusted source, thoroughly audit it before use. Start by reading the contents of the files bundled in the skill to understand what it does, paying particular attention to code dependencies and bundled resources like images or scripts. Similarly, pay attention to instructions or code within the skill that instruct Claude to connect to potentially untrusted external network sources.

## The future of Skills

Agent Skills are[supported today](https://www.anthropic.com/news/skills)across[Claude.ai](http://claude.ai/redirect/website.v1.bdb29daa-1a07-41ec-87f6-579dc33634bd), Claude Code, the Claude Agent SDK, and the Claude Developer Platform.

In the coming weeks, we’ll continue to add features that support the full lifecycle of creating, editing, discovering, sharing, and using Skills. We’re especially excited about the opportunity for Skills to help organizations and individuals share their context and workflows with Claude. We’ll also explore how Skills can complement[Model Context Protocol](https://modelcontextprotocol.io/)(MCP) servers by teaching agents more complex workflows that involve external tools and software.

Looking further ahead, we hope to enable agents to create, edit, and evaluate Skills on their own, letting them codify their own patterns of behavior into reusable capabilities.

Skills are a simple concept with a correspondingly simple format. This simplicity makes it easier for organizations, developers, and end users to build customized agents and give them new capabilities.

We’re excited to see what people build with Skills. Get started today by checking out our Skills[docs](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)and[cookbook](https://github.com/anthropics/claude-cookbooks/tree/main/skills).

## Acknowledgements

Written by Barry Zhang, Keith Lazuka, and Mahesh Murag, who all really like folders. Special thanks to the many others across Anthropic who championed, supported, and built Skills.

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

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22a44550f2799b41ba4_c4a48972044d45df475f1dd84df3b74d221b6580-1000x1000.svg)

### Cowork: Claude Code for the rest of your work

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d230e0a787df988a8558_97cf99624aa60f59b75f9e08cdf0f00d33c34804-1000x1000.svg)

### Building multi-agent systems: When and how to use them

## Transform how your organization operates with Claude

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

---
**Source:** https://claude.com/blog/equipping-agents-for-the-real-world-with-agent-skills
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
