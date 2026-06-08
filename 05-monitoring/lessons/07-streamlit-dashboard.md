# Streamlit Dashboard

Video: [Watch this lesson](https://www.youtube.com/watch?v=OrWlgDKZclI&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

Before we reach for Grafana, let's build a quick dashboard right in
Streamlit. For a lot of projects this is all you need. When you're
getting started, seeing latency, cost, and recent conversations in one
place is already enough. You often don't need Grafana at all.

If you stop here, you don't even need Postgres. You could swap it for
SQLite and skip Docker entirely. We're on Postgres only because Grafana
connects to it more easily than to SQLite, which matters later. For a
lightweight project, SQLite plus a Streamlit dashboard is a perfectly
good place to stop.

I'm not a Streamlit expert. When I build these pages, I describe what I
want to ChatGPT or a coding assistant. Then I let it write the layout. I
kept this one simple on purpose, so you can read it top to bottom and
follow what's happening.

First, add aggregate queries to `db_query.py`.

Add a `Stats` dataclass to `db_query.py`:

```python
@dataclass
class Stats:
    total: int
    avg_response_time: float
    total_cost: float
    avg_tokens: float
```

A function to compute aggregate stats:

```python
def get_stats():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT
                    COUNT(*),
                    AVG(response_time),
                    SUM(cost),
                    AVG(total_tokens)
                FROM conversations
            """)
            row = cur.fetchone()
    finally:
        conn.close()

    return Stats(
        total=row[0],
        avg_response_time=row[1],
        total_cost=row[2],
        avg_tokens=row[3],
    )
```

Create `dashboard.py`:

```python
import streamlit as st
from dataclasses import asdict
import pandas as pd
from db_query import get_conversations, get_stats
```

At the top we show four summary numbers, the ones most worth watching
when you're getting started. You can show far more, but these are a good
starting point.

Show the summary metrics:

```python
st.title("Course Assistant Dashboard")

stats = get_stats()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total conversations", stats.total)
col2.metric("Avg response time", f"{stats.avg_response_time:.2f}s")
col3.metric("Total cost", f"${stats.total_cost:.4f}")
col4.metric("Avg tokens", f"{stats.avg_tokens:.0f}")
```

For the time charts we pull the last 100 conversations and let Streamlit
plot them. This isn't the most efficient way to do it. We fetch whole
records just to chart two columns. A leaner version would query only the
timestamp and the value we want. With our volume it's fine, so we keep it
short.

Charts for cost and response time over time:

```python
records = get_conversations(limit=100)
df = pd.DataFrame([asdict(r) for r in records])

st.subheader("Cost over time")
st.line_chart(df, x="timestamp", y="cost")

st.subheader("Response time over time")
st.line_chart(df, x="timestamp", y="response_time")
```

Recent conversations:

```python
st.subheader("Recent conversations")
records = get_conversations(limit=20)

for record in records:
    st.write(f"**{record.prompt[:80]}...**")
    st.write(f"{record.answer[:200]}...")
    st.write(f"Time: {record.response_time:.2f}s | Cost: ${record.cost:.4f}")
    st.divider()
```

Run it.

The port 8501 is already in use (by the chat app), so we will use a
different port:

```bash
uv run streamlit run dashboard.py --server.port 8502
```

We didn't even use a table for the conversations - plain text is enough
to make the point. This simple dashboard already gives us real
visibility into the system. Later we set up Grafana for a more powerful
view, with alerting and richer panels.

[← Querying Data](06-querying.md) | [User Feedback →](08-user-feedback.md)
