# Build production agents with computer use, the Skills API, and the Files API
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229061abf091318fc81_6905c83d0735e1bc430025fdd1748d1406079036-1000x1000.svg)

# Build production agents with computer use, the Skills API, and the Files API

- CategoriaAnnunci sul prodottoAgentiIA aziendale

- ProdottoPiattaforma Claude

- Data20/8/26

- Tempo di lettura5min

- CondividiCopia linkhttps://claude.com/blog/computer-use-skills-api-files-api

Computer use, the Skills API, and the Files API are generally available on the Claude Platform today. Computer use also adds a new browser use tool for agents that work in web applications. Together they let you build agents that operate software, apply your team's expertise, and return finished files.

### Building agents on the Claude Platform

Computer uselets you build agents that operate software they can see. Given a screenshot, the agent clicks, types, and scrolls the way someone at the keyboard would. That lets it work in applications that were never built for automation. The newbrowser use toolextends this to the web. Alongside the screenshot, the agent reads the structure of the page and acts on a specific field or button rather than a position on screen.

TheSkills APIand theFiles APIlet you give that agent your expertise and your documents. A skill is a folder of instructions, scripts, and templates that Claude loads only when a task calls for it. With theSkills APIyou upload and version your own skills, then attach them to any request. They run in Claude's code execution sandbox, so there is nothing for you to host. TheFiles APIis storage for the documents an agent reads and writes: upload a PDF or spreadsheet once, reference it by ID in later requests instead of re-sending it, and download the files the agent creates.

Say you're building a claims agent. It reads the intake document from the Files API, follows a skill that encodes the team's filing procedure, completes the submission in an insurer's web portal with the browser use tool, and saves the confirmation back as a file. Code execution and web search, already generally available, fit into the same loop.

### What's new with general availability

- Computer use:the updated computer use tool lets Claude take several actions per turn instead of one per model call, so tasks finish in fewer calls and less time. Computer use is also now eligible for HIPAA-regulated workloads under our BAA.

- Browser use tool:new in computer use today. It uses the same multi-action turns and adds page structure, so agents target web elements more reliably than with pixels alone.

- Skills API:a simpler API for uploading and versioning your own skills.

- Files API:automatic file expiration, 5x higher rate limits, and 1 TB of storage per organization.

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a84d86b69e80750cfefc646_Asteroid_Logo_Black.svg)

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a84d83ff9fbb0abe47899c7_Asteroid_Logo_White.svg)

"Our agents work inside healthcare and insurance systems that have no API. On the new computer use tool, our longest claims workflow went from 32 minutes to 13, cost per task fell about 30% across every workflow we tested, and completion hit 100%, with no changes to our prompts."

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a8c287936531790c85c4_box_light.svg)

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5a8bdc1ea299a1a768655_box_dark.svg)

"The Skills API gave us a straightforward way to build specialized document creation into Box Agent. For a bank, a skill captures the firm's credit methodology and approved memo format; Box Agent applies it to the financial statements and deal documents already in Box and produces a source-grounded credit memo for analyst review. Banks get agents for complex workflows without building each one from scratch."

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

### Getting started

The [computer use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) tool, the [browser use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool), the [Skills API](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), and the [Files API](https://platform.claude.com/docs/en/build-with-claude/files) are now available on the Claude Platform. The [Skills API](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) and the [Files API](https://platform.claude.com/docs/en/build-with-claude/files) are also available through Microsoft Foundry, and the updated [computer use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) and [browser use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool)s are coming soon to Google Cloud's Vertex AI. Existing beta integrations keep working while you migrate. See the documentation for[computer use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool), the[browser use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool), the[Skills API](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), and the[Files API](https://platform.claude.com/docs/en/build-with-claude/files)to get started.

FAQ

## Articoli correlati

Accedi alle altre novità sui prodotti e scopri le best practice per i team che programmano con Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d223de65e7dcca8267d8_ea364001be6bf6d2e86b58109ead6a779d5771a7-1000x1000.svg)

### Come i team di Anthropic utilizzano Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2238ce207f9b2011d3f_e44a6b53398f189b9fd0d4f70516db614ac84db3-1000x1000.svg)

### Come Brex migliora la qualità del codice e la produttività con Claude Code

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2307f9555d7c1bc46cb_77dd9077412abc790bf2bc6fa3383b37724d6305-1000x1000.svg)

### Introduzione alle Skills agentiche

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/690937bee860a953417a8eee_Object-CodeBrowserGlobe.svg)

### Claude Code sul web

## Trasforma le operazioni della tua azienda con Claude

Ricevi la newsletter sullo sviluppo

Aggiornamenti sui prodotti, guide utili, informazioni sulla community e molto altro. Ogni mese nella tua e-mail.

Inserisci il tuo indirizzo e-mail per ricevere la newsletter mensile sullo sviluppo. Puoi annullare l'iscrizione in qualsiasi momento.

---
**Source:** https://claude.com/it/blog/computer-use-skills-api-files-api
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
