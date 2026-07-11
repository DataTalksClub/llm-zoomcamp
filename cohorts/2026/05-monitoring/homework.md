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
RAG with traces, capture metrics as span attributes, and build a
dashboard from the trace data - all without a database or a separate
dashboard server.

We keep using the same course-lessons RAG from homework 1. The
knowledge base is the 72 lesson pages pulled from GitHub, indexed
with minsearch.

> It's possible your answers won't match exactly. If so, select the closest one.

## Setup

Create a fresh project:

```bash
mkdir llm-zoomcamp-hw5 && cd llm-zoomcamp-hw5
uv init --no-workspace
uv add gitsource minsearch openai python-dotenv opentelemetry-api opentelemetry-sdk
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

## Q4. Instrumenting the judge

In the module we built an LLM judge that checks whether the answer is
relevant. We do the same here, and we trace it.

Create a judge using structured output (the same approach as in module
4 and the monitoring lesson). Wrap the judge call in a span and set the
relevance verdict as a span attribute:

```python
with tracer.start_as_current_span("judge") as span:
    relevance, explanation = evaluate_relevance(question, answer)
    span.set_attribute("relevance", relevance)
```

Run the judge on the answer from Q1. Keep the result - we'll re-use the
judge setup in Q5.

What's the relevance verdict?

* RELEVANT
* PARTLY_RELEVANT
* NON_RELEVANT

## Q5. Batch traces and total cost

Download the ground-truth questions from homework 4 (if you don't have
them already):

```bash
PREFIX=https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main
wget ${PREFIX}/cohorts/2026/04-evaluation/ground-truth.csv
```

Run the traced RAG on the first 5 questions from the ground truth, and
run the judge on each answer. Use an in-memory span exporter instead of
the console exporter so you can read the spans
programmatically:

```python
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter

memory_exporter = InMemorySpanExporter()
provider.add_span_processor(SimpleSpanProcessor(memory_exporter))
```

After running, read the finished spans and sum up the `cost` attribute
across all LLM spans (RAG + judge). What's the total cost?

* $0.001
* $0.01
* $0.10
* $1.00

> The exact number depends on your model. Pick the closest option.

## Q6. Building a dashboard from trace data

Re-use the spans from Q5. Export them to a JSON file, load it with
pandas, and compute the same metrics you'd see on a Grafana panel:

- Total conversations
- Average response time (from span durations)
- Total cost
- Relevance distribution

How many of the 5 answers did the judge classify as RELEVANT?

* 0-1
* 2-3
* 4-5
* All 5

> The exact number depends on the questions and model. Pick the closest option.

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
- Trace an LLM judge for relevance evaluation
- Build a dashboard from trace data - no database needed

Here's my homework solution: <LINK>

Following along with this amazing free course by @Alexey Grigorev - who else is learning to build with LLMs?

You can sign up here: https://github.com/DataTalksClub/llm-zoomcamp/
```

### Example post for X

```
Module 5 of LLM Zoomcamp done!

- OpenTelemetry instrumentation
- Metrics as span attributes
- Traced LLM judge
- Dashboard from trace data

My solution: <LINK>

Free course by @Al_Grigor & @DataTalksClub: https://github.com/DataTalksClub/llm-zoomcamp/
```

## Submit the results

* Submit your results here: https://courses.datatalks.club/llm-zoomcamp-2026/homework/hw5
* It's possible your answers won't match exactly. If so, select the closest one.
