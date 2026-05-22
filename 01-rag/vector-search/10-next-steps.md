# Next Steps

In this module, we:

- Learned what embeddings are and how they turn text into vectors
- Generated embeddings for our FAQ dataset using sentence-transformers
- Built vector search with numpy, minsearch, sqlitesearch, and PGVector
- Integrated vector search into our RAG pipeline with the `RAGVector`
  class

The code is available in the
[code directory](../code/).


## Using vector search

Text search (keyword search) is simple and fast, and for many
applications it is all you need. Start with text search first.

Vector search adds complexity:

- You need an embedding model
- You need to compute and store embeddings
- At query time you need to encode the query before searching

Even with the smallest model, the overhead is considerable. Don't add
this complexity unless you have a reason.

Many RAG tutorials and articles assume you need vector search from the
start. Many of these come from companies that sell vector databases.
You don't need it from the start.

A reasonable progression:

1. v1: Start with text search. Get your RAG pipeline working end to end.
   For our FAQ dataset, text search already handles most questions well.
   We saw that in module 1.
2. v2: Add vector search when you can measure that text search misses
   relevant results. This happens when users ask questions in different
   words than what is in your documents.
3. v3: Combine both with hybrid search (text + vector), which typically
   outperforms either one alone.

The right time to move from one version to the next is when evaluation
shows it is justified. In a later module, we will cover how to evaluate
search quality and compare different search methods. With evaluation,
you can measure whether the improvement from vector search is marginal
(not worth the overhead) or significant (justified).


## Hybrid search and reranking

Once you have both text search and vector search, you can combine them.
Hybrid search runs both methods and merges the results using techniques
like Reciprocal Rank Fusion (RRF).

Reranking takes it further. After retrieving candidate documents, a
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
