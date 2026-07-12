## Homework: Monitoring

In module 5 we learned how to monitor our RAG system: capture metrics
from each LLM call, store them in a database, and visualize them on a
dashboard.

In the module we built all of this by hand - a custom dataclass for
the metrics, PostgreSQL for storage, Streamlit and Grafana for
dashboards.

In this homework, we will explore an alternative: [OpenTelemetry](https://opentelemetry.io/) (OTel).
This is the industry standard for code instrumentation. Every monitoring
framework we mentioned is built
on top of it - like Logfire, Langfuse, Arize Phoenix and others.

In this homework we will use OTel directly. We will instrument our
RAG with traces, capture metrics as span attributes, persist the
spans to SQLite, and build a dashboard from the trace data.

We keep using the same course-lessons RAG from homework 1. The
knowledge base is the 72 lesson pages pulled from GitHub, indexed
with minsearch.

> It's possible your answers won't match exactly. If so, select the closest one.

## Setup

Create a fresh project:

```bash
mkdir llm-zoomcamp-hw5 && cd llm-zoomcamp-hw5
uv init
uv add gitsource minsearch openai python-dotenv
```

We want everyone to start with the same code, so we prepared a starter package.

Download it:

```bash
PREFIX=https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/cohorts/2026/05-monitoring
wget $PREFIX/rag_helper.py
wget $PREFIX/starter.py
```

We keep things simpler and focus only on RAG. However, all the concepts could be directly translated to agents.

Next, you need to put your OpenAI key in a `.env` file:

```
OPENAI_API_KEY=sk-...
```

Like previously, you can use any alternative you want.

The starter loads the 72 course lessons, builds a text-search index,
and wraps it in a `RAGBase` instance you can call right away:

```python
from starter import rag

query = "How does the agentic loop keep calling the model until it stops?"
answer = rag.rag(query)
print(answer)
```

For the LLM, we recommend OpenAI with `gpt-5.4-mini`, but you can use
any model and provider you want.

## OpenTelemetry setup

First, install the OpenTelemetry libraries:

```bash
uv add opentelemetry-api opentelemetry-sdk
```

`opentelemetry-api` is the interface - the classes and functions you
import in your code (`trace`, `Tracer`, `Span`). `opentelemetry-sdk`
is the implementation that actually creates and processes spans.
Without the SDK, the API calls do nothing. Together they let you
instrument code without tying yourself to any particular backend.

Before we configure OTel, a few concepts:

- A **trace** is the end-to-end story of a single request as it moves
  through your system - for us, one RAG call.
- A **span** is one operation within a trace. A trace is made of one
  or more spans, organized as a tree. Each span has a name, a start
  and end time, and a set of attributes.
- **Attributes** are key-value pairs attached to a span - anything you
  want to record, like the number of tokens used or the cost of a call.

Spans are not visible by themselves. When a span finishes, OTel hands
it to a **span processor**, which passes it to an **exporter**. The
exporter decides where the span goes - to the console, to a file, to
a database, or to a remote collector.

We start with the `ConsoleSpanExporter`, which prints each finished
span to the terminal so we can see what OTel captures:

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

Here is what each line does:

- `TracerProvider()` creates the SDK's central configuration object.
  It owns the span processors and decides how spans are built.
- `SimpleSpanProcessor(ConsoleSpanExporter())` wires a processor that
  forwards every finished span to the console exporter, one at a time.
  "Simple" means synchronous and immediate - good for development.
- `trace.set_tracer_provider(provider)` registers the provider
  globally, so every call to `trace.get_tracer(...)` returns a tracer
  backed by it.
- `trace.get_tracer("llm-zoomcamp")` returns a `Tracer` we use to
  create spans. The string is just a label for the instrumentation
  scope - it identifies which part of the code produced the spans.

Put this block at the top of your script, before you import or use
`starter` - so the tracer provider is ready before any code that
might create spans.

With the tracer in hand, you can wrap any block of code in a span:

```python
with tracer.start_as_current_span("my_operation") as span:
    # your code here
    span.set_attribute("my_key", "my_value")
```

`start_as_current_span` creates a new span and makes it the "current"
span for the duration of the `with` block. Any code inside the block -
including other calls to `start_as_current_span` - becomes a child of
this span. When the block exits, the span ends automatically.

You will use this pattern to instrument the RAG methods in the
questions below.

## Q1. First trace

Wrap the `rag()` method so each call produces a span. The simplest way
is to create a `RAGTraced` subclass of `RAGBase` that wraps `rag()`,
`search()`, and `llm()` each in their own span.

Run this query:

> How does the agentic loop keep calling the model until it stops?

The console exporter prints every finished span as a dictionary.
Count the spans in the console output - each one is a separate
`ReadableSpan` entry. How many spans does the trace produce?

* 1
* 3
* 5
* 7

## Q2. Capturing metrics as span attributes

Spans are not just timing markers - you can attach any information you
want to them with `set_attribute`. We already use spans to record how
long each step takes. Now we'll add the metrics we care about: tokens
and cost.

Read the token usage from the LLM response (the `llm()` method in the
starter already returns the raw response object) and set them as
attributes on the `llm` span:

```python
span.set_attribute("input_tokens", usage.input_tokens)
span.set_attribute("output_tokens", usage.output_tokens)
```

You can get the usage object from the response:

```python
response = self.llm_client.responses.create(...)
usage = response.usage
```

And since we know both input and output tokens, we can also compute
the cost using the code from the previous modules.

Now re-run the query. How many input tokens do we see?

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

Right now the spans are printed to the terminal and then gone. We want
to persist them so we can query them later - the same idea as saving
conversations to PostgreSQL in the module, but lighter.

In this homework, we'll use SQLite. It's built into Python, needs no
server, and stores data in a single file.

We don't change our instrumentation code at all. Instead, we write a
custom exporter - a class that receives finished spans and writes them
to the database. OTel calls the exporter through the same span
processor we already use; we just swap the destination.

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
