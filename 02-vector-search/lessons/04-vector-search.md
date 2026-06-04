# Vector Search

Video: [Watch this lesson](https://www.youtube.com/watch?v=h-_tdBc24qc&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

In the previous lesson we embedded our FAQ dataset into a matrix `X`
with 1208 document vectors. Here we see how vector search works under
the hood.

## Scoring documents

We have a matrix `X` with all document embeddings. We take a query,
compare it against every document, and keep the most similar ones.

When a query comes in, we embed it:

```python
query = "Can I still join the course after the start date?"
v_query = model.encode(query)
```

Next, we compute the dot product against all documents:

```python
scores = X.dot(v_query)
```

This is matrix-vector multiplication. Each element `i` of `scores` is
the cosine similarity between document `i` (row `i` of `X`) and
`v_query`.

We could compute the same thing with a for loop:

```python
scores = [v_query.dot(X[i]) for i in range(len(X))]
```

But `X.dot(v_query)` is much faster. Numpy runs optimized C code instead
of looping in Python, so the matrix version is hard to beat. The outcome
is the same either way: one score per document.

## Best match

The highest score is the most similar document:

```python
idx = np.argmax(scores)
idx, scores[idx]
```

This returns document 553 with score 0.76.

The index and score may differ for you. Our FAQ is a living document, so
we add and remove entries over time.

Let's see which document it is:

```python
documents[idx]
```

We see:

```python
{"id": "3f1424af17",
 "course": "data-engineering-zoomcamp",
 "section": "General Course-Related Questions",
 "question": "Course: Can I still join the course after the start date?",
 "answer": "Yes, even if you don't register, you're still eligible..."}
```

## Top 5 results

Usually we want more than the single best match, so let's pull the top
5.

`np.argsort` sorts from lowest to highest, so the last 5 are the top
ones:

```python
top5 = np.argsort(scores)[-5:]
```

They come out smallest-first, so we reverse them to get the highest
first:

```python
top5 = top5[::-1]
top5
```

Now we can read off the top 5 scores:

```python
scores[top5]
```

There's a shorter trick I usually reach for. We negate the scores
first, so the largest becomes the smallest. Then `argsort` puts the best
matches at the front.

Here it is in one line:

```python
top5 = np.argsort(-scores)[:5]
```

It looks cryptic the first time you see it. But it's a common way to
turn a min-sort into a max-sort.

Let's read off the actual documents:

```python
for idx in top5:
    print(scores[idx])
    print(documents[idx])
    print()
```

This is vector search in its simplest form. We embed the query, compute
dot products against all documents, and return the highest-scoring ones.

We return 5 and not the single best for a reason. The answer to a
question can be spread across several documents. One holds part of it,
another fills in the rest. Sometimes the top result isn't the right one
but the second is. We send all 5 to the LLM and let it combine them.

The number 5 is a starting point, picked on gut feeling. Later, when we
evaluate search quality, we can test whether 3 or 10 works better for
our data.

Doing this by hand with numpy is fine for a small dataset. A larger one
needs a library that also handles filtering and ranking. That's what we
turn to next.

[← Embedding Our Dataset](03-embeddings-dataset.md) | [Vector Search with minsearch →](05-minsearch-vector.md)
