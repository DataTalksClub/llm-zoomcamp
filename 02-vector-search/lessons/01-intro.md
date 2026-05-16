# What is Vector Search

In the first module, we used keyword search with minsearch and
sqlitesearch. Keyword search works by matching exact words. If you
search for "Docker" and the document contains "Docker", it matches.

But consider these two questions:

- "Can I still join the course after the start date?"
- "Is it possible to enroll late?"

They mean the same thing, but share almost no keywords. A keyword
search engine would struggle to match them.

Vector search solves this by working on the level of meaning. Instead of
matching words, it matches ideas.


## How vector search works

Vector search has two stages:

1. Offline (indexing): Convert all your documents into vectors
   (arrays of numbers) and store them in an index.
2. Online (querying): Convert the user's query into a vector using
   the same model, then find the closest document vectors by
   similarity.

The vectors are produced by an embedding model - a neural network
trained to capture semantic meaning. Similar texts get similar vectors.
The similarity between vectors is measured with a distance metric, most
commonly cosine similarity.

Cosine similarity measures the angle between two vectors:

- Vectors pointing in the same direction: similarity close to 1
  (very similar)
- Vectors at right angles: similarity close to 0 (unrelated)
- Vectors pointing in opposite directions: similarity close to -1
  (opposite meaning)

The larger the cosine similarity, the more semantically similar the
texts are.


## Keyword search vs vector search

| | Keyword search | Vector search |
|---|---|---|
| Matches on | Exact words | Semantic meaning |
| Good for | Specific terms, IDs, names | Paraphrased questions, natural language |
| Example query | "pandas dataframe" | "How do I work with tabular data?" |
| Index | Inverted index (BM25, TF-IDF) | Vector index (cosine similarity) |
| Limitations | Misses synonyms, paraphrases | Misses exact term matches |

In practice, both approaches work best together. We'll cover hybrid
search at the end of this module.


## What we'll build

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


## Prerequisites

In module 1, we set up a project with several libraries. If you're
starting this module from scratch, create a new project and install
them:

```bash
mkdir llm-zoomcamp-code
cd llm-zoomcamp-code
uv init
uv add requests minsearch openai jupyter python-dotenv
```

You also need a `.env` file with your API key. See the
[module 1 environment setup](../../01-intro/lessons/02-environment.md)
for details.

In this module, we add one more dependency:

```bash
uv add sentence-transformers
```


## RAG helper files

Throughout this module, we'll use `rag_helper.py` and `ingest.py`
from module 1. These contain the `RAGBase` class, the data loading
functions, and other utilities we built earlier.

If you don't have them yet, download them:

```bash
wget https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/01-intro/code/rag_helper.py
wget https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/01-intro/code/ingest.py
```

For a reminder of how these files work, see the
[RAG Helper lesson](../../01-intro/lessons/08-rag-helper.md)
from module 1.

[← Back to module](../) | [Embeddings →](02-embeddings.md)
