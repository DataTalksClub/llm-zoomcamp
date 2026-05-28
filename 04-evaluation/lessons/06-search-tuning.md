# Search Parameter Tuning

In the previous lesson, we defined Hit Rate, MRR, and the `evaluate`
function. Now we can use them to tune search parameters.

Instead of guessing which settings are better, we measure them on the
ground truth dataset.

This is the main benefit of offline evaluation. We can change one
parameter, run the same questions again, and see whether the metric
improves. The dataset stays fixed, so the comparison is fair.

## Trying different boosts

Start with a search function where the question boost is configurable:

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
```

Evaluate several boost values:

```python
for boost in [1.0, 3.0, 5.0, 10.0]:
    result = evaluate(
        ground_truth,
        lambda q: search_boost(q["question"], boost)
    )
    print(f"boost={boost}: {result}")
```

Compare the printed Hit Rate and MRR values. The best setting is the
one that gives the strongest metrics on the ground truth data.

Usually we care about both metrics. Hit Rate tells us whether the
correct document appears at all. MRR tells us whether it appears near
the top. A document near the top is more likely to be used by the RAG
prompt.

## Tuning Workflow

Search parameters can look arbitrary. This includes field boosts,
number of results, filters, and other settings. Evaluation gives us a
way to compare settings with evidence.

The same pattern works for other search changes:

- different field boosts
- different `num_results` values
- text search vs vector search
- hybrid search

Each time, define a search function and pass it to `evaluate`.

Next, we'll move from retrieval quality to answer quality and evaluate
the full RAG pipeline.

[← Search Evaluation Metrics](05-search-metrics.md) | [RAG and Agent Evaluation →](11-evaluation-intro.md)
