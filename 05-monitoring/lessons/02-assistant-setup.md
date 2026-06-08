# Assistant

Video: [Watch this lesson](https://www.youtube.com/watch?v=jMO8rqPmR-4&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

Before we monitor anything, we need something to monitor. So we start
with a RAG pipeline that answers questions about our courses.

We won't build it from scratch. We already did that in the earlier
modules, and the flow is the same three steps as always.

First we search the FAQ for the questions most relevant to the user's
question. Then we build a prompt from that question plus the documents we
found. Finally we send it to the LLM, which gives us the answer. That's
the whole pipeline, and we reuse it as-is.

## Setting up

Two helper files carry that pipeline. `ingest.py` downloads the FAQ
dataset and builds a search index over it, and `rag_helper.py` has the
`RAGBase` class that does the search-prompt-answer loop.

If you don't have them, download them:

```bash
PREFIX=https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main

wget ${PREFIX}/01-agentic-rag/code/ingest.py
wget ${PREFIX}/01-agentic-rag/code/rag_helper.py
```

Add dependencies:

```bash
uv add python-dotenv
```

We use `python-dotenv` to load the `OPENAI_API_KEY` from a `.env` file.

## Creating the assistant

Now we pull those two helpers together into one place. `assistant.py`
loads the data and builds the index, then hands both to `RAGBase`. We
don't pass our own instructions here. `RAGBase` already comes with a
system prompt telling the model to answer course questions. A second one
would be redundant.

Create `assistant.py`.

Imports:

```python
import sys

from dotenv import load_dotenv
from openai import OpenAI

from ingest import load_faq_data, build_index
from rag_helper import RAGBase
```

A function to create the assistant:

```python
def create_assistant():
    load_dotenv()

    documents = load_faq_data()
    index = build_index(documents)

    return RAGBase(
        index=index,
        llm_client=OpenAI(),
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

We'll run this command again and again, and typing it in full every time
gets old. So we put it in a `Makefile`.

Add a `run` target:

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

You should see an answer printed to the console. Running it from the
command line is fine for us, but it's not how a user would reach it.
Next we put a simple interface in front of it with Streamlit.

[← Intro](01-intro.md) | [Chat App →](03-chat-app.md)
