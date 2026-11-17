---
video_url: "https://www.youtube.com/watch?v=7tvpR8EE0gs&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
prev_url: 05-rag.md
next_url: 07-multi-agent.md
---
# AI Agents

In [Module 1](../01-agentic-rag/11-agents-intro.md) you built the agentic loop by hand: a `while` loop that called the LLM, executed any tool calls it returned, sent the results back, and stopped when the model produced a final answer with no more tool calls. That pattern is the foundation of every agent framework.

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

Flow: [`4_simple_agent.yaml`](flows/4_simple_agent.yaml)

This flow demonstrates a basic AI agent that summarizes text with controllable length and language. It shows how to structure agent prompts, chain agent tasks, use `pluginDefaults` to avoid repetition, and track token usage for cost monitoring.



## Advanced Agent Example: Web Research

Flow: [`5_web_research_agent.yaml`](flows/5_web_research_agent.yaml)

This flow demonstrates an agent with autonomous tool usage:

1. Receives a research prompt (e.g., "Latest trends in workflow orchestration")
2. Decides to use the web search tool to gather information
3. Evaluates search results and determines if more searches are needed
4. Synthesizes findings into a structured markdown report
5. Saves the report to a file using the filesystem tool


The agent autonomously decides when to use tools, can loop (search → evaluate → search again) until satisfied, and you only specify the goal — not the exact steps.

## Optional Lab: Release Lookup with HTTP MCP

Flow: [`7_mcp_release_lookup.yaml`](flows/7_mcp_release_lookup.yaml)

The [RAG example](flows/2_chat_with_rag.yaml) ingests a selected release document into Kestra's embedding store before answering. This lab asks the same Kestra 1.1 question using a public web search tool during the agent loop. Compare where the evidence comes from and whether you can follow the answer back to the original release announcement.

The flow uses Kestra's `StreamableHttpMcpClient` with Parallel's Unified MCP server. It exposes only `web_search` and `web_fetch`. Anonymous search and fetch require no Parallel API key and have lower rate limits; see [Parallel MCP setup](https://docs.parallel.ai/integrations/mcp/quickstart). Generation still requires your configured `GEMINI_API_KEY` and a tool-capable model available to your account. Use public documentation questions: search queries go to Parallel, and retrieved excerpts go to your generation provider.

Runtime versions for this lab: Kestra 1.3.21 and AI plugin 1.12.6. See the [HTTP MCP client documentation](https://kestra.io/plugins/plugin-ai/tool/io.kestra.plugin.ai.tool.streamablehttpmcpclient) for plugin installation if your instance does not recognize the tool.

1. Complete the [Kestra setup](03-setup.md), including the generation secret.
2. Open **Flows → Create** in the Kestra UI, paste the linked YAML, and save it in the `zoomcamp` namespace.
3. Execute `7_mcp_release_lookup`. Set `model_name` to a tool-capable generation model available to your account and keep the default release question.
4. In the `release_lookup` task outputs, inspect `toolExecutions`: confirm that `web_search` ran and inspect its returned URLs and excerpts. Check `textOutput` and the `log_answer` logs for links to the original sources, including the [official Kestra 1.1 announcement](https://kestra.io/blogs/release-1-1).
5. Compare with flow 2: which features are supported by the selected document, which are supported by the web results, and do the linked pages actually support each claim? Neither retrieval method guarantees a correct answer; verify the citations.

A retriever runs before generation; this MCP client makes tools available for the agent to call. The prompt requests search, and the flow caps sequential tool rounds at three, with a three-minute task timeout and a 45-second MCP timeout. If no tool ran or the answer has no source links, the lab's evidence check has not passed. A tool failure may fail the task; if an error is returned to the agent, the prompt asks it to report the missing evidence. On a rate limit, wait before retrying. This lab is optional; the earlier flows can be run independently.

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

<!-- nav:start -->
[← Previous: Retrieval Augmented Generation](05-rag.md) · [Next: Multi-Agent Systems →](07-multi-agent.md)
<!-- nav:end -->
