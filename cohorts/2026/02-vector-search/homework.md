## Homework: Vector Search

In this homework, we put what we learned in Module 2 into practice.

We'll first turn text into vectors, then search by similarity.
We'll also learn something new and see how to combine vector search with keyword search. We'll skip the RAG part and focus solely on search.

Like in homework 1, our knowledge base is the course lessons themselves.
Each module has a `lessons/` folder of numbered markdown
pages, and we pull them from GitHub. We use the same commit, `8c1834d`,
so everyone works with the exact same 72 pages.

> It's possible your answers won't match exactly. If so, select the closest one.

## Setup

In this homework we won't use the same approach for embedding as in the
module. That is, we won't use the sentence-transformers library. Instead,
we'll use the lightweight embedding approach with the ONNX `Embedder`.

Both approaches produce identical vectors, but the ONNX runtime is far
lighter. It needs no PyTorch and no CUDA, which makes the installation about
30x smaller and lets it run anywhere, including a basic Codespace. We
skimmed through it in the lesson and said we'd cover it in the homework -
so here we are.

We prepare the environment the same way as in the module's
[ONNX Runtime](../../../02-vector-search/lessons/09-onnx-embedder.md)
lesson.

Create a fresh project and install the dependencies:

```bash
mkdir llm-zoomcamp-hw2 && cd llm-zoomcamp-hw2
uv init --no-workspace
uv add onnxruntime tokenizers numpy tqdm minsearch gitsource
uv add --dev huggingface-hub jupyter
```

We also need two helper scripts from the `embed/` directory of the course
repo:

