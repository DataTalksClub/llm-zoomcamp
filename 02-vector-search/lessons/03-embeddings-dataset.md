# Embedding Our Dataset

Video: [Watch this lesson](https://www.youtube.com/watch?v=NC89mz1iG4E&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

In the previous lesson we saw how embeddings work on a couple of
examples. Now we apply them to the whole FAQ dataset.

## Loading the data

In [module 1](../../01-agentic-rag/) we created
[`ingest.py`](../../01-agentic-rag/code/ingest.py) for loading the
FAQ data.

Download it into your project:

```bash
wget https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/01-agentic-rag/code/ingest.py
```

We use it here:

```python
from ingest import load_faq_data

documents = load_faq_data()
```

## Generating embeddings

Each document is a Python dictionary with a question and an answer. We
embed both together. That way a query can match against the question
text and the answer text in our index.

Build one text per document:

```python
texts = []

for doc in documents:
    text = doc["question"] + " " + doc["answer"]
    texts.append(text)
```

Now we generate the embeddings. We have about 1200 texts here. We won't
hand the model all of them at once. That takes a long time, and we can't
see what's happening inside. Instead we split them into batches.

First we import `tqdm` so we can watch the progress:

```python
from tqdm.auto import tqdm
```

Next we chunk the dataset into batches of 50 and encode each batch:

```python
batch_size = 50
vectors = []

for i in tqdm(range(0, len(texts), batch_size)):
    batch = texts[i:i + batch_size]
    batch_vectors = model.encode(batch)
    vectors.extend(batch_vectors)

len(vectors)
```

We end up with 1208 vectors. On a GPU this is fast. Most of us run on
Codespaces without a GPU, so it takes a bit, but it's a one-off.

We turn them into a 2-dimensional array (matrix) where

- rows are documents (vectors)
- columns are dimensions of the vectors

```python
import numpy as np
X = np.array(vectors)
```

Calling `X.shape` returns (1208, 384) - number of documents vs number of dimensions.

[← Embeddings](02-embeddings.md) | [Vector Search →](04-vector-search.md)
