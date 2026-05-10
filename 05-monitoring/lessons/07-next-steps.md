# Next Steps

In this module, we built a monitoring system for our RAG pipeline:

- Streamlit app for the user interface with feedback buttons
- PostgreSQL for storing conversations and feedback
- Docker Compose to run everything together
- Grafana dashboards for real-time monitoring

This is a basic setup. For production, consider:

- OpenTelemetry for standardized observability across services
- Prometheus for metrics collection alongside Grafana
- Alerting rules in Grafana to get notified when metrics drop
- User session tracking to understand conversation flows

The 2024 cohort used Elasticsearch instead of minsearch, and included
Ollama for local models. If you're interested in that setup, see
[2024 monitoring module](../cohorts/2024/04-monitoring/).


## Further reading

- Cohorts and materials:
  - 2024 cohort monitoring module:
    [2024/04-monitoring](../cohorts/2024/04-monitoring/)


[<< Previous: Synthetic Data](06-synthetic-data.md)
|
[Back to module](../)
