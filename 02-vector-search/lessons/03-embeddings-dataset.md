# Embedding Our Dataset

In the previous lesson, we saw how embeddings work with simple examples.
Now let's embed our entire FAQ dataset and see vector search in action.


## Loading the data

First, let's load our FAQ dataset:

```python
from ingest import load_faq_data

documents = load_faq_data()
```


## Generating embeddings

For vector search, we want to embed a combination of the question and
the answer. This way, when a user asks a question, we can match it
against both the questions and answers in our index:

```python
texts = [doc['question'] + ' ' + doc['answer'] for doc in documents]
```

Now generate the embeddings. We'll do it in batches with a progress bar:

```python
import numpy as np
from tqdm import tqdm

batch_size = 50
vectors = []

for i in tqdm(range(0, len(texts), batch_size)):
    batch = texts[i:i + batch_size]
    batch_vectors = model.encode(batch)
    vectors.extend(batch_vectors)

vectors = np.array(vectors)
```

This takes a few seconds. Let's check the shape:

```python
vectors.shape
```

You should see the total number of documents, each represented by a
384-dimensional vector.


## How vector search works

Now let's see how vector search works under the hood. We have a matrix
`vectors` with all document embeddings. When a query comes in, we embed
it and compute the dot product against all documents:

```python
query = 'Can I still join the course after the start date?'
v_query = model.encode(query)

scores = vectors.dot(v_query)
```

The highest score is the most similar document:

```python
idx = np.argmax(scores)
scores[idx]
```

```python
documents[idx]
```

Let's look at the top 5 results:

```python
top5 = np.argsort(scores)[-5:]
top5 = top5[::-1]
top5
```

`np.argsort` returns indices sorted by score (ascending). We take the
last 5 (highest scores) and reverse to get descending order.

```python
scores[top5]
```

```python
for idx in top5:
    print(scores[idx], documents[idx]['question'])
```

This is vector search in its simplest form: embed the query, compute
dot products with all documents, return the one with the highest score.

Doing this manually with numpy works fine for small datasets. For
larger ones, you'd want a search library that handles filtering and ranking.
We'll use special libraries for that.

[← Embeddings](02-embeddings.md) | [Vector Search with minsearch →](04-minsearch-vector.md)
