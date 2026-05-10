# Module 5: Monitoring

How do you know if your RAG system is performing well after deployment?
This module covers online monitoring: collecting metrics from real users
and visualizing them on a dashboard.

We build a Streamlit chat app with feedback buttons, store conversations
in PostgreSQL, and create Grafana dashboards for real-time monitoring.


## Lessons

1. [Intro](lessons/01-intro.md) - Why monitoring matters, what we'll build
2. [Chat App with Feedback](lessons/02-chat-app.md) - Streamlit app with RAG and thumbs up/down
3. [Database](lessons/03-database.md) - PostgreSQL schema for conversations and feedback
4. [Docker Compose](lessons/04-docker-compose.md) - Running PostgreSQL, Streamlit, and Grafana together
5. [Grafana Dashboards](lessons/05-grafana.md) - SQL queries and dashboard panels
6. [Synthetic Data](lessons/06-synthetic-data.md) - Generating test data for dashboards
7. [Next Steps](lessons/07-next-steps.md) - OpenTelemetry, alerting, further reading


## Older content

- [2024 edition](../cohorts/2024/04-monitoring/)
- [2025 edition](../cohorts/2025/04-monitoring/)
