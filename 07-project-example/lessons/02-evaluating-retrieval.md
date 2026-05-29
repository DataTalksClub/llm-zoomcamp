# Evaluating Retrieval

<a href="https://www.youtube.com/watch?v=6ulnHtJPCWY&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/6ulnHtJPCWY">
</a>

Now that we have a dataset and a basic RAG flow, we need to
evaluate how well the retrieval works. We use the same approach
from module 04: generate ground truth data and measure Hit Rate
and MRR.

## Problem description and README

First, write a clear README that describes the problem, the data,
and how to run the project.

A good README should include:

- What the project does
- The dataset used
- How to install dependencies (`uv sync`)
- How to run the application
- How to run the Jupyter notebook

You can use ChatGPT to help draft the README. Give it your project
criteria, describe your dataset, and ask it to write a problem
description. Then edit the result to make it concise.

## Generating ground truth data

We need questions with known relevant documents.

We generate these
with an LLM, asking it to create questions for each exercise:

```python
prompt1_template = """
You are a fitness expert generating evaluation questions.
For the exercise below, generate 2 questions that a user might ask.
Return the result as a JSON array with objects containing 'id' and 'question' fields.

Exercise: {exercise_name}
Activity type: {type_of_activity}
Equipment: {type_of_equipment}
Body part: {body_part}
Muscle groups: {muscle_groups_activated}
Instructions: {instructions}
""".strip()

from tqdm.auto import tqdm
import json

df = pd.read_csv("data/data.csv")

results = []

for _, row in tqdm(df.iterrows(), total=len(df)):
    prompt = prompt1_template.format(**row.to_dict())
    response = openai_client.responses.create(
        model="gpt-5.4-mini",
        input=[{"role": "user", "content": prompt}]
    )
    questions = json.loads(response.output_text)
    for q in questions:
        q["id"] = row["id"]
        results.append(q)

df_questions = pd.DataFrame(results)
df_questions.to_csv("data/ground-truth-retrieval.csv", index=False)
```

Load the ground truth:

```python
df_question = pd.read_csv("data/ground-truth-retrieval.csv")
ground_truth = df_question.to_dict(orient="records")
```

## Evaluating retrieval quality

We use the same Hit Rate and MRR metrics from module 04:

```python
def hit_rate(relevance_total):
    cnt = 0
    for line in relevance_total:
        if True in line:
            cnt += 1
    return cnt / len(relevance_total)

def mrr(relevance_total):
    total_score = 0.0
    for line in relevance_total:
        for rank in range(len(line)):
            if line[rank]:
                total_score += 1 / (rank + 1)
                break
    return total_score / len(relevance_total)

def evaluate(ground_truth, search_function):
    relevance_total = []
    for q in tqdm(ground_truth):
        doc_id = q["id"]
        results = search_function(q)
        relevance = [d["id"] == doc_id for d in results]
        relevance_total.append(relevance)
    return {
        "hit_rate": hit_rate(relevance_total),
        "mrr": mrr(relevance_total)
    }
```

Evaluate the default search (no boosting):

```python
evaluate(ground_truth, lambda q: search(q["question"]))
```

## Finding the best boost parameters

We can optimize the boost values for each field using random
search.

Split the ground truth into validation and test sets:

```python
df_validation = df_question[:100]
df_test = df_question[100:]

gt_val = df_validation.to_dict(orient="records")
gt_test = df_test.to_dict(orient="records")
```

Define the search function with configurable boost:

```python
def minsearch_search(query, boost=None):
    if boost is None:
        boost = {}

    results = index.search(
        query=query,
        filter_dict={},
        boost_dict=boost,
        num_results=10
    )
    return results
```

Random search over boost values:

```python
import random

def simple_optimize(param_ranges, objective_function, n_iterations=10):
    best_params = None
    best_score = float("-inf")

    for _ in range(n_iterations):
        current_params = {}
        for field, (low, high) in param_ranges.items():
            current_params[field] = random.uniform(low, high)

        current_score = objective_function(current_params)

        if current_score > best_score:
            best_score = current_score
            best_params = current_params

    return best_params

param_ranges = {
    "exercise_name": (0.0, 3.0),
    "type_of_activity": (0.0, 3.0),
    "type_of_equipment": (0.0, 3.0),
    "body_part": (0.0, 3.0),
    "type": (0.0, 3.0),
    "muscle_groups_activated": (0.0, 3.0),
    "instructions": (0.0, 3.0),
}

def objective(boost_params):
    def search_function(q):
        return minsearch_search(q["question"], boost=boost_params)

    results = evaluate(gt_val, search_function)
    return results["hit_rate"]

best_params = simple_optimize(param_ranges, objective, n_iterations=20)
print("Best boost parameters:", best_params)
```

Now use these optimized boost values in the search:

```python
def search(query):
    boost = {
        "exercise_name": 2.11,
        "type_of_activity": 1.46,
        "type_of_equipment": 0.65,
        "body_part": 2.65,
        "type": 1.31,
        "muscle_groups_activated": 2.54,
        "instructions": 0.74
    }

    results = index.search(
        query=query,
        filter_dict={},
        boost_dict=boost,
        num_results=10
    )

    return results
```

Evaluate on the test set:

```python
evaluate(gt_test, lambda q: search(q["question"]))
```

The optimized boost values should give significantly better Hit
Rate and MRR than the default search.

[← End-to-End Project Example](01-intro.md) | [Evaluating RAG →](03-evaluating-rag.md)
