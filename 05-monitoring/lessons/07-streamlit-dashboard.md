# Streamlit Dashboard

Before setting up Grafana, let's build a quick dashboard in Streamlit
to visualize the data we're collecting. This is simpler and good enough
for many use cases.

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

Show summary metrics at the top:

```python
st.title("Course Assistant Dashboard")

stats = get_stats()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total conversations", stats.total)
col2.metric("Avg response time", f"{stats.avg_response_time:.2f}s")
col3.metric("Total cost", f"${stats.total_cost:.4f}")
col4.metric("Avg tokens", f"{stats.avg_tokens:.0f}")
```

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

Later we'll set up Grafana for a more production-ready dashboard.

[← Querying Data](06-querying.md) | [User Feedback →](08-user-feedback.md)
