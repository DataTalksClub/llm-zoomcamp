# Next Steps

Video: [Watch this lesson](https://www.youtube.com/watch?v=GpQeAniVGfk&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

Let's recap what we did. We took the RAG pipeline from the earlier
modules and wrapped it in a simple Streamlit interface. We started
recording every interaction to PostgreSQL.

On top of that data we built a dashboard, first in Streamlit and then in
Grafana. It tracks response time, cost, tokens, and which models we use.
Then we added two quality signals: an LLM judge, plus thumbs up and down
from users.

We now have two things we didn't have before. We have visibility into how
the system behaves, and we have logs to dig into when something looks
wrong.

## Build it yourself, or use a framework

Doing the instrumentation by hand gives you total flexibility. You
capture exactly what you want and store it where you want. You don't
always need that much control, though.

Several tools are built for this and take the wiring off your hands:

- [Langfuse](https://langfuse.com/) and
  [Arize Phoenix](https://phoenix.arize.com/) trace LLM apps.
- [Pydantic Logfire](https://pydantic.dev/logfire) is my favorite for
  monitoring. It instruments your code and gives you a dashboard with the
  metrics already wired up, so you write almost nothing.
- [Evidently](https://www.evidentlyai.com/) works for both monitoring and
  evaluation. I mostly reach for it on the eval side.

The automatic tools have a flip side. You get a dashboard for free, but
you don't always know what they capture. And changing something means
digging into the framework. So it's a real tradeoff: hand-rolling gives
you control, frameworks give you speed. Try a couple and see which you
like.

## Going to production

What we built is a minimal example to show the concepts, not a production
setup. Two things in particular change at scale.

The first is overhead. Each call now writes to the database, and the
judge adds another LLM call. In production you'd do this asynchronously so
it doesn't slow down the user's request. You capture into a queue and
process it separately.

The second is storage. Postgres is fine for us, but it isn't the best
place to store high-volume logs. A common pattern is to push events to
something like Kafka and let downstream systems store them.

[OpenTelemetry](https://opentelemetry.io/) is the standard worth knowing
here. It's the instrumentation layer that tools like Logfire and Langfuse
build on, and it's simple to set up. Conceptually your system will look
like what we built. The technology behind it will likely be something
else.

## Homework

We only covered RAG, so pick one of these to take it further:

- Monitor an agent. Apply the same instrumentation to an agent from the
  [agents module](../../01-agentic-rag/), capturing each tool call the
  way we captured LLM calls.
- Generate synthetic data and watch the Grafana dashboard fill out, as in
  the synthetic data lesson.
- Move everything to Docker Compose so the whole stack starts with one
  command.

## Older content

The 2024 cohort used Elasticsearch instead of minsearch and ran Ollama
for local models. If that setup is useful to you, see the
[2024 monitoring module](../../cohorts/2024/04-monitoring/).

[← Docker Compose](13-docker-compose.md) | [Back to module →](../)
