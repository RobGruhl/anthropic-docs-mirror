# Introducing the Message Batches API
*October 8, 2024*
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2239bf93c8cb72a719a_a0655eda5d58588738240e9960790468a3d2c9c0-1000x1000.svg)

# Introducing the Message Batches API

Claude now offers a Message Batches API that processes up to large volumes of queries asynchronously at lower cost.

- CategoryProduct announcements

- ProductClaude Platform

- DateOctober 8, 2024

- Reading time5min

- ShareCopy linkhttps://claude.com/blog/message-batches-api

Update:The [Message Batches API](https://docs.anthropic.com/en/docs/build-with-claude/message-batches) is Generally Available on the Anthropic API. Customers using Claude in Amazon Bedrock can use batch inference. Batch predictions is also available in preview on Google Cloud’s Vertex AI. (December 17, 2024)We’re introducing a new[Message Batches API](https://docs.anthropic.com/en/docs/build-with-claude/message-batches)—a powerful, cost-effective way to process large volumes of queries asynchronously.

Developers can send batches of up to 10,000 queries per batch. Each batch is processed in less than 24 hours and costs 50% less than standard API calls. This makes processing non-time-sensitive tasks more efficient and cost-effective.

The Batches API is available today in public beta with support for Claude 3.5 Sonnet, Claude 3 Opus, and Claude 3 Haiku on the Anthropic API. Customers using Claude in Amazon Bedrock can use[batch inference](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html). Support for batch processing for[Claude on Google Cloud’s Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/use-claude)is coming soon.

## High throughput at half the cost

Developers often use Claude to process vast amounts of data—from analyzing customer feedback to translating languages—where real-time responses aren't necessary.

Instead of managing complex queuing systems or worrying about rate limits, you can use the Batches API to submit groups of up to 10,000 queries and let Anthropic handle the processing at a 50% discount. Batches will be processed within 24 hours, though often much quicker. Additional benefits include:

- Enhanced throughput:Enjoy higher rate limits to process much larger request volumes without impacting your standard API rate limits.

- Scalability for big data:Handle large-scale tasks such as dataset analysis, classification of large datasets, or extensive model evaluations without infrastructure concerns.

The Batches API unlocks new possibilities for large-scale data processing that were previously less practical or cost-prohibitive. For example, analyzing entire corporate document repositories—which might involve millions of files—becomes more economically viable by leveraging our batching discount.

## Pricing

The Batches API allows you to take advantage of infrastructure cost savings and is offered at a 50% discount for both input and output tokens.

- Our most intelligent model to date

- 200K context window

- $1.50 / MTok

- $7.50 / MTok

- Powerful model for complex tasks

- 200K context window

- $7.50 / MTok

- $37.50 / MTok

- Fastest, most cost-effective model

- 200K context window

- $0.125 / MTok

- $0.625 / MTok

## Customer Spotlight: Quora

[Quora](https://cloud.google.com/customers/quora?hl=en), a user-based question-and-answer platform, leverages Anthropic's Batches API for summarization and highlight extraction to create new end-user features.

"Anthropic's Batches API provides cost savings while also reducing the complexity of running a large number of queries that don't need to be processed in real time," said Andy Edmonds, Product Manager at Quora. "It's very convenient to submit a batch and download the results within 24 hours, instead of having to deal with the complexity of running many parallel live queries to get the same result. This frees up time for our engineers to work on more interesting problems.”

## Get started

To start using the Batches API in public beta on the Anthropic API, explore our[documentation](https://docs.anthropic.com/en/docs/build-with-claude/message-batches)and[pricing page](https://docs.anthropic.com/en/docs/build-with-claude/message-batches).

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

FAQ

## Related posts

Explore more product news and best practices for teams building with Claude.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22e6fa9211768bbce0b_6e00dbffcddc82df5e471c43453abfc74ca94e8d-1000x1000.svg)

### Bringing Claude Code and Claude Cowork to government

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a3f14a08cb97bf1b16d40ef_ObjectClouds.svg)

### Claude Cowork is coming to mobile and web

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22349f86cd1968deab7_f06ca06f9d08ca4a85f26357eb896c3730274507-1000x1000.svg)

### Giving admins more visibility and control over Claude spend

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a42c9bc20d2072552ef256a_Node-EnterpriseAgents.svg)

### Introducing the Claude apps gateway for Amazon Bedrock and Google Cloud

## Transform how your organization operates with Claude

Get the developer newsletter

Product updates, how-tos, community spotlights, and more. Delivered monthly to your inbox.

Please provide your email address if you'd like to receive our monthly developer newsletter. You can unsubscribe at any time.

---
**Source:** https://claude.com/blog/message-batches-api
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
