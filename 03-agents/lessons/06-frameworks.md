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

We register our search function with the same tool schema from earlier
lessons:

```python
agent_tools = Tools()
agent_tools.add_tool(search, search_tool)
```

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

To run a single prompt and see the tool calls:

```python
callback = DisplayingRunnerCallback(chat_interface)
messages = runner.loop(prompt="How do I run Docker on Windows?", callback=callback)
```

The callback renders model messages, function calls, arguments, and
tool outputs in the notebook. During development, this shows whether
the model searched for the right thing.


## Interactive chat

For a chat-like workflow, run the built-in input loop:

```python
runner.run()
```

Type questions and get answers. Type "stop" to exit.

---

[<- Previous](05-agentic-loop.md) | [Next ->](07-other-frameworks.md)
