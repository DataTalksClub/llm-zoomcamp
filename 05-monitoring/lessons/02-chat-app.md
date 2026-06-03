# Chat App

We need a user interface where people can ask questions and see
answers. Streamlit is a Python framework that makes it easy to build
web apps with minimal code.

Let's build a chat app that:

- Lets the user select a course and ask a question
- Runs the RAG pipeline and shows the answer

## Setting up the RAG pipeline

First, the RAG pipeline.

We'll use helper files from module 01.

If you don't have them, download them:

```bash
PREFIX=https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main

wget ${PREFIX}/01-agentic-rag/code/ingest.py
wget ${PREFIX}/01-agentic-rag/code/rag_helper.py
```

Create `assistant.py`.

Imports:

```python
import sys

from rag_helper import RAGBase
from ingest import load_faq_data, build_index
from openai import OpenAI
```

Instructions for the LLM:

```python
INSTRUCTIONS = """
You're a course teaching assistant.
Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.
""".strip()
```

A function to create the assistant:

```python
def create_assistant():
    documents = load_faq_data()
    index = build_index(documents)

    return RAGBase(
        index=index,
        llm_client=OpenAI(),
        instructions=INSTRUCTIONS,
    )
```

Test it from the command line:

```python
if __name__ == "__main__":
    assistant = create_assistant()

    query = "How do I join the course?"
    if len(sys.argv) > 1:
        query = sys.argv[1]

    answer = assistant.rag(query)
    print(answer)
```

Run the assistant:

```bash
uv run python assistant.py
```

Or with a custom question:

```bash
uv run python assistant.py "How do I join the course?"
```

## Building the Streamlit app

Add Streamlit to your project:

```bash
uv add streamlit
```

Now the Streamlit interface - put this in `app.py`:

```python
import streamlit as st
from assistant import create_assistant

assistant = create_assistant()

st.title("Course Assistant")

user_input = st.text_input("Enter your question:")

if st.button("Ask"):
    with st.spinner("Processing..."):
        answer = assistant.rag(user_input)
        st.success("Completed!")
        st.write(answer)
```

Run the app:

```bash
uv run streamlit run app.py
```

You should see a web interface where you can ask questions and see
the answer.

Right now we don't track anything - no response time, no token usage,
no cost. In the next lesson, we'll add metrics capture to monitor the
LLM calls.

[← Monitoring](01-intro.md) | [Capturing Metrics →](03-metrics.md)
