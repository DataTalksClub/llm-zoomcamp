# Built-in Judge

In module 04, we used LLM-as-a-judge for offline evaluation. We can
use the same approach online. After each answer, ask an LLM to evaluate
whether the answer is relevant to the question.

Now we have an automatic relevance signal without waiting for user
feedback.

## Adding relevance evaluation

We use structured output to get a clean classification from the judge.

We need `evaluation_utils` from module 04. Download it if you don't
have it:

```bash
PREFIX=https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main
wget ${PREFIX}/04-evaluation/code/evaluation_utils.py
```

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


The evaluation function. Add this to `judge.py`:

```python
def evaluate_relevance(question, answer, client=None):
    if client is None:
        client = OpenAI()

    prompt = judge_prompt.format(question=question, answer=answer)

    result, usage = llm_structured_retry(
        client,
        judge_instructions,
        prompt,
        RelevanceVerdict,
    )

    return result.relevance, result.explanation
```

Test it:

```python
if __name__ == "__main__":
    question = "Can I still join the course?"
    answer = "Yes, you can still join. The course is self-paced."

    relevance, explanation = evaluate_relevance(question, answer)
    print(relevance)
    print(explanation)
```

```bash
uv run python judge.py
```

## Saving judge feedback to the database

We already created the `feedback` table in lesson 09. It has a
`source` column that tells us where the feedback came from.

We already have `db_feedback.py` with `save_feedback`. We just need
to call it with `source="judge"`.

## Integrating with the app

In `app.py`, call the judge after getting the answer and save it:

```python
from judge import evaluate_relevance
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

[← User Feedback](09-user-feedback.md) | [Synthetic Data →](11-synthetic-data.md)
