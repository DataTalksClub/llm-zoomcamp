# Vector Search with MinSearch

In the previous section, we saw how vector search works with numpy:
embed the query, compute dot products, find the best match. minsearch
does exactly the same thing, but it follows the same interface we
already know from module 1 - `fit`, `search`, `filter_dict`, and all
the rest.

It's the simplest way to get started with vector search.


## Creating the index

We already have our documents and vectors from the previous section.
Now let's index them:

```python
from minsearch import VectorSearch

vindex = VectorSearch(keyword_fields=["course"])
vindex.fit(X, documents)
```

We pass the numpy array `X` with all embeddings and the list of
documents as payload. The `keyword_fields` parameter works the same
as in the text `Index` - it lets us filter by course.


## Searching

Let's search for a question:

```python
query = "I just discovered the course. Can I still join it?"
query_vector = model.encode(query)

results = vindex.search(query_vector, num_results=5)
```

Look at the top result:

```python
results[0]
```

It should return the document about joining the course late. The search
found it even though the query "I just discovered the course" doesn't
contain the exact keywords from the original question "Can I still join
the course after the start date?"

## Filtering by course

Like the text index, we can filter by keyword fields:

```python
results = vindex.search(
    query_vector,
    filter_dict={"course": "llm-zoomcamp"},
    num_results=5
)
```

This restricts the search to documents from the data engineering
course.

Let's use it in RAG now.