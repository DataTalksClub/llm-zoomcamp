# Other Frameworks

The concepts you learned in this module - function calling, the agent
loop, tool definitions - are the same across all frameworks. They all
wrap the same pattern: send messages, check for function calls, execute
tools, repeat.

Now that you understand how the loop works under the hood, you can
use any production framework and know what it's doing.

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
basics. LangGraph adds graph-based workflows for more complex agent
patterns.

Good choice if you need lots of integrations (vector stores, document
loaders, etc.) and a large community.


## Others

- CrewAI - multi-agent orchestration
- AutoGen - multi-agent conversations from Microsoft
- Semantic Kernel - from Microsoft, supports C# and Python
- Smolagents - lightweight agent framework from HuggingFace
- Anthropic Tool Use - Anthropic's native tool use API

Pick one that fits your stack and your needs. The hard part is
designing good tools and prompts - the loop itself is always the same.

[<- ToyAIKit](06-frameworks.md) | [Back to module ->](../)
