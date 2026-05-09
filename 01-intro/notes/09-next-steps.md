# Next Steps

We built a working RAG system. But this is just the beginning. Here's
what you'd explore next to make it production-ready.


## Summary

In this workshop, we:

- Learned what RAG is and why it matters: retrieve documents, build a
  prompt, let the LLM generate a grounded answer
- Built a search engine over a real FAQ dataset using minsearch
- Created a prompt template that combines the user's question with
  search results
- Wired search + prompt + LLM into a working RAG pipeline
- Split ingestion and query into separate processes with sqlitesearch

You now have a working RAG system and a clear mental model for how
each piece fits together. The rest is making each piece better.


## Vector search

Our search uses TF-IDF/BM25 - keyword-based matching. If the user
asks "How do I deploy my model?" but the FAQ says "serving
predictions in production", keyword search might miss it because the
words don't overlap.

Vector search (also called semantic search) solves this by encoding
the meaning of the text into vectors (arrays of numbers). Questions
and answers with similar meaning end up close together in vector
space, even if they use different words.

How it works:

- An embedding model (like OpenAI's `text-embedding-3-small` or
  open-source models from Sentence Transformers) converts each
  document into a vector.
- The user's question is also converted to a vector.
- We find the documents whose vectors are closest to the question
  vector (using cosine similarity or dot product).
- The closest documents are the search results.

You store the vectors in a vector database (Qdrant, Weaviate, Milvus,
Pinecone) and query with the vector of the user's question.

In the LLM Zoomcamp, Module 3 covers vector search in detail.


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

In the LLM Zoomcamp, we cover Elasticsearch in the supplementary
materials for Module 1.


## Agents

In our RAG pipeline, the flow is fixed: search once, then generate.
But sometimes one search isn't enough. The user's question might be
ambiguous, or the first search might return irrelevant results.

An agent puts the LLM in the driver's seat. Instead of a fixed
pipeline, the LLM decides what to do:

- It can search multiple times with different queries.
- It can open and read specific documents.
- It can decide when it has enough information to answer.
- It can use multiple tools (search, database lookup, API calls).

The key shift: from a hardcoded pipeline to an LLM that chooses
what to do next based on what it sees.

In the LLM Zoomcamp, Module 2 covers agents in detail.


## Evaluation

How do you know if your RAG system is good? You need to measure:

- Retrieval quality: Is the right document in the top results?
  Metrics like hit rate and MRR (Mean Reciprocal Rank) answer this.
- Generation quality: Is the answer correct and grounded in the
  documents? LLM-as-judge evaluation can help.
- End-to-end quality: Does the full pipeline produce good answers?

Without evaluation, you're flying blind. Any change you make to the
search, the prompt, or the model could make things worse without you
knowing.

In the LLM Zoomcamp, Module 4 covers evaluation in detail.


## Monitoring

Once your RAG system is live, you need to track:

- How many questions it answers
- User feedback (thumbs up/down)
- Retrieval quality over time (is the index getting stale?)
- LLM cost and latency

Monitoring helps you catch issues before users complain and guides
where to invest in improvements.

In the LLM Zoomcamp, Module 5 covers monitoring in detail.


## Where to go from here

- Try different prompts and see how the answers change
- Add more data sources to the knowledge base
- Experiment with different LLM models (GPT-4o, Claude, Gemini, local
  models via Ollama)
- Implement vector search with embeddings
- Try Elasticsearch as a search backend
- Build an agent that can search multiple times

For the full course with structured exercises, code, homework, and a
capstone project, see
[LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp).
