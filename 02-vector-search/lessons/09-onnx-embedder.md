# Using ONNX Runtime instead of PyTorch

When you move to production, you want to reduce overhead - both the
dependencies and the size of your deployment. sentence-transformers
depends on PyTorch, which is huge. We can use ONNX Runtime
instead: it's much smaller.

I created two separate projects: one with sentence-transformers and
one with ONNX Runtime. Then I measured the virtual environment sizes:

| | sentence-transformers | ONNX Runtime |
|---|---|---|
| Size | 4.8 GB | 147 MB |
| Packages | 58 | 27 |

That's 33x smaller. Same embeddings, same results.

For development and experimentation, sentence-transformers is fine.
But for production you want something more lightweight.

Let's create a separate project for this lesson:

```bash
mkdir llm-zoomcamp-onnx && cd llm-zoomcamp-onnx
uv init
uv add onnxruntime tokenizers numpy tqdm
uv add --dev huggingface-hub
```

`huggingface-hub` is only needed to download the model. At runtime we'll need `onnxruntime`, `tokenizers`, and `numpy`.


## Downloading the model

We'll use [download.py](../embed/download.py) to fetch the ONNX model from
HuggingFace. Download it:

```bash
wget https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/02-vector-search/embed/download.py
```

Now run:

```bash
uv run python download.py
```

This creates:

```
models/
  Xenova/
    all-MiniLM-L6-v2/
      tokenizer.json
      model.onnx
```

You only run this once. After that, the model files are local.

Add the models directory to `.gitignore`:

```
models/
```


## The Embedder class

We'll use [embedder.py](../embed/embedder.py) for generating embeddings.
Download it:

```bash
wget https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/02-vector-search/embed/embedder.py
```

Under the hood, it does four things:

1. Tokenize - convert text into integer IDs and attention masks
2. Run ONNX model - execute the model graph on CPU
3. Mean pooling - average the token embeddings, weighted by the
   attention mask
4. Normalize - divide by L2 norm so vectors can be compared with
   dot product


## Same pipeline, no PyTorch

Let's repeat the same examples from earlier. First, comparing queries
against a document:

```python
from embedder import Embedder

embed = Embedder()

q1 = "Can I still join the course after the start date?"
q2 = "How to install Docker on Windows?"
d  = "You don't need to register. You're accepted. You can also just start learning and submitting homework without registering."

v1 = embed.encode(q1)
v2 = embed.encode(q2)
dv = embed.encode(d)
```

Compute similarities:

```python
v1.dot(dv)
```

```python
v2.dot(dv)
```

Same result as before: the first score is higher because the query
about joining the course is more similar to the document about
registration.

Now let's embed our FAQ dataset. First, load the documents:

```python
import requests

docs_url = 'https://datatalks.club/faq/json/courses.json'
response = requests.get(docs_url)
courses_raw = response.json()

documents = []
url_prefix = 'https://datatalks.club/faq'

for course in courses_raw:
    course_url = f'{url_prefix}{course["path"]}'
    course_response = requests.get(course_url)
    course_data = course_response.json()

    for doc in course_data:
        doc['course_name'] = course['course_name']
        documents.append(doc)
```

Combine question and answer for each document:

```python
texts = [doc['question'] + ' ' + doc['answer'] for doc in documents]
```

Embed in batches:

```python
from tqdm import tqdm
import numpy as np

batch_size = 50
X = []

for i in tqdm(range(0, len(texts), batch_size)):
    batch = texts[i:i + batch_size]
    batch_vectors = embed.encode_batch(batch)
    X.extend(batch_vectors)

X = np.array(X)
```

And search:

```python
query = "Can I still join the course after the start date?"
v_query = embed.encode(query)

scores = X.dot(v_query)
idx = np.argmax(scores)

documents[idx]
```

Same results, same pipeline, but ~33x lighter.


## Available models

All of these work with the same code - just change the model name in
`download.py` and the path in `Embedder()`:

| Model | Dimensions | Notes |
|---|---|---|
| [`Xenova/all-MiniLM-L6-v2`](https://huggingface.co/Xenova/all-MiniLM-L6-v2) | 384 | Best small general-purpose |
| [`Xenova/all-MiniLM-L12-v2`](https://huggingface.co/Xenova/all-MiniLM-L12-v2) | 384 | Better quality, slower |
| [`Xenova/paraphrase-MiniLM-L6-v2`](https://huggingface.co/Xenova/paraphrase-MiniLM-L6-v2) | 384 | Paraphrase detection |
| [`Xenova/paraphrase-multilingual-MiniLM-L12-v2`](https://huggingface.co/Xenova/paraphrase-multilingual-MiniLM-L12-v2) | 384 | Multilingual |
| [`Xenova/multilingual-e5-small`](https://huggingface.co/Xenova/multilingual-e5-small) | 384 | Multilingual retrieval |
| [`Xenova/multilingual-e5-base`](https://huggingface.co/Xenova/multilingual-e5-base) | 768 | Stronger multilingual |
| [`Xenova/bge-small-en-v1.5`](https://huggingface.co/Xenova/bge-small-en-v1.5) | 384 | Very strong retrieval |
| [`Xenova/bge-base-en-v1.5`](https://huggingface.co/Xenova/bge-base-en-v1.5) | 768 | Stronger retrieval |
| [`Xenova/gte-small`](https://huggingface.co/Xenova/gte-small) | 384 | Lightweight modern model |
| [`Xenova/gte-base`](https://huggingface.co/Xenova/gte-base) | 768 | Stronger GTE |

To use a different model, add it to `download.py`, run the download,
then update the path:

```python
embed = Embedder("models/Xenova/bge-base-en-v1.5")
vectors = embed.encode("your text here")
print(vectors.shape)
```

Since the runtime only depends on `onnxruntime`, `tokenizers`, and
`numpy`, you can deploy this in minimal environments: small Docker
images, serverless functions, or edge devices.

[<- Hybrid Search](08-hybrid-search.md) | [Back to module ->](../)
