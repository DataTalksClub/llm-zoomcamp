# Best Practices for RAG

In the previous modules we built search engines, agents, evaluation
pipelines, and monitoring dashboards. This module covers techniques
that improve retrieval quality - the most critical part of any RAG
system.

## The RAG pipeline

A RAG system has two stages:

- Indexing: documents are parsed, chunked, embedded, and stored in
  a vector database
- Retrieval: the user's question is embedded, the database is
  searched for the closest documents, and those documents are
  passed to the LLM as context

Most of the improvements we'll discuss focus on the retrieval
stage, because better retrieval means better answers.

## Five techniques

Here are the five techniques we'll cover:

1. Small-to-big chunk retrieval - use small chunks for indexing
   but retrieve surrounding context for the LLM
2. Leveraging document metadata - use titles, topics, dates, and
   other metadata to filter and boost results
3. Hybrid search - combine vector search (semantic) with keyword
   search (lexical) in one query
4. User query rewriting - use an LLM to reformulate the user's
   question into a better search query
5. Document reranking - re-order retrieved documents by relevance
   after the initial search

In this module, we'll focus on hybrid search and reranking. These
two techniques give the biggest improvement for the least effort.

Slides: [llm-zoomcamp-best-practicies.pdf](../llm-zoomcamp-best-practicies.pdf)

To learn more:

- [Survey on RAG techniques](https://arxiv.org/abs/2312.10997)

[← Back to module](../) | [Hybrid Search →](02-hybrid-search.md)
