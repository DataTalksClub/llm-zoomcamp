# Embeddings

Before we can do vector search, we need to convert our text into
vectors. This process is called embedding.

An embedding model takes text as input and outputs a fixed-length array
of numbers (a vector). The model is trained so that texts with similar
meanings get similar vectors. This is what makes semantic search
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
- Uses cosine similarity

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
```

The first time you run this, it downloads the model (~80 MB). After
that, it loads from a local cache.


## Trying it with simple examples

Before we embed our entire dataset, let's see how embeddings work with
a few examples. We'll use two queries and one document:

```python
q1 = 'Can I still join the course after the start date?'
q2 = 'How to install Docker on Windows?'
d  = "You don't need to register. You're accepted. You can also just start learning and submitting homework without registering."

v1 = model.encode(q1)
v2 = model.encode(q2)
dv = model.encode(d)
```

Now let's compare the queries against the document using dot product:

```python
v1.dot(dv)
```

```python
v2.dot(dv)
```

The first score (q1 vs d) should be higher - the query about joining
the course is more similar to the document about registration. The
second score (q2 vs d) should be lower - installing Docker has nothing
to do with registration.

This is the core idea behind vector search: similar texts get similar
vectors, and we can measure similarity with a simple dot product.


## Generating embeddings for our dataset

Now let's load our FAQ dataset and generate embeddings:

```python
from rag_helper import load_faq_data

documents = load_faq_data()
```

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

This is vector search in its simplest form: embed the query, compute
dot products with all documents, return the one with the highest score.

Doing this manually with numpy works fine for small datasets. For
larger ones, you'd want a search library that handles filtering and ranking.
We'll use special libraries for that.

[← What is Vector Search](01-intro.md) | [Vector Search with MinSearch →](03-minsearch-vector.md)
