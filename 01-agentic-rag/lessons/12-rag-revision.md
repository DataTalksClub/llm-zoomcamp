# Quick RAG Revision

Before we talk about agents, let's set up the RAG pipeline from module
1.

We'll use two helpers that we defined previously in [module 1](../../01-rag/):

- [`rag_helper.py`](../../01-rag/code/rag_helper.py) - the `RAGBase` class wrapping search, prompt building, and the LLM call
- [`ingest.py`](../../01-rag/code/ingest.py) - `load_faq_data` and `build_index` for loading the FAQ and building a minsearch index

Let's download them:

```bash
wget https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/01-rag/code/rag_helper.py
wget https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/01-rag/code/ingest.py
```

## Setting up RAG

Set up the OpenAI client:

```python
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_client = OpenAI()
```

Load the data and build the search index:

```python
from rag_helper import RAGBase
from ingest import load_faq_data, build_index

documents = load_faq_data()
index = build_index(documents)
```

Create the assistant:

```python
instructions = """
You're a course teaching assistant.
Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.
""".strip()

assistant = RAGBase(
    index=index,
    llm_client=openai_client,
    instructions=instructions,
)
```

## Testing it

Let's try a question:

```python
assistant.rag('How do I run Ollama locally?')
```

This should work fine. The search finds relevant FAQ entries about
Ollama, and the LLM gives a good answer.

Try something slightly different:

```python
assistant.rag('How do I run Olama locally?')
```

The word "Olama" doesn't match "Ollama" in our index. The search
returns poor results - maybe some unrelated documents about other
topics. The LLM gets these bad results and either says "I don't know"
or tries to answer with irrelevant information.

This is the limitation of a fixed pipeline. The search runs once with
the exact query the user typed. There's no second chance. The pipeline
can't adapt - it doesn't know the search failed, and it can't try
again with a corrected query.

We need something smarter. We need an agent.

[← Introduction](01-intro.md) | [Function Calling →](03-function-calling.md)
