# Function Calling

So far, our RAG pipeline does search and then generation in a fixed
order: we search, build a prompt, and send it to the LLM. The LLM
never decides whether to search - we always do it.

Function calling changes that. We tell the LLM about our search
function and let it decide when to call it.


## Asking without tools

First, let's see what happens when we ask the LLM a course-specific
question without giving it any tools:

```python
response = openai_client.responses.create(
    model="gpt-5.4-mini",
    input=[
        {"role": "user", "content": "I just discovered the course. Can I join it?"}
    ],
)

response.output_text
```

The model answers from its general knowledge. It says something like
"it depends on the course" or "check the course website". It doesn't
know about our specific FAQ, so the answer is vague and not very
helpful.


## Defining the tool

We need to tell the model about our search function. The model doesn't
see our Python code - it only sees a schema that describes what the
function does and what arguments it takes.

```python
search_tool = {
    "type": "function",
    "name": "search",
    "description": "Search the FAQ database for entries matching the given query.",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "Search query text to look up in the course FAQ."
            }
        },
        "required": ["query"],
        "additionalProperties": False
    }
}
```

Let's go through each field:

- `type` - this is a function-type tool (the API also supports other
  tool types)
- `name` - the name of the function. When the model decides to call
  it, it references this name
- `description` - this is important. The model reads it to decide
  when to call the function. A good description helps the model make
  better decisions
- `parameters` - a JSON schema for the function arguments. The model
  generates arguments that match this schema
- `additionalProperties: False` - tells the model it can only use the
  fields we listed, no extra ones


## Sending the question with the tool

Now we send the same question, but this time we include the tool in the
request:

```python
developer_prompt = """
You're a course teaching assistant.
You're given a question from a course student and your task is to answer it.
If you look up information, use FAQ search.
""".strip()

chat_messages = [
    {"role": "developer", "content": developer_prompt},
    {"role": "user", "content": "I just discovered the course. Can I still join it?"}
]

response = openai_client.responses.create(
    model="gpt-5.4-mini",
    input=chat_messages,
    tools=[search_tool],
)

response.output
```

Look at the output. Instead of a message with the answer, the response
contains a `function_call` entry. The model decided it needs to search
the FAQ before answering. It didn't answer yet - it asked us to run
the search function first.


## Executing the function and sending the result back

The function call contains JSON arguments. We parse them, call our
Python `search` function, and serialize the result:

```python
import json

call = response.output[0]
args = json.loads(call.arguments)

results = search(**args)
result_json = json.dumps(results, indent=2)
```

Now we need to send this result back to the model. First, we add the
model's output to the conversation history - the model needs to see
its own function call. Then we add the tool result:

```python
chat_messages.extend(response.output)

chat_messages.append({
    "type": "function_call_output",
    "call_id": call.call_id,
    "output": result_json,
})
```

The `call_id` links the tool result to the specific function call the
model requested. If the model makes multiple function calls in one
turn, each one gets its own `call_id`.


## Asking the model again

Now we call the API a second time with the expanded history:

```python
response = openai_client.responses.create(
    model="gpt-5.4-mini",
    input=chat_messages,
    tools=[search_tool],
)

response.output_text
```

This time the model has the original question, its own decision to
call `search`, and the FAQ results. It can now produce a proper
course-specific answer.

Important point: LLMs are stateless between API calls. The memory is
the list you send as `input`. If you leave out previous messages, the
model doesn't know what happened.

---

[<- Previous](03-agents-concept.md) | [Next ->](05-agentic-loop.md)
