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

Part 2 evaluates answer quality and agent behavior after retrieval.

6. [RAG Evaluation: Cosine Similarity](lessons/06-rag-evaluation-cosine.md) - A->Q->A' evaluation with embeddings
7. [LLM as a Judge](lessons/07-llm-as-judge.md) - Using an LLM to evaluate answer quality
8. [Collecting Agent Data](lessons/08-agent-data.md) - Running the agent with logging, collecting trajectories
9. [Trajectory Evaluation](lessons/09-trajectory-evaluation.md) - Simple checks and LLM-based trajectory scoring
10. [Instruction Following](lessons/10-instruction-following.md) - Answer correctness and instruction following
11. [Next Steps](lessons/11-next-steps.md) - Evaluation frameworks, monitoring, and resources


## Older content

Older cohort materials:

- [2025 cohort](../cohorts/2025/03-evaluation/)
