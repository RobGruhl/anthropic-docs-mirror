# Question Decomposition Improves the Faithfulness of Model-Generated Reasoning
---
**Summary:** Anthropic is an AI safety and research company that's working to build reliable, interpretable, and steerable AI systems.

# Question Decomposition Improves the Faithfulness of Model-Generated Reasoning

## Abstract

As large language models (LLMs) perform more difficult tasks, it becomes harder to verify the correctness and safety of their behavior. One approach to help with this issue is to prompt LLMs to externalize their reasoning, e.g., by having them generate step-by-step reasoning as they answer a question (Chain-of-Thought; CoT). The reasoning may enable us to check the process that models use to perform tasks. However, this approach relies on the stated reasoning faithfully reflecting the model’s actual reasoning, which is not always the case. To improve over the faithfulness of CoT reasoning, we have models generate reasoning by decomposing questions into subquestions. Decomposition-based methods achieve strong performance on question-answering tasks, sometimes approaching that of CoT while improving the faithfulness of the model’s stated reasoning on several recently-proposed metrics. By forcing the model to answer simpler subquestions in separate contexts, we greatly increase the faithfulness of model-generated reasoning over CoT, while still achieving some of the performance gains of CoT. Our results show it is possible to improve the faithfulness of model-generated reasoning; continued improvements may lead to reasoning that enables us to verify the correctness and safety of LLM behavior.

## Related content

### Labor market impacts of AI: A new measure and early evidence

### An update on our model deprecation commitments for Claude Opus 3

### The persona selection model

---
**Source:** https://www.anthropic.com/research/question-decomposition-improves-the-faithfulness-of-model-generated-reasoning
*This is a mirror of an Anthropic research paper for local access and AI-assisted development.*
