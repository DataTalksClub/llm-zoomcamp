## Homework: Monitoring

In module 5 we learned how to monitor our RAG system: capture metrics
from each LLM call, store them in a database, and visualize them on a
dashboard.

In the module we built all of this by hand - a custom dataclass for
the metrics, PostgreSQL for storage, Streamlit and Grafana for
dashboards. That gives you full control, but it's a lot of moving parts.

The industry standard for instrumentation is
[OpenTelemetry](https://opentelemetry.io/) (OTel). Every monitoring
framework we mentioned - Logfire, Langfuse, Arize Phoenix - is built
on top of it. In this homework we use OTel directly. We instrument our
RAG with traces, capture metrics as span attributes, persist the
spans to SQLite, and build a dashboard from the trace data - no Docker, no
separate server, just Python.

We keep using the same course-lessons RAG from homework 1. The
knowledge base is the 72 lesson pages pulled from GitHub, indexed
with minsearch.

> It's possible your answers won't match exactly. If so, select the closest one.

## Setup

Create a fresh project:

```bash
mkdir llm-zoomcamp-hw5 && cd llm-zoomcamp-hw5
uv init --no-workspace
uv add gitsource minsearch openai python-dotenv pandas opentelemetry-api opentelemetry-sdk
```

Download the starter code:

```bash
PREFIX=https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/cohorts/2026/05-monitoring
wget $PREFIX/rag_helper.py
wget $PREFIX/starter.py
```

Put your OpenAI key in a `.env` file:

```
OPENAI_API_KEY=sk-...
```

The starter loads the 72 course lessons, builds a text-search index,
and wraps it in a `RAGBase` instance you can call right away:

```python
from starter import rag

query = "How does the agentic loop keep calling the model until it stops?"
answer = rag.rag(query)
print(answer)
```

For the LLM, we recommend OpenAI with `gpt-5.4-mini`, but you can use
any model and provider you like - just adapt the client accordingly.

## OpenTelemetry setup

OTel needs a few lines of configuration. We use the `ConsoleSpanExporter`,
which prints every span to the terminal. No server, no collector, no
Docker - just output we can read.

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

provider = TracerProvider()
provider.add_span_processor(
    SimpleSpanProcessor(ConsoleSpanExporter())
)
trace.set_tracer_provider(provider)

tracer = trace.get_tracer("llm-zoomcamp")
```

Put this at the top of your script, before any tracing code.

To create a span:

```python
with tracer.start_as_current_span("my_operation") as span:
    # do work
    span.set_attribute("my_key", "my_value")
```

## Q1. First trace

Wrap the `rag()` method so each call produces a span. The simplest way
is to create a `RAGTraced` subclass of `RAGBase` that wraps `rag()`,
`search()`, and `llm()` each in their own span.

Run this query:

> How does the agentic loop keep calling the model until it stops?

How many spans does the trace produce?

* 1
* 3
* 5
* 7

## Q2. Capturing metrics as span attributes

Re-use the trace from Q1. Read the token usage from the LLM response
and set them as attributes on the `llm` span:

```python
span.set_attribute("input_tokens", usage.input_tokens)
span.set_attribute("output_tokens", usage.output_tokens)
```

Also compute the cost and store it as `span.set_attribute("cost", cost)`.

Re-run the query. What are the input tokens?

* 700
* 7000
* 70000
* 700000

> These numbers vary between runs. Pick the closest option.

## Q3. Span timing

Each span automatically records its duration. Look at the console output
from Q1 and find the durations for the `search` span and the `llm` span.

For a typical query, roughly how long does the LLM call take?

* Under 100ms
* 100-500ms
* 500-2000ms
* Over 2000ms

## Q4. Saving traces to SQLite

In the module we saved conversations to PostgreSQL. Here we do the
same thing, but with SQLite (built into Python, zero setup) and with
OTel doing the capturing.

Write a custom `SpanExporter` that saves each finished span to a
SQLite database. The exporter interface is small - it needs an
`export` method that receives a list of `ReadableSpan` objects, plus
`shutdown` and `force_flush` methods:

```python
import sqlite3
from opentelemetry.sdk.trace.export import SpanExporter, SpanExportResult


class SQLiteSpanExporter(SpanExporter):

    def __init__(self, db_path="traces.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS spans (
                name TEXT,
                start_time INTEGER,
                end_time INTEGER,
                input_tokens INTEGER,
                output_tokens INTEGER,
                cost REAL
            )
        """)
        self.conn.commit()

    def export(self, spans):
        for span in spans:
            attrs = dict(span.attributes or {})
            self.conn.execute(
                "INSERT INTO spans VALUES (?, ?, ?, ?, ?, ?)",
                (
                    span.name,
                    span.start_time,
                    span.end_time,
                    attrs.get("input_tokens"),
                    attrs.get("output_tokens"),
                    attrs.get("cost"),
                ),
            )
        self.conn.commit()
        return SpanExportResult.SUCCESS

    def shutdown(self):
        self.conn.close()

    def force_flush(self):
        return True
```

Register it in place of the console exporter:

```python
provider.add_span_processor(
    SimpleSpanProcessor(SQLiteSpanExporter("traces.db"))
)
```

Re-run the query from Q1. How many rows does the `spans` table contain?

* 1
* 3
* 5
* 7

## Q5. Querying trace data

The traces are now in SQLite. Run one more query through the traced
RAG, then query the database.

Using SQL (or pandas), compute the total cost across all `llm` spans
in the database. What's the total cost?

* Under $0.001
* $0.001 - $0.01
* $0.01 - $0.10
* Over $0.10

> The exact number depends on your model. Pick the closest option.

## Q6. Building a dashboard from trace data

Load the SQLite data with pandas and build a simple dashboard - the
same metrics you'd see in Grafana or Streamlit in the module:

- Total number of traces (count `rag` spans)
- Average LLM response time (duration of `llm` spans)
- Total cost
- Average input tokens

What's the average LLM response time?

* Under 500ms
* 500-2000ms
* 2000-5000ms
* Over 5000ms

> The exact number depends on the questions and model. Pick the closest option.
## Going further

We built a custom SQLite exporter to understand how OTel works under
the hood. In practice you rarely instrument everything by hand.

**Collectors and backends.** Instead of writing your own exporter, you
send spans to an
[OTel Collector](https://opentelemetry.io/docs/collector/), which
forwards them to a backend like
[Jaeger](https://www.jaegertracing.io/),
[Tempo](https://grafana.com/oss/tempo/), or a managed service. The
collector handles batching, retries, and routing so your app does not
have to. Jaeger (or Grafana's Tempo) then gives you a UI to browse
traces, filter by span name, and drill into timing - the same things
we did by querying SQLite, but interactive and built for scale.

**Auto-instrumentation.** Most ecosystems have OTel wrappers that add
spans for you. For Python there is
`opentelemetry-instrumentation-openai` and similar libraries for
popular frameworks. You call one or two lines of setup and get LLM
spans, token counts, and tool calls traced automatically - no
subclassing, no manual `set_attribute`.

Frameworks like
[Pydantic Logfire](https://logfire.dev/) build on top of OTel and
take it even further: you get a hosted dashboard, automatic
instrumentation for Pydantic AI agents, and structured logging - all
with minimal code. We used Logfire in the
[dlt workshop homework](../workshops/dlt/homework.md), where we
instrumented an agent and pulled the traces back out with dlt. This
homework is the manual version of the same idea: same OTel standard
underneath, just more hands-on.


## Learning in Public

We encourage everyone to share what they learned. This is called "learning in public".

Read more about the benefits [here](https://alexeyondata.substack.com/p/benefits-of-learning-in-public-and) and in the [course's learning in public guide](https://datatalks.club/docs/courses/zoomcamp-logistics/learning-in-public/).

### Example post for LinkedIn

Tag [@Alexey Grigorev](https://www.linkedin.com/in/agrigorev/) and [@DataTalksClub](https://www.linkedin.com/company/datatalks-club/) in your post - we'll like and comment to give your post more reach.

```
Module 5 of LLM Zoomcamp by @DataTalksClub complete!

Just finished Module 5 - Monitoring. Learned how to:

- Instrument a RAG system with OpenTelemetry
- Capture tokens, cost, and response time as span attributes
- Write a custom SQLite span exporter
- Build a dashboard from trace data

Here's my homework solution: <LINK>

Following along with this amazing free course by @Alexey Grigorev - who else is learning to build with LLMs?

You can sign up here: https://github.com/DataTalksClub/llm-zoomcamp/
```

### Example post for X

```
Module 5 of LLM Zoomcamp done!

- OpenTelemetry instrumentation
- Metrics as span attributes
- Custom SQLite span exporter
- Dashboard from trace data

My solution: <LINK>

Free course by @Al_Grigor & @DataTalksClub: https://github.com/DataTalksClub/llm-zoomcamp/
```

## Submit the results

* Submit your results here: https://courses.datatalks.club/llm-zoomcamp-2026/homework/hw5
* It's possible your answers won't match exactly. If so, select the closest one.
