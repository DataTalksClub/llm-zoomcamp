# User Feedback

Video: [Watch this lesson](https://www.youtube.com/watch?v=GEifsHDadBw&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

So far we capture execution metrics like response time, tokens, and
cost. But none of that tells us whether the answer was any good. The
people using the system know, the way you can rate a reply in ChatGPT. So
we add thumbs-up and thumbs-down buttons, then record what people click.

This feedback is worth collecting beyond the dashboard. It feeds back
into evaluation. If a user marks an answer as good, the judge you built
in the previous module should ideally agree. That agreement gives you
data to align the judge against.

The signal is noisy. Someone clicks by accident, or rates a bad answer as
good (I do it myself in the demo). But it's still valuable for building an
evaluation dataset. And on the dashboard, a wave of thumbs-down in the
last hour is a clear sign. Go check what broke.

## Feedback table

Feedback can come from a person or, later, from an LLM judge. So we use
one feedback table with a `source` column that records where each row
came from. For now `source` is `"user"` and we store a score.

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

We already save conversations in `app.py` from lesson 05. To attach
feedback to the right answer, we need the `conversation_id` that
`save_conversation` returns. We keep it in `st.session_state`. Streamlit
reruns the whole script on every click. Session state is how we carry the
id from the answer to the button press.

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

Now people can rate each answer. We show the buttons all the time rather
than only after a response. It would be cleaner to reveal them once the
answer is in. But that adds logic I'd rather keep out of this small app.
If you want it, ask a coding assistant to gate the buttons on having an
answer.

Next we add a second source of feedback to the same table. An LLM judge
scores answers automatically, without waiting for anyone to click.

[← Streamlit Dashboard](07-streamlit-dashboard.md) | [Built-in Judge →](09-built-in-judge.md)
