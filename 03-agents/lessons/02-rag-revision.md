# Quick RAG Revision

Before we talk about agents, let's set up the RAG pipeline from module
1. We'll use the `RAGBase` class we created in lesson 08.

If you completed module 1, this will be a quick recap. If you skipped
it, copy the `rag_helper.py` file from module 1 into your project.


## Setting up RAG

First, load the data and create the search index:

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

instructions = """
You're a course teaching assistant.
Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.
""".strip()

rag = RAGBase(
    index=index,
    llm_client=OpenAI(),
    instructions=instructions,
)
```


## Testing it

Let's try a question:

```python
rag.rag("How do I run Docker on Windows?")
```

This should work fine. The search finds relevant FAQ entries about
Docker, and the LLM gives a good answer.

Now let's try something slightly different:

```python
rag.rag("How do I run ducker on windows?")
```

The word "ducker" doesn't match "Docker" in our index. The search
returns poor results - maybe some unrelated documents about other
topics. The LLM gets these bad results and either says "I don't know"
or tries to answer with irrelevant information.

This is the limitation of a fixed pipeline. The search runs once with
the exact query the user typed. There's no second chance. The pipeline
can't adapt - it doesn't know the search failed, and it can't try
again with a corrected query.

We need something smarter. We need an agent.


[← Agents](01-intro.md) | [What Are Agents? →](03-agents-concept.md)
