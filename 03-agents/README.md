# Module 3: Agents

In modules 1 and 2, we built RAG pipelines with keyword search and
vector search. The pipeline was always fixed: search once, build a
prompt, send to the LLM. But what if the search doesn't find what we
need? What if the user makes a typo?

Agents give the LLM the ability to decide what to do. Instead of a
fixed pipeline, the LLM chooses which tools to call, when to call them,
and when to stop and give the final answer.

In this module, we will:

- Revise the RAG pipeline from module 1
- Understand what agents are and how they differ from standard RAG
- Implement function calling with the OpenAI Responses API
- Build the agentic loop from scratch
- Use ToyAI Kit as a teaching framework


## Lessons

1. [Introduction](lessons/01-intro.md) - What we'll cover in this module
2. [Quick RAG Revision](lessons/02-rag-revision.md) - Setting up the RAG pipeline from module 1
3. [What Are Agents?](lessons/03-agents-concept.md) - Conceptual overview of agents vs RAG
4. [Function Calling](lessons/04-function-calling.md) - Giving the LLM tools it can use
5. [The Agentic Loop](lessons/05-agentic-loop.md) - Repeating until the model stops calling tools
6. [ToyAIKit](lessons/06-frameworks.md) - A teaching framework for the agent loop
7. [Other Frameworks](lessons/07-other-frameworks.md) - Production frameworks worth exploring


## Old content

See old materials in [2024](../cohorts/2024/) and [2025](../cohorts/2025/) cohorts.
