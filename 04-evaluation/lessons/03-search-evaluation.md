# Search Evaluation

Now that we have ground truth data, we can evaluate how well our search
retrieves the correct documents.

For each question in our ground truth dataset, we run search. Then we
check whether the results include the correct document.

## Setting up search

Create a new notebook for search evaluation. We'll use the ground truth
CSV from the previous lesson and set up the search index here.

If you don't have `pandas` and `tqdm` installed yet, add them first:

```bash
uv add pandas tqdm
```

For search evaluation, we only need the search part of the RAG
pipeline. We don't need to call the LLM yet.

Load the ground truth file from the previous notebook:

```python
import pandas as pd

df_ground_truth = pd.read_csv("data/ground-truth-data.csv")
ground_truth = df_ground_truth.to_dict(orient="records")
```

Use the same `ingest.py` file we downloaded in the previous notebook.

Load the documents and build a minsearch index:

```python
from ingest import load_faq_data, build_index

documents = load_faq_data()
index = build_index(documents)
```

Wrap the search call in a function called `text_search`. Later, we can
compare it with other search functions.

```python
def text_search(query):
    boost_dict = {"question": 3.0, "section": 0.5}
    filter_dict = {"course": "llm-zoomcamp"}

    return index.search(
        query,
        num_results=5,
        boost_dict=boost_dict,
        filter_dict=filter_dict,
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
    print(d["id"], doc_id, d["id"] == doc_id)
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
q["question"]
# 'Can I take this course at my own pace and still receive a certificate at the end?'
```

Compute relevance for it:

```python
compute_relevance_text(q)
# [1, 0, 0, 0, 0]
```

The correct document was the first search result.

Here are two more examples from the generated ground truth data.

For this question:

```python
q = ground_truth[11]
q["question"]
# 'If I sign up late, what do I need to do in order to still earn the course certificate?'

compute_relevance_text(q)
# [0, 0, 1, 0, 0]
```

Here, the first two retrieved documents are not correct. The third
retrieved document has the same ID as the ground truth document, so the
`1` is in position 3.

For this question:

```python
q = ground_truth[12]
q["question"]
# 'Is it okay to start the course after it has already begun, or is there a deadline for joining?'

compute_relevance_text(q)
# [0, 0, 0, 0, 0]
```

The correct document was not found at all.

Now do the same thing for all ground truth questions:

```python
from tqdm.auto import tqdm

def compute_relevance_total(ground_truth):
    relevance_total = []

    for q in tqdm(ground_truth):
        relevance = compute_relevance_text(q)
        relevance_total.append(relevance)

    return relevance_total
```

Call it for the ground truth dataset:

```python
relevance_total = compute_relevance_total(ground_truth)
```

Each entry in `relevance_total` is a relevance list.

## Hit Rate

Hit Rate (also called Recall@k) measures the fraction of queries where
the correct document appears anywhere in the results:

```python
def hit_rate(relevance_total):
    cnt = 0

    for line in relevance_total:
        if 1 in line:
            cnt = cnt + 1

    return cnt / len(relevance_total)
```

If the correct document is in the top 5 results, that's a hit. Hit Rate
is the percentage of queries that are hits.

Let's check with an example:

```python
example = [
    [1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
]

hit_rate(example)
# 0.5833
```

7 out of 12 queries found the correct document somewhere in the results.

## Mean Reciprocal Rank (MRR)

Hit Rate tells us if we found the right document, but not where it was.

MRR also considers the position:

```python
def mrr(relevance_total):
    total_score = 0.0

    for line in relevance_total:
        for rank in range(len(line)):
            if line[rank] == 1:
                total_score = total_score + 1 / (rank + 1)

    return total_score / len(relevance_total)
```

For each query, the score is `1/rank` where rank is the position of the
first correct document. If the correct document is at position 1, the
score is 1.0. At position 2, it's 0.5. At position 3, it's 0.333. If
not found, the score is 0.

MRR is the average of these scores across all queries. It rewards
systems that put the correct document near the top.

```python
mrr(example)
# 0.5278
```

## Putting it together

Next, make the relevance functions generic, so they can use any search
function:

```python
def compute_relevance(q, search_function):
    doc_id = q["document"]
    results = search_function(q["question"])

    relevance = []
    for d in results:
        relevance.append(int(d["id"] == doc_id))

    return relevance
```

The total relevance function gets a `search_function` too:

```python
def compute_relevance_total(ground_truth, search_function):
    relevance_total = []

    for q in tqdm(ground_truth):
        relevance = compute_relevance(q, search_function)
        relevance_total.append(relevance)

    return relevance_total
```

Then wrap the metrics in a reusable evaluation function:

```python
def evaluate(ground_truth, search_function):
    relevance_total = compute_relevance_total(ground_truth, search_function)

    return {
        "hit_rate": hit_rate(relevance_total),
        "mrr": mrr(relevance_total),
    }
```

We can evaluate any search function:

```python
evaluate(
    ground_truth,
    text_search
)
```

You should see something like:

```python
{"hit_rate": 0.77, "mrr": 0.66}
```

Try different boost values to see what works best:

```python
def search_boost(query, question_boost):
    boost_dict = {"question": question_boost, "section": 0.5}
    filter_dict = {"course": "llm-zoomcamp"}

    return index.search(
        query,
        num_results=5,
        boost_dict=boost_dict,
        filter_dict=filter_dict,
    )

for boost in [1.0, 3.0, 5.0, 10.0]:
    result = evaluate(
        ground_truth,
        lambda q: search_boost(q["question"], boost)
    )
    print(f"boost={boost}: {result}")
```

This is how you tune search parameters. Instead of guessing, you measure.
The ground truth dataset gives you a reliable way to compare different
configurations.

[← Generating Ground Truth Data](02-generating-ground-truth.md) | [RAG Evaluation: Cosine Similarity →](04-rag-evaluation-cosine.md)
