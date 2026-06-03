# Feedback Dashboard

Now that we have both user feedback and judge evaluations, let's add
them to the Streamlit dashboard.

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


[← Built-in Judge](09-built-in-judge.md) | [Synthetic Data →](11-synthetic-data.md)
