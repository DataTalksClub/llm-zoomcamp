# Storing Data in PostgreSQL

To monitor our system, we need to store every conversation and every
piece of feedback. PostgreSQL is a good choice: it handles structured
data well and integrates with Grafana for dashboards.

We need two tables:

- `conversations`: stores questions, answers, metrics
- `feedback`: stores thumbs up / thumbs down


## Database schema

The conversations table stores everything about each interaction.
First, the connection helper and timezone:

```python
import os
import psycopg2
from psycopg2.extras import DictCursor
from datetime import datetime
from zoneinfo import ZoneInfo

tz = ZoneInfo('Europe/Berlin')

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv('POSTGRES_HOST', 'localhost'),
        database=os.getenv('POSTGRES_DB', 'course_assistant'),
        user=os.getenv('POSTGRES_USER', 'user'),
        password=os.getenv('POSTGRES_PASSWORD', 'password'),
    )
```

The `init_db` function creates both tables:

```python
def init_db():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS feedback")
            cur.execute("DROP TABLE IF EXISTS conversations")

            cur.execute("""
                CREATE TABLE conversations (
                    id TEXT PRIMARY KEY,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL,
                    course TEXT NOT NULL,
                    model_used TEXT NOT NULL,
                    response_time FLOAT NOT NULL,
                    relevance TEXT NOT NULL,
                    relevance_explanation TEXT NOT NULL,
                    prompt_tokens INTEGER NOT NULL,
                    completion_tokens INTEGER NOT NULL,
                    total_tokens INTEGER NOT NULL,
                    openai_cost FLOAT NOT NULL,
                    timestamp TIMESTAMP WITH TIME ZONE NOT NULL
                )
            """)

            cur.execute("""
                CREATE TABLE feedback (
                    id SERIAL PRIMARY KEY,
                    conversation_id TEXT REFERENCES conversations(id),
                    feedback INTEGER NOT NULL,
                    timestamp TIMESTAMP WITH TIME ZONE NOT NULL
                )
            """)
        conn.commit()
    finally:
        conn.close()
```

The `conversations` table has columns for:

- `id`: unique conversation identifier (UUID)
- `question` and `answer`: the text
- `course`: which course was selected
- `model_used`: which LLM model
- `response_time`: how long the LLM took (seconds)
- `relevance`: RELEVANT, PARTLY_RELEVANT, or NON_RELEVANT
- `relevance_explanation`: why the judge gave this rating
- `prompt_tokens`, `completion_tokens`, `total_tokens`: token usage
- `openai_cost`: estimated cost
- `timestamp`: when the conversation happened

The `feedback` table is simpler: it links a conversation to a +1 or -1.


## Saving data

Use these functions to save conversations and feedback to the database:

```python
def save_conversation(conversation_id, question, answer_data, course, timestamp=None):
    if timestamp is None:
        timestamp = datetime.now(tz)

    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO conversations
                (id, question, answer, course, model_used, response_time,
                 relevance, relevance_explanation, prompt_tokens,
                 completion_tokens, total_tokens, openai_cost, timestamp)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    conversation_id,
                    question,
                    answer_data['answer'],
                    course,
                    answer_data['model_used'],
                    answer_data['response_time'],
                    answer_data['relevance'],
                    answer_data['relevance_explanation'],
                    answer_data['prompt_tokens'],
                    answer_data['completion_tokens'],
                    answer_data['total_tokens'],
                    answer_data['openai_cost'],
                    timestamp,
                ),
            )
        conn.commit()
    finally:
        conn.close()
```

Feedback is simpler, just a conversation ID and a score:

```python
def save_feedback(conversation_id, feedback, timestamp=None):
    if timestamp is None:
        timestamp = datetime.now(tz)

    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO feedback (conversation_id, feedback, timestamp) VALUES (%s, %s, %s)",
                (conversation_id, feedback, timestamp),
            )
        conn.commit()
    finally:
        conn.close()
```

We use timezone-aware timestamps (`TIMESTAMP WITH TIME ZONE`). This
matters for Grafana, we want the dashboard to show times in the
user's timezone, and Grafana handles this conversion when we use proper
time zones.


## Querying data

For the Streamlit app, we also need functions to retrieve data:

```python
def get_recent_conversations(limit=5, relevance=None):
    conn = get_db_connection()
    try:
        with conn.cursor(cursor_factory=DictCursor) as cur:
            query = """
                SELECT c.*, f.feedback
                FROM conversations c
                LEFT JOIN feedback f ON c.id = f.conversation_id
            """
            if relevance:
                query += f" WHERE c.relevance = '{relevance}'"
            query += ' ORDER BY c.timestamp DESC LIMIT %s'

            cur.execute(query, (limit,))
            return cur.fetchall()
    finally:
        conn.close()

def get_feedback_stats():
    conn = get_db_connection()
    try:
        with conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute("""
                SELECT
                    SUM(CASE WHEN feedback > 0 THEN 1 ELSE 0 END) as thumbs_up,
                    SUM(CASE WHEN feedback < 0 THEN 1 ELSE 0 END) as thumbs_down
                FROM feedback
            """)
            return cur.fetchone()
    finally:
        conn.close()
```

Grafana queries the database directly, so we don't need Python
functions for the dashboard. But for the Streamlit app, these are
useful to show recent conversations and feedback stats.

[← Chat App with Feedback](02-chat-app.md) | [Docker Compose →](04-docker-compose.md)
