# Building the Prompt

The LLM doesn't see our documents unless we pass them in. So we need
to build a prompt that includes the user's question and the search
results.

In the OpenAI Responses API, we send two things:
`instructions` tells the LLM how to behave (the system message).
`input` is the user's question together with the retrieved context.


## Instructions

The instructions tell the LLM its role and how to answer:

```python
INSTRUCTIONS = """
You're a course teaching assistant.
Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.
""".strip()
```

This is what grounds the answer in our data and reduces hallucinations.


## Building the context

The `context` is a formatted string with all the search results:

```python
def build_context(search_results):
    lines = []

    for doc in search_results:
        lines.append(doc['section'])
        lines.append('Q: ' + doc['question'])
        lines.append('A: ' + doc['answer'])
        lines.append('')

    return '\n'.join(lines).strip()
```

Each document becomes a block with the section, question, and answer.
This format makes it easy for the LLM to read.


## The user prompt

Now we combine the question with the context into the user prompt:

```python
PROMPT_TEMPLATE = """
QUESTION: {question}

CONTEXT:
{context}
""".strip()

def build_prompt(query, search_results):
    context = build_context(search_results)
    return PROMPT_TEMPLATE.format(question=query, context=context)
```

Let's try it:

```python
query = 'How do I run Docker on Windows?'
search_results = search(query)
prompt = build_prompt(query, search_results)

print(prompt)
```

You should see a prompt with the question at the top and several
FAQ entries below it. This is exactly what we'll send to the LLM.

The prompt looks something like:

```
QUESTION: How do I run Docker on Windows?

CONTEXT:
Module 5: Monitoring
Q: How can I remove all Docker containers, images, and volumes, and builds from the terminal?
A: 1. Delete all containers (including running ones): ...

...
Q: ...
A: ...
```

The prompt is the bridge between search and the LLM. A bad prompt
means the LLM ignores the context and hallucinates. A good prompt
keeps the answer grounded.

- Be explicit: tell the LLM to use only the provided context.
- Give it a role: "you're a course teaching assistant" tells the LLM
  how to behave.
- Be structured: format the context clearly so the LLM can parse it.
- Be concise: don't pad the prompt with unnecessary instructions.

Prompt engineering is a mix of art and science. You experiment, try
different things, and see what works. Later in the course we'll talk
about evaluation metrics so you can numerically measure how well your
prompt performs. For now, this template is a good starting point.

[← Search](05-search.md) | [The LLM →](07-llm.md)
