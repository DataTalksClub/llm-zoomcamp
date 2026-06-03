# Monitoring

In module 04, we evaluated our system offline, before deployment. We
measured search quality with Hit Rate and MRR, and answer quality with
cosine similarity and LLM-as-a-judge.

After we deploy, users ask questions and the system gives answers. But we
have no idea if the answers are good. Offline evaluation doesn't tell us
how the system performs with real users.

That's where monitoring comes in. Monitoring is online evaluation,
collecting metrics from a running system to track its health and quality.

There are several things we want to monitor:

- User feedback: thumbs up / thumbs down on answers
- Response time: how long the LLM takes to answer
- Relevance: is the answer relevant to the question?
- Token usage and cost: how much are we spending?
- Model usage: which models are being used?

To collect this data, we need:

- A user interface where users can interact with the system
- A database to store conversations and feedback
- A dashboard to visualize the metrics

In this module, we'll build all three. We'll use Streamlit for the UI,
PostgreSQL for the database, and Grafana for the dashboard.

We'll cover:

- Building a chat app with Streamlit and feedback buttons
- Storing conversations and feedback in PostgreSQL
- Docker Compose to run everything together
- Grafana dashboards with SQL queries
- Generating synthetic data to test dashboards

[← Back to module](../) | [Assistant →](02-assistant-setup.md)
