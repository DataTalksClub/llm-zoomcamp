# Generating Ground Truth Data

Video: [Watch this lesson](https://www.youtube.com/watch?v=YScoH28cVf8&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

To evaluate search, we need a dataset of queries where we know which
document is the correct answer. This is called ground truth (or gold
standard) data.

For each query in our ground truth dataset, we know which document in
the knowledge base is relevant. When we run a search, we check whether
the results include the correct document.

There are several ways to get ground truth data:

- Human annotators look at documents and write queries (best quality, expensive)
- Collect real user queries and label them (requires a running system)
- Generate synthetic data with an LLM (what we'll do)

We don't have a production system yet, so we'll use an LLM to generate
questions. For each FAQ document, we ask the LLM to create 5 questions
that this document would answer. Then we know that for each generated
question, the source document is the correct answer.

## Loading the documents

We'll use helper files from module 01 and this module.

If you don't have them in your notebook directory, download them:

```bash
PREFIX=https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main

wget ${PREFIX}/01-agentic-rag/code/ingest.py
wget ${PREFIX}/01-agentic-rag/code/rag_helper.py
wget ${PREFIX}/04-evaluation/code/evaluation_utils.py
```

Then load the FAQ data:

```python
from ingest import load_faq_data
documents = load_faq_data()
```

We'll generate questions only for the LLM Zoomcamp FAQ. The full FAQ
dataset contains documents from multiple courses. Generating five
questions for every document would take longer and cost more.

```python
documents_llm = []

for doc in documents:
    if doc["course"] == "llm-zoomcamp":
        documents_llm.append(doc)

len(documents_llm)
```

We'll use these documents from now on so let's name them as `documents`

```python
documents = documents_llm
```

Each document already has an `id` field:

```python
doc = documents[0]
print(doc["id"])
print(doc["question"])
print(doc["answer"])
```

The ID becomes the label in our ground truth dataset. We generate
questions from a document, so we know that this document holds the
answer. Later, search evaluation checks whether search brings back the
document with this ID.

This is why every record needs a stable ID. If you can't uniquely
identify a document, you can't tell whether search retrieved the right
one. When you build your own evaluation set, assign an ID to each record
in your knowledge base first.

## Generating questions with structured output

We use an LLM to generate questions for each document.

This is the first time we're using structured output in the course.
With structured output, we ask the LLM to return data in a specific
format instead of free-form text. For example, instead of getting a
paragraph that contains questions, we can ask for a Python object with
a `questions` field.

This is useful when code will process the output. The model returns the
same structure every time. We can access the generated questions
directly instead of parsing text manually.

We want the output as a list of strings, so we define that structure
with a Pydantic model:

```python
from pydantic import BaseModel

class Questions(BaseModel):
    questions: list[str]
```

The instructions for the LLM:

```python
data_gen_instructions = """
You emulate a student who's taking our course.
Formulate 5 questions this student might ask based on a FAQ record. The record
should contain the answer to the questions, and the questions should be complete and not too short.
If possible, use as fewer words as possible from the record.

The output should resemble how people ask questions
on the internet. Not too formal, not too short, not too long.
""".strip()
```

We ask the LLM to use different wording from the original document.
This makes the evaluation more realistic - real users won't phrase
their questions the same way as the FAQ.

Call the LLM for one document:

```python
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_client = OpenAI()
```

Prepare the document as JSON:

```python
import json

user_prompt = json.dumps(doc)
```

Create the messages:

```python
messages = [
    {"role": "developer", "content": data_gen_instructions},
    {"role": "user", "content": user_prompt}
]
```

Until now we called `responses.create` and read `response.output_text`.
For structured output we switch to `responses.parse` and pass
`text_format=Questions`, which tells the API to return our class instead
of free text.

Call the model:

```python
response = openai_client.responses.parse(
    model="gpt-5.4-mini",
    input=messages,
    text_format=Questions
)
```

The parsed object is available in `response.output_parsed`:

```python
result = response.output_parsed

print(result)
```

We can access the list directly:

```python
print(result.questions)
```

You should see 5 questions that relate to the first FAQ document.

## Reusable utilities

We'll need this pattern again in other evaluation sections today, so
we put it in a reusable helper.

It contains helper functions we'll reuse in this module:

- `llm_structured`: calls the OpenAI API with structured output
- `llm_structured_retry`: retries structured-output calls when a
  request fails
- `calc_price`: calculates the price from token usage
- `calc_total_price`: calculates the total price from multiple usage
  objects
- `map_progress`: runs work in parallel and tracks progress. We'll use it
  in the next lesson.

Import the structured-output helper:

```python
from evaluation_utils import llm_structured
```

Use it on the same document:

```python
result, usage = llm_structured(
    openai_client,
    data_gen_instructions,
    user_prompt,
    Questions
)

print(result.questions)
```

## Tracking cost

The response also contains token usage:

```python
usage.input_tokens, usage.output_tokens
```

As in the agents module, we calculate the price from `response.usage`.

Import the price helper:

```python
from evaluation_utils import calc_price
```

Calculate the cost of this call:

```python
cost = calc_price(usage)

cost
```

Now convert these questions into ground truth records:

```python
records = []

for q in result.questions:
    records.append({
        "question": q,
        "document": doc["id"]
    })

records
```

Each record has two fields:

- `question`: the question generated by the LLM
- `document`: the ID of the FAQ document that should answer the question

The `document` field connects the generated question to the document
that contains the answer. Later, when we evaluate search, we'll ask the
search engine the generated question. Then we'll check if it retrieves
the document with this ID.

We now know how to generate and store questions for one document. In
the next lesson, we'll run this for all LLM Zoomcamp FAQ documents and
save the full ground truth dataset.

[← Evaluation](01-intro.md) | [Generating Ground Truth for All Documents →](03-ground-truth-batch.md)
