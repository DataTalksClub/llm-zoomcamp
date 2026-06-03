# User Feedback

We track LLM calls and costs, but we don't know if users find the
answers helpful. Let's add thumbs up/down buttons to collect feedback.

## Feedback table

Create a generic feedback table. The `source` column tells us where
the feedback came from. For now we use `source="user"` with a score.

Add a new function `init_feedback` to `db_init.py`:

```python
def init_feedback():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS feedback")

            cur.execute("""
                CREATE TABLE feedback (
                    id SERIAL PRIMARY KEY,
                    conversation_id INTEGER REFERENCES conversations(id),
                    source TEXT NOT NULL,
                    relevance TEXT,
                    explanation TEXT,
                    score INTEGER,
                    timestamp TIMESTAMP WITH TIME ZONE NOT NULL
                )
            """)
        conn.commit()
    finally:
        conn.close()
```

Update the `__main__` block to call both:

```python
if __name__ == "__main__":
    init_db()
    init_feedback()
    print("Database initialized")
```

Re-run the init script:

```bash
uv run python db_init.py
```

- `source`: `"user"` for human feedback, `"judge"` for LLM evaluations
- `score`: +1 for thumbs up, -1 for thumbs down
- `relevance` and `explanation`: will be used later by the built-in judge

## Saving feedback

Create `db_feedback.py`:

```python
from datetime import datetime
from db_init import get_db_connection

tz = datetime.now().astimezone().tzinfo

def save_feedback(conversation_id, source, relevance=None,
                  explanation=None, score=None):
    timestamp = datetime.now(tz)

    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO feedback (
                    conversation_id, source, relevance,
                    explanation, score, timestamp
                ) VALUES (
                    %s, %s, %s, %s, %s, %s
                )
                """,
                (conversation_id, source, relevance,
                 explanation, score, timestamp),
            )
        conn.commit()
    finally:
        conn.close()
```

## Adding buttons to the app

Update `app.py` to show thumbs up/down buttons:

```python
from db_feedback import save_feedback

if st.button("Ask"):
    with st.spinner("Processing..."):
        assistant.rag(user_input)
        record = assistant.last_call
        save_conversation(record, user_input, "llm-zoomcamp")

        st.success("Completed!")
        st.write(record.answer)

        st.write(f"Response time: {record.response_time:.2f}s")
        st.write(f"Cost: ${record.cost:.4f}")

        st.session_state.last_conversation_id = record.id
```

Wait, `record.id` is from `LLMCallRecord` which doesn't have an `id`
field. We need the database row ID. Let's update `save_conversation`
to return it:

```python
def save_conversation(record, question, course):
    timestamp = datetime.now(tz)

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
                (...),
            )
            conversation_id = cur.fetchone()[0]
        conn.commit()
    finally:
        conn.close()
    return conversation_id
```

Now the feedback buttons:

```python
col1, col2 = st.columns(2)
with col1:
    if st.button("+1"):
        cid = st.session_state.last_conversation_id
        save_feedback(cid, "user", score=1)
        st.write("Thanks!")

with col2:
    if st.button("-1"):
        cid = st.session_state.last_conversation_id
        save_feedback(cid, "user", score=-1)
        st.write("Thanks for the feedback!")
```

Now users can rate each answer. In the next lesson, we'll add an
LLM judge that uses the same feedback table.

[← Streamlit Dashboard](06-streamlit-dashboard.md) | [Built-in Judge →](08-built-in-judge.md)
