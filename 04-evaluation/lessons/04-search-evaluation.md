# Search Evaluation

Video: [Watch this lesson](https://www.youtube.com/watch?v=KoyYkv8P_jU&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

Now that we have ground truth data, we can evaluate how well our search
retrieves the correct documents.

For each question in our ground truth dataset, we run search. Then we
check whether the results include the correct document.

## Setting up search

Create a new notebook for search evaluation. We'll use the ground truth
CSV from the previous lesson and set up the search index here.

For search evaluation, we only need the search part of the RAG
pipeline. We don't need to call the LLM yet.

Load the ground truth file from the previous notebook:

```python
import pandas as pd

df_ground_truth = pd.read_csv("data/ground_truth-new.csv")
ground_truth = df_ground_truth.to_dict(orient="records")
```

Use the same `ingest.py` file we downloaded in the previous notebook.

Load the documents and build a minsearch index:

```python
from ingest import load_faq_data, build_index

documents = load_faq_data()

documents_llm = []

for doc in documents:
    if doc["course"] == "llm-zoomcamp":
        documents_llm.append(doc)

documents = documents_llm
index = build_index(documents)
```

Wrap the search call in a function called `text_search`. The name is
deliberate. Later we'll write `vector_search` or a hybrid version and
run the exact same evaluation on it. Everything downstream only needs a
function that takes a query and returns results, so we can swap one for
another. That mirrors how RAG works: the retrieval step doesn't care
which search function sits behind it.

```python
def text_search(query):
    boost_dict = {"question": 3.0, "section": 0.5}

    return index.search(
        query,
        num_results=5,
        boost_dict=boost_dict
    )
```

## Collecting relevance data

Start with one ground truth record:

```python
q = ground_truth[0]
q
```

Run search for this question:

```python
doc_id = q["document"]
results = text_search(query=q["question"])
```

First, compare the retrieved document IDs with the correct document ID:

```python
for d in results:
    print(f'{d["id"]} == {doc_id}: {d["id"] == doc_id}')
```

Then turn this comparison into a relevance list. In this lesson,
relevance means whether a retrieved document is the correct document
for this question.

```python
relevance = []

for d in results:
    relevance.append(int(d["id"] == doc_id))

relevance
```

This gives a list of `0` and `1` values. `1` means the retrieved
document has the same ID as the correct document.

Put this logic into a function:

```python
def compute_relevance_text(q):
    doc_id = q["document"]
    results = text_search(query=q["question"])

    relevance = []
    for d in results:
        relevance.append(int(d["id"] == doc_id))

    return relevance
```

For the first ground truth record, the relevance list is:

```python
q = ground_truth[0]
print(q["question"])
compute_relevance_text(q)
# [1, 0, 0, 0, 0]
```

The correct document was the first search result.

Here are two more examples from the generated ground truth data.

For this question:

```python
q = ground_truth[11]
print(q["question"])
compute_relevance_text(q)
# [1, 0, 0, 0, 0]
```

Here, the correct document was also the first search result.

For this question:

```python
q = ground_truth[50]
print(q["question"])
compute_relevance_text(q)
# [1, 0, 0, 0, 0]
```

The correct document was found at the first position again.

Now do the same thing for all ground truth questions:

```python
from tqdm.auto import tqdm

def compute_relevance_total_text(ground_truth):
    relevance_total = []

    for q in tqdm(ground_truth):
        relevance = compute_relevance_text(q)
        relevance_total.append(relevance)

    return relevance_total
```

Call it for the first 15 ground truth questions:

```python
ground_truth_sample = ground_truth[:15]
relevance_total_text = compute_relevance_total_text(ground_truth_sample)
```

Look at the results:

```python
relevance_total_text
```

For the data we prepared on May 29, 2026, this gives:

```python
[
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
]
```

Each entry in `relevance_total_text` is a relevance list. This is
enough to check that the function works before we run it for the full
dataset.

Next, make the relevance functions generic. We start with text search,
but later we may want to evaluate vector search, hybrid search, or
another retrieval method. The relevance logic is the same. Only the
search function changes.

```python
def compute_relevance(q, search_function):
    doc_id = q["document"]
    results = search_function(query=q["question"])

    relevance = []
    for d in results:
        relevance.append(int(d["id"] == doc_id))

    return relevance
```

The total relevance function gets a `search_function` too.

We need to provide it explicitly:

```python
def compute_relevance_total(ground_truth, search_function):
    relevance_total = []

    for q in tqdm(ground_truth):
        relevance = compute_relevance(q, search_function)
        relevance_total.append(relevance)

    return relevance_total
```

Use it with `text_search` on the same sample:

```python
relevance_total = compute_relevance_total(ground_truth_sample, text_search)
relevance_total
```

Now run it for all ground truth questions:

```python
relevance_total = compute_relevance_total(ground_truth, text_search)
```

Now we can represent search results as relevance lists. In the next
lesson, we'll turn these lists into metrics: Hit Rate and MRR.

[← Generating Ground Truth for All Documents](03-ground-truth-batch.md) | [Search Evaluation Metrics →](05-search-metrics.md)
