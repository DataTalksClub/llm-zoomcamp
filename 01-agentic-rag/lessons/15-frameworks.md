# ToyAIKit

Video: [Watch this lesson](https://www.youtube.com/watch?v=PQpQOR3Un3w&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

The handwritten agent loop from the previous lesson is educational but
repetitive. Every time you build a new agent, you'd write the same
while-loop, the same function-call handling, the same message
management.

ToyAIKit wraps this pattern so you can focus on tools, prompts, and
behavior. We built it together in a DataTalks.Club workshop a while
back. It does the same thing as our handwritten loop with less
boilerplate. If you open its `runners` code, you'll find the same
`while True` loop we wrote by hand.

I use it here on purpose, because I don't want to pick a winner among
the production frameworks. ToyAIKit is small and easy to read, so when
something breaks you can see exactly what happened. That makes it handy
for developing and debugging locally before you go to production.

One caveat. ToyAIKit is a teaching and experimentation library, and it
is NOT meant for production use. We use it because it's minimal and you
can see what it does.

## Setup

Install it:

```bash
uv add toyaikit
```

Import the classes we need:

```python
from toyaikit.llm import OpenAIClient
from toyaikit.tools import Tools
from toyaikit.chat import IPythonChatInterface
from toyaikit.chat.runners import OpenAIResponsesRunner, DisplayingRunnerCallback
```

## Registering the tool

We register our `search` function along with the schema from earlier
lessons:

```python
agent_tools = Tools()
agent_tools.add_tool(search, search_tool)
```

## Letting ToyAIKit generate the schema

Writing that schema by hand is annoying, and we don't want to do it
for every function. So we don't have to.

If we add a type hint and a docstring to `search`, ToyAIKit reads them
and derives the schema for us:

```python
def search(query: str) -> dict[str, str]:
    """
    Search the FAQ database for entries matching the given query.
    """
    return index.search(
        query,
        num_results=5,
        boost_dict={"question": 3.0, "section": 0.5},
        filter_dict={"course": "llm-zoomcamp"}
    )
```

Then register it without passing a schema:

```python
agent_tools = Tools()
agent_tools.add_tool(search)
```

You can look at what ToyAIKit produced.

```python
agent_tools.get_tools()
```

The output is the same JSON schema we hand-wrote in the function
calling lesson. ToyAIKit generated it from the docstring and the type
hint.

Every modern agent framework does this same trick. It reads a typed
Python function with a docstring and builds the schema from it. The
OpenAI Agents SDK, PydanticAI, LangChain and Google ADK all work this
way. You write the tool and the framework figures out how to describe
it.

## The chat interface and runner

Create the chat interface and a callback, then build the runner:

```python
chat_interface = IPythonChatInterface()
callback = DisplayingRunnerCallback(chat_interface)

runner = OpenAIResponsesRunner(
    tools=agent_tools,
    developer_prompt=instructions,
    chat_interface=chat_interface,
    llm_client=OpenAIClient(model="gpt-5.4-mini")
)
```

The `chat_interface` handles display in the notebook. The `callback`
renders model messages and tool calls as they happen. The runner runs
the agent loop, the same `while True` we wrote by hand. It sends
messages, executes function calls, adds tool outputs back, and repeats
until the model is done.

We pick `gpt-5.4-mini` here on purpose. Without it, ToyAIKit falls
back to a smaller, faster default that doesn't follow the instructions
as reliably.

## Running one prompt

Run a single prompt:

```python
result = runner.loop(
    prompt="How do I run Olama locally?",
    callback=callback,
)
```

We used the typo "Olama" on purpose. The agent searches and gets poor
results, then retries with "Ollama". The recovery is the same as the
handwritten loop. The notebook output is nicer to watch. Each tool
call and message renders inline, so you can look at every search
result.

The `result` is a `LoopResult` with `all_messages` (the full
conversation), token counts, and `cost` (computed from token usage).

## Cost and tokens

Look at what the call cost:

```python
result.cost
```

Useful while developing - especially with multi-turn agents where one
prompt can trigger several model calls. The handwritten loop made you
compute this by hand. The framework keeps a running total for you.

You can also look at the full message history.

```python
result.all_messages
```

This is just a list - the same `messages` list we maintained by hand.

## Continuing the conversation

Take the messages from the previous result and pass them as
`previous_messages` on the next `loop` call:

```python
result2 = runner.loop(
    prompt="How do I run a different model?",
    previous_messages=result.all_messages,
    callback=callback,
)
```

The runner picks up where the last call left off, with the same agent
loop and an extended history. The model knows "different model" refers
to Ollama because it sees the previous turn in memory. Without that
history, it would have no idea what we're asking about.

## Interactive chat

For a chat-like workflow, run the built-in input loop:

```python
runner.run()
```

Type questions and get answers. Type "stop" to exit.

[← The Agentic Loop](14-agentic-loop.md) | [Other Frameworks →](16-other-frameworks.md)
