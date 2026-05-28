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

## Anatomy of an agent

An agent is an LLM assistant that has three parts:

- Instructions - the role and behavior we want. We pass this as
  the `developer` message. The better the instructions, the better the
  agent behaves.
- Tools - the functions the agent can call to act on the world.
  In our case, just `search`.
- Memory - the message history. Every prompt, every model output,
  every tool result is appended. The agent uses this to know what it
  has already tried.

Everything below is code that wires these three together inside a
loop.

## A developer prompt

So far we've relied on the model to figure out when to search. We can
make that more reliable by giving it a `developer` message that
spells out how to behave. The same message can also push it toward
multiple searches when the first one doesn't find the answer.

```python
instructions = """
You're a course teaching assistant.
You're given a question from a course student and your task is to answer it.

If you want to look up information, use the search function. 
Use as many keywords from the user question as possible when making first requests.

Make multiple searches.

Try to expand your search by using new keywords
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

    if call.name == "search":
        result = search(**args)

    result_json = json.dumps(result, indent=2)

    return {
        "type": "function_call_output",
        "call_id": call.call_id,
        "output": result_json,
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
question = "I just discovered the course. Can I join it?"

messages = [
    {"role": "developer", "content": instructions},
    {"role": "user", "content": question},
]

response = openai_client.responses.create(
    model="gpt-5.4-mini",
    input=messages,
    tools=[search_tool],
)

messages.extend(response.output)
has_function_calls = False

for item in response.output:
    if item.type == "function_call":
        print("function_call:", item.name, item.arguments)
        call_output = make_call(item)
        messages.append(call_output)
        has_function_calls = True

    elif item.type == "message":
        print("ASSISTANT:")
        print(item.content[0].text)
```

The `has_function_calls` flag tells us whether the model needs another
API call. If the response contains a function call, the updated
`messages` has tool output the model hasn't seen yet.

## The full agent loop

We wrap this in a `while` loop. The loop keeps calling the model until
it returns a response without any function calls. We also keep an
iteration counter so we can see how many round-trips happened.

```python
it = 1

while True:
    print(f"iteration #{it}...")
    has_function_calls = False

    response = openai_client.responses.create(
        model="gpt-5.4-mini",
        input=messages,
        tools=[search_tool],
    )

    messages.extend(response.output)

    for item in response.output:
        if item.type == "function_call":
            print("function_call:", item.name, item.arguments)
            call_output = make_call(item)
            messages.append(call_output)
            has_function_calls = True

        elif item.type == "message":
            print("ASSISTANT:")
            print(item.content[0].text)

    it = it + 1
    if has_function_calls == False:
        break
```

This is the core agent loop. The model reasons about the next action.
Your code performs it, and the model sees the result on the next
turn. The loop stops when the model produces a final answer without
any more tool calls.

The exit condition is the simplest one possible: "no function calls
this turn, we're done."

Other agent frameworks add safety nets on top of this. Common ones
are a max iteration count, a total token budget, or a wall-clock
limit. The core is still just this flag.

## Wrapping it in a function

Let's wrap the loop in a function so we can reuse it. The function
takes the instructions and the question as parameters, and returns
the final answer.

```python
def agent_loop(instructions, question, model="gpt-5.4-mini") -> str:
    messages = [
        {"role": "developer", "content": instructions},
        {"role": "user", "content": question}
    ]

    it = 1

    while True:
        print(f"iteration #{it}...")
        has_function_calls = False

        response = openai_client.responses.create(
            model=model,
            input=messages,
            tools=[search_tool]
        )

        messages.extend(response.output)

        for item in response.output:
            if item.type == "function_call":
                print("function_call:", item.name, item.arguments)
                call_output = make_call(item)
                messages.append(call_output)
                has_function_calls = True

            elif item.type == "message":
                print("ASSISTANT:")
                last_answer = item.content[0].text
                print(item.content[0].text)

        it = it + 1
        if has_function_calls == False:
            break

    return last_answer
```

Let's test it with a question that has a typo:

```python
agent_loop(instructions, "How do I run Olama locally?")
```

Watch what happens. The agent searches for "Olama", gets poor results,
then searches again with "Ollama" and finds the answer. The agent
loop lets the model recover from bad searches on its own.

Also try the course enrollment question:

```python
agent_loop(instructions, "I just discovered the course. Can I still join it?")
```

## Encouraging multiple searches

A subtle issue: the model often answers after the first search, even
when more searches would help. We can push it to explore more by
rewriting the instructions.

```python
instructions = """
You're a course teaching assistant.
You're given a question from a course student and your task is to answer it.

If you want to look up information, use the search function. 
Use as many keywords from the user question as possible when making first requests.

Make multiple searches. First perform search, analyze the results 
and then perform more searches. 

At the end, ask if there are other areas that the user wants to explore.
""".strip()

agent_loop(instructions, "I just discovered the course. Can I join it?")
```

Now the agent makes multiple searches per question and doesn't stop
after the first round of results. The instructions are the steering
wheel.

## Restricting off-topic questions

Right now the agent will happily answer anything.
Ask it about chess and it will still try.

```python
agent_loop(instructions, "what's queen gambit?")
```

We want a course assistant, not a general chatbot.
Tighten the instructions so the agent only answers from the FAQ.

```python
instructions = """
You're a course teaching assistant.
You're given a question from a course student and your task is to answer it.

If you want to look up information, use the search function. 
Use as many keywords from the user question as possible when making first requests.

Make multiple searches. First perform search, analyze the results 
and then perform more searches. 

The question has to be about the course or its logistics, offtopic questions 
shouldn't be answered. If the search returns nothing, it's likely an off-topic question.
If you can't answer the question using FAQ, don't do it yourself. Only use the 
facts from the FAQ database.

At the end, ask if there are other areas that the user wants to explore.
""".strip()

agent_loop(instructions, "what's queen gambit?")
```

This is a lightweight form of an input guardrail - we're telling the
agent what is in scope and what isn't. Real production guardrails are
a separate topic, but instructions are the first place to start.

This handwritten loop is the best way to understand what frameworks
hide from you. Every agent framework wraps this same pattern -
LangChain, PydanticAI, and the OpenAI Agents SDK all do it.

[← Function Calling](13-function-calling.md) | [ToyAIKit →](15-frameworks.md)
