# Embedding Our Dataset

In the previous lesson, we saw how embeddings work with simple examples.
In this lesson we apply them to the entire FAQ dataset.

## Loading the data

In the previous module, we created a helper script for downloading the
data ([ingest.py](../../01-intro/code/ingest.py)).

If you don't have it from the previous lesson, let's download it:

```bash
wget https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/01-intro/code/ingest.py
```

We can use it:

```python
from ingest import load_faq_data

documents = load_faq_data()
```

## Generating embeddings

For vector search, we want to embed a combination of the question and
the answer.

This way, when a user asks a question, we can match it
against both the questions and answers in our index:

```python
texts = []

for doc in documents:
    text = doc['question'] + ' ' + doc['answer']
    texts.append(text)
```

Now generate the embeddings. We'll do it in batches.

First we'll import `tqdm` - we'll need it to see the progress.

```python
from tqdm.auto import tqdm
```

Next, chunk the dataset into batches of 50 and encode the vectors:

```python
batch_size = 50
vectors = []

for i in tqdm(range(0, len(texts), batch_size)):
    batch = texts[i:i + batch_size]
    batch_vectors = model.encode(batch)
    vectors.extend(batch_vectors)

len(vectors)
```

We end up with 1208 vectors.

We turn them into a 2-dimensional array (matrix) where

- rows are documents (vectors)
- columns are dimenstions of the vectors

```python
import numpy as np
X = np.array(vectors)
```

This matrix `X` has shape (1208, 384) - number of documents vs number of dimensions.

[← Embeddings](02-embeddings.md) | [Vector Search →](04-vector-search.md)
