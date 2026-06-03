# Docker Compose

We now have three components running - PostgreSQL, Grafana, and the
Streamlit app. Starting each one manually and connecting them with
networks works, but Docker Compose makes it easier to manage them
together.

## Project structure

The project layout:

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
├── db_init.py       # Database init
├── db_save.py       # Save conversations
└── dashboard.py     # Streamlit dashboard
```

## Dockerfile

The Streamlit app needs its own container:

```dockerfile
FROM python:3.12-slim

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

The Compose file defines all three services on the same network:

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:17
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
    volumes:
      - grafana_data:/var/lib/grafana
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    depends_on:
      - postgres
```

The Streamlit service is built from the Dockerfile:

```yaml
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

volumes:
  postgres_data:
  grafana_data:
```

## Starting everything

Start all services:

```bash
docker-compose up
```

Initialize the database:

```bash
uv run python db_init.py
```

Access the app at `http://localhost:8501` and Grafana at
`http://localhost:3000` (login: admin / admin).

To stop:

```bash
docker-compose down
```

The data in PostgreSQL and Grafana persists across restarts thanks to
Docker volumes.

[← Grafana](12-grafana.md) | [Next Steps →](14-next-steps.md)