- [`download.py`](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/02-vector-search/embed/download.py)
(fetches an ONNX model from HuggingFace) and
- [`embedder.py`](https://github.com/DataTalksClub/llm-zoomcamp/blob/main/02-vector-search/embed/embedder.py) (the `Embedder` class with an `encode` interface)

Let's download them:

```bash
PREFIX=https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/02-vector-search/embed
wget $PREFIX/download.py
wget $PREFIX/embedder.py
```

By default `download.py` fetches `Xenova/all-MiniLM-L6-v2`, the ONNX
version of the `all-MiniLM-L6-v2` model from the lessons:

```bash
uv run python download.py
```

Now we're ready to do the homework.

## Q1. Embedding a query

Embed the following query:

> How does approximate nearest neighbor search work?

The embedder returns a vector of 384 numbers. What's the first value
(`v[0]`)?

* -0.31
* -0.02
* 0.12
* 0.44

## Loading the data

We pull the lesson pages from the course repository, the same way as in
homework 1. We pin to commit `8c1834d` so everyone works with the same
data.

```python
from gitsource import GithubRepositoryDataReader

reader = GithubRepositoryDataReader(
    repo_owner="DataTalksClub",
    repo_name="llm-zoomcamp",
    commit_id="8c1834d",
    allowed_extensions={"md"},
    filename_filter=lambda path: "/lessons/" in path,
)

documents = [file.parse() for file in reader.read()]
```

Each document is a dictionary with a `filename` and `content`, and there
are 72 pages.

## Q2. Cosine similarity

The embedder returns normalized vectors, so the dot product between two
of them is their cosine similarity.

Take the page `02-vector-search/lessons/07-sqlitesearch-vector.md`, embed
its `content`, and compute the cosine similarity with the query vector
from Q1. What do you get?

* 0.07
* 0.37
* 0.68
* 0.92

## Q3. Chunking and search by hand

A full page covers several topics, which waters down its embedding.

We chunk the pages the same way as in homework 1:

```python
from gitsource import chunk_documents
chunks = chunk_documents(documents, size=2000, step=1000)
```

We embed every chunk's `content` with `encode_batch`, stack the vectors
into a matrix `X`, and score the Q1 query against all chunks:

```python
scores = X.dot(v)
```

Which file does the highest-scoring chunk belong to (its `filename`)?

* `02-vector-search/lessons/03-embeddings-dataset.md`
* `02-vector-search/lessons/06-rag-vector.md`
* `02-vector-search/lessons/07-sqlitesearch-vector.md`
* `02-vector-search/lessons/09-onnx-embedder.md`

## Q4. Vector search with minsearch

We've done vector search by hand, which is good for learning, but it's not
what we do in practice. In practice we use libraries.

Let's use `VectorSearch` from minsearch and run a search for the following
query:

> What metric do we use to evaluate a search engine?

Which file is the `filename` of the first result?

* `02-vector-search/lessons/04-vector-search.md`
* `04-evaluation/lessons/05-search-metrics.md`
* `04-evaluation/lessons/13-llm-as-judge.md`
* `05-monitoring/lessons/04-metrics.md`

## Q5. Text search vs vector search

Vector search matches by meaning, keyword search by exact words.

Let's compare them. Index
the same chunks with `Index` from minsearch. Use `content` as a
text field.

Run both searches for this query:

> How do I store vectors in PostgreSQL?

Take the top 5 results from each method. Which file shows up in the
vector results but not in the text results?

* `02-vector-search/lessons/01-intro.md`
* `02-vector-search/lessons/02-embeddings.md`
* `02-vector-search/lessons/08-pgvector.md`
* `03-orchestration/lessons/05-rag.md`

## Q6. Hybrid search

Both vector and text search have their strengths and weaknesses. Vector
search matches by meaning, so it finds relevant pages even when they use
words different from the query. But it can miss exact terms like names,
codes, or rare keywords. Text search is the opposite: it nails exact words
but misses paraphrases and synonyms.

We don't have to pick one or the other - we can use both and merge their
results. This approach is called "hybrid search".

Each search produces its own ranked list, so we need a way to combine them
into one. In this homework we use Reciprocal Rank Fusion (RRF). It ignores
the raw scores from each method, which live on different scales and aren't
directly comparable. Instead, it looks only at the position of each
document in each list.

Every document scores by its position (`rank`, starting at 0) in each
list, and we sum the scores across lists with a constant `k = 60`:

```text
RRF(d) = sum over lists of  1 / (k + rank(d))
```

"Sum over lists" means we go through every ranked list and, for each list
where the document appears, add its `1 / (k + rank)` contribution. A
document found by both searches collects a score from each list, while one
found by only a single search collects just one.

The constant `k` controls how much the exact rank matters. A larger `k`
flattens the gap between positions, so the difference between rank 0 and
rank 5 counts for less. A smaller `k` does the opposite: it sharpens that
gap, so being at the top of a list matters much more.

The value 60 comes from the original RRF paper and is the usual default.
You rarely need to tune it. Lower it when only the top results matter.
Raise it to reward documents that appear across many lists, even when they
never quite reach the top.

A document that ranks well in both lists ends up higher than one that's
only strong in a single list.

```python
def rrf(result_lists, k=60, num_results=5):
    scores = {}
    docs = {}

    for results in result_lists:
        for rank, doc in enumerate(results):
            key = (doc["filename"], doc["start"])
            scores[key] = scores.get(key, 0) + 1 / (k + rank)
            docs[key] = doc

    ranked = sorted(scores, key=scores.get, reverse=True)
    return [docs[key] for key in ranked[:num_results]]
```

Now run the query `"How do I give the model access to tools?"`
with vector and text search and fuse the results with `rrf`:

```python
results = rrf([vector_results, text_results])
```

Which file is ranked first after RRF?

* `01-agentic-rag/lessons/01-intro.md`
* `01-agentic-rag/lessons/13-function-calling.md`
* `01-agentic-rag/lessons/14-agentic-loop.md`
* `01-agentic-rag/lessons/16-other-frameworks.md`

Notice that this file isn't first in either search on its own - it wins
because it ranks high in both.

## Selecting the best approach

By now you can search several ways:

- vector search
- keyword search
- hybrid search

Which is the best way? 

The right choice depends on your data, and the way to decide is to
measure.

We cover how to evaluate and compare search approaches in the
[evaluation module](../../../04-evaluation/lessons/04-search-evaluation.md),
and you'll do exactly that in the [evaluation homework](../04-evaluation/homework.md).

## Learning in Public

We encourage everyone to share what they learned. This is called "learning in public".

Read more about the benefits [here](https://alexeyondata.substack.com/p/benefits-of-learning-in-public-and) and in the [course's learning in public guide](https://datatalks.club/docs/courses/zoomcamp-logistics/learning-in-public/).

### Example post for LinkedIn

Tag [@Alexey Grigorev](https://www.linkedin.com/in/agrigorev/) and [@DataTalksClub](https://www.linkedin.com/company/datatalks-club/) in your post - we'll like and comment to give your post more reach.

```
🚀 Module 2 of LLM Zoomcamp by @DataTalksClub complete!

Just finished Module 2 - Vector Search. Learned how to:

✅ Turn text into embeddings with a lightweight ONNX model
✅ Build vector search from scratch with numpy
✅ Use minsearch for vector search, with chunking for long pages
✅ Compare keyword and vector search, and combine them with hybrid search (RRF)

Here's my homework solution: <LINK>

Following along with this amazing free course by @Alexey Grigorev - who else is learning to build with LLMs?

You can sign up here: https://github.com/DataTalksClub/llm-zoomcamp/
```

### Example post for X

```
🔍 Module 2 of LLM Zoomcamp done!

- Embeddings with a lightweight ONNX model
- Vector search from scratch with numpy
- minsearch + chunking
- Keyword vs vector, and hybrid search with RRF

My solution: <LINK>

Free course by @Al_Grigor & @DataTalksClub: https://github.com/DataTalksClub/llm-zoomcamp/
```

## Submit the results

* Submit your results here: https://courses.datatalks.club/llm-zoomcamp-2026/homework/hw2
* It's possible your answers won't match exactly. If so, select the closest one.
