# Vector Search

This is the second module of the
[LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) -
a free course about building LLM applications.

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


## Workshop sections

1. [What is Vector Search](01-intro.md) - Keyword search vs vector search, why it matters
2. [Embeddings](02-embeddings.md) - Turning text into vectors with sentence-transformers
3. [Vector Search with MinSearch](03-minsearch-vector.md) - In-memory vector search
4. [RAG with Vector Search](04-rag-vector.md) - Replacing keyword search with vector search in our RAG pipeline
5. [Vector Search with sqlitesearch](05-sqlitesearch-vector.md) - Persistent vector search backed by SQLite
6. [Vector Search with PGVector](06-pgvector.md) - Production vector search with PostgreSQL and pgvector
7. [Text vs Vector Search](07-text-vs-vector.md) - Comparing keyword and vector search side by side
8. [Hybrid Search](08-hybrid-search.md) (Optional) - Combining keyword and vector search for better results
9. [ONNX Embedder](09-onnx-embedder.md) (Optional) - Using ONNX Runtime instead of PyTorch for embeddings
