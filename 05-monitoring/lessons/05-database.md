# Storing Data in PostgreSQL

Right now the metrics are lost when we close the app. We need to store
every conversation so we can track usage over time and build
dashboards. PostgreSQL is a good choice: it handles structured data
well and integrates with Grafana.

## Starting PostgreSQL with Docker

First, create a Docker network so that later Grafana can connect to
PostgreSQL:

```bash
docker network create monitoring
```

Start PostgreSQL with a volume for data persistence and connect it to
the network:

```bash
docker run -it \
    --name course-assistant-pg \
    --network monitoring \
    -e POSTGRES_USER=user \
    -e POSTGRES_PASSWORD=password \
    -e POSTGRES_DB=course_assistant \
    -p 5432:5432 \
    -v pgdata:/var/lib/postgresql/data \
    postgres:17
```

We'll be running this a lot, so let's add it to the `Makefile` we
created in lesson 02.

Add these targets:

```makefile
network:
	docker network create monitoring

postgres: network
	docker run -it \
		--name course-assistant-pg \
		--network monitoring \
		-e POSTGRES_USER=user \
		-e POSTGRES_PASSWORD=password \
		-e POSTGRES_DB=course_assistant \
		-p 5432:5432 \
		-v pgdata:/var/lib/postgresql/data \
		postgres:17
```

Now we can just run:

```bash
make postgres
```


We need `psycopg` to connect to PostgreSQL from Python:

```bash
uv add "psycopg[binary]"
```

## Initializing the database

The `conversations` table stores everything from our `LLMCallRecord`
plus the question and course. We use timezone-aware timestamps
(`TIMESTAMP WITH TIME ZONE`) - this matters for Grafana dashboards
later.

The SQL to create the table:

```sql
CREATE TABLE conversations (
    id SERIAL PRIMARY KEY,
    question TEXT NOT NULL,
    answer TEXT NOT NULL,
    course TEXT NOT NULL,
    model TEXT NOT NULL,
    instructions TEXT NOT NULL,
    prompt TEXT NOT NULL,
    prompt_tokens INTEGER NOT NULL,
    completion_tokens INTEGER NOT NULL,
    total_tokens INTEGER NOT NULL,
    response_time FLOAT NOT NULL,
    cost FLOAT NOT NULL,
    timestamp TIMESTAMP WITH TIME ZONE NOT NULL
)
```

We can run this via `psql` or any other tool, but let's create a
Python script.


Create `db_init.py`.

Imports:

```python
import os
import psycopg
from datetime import datetime

DB_TIMEZONE = datetime.now().astimezone().tzinfo
print(f"Using timezone: {DB_TIMEZONE}")
```

A helper to connect to the database.

It uses environment variables with defaults matching the Docker
container we just started:

```python
def get_db_connection():
    return psycopg.connect(
        host=os.getenv("POSTGRES_HOST", "localhost"),
        dbname=os.getenv("POSTGRES_DB", "course_assistant"),
        user=os.getenv("POSTGRES_USER", "user"),
        password=os.getenv("POSTGRES_PASSWORD", "password"),
    )
```

The init function creates the table.

With `drop=True` it drops the table first, which deletes all
existing data:

```python
def init_db(drop=False):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            if drop:
                cur.execute("DROP TABLE IF EXISTS conversations")

            cur.execute("""
                CREATE TABLE conversations (
                    id SERIAL PRIMARY KEY,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL,
                    course TEXT NOT NULL,
                    model TEXT NOT NULL,
                    instructions TEXT NOT NULL,
                    prompt TEXT NOT NULL,
                    prompt_tokens INTEGER NOT NULL,
                    completion_tokens INTEGER NOT NULL,
                    total_tokens INTEGER NOT NULL,
                    response_time FLOAT NOT NULL,
                    cost FLOAT NOT NULL,
                    timestamp TIMESTAMP WITH TIME ZONE NOT NULL
                )
            """)
        conn.commit()
    finally:
        conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized")
```

Run the init script:

```bash
uv run python db_init.py
```

## Saving conversations

We want to insert an `LLMCallRecord` into the `conversations` table.

The SQL we want to execute:

```sql
INSERT INTO conversations (
    question, answer, course, model, instructions, prompt,
    prompt_tokens, completion_tokens, total_tokens,
    response_time, cost, timestamp
) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
)
RETURNING id
```

Create `db_save.py`.

Imports:

```python
from datetime import datetime
from db_init import get_db_connection, DB_TIMEZONE
```

The save function takes an `LLMCallRecord` and inserts it into the
database:

```python
def save_conversation(record, question, course):
    timestamp = datetime.now(DB_TIMEZONE)

    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO conversations (
                    question, answer, course, model, instructions, prompt,
                    prompt_tokens, completion_tokens, total_tokens,
                    response_time, cost, timestamp
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                )
                RETURNING id
                """,
                (
                    question,
                    record.answer,
                    course,
                    record.model,
                    record.instructions,
                    record.prompt,
                    record.prompt_tokens,
                    record.completion_tokens,
                    record.total_tokens,
                    record.response_time,
                    record.cost,
                    timestamp,
                ),
            )
            conversation_id = cur.fetchone()[0]
        conn.commit()
    finally:
        conn.close()
    return conversation_id
```

We can also add it to the `__main__` block in `assistant.py` so every
CLI test gets saved.

Add this import at the top of `assistant.py`:

```python
from db_save import save_conversation
```

Then add the save call after the answer in the `__main__` block:

```python
save_conversation(assistant.last_call, query, "llm-zoomcamp")
```

Test it:

```bash
uv run python assistant.py "How do I join the course?"
```

Check the data:

```bash
docker exec -it course-assistant-pg psql -U user -d course_assistant \
    -c "SELECT id, question, response_time, cost FROM conversations;"
```

## Integrating with Streamlit

In `app.py`, just add the import and one line after `assistant.rag()`:

```python
from db_save import save_conversation
```

And later:

```python
answer = assistant.rag(user_input)
st.success("Completed!")
st.write(answer)

record = assistant.last_call
st.write(f"Response time: {record.response_time:.2f}s")
st.write(f"Prompt tokens: {record.prompt_tokens}")
st.write(f"Completion tokens: {record.completion_tokens}")
st.write(f"Cost: ${record.cost:.4f}")

conversation_id = save_conversation(record, user_input, "llm-zoomcamp")
st.session_state.conversation_id = conversation_id
```

That's it - every question and answer is now saved to PostgreSQL. In the next
lesson, we'll query the data to see recent conversations.

[← Capturing Metrics](04-metrics.md) | [Querying Data →](06-querying.md)
