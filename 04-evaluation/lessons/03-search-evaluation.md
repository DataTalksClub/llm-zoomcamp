# Search Evaluation

Now that we have ground truth data, we can evaluate how well our search
retrieves the correct documents.

For each question in our ground truth dataset, run the search and check
if the correct document shows up in the results.

## Setting up search

Let's set up our search using `RAGBase` from module 01:

```python
from rag_helper import RAGBase, load_faq_data
from minsearch import Index
from openai import OpenAI

documents = load_faq_data()

index = Index(
    text_fields=['question', 'section', 'answer'],
    keyword_fields=['course']
)
index.fit(documents)

openai_client = OpenAI()

instructions = """
You're a course teaching assistant.
Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.
""".strip()

assistant = RAGBase(
    index=index,
    llm_client=openai_client,
    instructions=instructions,
)
```

We'll use `assistant.search` to evaluate different boost configurations.

The default search function for evaluation:

```python
def search_fn(query, course):
    return assistant.search(
        query,
        boost_dict={'question': 3.0, 'section': 0.5},
        filter_dict={'course': course},
    )
```

## Collecting relevance data

For each ground truth question, we run the search and check if the
correct document appears in the results:

```python
relevance_total = []

for q in tqdm(ground_truth_flat):
    doc_id = q['document']
    results = search_fn(query=q['question'], course=q['course'])
    relevance = [d['id'] == doc_id for d in results]
    relevance_total.append(relevance)
```

Each entry in `relevance_total` is a list of booleans.

For example:

```python
[True, False, False, False, False]
```

This means the correct document was at position 1.

Or:

```python
[False, False, True, False, False]
```

The correct document was at position 3.

Or:

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
evaluate(
    ground_truth_flat,
    lambda q: search_fn(q['question'], q['course'])
)
```

You should see something like:

```python
{'hit_rate': 0.77, 'mrr': 0.66}
```

Try different boost values to see what works best:

```python
def search_boost(query, course, question_boost):
    return assistant.search(
        query,
        boost_dict={'question': question_boost, 'section': 0.5},
        filter_dict={'course': course},
    )

for boost in [1.0, 3.0, 5.0, 10.0]:
    result = evaluate(
        ground_truth_flat,
        lambda q: search_boost(q['question'], q['course'], boost)
    )
    print(f'boost={boost}: {result}')
```

This is how you tune search parameters. Instead of guessing, you measure.
The ground truth dataset gives you a reliable way to compare different
configurations.

[← Generating Ground Truth Data](02-generating-ground-truth.md) | [RAG Evaluation: Cosine Similarity →](04-rag-evaluation-cosine.md)
