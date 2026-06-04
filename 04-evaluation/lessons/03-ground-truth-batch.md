# Generating Ground Truth for All Documents

Video: [Watch this lesson](https://www.youtube.com/watch?v=eM6xmdZDT6k&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

In the previous lesson, we generated questions for one document and
converted them into ground truth records.

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

Each record contains the generated question and the ID of the document
that should answer the question.

When we send many requests, one of them might fail. We don't want the
entire batch to fail because of one temporary error.

Import the retry helper from `evaluation_utils.py`:

```python
from evaluation_utils import llm_structured_retry
```

`llm_structured` makes one structured-output call. `llm_structured_retry`
wraps the same call in a retry loop. If one request fails because of a
temporary API or network issue, it waits briefly and tries again.

Use it in the processing function:

```python
def generate_ground_truth(doc):
    user_prompt = json.dumps(doc)

    out, usage = llm_structured_retry(
        openai_client,
        data_gen_instructions,
        user_prompt,
        Questions
    )

    results = []

    for q in out.questions:
        results.append({
            "question": q,
            "document": doc["id"]
        })

    return results, usage
```

Try it for the first 5 documents.

Import `tqdm` and run the loop:

```python
from tqdm.auto import tqdm

ground_truth = []
usages = []

for doc in tqdm(documents[:5]):
    records, usage = generate_ground_truth(doc)
    ground_truth.extend(records)
    usages.append(usage)
```

This works, but it runs one LLM call after another. Running it for all
documents this way would take too long.

## Parallel processing

Running the calls one after another wastes most of the time waiting on
the network. Each request just sits there until OpenAI responds, so we
can fire several at once and wait on them together. We process the
documents in parallel and track progress while the requests run.

One caution: don't open too many connections at once, or you'll hit the
provider's rate limits. Five or six workers is a safe default here.

Import `ThreadPoolExecutor`:

```python
from concurrent.futures import ThreadPoolExecutor
from evaluation_utils import map_progress
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

len(ground_truth)
```

With 5 questions per document, you should get roughly 5x the number of
documents.


Calculate the total cost:

```python
from evaluation_utils import calc_price

total_cost = 0.0

for usage in usages:
    cost = calc_price(usage)
    total_cost = total_cost + cost["total_cost"]

total_cost
```

We'll calculate total cost several times in this module, so the utility
file has a helper for it:

```python
from evaluation_utils import calc_total_price

calc_total_price(usages)
```

Create a dataframe so we can look at the records as a table and save
them as a CSV file.

Create the dataframe:

```python
import pandas as pd

df_ground_truth = pd.DataFrame(ground_truth)
```

Because we generated the questions from specific documents, we know
which document is correct for each question. We now have the ground
truth we need for evaluation.

Save it for later use:

```python
df_ground_truth.to_csv("data/ground_truth-new.csv", index=False)
```

We generated this file for the course materials on May 29, 2026. The
run used 79 LLM Zoomcamp documents and produced 395 questions.

The FAQ data can change over time. If you run the notebook later, you
may see different documents and generated questions. Token usage, cost,
and search evaluation results may also change.

The total cost was $0.057187, about 6 cents.

If you don't want to generate the questions yourself, download the file
we prepared:

```bash
PREFIX=https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main

wget -O data/ground_truth-new.csv ${PREFIX}/04-evaluation/data/ground_truth-new.csv
```

Now we have questions with known correct documents. In the next lesson,
we'll run search for these questions and check whether the correct
documents appear in the results.

[← Generating Ground Truth Data](02-ground-truth.md) | [Search Evaluation →](04-search-evaluation.md)
