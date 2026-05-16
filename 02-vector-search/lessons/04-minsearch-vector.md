# Vector Search with minsearch

In the previous section, we saw how vector search works with numpy:
embed the query, compute dot products, find the best match.

We'll use [minsearch](https://github.com/alexeygrigorev/minsearch) for that. 

It's  a small in-memory search library that we already used in module 1 for text search. 

Now we'll use its `VectorSearch` class for vector
search.

Both classes share the same API:

- `fit` to index data
- `search` to query
- `filter_dict` parameter in `search` for filtering by keyword


It's the simplest way to get started with vector search.


## Creating the index

We already have our documents and vectors from the previous section.
Now let's index them:

```python
from minsearch import VectorSearch

vindex = VectorSearch(keyword_fields=['course'])
vindex.fit(X, documents)
```

We pass the numpy array `X` with all embeddings and the list of
documents as payload. The `keyword_fields` parameter works the same
as in the text `Index` - it lets us filter by course.


## Searching

Let's search for a question:

```python
query = 'I just discovered the course. Can I still join it?'
query_vector = model.encode(query)

results = vindex.search(query_vector, num_results=5)
```

Under the hood it's doing the exact same thing we did in this module:
it's comptuting the dot product between each vector (after filtering)
and our query vector.

Look at the top result:

```python
results[0]
```

It should return the document about joining the course late:


```python
{'id': '74eb249bbf',
 'course': 'llm-zoomcamp',
 'section': 'General Course-Related Questions',
 'question': 'I just discovered the course. Can I still join?',
 'answer': 'Yes, but if you want to receive a certificate, you need to submit your project while we’re still accepting submissions.'}
```

## Filtering by course

Like the text index, we can filter by keyword fields:

```python
results = vindex.search(
    query_vector,
    filter_dict={'course': 'llm-zoomcamp'},
    num_results=5
)
```

Now we know to perform vector search, so we can use it in RAG.


[← Embedding Our Dataset](03-embeddings-dataset.md) | [RAG with Vector Search →](05-rag-vector.md)
