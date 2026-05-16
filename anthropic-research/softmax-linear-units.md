# Softmax Linear Units
---
**Summary:** Anthropic is an AI safety and research company that's working to build reliable, interpretable, and steerable AI systems.

# Softmax Linear Units

## Abstract

In this paper, we report an architectural change which appears to substantially increase the fraction of MLP neurons which appear to be "interpretable" (i.e. respond to an articulable property of the input), at little to no cost to ML performance. Specifically, we replace the activation function with a softmax linear unit (which we term SoLU) and show that this significantly increases the fraction of neurons in the MLP layers which seem to correspond to readily human-understandable concepts, phrases, or categories on quick investigation, as measured by randomized and blinded experiments. We then study our SoLU models and use them to gain several new insights about how information is processed in transformers. However, we also discover some evidence that the superposition hypothesis is true and there is no free lunch: SoLU may be making some features more interpretable by “hiding” others and thus making them even more deeply uninterpretable. Despite this, SoLU still seems like a net win, as in practical terms it substantially increases the fraction of neurons we are able to understand.

## Related content

### Labor market impacts of AI: A new measure and early evidence

### An update on our model deprecation commitments for Claude Opus 3

### The persona selection model

---
**Source:** https://www.anthropic.com/research/softmax-linear-units
*This is a mirror of an Anthropic research paper for local access and AI-assisted development.*
