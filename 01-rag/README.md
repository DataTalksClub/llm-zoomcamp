# Module 1: RAG and Vector Search

In this module, we learn what LLMs and RAG are, build a simple RAG
pipeline using keyword search, and then improve it with vector search
that matches on meaning rather than exact words.

Videos:

- RAG: https://www.youtube.com/watch?v=KSItlTAsMsk
- Vector Search: https://www.youtube.com/watch?v=BC3NsRUNEIg

Code: [code/](code/)


## Part 1: RAG

1. [Introduction](rag/01-intro.md) - What we'll build and why
2. [Environment Setup](rag/02-environment.md) - Python, uv, OpenAI API
3. [What is RAG](rag/03-rag.md) - Why LLMs need context, the RAG architecture
4. [The Course FAQ Dataset](rag/04-dataset.md) - Fetching and exploring the FAQ data
5. [Search](rag/05-search.md) - Building a search engine with minsearch
6. [Building a Prompt](rag/06-building-prompt.md) - Combining search results into a prompt
7. [RAG Pipeline](rag/07-llm.md) - Wiring search + prompt + LLM together
8. [RAG Helper](rag/08-rag-helper.md) - Reusable RAGBase class and data loading
9. [Data Ingestion](rag/09-data-ingestion.md) - Persistent search with sqlitesearch
10. [Next Steps](rag/10-next-steps.md) - Where to go from here


## Part 2: Vector Search

1. [What is Vector Search](vector-search/01-intro.md) - Keyword search vs vector search, why it matters
2. [Embeddings](vector-search/02-embeddings.md) - Turning text into vectors with sentence-transformers
3. [Embedding Our Dataset](vector-search/03-embeddings-dataset.md) - Generating embeddings for the FAQ dataset
4. [Vector Search](vector-search/04-vector-search.md) - Vector search with numpy
5. [Vector Search with minsearch](vector-search/05-minsearch-vector.md) - In-memory vector search
6. [RAG with Vector Search](vector-search/06-rag-vector.md) - Replacing keyword search with vector search in our RAG pipeline
7. [Vector Search with sqlitesearch](vector-search/07-sqlitesearch-vector.md) - Persistent vector search backed by SQLite
8. [Vector Search with PGVector](vector-search/08-pgvector.md) - Production vector search with PostgreSQL and pgvector
9. [ONNX Embedder](vector-search/09-onnx-embedder.md) (Optional) - Using ONNX Runtime instead of PyTorch for embeddings
10. [Next Steps](vector-search/10-next-steps.md) - When to use vector search and what's next


## Optional

- [Build a Search Engine](https://www.youtube.com/watch?v=nMrGK5QgPVE) ([Code](https://github.com/alexeygrigorev/build-your-own-search-engine)) - How minsearch was built from scratch


## Old content

See old content for [2024](../cohorts/2024/) and [2025](../cohorts/2025/) cohorts.


## Notes 

- Add your notes above this line
