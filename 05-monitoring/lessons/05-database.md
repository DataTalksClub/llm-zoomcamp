# Storing Data in PostgreSQL

Video: [Watch this lesson](https://www.youtube.com/watch?v=iXRu_AbMtuU&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

The metrics disappear when we close the app, so we need somewhere to
keep them. We store every conversation in PostgreSQL, which we run only
for monitoring. No other part of the system touches this database. We
pick Postgres for two reasons: it handles structured data well, and
Grafana connects to it easily later on.

## Starting PostgreSQL with Docker

First we create a Docker network. Postgres and Grafana both run in
containers, and Grafana reaches Postgres by name, so they need to share
a network.

Create the network:

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

If the commands feel opaque, paste them into ChatGPT and ask it to walk
you through each flag. The first module of our
[data-engineering-zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp)
goes deeper into Docker if you want the longer version.

These are long commands we'll run again and again, so they go in the
`Makefile` from lesson 02. The `postgres` target depends on `network`,
so `make postgres` creates the network first and then starts the
container.

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


To reach Postgres from Python, we install the `psycopg` driver:

```bash
uv add "psycopg[binary]"
```

## Initializing the database

The table stores everything from our `LLMCallRecord`, plus the question
and the course. I call it `conversations`, which isn't the best name. I
carried it over from materials I recorded a couple of years ago.
Something like `llm_call_records` would describe it better, but the name
stuck. Name yours however you like.

Two fields are worth a word. We store the `course` because the same
assistant can serve more than one course. Right now everything is
`llm-zoomcamp`, but keeping the column means we don't have to reshape the
table when we add others. The `timestamp` is timezone-aware
(`TIMESTAMP WITH TIME ZONE`) on purpose. Without the time zone, Grafana
won't line the data up correctly on its time axis later.

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

The init function creates the table. With `drop=True` it drops the table
first, which wipes all existing data. That's handy while we're still
changing the schema and want a clean start. But be careful with it. You
never want to run a drop against a real database by accident.

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

We run this once and don't add it to the `Makefile`. The `postgres`
container uses a named volume (`pgdata`), so the data survives restarts.
The table is still there next time we start Postgres. We only run
`db_init.py` again when we change the schema.

## Saving conversations

We want to insert an `LLMCallRecord` into the `conversations` table. The
`id` column is a `SERIAL`, so Postgres assigns it automatically. We add
`RETURNING id` to get that value back, because we need it later. When a
user rates an answer, we have to know which conversation the feedback
belongs to.

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

We pass `question` in separately rather than reading it off the record.
The record's `prompt` is the full text we send to the model, specific to
how we call the LLM. The raw question the user typed is a different
thing. We want it in its own column so we always know what was actually
asked. You could fold the question into the prompt instead, but here we
keep them apart.

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

Every question and answer is now saved to PostgreSQL. Next we query the
data to pull recent conversations back out.

[← Capturing Metrics](04-metrics.md) | [Querying Data →](06-querying.md)
