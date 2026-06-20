# AI Agents

Video: [Agentic Workflows](https://www.youtube.com/watch?v=7tvpR8EE0gs&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

In [Module 1](../../01-agentic-rag/lessons/11-agents-intro.md) you built the agentic loop by hand: a `while` loop that called the LLM, executed any tool calls it returned, sent the results back, and stopped when the model produced a final answer with no more tool calls. That pattern is the foundation of every agent framework.

In Kestra, the `AIAgent` plugin handles that loop for you. You define the goal, the tools, and optionally a system message - Kestra drives the loop, manages conversation history, and surfaces the result as a task output.

> Note: The flows in this lesson use `{{ secret('GEMINI_API_KEY') }}`. Make sure you've completed the [setup instructions](03-setup.md) to configure this secret before running them.

The example flows use Gemini, but the `provider` block supports any major AI provider — swap `io.kestra.plugin.ai.provider.GoogleGemini` for `OpenAI`, `Anthropic`, or others. See the [full list of supported providers](https://kestra.io/plugins/plugin-ai/provider).

Traditional Workflow — fixed sequence, predetermined logic:

```yaml
tasks:
  - id: step1
    type: Task1
  - id: step2
    type: Task2
  - id: step3
    type: Task3
```

AI Agent Workflow — agent decides what to do, in what order, based on the goal:

```yaml
tasks:
  - id: agent
    type: io.kestra.plugin.ai.agent.AIAgent
    prompt: "Research data engineering trends and create a report"
    tools:
      - WebSearch
      - TaskExecution
```

## When to Use AI Agents

Use AI Agents when the exact sequence of steps isn't known in advance, decisions depend on dynamic changing information, or you need to adapt to unexpected conditions.

Use traditional workflows when steps are deterministic and repeatable, compliance requires exact auditable processes, or cost and latency must be minimized.

## Anatomy of an AI Agent

```yaml
id: example_agent
namespace: zoomcamp

tasks:
  - id: agent
    type: io.kestra.plugin.ai.agent.AIAgent

    # Defines the agent's role and behavior
    systemMessage: |
      You are a data analyst. Analyze data and provide insights.

    # The actual task or question
    prompt: "What are the top 3 trends in this data?"

    # LLM provider configuration
    provider:
      type: io.kestra.plugin.ai.provider.GoogleGemini
      modelName: gemini-2.5-flash
      apiKey: "{{ secret('GEMINI_API_KEY') }}"

    # Tools the agent can use
    tools:
      - type: io.kestra.plugin.ai.tool.TavilyWebSearch
        apiKey: "{{ secret('TAVILY_API_KEY') }}"

    # Memory for context across executions
    memory:
      type: io.kestra.plugin.ai.memory.KestraKVStore
      memoryId: analyst_001
```

## Simple Agent Example

Flow: [`4_simple_agent.yaml`](../flows/4_simple_agent.yaml)

This flow demonstrates a basic AI agent that summarizes text with controllable length and language. It shows how to structure agent prompts, chain agent tasks, use `pluginDefaults` to avoid repetition, and track token usage for cost monitoring.

## Advanced Agent Example: Web Research

Flow: [`5_web_research_agent.yaml`](../flows/5_web_research_agent.yaml)

This flow demonstrates an agent with autonomous tool usage:

1. Receives a research prompt (e.g., "Latest trends in workflow orchestration")
2. Decides to use the web search tool to gather information
3. Evaluates search results and determines if more searches are needed
4. Synthesizes findings into a structured markdown report
5. Saves the report to a file using the filesystem tool

The agent autonomously decides when to use tools, can loop (search → evaluate → search again) until satisfied, and you only specify the goal — not the exact steps.

## Agent Tools Available in Kestra

| Tool | Purpose | Example Use |
|------|---------|-------------|
| `TavilyWebSearch` | Search the web for current information | Market research, news monitoring |
| `GoogleCustomWebSearch` | Search with Google Custom Search API | Google search |
| `CodeExecution` | Run code safely via Judge0 | Math calculations, data validation |
| `KestraTask` | Execute any Kestra task | Run tasks based on 1000+ Kestra plugins |
| `KestraFlow` | Trigger other Kestra flows | Call other flows for modularity |
| `StreamableHttpMcpClient` | Use MCP servers via HTTP/SSE | Connect to remote MCP servers |
| `DockerMcpClient` | Use MCP servers in Docker | MCP servers spun up on-demand via Docker |
| `StdioMcpClient` | Use MCP servers via stdio | Integration with external systems |
| `AIAgent` | Use another agent as a tool | Multi-agent systems, specialized sub-agents |

## Agent Observability

Kestra provides full observability for agent executions — token usage, tool executions, request and response logs, outputs, and execution time.

Enable detailed logging via the `configuration` property:

```yaml
tasks:
  - id: research_agent
    type: io.kestra.plugin.ai.agent.AIAgent
    description: Autonomous research agent with web search capabilities
    provider:
      type: io.kestra.plugin.ai.provider.GoogleGemini
      apiKey: "{{ secret('GEMINI_API_KEY') }}"
      modelName: gemini-2.5-flash
    configuration:
      logRequests: true
      logResponses: true
```

[← RAG](05-rag.md) | [Multi-Agent Systems →](07-multi-agent.md)
