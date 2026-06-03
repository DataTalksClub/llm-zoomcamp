# Next Steps

In this module, we built a monitoring system for our RAG pipeline:

- Streamlit app for the user interface
- Metrics capture with LLMCallRecord
- PostgreSQL for storing conversations
- Grafana dashboards for real-time monitoring
- Docker Compose to run everything together

This is a basic setup.

For production, consider:

- OpenTelemetry for standardized observability across services
- Prometheus for metrics collection alongside Grafana
- Alerting rules in Grafana to get notified when metrics drop
- User session tracking to understand conversation flows

The 2024 cohort used Elasticsearch instead of minsearch, and included
Ollama for local models. If you're interested in that setup, see
[2024 monitoring module](../cohorts/2024/04-monitoring/).

## To learn more

For additional resources:

- Cohorts and materials:
  - 2024 cohort monitoring module:
    [2024/04-monitoring](../cohorts/2024/04-monitoring/)

[← Docker Compose](13-docker-compose.md) | [Back to module →](../)
