# Vector Search with sqlitesearch

In the previous section, we used minsearch for vector search. It works,
but it has a problem: re-indexing on startup.

It's fine for text search because it's fast, but for vector search, computing embeddings takes a long time: it involves running a neural network over every document.

For one document we don't feel it, but for a large collections, 
it's significant and can take a lot of time.


## Saving and loading minsearch vectors 

The simplest way to solve it is to save the vectors:

```python
vindex.save('vector_index.pkl')
```

And load it back:

```python
vindex = VectorSearch.load('vector_index.pkl')
```

This avoids re-computing embeddings every time you restart.


But there are still two limitations with minsearch for vector search:

1. It keeps everything in memory - for large collections, this uses
   a lot of RAM
2. It uses brute-force search - it compares the query against every
   document. For our small dataset this is instant, but for millions
   of documents it becomes slow. You'd want approximate nearest
   neighbor (ANN) methods instead.

sqlitesearch solves it.

In module 1, we used sqlitesearch as a persistent replacement for
minsearch text search. sqlitesearch also supports vector search with
its `VectorSearchIndex` class. It stores vectors in SQLite and uses
approximate nearest neighbor (ANN) strategies for efficient retrieval.

## Creating the index

```python
from sqlitesearch import VectorSearchIndex

vs_index = VectorSearchIndex(
    keyword_fields=['course'],
    mode='lsh',
    db_path='faq_vectors.db'
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
    filter_dict={'course': 'data-engineering-zoomcamp'},
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
    mode='lsh',
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

The key advantage of sqlitesearch is persistence. In a separate
notebook, we can open the index and use it without re-computing
embeddings:

```python
from sentence_transformers import SentenceTransformer
from sqlitesearch import VectorSearchIndex

model = SentenceTransformer('all-MiniLM-L6-v2')

vs_index = VectorSearchIndex(
    keyword_fields=['course'],
    mode='lsh',
    db_path='faq_vectors.db'
)
```

No `fit` call needed. One notebook built the index, another notebook
queries it.

Now let's use it in our RAG pipeline. Set up `RAGBase`:

```python
from rag_helper import RAGBase
from openai import OpenAI

openai_client = OpenAI()

instructions = """
You're a course teaching assistant.
Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.
""".strip()

assistant = RAGBase(
    index=vs_index,
    llm_client=openai_client,
    instructions=instructions,
)
```

Vector search requires embedding the query, so we use `build_prompt`
and `llm` from `RAGBase` with manual search:

```python
def vector_rag(query, course='data-engineering-zoomcamp', num_results=5):
    query_vector = model.encode(query)
    search_results = vs_index.search(
        query_vector,
        filter_dict={'course': course},
        num_results=num_results
    )
    prompt = assistant.build_prompt(query, search_results)
    answer = assistant.llm(prompt)
    return answer
```

Try it:

```python
vector_rag('I just discovered the course. Can I still join it?')
```


## Comparing minsearch and sqlitesearch for vector search

| | minsearch `VectorSearch` | sqlitesearch `VectorSearchIndex` |
|---|---|---|
| Storage | In-memory (numpy) | Persistent (SQLite `.db` file) |
| Search | Exact cosine similarity | ANN (LSH/IVF/HNSW) + exact rerank |
| Startup | Must re-compute embeddings | Open existing index |
| Best for | Experiments, notebooks | Projects, persistence |

[← RAG with Vector Search](04-rag-vector.md) | [Vector Search with PGVector →](06-pgvector.md)
