# Module 1: Agentic RAG

In this module, we learn what LLMs are and build a simple RAG
pipeline using keyword search. Then we make it agentic, so the LLM
decides when and what to search instead of running a fixed pipeline.

Code: [code/](code/)


## Part 1: RAG

The first 10 lessons walk through building a working RAG pipeline
from scratch with keyword search.

1. [Introduction](lessons/01-intro.md) - What we'll build and why
2. [Environment Setup](lessons/02-environment.md) - Python, uv, OpenAI API
3. [What is RAG](lessons/03-rag.md) - Why LLMs need context, the RAG architecture
4. [The Course FAQ Dataset](lessons/04-dataset.md) - Fetching and exploring the FAQ data
5. [Search](lessons/05-search.md) - Building a search engine with minsearch
6. [Building a Prompt](lessons/06-building-prompt.md) - Combining search results into a prompt
7. [RAG Pipeline](lessons/07-llm.md) - Wiring search + prompt + LLM together
8. [RAG Helper](lessons/08-rag-helper.md) - Reusable RAGBase class and data loading
9. [Data Ingestion](lessons/09-data-ingestion.md) - Persistent search with sqlitesearch
10. [Wrap-up of Part 1](lessons/10-rag-next-steps.md) - Where to go from here


## Part 2: Agents

Part 2 puts the LLM in charge of the search decisions, turning the
fixed pipeline into an agent.

11. [Agents](lessons/11-agents-intro.md) - Why a fixed RAG pipeline isn't enough
12. [Quick RAG Revision (Optional)](lessons/12-rag-revision.md) - Setting up RAG (also a standalone workshop entry point)
13. [Function Calling](lessons/13-function-calling.md) - Giving the LLM tools it can use
14. [The Agentic Loop](lessons/14-agentic-loop.md) - Repeating until the model stops calling tools
15. [ToyAIKit](lessons/15-frameworks.md) - A teaching framework for the agent loop
16. [Other Frameworks](lessons/16-other-frameworks.md) - Production frameworks worth exploring


## Homework

- [Homework](../cohorts/2026/01-agentic-rag/homework.md)


## Optional

Extra material for going deeper on search internals.

- [Build a Search Engine](https://www.youtube.com/watch?v=nMrGK5QgPVE) ([Code](https://github.com/alexeygrigorev/build-your-own-search-engine)) - How minsearch was built from scratch


## Original workshop recordings

This module was taught as two live workshops, which we chopped into the
per-lesson videos above. To watch the full uncut recordings:

- Part 1 – RAG: [Build Your First RAG Application](https://www.youtube.com/watch?v=KSItlTAsMsk)
- Part 2 – Agents: [From RAG to AI Agents: Function Calling and Tool Use](https://www.youtube.com/watch?v=RAqLWJsLZb4)


## Old content

Earlier cohorts taught this module differently. See the archived
materials for the [2024](../cohorts/2024/) and
[2025](../cohorts/2025/) cohorts.


## Notes

Write your own notes below this line:

- [Notes from Vignesh Mayilappan](https://github.com/vigneshmailappan/llm-zoomcamp/blob/main/llm-zoomcamp-code/01-readme-rag.md)
- [Cohort 2026| Notes from Nitin Gupta](https://github.com/niting9881/llm-zoomcamp-2026-code/blob/main/rag-notes.md)
- Add your notes above this line
