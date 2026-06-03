# Capturing Metrics

Right now our chat app works, but we have no visibility into what's
happening. We don't know how long responses take, how many tokens
we're using, or how much each call costs.

Let's fix that by instrumenting the RAG pipeline.

Create `metrics.py`.

Imports:

```python
import time
from dataclasses import dataclass, field
from datetime import datetime

from rag_helper import RAGBase
```

A dataclass to store all the details of each call:

```python
@dataclass
class LLMCallRecord:
    model: str
    prompt: str
    instructions: str
    answer: str
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    response_time: float
    cost: float
    timestamp: datetime = field(default_factory=datetime.now)
```

## Cost calculation

A function to calculate the cost of an LLM call:

```python
def calculate_cost(model, usage):
    cost = 0
    if "gpt-5.4-mini" in model:
        cost = (usage.input_tokens * 0.15 + usage.output_tokens * 0.60) / 1_000_000
    return cost
```

## Instrumented RAG

Now we create a subclass of `RAGBase` that captures metrics
automatically. This way we don't have to instrument each LLM call by
hand. Every time `rag()` calls the LLM internally, the metrics are
recorded.

The same approach works for agentic workflows too. Just capture tool
calls the same way we did in the evaluations module.

Also in `metrics.py`, the subclass that captures metrics:

```python
class RAGWithMetrics(RAGBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_call: LLMCallRecord = None

    def llm(self, prompt):
        start_time = time.time()
        response = self._call_llm(prompt)
        response_time = time.time() - start_time
        self._log_response(prompt, response, response_time)
        return response.output_text
```

The `_call_llm` method sends the request to the LLM:

```python
    def _call_llm(self, prompt):
        input_messages = [
            {"role": "developer", "content": self.instructions},
            {"role": "user", "content": prompt}
        ]
        response = self.llm_client.responses.create(
            model=self.model,
            input=input_messages
        )
        return response
```

The `_log_response` method captures all the metrics:

```python
    def _log_response(self, prompt, response, response_time):
        usage = response.usage
        cost = calculate_cost(self.model, usage)

        call_record = LLMCallRecord(
            model=self.model,
            prompt=prompt,
            instructions=self.instructions,
            answer=response.output_text,
            prompt_tokens=usage.input_tokens,
            completion_tokens=usage.output_tokens,
            total_tokens=usage.total_tokens,
            response_time=response_time,
            cost=cost,
        )
    
        print(call_record)
        self.last_call = call_record
```

Now update `assistant.py` to import `RAGWithMetrics` instead of `RAGBase`:

```python
import sys

from dotenv import load_dotenv
from openai import OpenAI

from ingest import load_faq_data, build_index
from metrics import RAGWithMetrics

def create_assistant():
    load_dotenv()

    documents = load_faq_data()
    index = build_index(documents)

    return RAGWithMetrics(
        index=index,
        llm_client=OpenAI()
    )
```

## Updating the Streamlit app

`app.py` doesn't need changes - it still calls `create_assistant()` and
`assistant.rag()`.

But now we can also display the metrics:

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
```

Run the app again:

```bash
make chat
```

Now you can see response time, token usage, and cost for each answer.

In the next lesson, we'll save these records to a database so we can
track usage over time.

[← Chat App](03-chat-app.md) | [Storing Data in PostgreSQL →](05-database.md)
