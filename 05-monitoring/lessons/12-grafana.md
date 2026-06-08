# Grafana Dashboards

Video: [Watch this lesson](https://www.youtube.com/watch?v=Pmh2jT8tEiw&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

Our Streamlit dashboard already works. We bring in Grafana because it
does more. It's a dedicated dashboarding tool: it connects to many data
sources and offers more panel types. It can also raise alerts when a
metric crosses a line.

The tradeoff is that it's a separate, heavier application to run. That's
exactly why, if your needs are simple, the Streamlit dashboard is enough.
When you want more, Grafana reads straight from the Postgres we already
have and shows what's happening in real time.

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
database lesson. We run Grafana detached with `-d`. If you'd rather watch
its logs while you set things up, drop the `-d` and run it attached. The
volume means everything you build in Grafana survives a restart, both
data sources and dashboards.

Access Grafana at `http://localhost:3000`. The first login is admin /
admin, and it asks you to set a new password. For local work, admin /
admin again is fine.

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

Create a new dashboard. We add panels one at a time, and each panel is a
SQL query that Grafana runs against PostgreSQL.

Two habits make these queries behave. First, alias your time column as
`time`. Grafana reads that column to place points on the x-axis, so a
time chart needs it. Second, filter on the selected time range. The panel
then follows whatever you pick at the top instead of the whole table.

Grafana gives us special SQL variables for exactly that filtering:

- `$__timeFrom()`: start of the selected time range
- `$__timeTo()`: end of the selected time range
- `$__timeGroup(column, interval)`: groups results by time intervals

Including `$__timeFrom()` and `$__timeTo()` in the `WHERE` clause isn't
strictly required, but it's better to be explicit. The panel then tracks
whatever range you select at the top.

## Response Time Panel

Shows how long the LLM takes to respond over time.

Each row in the conversations table is already one LLM call, so we
just plot the raw values:

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

Shows token consumption over time.

Over a long time range there would be too many points to plot
individually.

We group by time intervals (e.g. every 5 minutes) and take the average
within each bucket:

```sql
SELECT
  $__timeGroup(timestamp, $__interval) AS time,
  AVG(total_tokens) AS avg_tokens
FROM conversations
WHERE timestamp BETWEEN $__timeFrom() AND $__timeTo()
GROUP BY 1
ORDER BY 1
```

- `$__timeGroup` rounds timestamps into buckets.
- `GROUP BY 1` groups by the first column (the bucket). 
- `AVG` gives the average tokens per bucket.

Use the Time series visualization for this panel.

## Cost Panel

Shows cumulative cost over time.

Same idea, but instead of averaging we `SUM` the costs within each
time bucket:

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

## Relevance Distribution Panel

Shows how many answers are RELEVANT, PARTLY_RELEVANT, or
NON_RELEVANT according to the judge:

```sql
SELECT
  relevance,
  COUNT(*) as count
FROM feedback
WHERE source = 'judge'
  AND timestamp BETWEEN $__timeFrom() AND $__timeTo()
GROUP BY relevance
```

Use a Pie chart for this panel.

## User Feedback Panel

Shows thumbs up vs thumbs down:

```sql
SELECT
  SUM(CASE WHEN score > 0 THEN 1 ELSE 0 END) as thumbs_up,
  SUM(CASE WHEN score < 0 THEN 1 ELSE 0 END) as thumbs_down
FROM feedback
WHERE source = 'user'
  AND timestamp BETWEEN $__timeFrom() AND $__timeTo()
```

Use a Gauge or Pie chart for this panel.

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
- Middle row: model usage bar chart | relevance pie chart
- Bottom row: response time | token usage | cost

Don't treat these panel types as fixed. On the same query you can try a
bar chart, a pie, or a time series. Experiment and keep whatever reads
best. With the synthetic data still streaming in, you'll see the charts
move as you go.

This dashboard gives you a clear view of how the system is doing. Response
speed, cost, relevance, and user ratings are all in one place.

[← Synthetic Data](11-synthetic-data.md) | [Docker Compose →](13-docker-compose.md)
