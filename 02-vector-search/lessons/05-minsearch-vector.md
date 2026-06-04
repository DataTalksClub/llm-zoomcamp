# Vector Search with minsearch

Video: [Watch this lesson](https://www.youtube.com/watch?v=E7KdO3xmESg&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

In the previous section we did vector search by hand with numpy. We
embedded the query, computed dot products, and found the best matches.
Writing the argsort and matrix code every time gets old, and it can't
filter by course. So instead we'll use a library that wraps all of it.

We'll use [minsearch](https://github.com/alexeygrigorev/minsearch), the
small in-memory search library we already used in module 1 for text
search. It has a `VectorSearch` class for vector search.

Both classes share the same API:

- `fit` to index data
- `search` to query
- `filter_dict` in `search` to filter by keyword

It's the simplest way to get started with vector search.

## Creating the index

We already have our documents and vectors from the previous section.

Index them:

```python
from minsearch import VectorSearch

vindex = VectorSearch(keyword_fields=["course"])
vindex.fit(X, documents)
```

We pass the numpy array `X` with all embeddings and the list of
documents as payload. The `keyword_fields` parameter works the same as
in the text `Index`, so we can filter by course later.

## Searching

Let's search for a question:

```python
query = "I just discovered the course. Can I still join it?"
query_vector = model.encode(query)

results = vindex.search(query_vector, num_results=5)
```

Under the hood it does the same thing we just did by hand. It computes
the dot product between each vector (after filtering) and our query
vector.

Look at the top result:

```python
results[0]
```

It should return the document about joining the course late:


```python
{"id": "74eb249bbf",
 "course": "llm-zoomcamp",
 "section": "General Course-Related Questions",
 "question": "I just discovered the course. Can I still join?",
 "answer": "Yes, but if you want to receive a certificate, you need to submit your project while we’re still accepting submissions."}
```

## Filtering by course

Like the text index, we can filter by keyword fields. This matters for
user experience. A student in LLM Zoom Camp doesn't care about answers
from the data engineering course. So we narrow to their course first,
then score only within it.

Pass a `filter_dict`:

```python
results = vindex.search(
    query_vector,
    filter_dict={"course": "llm-zoomcamp"},
    num_results=5
)
```

Now that we can run vector search, let's use it in RAG.

[← Vector Search](04-vector-search.md) | [RAG with Vector Search →](06-rag-vector.md)
