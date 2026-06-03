# Querying Data

Now that we're saving conversations to PostgreSQL, let's query them.

Create `db_query.py`.

Connect to the same database:

```python
from dataclasses import dataclass

from db_init import get_db_connection
from metrics import LLMCallRecord
```

## Fetching conversations

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

Now you can use the same dataclass for live calls and database results.

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

[← Storing Data in PostgreSQL](05-database.md) | [Streamlit Dashboard →](07-streamlit-dashboard.md)
