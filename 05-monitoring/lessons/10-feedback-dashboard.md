# Feedback Dashboard

_This lesson has no video._

We collect two kinds of feedback now. People give thumbs up and down, and
the judge gives relevance labels. But we can't see either one yet. So we
add them to the Streamlit dashboard from lesson 07, beside the cost and
latency panels.

First, add feedback queries to `db_query.py`.

Get judge relevance distribution:

```python
def get_relevance_stats():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT relevance, COUNT(*)
                FROM feedback
                WHERE source = 'judge'
                GROUP BY relevance
            """)
            rows = cur.fetchall()
    finally:
        conn.close()
    return dict(rows)
```

Get user feedback stats:

```python
def get_user_feedback_stats():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT
                    SUM(CASE WHEN score > 0 THEN 1 ELSE 0 END),
                    SUM(CASE WHEN score < 0 THEN 1 ELSE 0 END)
                FROM feedback
                WHERE source = 'user'
            """)
            row = cur.fetchone()
    finally:
        conn.close()
    return row
```

Update `dashboard.py` to show the feedback panels.

Import the new functions:

```python
from db_query import get_conversations, get_stats, get_relevance_stats, get_user_feedback_stats
```

Judge relevance distribution:

```python
st.subheader("Judge relevance")
relevance = get_relevance_stats()
st.bar_chart(relevance)
```

User feedback:

```python
st.subheader("User feedback")
thumbs_up, thumbs_down = get_user_feedback_stats()
col1, col2 = st.columns(2)
col1.metric("Thumbs up", int(thumbs_up or 0))
col2.metric("Thumbs down", int(thumbs_down or 0))
```

The dashboard now shows quality alongside cost and speed. The catch is
that with only a few real conversations, the charts look empty. Before
we move to Grafana, let's fill the database with some data so there's
actually something to look at.

[← Built-in Judge](09-built-in-judge.md) | [Synthetic Data →](11-synthetic-data.md)
