# Module 4: Evaluation

How do you know if your search, RAG, or agent system is actually good?
This module covers systematic evaluation at three levels: search quality,
RAG answer quality, and agent behavior.

We generate ground truth data with an LLM, then measure performance
using metrics like Hit Rate, MRR, cosine similarity, and LLM-as-a-judge.


## Lessons

1. [Intro](lessons/01-intro.md) -- Why evaluation matters, offline vs online
2. [Generating Ground Truth](lessons/02-generating-ground-truth.md) -- Synthetic test data with structured LLM output
3. [Search Evaluation](lessons/03-search-evaluation.md) -- Hit Rate, MRR, the evaluate() function
4. [RAG Evaluation: Cosine Similarity](lessons/04-rag-evaluation-cosine.md) -- A->Q->A' evaluation with embeddings
5. [LLM as a Judge](lessons/05-llm-as-judge.md) -- Using an LLM to evaluate answer quality
6. [Agent Evaluation](lessons/06-agent-evaluation.md) -- Trajectory and instruction following
7. [Next Steps](lessons/07-next-steps.md) -- Evaluation frameworks, monitoring, further reading


## Older content

- [2025 cohort](../cohorts/2025/03-evaluation/)
