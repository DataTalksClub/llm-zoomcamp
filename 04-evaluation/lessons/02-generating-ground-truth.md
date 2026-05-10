# Generating Ground Truth Data

To evaluate search, we need a dataset of queries where we know which
document is the correct answer. This is called ground truth (or gold
standard) data.

For each query in our ground truth dataset, we know which document in
the knowledge base is relevant. When we run a search, we check if the
correct document shows up in the results.

There are several ways to get ground truth data:

- Human annotators look at documents and write queries (best quality, expensive)
- Collect real user queries and label them (requires a running system)
- Generate synthetic data with an LLM (what we'll do)

We don't have a production system yet, so we'll use an LLM to generate
questions. For each FAQ document, we ask the LLM to create 5 questions
that this document would answer. Then we know that for each generated
question, the source document is the correct answer.


## Loading the documents

Let's load the FAQ data from the same dataset we used in previous
modules:

```python
import requests

docs_url = 'https://datatalks.club/faq/json/courses.json'
response = requests.get(docs_url)
courses_raw = response.json()

documents = []
url_prefix = 'https://datatalks.club/faq'

for course in courses_raw:
    course_url = f'{url_prefix}{course["path"]}'
    course_response = requests.get(course_url)
    course_data = course_response.json()

    for doc in course_data:
        doc['course_name'] = course['course_name']
        documents.append(doc)
```

Each document already has an `id` field:

```python
print(documents[0]['id'])
print(documents[0]['question'])
```

We'll use this ID to track which document was retrieved.


## Generating questions with structured output

Now we use an LLM to generate questions for each document. We want the
output as a list of strings, so we use structured output with a Pydantic
model:

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
This makes the evaluation more realistic -- real users won't phrase
their questions the same way as the FAQ.

The function to call the LLM with structured output:

```python
from openai import OpenAI
openai_client = OpenAI()

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

    return response.output_parsed
```

Let's test it on one document:

```python
import json

result = llm_structured(
    data_gen_instructions,
    json.dumps(documents[0]),
    Questions
)

print(result.questions)
```

You should see 5 questions that relate to the first FAQ document.


## Parallel processing

Generating questions for all documents takes a while. We can speed it
up with parallel processing:

```python
from tqdm.auto import tqdm
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

The processing function takes a document and returns ground truth
records:

```python
def process(doc):
    out = llm_structured(
        data_gen_instructions,
        json.dumps(doc),
        Questions
    )

    results = []

    for q in out.questions:
        results.append({
            'question': q,
            'course': doc['course'],
            'document': doc['id']
        })

    return results
```

Now generate for all documents:

```python
with ThreadPoolExecutor(max_workers=6) as pool:
    ground_truth = map_progress(pool, documents, process)
```

Flatten the nested lists into a single dataset:

```python
import pandas as pd

ground_truth_flat = [item for sublist in ground_truth for item in sublist]
df_ground_truth = pd.DataFrame(ground_truth_flat)

print(len(df_ground_truth))
```

With 5 questions per document, you should get roughly 5x the number of
documents.

The key insight: because we generated the questions from specific
documents, we know which document is correct for each question. This
gives us the ground truth we need for evaluation.

Save it for later use:

```python
df_ground_truth.to_csv('ground-truth-data.csv', index=False)
```


[<< Previous: Intro](01-intro)
|
[Next: Search Evaluation >>](03-search-evaluation)
