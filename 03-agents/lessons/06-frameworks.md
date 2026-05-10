# Frameworks

The handwritten agent loop from the previous lesson is educational but
repetitive. Every time you build a new agent, you'd write the same
while-loop, the same function-call handling, the same message
management. Frameworks wrap this pattern so you can focus on tools,
prompts, and behavior.


## ToyAI Kit

ToyAI Kit (toyaikit) is a teaching framework. It does the same thing
as our handwritten loop, but with less boilerplate. It's designed for
notebooks and workshops.

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

Important: toyaikit is a teaching and experimentation library. It is
useful for notebooks and workshops because it keeps display code out of
the way. It is NOT recommended for production use.


## Other frameworks

The concepts you learned - function calling, the agent loop, tool
definitions - are the same across all frameworks. They all wrap the
same pattern: send messages, check for function calls, execute tools,
repeat.

Here are some frameworks worth exploring:

- OpenAI Agents SDK - official SDK from OpenAI for building agents
- PydanticAI - type-safe agent framework with multi-provider support
- LangChain / LangGraph - popular framework with lots of integrations
- CrewAI - multi-agent orchestration
- AutoGen - multi-agent conversations from Microsoft
- Semantic Kernel - from Microsoft, supports C# and Python

Pick one that fits your stack and your needs. The hard part is
designing good tools and prompts - the loop itself is always the same.

---

[<- Previous](05-agentic-loop.md) | [Next ->](../README.md)
