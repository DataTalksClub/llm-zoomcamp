# Text Search vs Vector Search

Now that we've used both keyword search and vector search, let's compare
them side by side on the same queries.


## Setting up both search functions

We need both search functions ready. The vector search function is from
the previous section:

```python
def vector_search(query, course='data-engineering-zoomcamp', num_results=5):
    query_vector = model.encode(query)
    return vindex.search(
        query_vector,
        filter_dict={'course': course},
        num_results=num_results
    )
```

And the keyword search function from module 1:

```python
from minsearch import Index

text_index = Index(
    text_fields=['question', 'answer', 'section'],
    keyword_fields=['course']
)
text_index.fit(documents)

def keyword_search(query, course='data-engineering-zoomcamp', num_results=5):
    boost_dict = {'question': 3.0, 'section': 0.5}
    return text_index.search(
        query,
        num_results=num_results,
        boost_dict=boost_dict,
        filter_dict={'course': course}
    )
```


## Comparing results

Let's run both searches on the same queries and look at the top
questions each returns.

Query 1 - a natural language question:

```python
query = 'Can I still join the course?'

print('Keyword search:')
print([doc['question'] for doc in keyword_search(query)])

print('Vector search:')
print([doc['question'] for doc in vector_search(query)])
```

Both should find the right answer, but vector search may also find
semantically related documents that keyword search misses.

Query 2 - a specific tool name:

```python
query = 'pandas dataframe'

print('Keyword search:')
print([doc['question'] for doc in keyword_search(query)])

print('Vector search:')
print([doc['question'] for doc in vector_search(query)])
```

Keyword search should be more precise here - it matches "pandas"
directly. Vector search might return results about data manipulation
more broadly.

Query 3 - a paraphrased question:

```python
query = "I'm having trouble with my homework submission"

print('Keyword search:')
print([doc['question'] for doc in keyword_search(query)])

print('Vector search:')
print([doc['question'] for doc in vector_search(query)])
```

Vector search should do better here - it can match the meaning of
"trouble with homework submission" even if the FAQ doesn't use those
exact words.


## Observations

In general:

- Keyword search is better when the query contains specific terms,
  names, or identifiers that must match exactly
- Vector search is better when the query is phrased in natural language
  and the meaning matters more than the exact words
- For some queries, both return similar results

Neither is always better. This is why in the next section we'll combine
them with hybrid search.


## When to add vector search

Text search is cheap, fast, easy to implement, and easy to maintain.
Vector search adds overhead: it's slower, requires a model, and adds
more dependencies.

So don't start with vector search. My first version always uses text
search. Only after I see that the initial version works, I would try
introducing vector search. I'd evaluate - and we'll talk about
evaluation later - to see if it actually brings value. If it does, then
I add vector search.

In practice, vector search does help - I see in many cases that the
results become better. But the question is: how much better? And is the
increase in search quality worth all the overhead we introduce?


## A quick comparison

| | Keyword search | Vector search |
|---|---|---|
| How it matches | Exact words | Semantic meaning |
| Good for | Tool names, error messages, IDs | Natural language, paraphrased queries |
| Speed | Very fast (no neural network) | Slower (needs embedding inference) |
| Indexing | Instant (TF-IDF) | Slow (neural network inference) |
| Persistence | Easy (re-index on startup) | Important (embeddings are expensive to recompute) |

In the next section, we'll combine both approaches with hybrid search.

[← Vector Search with PGVector](06-pgvector.md) | [Hybrid Search →](08-hybrid-search.md)
