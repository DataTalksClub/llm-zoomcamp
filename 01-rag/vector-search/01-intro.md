# Vector Search

In the first module, we used keyword search with minsearch and
sqlitesearch. This approach matches exact words. Search for "Docker"
and the document must contain "Docker" to match.

But consider these two questions:

- "Can I still join the course after the start date?"
- "Is it possible to enroll late?"

They mean the same thing, but share almost no keywords. A keyword
search engine would struggle to match them.

Vector search solves this by working on the level of meaning. Instead of
matching words, it matches ideas.

## The vector search process

Vector search has two stages.

1. Offline (indexing): Convert all documents into vectors (arrays of
   numbers). Store them in an index.
2. Online (querying): Convert the user's query into a vector with
   the same model. Find the closest document vectors by similarity.

The vectors are produced by an embedding model - a neural network
trained to capture semantic meaning. Similar texts get similar vectors.
Similarity between vectors is measured with a distance metric. The most
common one is cosine similarity.

Cosine similarity measures the angle between two vectors:

- Vectors pointing in the same direction: similarity close to 1
  (similar)
- Vectors at right angles: similarity close to 0 (unrelated)
- Vectors pointing in opposite directions: similarity close to -1
  (opposite meaning)

The larger the cosine similarity, the more semantically similar the
texts are.

## Keyword search vs vector search

Key differences between the two approaches:

- Keyword search matches exact words. Vector search matches semantic
  meaning.
- Keyword search suits specific terms, IDs, and names. Vector search
  suits paraphrased questions and natural language.
- Keyword search example: "pandas dataframe". Vector search example:
  "How do I work with tabular data?"
- Keyword search uses an inverted index (BM25, TF-IDF). Vector search
  uses a vector index based on cosine similarity.
- Keyword search misses synonyms and paraphrases. Vector search misses
  exact term matches.

In practice, both approaches work best together. We'll cover hybrid
search at the end of this module.

## Building vector search

In this module, we'll take the same FAQ dataset from module 1 and build
vector search with three tools:

1. minsearch - in-memory vector search (simplest, good for
   experiments)
2. sqlitesearch - persistent vector search backed by SQLite
   (production-friendly, same API as minsearch)
3. PGVector - vector search in PostgreSQL (scalable, runs in
   Docker)

Then we'll integrate vector search into our RAG pipeline and explore
hybrid search that combines keyword and vector search.

The code from this module is available in the
[code directory](../code/).

## Prerequisites

In module 1, we set up a project with several libraries.

If you're
starting this module from scratch, create a new project and install
them:

```bash
mkdir llm-zoomcamp-code
cd llm-zoomcamp-code
uv init
uv add requests minsearch openai jupyter python-dotenv
```

You also need a `.env` file with your API key. See the
[module 1 environment setup](../rag/02-environment.md)
for details.

[← Back to module](../) | [Embeddings →](02-embeddings.md)
