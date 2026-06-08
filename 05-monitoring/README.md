# Module 5: Monitoring

Offline evaluation can't tell you how your RAG system performs once real
people use it. This module covers online monitoring: collecting metrics
from real traffic and visualizing them on a dashboard.

We build a Streamlit chat app, capture metrics, store conversations
in PostgreSQL, and create Grafana dashboards for real-time monitoring.

## Lessons

Work through them in order:

1. [Intro](lessons/01-intro.md) - Why monitoring matters, what we'll build
2. [Assistant Setup](lessons/02-assistant-setup.md) - Setting up the RAG assistant
3. [Chat App](lessons/03-chat-app.md) - Basic Streamlit app with RAG
4. [Capturing Metrics](lessons/04-metrics.md) - LLMCallRecord, cost tracking
5. [Database](lessons/05-database.md) - PostgreSQL with Docker, saving conversations
6. [Querying Data](lessons/06-querying.md) - Fetching stored conversations
7. [Streamlit Dashboard](lessons/07-streamlit-dashboard.md) - Visualizing metrics in Streamlit
8. [User Feedback](lessons/08-user-feedback.md) - Thumbs up/down buttons
9. [Built-in Judge](lessons/09-built-in-judge.md) - LLM-as-a-judge for automatic relevance evaluation
10. [Feedback Dashboard](lessons/10-feedback-dashboard.md) - Adding feedback panels to the Streamlit dashboard
11. [Synthetic Data](lessons/11-synthetic-data.md) - Generating test data for dashboards
12. [Grafana Dashboards](lessons/12-grafana.md) - SQL queries and dashboard panels
13. [Docker Compose](lessons/13-docker-compose.md) - Running everything together
14. [Next Steps](lessons/14-next-steps.md) - OpenTelemetry, alerting, frameworks to learn more


## Homework

- [Homework](../cohorts/2026/05-monitoring/homework.md)


## Original workshop recording

This module was taught as a live workshop, which we chopped into the
per-lesson videos above. To watch the full uncut recording:

- [Monitoring LLM Applications: Traces, Feedback, and Production Quality](https://www.youtube.com/watch?v=ImY5-Q97sRw)


## Older content

Earlier cohorts ran this module with a different stack:

- [2024 edition](../cohorts/2024/04-monitoring/)
- [2025 edition](../cohorts/2025/04-monitoring/)
