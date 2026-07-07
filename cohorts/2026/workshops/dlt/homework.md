# Homework: dlt + Logfire

We take the FAQ agent from Module 1, instrument it with Pydantic Logfire,
then pull the trace data back out with dlt and analyze it.

In Module 1 we wrote the agent loop by hand.

Here we rewrite it with [Pydantic AI](https://ai.pydantic.dev/), a
lightweight agent framework. Tools are plain Python functions. The
function-calling loop from Module 1 is built in: you register a tool,
call `run_sync()`, and the agent decides when to search and when to
answer.

Later, in Question 1, we add [Pydantic Logfire](https://logfire.dev)
for observability.

Pydantic AI and Logfire work really well together, that's why we use
them here.

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
Pydantic AI which we didn't cover previously. But the comments in the file
explain what's happening and how things map to what we built in Module 1.

Make sure to read through it before proceeding.

## Setup

Now let's configure out project

```bash
uv init --no-readme
uv add openai minsearch requests python-dotenv pydantic-ai logfire
uv add "dlt[duckdb]"
```

Open `.env` and add your `OPENAI_API_KEY`:

```bash
OPENAI_API_KEY=sk-YOUR_KEY_HERE
```

You can use any other provider instead of OpenAI. Check Pydantic AI documentation
to see how you can use your provider.

Verify that the agent runs:

```bash
uv run python main.py
```

## Question 1. Instrument the agent with Logfire

Sign up for a free [Logfire](https://logfire.dev) account, create a
project, and generate a **write token**. Put it in `.env` as
`LOGFIRE_TOKEN`.

Instrument the agent:

1. Add `logfire.configure()` to `main.py` to connect to your project.
2. Call `logfire.instrument_pydantic_ai()` so every agent run, LLM
   call, and tool call is captured automatically as nested spans.

Run the agent a few times with different questions and open your
project on logfire.dev to see the traces.

**Question:** In the Logfire UI, how many spans does a single agent
run produce for the question "How do I run Ollama locally?" Count the
top-level agent span plus all nested spans (LLM calls, tool calls).

## Question 2. Load traces into DuckDB with dlt

Generate a **read token** for your Logfire project and set it as
`LOGFIRE_READ_TOKEN` in `.env`.

Write a dlt pipeline that pulls your trace data into DuckDB using
`LogfireQueryClient`. The query API exposes your traces as a `records`
table that you can query with SQL:

```python
from logfire.experimental.query_client import LogfireQueryClient

with LogfireQueryClient(read_token) as client:
    result = client.query_json_rows(
        sql="SELECT * FROM records WHERE start_timestamp > now() - INTERVAL '7 days'",
        min_timestamp=...,
    )
    rows = result['rows']
```

Wrap that in a `@dlt.resource` and run it through a pipeline into
DuckDB.

**Question:** How many rows did dlt load into your table? Check the
dlt trace output or query DuckDB directly.

## Question 3. Query traces with an agent

Write a script (or ask your coding agent) to query your Logfire data
using the read token and answer: what is the total token usage (input
+ output) across all LLM calls from Question 1?

The token counts live in the span attributes as
`gen_ai.usage.input_tokens` and `gen_ai.usage.output_tokens`.

**Question:** What is the total number of tokens (input + output
combined) consumed across all your agent runs?

## Question 4. Estimate the cost

Using the token counts from Question 3, estimate the total cost of
running the agent.

Assume `gpt-5.4-mini` pricing: $0.15 per 1M input tokens, $0.60 per
1M output tokens.

**Question:** What is the estimated total cost in USD?

## Submit the results

* Submit your results here: https://courses.datatalks.club/llm-zoomcamp-2026/homework/dlt
