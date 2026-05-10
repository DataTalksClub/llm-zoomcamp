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
and how to run the project. A good README should include:

- What the project does
- The dataset used
- How to install dependencies
- How to run the application

You can use ChatGPT to help draft the README. Give it your project
criteria, describe your dataset, and ask it to write a problem
description. Then edit the result to make it concise.


## Generating ground truth data

We need questions with known relevant documents to evaluate
retrieval. We generate these with an LLM:

```python
from openai import OpenAI
import json

openai_client = OpenAI()

def generate_questions(doc):
    prompt = f"""
    You are a fitness expert. Generate 2-3 questions that a user might ask
    about this exercise. The questions should be answerable from the
    exercise information provided.

    Exercise: {doc['exercise']}
    Muscle group: {doc['muscle_group']}
    Equipment: {doc['equipment']}
    Instructions: {doc['instructions']}
    """.strip()

    response = openai_client.responses.create(
        model="gpt-5.4-mini",
        input=[{"role": "user", "content": prompt}]
    )
    return response.output_text
```

Run this for all documents and save the results as ground truth data.


## Evaluating retrieval quality

With ground truth data, we can measure retrieval quality:

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
        'mrr': mrr(relevance_total)
    }
```

Then experiment with different boost coefficients to find the best
configuration:

```python
def search(query, boost_dict, course):
    results = index.search(
        query=query,
        boost_dict=boost_dict,
        filter_dict={"course": course},
        num_results=5
    )
    return results
```

Try different boost values for the question, text, and section
fields. The configuration with the highest Hit Rate and MRR wins.


[<< Previous: Intro](01-intro)
|
[Next: Evaluating RAG >>](03-evaluating-rag)
