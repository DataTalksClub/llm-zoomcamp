# Chat App with Feedback

We need a user interface where people can ask questions and give
feedback on the answers. Streamlit is a Python framework that makes it
easy to build web apps with minimal code.

Let's build a chat app that:

- Lets the user select a course and ask a question
- Runs the RAG pipeline and shows the answer
- Has thumbs up / thumbs down buttons for feedback

## Setting up the RAG pipeline

First, the RAG pipeline.

We use the `RAGBase` class from module 01:

```python
from rag_helper import RAGBase, load_faq_data
from minsearch import Index
from openai import OpenAI

documents = load_faq_data()

index = Index(
    text_fields=["question", "section", "answer"],
    keyword_fields=["course"]
)
index.fit(documents)

INSTRUCTIONS = """
You're a course teaching assistant.
Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.
""".strip()

assistant = RAGBase(
    index=index,
    llm_client=OpenAI(),
    instructions=INSTRUCTIONS,
)
```

For monitoring, we need to track response time and token usage.

We create a subclass of `RAGBase` that captures these metrics
automatically. This way we don't have to instrument each LLM call by
hand. Every time `rag()` calls the LLM internally, the metrics are
recorded.

```python
import time

class RAGWithMetrics(RAGBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last_response_time = None
        self.last_tokens = None

    def llm(self, prompt):
        start_time = time.time()

        input_messages = [
            {"role": "developer", "content": self.instructions},
            {"role": "user", "content": prompt}
        ]
        response = self.llm_client.responses.create(
            model=self.model,
            input=input_messages
        )

        self.last_response_time = time.time() - start_time
        self.last_tokens = {
            "prompt_tokens": response.usage.input_tokens,
            "completion_tokens": response.usage.output_tokens,
            "total_tokens": response.usage.total_tokens
        }

        return response.output_text
```

Use the subclass instead of `RAGBase`:

```python
assistant = RAGWithMetrics(
    index=index,
    llm_client=OpenAI(),
    instructions=INSTRUCTIONS,
)
```

Now when we call `assistant.rag(question)`, the metrics are available
as `assistant.last_response_time` and `assistant.last_tokens`.

The main function that ties it together:

```python
def calculate_cost(model, tokens):
    cost = 0
    if "gpt-5.4-mini" in model:
        cost = (tokens["prompt_tokens"] * 0.15 + tokens["completion_tokens"] * 0.60) / 1_000_000
    return cost

def get_answer(query, course):
    answer = assistant.rag(query)

    openai_cost = calculate_cost(assistant.model, assistant.last_tokens)

    return {
        "answer": answer,
        "response_time": assistant.last_response_time,
        "model_used": assistant.model,
        "prompt_tokens": assistant.last_tokens["prompt_tokens"],
        "completion_tokens": assistant.last_tokens["completion_tokens"],
        "total_tokens": assistant.last_tokens["total_tokens"],
        "openai_cost": openai_cost,
    }
```

## Building the Streamlit app

Add Streamlit to your project:

```bash
uv add streamlit
```

Now the Streamlit interface:

```python
import streamlit as st
from assistant import get_answer

st.title("Course Assistant")

course = st.selectbox(
    "Select a course:",
    ["data-engineering-zoomcamp", "machine-learning-zoomcamp", "mlops-zoomcamp", "llm-zoomcamp"],
)

user_input = st.text_input("Enter your question:")

if st.button("Ask"):
    with st.spinner("Processing..."):
        answer_data = get_answer(user_input, course)
        st.success("Completed!")
        st.write(answer_data["answer"])

        st.write(f"""Response time: {answer_data["response_time"]:.2f}s""")
```

Run the app:

```bash
uv run streamlit run app.py
```

You should see a web interface where you can ask questions and see the
answer with response time and token usage.

In the next lesson, we'll add persistence to save conversations and
feedback to a database.

[← Monitoring](01-intro.md) | [Storing Data in PostgreSQL →](03-database.md)
