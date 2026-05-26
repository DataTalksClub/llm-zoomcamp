# Wrap-up of Part 1

In Part 1 of this module, we:

- Learned what RAG is and why it matters: retrieve documents, build a
  prompt, let the LLM generate a grounded answer
- Built a search engine over a real FAQ dataset using minsearch
- Created a prompt template that combines the user's question with
  search results
- Wired search + prompt + LLM into a working RAG pipeline
- Split ingestion and query into separate processes with sqlitesearch

You now have a working RAG system and a clear mental model for how
each piece fits together. The rest is making each piece better.

## Two directions forward

[Part 2 of this module: Agents](11-agents-intro.md). Our pipeline runs
search once with the exact user query. If the search returns garbage,
the LLM has no way to recover. An agent puts the LLM in charge - it
decides what to search for and when to search again.

[Module 2: Vector Search](../../02-vector-search/). Keyword matches
are exact. Vector search matches by semantic meaning instead, which
helps when the user phrases things differently from the FAQ.

## Elasticsearch

Elasticsearch is the industry standard for text search.

It supports:

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

## Fine-tuning vs RAG

Instead of retrieving documents at query time, you could fine-tune
the LLM on your data.

Fine-tuning means taking a model's weights and adjusting them for
your specific use case.

This works, but it has downsides:

- It requires special hardware (GPUs) and tools we don't cover in
  this course
- It's difficult to update when new data arrives - you don't want to
  retrain the model every time a new FAQ entry is added
- The LLM already has internal knowledge, but RAG gives it access to
  information it wasn't trained on

RAG is more flexible, cheaper, and works with any LLM. In practice,
fine-tuning is rarely needed - focus on RAG first, and only use
fine-tuning when you need it.

## Moving forward

Try these next steps:

- Try different prompts and see how the answers change
- Add more data sources to the knowledge base
- Experiment with different LLM models (GPT-4o, Claude, Gemini, local
  models via Ollama)
- Try Elasticsearch as a search backend

[← Data Ingestion](09-data-ingestion.md) | [Agents →](11-agents-intro.md)
