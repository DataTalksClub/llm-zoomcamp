# Generating Ground Truth Data

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

We'll use the same ingestion script from module 01.

If you don't have `ingest.py` in your notebook directory, download it:

```bash
wget https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/01-agentic-rag/code/ingest.py
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

documents = documents_llm

len(documents)
```

Each document already has an `id` field:

```python
doc = documents[0]
print(doc["id"])
print(doc["question"])
```

The ID becomes the label in our ground truth dataset. We generate
questions from a document, so we know that this document contains the
answer. Later, search evaluation checks whether search retrieves the
document with this ID.

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

Create the messages:

```python
import json

user_prompt = json.dumps(doc)

messages = [
    {"role": "developer", "content": data_gen_instructions},
    {"role": "user", "content": user_prompt}
]
```

Call the model:

```python
response = openai_client.responses.parse(
    model="gpt-5.4-mini",
    input=messages,
    text_format=Questions
)
```

The parsed output is available in `response.output_parsed`:

```python
result = response.output_parsed

print(result)
```

We can access the list directly:

```python
print(result.questions)
```

You should see 5 questions that relate to the first FAQ document.

## Tracking cost

The response also contains token usage:

```python
usage = response.usage
usage.input_tokens, usage.output_tokens
```

As in the agents module, we calculate the price from `response.usage`:

```python
def calc_price(usage):
    INPUT_PRICE_PER_MILLION = 0.75
    OUTPUT_PRICE_PER_MILLION = 4.50

    input_cost = (usage.input_tokens / 1_000_000) * INPUT_PRICE_PER_MILLION
    output_cost = (usage.output_tokens / 1_000_000) * OUTPUT_PRICE_PER_MILLION
    total_cost = input_cost + output_cost

    return {
        "input_cost": input_cost,
        "output_cost": output_cost,
        "total_cost": total_cost,
    }
```

Calculate the cost of this call:

```python
cost = calc_price(usage)

cost
```

Wrap the structured-output call into a function so we can reuse it for
all documents:

```python
def llm_structured(instructions, user_prompt, output_type, model="gpt-5.4-mini"):
    messages = [
        {"role": "developer", "content": instructions},
        {"role": "user", "content": user_prompt}
    ]

    response = openai_client.responses.parse(
        model=model,
        input=messages,
        text_format=output_type
    )

    return response.output_parsed, response.usage
```

Test it on the same document:

```python
user_prompt = json.dumps(doc)

out, usage = llm_structured(data_gen_instructions, user_prompt, Questions)

print(out.questions)
print(calc_price(usage))
```

Now convert these questions into ground truth records:

```python
records = []

for q in out.questions:
    records.append({
        "question": q,
        "course": doc["course"],
        "document": doc["id"]
    })

records
```

Each record has three fields:

- `question`: the question generated by the LLM
- `course`: the course this FAQ document belongs to
- `document`: the ID of the FAQ document that should answer the question

The `document` field connects the generated question to the document
that contains the answer. Later, when we evaluate search, we'll ask the
search engine the generated question. Then we'll check if it retrieves
the document with this ID.

## Generating questions for all documents

We want to do the same thing for every document in the FAQ dataset.
For each document, we generate questions and save them as ground truth
records.

For this part, we'll use `tqdm` for progress bars and `pandas` for
saving the final CSV.

If you don't have them installed yet, add them first:

```bash
uv add tqdm pandas
```

The processing function takes one document and turns it into ground
truth records.

For each document, we:

- convert the document to JSON so we can send it to the LLM
- ask the LLM to return a `Questions` object
- create one ground truth record for each generated question

Each record contains the generated question, the course, and the ID of
the document that should answer the question.

When we send many requests, one of them might fail. We don't want the
entire batch to fail because of one temporary error.

Add a retry wrapper:

```python
import time

def llm_structured_retry(instructions, user_prompt, output_type, max_retries=3):
    for attempt in range(max_retries):
        try:
            return llm_structured(instructions, user_prompt, output_type)
        except Exception:
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt)
```

Use it in the processing function:

```python
def generate_ground_truth(doc):
    user_prompt = json.dumps(doc)

    out, usage = llm_structured_retry(
        data_gen_instructions,
        user_prompt,
        Questions
    )

    results = []

    for q in out.questions:
        results.append({
            "question": q,
            "course": doc["course"],
            "document": doc["id"]
        })

    return results, usage
```

Try it for the first 10 documents.

Import `tqdm` and run the loop:

```python
from tqdm.auto import tqdm

ground_truth = []
usages = []

for doc in tqdm(documents[:10]):
    records, usage = generate_ground_truth(doc)
    ground_truth.extend(records)
    usages.append(usage)
```

This works, but it runs one LLM call after another. Running it for all
documents this way would take too long.

## Parallel processing

We want to process documents in parallel and track progress while the
requests are running.

We'll use this helper:

```python
from concurrent.futures import ThreadPoolExecutor

def map_progress(pool, seq, f):
    results = []

    with tqdm(total=len(seq)) as progress:
        futures = []

        for el in seq:
            future = pool.submit(f, el)
            future.add_done_callback(lambda p: progress.update())
            futures.append(future)

        for future in futures:
            result = future.result()
            results.append(result)

    return results
```

This submits one job per document, updates the progress bar when a job
finishes, and collects the results. If you want a more detailed
explanation of `ThreadPoolExecutor` and futures, ask ChatGPT to walk
through this helper line by line.

Then replace the loop with the parallel version:

```python
with ThreadPoolExecutor(max_workers=6) as pool:
    results = map_progress(pool, documents, generate_ground_truth)
```

`generate_ground_truth` returns two things for each document: the
generated records and the token usage.

Split those into separate lists:

```python
ground_truth = []
usages = []

for records, usage in results:
    ground_truth.extend(records)
    usages.append(usage)
```

Check the list size:

```python
len(ground_truth)
```

Calculate the total cost:

```python
total_cost = 0.0

for usage in usages:
    cost = calc_price(usage)
    total_cost = total_cost + cost["total_cost"]

total_cost
```

Create a dataframe so we can look at the records as a table and save
them as a CSV file.

Create the dataframe:

```python
import pandas as pd

df_ground_truth = pd.DataFrame(ground_truth)
```

Check the dataframe size:

```python
print(len(df_ground_truth))
```

With 5 questions per document, you should get roughly 5x the number of
documents.

Because we generated the questions from specific documents, we know
which document is correct for each question. We now have the ground
truth we need for evaluation.

Save it for later use:

```python
from pathlib import Path
df_ground_truth.to_csv("data/ground-truth-data.csv", index=False)
```

We generated this file for the course materials on May 28, 2026. The
run used 79 LLM Zoomcamp documents and produced 395 questions.

The FAQ data can change over time. If you run the notebook later, you
may see different documents and generated questions. Token usage, cost,
and search evaluation results may also change.

The token usage was:

- Input tokens: 21,762
- Output tokens: 9,699
- Estimated cost with the prices above: $0.059967, about 6 cents

If you don't want to generate the questions yourself, download the file
we prepared:

```bash
mkdir -p data
wget -O data/ground-truth-data.csv https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/04-evaluation/data/ground-truth-data.csv
```

[← Evaluation](01-intro.md) | [Search Evaluation →](03-search-evaluation.md)
