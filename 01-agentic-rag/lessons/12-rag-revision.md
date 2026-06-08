# Quick RAG Revision (Optional)

Video: [Watch this lesson](https://www.youtube.com/watch?v=gH8fB-6Emmo&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

Before we talk about agents, let's set up the RAG pipeline we built
in Part 1.

Our courses have a lot of participants. They ask the same questions
over and over, so we keep a FAQ document and point students to it. RAG
takes that FAQ and finds the entry that matches a question. It then
sends the entry to an LLM so it can answer. That way a student gets a
reply right away instead of scrolling through a long document.

We'll use two helpers we defined earlier in this module:

- [`rag_helper.py`](../code/rag_helper.py) - the `RAGBase` class wrapping search, prompt building, and the LLM call
- [`ingest.py`](../code/ingest.py) - `load_faq_data` and `build_index` for loading the FAQ and building a minsearch index

If you're working through Part 2 as a standalone workshop (without
Part 1), download them into your project:

```bash
wget https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/01-agentic-rag/code/rag_helper.py
wget https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/01-agentic-rag/code/ingest.py
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
assistant.rag("How do I run Ollama locally?")
```

This works fine. The search finds relevant FAQ entries about Ollama,
and the LLM gives a good answer.

Now try something slightly different:

```python
assistant.rag("How do I run Olama locally?")
```

The word "Olama" doesn't match "Ollama" in our index. We use lexical
search, so it looks for the exact word and finds nothing. The LLM
gets these bad results and either says "I don't know" or answers with
irrelevant information.

This is the limitation of a fixed pipeline. The search runs once with
the exact query the user typed, and there's no second chance. The
pipeline doesn't know the search failed, so it can't try again with a
corrected query.

We need something smarter. We need an agent.

[← Agents (Part 2 intro)](11-agents-intro.md) | [Function Calling →](13-function-calling.md)
