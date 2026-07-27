# dlt + Logfire homework

## Setup

Create a virtual environment and install dependencies:

```bash
uv init --no-readme
uv add openai minsearch requests python-dotenv pydantic-ai
```

Copy `.env.example` to `.env` and fill in your `OPENAI_API_KEY`:

```bash
cp .env.example .env
```

## Run the agent

```bash
uv run python main.py
```

## Files

- `ingest.py` — downloads the course FAQ and builds the search index
- `agent.py` — the FAQ agent built with Pydantic AI (system prompt + search tool)
- `main.py` — entry point that wires everything together
