# Querying Data

Video: [Watch this lesson](https://www.youtube.com/watch?v=18vEtjPJwLc&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

We're saving conversations now, so the next step is reading them back.
That's what the dashboard runs on. Normally I'd open a Jupyter notebook
here and poke at the data first. I'd try a few queries to see what the
rows look like. Our data is small and simple, so we skip that and go
straight to a script.

Create `db_query.py`.

Connect to the same database:

```python
from dataclasses import dataclass

from db_init import get_db_connection
from metrics import LLMCallRecord
```

## Fetching conversations

A query returns each row as a plain tuple. You have to remember that
column 4 is the model and column 6 is the prompt. That's no fun to work
with. So we convert each row back into the `LLMCallRecord` dataclass we
already use for live calls.

A helper to convert a database row into an `LLMCallRecord`:

```python
def row_to_record(row):
    return LLMCallRecord(
        model=row[4],
        prompt=row[6],
        instructions=row[5],
        answer=row[2],
        prompt_tokens=row[7],
        completion_tokens=row[8],
        total_tokens=row[9],
        response_time=row[10],
        cost=row[11],
        timestamp=row[12],
    )
```

Now update `get_conversations` to use it:

```python
def get_conversations(limit=10):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT id, question, answer, course, model,
                       instructions, prompt,
                       prompt_tokens, completion_tokens, total_tokens,
                       response_time, cost, timestamp
                FROM conversations
                ORDER BY timestamp DESC
                LIMIT %s
                """,
                (limit,),
            )
            rows = cur.fetchall()
    finally:
        conn.close()

    return [row_to_record(row) for row in rows]
```

We order by `timestamp` to get the most recent calls. One thing to keep
in mind as the table grows: there's no index on `timestamp`, but there
is one on `id`. Since ids increase over time anyway, ordering by `id`
would be faster - or you add an index on `timestamp`. With a handful of
rows it doesn't matter, so we leave it simple for now.

Test it:

```python
if __name__ == "__main__":
    records = get_conversations()
    for record in records:
        print(record)
```

Run it:

```bash
uv run python db_query.py
```

The output is a wall of text, not something you'd want to read all day.
Still, it proves we can pull the data back out of the database. Now we
put it in front of a dashboard.

[← Storing Data in PostgreSQL](05-database.md) | [Streamlit Dashboard →](07-streamlit-dashboard.md)
