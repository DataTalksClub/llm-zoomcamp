# Interface and Ingestion Pipeline

<a href="https://www.youtube.com/watch?v=vMHve2EyA5M&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/vMHve2EyA5M">
</a>

So far we've been working in notebooks. Now we turn the notebook
into a proper application with an ingestion pipeline and a web API.

## From notebook to scripts

Convert the notebook to Python:

```bash
jupyter nbconvert --to=script rag-test.ipynb
```

Then organize the code into a package structure:

```text
fitness_assistant/
    __init__.py
    rag.py          # RAG flow + search + LLM
    ingest.py       # Load data into search index
    minsearch.py    # (installed via uv add minsearch instead)
app.py              # Flask API
db.py               # Database functions (added later)
```

Since we're using `minsearch` as a package (installed with
`uv add minsearch`), we don't need to copy `minsearch.py`.

## Ingestion

The ingestion script loads the CSV and builds the search index.

Since minsearch is in-memory, ingestion happens when the app
starts:

```python
import os
import pandas as pd
from minsearch import Index

DATA_PATH = os.getenv("DATA_PATH", "data/data.csv")

def load_index(data_path=DATA_PATH):
    df = pd.read_csv(data_path)
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
        keyword_fields=["id"],
    )

    index.fit(documents)
    return index
```

If you use a real database like Elasticsearch, ingestion would be
a separate step that indexes documents into the database.

## RAG module

The RAG module imports the index and provides the `rag` function:

```python
import json
from time import time
from openai import OpenAI
import ingest

openai_client = OpenAI()
index = ingest.load_index()

def search(query):
    boost = {
        "exercise_name": 2.11,
        "type_of_activity": 1.46,
        "type_of_equipment": 0.65,
        "body_part": 2.65,
        "type": 1.31,
        "muscle_groups_activated": 2.54,
        "instructions": 0.74
    }

    results = index.search(
        query=query, filter_dict={}, boost_dict=boost, num_results=10
    )
    return results
```

Define the prompt templates and the prompt builder:

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

Add the LLM call and the full RAG function:

```python
def llm(prompt, model="gpt-5.4-mini"):
    response = openai_client.responses.create(
        model=model,
        input=[{"role": "user", "content": prompt}]
    )
    answer = response.output_text
    token_stats = {
        "prompt_tokens": response.usage.input_tokens,
        "completion_tokens": response.usage.output_tokens,
        "total_tokens": response.usage.total_tokens,
    }
    return answer, token_stats

def rag(query, model="gpt-5.4-mini"):
    t0 = time()
    search_results = search(query)
    prompt = build_prompt(query, search_results)
    answer, token_stats = llm(prompt, model=model)
    took = time() - t0

    return {
        "answer": answer,
        "model_used": model,
        "response_time": took,
        "prompt_tokens": token_stats["prompt_tokens"],
        "completion_tokens": token_stats["completion_tokens"],
        "total_tokens": token_stats["total_tokens"],
    }
```

## Flask API

Create a simple API endpoint:

```python
import uuid
from flask import Flask, request, jsonify
from rag import rag

app = Flask(__name__)

@app.route("/question", methods=["POST"])
def handle_question():
    data = request.json
    question = data["question"]

    if not question:
        return jsonify({"error": "No question provided"}), 400

    conversation_id = str(uuid.uuid4())
    answer_data = rag(question)

    result = {
        "conversation_id": conversation_id,
        "question": question,
        "answer": answer_data["answer"],
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
```

Install Flask:

```bash
uv add flask
```

Test it:

```bash
uv run python app.py
```

Then send a request:

```bash
curl -X POST http://localhost:5000/question \
  -H "Content-Type: application/json" \
  -d '{"question": "What exercises target the chest?"}'
```

## Improving the README

Update the README with instructions for:

- Installing dependencies (`uv sync`)
- Running the ingestion pipeline
- Starting the API server
- Example API calls

A good README makes it easy for anyone to run your project.

[← Evaluating RAG](03-evaluating-rag.md) | [Monitoring and Containerization →](05-monitoring.md)
