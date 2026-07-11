# Homework: dlt

In this homework we will take the FAQ agent from Module 1,
instrument it with [Pydantic Logfire](https://logfire.dev) for
observability,
then pull the trace data back out with dlt and analyze it.

In Module 1 we wrote the agent loop by hand and then we saw toyaikit - 
an agentic framework.

For this homework we rewrote into [Pydantic AI](https://ai.pydantic.dev/),
so it's easier to integrate it with Logfire. Pydantic AI and Logfire
work really well together, that's why we use them here.

In Module 5 we learn about monitoring and observability, and implement 
our own monitoring solution. Logfire is an alternative for that.

## Getting the code

The rewritten agent is in the [homework/](homework/) directory. Download
it with `wget`:

```bash
PREFIX=https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/cohorts/2026/workshops/dlt/homework

wget $PREFIX/agent.py
wget $PREFIX/ingest.py
wget $PREFIX/main.py
wget $PREFIX/.env.example -O .env
```

The agent code is in [homework/agent.py](homework/agent.py). Here we use
Pydantic AI which we didn't cover previously.
Conceptually there's nothing new: we covered everything already in module 1.
The comments in the file will explain what's happening and how things map to
what we learned previously.

Make sure to read through it before proceeding.

## Setup

We start by configuring our project:

```bash
uv init
uv add openai minsearch requests python-dotenv pydantic-ai logfire
uv add "dlt[duckdb]"
```

Open `.env` and add your `OPENAI_API_KEY`:

```bash
OPENAI_API_KEY=sk-YOUR_KEY_HERE
```

Make sure it's in `.gitignore`:

```
.env
```

You can use any other provider instead of OpenAI. Check Pydantic AI documentation
to see how you can use your provider.

Verify that the agent runs:

```bash
uv run python main.py
```

## Question 1. Instrument the agent with Logfire

Sign up for a free [Logfire](https://logfire.dev) account, create a
project, and generate a write token. Put it in `.env` as
`LOGFIRE_TOKEN`.

Instrument the agent:

```python
logfire.configure()
logfire.instrument_pydantic_ai()
```

Run the agent a few times with different questions and open your
project on Logfire to see the traces.

For the following query

> How do I run Ollama locally?

how many spans does a single agent run produce?

Each span is either the agent run itself, an LLM call, or a tool call.
The number can vary between runs because the model decides how many
times to search.

* 1
* 5
* 15
* 30

## Question 2. Load traces into DuckDB with dlt

Generate a read token for your Logfire project and set it as
`LOGFIRE_READ_TOKEN` in `.env`.

Initialize a dlt-hub project like in the workshop. Then ask your coding
agent to pull the data from Pydantic Logfire and save it into DuckDB.

The dltHub AI workbench has a ready-made context for Logfire. Point your
agent to it: https://dlthub.com/context/source/logfire

If you don't currently use a coding agent, you can use something like OpenCode:
you should be able to complete one session with the free account.

Alternatively, you can do it in the old way (using ChatGPT or your favorite search engine).

If you don't currently use a coding agent, you can use something like OpenCode:
you should be able to complete one session with the free account. 

Alternatively, you can do it in the old way (using ChatGPT or your favorite search engine).

The logfire traces contain deeply nested JSON (span attributes with
LLM messages, tool calls, token usage, etc.). dlt automatically
normalizes this into a set of tables - one for the main records, plus
child tables for each nested level.

How many tables did dlt create? Check with:

```sql
SELECT COUNT(*) FROM information_schema.tables 
WHERE table_schema = 'agent_traces';
```

* 1
* 3
* 24
* 100

## Question 3. Query traces with an agent

Using a coding agent (you can also write the code by hand) find the
input token usage for the agent run from Q1.

The token counts are stored in the span attributes as
`gen_ai.usage.input_tokens`. Sum them across all LLM calls within the
trace. The number depends on how many searches the agent made, so
report the range it falls into:

* 100 - 500
* 1500 - 5000
* 10000 - 20000
* 50000 - 100000

## Submit the results

* Submit your results here: https://courses.datatalks.club/llm-zoomcamp-2026/homework/dlt
