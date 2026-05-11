# Building the Prompt

The LLM doesn't see our documents unless we pass them in. So we need
to build a prompt that includes the user's question and the search
results.

Typically when we build AI systems, the prompt consists of two parts:

- Instructions (also called system prompt): this tells the LLM how to
  behave. It never changes - it's the same for every request.
- User prompt: this changes with every request. It contains the actual
  question and the retrieved context.

## Instructions

The instructions tell the LLM its role and how to answer:

```python
INSTRUCTIONS = '''
Your task is to answer questions from the course participants
based on the provided context.

Use the context to find relevant information and provide accurate
answers. If the answer is not found in the context,
respond with "I don't know."
'''
```

This is what grounds the answer in our data and reduces hallucinations.


## The user prompt template

The user prompt template has placeholders for the question and the
context:

```python
USER_PROMPT_TEMPLATE = '''
Question:
{question}

Context:
{context}
'''
```


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
This format makes it easy for the LLM to read. We just turned a
dictionary into a string - nothing fancy here.


## Building the prompt

Now we combine the question with the context into the user prompt:

```python
def build_prompt(question, search_results):
    context = build_context(search_results)
    prompt = USER_PROMPT_TEMPLATE.format(
        question=question,
        context=context
    )
    return prompt.strip()
```

Let's try it:

```python
prompt = build_prompt(question, search_results)

print(prompt)
```

You should see a prompt with the question at the top and several
FAQ entries below it. This is exactly what we'll send to the LLM.

The prompt looks something like:

```
Question:
I just discovered the course. Can I join now?

Context:
General Course-Related Questions
Q: I just discovered the course. Can I still join?
A: Yes, but if you want to receive a certificate, you need to submit your project while we're still accepting submissions.

General Course-Related Questions
Q: Course: I have registered for the LLM Zoomcamp. When can I expect to receive the confirmation email?
A: You don't need it. You're accepted. You can also just start learning and submitting homework...

...
```

The prompt is the bridge between search and the LLM. A bad prompt
means the LLM ignores the context and hallucinates. A good prompt
keeps the answer grounded.

Prompt engineering is a mix of art and science. You experiment, try
different things, and see what works. Later in the course we'll talk
about evaluation metrics so you can numerically measure how well your
prompt performs. For now, this template is a good starting point.

Code: [notebook.ipynb](../code/notebook.ipynb)

[← Search](05-search.md) | [The LLM →](07-llm.md)
