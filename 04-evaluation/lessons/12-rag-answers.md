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

Download the helper files:

```bash
PREFIX=https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main

wget ${PREFIX}/01-agentic-rag/code/ingest.py
wget ${PREFIX}/01-agentic-rag/code/rag_helper.py
wget ${PREFIX}/04-evaluation/code/evaluation_utils.py
```

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

documents_llm = []

for doc in documents:
    if doc["course"] == "llm-zoomcamp":
        documents_llm.append(doc)

documents = documents_llm
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

Import the usual things first:

```python
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_client = OpenAI()
```

For this lesson, use `RAGWithUsage` from the evaluation utilities. It
subclasses `RAGBase` from module 01, so it has the same `rag` method.

It stores token usage after each LLM call. Then we can calculate the
total cost later.

```python
from evaluation_utils import RAGWithUsage

assistant = RAGWithUsage(
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

`RAGWithUsage` is a small subclass of `RAGBase`. It works the same way,
but it also stores token usage after each LLM call.

Check the cost of this call:

```python
assistant.total_cost()
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

## Processing all questions

Create a function that processes one ground truth record:

```python
def generate_rag_answer(rec):
    question = rec["question"]
    doc_id = rec["document"]
    original_doc = doc_idx[doc_id]

    answer_llm = assistant.rag(question)
    answer_orig = original_doc["answer"]

    result = {
        "question": question,
        "answer_llm": answer_llm,
        "answer_orig": answer_orig,
        "document": doc_id,
    }

    return result
```

Test it on one record:

```python
answer_record = generate_rag_answer(ground_truth[0])
answer_record
```

Before running the full batch, reset the usage we collected while
testing:

```python
assistant.reset_usage()
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

`generate_rag_answer` returns one answer record for each question.

Collect the answer records:

```python
answers = []

for answer_record in results:
    answers.append(answer_record)
```

Calculate the total cost:

```python
assistant.total_cost()
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
- Cost with the prices above: $0.321433, about 32 cents

If you don't want to generate the RAG answers yourself, download the
file we prepared:

```bash
PREFIX=https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main

wget -O data/rag-answers.csv ${PREFIX}/04-evaluation/data/rag-answers.csv
```

In the next lesson, we'll evaluate these answers with an LLM judge.

[← RAG and Agent Evaluation](11-evaluation-intro.md) | [LLM as a Judge →](13-llm-as-judge.md)
