# Built-in Judge

Video: [Watch this lesson](https://www.youtube.com/watch?v=YLOLQyrMDuY&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

In the previous module we used an LLM as a judge for offline evaluation.
One LLM grades the output of another. We can run the same idea online.

After each answer, we ask a judge whether it's relevant to the question.
That gives us an automatic quality signal on every response. We don't
have to wait for anyone to click thumbs up or down.

There's one real difference from the offline setup. Back then we had
ground truth: a reference answer to compare against. The judge could
check our answer against that known-good one. Online we don't have it.

The judge now only sees the question and the answer. It has to make the
call on its own. That's a harder job, so in the instructions we describe
more carefully what a good answer looks like.

## Adding relevance evaluation

We use structured output so the judge returns a clean label instead of
free text we'd have to parse.

We need `evaluation_utils` from module 04.

Download it if you don't have it:

```bash
PREFIX=https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main
wget ${PREFIX}/04-evaluation/code/evaluation_utils.py
```

Create `judge.py`:

```python
import json

from pydantic import BaseModel
from typing import Literal
from openai import OpenAI
from dotenv import load_dotenv

from evaluation_utils import llm_structured_retry

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


The `explanation` field matters even though we don't always do anything
with it. Asking the judge to explain forces it to reason about the answer
before it commits to a label. That tends to make the label better.

We call the judge through `llm_structured_retry`, the helper from the
previous module. It's the same as `llm_structured`, but it retries if
something breaks.

Once in a while a model returns JSON that doesn't quite match the
structure we asked for. It's rare with OpenAI's small models, maybe once
or twice in my experience. It's more common with other providers, where
it might be a handful out of a thousand calls. The retry covers those
cases.

The evaluation function.

Add this to `judge.py`:

```python
def evaluate_relevance(question, answer, client=None):
    if client is None:
        client = OpenAI()

    prompt = judge_prompt.format(
        question=question,
        answer=answer
    )

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
    load_dotenv()

    question = "Can I still join the course?"
    answer = "Yes, you can still join. The course is self-paced."

    relevance, explanation = evaluate_relevance(question, answer)
    print(relevance)
    print(explanation)
```

Run it:

```bash
uv run python judge.py
```

This judge is deliberately basic, so handle its verdicts with care.
Sometimes it'll call a weak answer relevant, or the other way around.
When you build your own, spend time on the prompt until "relevant" means
relevant.

The way to get there is alignment. You collect some labels from your
users, or label a sample yourself. Then you tune the judge until it
agrees with them. The team at Evidently has a good talk on this on our
DataTalks Club channel. Look for
[automated prompt optimization](https://www.youtube.com/watch?v=uMNYVw4jh-8).

## Saving judge feedback to the database

We already created the `feedback` table in lesson 08. It has a
`source` column that tells us where the feedback came from.

We already have `db_feedback.py` with `save_feedback`. We just need
to call it with `source="judge"`.

## Integrating with the app

In `app.py`, call the judge after getting the answer and save it:

```python
from judge import evaluate_relevance
from db_feedback import save_feedback
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

relevance, explanation = evaluate_relevance(user_input, answer)
save_feedback(conversation_id, "judge",
                relevance=relevance, explanation=explanation)
st.write(f"Relevance: {relevance}")
st.write(f"Explanation: {explanation}")
```

Now every answer carries an automatic relevance label. It lands in the
same `feedback` table as the user's thumbs up and down from lesson 08.
Because both are there, we can compare what the judge thinks with what
people think. And if relevance starts dropping on the dashboard,
something is off with the search or the prompt.

A few things to keep in mind for anything beyond a demo:

- The judge is an extra LLM call per question, so it adds latency and
  cost. In a real system you'd run it asynchronously. Return the answer
  to the user first, then score it in the background.
- Track the judge's own cost separately, since it spends money too. A
  `judge_feedback` table with relevance, explanation, and cost would do
  it.
- Once you have real traffic, you don't have to judge every answer.
  Sample, say one in ten, and you still get the signal at a fraction of
  the cost.

Here we run it inline on every call to keep the code simple.

[← User Feedback](08-user-feedback.md) | [Feedback Dashboard →](10-feedback-dashboard.md)
