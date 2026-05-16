# SEPs Are Moving to Pull Requests

*2025-11-28*

---

**Summary:** We’re updating how Specification Enhancement Proposals (SEPs) are submitted and managed. Starting today, SEPs will be created as pull requests to the seps/ directory instead of GitHub issues.
Why the Change?
When we introduced SEPs in July, we chose GitHub Issues as our starting point. Issues are familiar to developers, low-friction, and got us up and running quickly. But as more proposals have come through the process, we’ve identified some key pain points:

We’re updating how Specification Enhancement Proposals (SEPs) are submitted and managed. Starting today, SEPs will be created as pull requests to theseps/directoryinstead of GitHub issues.


```
seps/
```



## Why the Change?#


When weintroduced SEPs in July, we chose GitHub Issues as our starting point. Issues are familiar to developers, low-friction, and got us up and running quickly. But as more proposals have come through the process, we’ve identified some key pain points:

Scattered discussions.With issues, the proposal text lives in the issue body while implementation details often end up in a separate PR. This splits the conversation and makes it harder to follow the full history of a proposal. This also introduces two distinct numbers referencing the same SEP, making it harder to consistently track and manage changes.

No version history.Issues don’t have the same revision tracking that files in a repository do. When a SEP evolves through review, it’s difficult to see what changed and when.

The new PR-based approach, inspired byPython’s PEP process, solves both problems.


## How It Works#


The new workflow will be familiar if you’ve submitted pull requests on GitHub before:

Draft your SEPas a markdown file named0000-your-feature.mdusing theSEP templateCreate a pull requestadding your SEP to theseps/directoryUpdate the SEP numberonce your PR is created, rename the file using the PR number (e.g., PR #1850 becomes1850-your-feature.md) and push a new commit with the renameFind a sponsorfrom ourmaintainer listto shepherd your proposalIterateon feedback directly in the PR

1. Draft your SEPas a markdown file named0000-your-feature.mdusing theSEP template

Draft your SEPas a markdown file named0000-your-feature.mdusing theSEP template


```
0000-your-feature.md
```


1. Create a pull requestadding your SEP to theseps/directory

Create a pull requestadding your SEP to theseps/directory


```
seps/
```


1. Update the SEP numberonce your PR is created, rename the file using the PR number (e.g., PR #1850 becomes1850-your-feature.md) and push a new commit with the rename

Update the SEP numberonce your PR is created, rename the file using the PR number (e.g., PR #1850 becomes1850-your-feature.md) and push a new commit with the rename


```
1850-your-feature.md
```


1. Find a sponsorfrom ourmaintainer listto shepherd your proposal

Find a sponsorfrom ourmaintainer listto shepherd your proposal

1. Iterateon feedback directly in the PR

Iterateon feedback directly in the PR

That’s it. The PR number becomes the SEP number, discussion happens in one place, and git tracks every revision.


## What About Status?#


One notable change:sponsors are now responsible for updating SEP status. In addition to applying labels to the pull request, the sponsor is responsible for ensuring that theStatusfield is updated in the SEP markdown file. This keeps the canonical state of the proposal in the file itself, versioned alongside the content, while PR labels make it easy to filter and find SEPs by status.


```
Status
```


Status transitions work the same as before:DrafttoIn-ReviewtoAcceptedtoFinal, with the sponsor managing each transition as the proposal progresses.


```
Draft
```



```
In-Review
```



```
Accepted
```



```
Final
```



## Getting Started#


Ready to propose a change to MCP? Here’s what you need to know:

For new SEPs:

Read the latestSEP GuidelinesUse theSEP templateto create your proposalBrowse existing SEPs in theseps/directoryfor examplesFollow the workflow described above

- Read the latestSEP Guidelines

- Use theSEP templateto create your proposal

- Browse existing SEPs in theseps/directoryfor examples


```
seps/
```


- Follow the workflow described above

For existing SEPs:If you have a SEP submitted as a GitHub issue, you can continue with your current workflow. We strongly encourage migrating to the new process for better version control and centralized discussion. To migrate:

Create a markdown file using the SEP template, starting with0000-your-feature.mdCopy and adapt your proposal content to fit the template structureSubmit a pull request to theseps/directoryRename the file using your new PR number (e.g., PR #1900 becomes1900-your-feature.md)Close the original issue with a link to the new PR

1. Create a markdown file using the SEP template, starting with0000-your-feature.md


```
0000-your-feature.md
```


1. Copy and adapt your proposal content to fit the template structure

1. Submit a pull request to theseps/directory


```
seps/
```


1. Rename the file using your new PR number (e.g., PR #1900 becomes1900-your-feature.md)


```
1900-your-feature.md
```


1. Close the original issue with a link to the new PR

The new PR gets a fresh SEP number and gives your proposal proper version control and centralized discussion. Any valuable context from the original issue discussion should be summarized in the new SEP or referenced via links.

As always, if you’re unsure whether your idea warrants a SEP, start a conversation onDiscordorGitHub Discussions. We’re happy to help you figure out the right path forward.


## Thank You#


This change is a direct result of feedback from contributors who’ve been through the SEP process. Your input helps us continuously improve how we build MCP together. Keep it coming.

---

**Source:** http://blog.modelcontextprotocol.io/posts/2025-11-28-sep-process-update/

*This is a mirror of the MCP blog for offline reading. All content is copyright the Model Context Protocol project.*