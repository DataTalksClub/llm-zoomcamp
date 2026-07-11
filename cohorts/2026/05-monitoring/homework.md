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

``+OPENAI_API_KEY=sk-...
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

Right now the `llm()` method returns the raw response object. Read the
token usage from it and set them as attributes on the LLM span:

```python
span.set_attribute("input_tokens", usage.input_tokens)
span.set_attribute("output_tokens", usage.output_tokens)
```

Also compute the cost and store it as `span.set_attribute("cost", cost)`.

Run the same query as Q1. What are the input tokens?

* 700
* 7000
* 70000
* 700000

> These numbers vary between runs. Pick the closest option.

## Q3. Span timing

Each span automatically records its duration. Look at the console output
from Q2 and find the durations for the `search` span and the `llm` span.

For a typical query, roughly how much time does the LLM call take
compared to the search?

* About the same
* Search is much slower
* The LLM call is much slower
* Both are under 10ms

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

Run the judge on the answer from Q1. What's the relevance verdict?

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

Run the traced RAG on the first 5 questions. Instead of the console
exporter, use an in-memory span exporter so you can read the spans
programmatically:

```python
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.exporter.otlp.proto.common import (
    InMemorySpanExporter,
)

# In-memory exporter instead of console
memory_exporter = InMemorySpanExporter()
provider.add_span_processor(
    SimpleSpanProcessor(memory_exporter)
)
```

After running the 5 questions, read the finished spans and sum up the
`cost` attribute across all LLM spans. What's the total cost?

* $0.001
* $0.01
* $0.10
* $1.00

> The exact number depends on your model. Pick the closest option.

## Q6. Building a dashboard from trace data

Instead of the console or in-memory exporter, export the spans to a
JSON file. Write a small script that:

1. Runs the traced RAG on 10 questions from the ground truth
2. Runs the judge on each answer
3. Collects all spans
4. Saves them to a `traces.json` file

Then load the JSON with pandas and compute the same metrics you'd see
on a dashboard:

- Total conversations
- Average response time (from span durations)
- Total cost
- Relevance distribution

What's the relevance distribution (count of each verdict)?

* Mostly RELEVANT
* Mostly PARTLY_RELEVANT
* Mostly NON_RELEVANT
* Evenly split

> The exact distribution depends on the questions and model. Pick the
> closest description.

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

