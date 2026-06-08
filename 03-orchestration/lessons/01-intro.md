# AI Orchestration

Video: [Using AI in Workflows](https://youtu.be/xUAkcgNIcRI)

This module introduces AI-powered workflow orchestration using Kestra. You'll learn how AI can accelerate workflow development and enable autonomous task automation through three techniques: AI Copilot for generating flows, RAG for grounding responses in real data, and AI Agents for autonomous task execution.

## Learning Objectives

By the end of this module, you will:

- Understand the importance of context engineering in AI applications
- Use AI Copilot to build Kestra flows faster and more accurately
- Implement Retrieval Augmented Generation (RAG) to ground AI responses in real data
- Build autonomous AI agents that can make decisions and use tools dynamically
- Design multi-agent systems where specialized agents collaborate to solve complex tasks
- Apply best practices for using AI in production data workflows

## Prerequisites

- Kestra running locally (see [Setting up Kestra](03-setup.md))
- Google Cloud account with access to Gemini API
- Basic understanding of YAML and workflow concepts

> Note: The flows in this module use Gemini, but Kestra's AI plugins support any major provider — OpenAI, Gemini, Anthropic, and more. See the [full list of supported providers](https://kestra.io/plugins/plugin-ai/provider). You can swap the provider in your flows without changing anything else.

## Why AI for Workflows?

When building LLM applications and workflows, we often spend significant time writing boilerplate code, searching documentation, and structuring pipelines. AI tools can help us:

- Generate workflows faster: describe what you want in natural language instead of writing YAML from scratch
- Avoid errors: get syntax-correct, up-to-date code that follows best practices
- Automate complex decisions: let AI agents dynamically orchestrate tasks based on changing conditions
- Ground responses in data: use RAG to ensure AI provides accurate, contextual information

However, AI is only as good as the context we provide. This module teaches you how to engineer that context for reliable, production-ready workflows.

## What Makes This Different from AI Assistants?

Traditional AI assistants (like ChatGPT or Gemini in a browser) don't have context about your codebase and workflow patterns, real-time data from your systems, or the latest documentation and best practices.

By integrating AI directly into Kestra and using techniques like RAG and specialized agents, we can provide this context and get much better results.

[← Back to module](../) | [Context Engineering →](02-context-engineering.md)
