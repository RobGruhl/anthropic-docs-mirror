# Evaluating and Mitigating Discrimination in Language Model Decisions
---
**Summary:** Anthropic is an AI safety and research company that's working to build reliable, interpretable, and steerable AI systems.

# Evaluating and Mitigating Discrimination in Language Model Decisions

## Abstract

As language models (LMs) advance, interest is growing in applying them to high-stakes societal decisions, such as determining financing or housing eligibility. However, their potential for discrimination in such contexts raises ethical concerns, motivating the need for better methods to evaluate these risks. We present a method for proactively evaluating the potential discriminatory impact of LMs in a wide range of use cases, including hypothetical use cases w[here](https://huggingface.co/datasets/Anthropic/discrim-eval) they have not yet been deployed. Specifically, we use an LM to generate a wide array of potential prompts that decision-makers may input into an LM, spanning 70 diverse decision scenarios across society, and systematically vary the demographic information in each prompt. Applying this methodology reveals patterns of both positive and negative discrimination in the Claude 2.0 model in select settings when no interventions are applied. While we do not endorse or permit the use of language models to make automated decisions for the high-risk use cases we study, we demonstrate techniques to significantly decrease both positive and negative discrimination through careful prompt engineering, providing pathways toward safer deployment in use cases w[here](https://huggingface.co/datasets/Anthropic/discrim-eval) they may be appropriate. Our work enables developers and policymakers to anticipate, measure, and address discrimination as language model capabilities and applications continue to expand. We release our dataset and prompts[here](https://huggingface.co/datasets/Anthropic/discrim-eval).

## Policy Memo

[Evaluating and Mitigating Discrimination in Language Model Decisions Policy Memo](https://www-cdn.anthropic.com/f0dfb70b9b309d7c52845f73da8d964140669ff7/Anthropic_DiscriminationEval.pdf)

## Related content

### Labor market impacts of AI: A new measure and early evidence

### An update on our model deprecation commitments for Claude Opus 3

### The persona selection model

---
**Source:** https://www.anthropic.com/research/evaluating-and-mitigating-discrimination-in-language-model-decisions
*This is a mirror of an Anthropic research paper for local access and AI-assisted development.*
