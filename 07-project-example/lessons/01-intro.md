# End-to-End Project Example

<a href="https://www.youtube.com/watch?v=E9O0Tg68PPg&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/E9O0Tg68PPg">
</a>

In this module, we build a complete RAG project from scratch. The
project is a fitness assistant that helps users with exercise questions.

The final project is at
[alexeygrigorev/fitness-assistant](https://github.com/alexeygrigorev/fitness-assistant)
on GitHub. Check the final result - it's been polished beyond what
we show in the videos.

## Project overview

A RAG application that:

- Uses a dataset of exercises with muscle groups, equipment, and
  instructions
- Answers questions about exercises, replacements, and proper form
- Has a search component, an LLM component, and evaluation
- Includes an API interface (Flask)
- Has monitoring with PostgreSQL and Grafana
- Is containerized with Docker

## Setting up the project

Create a new project with uv:

```bash
mkdir fitness-assistant
cd fitness-assistant
uv init
uv add openai minsearch requests python-dotenv jupyter pandas scikit-learn tqdm
rm main.py
```

Create a `.env` file with your OpenAI API key:

```env
OPENAI_API_KEY=sk-...
```

Add `.env` to `.gitignore`:

```gitignore
.env
```

Start Jupyter:

```bash
uv run jupyter notebook
```

## Generating the dataset

Since we don't have a real fitness FAQ database, we generate one
with an LLM. We use structured output (from module 04) to make
sure the data comes back in the right format.

First, define a Pydantic model for a single exercise:

```python
from pydantic import BaseModel, Field
from typing import List

class Exercise(BaseModel):
    id: str = Field(description="Unique identifier, e.g. 'push-up-001'")
    exercise_name: str = Field(description="Name of the exercise")
    type_of_activity: str = Field(description="Strength, Cardio, Flexibility, etc.")
    type_of_equipment: str = Field(description="Dumbbells, Barbell, None (bodyweight), etc.")
    body_part: str = Field(description="Chest, Back, Legs, etc.")
    type: str = Field(description="Compound, Isolation, etc.")
    muscle_groups_activated: str = Field(description="Comma-separated list, e.g. 'Chest, Triceps, Shoulders'")
    instructions: str = Field(description="Detailed step-by-step instructions")

class ExerciseDataset(BaseModel):
    exercises: List[Exercise]
```

Now generate the data using `responses.parse`:

```python
from openai import OpenAI
import pandas as pd

openai_client = OpenAI()

prompt = """
Generate a dataset of 50 diverse fitness exercises.
Cover different muscle groups, equipment types, and difficulty levels.
Include bodyweight exercises, free weights, and machine exercises.
""".strip()

response = openai_client.responses.parse(
    model="gpt-5.4-mini",
    input=[{"role": "user", "content": prompt}],
    text_format=ExerciseDataset,
)

dataset = response.output_parsed
df = pd.DataFrame([ex.model_dump() for ex in dataset.exercises])
df.to_csv("data/data.csv", index=False)
print(f"Generated {len(df)} exercises")
```

You may need to run this multiple times with different prompts
to cover enough exercises. Append all results to `data/data.csv`.

## The RAG flow

Build the basic RAG flow in a notebook.

First, load the data and
create a search index:

```python
import pandas as pd
from minsearch import Index

df = pd.read_csv("data/data.csv")
documents = df.to_dict(orient="records")

index = Index(
    text_fields=[
        "exercise_name",
        "type_of_activity",
        "type_of_equipment",
        "body_part",
        "type",
        "muscle_groups_activated",
        "instructions",
    ],
    keyword_fields=["id"]
)

index.fit(documents)
```

Search function:

```python
def search(query):
    boost = {}

    results = index.search(
        query=query,
        filter_dict={},
        boost_dict=boost,
        num_results=10
    )

    return results
```

Build the prompt:

```python
prompt_template = """
You're a fitness instructor. Answer the QUESTION based on the CONTEXT from our exercises database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT:
{context}
""".strip()

entry_template = """
exercise_name: {exercise_name}
type_of_activity: {type_of_activity}
type_of_equipment: {type_of_equipment}
body_part: {body_part}
type: {type}
muscle_groups_activated: {muscle_groups_activated}
instructions: {instructions}
""".strip()

def build_prompt(query, search_results):
    context = ""

    for doc in search_results:
        context = context + entry_template.format(**doc) + "\n\n"

    prompt = prompt_template.format(question=query, context=context).strip()
    return prompt
```

Call the LLM:

```python
from openai import OpenAI

openai_client = OpenAI()

def llm(prompt, model="gpt-5.4-mini"):
    response = openai_client.responses.create(
        model=model,
        input=[{"role": "user", "content": prompt}]
    )

    return response.output_text
```

Put it together:

```python
def rag(query, model="gpt-5.4-mini"):
    search_results = search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(prompt, model=model)
    return answer
```

Test it:

```python
question = "Is the Lat Pulldown considered a strength training activity, and if so, why?"
answer = rag(question)
print(answer)
```

We now have a working RAG flow. In the next lessons, we'll
evaluate it, wrap it in an API, and add monitoring.

[← Back to module](../) | [Evaluating Retrieval →](02-evaluating-retrieval.md)
