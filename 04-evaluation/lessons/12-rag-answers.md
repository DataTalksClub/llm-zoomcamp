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

Run RAG for one question:

```python
rec = ground_truth[0]
question = rec["question"]

answer_llm = assistant.rag(question)
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

## Processing all questions

Do the same thing for all ground truth questions:

```python
from tqdm.auto import tqdm

answers = []

for rec in tqdm(ground_truth):
    question = rec["question"]
    doc_id = rec["document"]
    original_doc = doc_idx[doc_id]

    answer_llm = assistant.rag(question)
    answer_orig = original_doc["answer"]

    answers.append({
        "question": question,
        "answer_llm": answer_llm,
        "answer_orig": answer_orig,
        "document": doc_id,
    })
```

This calls the LLM once per ground truth question, so it can take some
time.

Save the answers:

```python
df_answers = pd.DataFrame(answers)
df_answers.to_csv("data/rag-answers.csv", index=False)
```

In the next lesson, we'll evaluate these answers with an LLM judge.

[← RAG and Agent Evaluation](11-evaluation-intro.md) | [LLM as a Judge →](13-llm-as-judge.md)
