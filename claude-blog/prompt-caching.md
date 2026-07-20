# Prompt caching with Claude
*August 14, 2025*
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22606367ec36d6a7179_6380b3c2dc9e4011a3cd96fec382bd9197511e31-1000x1000.svg)

# Prompt caching with Claude

Claude caches frequently used context between API calls, reducing costs and latency for long prompts.

- CategoryProduct announcements

- ProductClaude Platform

- DateAugust 14, 2025

- Reading time5min

- ShareCopy linkhttps://claude.com/blog/prompt-caching

Update: Prompt caching is Generally Available on the Anthropic API. Prompt caching is also available in preview in Amazon Bedrock and on Google Cloud’s Vertex AI. (December 17, 2024)Prompt caching, which enables developers to cache frequently used context between API calls, is now available on the Anthropic API. With prompt caching, customers can provide Claude with more background knowledge and example outputs—all while reducing costs by up to 90% and latency by up to 85% for long prompts. Prompt caching is available today in public beta for Claude 3.5 Sonnet, Claude 3 Opus, and Claude 3 Haiku.

## When to use prompt caching

Prompt caching can be effective in situations where you want to send a large amount of prompt context once and then refer to that information repeatedly in subsequent requests, including:

- Conversational agents:Reduce cost and latency for extended conversations, especially those with long instructions or uploaded documents.

- Coding assistants:Improve autocomplete and codebase Q&A by keeping a summarized version of the codebase in the prompt.

- Large document processing:Incorporate complete long-form material including images in your prompt without increasing response latency.

- Detailed instruction sets:Share extensive lists of instructions, procedures, and examples to fine-tune Claude's responses. Developers often include a few examples in their prompt, but with prompt caching you can get even better performance by including dozens of diverse examples of high quality outputs.

- Agentic search and tool use:Enhance performance for scenarios involving multiple rounds of tool calls and iterative changes, where each step typically requires a new API call.

- Talk to books, papers, documentation, podcast transcripts, and other long-form content:Bring any knowledge base alive by embedding the entire document(s) into the prompt, and letting users ask it questions.

Early customers have seen substantial speed and cost improvements with prompt caching for a variety of use cases—from including a full knowledge base to 100-shot examples to including each turn of a conversation in their prompt.

### How we price cached prompts

Cached prompts are priced based on the number of input tokens you cache and how frequently you use that content. Writing to the cache costs 25% more than our base input token price for any given model, while using cached content is significantly cheaper, costing only 10% of the base input token price.

- Our most intelligent model to date

- 200K context window

- $3 / MTok

- $3.75 / MTok -Cache write

- $0.30 / MTok - Cache read

- $15 / MTok

- Powerful model for complex tasks

- 200K context window

- $15 / MTok

- $18.75 / MTok -Cache write

- $1.50 / MTok - Cache read

- $75 / MTok

- Fastest, most cost-effective model

- 200K context window

- $0.25 / MTok

- $0.30 / MTok-Cache write

- $0.03 / MTok - Cache read

- $1.25 / MTok

### Customer spotlight: Notion

[Notion](https://www.notion.so/product/ai)is adding prompt caching to Claude-powered features for its AI assistant, [Notion](https://www.notion.so/product/ai) AI. With reduced costs and increased speed, [Notion](https://www.notion.so/product/ai) is able to optimize internal operations and create a more elevated and responsive user experience for their customers.

> We're excited to use prompt caching to make Notion AI faster and cheaper, all while maintaining state-of-the-art quality.

— Simon Last, Co-founder at Notion

### Get started

To start using the prompt caching public beta on the Anthropic API, explore our[documentation](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)and[pricing page](https://www.anthropic.com/pricing#anthropic-api).

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a025cf25f0694905405e054_Object-Scale.svg)

### Claude for the legal industry

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3f14a08cb97bf1b16d40ef_ObjectClouds.svg)

### Claude Cowork is coming to mobile and web

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2238ce207f9b2011d3f_e44a6b53398f189b9fd0d4f70516db614ac84db3-1000x1000.svg)

### Making Claude Cowork ready for enterprise

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225c16d1b0cc3b1ded5_6457c34fbcb012acf0f27f15a6006f700d0f50de-1000x1000.svg)

### Auto mode for Claude Code

## Transform how your organization operates with Claude

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

---
**Source:** https://claude.com/blog/prompt-caching
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
