# Next Steps

In this module, we:

- Learned what embeddings are and how they turn text into vectors
- Generated embeddings for our FAQ dataset using sentence-transformers
- Built vector search with numpy, minsearch, sqlitesearch, and PGVector
- Integrated vector search into our RAG pipeline with the `RAGVector`
  class

The code is available in the
[code repository](https://github.com/alexeygrigorev/llm-zoomcamp-2026-vector).


## When to use vector search

Text search (keyword search) is simple and fast. For many applications,
it's all you need. Start with text search first.

Vector search adds complexity: you need an embedding model, you need to
compute and store embeddings, and the search itself is more involved.
Don't add this complexity unless you have a reason.

The right time to switch to vector search is when you notice that text
search misses relevant results - when users ask questions in different
words than what's in your documents. That's when the semantic matching
of vector search helps.

But how do you know when text search is not enough? That's what
evaluation is for. In a later module, we'll cover how to evaluate
search quality and compare different search methods. With evaluation,
you can measure which approach works best for your data and make an
informed decision.


## Hybrid search and reranking

Once you have both text search and vector search, you can combine them.
Hybrid search runs both methods and merges the results using techniques
like Reciprocal Rank Fusion (RRF).

Reranking takes it further: after retrieving candidate documents, a
separate model re-scores them for relevance.

Both techniques can improve retrieval quality. We cover them in the
[Hybrid Search lesson in the Best Practices module](../../06-best-practices/lessons/02-hybrid-search.md).


## Moving forward

Try these next steps:

- Compare text search and vector search on your own data
- Experiment with different embedding models
- Try PGVector with a larger dataset
- Try a different vector database - Elasticsearch, Qdrant,
  Weaviate, Chroma, or any other. The concepts are the same:
  embed documents, store vectors, search by similarity
- Evaluate your search results (covered in a later module)

[← Vector Search with PGVector](08-pgvector.md) | [Back to module →](../)
