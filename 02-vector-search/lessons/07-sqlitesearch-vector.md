# Vector Search with sqlitesearch

In the previous section, we used minsearch for vector search.

It works, but it has a few problems:

- Indexing on startup
- Keeping everything in memory
- Brute-force search

In case of text search, we didn't feel these problems. Indexing was
fast, because we didn't need to embed text into vectors.

For vector search, it takes some time: we run a neural network over
every document.

Then, we keep everything in memory. For this dataset it is not a
problem, but for larger datasets it would take too much space.

And the last problem: for each search query, we compare the query
vector with every single document by matrix multiplication. This is
not a problem for our small dataset. It is probably even faster than
other approaches.

But as our dataset grows, it would take more and more time. Eventually
we will need to switch to approximate methods and use approximate
nearest neighbor (ANN) search instead.

What we've done so far is exact nearest neighbor (NN) search. For each
query, we compute the similarity against every single document and pick
the top ones. With 1,000 documents this is fast. It is even faster than
smarter approaches. But at 10,000+ documents, it gets slow.

Approximate nearest neighbor (ANN) search takes a shortcut. Instead of
comparing the query against everything, it first narrows down to a
region of documents that are likely similar. Then it computes exact
scores only within that region. It may miss the absolute best match, but
the results are still good, and it is much faster.

```text
NN (exact):    compare query against ALL documents -> top 5
ANN (approx):  narrow down to a region -> compare within region -> top 5
```

## sqlitesearch

sqlitesearch (the persistent sibling of minsearch) solves it.

We already used it in module 1 for persistent text search. It also
supports vector search with its `VectorSearchIndex` class. It stores
vectors in SQLite and uses approximate nearest neighbor (ANN) strategies
for efficient retrieval.

If you didn't install it in the previous module, add it to your project:

```bash
uv add sqlitesearch
```

## Creating the index

Initialize it:

```python
from sqlitesearch import VectorSearchIndex

vs_index = VectorSearchIndex(
    keyword_fields=['course'],
    mode='ivf',
    db_path='faq_vectors2.db'
)
```

sqlitesearch supports three ANN modes:

- `lsh` (default): up to 100K vectors, random hyperplane projections
- `ivf`: 10K-500K vectors, K-means clustering
- `hnsw`: 10K-1M+ vectors, proximity graph (highest recall)

For our small dataset, `lsh` is fine. All modes use two-phase search:
approximate candidate retrieval, then exact cosine similarity
reranking.

## Indexing the data

Fit the index with our vectors and documents:

```python
vs_index.fit(vectors, documents)
```

The index is saved to `faq_vectors2.db`. Unlike minsearch, this file
persists on disk. You can search immediately after indexing, or reopen
the index later without re-indexing.

## Searching

Search works the same way as with minsearch:

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

## Closing the connection

When you're done with the index:

```python
vs_index.close()
```


## Reopening the index

In a new Python session, you can reopen the index without re-computing
embeddings:

```python
from sentence_transformers import SentenceTransformer
from sqlitesearch import VectorSearchIndex

model = SentenceTransformer('all-MiniLM-L6-v2')

vs_index = VectorSearchIndex(
    keyword_fields=['course'],
    mode='ivf',
    db_path='faq_vectors2.db'
)
```

Now we can search:

```python
query_vector = model.encode('How do I run Kafka?')
results = vs_index.search(query_vector, num_results=5)
```

We still need to load the embedding model to encode the query. But we
don't need to re-embed all the documents. No `fit` call needed. The
index is already built and ready.

This is the same two-process architecture we used for text search in
module 1. One process ingests and builds the index, another process
queries it.

## Using sqlitesearch vector search in RAG

Let's use our persistent vector index in RAG.

In a new notebook, set up the model and open the index (same as
the "Reopening the index" section above):

```python
from sentence_transformers import SentenceTransformer
from sqlitesearch import VectorSearchIndex

model = SentenceTransformer('all-MiniLM-L6-v2')

vs_index = VectorSearchIndex(
    keyword_fields=['course'],
    mode='ivf',
    db_path='faq_vectors2.db'
)
```

We'll use the `RAGVector` class we defined in the
[previous lesson](06-rag-vector.md). It overrides the `search` method
to embed the query and use vector search.

Set up the OpenAI client and create the assistant:

```python
from rag_helper import RAGBase
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_client = OpenAI()

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

vector_assistant = RAGVector(
    embedder=model,
    index=vs_index,
    llm_client=openai_client,
)
```

Try it:

```python
vector_assistant.rag('the program has already begun, can I still sign up?')
```

When you're done, close the connection:

```python
vs_index.close()
```

## Comparing minsearch and sqlitesearch for vector search

Here is how the two compare:

- minsearch `VectorSearch`: in-memory (numpy), exact cosine similarity,
  must re-compute embeddings on startup, good for experiments and
  notebooks
- sqlitesearch `VectorSearchIndex`: persistent (SQLite `.db` file), ANN
  (LSH/IVF/HNSW) with exact rerank, can open an existing index, good
  for projects and persistence

[← RAG with Vector Search](06-rag-vector.md) | [Vector Search with PGVector →](08-pgvector.md)
