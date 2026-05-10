# Next Steps

In this workshop, we:

- Learned what RAG is and why it matters: retrieve documents, build a
  prompt, let the LLM generate a grounded answer
- Built a search engine over a real FAQ dataset using minsearch
- Created a prompt template that combines the user's question with
  search results
- Wired search + prompt + LLM into a working RAG pipeline
- Split ingestion and query into separate processes with sqlitesearch

You now have a working RAG system and a clear mental model for how
each piece fits together. The rest is making each piece better.


## Elasticsearch

Elasticsearch is the industry standard for text search. It supports:

- Full-text search with BM25
- Filtering, aggregations, and faceting
- Vector search (dense and sparse)
- Distributed scaling
- Real-time indexing

It's heavier than sqlitesearch but handles production workloads at
scale. If you're building a real RAG system, Elasticsearch (or
OpenSearch) is a common choice for the search backend.

For an Elasticsearch tutorial, see the
[supplementary materials for Module 1](../../cohorts/2025/01-intro/elastic-search.md).


## Vector Search

In the next module, we'll cover vector search - matching documents by
semantic meaning instead of exact keywords.

If you're curious about how we taught this before:
- [2024 cohort](../../cohorts/2024/) used Elasticsearch for vector search
- [2025 cohort](../../cohorts/2025/02-vector-search/) used Qdrant


## Where to go from here

- Try different prompts and see how the answers change
- Add more data sources to the knowledge base
- Experiment with different LLM models (GPT-4o, Claude, Gemini, local
  models via Ollama)
- Try Elasticsearch as a search backend

---

[<- Previous](08-data-ingestion.md) | [Next ->](../README.md)
