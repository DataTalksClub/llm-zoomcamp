# Module 4: Evaluation

This module covers systematic evaluation for search, RAG, and agent
systems.

We generate ground truth data with an LLM. Then we measure performance
with Hit Rate, MRR, cosine similarity, and LLM-as-a-judge.


## Part 1: Search Evaluation

Part 1 creates a ground truth dataset and uses it to evaluate retrieval
quality.

1. [Intro](lessons/01-intro.md) - Why evaluation matters, offline vs online
2. [Generating Ground Truth](lessons/02-generating-ground-truth.md) - Structured output for one document
3. [Generating Ground Truth for All Documents](lessons/03-generating-ground-truth-batch.md) - Batch generation, cost, and prepared data
4. [Search Evaluation](lessons/04-search-evaluation.md) - Search setup and relevance lists
5. [Search Evaluation Metrics](lessons/05-search-metrics.md) - Hit Rate, MRR, the evaluate() function


## Part 2: RAG and Agent Evaluation

Part 2 evaluates answer quality after retrieval. It also shows the
basic idea of agent evaluation: save the final answer and the tool-call
trajectory.

11. [RAG and Agent Evaluation](lessons/11-rag-and-agent-evaluation-intro.md) - What changes after retrieval
12. [Generating RAG Answers](lessons/12-rag-answers.md) - Running RAG on the ground truth questions
13. [RAG Evaluation: Cosine Similarity](lessons/13-rag-evaluation-cosine.md) - Comparing generated answers with original answers
14. [LLM as a Judge](lessons/14-llm-as-judge.md) - Using an LLM to evaluate answer quality
15. [Agent Evaluation](lessons/15-agent-evaluation.md) - Capturing answers and tool-call trajectories
16. [Next Steps](lessons/16-next-steps.md) - Evaluation frameworks, monitoring, and resources


## Older content

Older cohort materials:

- [2025 cohort](../cohorts/2025/03-evaluation/)
