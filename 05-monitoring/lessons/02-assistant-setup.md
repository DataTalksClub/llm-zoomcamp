# Assistant

We need a RAG pipeline that can answer questions about our courses.

Let's set it up step by step.

## Setting up

We'll use helper files from module 01. If you don't have them,
download them:

```bash
PREFIX=https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main

wget ${PREFIX}/01-agentic-rag/code/ingest.py
wget ${PREFIX}/01-agentic-rag/code/rag_helper.py
```

## Creating the assistant

Create `assistant.py`.

```makefile
run:
	uv run python assistant.py
```

Now we can run:

```bash
make run
```

We'll add more targets for repeated actions as we go.

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

Since we'll run this often, add it to the `Makefile`:

```makefile
run:
	uv run python assistant.py
```

Now we can run:

```bash
make run
```

Or with a custom question:

```bash
uv run python assistant.py "How do I join the course?"
```

You should see an answer printed to the console. In the next lesson,
we'll wrap this in a Streamlit app.

[← Monitoring](01-intro.md) | [Chat App →](02-chat-app.md)
