# ToyAIKit

The handwritten agent loop from the previous lesson is educational but
repetitive. Every time you build a new agent, you'd write the same
while-loop, the same function-call handling, the same message
management.

ToyAIKit wraps this pattern so you can focus on tools,
prompts, and behavior. It does the same thing as our handwritten loop,
but with less boilerplate. It's designed for notebooks and workshops.

Important: ToyAIKit is a teaching and experimentation library. It is
NOT recommended for production use. We use it here because it's
minimal and educational - you can see what it does.

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

We don't actually need to write the schema ourselves. If we add a type
hint and a docstring to `search`, ToyAIKit can derive the schema from
the function:

```python
def search(query: str):
    """
    Search the FAQ database for entries matching the given query.
    """
    return index.search(
        query,
        num_results=5,
        boost_dict={'question': 3.0, 'section': 0.5},
        filter_dict={'course': 'llm-zoomcamp'}
    )
```

Then register it without passing a schema:

```python
agent_tools = Tools()
agent_tools.add_tool(search)
```

ToyAIKit reads the function name, type hints, and docstring and builds
the JSON schema automatically. The schema stays in sync with the
function.

## The chat interface and runner

Create the chat interface and the runner:

```python
chat_interface = IPythonChatInterface()

runner = OpenAIResponsesRunner(
    tools=agent_tools,
    developer_prompt=developer_prompt,
    chat_interface=chat_interface,
    llm_client=OpenAIClient()
)
```

The `chat_interface` handles display in the notebook. The runner
handles the agent loop - sending messages, executing function calls,
adding tool outputs back, and repeating until the model is done.

## Running one prompt

First, set up a callback that renders model messages, function calls,
arguments, and tool outputs in the notebook:

```python
callback = DisplayingRunnerCallback(chat_interface)
```

Now run a single prompt:

```python
result = runner.loop(
    prompt='How do I run Ollama locally?',
    callback=callback,
)
```

The `result` is a `LoopResult` with `all_messages` (the full
conversation), `tokens` (input/output counts), and `cost` (computed
from token usage).

## Cost and tokens

Inspect what the call cost:

```python
print(f"Tokens: {result.tokens.input_tokens} in / {result.tokens.output_tokens} out")
print(f"Cost: ${result.cost.total_cost:.6f}")
```

Useful while developing - especially with multi-turn agents where one
prompt can trigger several model calls.

## Continuing the conversation

Take the messages from the previous result and pass them as
`previous_messages` on the next `loop` call:

```python
messages = result.all_messages

result = runner.loop(
    prompt='What about on Windows?',
    previous_messages=messages,
    callback=callback,
)

messages = result.all_messages
```

The runner picks up where the last call left off - same agent loop,
extended history.

## Interactive chat

For a chat-like workflow, run the built-in input loop:

```python
runner.run()
```

Type questions and get answers. Type "stop" to exit.

[← The Agentic Loop](14-agentic-loop.md) | [Other Frameworks →](16-other-frameworks.md)
