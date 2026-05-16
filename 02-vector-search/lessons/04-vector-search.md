# Vector Search

In the previous lesson, we embedded our FAQ dataset into a matrix `X`
with 1208 document vectors. Now let's see how vector search works
under the hood.


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

This is matrix-vector multiplication, and it's typically very very fast. Each element `i` of the `scores` vector is the cosine similarity between the document `i` (on row `i`) and `v_query`.


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

We can also look at the top 5 results:

```python
top5 = np.argsort(scores)[-5:]
```

We get the last 5 results (sorting it from lowest to highest in numpy).
This returns an array with 5 indicies:

```python
array([558, 472,  29, 955, 553])
```

Next, we need to reverse them:

```python
top5 = top5[::-1]
top5
```

Now we can see the top 5 scores:

```python
scores[top5]
```

Let's see the actual documents:

```python
for idx in top5:
    print(scores[idx])
    print(documents[idx])
    print()
```

This is vector search in its simplest form: embed the query, compute
dot products with all documents, return the ones with the highest scores.

Doing this manually with numpy works fine for small datasets. For
larger ones, you'd want a search library that handles filtering and ranking.
We'll use special libraries for that.

[← Embedding Our Dataset](03-embeddings-dataset.md) | [Vector Search with minsearch →](05-minsearch-vector.md)
