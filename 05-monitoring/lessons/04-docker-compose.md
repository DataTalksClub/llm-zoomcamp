# Docker Compose

We now have three components - the Streamlit app, PostgreSQL, and
(soon) Grafana. Starting each one manually works, but Docker Compose
makes it easier to manage them together.


## Project structure

The project contains the app, database schema, and infrastructure files:

```text
code/
├── docker-compose.yaml
├── Dockerfile
├── .env
├── pyproject.toml
├── uv.lock
├── .python-version
├── app.py           # Streamlit app
├── assistant.py     # RAG pipeline + LLM
├── db.py            # Database functions
├── prep.py          # Initialize DB and load data
└── generate_data.py # Synthetic data generator
```


## Dockerfile

The Streamlit app needs its own container. We use uv inside Docker,
just like we do locally:

```dockerfile
FROM python:3.14-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app
ENV PATH="/app/.venv/bin:$PATH"

COPY pyproject.toml uv.lock .python-version ./
RUN uv sync --locked

COPY . .

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```


## Environment variables

The `.env` file stores configuration:

```text
POSTGRES_DB=course_assistant
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_HOST=postgres
OPENAI_API_KEY=your-key-here
```


## Docker Compose

The Compose file defines three services. First, PostgreSQL and the
Streamlit app:

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:16
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  streamlit:
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      - POSTGRES_HOST=postgres
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    ports:
      - "8501:8501"
    depends_on:
      - postgres
```

Grafana gets its own container with a persistent volume:

```yaml
  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    volumes:
      - grafana_data:/var/lib/grafana
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=${GRAFANA_ADMIN_PASSWORD:-admin}
    depends_on:
      - postgres

volumes:
  postgres_data:
  grafana_data:
```


## Preparation script

Before using the app, we need to initialize the database and load the
FAQ data. The `prep.py` script does this:

```python
from db import init_db
from assistant import index, documents

if __name__ == '__main__':
    print('Initializing database...')
    init_db()
    print('Database initialized.')

    print(f'Loaded {len(documents)} documents into search index.')
    print('Ready to use.')
```


## Starting everything

To launch all services:

```bash
docker compose up -d
```

Then initialize the database:

```bash
uv run python prep.py
```

Access the app at `http://localhost:8501` and Grafana at
`http://localhost:3000` (login: admin / admin).

To stop:

```bash
docker compose down
```

The data in PostgreSQL and Grafana persists across restarts thanks to
Docker volumes.

[← Storing Data in PostgreSQL](03-database.md) | [Grafana Dashboards →](05-grafana.md)
