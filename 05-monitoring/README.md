# Module 5: Monitoring

How do you know if your RAG system is performing well after deployment?
This module covers online monitoring: collecting metrics from real users
and visualizing them on a dashboard.

We build a Streamlit chat app, capture metrics, store conversations
in PostgreSQL, and create Grafana dashboards for real-time monitoring.


## Lessons

1. [Intro](lessons/01-intro.md) - Why monitoring matters, what we'll build
2. [Chat App](lessons/02-chat-app.md) - Basic Streamlit app with RAG
3. [Capturing Metrics](lessons/03-metrics.md) - LLMCallRecord, cost tracking
4. [Database](lessons/04-database.md) - PostgreSQL with Docker, saving conversations
5. [Querying Data](lessons/05-querying.md) - Fetching stored conversations
6. [Streamlit Dashboard](lessons/06-streamlit-dashboard.md) - Visualizing metrics in Streamlit
7. [User Feedback](lessons/07-user-feedback.md) - Thumbs up/down buttons
8. [Built-in Judge](lessons/08-built-in-judge.md) - LLM-as-a-judge for automatic relevance evaluation
9. [Grafana Dashboards](lessons/09-grafana.md) - SQL queries and dashboard panels
10. [Docker Compose](lessons/10-docker-compose.md) - Running everything together
11. [Synthetic Data](lessons/11-synthetic-data.md) - Generating test data for dashboards
12. [Next Steps](lessons/12-next-steps.md) - OpenTelemetry, alerting, further reading


## Older content

- [2024 edition](../cohorts/2024/04-monitoring/)
- [2025 edition](../cohorts/2025/04-monitoring/)
