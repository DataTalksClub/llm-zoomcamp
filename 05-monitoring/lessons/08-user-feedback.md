# User Feedback

We track LLM calls and costs, but we don't know if users find the
answers helpful. Let's add thumbs up/down buttons to collect feedback.

## Feedback table

We create a generic feedback table where the `source` column tells us
where the feedback came from. For now we use `source="user"` with a score.

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
from db_init import get_db_connection, DB_TIMEZONE

def save_feedback(conversation_id, source, relevance=None,
                  explanation=None, score=None):
    timestamp = datetime.now(DB_TIMEZONE)

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

We already save conversations in `app.py` from lesson 05. Now we need
to capture the `conversation_id` returned by `save_conversation` and
add feedback buttons.

Add this import to `app.py`:

```python
from db_feedback import save_feedback
```

Update the ask button to save the conversation ID:

```python
if st.button("Ask"):
    with st.spinner("Processing..."):
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

Now add the feedback buttons:

```python
col1, col2 = st.columns(2)
with col1:
    if st.button("+1"):
        cid = st.session_state.conversation_id
        save_feedback(cid, "user", score=1)
        st.write("Thanks!")

with col2:
    if st.button("-1"):
        cid = st.session_state.conversation_id
        save_feedback(cid, "user", score=-1)
        st.write("Thanks for the feedback!")
```

Now users can rate each answer. In the next lesson, we'll add an
LLM judge that uses the same feedback table.

[← Streamlit Dashboard](07-streamlit-dashboard.md) | [Built-in Judge →](09-built-in-judge.md)
