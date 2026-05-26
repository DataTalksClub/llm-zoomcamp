# Vector Search

In the previous lesson, we embedded our FAQ dataset into a matrix `X`
with 1208 document vectors. This lesson shows how vector search
works under the hood.

## Scoring documents

We have a matrix `X` with all document embeddings.

When a query comes in, we embed it:

```python
query = 'Can I still join the course after the start date?'
v_query = model.encode(query)
```

Next, we compute the dot product against all documents:

```python
scores = X.dot(v_query)
```

This is matrix-vector multiplication, and it's typically fast. Each element `i` of the `scores` vector is the cosine similarity between the document `i` (on row `i`) and `v_query`.

We could do the same thing with a for loop:

```python
scores = [v_query.dot(X[i]) for i in range(len(X))]
```

But `X.dot(v_query)` is much faster. Numpy uses optimized C code
under the hood instead of iterating in Python. The outcome is the same:
a score for every document.

## Best match

The highest score is the most similar document:

```python
idx = np.argmax(scores)
idx, scores[idx]
```

This returns a document 553 with score 0.76.

Note: this may change for you because our dataset is evolving over time.

Let's see which document is it:

```python
documents[idx]
```

We see:

```python
{'id': '3f1424af17',
 'course': 'data-engineering-zoomcamp',
 'section': 'General Course-Related Questions',
 'question': 'Course: Can I still join the course after the start date?',
 'answer': "Yes, even if you don't register, you're still eligible..."}
```

## Top 5 results

We can also look at the top 5 results.

`np.argsort` sorts from lowest to highest, so the last 5 are the top ones:

```python
top5 = np.argsort(scores)[-5:]
```

We need to reverse them to get the highest first:

```python
top5 = top5[::-1]
top5
```

We can see the top 5 scores:

```python
scores[top5]
```

There's also a shortcut - negate the scores first, so `argsort` gives
us the highest first directly:

```python
top5 = np.argsort(-scores)[:5]
```

Let's see the actual documents:

```python
for idx in top5:
    print(scores[idx])
    print(documents[idx])
    print()
```

This is vector search in its simplest form. We embed the query, compute
dot products with all documents, and return the highest-scoring ones.

We return top 5 and not just the best match. The answer to a question
might be spread across multiple documents. One has part of it, another
fills in the rest. Sometimes the top result is not the right one, but
the second is. We send all 5 to the LLM so it can combine them.

The number 5 is a starting point. Later, when we evaluate our search
quality, we can test whether 3 or 10 works better for our data.

Doing this manually with numpy works fine for small datasets. For
larger ones, you'd want a search library that handles filtering and ranking.
We'll use special libraries for that.

[← Embedding Our Dataset](03-embeddings-dataset.md) | [Vector Search with minsearch →](05-minsearch-vector.md)
