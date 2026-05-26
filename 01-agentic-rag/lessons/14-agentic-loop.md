# The Agentic Loop

In the previous lesson, we did function calling by hand. We sent a
message and got a function call. We ran it, sent the result back, and
got the answer.

That works for one function call. It breaks down when the model wants
to search multiple times, or when the first search doesn't find the
answer.

We need a loop. An agent is exactly that.

A loop that keeps calling the model and executing tools, sending
results back, until the model is done.

## A developer prompt

So far we've relied on the model to figure out when to search. We can
make that more reliable by giving it a `developer` message that
spells out how to behave. The same message can also push it toward
multiple searches when the first one doesn't find the answer.

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

## A function-call helper

We'll be running function calls repeatedly inside the loop, so let's
wrap that in a small helper. We only have one tool for now, so we
dispatch on the function name directly.

```python
def make_call(call):
    args = json.loads(call.arguments)

    if call.name == 'search':
        result = search(**args)

    result_json = json.dumps(result, indent=2)

    return {
        "type": "function_call_output",
        'call_id': call.call_id,
        'output': result_json,
    }
```

The helper returns the exact structure the Responses API expects.
When we add more tools later, we'll extend this with more `if`
branches (or switch to a registry).

## Processing one response

Let's process a single model response. We append each output entry to
the conversation, print any messages, and run any function calls.
Function-call results get appended too.

```python
response = openai_client.responses.create(
    model='gpt-5.4-mini',
    input=chat_messages,
    tools=[search_tool],
)

has_function_calls = False

for entry in response.output:
    chat_messages.append(entry)

    if entry.type == 'message':
        print(entry.content[0].text)

    if entry.type == 'function_call':
        print('function_call:', entry.name, entry.arguments)
        result = make_call(entry)
        chat_messages.append(result)
        has_function_calls = True
```

The `has_function_calls` flag tells us whether the model needs another
API call. If the response contains a function call, the updated
`chat_messages` has tool output the model hasn't seen yet.

## The full agent loop

We wrap this in a `while` loop.

The loop keeps calling the model
until it returns a response without any function calls:

```python
while True:
    response = openai_client.responses.create(
        model='gpt-5.4-mini',
        input=chat_messages,
        tools=[search_tool],
    )

    chat_messages.extend(response.output)
    has_function_calls = False

    for entry in response.output:
        if entry.type == 'message':
            print(entry.content[0].text)

        if entry.type == 'function_call':
            print('function_call:', entry.name, entry.arguments)
            result = make_call(entry)
            chat_messages.append(result)
            has_function_calls = True

    if not has_function_calls:
        break
```

This is the core agent loop. The model reasons about the next action.
Your code performs it, and the model sees the result on the next
turn. The loop stops when the model produces a final answer without
any more tool calls.

## Wrapping it in a function

Let's wrap the loop in a function so we can reuse it:

```python
def agent_loop(question, model='gpt-5.4-mini'):
    chat_messages = [
        {'role': 'developer', 'content': developer_prompt},
        {'role': 'user', 'content': question}
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
            if entry.type == 'message':
                print(entry.content[0].text)

            if entry.type == 'function_call':
                print('function_call:', entry.name, entry.arguments)
                result = make_call(entry)
                chat_messages.append(result)
                has_function_calls = True

        if not has_function_calls:
            break
```

Let's test it with a question that has a typo:

```python
agent_loop('How do I run Olama locally?')
```

Watch what happens. The agent searches for "Olama", gets poor results,
then searches again with "Ollama" and finds the answer. The agent
loop lets the model recover from bad searches on its own.

Also try the course enrollment question:

```python
agent_loop('I just discovered the course. Can I still join it?')
```

This handwritten loop is the best way to understand what frameworks
hide from you. Every agent framework wraps this same pattern -
LangChain, PydanticAI, and the OpenAI Agents SDK all do it.

[← Function Calling](13-function-calling.md) | [ToyAIKit →](15-frameworks.md)
