# The Agentic Loop

Video: [Watch this lesson](https://www.youtube.com/watch?v=ePlQUcTPPjw&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

In the previous lesson, we did function calling by hand. We sent a
message and got back a function call. We ran it, sent the result back,
and got the answer.

That works for one function call. It breaks down when the model wants
to search several times, or when the first search misses the answer.
We don't know in advance how many calls the model will want. So we
need a loop that keeps calling the model and running tools until it's
done. An agent is exactly that.

## Anatomy of an agent

With the LLM in the driver's seat, we have an agent. It's an AI
assistant whose goal is to help the user.

An agent has three parts:

- Instructions, the role and behavior we want. We pass this as the
  `developer` message. The better the instructions, the better the
  agent helps.
- Tools, the functions the agent can call to carry out the task. For
  us that's only `search`.
- Memory, the message history. We append every prompt, every model
  output, and every tool result. The agent reads this to know what it
  has already tried.

Everything below is the code that wires these three together inside a
loop.

## A developer prompt

So far we've relied on the model to figure out when to search. We make
that more reliable with a `developer` message that spells out how to
behave. This is where we give the agent its role. The same message
also pushes it toward multiple searches, so we get to watch the loop
run more than once.

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
wrap that in a small helper. It turns the JSON arguments into a Python
dict, calls the right function, and serializes the result. We only
have one tool for now, so we dispatch on the function name directly.

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
`messages` has tool output the model hasn't seen yet. We'll need to
send it back.

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
Your code performs it, and the model sees the result on the next turn.
The loop stops when the model returns a final answer with no more tool
calls.

We don't decide how many times the model searches. The model does,
and we keep looping until it stops asking for tools.

The exit condition is the simplest one possible. No function calls
this turn means we're done. Other frameworks add safety nets on top,
like a max iteration count, a token budget, or a wall-clock limit. You
might cap it at five iterations and force an answer on the last one.
The core is still this one flag.

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

Try it with a question that has a typo:

```python
agent_loop(instructions, "How do I run Olama locally?")
```

Watch what happens. The agent searches for "Olama" and gets poor
results. It then searches again with "Ollama" and finds the answer.
The loop lets the model recover from a bad search on its own. That's
the whole point of going agentic.

Also try the course enrollment question:

```python
agent_loop(instructions, "I just discovered the course. Can I still join it?")
```

## Encouraging multiple searches

There's a subtle issue here. The model often answers after the first
search, even when more searches would help. It reasons that it already
knows enough, so why bother. We push it to explore more by rewriting
the instructions.

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
after the first round of results. The instructions are how we steer
the agent. It can still decide to skip ahead sometimes, so don't
expect it to follow them every single run.

## Restricting off-topic questions

Right now the agent will answer anything. Ask it about chess and it
will still try.

```python
agent_loop(instructions, "what's queen gambit?")
```

We want a course assistant, not a general chatbot. We tighten the
instructions so the agent only answers from the FAQ. For our own use
we might be fine letting it answer from general knowledge. So treat
this mainly as an illustration of steering scope.

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

This is a lightweight form of an input guardrail. We tell the agent
what's in scope and what isn't. A real guardrail checks the input
before the agent runs and can block off-topic questions outright.
That's a separate topic, but instructions are the first place to start.

This handwritten loop is the best way to understand what frameworks
hide from you. Every agent framework wraps this same pattern, whether
it's LangChain, PydanticAI, or the OpenAI Agents SDK.

[← Function Calling](13-function-calling.md) | [ToyAIKit →](15-frameworks.md)
