# Other Frameworks

The concepts you learned in Part 2 are the same across frameworks.
Function calling, the agent loop, and tool definitions all wrap the
same pattern. Send messages, run any function calls, and repeat until
the model is done.

Now that you understand how the loop works, you can pick up any
production framework and know what it's doing.

Here are some frameworks worth exploring:

## OpenAI Agents SDK

The official SDK from OpenAI for building agents. It uses the same
Responses API we used throughout this module. It supports tool
definition, multi-turn conversations, and handoffs between agents.

```bash
uv add openai-agents
```

Good choice if you're already using OpenAI and want something
official and well-maintained.

## PydanticAI

A type-safe agent framework that supports multiple LLM providers.
Tools are plain Python functions with type hints - no wrappers needed.
Switching providers is as simple as changing the model string.

```bash
uv add pydantic-ai
```

Good choice if you want type safety and multi-provider support.

## LangChain / LangGraph

A popular framework with lots of integrations. LangChain handles the
basics, and LangGraph adds graph-based workflows for more complex
agent patterns.

Good choice if you need lots of integrations (vector stores, document
loaders, etc.) and a large community.

## Google ADK

The Agent Development Kit from Google. It's the natural pick if you
plan to use Gemini models. It exposes the same building blocks
(tools, instructions, sessions) and integrates with Google Cloud.

Good choice if your stack is on Google Cloud or you specifically want
Gemini.

## Others

Other frameworks worth knowing:

- CrewAI - multi-agent orchestration
- AutoGen - multi-agent conversations from Microsoft
- Semantic Kernel - from Microsoft, supports C# and Python
- Smolagents - lightweight agent framework from HuggingFace
- Anthropic Tool Use - Anthropic's native tool use API

Pick one that fits your stack and your needs. The hard part is
designing good tools and prompts - the loop is always the same.

## Avoiding agents when you can

A closing thought: you don't always need an agent. Adding one is a
real cost.

- More API calls per request - the loop can fire many tool calls
  before the model is satisfied.
- Higher latency - each round-trip waits on the model.
- More money spent - every iteration is another billed call, and the
  full message history is re-sent each turn.
- More moving parts - you now monitor cost, iteration count, and
  whether the agent is going in circles.
- Less predictable - the LLM decides what to do, so two runs of the
  same prompt can take different paths.

Before reaching for an agent, ask whether the problem actually needs
one. A lot of tasks are well-served by simpler approaches.

- Plain RAG (one search, one answer).
- Parsing or templating.
- A single LLM call with no tools.

Try the simpler approach first. If it works, ship it.
Add the agent loop only when the simpler solution genuinely can't
handle the problem. By then you should also be ready to take on the
extra complexity that comes with it.

[← ToyAIKit](15-frameworks.md) | [Back to module →](../)
