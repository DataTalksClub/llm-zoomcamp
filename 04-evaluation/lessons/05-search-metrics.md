# Search Evaluation Metrics

In the previous lesson, we computed relevance lists for search results.
We can turn those lists into metrics.

## Hit Rate

Hit Rate (also called Recall@k) measures the fraction of queries where
the correct document appears anywhere in the results:

```python
example = [
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0],
]
```

Each line is one query. If a line contains `1`, search found the
correct document somewhere in the top 5 results. If the line contains
only zeros, search did not find the correct document.

In our setup, each query has one correct document, so Hit Rate and
Recall@k mean the same thing.

Let's calculate it:

```python
cnt = 0

for line in example:
    if 1 in line:
        cnt = cnt + 1

cnt
```

There are 14 hits. The example has 15 queries.

The Hit Rate is:

```python
cnt / len(example)
# 0.933
```

This means that search found the correct document for 93.3% of the
queries in this example.

Put the same logic into a function:

```python
def hit_rate(relevance):
    cnt = 0

    for line in relevance:
        if 1 in line:
            cnt = cnt + 1

    return cnt / len(relevance)
```

Check it on the same example:

```python
hit_rate(example)
# 0.933
```

## Mean Reciprocal Rank (MRR)

Hit Rate tells us if we found the right document, but not where it was.

MRR also considers the position.

For each query, the score is based on the rank of the first correct
document:

- position 1: score is 1.0
- position 2: score is 0.5
- position 3: score is 0.333
- not found: score is 0

In the example, most hits are at the first position. Some hits are at
the second position.

Look at that line:

```python
example[8]
# [0, 1, 0, 0, 0]
```

For this line, the score is `1/2` because the correct document is at
position 2.

Let's calculate MRR:

```python
total_score = 0.0

for line in example:
    for rank in range(len(line)):
        if line[rank] == 1:
            total_score = total_score + 1 / (rank + 1)
            break

total_score
```

The total score is `12.5`.

Divide it by the number of queries:

```python
total_score / len(example)
# 0.833
```

MRR is the average of these scores across all queries. It rewards
systems that put the correct document near the top.

Hit Rate is the upper bound for MRR. In practice, MRR is usually
smaller because some correct documents are found below the first
position.

Put the same logic into a function:

```python
def mrr(relevance):
    total_score = 0.0

    for line in relevance:
        for rank in range(len(line)):
            if line[rank] == 1:
                total_score = total_score + 1 / (rank + 1)
                break

    return total_score / len(relevance)
```

Check it on the same example:

```python
mrr(example)
# 0.833
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
{"hit_rate": 0.886, "mrr": 0.771}
```

Search metrics tell us whether retrieval works. Next, we'll use these
metrics to tune the search parameters.

[← Search Evaluation](04-search-evaluation.md) | [Search Parameter Tuning →](06-search-tuning.md)
