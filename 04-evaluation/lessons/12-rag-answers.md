# Generating RAG Answers

In the first part of this module, we evaluated search quality. We
checked whether the right document appeared in the search results.

Now we evaluate the full RAG pipeline. For each generated question, we
run RAG and save the answer produced by the LLM. Later, we'll compare
this answer with the original FAQ answer.

This is the A->Q->A' setup:

- A = original answer in the FAQ
- Q = generated question from this answer
- A' = answer produced by our RAG system

If A' is close to A, the RAG system is doing a good job.

This is still offline evaluation. We can compare A and A' because our
questions came from FAQ records. For each question, we know which
original answer it came from.

## Loading the data

Create a new notebook for RAG evaluation.

Load the ground truth questions:

```python
import pandas as pd

df_ground_truth = pd.read_csv("data/ground-truth-data.csv")
ground_truth = df_ground_truth.to_dict(orient="records")
```

Load the FAQ documents and the search index:

```python
from ingest import load_faq_data, build_index

documents = load_faq_data()
index = build_index(documents)
```

Create a lookup table for the original FAQ documents:

```python
doc_idx = {}

for doc in documents:
    doc_idx[doc["id"]] = doc
```

We'll use this lookup table to find the original answer for each
ground truth question.

## Running RAG

Use the same `RAGBase` helper from module 01:

```python
from dotenv import load_dotenv
from openai import OpenAI
from rag_helper import RAGBase

load_dotenv()
openai_client = OpenAI()

assistant = RAGBase(
    index=index,
    llm_client=openai_client,
)
```

For each question, `RAGBase` searches the FAQ, builds a prompt with the
retrieved context, and asks the LLM to answer. We save the answer so the
next lesson can judge it.

Run RAG for one question:

```python
rec = ground_truth[0]
question = rec["question"]

answer_llm = assistant.rag(question)
answer_llm
```

The `rag` method returns the answer, but it doesn't return token usage.

For this notebook, use a small wrapper that returns both:

```python
def rag_with_usage(question):
    search_results = assistant.search(question)
    prompt = assistant.build_prompt(question, search_results)

    messages = [
        {"role": "developer", "content": assistant.instructions},
        {"role": "user", "content": prompt}
    ]

    response = openai_client.responses.create(
        model=assistant.model,
        input=messages
    )

    return response.output_text, response.usage
```

Test it:

```python
answer_llm, usage = rag_with_usage(question)

answer_llm
```

Get the original answer from the document ID:

```python
doc_id = rec["document"]
original_doc = doc_idx[doc_id]
answer_orig = original_doc["answer"]

answer_orig
```

Now save both answers in one record:

```python
rag_result = {
    "question": question,
    "answer_llm": answer_llm,
    "answer_orig": answer_orig,
    "document": doc_id,
}

rag_result
```

Calculate the price from `response.usage`, using the helper from the
ground truth generation notebook.

Import it:

```python
from evaluation_utils import calc_price
```

Check the cost of one call:

```python
calc_price(usage)
```

## Processing all questions

Create a function that processes one ground truth record:

```python
def generate_rag_answer(rec):
    question = rec["question"]
    doc_id = rec["document"]
    original_doc = doc_idx[doc_id]

    answer_llm, usage = rag_with_usage(question)
    answer_orig = original_doc["answer"]

    result = {
        "question": question,
        "answer_llm": answer_llm,
        "answer_orig": answer_orig,
        "document": doc_id,
    }

    return result, usage
```

Test it on one record:

```python
answer_record, usage = generate_rag_answer(ground_truth[0])

answer_record
```

And check the cost:

```python
calc_price(usage)
```

This calls the LLM once per ground truth question, so it can take some
time. Let's process the questions in parallel and track progress.

Import the parallel processing helper from the same utility file:

```python
from concurrent.futures import ThreadPoolExecutor
from evaluation_utils import map_progress
```

Run RAG for all ground truth questions:

```python
with ThreadPoolExecutor(max_workers=6) as pool:
    results = map_progress(pool, ground_truth, generate_rag_answer)
```

`generate_rag_answer` returns two things for each question: the answer
record and the token usage.

Split those into separate lists:

```python
answers = []
usages = []

for answer_record, usage in results:
    answers.append(answer_record)
    usages.append(usage)
```

Calculate the total cost:

```python
total_cost = 0.0

for usage in usages:
    cost = calc_price(usage)
    total_cost = total_cost + cost["total_cost"]

total_cost
```

Save the answers:

```python
df_answers = pd.DataFrame(answers)
df_answers.to_csv("data/rag-answers.csv", index=False)
```

We generated this file for the course materials on May 28, 2026. The
run used 395 ground truth questions.

The token usage was:

- Input tokens: 282,544
- Output tokens: 24,339
- Estimated cost with the prices above: $0.321433, about 32 cents

If you don't want to generate the RAG answers yourself, download the
file we prepared:

```bash
wget -O data/rag-answers.csv https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/04-evaluation/data/rag-answers.csv
```

In the next lesson, we'll evaluate these answers with an LLM judge.

[← RAG and Agent Evaluation](11-evaluation-intro.md) | [LLM as a Judge →](13-llm-as-judge.md)
