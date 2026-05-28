# Search Evaluation Metrics

In the previous lesson, we computed relevance lists for search results.
Now we can turn those lists into metrics.

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

Wrap the metrics in a reusable evaluation function:

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

Search metrics tell us whether retrieval works. Next, we'll evaluate
the answers produced by RAG and agent systems.

[← Search Evaluation](04-search-evaluation.md) | [RAG and Agent Evaluation →](11-evaluation-intro.md)
