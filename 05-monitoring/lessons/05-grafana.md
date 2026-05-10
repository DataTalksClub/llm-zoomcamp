# Grafana Dashboards

Grafana is a dashboard tool that visualizes data from databases. We
already store conversations and feedback in PostgreSQL, so we can build
dashboards that show what's happening in our system in real time.


## Setting up the data source

1. Open Grafana at `http://localhost:3000`
2. Login with admin / admin
3. Go to Configuration > Data Sources > Add data source
4. Select PostgreSQL
5. Fill in the connection details:
   - Host: `postgres:5432`
   - Database: `course_assistant`
   - User: `user`
   - Password: `password`
   - SSL Mode: disable
6. Click Save & Test -- it should say "Database Connection OK"


## Creating the dashboard

Create a new dashboard. We'll add panels one by one. Each panel has a
SQL query that Grafana runs against PostgreSQL.

Grafana provides special SQL variables for time-based filtering:

- `$__timeFrom()` -- start of the selected time range
- `$__timeTo()` -- end of the selected time range
- `$__timeGroup(column, interval)` -- groups results by time intervals

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

Panel type: Time series


## Relevance Distribution Panel

Shows how many answers are RELEVANT, PARTLY_RELEVANT, or NON_RELEVANT:

```sql
SELECT
  relevance,
  COUNT(*) as count
FROM conversations
WHERE timestamp BETWEEN $__timeFrom() AND $__timeTo()
GROUP BY relevance
```

Panel type: Gauge or Pie chart


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

Panel type: Time series


## OpenAI Cost Panel

Shows cumulative cost over time:

```sql
SELECT
  $__timeGroup(timestamp, $__interval) AS time,
  SUM(openai_cost) AS total_cost
FROM conversations
WHERE timestamp BETWEEN $__timeFrom() AND $__timeTo()
  AND openai_cost > 0
GROUP BY 1
ORDER BY 1
```

Panel type: Time series


## Model Usage Panel

Shows which models are being used:

```sql
SELECT
  model_used,
  COUNT(*) as count
FROM conversations
WHERE timestamp BETWEEN $__timeFrom() AND $__timeTo()
GROUP BY model_used
```

Panel type: Bar chart


## Recent Conversations Panel

Shows the last 5 conversations in a table:

```sql
SELECT
  timestamp AS time,
  question,
  answer,
  relevance
FROM conversations
WHERE timestamp BETWEEN $__timeFrom() AND $__timeTo()
ORDER BY timestamp DESC
LIMIT 5
```

Panel type: Table


## Feedback Statistics Panel

Shows thumbs up vs thumbs down:

```sql
SELECT
  SUM(CASE WHEN feedback > 0 THEN 1 ELSE 0 END) as thumbs_up,
  SUM(CASE WHEN feedback < 0 THEN 1 ELSE 0 END) as thumbs_down
FROM feedback
WHERE timestamp BETWEEN $__timeFrom() AND $__timeTo()
```

Panel type: Pie chart


## Dashboard settings

Set the dashboard to auto-refresh every 30 seconds so the data stays
current. You can also set the default time range to "Last 6 hours".

Arrange the panels in a layout that makes sense. A common layout:

- Top row: recent conversations table (wide)
- Middle row: feedback pie chart | relevance gauge | model usage bar
- Bottom row: response time | token usage | cost

With this dashboard, you can see at a glance how your system is
performing: are answers relevant? are users happy? how much is it
costing? which models are popular?

[<- Docker Compose](04-docker-compose.md) | [Synthetic Data Generation ->](06-synthetic-data.md)
