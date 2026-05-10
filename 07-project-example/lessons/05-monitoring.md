# Monitoring and Containerization

<a href="https://www.youtube.com/watch?v=nQda9etJWW8&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/nQda9etJWW8">
</a>

We take the same monitoring approach from module 05 and apply it
to our fitness assistant. Then we containerize everything with
Docker Compose.


## Docker Compose setup

We need three services: PostgreSQL for logging, the Flask app, and
Grafana for dashboards:

```yaml
services:
  postgres:
    image: postgres:16
    environment:
      POSTGRES_DB: fitness_assistant
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  app:
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      - POSTGRES_HOST=postgres
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    ports:
      - "5000:5000"
    depends_on:
      - postgres

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    depends_on:
      - postgres

volumes:
  postgres_data:
```

The Dockerfile uses uv:

```dockerfile
FROM python:3.14-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
ENV PATH="/app/.venv/bin:$PATH"

COPY pyproject.toml uv.lock .python-version ./
RUN uv sync --locked

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
```


## Database schema

Store conversations and feedback in PostgreSQL:

```python
import psycopg

def init_db():
    conn = psycopg.connect("postgresql://user:password@postgres/fitness_assistant")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id TEXT PRIMARY KEY,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            model_used TEXT,
            response_time FLOAT,
            relevance TEXT,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id SERIAL PRIMARY KEY,
            conversation_id TEXT REFERENCES conversations(id),
            feedback INTEGER NOT NULL,
            created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
        )
    """)

    conn.commit()
    cur.close()
    conn.close()
```


## Logging from the app

Add logging to the Flask endpoint:

```python
@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')

    start_time = time.time()
    answer = rag(question)
    response_time = time.time() - start_time

    save_conversation(conversation_id, question, answer, response_time)

    return jsonify({'answer': answer, 'id': conversation_id})
```


## Grafana dashboards

Create dashboards with the same SQL queries from module 05 to
monitor response time, relevance, feedback, and token usage.

Automate dashboard provisioning with an init script that creates
the PostgreSQL data source and loads the dashboard JSON through
the Grafana API.


[<< Previous: Interface and Ingestion](04-interface)
|
[Next: Summary >>](06-summary)
