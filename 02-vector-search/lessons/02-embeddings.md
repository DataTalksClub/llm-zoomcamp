# Embeddings

Before we can do vector search, we need to convert our text into
vectors. This process is called embedding the text into the vector space,
or "embedding" for short. Also, often by "embeddings" we also mean the 
vectors that we get as a result of this transformation.

An embedding model takes text as input and outputs a fixed-length array
of numbers (a vector).

The embedding model is trained in a way that texts with similar
meanings get similar vectors. This makes semantic search
possible.

We'll use [sentence-transformers](https://www.sbert.net/), a popular
open-source library for generating embeddings. It runs locally on your
machine, so there are no API costs.


## Installing sentence-transformers

```bash
uv add sentence-transformers
```

This also installs PyTorch under the hood. The download may take a
minute.


## Choosing a model

Sentence-transformers supports many models. The choice depends on your
task, language, and how much resources you have. For our FAQ dataset
(short English texts), a small model is sufficient.

We'll use `all-MiniLM-L6-v2`:

- 384-dimensional vectors (compact)
- Fast on CPU
- Good quality for general English text
- Uses cosine similarity (we'll explain this below)

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
```

The first time you run this, it downloads the model (~80 MB). After
that, it loads from a local cache.


## Trying it with simple examples

Let's see how embeddings work with
a few examples. We'll start with a query:

```python
q1 = 'Can I still join the course after the start date?'
v1 = model.encode(q1)
```

`v1` is a vector - an array with 384 numbers. 

Now let's encode our document:

```python
d  = "You don't need to register. You're accepted. You can also just start learning and submitting homework without registering."
dv = model.encode(d)
```

Next, we compare the query against the document using dot product:

```python
v1.dot(dv)
```

We get 0.32.

Let's take a different query:

```python
q2 = 'How to install Docker on Windows?'
v2 = model.encode(q2)
```

We can see that the similarity between this query and the document is smaller - they are less similar:

```python
v2.dot(dv)
```

And we get 0.01.

The first score for `q1` vs `d` (0.32) is be higher, so the query is more similar to the document about registration.

The second score (`q2` vs `d`) is be lower - it's near 0. Installing Docker has nothing to do with registration.

This is the core idea behind vector search: similar texts get similar
vectors, and we can measure similarity with a simple dot product.


## Cosine similarity

The `all-MiniLM-L6-v2` model outputs normalized vectors - vectors with
unit length. When both vectors are normalized, the dot product equals
cosine similarity. That's why the model documentation says it "uses
cosine similarity."

Cosine similarity measures the angle between two vectors, ignoring
their length:

- 1.0 = same direction (very similar)
- 0.0 = perpendicular (unrelated)
- -1.0 = opposite direction (opposite meaning)

TODO: let theta be the angle between vectorts. cos(theta) = 1 when 
cos(theta) = 0 when ..

Because our vectors are normalized, the dot product gives us cosine
similarity directly. This is why we can use `v1.dot(dv)` to compare
texts.

In practive we rarely get vectors that are smaller than 0 (TODO explain why).

[← What is Vector Search](01-intro.md) | [Embedding Our Dataset →](03-embeddings-dataset.md)
