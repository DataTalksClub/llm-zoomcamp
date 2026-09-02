# Monitoring and Containerization

<a href="https://www.youtube.com/watch?v=nQda9etJWW8&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/nQda9etJWW8">
</a>

We take the same monitoring approach from module 05 and apply it
to our fitness assistant. Then we containerize everything with
Docker Compose.

## Adding evaluation to the RAG flow

First, add the LLM-as-a-judge evaluation directly into the RAG
function so every answer gets a relevance score:

```python
import json
from time import time
from openai import OpenAI
import ingest

openai_client = OpenAI()
index = ingest.load_index()

evaluation_prompt_template = """
You are an expert evaluator for a RAG system.
Your task is to analyze the relevance of the generated answer to the given question.
Based on the relevance of the generated answer, you will classify it
as 'NON_RELEVANT', 'PARTLY_RELEVANT', or 'RELEVANT'.

Here is the data for evaluation:

Question: {question}
Generated Answer: {answer}

Please analyze the content and context of the generated answer in relation to the question
and provide your evaluation in parsable JSON without using code blocks:

{{
  'Relevance': 'NON_RELEVANT' | 'PARTLY_RELEVANT' | 'RELEVANT',
  'Explanation': '[Provide a brief explanation for your evaluation]'
}}
""".strip()
```

Define the evaluation and cost helper functions:

```python
def evaluate_relevance(question, answer):
    prompt = evaluation_prompt_template.format(question=question, answer=answer)
    evaluation, tokens = llm(prompt, model="gpt-5.4-mini")

    try:
        json_eval = json.loads(evaluation)
        return json_eval, tokens
    except json.JSONDecodeError:
        result = {"Relevance": "UNKNOWN", "Explanation": "Failed to parse evaluation"}
        return result, tokens

def calculate_openai_cost(model, tokens):
    openai_cost = 0
    if "gpt-5.4-mini" in model:
        openai_cost = (
            tokens["prompt_tokens"] * 0.15
            + tokens["completion_tokens"] * 0.60
        ) / 1_000_000
    return openai_cost
```

Now update the `rag` function to call the evaluator and track costs:

```python
def rag(query, model="gpt-5.4-mini"):
    t0 = time()

    search_results = search(query)
    prompt = build_prompt(query, search_results)
    answer, token_stats = llm(prompt, model=model)

    relevance, rel_token_stats = evaluate_relevance(query, answer)

    t1 = time()
    took = t1 - t0

    openai_cost_rag = calculate_openai_cost(model, token_stats)
    openai_cost_eval = calculate_openai_cost(model, rel_token_stats)
    openai_cost = openai_cost_rag + openai_cost_eval

    return {
        "answer": answer,
        "model_used": model,
        "response_time": took,
        "relevance": relevance.get("Relevance", "UNKNOWN"),
        "relevance_explanation": relevance.get("Explanation", "Failed to parse"),
        "prompt_tokens": token_stats["prompt_tokens"],
        "completion_tokens": token_stats["completion_tokens"],
        "total_tokens": token_stats["total_tokens"],
        "eval_prompt_tokens": rel_token_stats["prompt_tokens"],
        "eval_completion_tokens": rel_token_stats["completion_tokens"],
        "eval_total_tokens": rel_token_stats["total_tokens"],
        "openai_cost": openai_cost,
    }
```

## Database functions

Store conversations and feedback in PostgreSQL:

```python
import os
import psycopg2
from psycopg2.extras import DictCursor
from datetime import datetime
from zoneinfo import ZoneInfo

TZ_INFO = os.getenv("TZ", "Europe/Berlin")
tz = ZoneInfo(TZ_INFO)

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "postgres"),
        database=os.getenv("POSTGRES_DB", "fitness_assistant"),
        user=os.getenv("POSTGRES_USER", "user"),
        password=os.getenv("POSTGRES_PASSWORD", "password"),
    )
```

Create the database schema with a table for conversations and a table for feedback:

```python
def init_db():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS feedback")
            cur.execute("DROP TABLE IF EXISTS conversations")

            cur.execute("""
                CREATE TABLE conversations (
                    id TEXT PRIMARY KEY,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL,
                    model_used TEXT NOT NULL,
                    response_time FLOAT NOT NULL,
                    relevance TEXT NOT NULL,
                    relevance_explanation TEXT NOT NULL,
                    prompt_tokens INTEGER NOT NULL,
                    completion_tokens INTEGER NOT NULL,
                    total_tokens INTEGER NOT NULL,
                    eval_prompt_tokens INTEGER NOT NULL,
                    eval_completion_tokens INTEGER NOT NULL,
                    eval_total_tokens INTEGER NOT NULL,
                    openai_cost FLOAT NOT NULL,
                    timestamp TIMESTAMP WITH TIME ZONE NOT NULL
                )
            """)
            cur.execute("""
                CREATE TABLE feedback (
                    id SERIAL PRIMARY KEY,
                    conversation_id TEXT REFERENCES conversations(id),
                    feedback INTEGER NOT NULL,
                    timestamp TIMESTAMP WITH TIME ZONE NOT NULL
                )
            """)
        conn.commit()
    finally:
        conn.close()
```

