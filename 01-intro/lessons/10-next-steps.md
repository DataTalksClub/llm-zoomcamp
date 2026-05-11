# Next Steps

In this module, we:

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


## Agents

In our RAG pipeline, the flow is fixed: we always take the user's
question and send it directly to the knowledge base. But we can be
smarter. We can let an LLM sit between the user and the database,
deciding what questions to send to the knowledge base, how many, and
so on.

This is what agents are about. The LLM becomes an intelligent
intermediary that can reason about what to search for. We'll cover
agents in detail in module 03.


## Fine-tuning vs RAG

A common question is: why not just fine-tune the LLM on our data?

Fine-tuning means taking a model's weights and adjusting them for
your specific use case. This works, but it has downsides:

- It requires special hardware (GPUs) and tools we don't cover in
  this course
- It's difficult to update when new data arrives - you don't want to
  retrain the model every time a new FAQ entry is added
- The LLM already has internal knowledge, but RAG gives it access to
  information it wasn't trained on

RAG is more flexible, cheaper, and works with any LLM. In practice,
fine-tuning is rarely needed - focus on RAG first, and only use
fine-tuning when you really need it.


## Where to go from here

- Try different prompts and see how the answers change
- Add more data sources to the knowledge base
- Experiment with different LLM models (GPT-4o, Claude, Gemini, local
  models via Ollama)
- Try Elasticsearch as a search backend

[← Data Ingestion](09-data-ingestion.md) | [Back to module →](../)
