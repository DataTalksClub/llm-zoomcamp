# Capturing Metrics

Video: [Watch this lesson](https://www.youtube.com/watch?v=JGh6-DqaueA&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

Our chat app works, but every call is a black box. We don't know how
long it took, how many tokens it used, or what it cost. To monitor the
system, we first have to capture those numbers as they happen. So we
instrument the RAG pipeline.

Create `metrics.py`.

Imports:

```python
import time
from dataclasses import dataclass, field
from datetime import datetime

from rag_helper import RAGBase
```

Every call produces a bundle of values we want to keep together. We
could pass them around as a dictionary, but then you have to remember
what keys are in it. A dataclass spells the fields out, so anyone reading
the code can see what we record for each call.

The `LLMCallRecord` dataclass:

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

Next we need the cost of each call. The provider charges a price per
million input tokens and another per million output tokens. So we
multiply each count by its rate and divide by a million. The `usage`
object comes straight from the LLM response. It carries the token counts
for the call we just made.

```python
def calculate_cost(model, usage):
    cost = 0
    if "gpt-5.4-mini" in model:
        cost = (usage.input_tokens * 0.15 + usage.output_tokens * 0.60) / 1_000_000
    return cost
```

I keep copy-pasting a version of this function across modules, which
isn't the tidiest thing in the world. For a real project you'd pull it
into one shared place, but here it keeps each lesson self-contained.

## Instrumented RAG

`RAGBase` already works, and I like carrying it around as-is because it
keeps things simple. So instead of rewriting it, we subclass it and only
change the one method that calls the LLM. Everything else stays the same,
and every time `rag()` makes a call, the metrics get recorded for free.

The same trick works for agents. You'd capture each tool call the same
way we captured LLM calls in the evaluation module.

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

The `_log_response` method builds the record and stashes it on
`self.last_call`. Keeping state on the object isn't the cleanest design.
If two things called it at once, they'd fight over `last_call`.

But it lets us read the metrics back without changing the method's return
type. For one person clicking through a Streamlit app, that's good
enough. We also print the record so we can see what we're capturing.

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

Now you can see response time, token usage, and cost under each answer.
It isn't a pretty panel, but it shows the numbers we care about. One
naming note: I call these `prompt_tokens` and `completion_tokens` to
follow the API. The names `input_tokens` and `output_tokens` read more
clearly, so feel free to rename them in your own version.

We capture the metrics now, but they vanish the moment we close the app.
Next we save each record to a database so we can track usage over time.

[← Chat App](03-chat-app.md) | [Storing Data in PostgreSQL →](05-database.md)
