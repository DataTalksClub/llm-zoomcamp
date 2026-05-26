# Embeddings

Before we can do vector search, we need to convert our text into
vectors. This process is called embedding - we embed text into a vector
space. The resulting vectors are also called "embeddings."

## Word embeddings and sentence embeddings

This concept comes from
[word2vec](https://en.wikipedia.org/wiki/Word2vec). The model learns to
represent words as points in a multi-dimensional space. Words with
similar meanings end up close to each other.

Imagine a 2D space where "enroll" and "join" are near each other and
"Docker" is far away:

```text
        · enroll
       · join
                   · Docker
```

The same idea works for entire sentences:

```text
Q1: "I just discovered the course. Can I still join it?"
Q2: "I just found out about the program. Can I still enroll?"

These two are close - they mean the same thing.

Q3: "How do I run Docker on Windows?"

This one is far away from Q1 and Q2.
```

Now imagine all 1200 documents in our FAQ dataset. Each one is a point
in this space. When a user asks a question, we embed it into the same
space and find the closest documents. These nearest neighbors are the
search results.

Because the model encodes the entire sentence (not just individual
words), it can disambiguate words based on context. Consider the word
"judge." In "the judge ruled out the possibility of crime" (legal) it
gets one vector. In "LLM-as-a-judge approach to evaluate LLMs" (ML
evaluation) it gets a different one. The surrounding context changes
the embedding.

An embedding model takes text as input and outputs a fixed-length array
of numbers (a vector). The model is trained so that texts with similar
meanings get similar vectors.

We'll use [sentence-transformers](https://www.sbert.net/), a popular
open-source library for generating embeddings. It runs locally on your
machine, so there are no API costs.

## Installing sentence-transformers

Install the library:

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
a few examples.

We'll start with a query:

```python
q1 = 'Can I still join the course after the start date?'
v1 = model.encode(q1)
```

`v1` is a vector - an array with 384 numbers. 

Encode our document:

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

The first score for `q1` vs `d` (0.32) is higher, so the query is more similar to the document about registration.

The second score (`q2` vs `d`) is lower - it's near 0. Installing Docker has nothing to do with registration.

This is the core idea behind vector search: similar texts get similar
vectors. We can measure similarity with a simple dot product.

## Cosine similarity

The `all-MiniLM-L6-v2` model outputs normalized vectors - vectors with
unit length. When both vectors are normalized, the dot product equals
cosine similarity. That's why the model documentation says it "uses
cosine similarity."

Cosine similarity measures the angle between two vectors, ignoring
their length:

- 1.0 = same direction (similar)
- 0.0 = perpendicular (unrelated)
- -1.0 = opposite direction (opposite meaning)

Formally, if `theta` is the angle between two vectors, cosine similarity
is `cos(theta)`:

- `cos(0) = 1` - vectors point in the same direction
- `cos(90) = 0` - vectors are perpendicular
- `cos(180) = -1` - vectors point in opposite directions

Because our vectors are normalized, the dot product gives us cosine
similarity directly. This is why we can use `v1.dot(dv)` to compare
texts.

In practice, we rarely get cosine similarity below 0. The embedding
model maps text to a region of the vector space where most vectors
have positive components. There's no concept of "opposite meaning"
that maps to a vector pointing the other way.

[← What is Vector Search](01-intro.md) | [Embedding Our Dataset →](03-embeddings-dataset.md)
