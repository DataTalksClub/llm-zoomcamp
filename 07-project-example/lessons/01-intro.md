# End-to-End Project Example

<a href="https://www.youtube.com/watch?v=E9O0Tg68PPg&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/E9O0Tg68PPg">
</a>

In this module, we walk through building a complete RAG project
from scratch - a fitness assistant that helps users with exercise
questions.

The final project is at
[alexeygrigorev/fitness-assistant](https://github.com/alexeygrigorev/fitness-assistant)
on GitHub. Check the final result - it's been polished beyond what
we show in the videos.


## What we'll build

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

```
OPENAI_API_KEY=sk-...
```

Add `.env` to `.gitignore`:

```
.env
```

Start Jupyter:

```bash
uv run jupyter notebook
```


## Generating the dataset

Since we don't have a real fitness FAQ database, we generate one
with an LLM. The idea is to create a CSV with records like:

```csv
id,exercise_name,type_of_activity,type_of_equipment,body_part,type,muscle_groups_activated,instructions
push-up-001,Push-up,Strength,None (bodyweight),Chest,Compound,"Chest, Triceps, Shoulders","Start in a plank position with hands slightly wider than shoulders..."
```

We use GPT to generate hundreds of these records across different
muscle groups and exercise types. The prompt looks like this:

```python
from openai import OpenAI
import pandas as pd
import json

openai_client = OpenAI()

prompt = """
Generate a dataset of 50 fitness exercises as JSON array.
Each exercise should have these fields:
- id: unique identifier (e.g. "push-up-001")
- exercise_name: name of the exercise
- type_of_activity: "Strength", "Cardio", "Flexibility", etc.
- type_of_equipment: "Dumbbells", "Barbell", "None (bodyweight)", etc.
- body_part: "Chest", "Back", "Legs", etc.
- type: "Compound", "Isolation", etc.
- muscle_groups_activated: "Chest, Triceps, Shoulders"
- instructions: detailed step-by-step instructions

Cover different muscle groups and difficulty levels.
""".strip()

response = openai_client.responses.create(
    model="gpt-5.4-mini",
    input=[{"role": "user", "content": prompt}]
)

data = json.loads(response.output_text)
df = pd.DataFrame(data)
df.to_csv('data/data.csv', index=False)
```

You may need to run this multiple times with different prompts
to cover enough exercises. Save all results to `data/data.csv`.


## The RAG flow

Now let's build the basic RAG flow in a notebook. First, load the
data and create a search index:

```python
import pandas as pd
from minsearch import Index

df = pd.read_csv('data/data.csv')
documents = df.to_dict(orient='records')

index = Index(
    text_fields=[
        'exercise_name',
        'type_of_activity',
        'type_of_equipment',
        'body_part',
        'type',
        'muscle_groups_activated',
        'instructions',
    ],
    keyword_fields=['id']
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

def llm(prompt, model='gpt-5.4-mini'):
    response = openai_client.responses.create(
        model=model,
        input=[{"role": "user", "content": prompt}]
    )

    return response.output_text
```

Put it together:

```python
def rag(query, model='gpt-5.4-mini'):
    search_results = search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(prompt, model=model)
    return answer
```

Test it:

```python
question = 'Is the Lat Pulldown considered a strength training activity, and if so, why?'
answer = rag(question)
print(answer)
```

This gives us a working RAG flow. In the next lessons, we'll
evaluate it, wrap it in an API, and add monitoring.


[<< Back to module](../)
|
[Next: Evaluating Retrieval >>](02-evaluating-retrieval.md)
