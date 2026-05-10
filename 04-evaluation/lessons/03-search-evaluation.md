# Search Evaluation

Now that we have ground truth data, we can evaluate how well our search
retrieves the correct documents.

The idea is simple: for each question in our ground truth dataset, run
the search and check if the correct document shows up in the results.


## Setting up search

Let's set up our minsearch index the same way we did in module 03:

```python
from minsearch import Index

index = Index(
    text_fields=["question", "section", "answer"],
    keyword_fields=["course"]
)
index.fit(documents)

def search(query, course="data-engineering-zoomcamp"):
    boost_dict = {"question": 3.0, "section": 0.5}
    results = index.search(
        query,
        boost_dict=boost_dict,
        filter_dict={"course": course},
        num_results=5
    )
    return results
```


## Collecting relevance data

For each ground truth question, we run the search and check if the
correct document appears in the results:

```python
relevance_total = []

for q in tqdm(ground_truth_flat):
    doc_id = q['document']
    results = search(query=q['question'], course=q['course'])
    relevance = [d['id'] == doc_id for d in results]
    relevance_total.append(relevance)
```

Each entry in `relevance_total` is a list of booleans. For example:

```python
[True, False, False, False, False]
```

This means the correct document was at position 1. Or:

```python
[False, False, True, False, False]
```

The correct document was at position 3. Or:

```python
[False, False, False, False, False]
```

The correct document was not found at all.


## Hit Rate

Hit Rate (also called Recall@k) measures the fraction of queries where
the correct document appears anywhere in the results:

```python
def hit_rate(relevance_total):
    cnt = 0

    for line in relevance_total:
        if True in line:
            cnt = cnt + 1

    return cnt / len(relevance_total)
```

If the correct document is in the top 5 results, that's a hit. Hit Rate
is the percentage of queries that are hits.

Let's check with an example:

```python
example = [
    [True,  False, False, False, False],
    [False, False, False, False, False],
    [False, False, False, False, False],
    [False, False, False, False, False],
    [False, False, False, False, False],
    [True,  False, False, False, False],
    [True,  False, False, False, False],
    [True,  False, False, False, False],
    [True,  False, False, False, False],
    [True,  False, False, False, False],
    [False, False, True,  False, False],
    [False, False, False, False, False],
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
            if line[rank] == True:
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

We can wrap the evaluation in a reusable function:

```python
def evaluate(ground_truth, search_function):
    relevance_total = []

    for q in tqdm(ground_truth):
        doc_id = q['document']
        results = search_function(q)
        relevance = [d['id'] == doc_id for d in results]
        relevance_total.append(relevance)

    return {
        'hit_rate': hit_rate(relevance_total),
        'mrr': mrr(relevance_total),
    }
```

Now we can evaluate any search function:

```python
# Evaluate minsearch with default boost
evaluate(
    ground_truth_flat,
    lambda q: search(q['question'], q['course'])
)
```

You should see something like:

```python
{'hit_rate': 0.77, 'mrr': 0.66}
```

Now we can try different boost values and see what works best:

```python
def search_boost(query, course, question_boost):
    boost_dict = {"question": question_boost, "section": 0.5}
    return index.search(
        query,
        boost_dict=boost_dict,
        filter_dict={"course": course},
        num_results=5
    )

for boost in [1.0, 3.0, 5.0, 10.0]:
    result = evaluate(
        ground_truth_flat,
        lambda q: search_boost(q['question'], q['course'], boost)
    )
    print(f"boost={boost}: {result}")
```

This is how you tune search parameters. Instead of guessing, you measure.
The ground truth dataset gives you a reliable way to compare different
configurations.


[<< Previous: Generating Ground Truth](02-generating-ground-truth)
|
[Next: RAG Evaluation: Cosine Similarity >>](04-rag-evaluation-cosine)
