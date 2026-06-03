# Built-in Judge

In module 04, we used LLM-as-a-judge for offline evaluation. We can
use the same approach online. After each answer, ask an LLM to evaluate
whether the answer is relevant to the question.

Now we have an automatic relevance signal without waiting for user
feedback.

## Adding relevance evaluation

We use structured output to get a clean classification from the judge.

Create `judge.py`:

```python
import json
from pydantic import BaseModel
from typing import Literal
from evaluation_utils import llm_structured_retry
from openai import OpenAI

class RelevanceVerdict(BaseModel):
    relevance: Literal["NON_RELEVANT", "PARTLY_RELEVANT", "RELEVANT"]
    explanation: str

judge_instructions = """
You are an expert evaluator for a RAG system.
Analyze the relevance of the generated answer to the given question.

Classify the answer as:
- RELEVANT: the answer addresses the question
- PARTLY_RELEVANT: the answer partially addresses the question
- NON_RELEVANT: the answer does not address the question
""".strip()

judge_prompt = """
Question: {question}
Generated Answer: {answer}
""".strip()
```

We need `evaluation_utils` from module 04. Download it if you don't
have it:

```bash
PREFIX=https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main
wget ${PREFIX}/04-evaluation/code/evaluation_utils.py
```

The evaluation function. Add this to `metrics.py`:

```python
from openai import OpenAI

openai_client = OpenAI()

def evaluate_relevance(question, answer):
    prompt = judge_prompt.format(question=question, answer=answer)

    result, usage = llm_structured_retry(
        openai_client,
        judge_instructions,
        prompt,
        RelevanceVerdict,
    )

    return result.relevance, result.explanation
```

Test it on one answer:

```python
question = "Can I still join the course?"
answer = "Yes, you can still join. The course is self-paced."

relevance, explanation = evaluate_relevance(question, answer)
print(relevance)
print(explanation)
```

## Saving feedback to the database

Create a generic feedback table that works for both LLM judge
evaluations and user thumbs up/down. The `source` column tells us
where the feedback came from.

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

- `source`: `"judge"` for LLM evaluations, `"user"` for human feedback
- `relevance` and `explanation`: used by the judge
- `score`: used by user feedback (+1 or -1)

Create `db_feedback.py` to save feedback:

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

## Integrating with the app

In `app.py`, call the judge after getting the answer and save it:

```python
from metrics import evaluate_relevance
from db_feedback import save_feedback

        assistant.rag(user_input)
        record = assistant.last_call
        save_conversation(record, user_input, "llm-zoomcamp")

        relevance, explanation = evaluate_relevance(user_input, record.answer)
        save_feedback(record.id, "judge",
                      relevance=relevance, explanation=explanation)
        st.write(f"Relevance: {relevance}")
```

Now each answer comes with an automatic relevance label. This is useful
for monitoring: if relevance drops, something is wrong with the search
or the prompt.

Later we'll also save user feedback (+1/-1) to the same table with
`source="user"` and `score=+1` or `score=-1`. This way we can compare
human judgment with the LLM judge.

The judge adds an extra LLM call per question, which increases cost and
latency. For high-traffic applications, evaluate only a sample of
answers instead of every one.

[← User Feedback](07-user-feedback.md) | [Synthetic Data →](09-synthetic-data.md)