Add functions to save conversations and feedback:

```python
def save_conversation(conversation_id, question, answer_data, timestamp=None):
    if timestamp is None:
        timestamp = datetime.now(tz)

    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO conversations
                (id, question, answer, model_used, response_time, relevance,
                relevance_explanation, prompt_tokens, completion_tokens, total_tokens,
                eval_prompt_tokens, eval_completion_tokens, eval_total_tokens,
                openai_cost, timestamp)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    conversation_id,
                    question,
                    answer_data["answer"],
                    answer_data["model_used"],
                    answer_data["response_time"],
                    answer_data["relevance"],
                    answer_data["relevance_explanation"],
                    answer_data["prompt_tokens"],
                    answer_data["completion_tokens"],
                    answer_data["total_tokens"],
                    answer_data["eval_prompt_tokens"],
                    answer_data["eval_completion_tokens"],
                    answer_data["eval_total_tokens"],
                    answer_data["openai_cost"],
                    timestamp
                ),
            )
        conn.commit()
    finally:
        conn.close()
```

And a function to record user feedback:

```python
def save_feedback(conversation_id, feedback, timestamp=None):
    if timestamp is None:
        timestamp = datetime.now(tz)

    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO feedback (conversation_id, feedback, timestamp) VALUES (%s, %s, %s)",
                (conversation_id, feedback, timestamp),
            )
        conn.commit()
    finally:
        conn.close()
```

## Updated Flask API with logging

Now the API saves every conversation and accepts feedback:

```python
import uuid
from flask import Flask, request, jsonify
from rag import rag
import db

app = Flask(__name__)

@app.route("/question", methods=["POST"])
def handle_question():
    data = request.json
    question = data["question"]

    if not question:
        return jsonify({"error": "No question provided"}), 400

    conversation_id = str(uuid.uuid4())
    answer_data = rag(question)

    db.save_conversation(
        conversation_id=conversation_id,
        question=question,
        answer_data=answer_data,
    )

    result = {
        "conversation_id": conversation_id,
        "question": question,
        "answer": answer_data["answer"],
    }

    return jsonify(result)
```

Add a feedback endpoint:

```python
@app.route("/feedback", methods=["POST"])
def handle_feedback():
    data = request.json
    conversation_id = data["conversation_id"]
    feedback = data["feedback"]

    if not conversation_id or feedback not in [1, -1]:
        return jsonify({"error": "Invalid input"}), 400

    db.save_feedback(
        conversation_id=conversation_id,
        feedback=feedback,
    )

    return jsonify({"message": f"Feedback received: {feedback}"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
```

Install the database driver:

```bash
uv add psycopg2-binary
```

## Docker Compose

Create a `docker-compose.yaml` with three services:

```yaml
services:
  postgres:
    image: postgres:16
    environment:
      POSTGRES_DB: fitness_assistant
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  app:
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      - POSTGRES_HOST=postgres
      - POSTGRES_DB=fitness_assistant
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    ports:
      - "5000:5000"
    depends_on:
      - postgres

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    depends_on:
      - postgres

volumes:
  postgres_data:
```

Dockerfile using uv:

```dockerfile
FROM python:3.14-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
ENV PATH="/app/.venv/bin:$PATH"

COPY pyproject.toml uv.lock .python-version ./
RUN uv sync --locked

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
```

The `.env` file:

```env
OPENAI_API_KEY=your-key-here
```

Start everything:

```bash
docker compose up -d
```

Initialize the database:

```bash
uv run python -c "import db; db.init_db()"
```

Access the app at `http://localhost:5000` and Grafana at
`http://localhost:3000`.

## Grafana dashboards

Create the same dashboards from module 05 using SQL queries against
the `conversations` and `feedback` tables. To automate provisioning,
write a script that calls the Grafana API. The script creates the
PostgreSQL data source and loads a dashboard JSON file.

The final project includes an automated `init.py` script for
this in the `grafana/` directory.

[← Interface and Ingestion Pipeline](04-interface.md) | [Summary and Closing Remarks →](06-summary.md)
