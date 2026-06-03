# Built-in Judge

In module 04, we used LLM-as-a-judge for offline evaluation. We can use
the same approach online: after each answer, ask an LLM to evaluate
whether the answer is relevant to the question.

This gives us an automatic relevance signal without waiting for user
feedback.

## Adding relevance evaluation

We use structured output to get a clean classification from the judge:

```python
import json
from pydantic import BaseModel
from typing import Literal
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

The evaluation function:

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

## Integrating with the app

Update `get_answer` to include the judge evaluation:

```python
def get_answer(query, course):
    answer = assistant.rag(query)
    openai_cost = calculate_cost(assistant.model, assistant.last_tokens)

    relevance, relevance_explanation = evaluate_relevance(query, answer)

    return {
        "answer": answer,
        "response_time": assistant.last_response_time,
        "relevance": relevance,
        "relevance_explanation": relevance_explanation,
        "model_used": assistant.model,
        "prompt_tokens": assistant.last_tokens["prompt_tokens"],
        "completion_tokens": assistant.last_tokens["completion_tokens"],
        "total_tokens": assistant.last_tokens["total_tokens"],
        "openai_cost": openai_cost,
    }
```

Update the Streamlit app to show relevance:

```python
if st.button("Ask"):
    with st.spinner("Processing..."):
        answer_data = get_answer(user_input, course)
        st.success("Completed!")
        st.write(answer_data["answer"])

        st.write(f"""Response time: {answer_data["response_time"]:.2f}s""")
        st.write(f"""Relevance: {answer_data["relevance"]}""")
```

Now each answer comes with an automatic relevance label. This is useful
for monitoring: if relevance drops, something is wrong with the search
or the prompt.

The judge adds an extra LLM call per question, which increases cost and
latency. For high-traffic applications, you may want to evaluate only a
sample of answers instead of every one.

[← Storing Data in PostgreSQL](03-database.md) | [Docker Compose →](05-docker-compose.md)
