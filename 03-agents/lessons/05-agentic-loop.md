# The Agentic Loop

In the previous lesson, we did function calling by hand: send a
message, get a function call, run it, send the result, get the answer.
That works for one function call. But what if the model wants to make
multiple searches? What if the first search doesn't find the answer?

We need a loop. That's what an agent is: a loop that keeps calling the
model, executing tools, and sending results back until the model is
done.


## A stronger developer prompt

First, let's give the agent more explicit instructions. This prompt
encourages the model to search multiple times and expand its search:

```python
developer_prompt = """
You're a course teaching assistant.
You're given a question from a course student and your task is to answer it.

If you want to look up information, use the search function. 
Use as many keywords from the user question as possible when making first requests.

Make multiple searches if needed. Try to expand your search by using new keywords
based on the results you get from the search.

At the end, ask if there are other areas that the user wants to explore.
""".strip()
```


## A generic function-call helper

Instead of hard-coding the search function, let's create a helper that
reads the function name from the model output and calls the matching
Python function:

```python
def make_call(call):
    args = json.loads(call.arguments)
    f_name = call.name
    f = globals()[f_name]
    result = f(**args)
    result_json = json.dumps(result, indent=2)
    return {
        "type": "function_call_output",
        "call_id": call.call_id,
        "output": result_json,
    }
```

The helper returns the exact object shape the Responses API expects.
`globals()` is fine for notebooks - in production code, use an explicit
registry like `{"search": search}` so the model can only call functions
you intentionally expose.


## Processing one response

Let's process a single model response. We append each output entry to
the conversation. If it's a message, we print it. If it's a function
call, we run it and append the result:

```python
response = openai_client.responses.create(
    model="gpt-5.4-mini",
    input=chat_messages,
    tools=[search_tool],
)

has_function_calls = False

for entry in response.output:
    chat_messages.append(entry)

    if entry.type == "message":
        print(entry.content[0].text)

    if entry.type == "function_call":
        print("function_call:", entry.name, entry.arguments)
        result = make_call(entry)
        chat_messages.append(result)
        has_function_calls = True
```

The `has_function_calls` flag tells us whether the model needs another
API call. If the response contains a function call, the updated
`chat_messages` has tool output the model hasn't seen yet.


## The full agent loop

Now we wrap this in a `while` loop. The loop keeps calling the model
until it returns a response without any function calls:

```python
while True:
    response = openai_client.responses.create(
        model="gpt-5.4-mini",
        input=chat_messages,
        tools=[search_tool],
    )

    chat_messages.extend(response.output)
    has_function_calls = False

    for entry in response.output:
        if entry.type == "message":
            print(entry.content[0].text)

        if entry.type == "function_call":
            print("function_call:", entry.name, entry.arguments)
            result = make_call(entry)
            chat_messages.append(result)
            has_function_calls = True

    if not has_function_calls:
        break
```

This is the core agent loop. The model reasons about the next action,
your code performs the action, and the model sees the result on the
next turn. The loop stops when the model produces a final answer
without requesting any more tool calls.


## Wrapping it in a function

Let's wrap the loop in a function so we can reuse it:

```python
def agent_loop(question, model="gpt-5.4-mini"):
    chat_messages = [
        {"role": "developer", "content": developer_prompt},
        {"role": "user", "content": question}
    ]

    while True:
        response = openai_client.responses.create(
            model=model,
            input=chat_messages,
            tools=[search_tool],
        )

        chat_messages.extend(response.output)
        has_function_calls = False

        for entry in response.output:
            if entry.type == "message":
                print(entry.content[0].text)

            if entry.type == "function_call":
                print("function_call:", entry.name, entry.arguments)
                result = make_call(entry)
                chat_messages.append(result)
                has_function_calls = True

        if not has_function_calls:
            break
```

Let's test it with a question that has a typo:

```python
agent_loop("How do I run ducker on windows?")
```

Watch what happens. The agent searches for "ducker", gets poor results,
then searches again with "docker" and finds the answer. The agent
loop lets the model recover from bad searches on its own.

Also try the course enrollment question:

```python
agent_loop("I just discovered the course. Can I still join it?")
```

This handwritten loop is the best way to understand what frameworks
hide from you. Every agent framework - LangChain, PydanticAI, OpenAI
Agents SDK - wraps this same pattern.

---

[<- Previous](04-function-calling.md) | [Next ->](06-frameworks.md)
