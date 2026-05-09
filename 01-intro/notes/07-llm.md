# The LLM

The last component of our RAG pipeline is the LLM itself. It takes
the prompt we built and generates an answer.


## The LLM function

The `llm` function takes a prompt and sends it to the OpenAI API:

```python
from openai import OpenAI

openai_client = OpenAI()

def llm(prompt, model="gpt-4o-mini"):
    response = openai_client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
```

Test it with a simple prompt:

```python
llm("What is 2 + 2?")
```

If you get an error, check your API key.

We're using the chat completions API with a single user message. The
`model` parameter defaults to `gpt-4o-mini` which is cheap and fast.
You can use any model you like.

For Groq or other OpenAI-compatible providers, adjust the client
initialization (see the environment setup section).
