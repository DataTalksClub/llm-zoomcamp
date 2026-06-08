# Module 2: Vector Search

In this module, we extend the RAG pipeline from
[module 1](../01-agentic-rag/) with vector search. Vector search
matches documents by semantic meaning instead of exact keyword
overlap. We start from embeddings and end with persistent vector
indexes (sqlitesearch, PGVector) and ONNX-based embedders for
lightweight deployments.

Code: [code/](code/)

Embeddings runtime: [embed/](embed/)


## Lessons

The lessons cover vector search end to end, from embeddings to
persistent indexes.

1. [What is Vector Search](lessons/01-intro.md) - Keyword search vs vector search, why it matters
2. [Embeddings](lessons/02-embeddings.md) - Turning text into vectors with sentence-transformers
3. [Embedding Our Dataset](lessons/03-embeddings-dataset.md) - Generating embeddings for the FAQ dataset
4. [Vector Search](lessons/04-vector-search.md) - Vector search with numpy
5. [Vector Search with minsearch](lessons/05-minsearch-vector.md) - In-memory vector search
6. [RAG with Vector Search](lessons/06-rag-vector.md) - Replacing keyword search with vector search in our RAG pipeline
7. [Vector Search with sqlitesearch](lessons/07-sqlitesearch-vector.md) - Persistent vector search backed by SQLite
8. [Vector Search with PGVector](lessons/08-pgvector.md) - Production vector search with PostgreSQL and pgvector
9. [ONNX Embedder](lessons/09-onnx-embedder.md) (Optional) - Using ONNX Runtime instead of PyTorch for embeddings
10. [Next Steps](lessons/10-next-steps.md) - When to use vector search and what's next


## Homework

- [Homework](../cohorts/2026/02-vector-search/homework.md)


## Original workshop recording

This module was taught as a live workshop, which we chopped into the
per-lesson videos above. To watch the full uncut recording:

- [Vector Databases: Embeddings, Semantic Search, and Hybrid Retrieval](https://www.youtube.com/watch?v=BC3NsRUNEIg)


## Old content

Earlier cohorts taught vector search differently. See the archived
materials for the [2024](../cohorts/2024/) and
[2025](../cohorts/2025/) cohorts.


## Notes

- Add your notes above this line
