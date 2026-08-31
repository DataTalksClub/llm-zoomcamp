# Next Steps

In this module, we covered hybrid search and document reranking,
two of the most impactful techniques for improving RAG quality.

The key takeaways:

- Hybrid search combines vector and keyword search for better
  retrieval. It works because vector search captures semantic
  meaning while keyword search catches exact term matches.
- Reranking re-orders results with a better relevance score. Even
  a simple RRF implementation can improve metrics.
- LangChain wraps Elasticsearch functionality in a cleaner
  interface, but the underlying queries are the same.

## Other techniques to explore

We only covered two of the five techniques from the intro lesson.

Here are pointers for the rest:

- Small-to-big chunk retrieval: use small chunks for embedding
  but retrieve surrounding context for the LLM. Look at
  LangChain's ParentDocumentRetriever.
- Document metadata: add titles, topics, dates as filterable
  fields in your search index. Use them to narrow results before
  ranking.
- Query rewriting: ask an LLM to reformulate the user's question
  into a clearer search query before hitting the database.

## To learn more

Check out these resources:

- [Advanced RAG techniques overview](https://arxiv.org/abs/2312.10997)
- [LangChain retrieval docs](https://python.langchain.com/docs/concepts/retrievers/)

[← Hybrid Search with LangChain](04-langchain.md) | [Back to module →](../)
