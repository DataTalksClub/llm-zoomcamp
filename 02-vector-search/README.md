# Module 2: Vector Search

In the first module, we built a RAG pipeline using keyword search with
minsearch and sqlitesearch. Keyword search works well when the query
contains the exact words present in the documents. But what happens when
the user phrases the question differently? "How do I join late?" and
"Can I still enroll after the start date?" mean the same thing, but
they share few keywords.

Vector search solves this by matching on meaning, not just words. It
converts text into numerical vectors and finds the closest matches by
semantic similarity.

In this module, we will:

- Understand what vector search is and how it differs from keyword search
- Generate embeddings using sentence-transformers
- Build vector search with minsearch, sqlitesearch, and PGVector
- Integrate vector search into our RAG pipeline
- Combine keyword and vector search with hybrid search


## Lessons

1. [What is Vector Search](lessons/01-intro.md) - Keyword search vs vector search, why it matters
2. [Embeddings](lessons/02-embeddings.md) - Turning text into vectors with sentence-transformers
3. [Embedding Our Dataset](lessons/03-embeddings-dataset.md) - Generating embeddings for the FAQ dataset
4. [Vector Search with minsearch](lessons/04-minsearch-vector.md) - In-memory vector search
5. [RAG with Vector Search](lessons/05-rag-vector.md) - Replacing keyword search with vector search in our RAG pipeline
6. [Vector Search with sqlitesearch](lessons/06-sqlitesearch-vector.md) - Persistent vector search backed by SQLite
7. [Vector Search with PGVector](lessons/07-pgvector.md) - Production vector search with PostgreSQL and pgvector
8. [Text vs Vector Search](lessons/08-text-vs-vector.md) - Comparing keyword and vector search side by side
9. [Hybrid Search](lessons/09-hybrid-search.md) (Optional) - Combining keyword and vector search for better results
10. [ONNX Embedder](lessons/10-onnx-embedder.md) (Optional) - Using ONNX Runtime instead of PyTorch for embeddings


## Old content

See [2024](../cohorts/2024/) and [2025](../cohorts/2025/) cohorts.
