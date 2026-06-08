# Using ONNX Runtime instead of PyTorch

Video: [Watch this lesson](https://www.youtube.com/watch?v=BMqa4OsCk58&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

When you move to production, you want to cut overhead, both the
dependencies and the size of your deployment. sentence-transformers
drags in PyTorch plus a pile of Nvidia libraries, which is a lot. ONNX
Runtime serves the same model without that weight.

To put a number on it, I created two empty projects. In one I ran `uv
add sentence-transformers`, in the other I set up ONNX Runtime.

Then I measured the virtual environment sizes:

- sentence-transformers: 4.8 GB, 58 packages
- ONNX Runtime: 147 MB, 27 packages

That's 33x smaller for the same embeddings and the same results. Often
we don't even convert the model ourselves. Someone has usually published
an ONNX version we can download.

For development and experiments, sentence-transformers is fine. For
production you want the lighter option.

Let's create a separate project for this lesson:

```bash
mkdir llm-zoomcamp-onnx && cd llm-zoomcamp-onnx
uv init --no-workspace
uv add onnxruntime tokenizers numpy tqdm minsearch
uv add --dev huggingface-hub jupyter
```


`huggingface-hub` is only needed to download the model. At runtime we'll need `onnxruntime`, `tokenizers`, and `numpy`.

Then register a kernel for this project:

```bash
uv run python -m ipykernel install --user --name llm-zoomcamp-onnx --display-name "llm-zoomcamp-onnx"
```


## Downloading the model

We'll use the [download.py](../embed/download.py) script from the
`embed/` directory to fetch the ONNX model from HuggingFace.

Copy it to your project, then run:

```bash
uv run python download.py
```

This creates:

```text
models/
  Xenova/
    all-MiniLM-L6-v2/
      tokenizer.json
      model.onnx
```

You only run this once. After that, the model files are local.

Add the models directory to `.gitignore`:

```text
models/
```

## The Embedder class

We'll use the [embedder.py](../embed/embedder.py) script from the
`embed/` directory for generating embeddings.

Copy it to your project as well.

Under the hood, it does four things:

1. Tokenize - convert text into integer IDs and attention masks
2. Run ONNX model - execute the model graph on CPU
3. Mean pooling - average the token embeddings, weighted by the
   attention mask
4. Normalize - divide by L2 norm so vectors can be compared with
   dot product

You don't need to follow every step inside `embedder.py`. It gives us
the same `encode` interface as before, with none of the PyTorch weight.

## Same pipeline, no PyTorch

Let's repeat the examples from earlier and confirm the numbers match.

First, comparing two queries against a document:

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

And the second similarity:

```python
v2.dot(dv)
```

We get the same result as before. The first score is higher because
the query about joining the course is more similar to the document
about registration.

Next, we embed the FAQ dataset.

If you didn't fetch `ingest.py` earlier, grab it now:

```bash
wget https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/01-agentic-rag/code/ingest.py
```

Load the documents:

```python
from ingest import load_faq_data

documents = load_faq_data()
```

Combine question and answer for each document:

```python
texts = [doc["question"] + " " + doc["answer"] for doc in documents]
```

Embed in batches:

```python
from tqdm.auto import tqdm
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

- [Xenova/all-MiniLM-L6-v2](https://huggingface.co/Xenova/all-MiniLM-L6-v2) (384d) - best small general-purpose
- [Xenova/all-MiniLM-L12-v2](https://huggingface.co/Xenova/all-MiniLM-L12-v2) (384d) - better quality, slower
- [Xenova/paraphrase-MiniLM-L6-v2](https://huggingface.co/Xenova/paraphrase-MiniLM-L6-v2) (384d) - paraphrase detection
- [Xenova/paraphrase-multilingual-MiniLM-L12-v2](https://huggingface.co/Xenova/paraphrase-multilingual-MiniLM-L12-v2) (384d) - multilingual
- [Xenova/multilingual-e5-small](https://huggingface.co/Xenova/multilingual-e5-small) (384d) - multilingual retrieval
- [Xenova/multilingual-e5-base](https://huggingface.co/Xenova/multilingual-e5-base) (768d) - stronger multilingual
- [Xenova/bge-small-en-v1.5](https://huggingface.co/Xenova/bge-small-en-v1.5) (384d) - strong retrieval
- [Xenova/bge-base-en-v1.5](https://huggingface.co/Xenova/bge-base-en-v1.5) (768d) - stronger retrieval
- [Xenova/gte-small](https://huggingface.co/Xenova/gte-small) (384d) - lightweight modern model
- [Xenova/gte-base](https://huggingface.co/Xenova/gte-base) (768d) - stronger GTE

To use a different model, add it to `download.py`, run the download,
then update the path:

```python
embed = Embedder("models/Xenova/bge-base-en-v1.5")
vectors = embed.encode("your text here")
print(vectors.shape)
```

Since the runtime only depends on `onnxruntime`, `tokenizers`, and
`numpy`, you can deploy this in minimal environments:

- small Docker images
- serverless functions
- edge devices

[← Vector Search with PGVector](08-pgvector.md) | [Next Steps →](10-next-steps.md)
