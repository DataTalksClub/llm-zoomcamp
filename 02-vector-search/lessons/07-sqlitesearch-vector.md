# Vector Search with sqlitesearch

In the previous section, we used minsearch for vector search.

It works, but it has a few problems problem:

- Indexing on startup
- Keeping everything in memory
- Brute-force search

In case of text search, we didn't really feel these problems. Indexing was fast, becase we didn't need to embed text into vectors.

For vector search, it takes some time: we run a neural network over every document.

Then, we keep everything in memory. For this dataset it's not a problem, but for larger datasets it would take too much space. 

And the last problem - for each search query, we compare the query vector 
with every single document (by doing matrix multiplication). Again, for such 
a small dataset such as ours it's actually not a problem.
It's probably even faster than other approaches.

But as our dataset grows, it would take more and more time.
Eventually we will need to switch to approximate methods and use 
approximate nearest neighbor (ANN) search instead.


## sqlitesearch

sqlitesearch (the persistant sibling of minsearch) solves it.

We already used it in module 1 for persistant text search.
It also supports vector search with its `VectorSearchIndex` class.

It stores vectors in SQLite and uses
approximate nearest neighbor (ANN) strategies for efficient retrieval.

If you didn't install it in the previous module, add it to your project:

```bash
uv add sqlitesearch
```

## Creating the index

Now let's initialize it:

```python
from sqlitesearch import VectorSearchIndex

vs_index = VectorSearchIndex(
    keyword_fields=['course'],
    mode='ivf',
    db_path='faq_vectors2.db'
)
```

sqlitesearch supports three ANN modes:

| Mode | Best for | How it works |
|---|---|---|
| `lsh` (default) | Up to 100K vectors | Random hyperplane projections |
| `ivf` | 10K-500K vectors | K-means clustering |
| `hnsw` | 10K-1M+ vectors | Proximity graph (highest recall) |

For our small dataset, `lsh` is fine. All modes use two-phase search:
approximate candidate retrieval, then exact cosine similarity
reranking.


## Indexing the data

Fit the index with our vectors and documents:

```python
vs_index.fit(vectors, documents)
```

The index is saved to `faq_vectors.db`. Unlike minsearch, this file
persists on disk. You can search immediately after indexing, or reopen
the index later without re-indexing.


## Searching

```python
query = 'I just discovered the course. Can I still join it?'
query_vector = model.encode(query)

results = vs_index.search(query_vector, num_results=5)
```

Look at the results:

```python
results
```


## Filtering by course

Filtering works the same way:

```python
results = vs_index.search(
    query_vector,
    filter_dict={'course': 'llm-zoomcamp'},
    num_results=5
)
```


## Reopening the index

The key advantage of sqlitesearch is persistence. In a new Python
session, you can reopen the index without re-computing embeddings:

```python
from sqlitesearch import VectorSearchIndex

vs_index = VectorSearchIndex(
    keyword_fields=['course'],
    mode='ivf',
    db_path='faq_vectors.db'
)

query_vector = model.encode('How do I run Kafka?')
results = vs_index.search(query_vector, num_results=5)
```

No `fit` call needed. The index is already built and ready.

This is the same two-process architecture we used for text search in
module 1: one process ingests and builds the index, another process
queries it.


## Closing the connection

When you're done:

```python
vs_index.close()
```


## Using sqlitesearch vector search in RAG

Since sqlitesearch is persistent, we can open a separate notebook
and use it without re-computing embeddings:

```python
from sentence_transformers import SentenceTransformer
from sqlitesearch import VectorSearchIndex

model = SentenceTransformer('all-MiniLM-L6-v2')

vs_index = VectorSearchIndex(
    keyword_fields=['course'],
    mode='ivf',
    db_path='faq_vectors.db'
)
```

No `fit` call needed. One notebook built the index, another notebook
queries it.

Now let's use it in our RAG pipeline. We'll use `RAGVector` from the
previous lesson - it's a subclass of `RAGBase` that handles embedding
the query:

```python
from rag_helper import RAGBase
from openai import OpenAI

class RAGVector(RAGBase):

    def __init__(self, embedder, **kwargs):
        super().__init__(**kwargs)
        self.embedder = embedder

    def search(self, query, num_results=5):
        query_vector = self.embedder.encode(query)
        filter_dict = {'course': self.course}

        return self.index.search(
            query_vector,
            num_results=num_results,
            filter_dict=filter_dict
        )

openai_client = OpenAI()

assistant = RAGVector(
    embedder=model,
    index=vs_index,
    llm_client=openai_client,
)
```

Try it:

```python
assistant.rag('I just discovered the course. Can I still join it?')
```


## Comparing minsearch and sqlitesearch for vector search

| | minsearch `VectorSearch` | sqlitesearch `VectorSearchIndex` |
|---|---|---|
| Storage | In-memory (numpy) | Persistent (SQLite `.db` file) |
| Search | Exact cosine similarity | ANN (LSH/IVF/HNSW) + exact rerank |
| Startup | Must re-compute embeddings | Open existing index |
| Best for | Experiments, notebooks | Projects, persistence |

[← RAG with Vector Search](06-rag-vector.md) | [Vector Search with PGVector →](08-pgvector.md)
