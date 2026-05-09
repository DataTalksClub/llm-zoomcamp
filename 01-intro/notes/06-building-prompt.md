# Building the Prompt

The LLM doesn't see our documents unless we pass them in. So we need
to build a prompt that includes the user's question and the search
results.


## Prompt template

A good RAG prompt has two parts:

1. Instructions - tell the LLM how to behave
2. Context - the retrieved documents + the user's question

Let's define both:

```python
PROMPT_TEMPLATE = """
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT:
{context}
""".strip()
```

The prompt tells the LLM to only use information from the CONTEXT.
This is what grounds the answer in our data and reduces hallucinations.


## Building the context

The `context` is a formatted string with all the search results:

```python
def build_context(search_results):
    context = ""
    for doc in search_results:
        context += f"section: {doc['section']}\n"
        context += f"question: {doc['question']}\n"
        context += f"answer: {doc['answer']}\n"
        context += "\n"
    return context.strip()
```

Each document becomes a block with the section, question, and answer.
This format makes it easy for the LLM to read.


## Putting it together

Now the `build_prompt` function combines the template with the search
results:

```python
def build_prompt(query, search_results):
    context = build_context(search_results)
    return PROMPT_TEMPLATE.format(question=query, context=context)
```

Let's try it:

```python
query = "How do I run Docker on Windows?"
search_results = search(query)
prompt = build_prompt(query, search_results)

print(prompt)
```

You should see a prompt with the question at the top and several
FAQ entries below it. This is exactly what we'll send to the LLM.

The prompt looks something like:

```
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: How do I run Docker on Windows?

CONTEXT:
section: Module 5: Monitoring
question: How can I remove all Docker containers, images, and volumes, and builds from the terminal?
answer: 1. Delete all containers (including running ones): ...

section: ...
question: ...
answer: ...
```


## Why the prompt matters

The prompt is the bridge between search and the LLM. A bad prompt
means the LLM ignores the context and hallucinates. A good prompt
keeps the answer grounded.

Key principles:

- Be explicit: tell the LLM to use only the provided context.
- Be structured: format the context clearly so the LLM can parse it.
- Be concise: don't pad the prompt with unnecessary instructions.

We'll keep this prompt simple. In a real system you might add more
instructions, but the structure stays the same.
