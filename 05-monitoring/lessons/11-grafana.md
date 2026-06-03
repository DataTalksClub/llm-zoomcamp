# Grafana Dashboards

Grafana is a dashboard tool that visualizes data from databases. We
already store conversations in PostgreSQL. We can build dashboards
that show what's happening in our system in real time.

## Starting Grafana with Docker

Start Grafana on the same network with a volume for data persistence:

```bash
docker run -d \
    --name grafana \
    --network monitoring \
    -p 3000:3000 \
    -v grafana_data:/var/lib/grafana \
    grafana/grafana
```

We already created the network and started PostgreSQL on it in the
database lesson.

Access Grafana at `http://localhost:3000` (login: admin / admin).

## Setting up the data source

Connect Grafana to PostgreSQL:

1. Go to Configuration > Data Sources > Add data source
2. Select PostgreSQL
3. Fill in the connection details:
   - Host: `course-assistant-pg:5432`
   - Database: `course_assistant`
   - User: `user`
   - Password: `password`
   - SSL Mode: disable
4. Click Save & Test. It should say "Database Connection OK"

## Creating the dashboard

Create a new dashboard. We'll add panels one by one. Each panel has a
SQL query that Grafana runs against PostgreSQL.

Grafana provides special SQL variables for time-based filtering:

- `$__timeFrom()`: start of the selected time range
- `$__timeTo()`: end of the selected time range
- `$__timeGroup(column, interval)`: groups results by time intervals

These let the user select "last 30 minutes" or "last 6 hours" and the
queries automatically filter to that range.

## Response Time Panel

Shows how long the LLM takes to respond over time:

```sql
SELECT
  timestamp AS time,
  response_time
FROM conversations
WHERE timestamp BETWEEN $__timeFrom() AND $__timeTo()
ORDER BY timestamp
```

Use the Time series visualization for this panel.

## Token Usage Panel

Shows token consumption over time:

```sql
SELECT
  $__timeGroup(timestamp, $__interval) AS time,
  AVG(total_tokens) AS avg_tokens
FROM conversations
WHERE timestamp BETWEEN $__timeFrom() AND $__timeTo()
GROUP BY 1
ORDER BY 1
```

Use the Time series visualization for this panel.

## Cost Panel

Shows cumulative cost over time:

```sql
SELECT
  $__timeGroup(timestamp, $__interval) AS time,
  SUM(cost) AS total_cost
FROM conversations
WHERE timestamp BETWEEN $__timeFrom() AND $__timeTo()
  AND cost > 0
GROUP BY 1
ORDER BY 1
```

Use the Time series visualization for this panel.

## Model Usage Panel

Shows which models are being used:

```sql
SELECT
  model,
  COUNT(*) as count
FROM conversations
WHERE timestamp BETWEEN $__timeFrom() AND $__timeTo()
GROUP BY model
```

Use a Bar chart for this panel.

## Recent Conversations Panel

Shows the last 5 conversations in a table:

```sql
SELECT
  timestamp AS time,
  question,
  answer,
  response_time,
  cost
FROM conversations
WHERE timestamp BETWEEN $__timeFrom() AND $__timeTo()
ORDER BY timestamp DESC
LIMIT 5
```

Panel type: Table

## Dashboard settings

Set the dashboard to auto-refresh every 30 seconds so the data stays
current. You can also set the default time range to "Last 6 hours".

Arrange the panels in a layout that makes sense:

- Top row: recent conversations table (wide)
- Middle row: model usage bar chart
- Bottom row: response time | token usage | cost

This dashboard gives you a clear view of system performance. It covers
response speed, cost, and model popularity at a glance.

[← Synthetic Data](10-synthetic-data.md) | [Docker Compose →](12-docker-compose.md)
