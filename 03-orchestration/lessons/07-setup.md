# Getting Started

Here's how to set up everything you need to run the example flows in this module.

## Step 1: Start Kestra

This module includes a `docker-compose.yml` with Kestra pre-configured:

```bash
cd 03-orchestration
docker compose up -d
```

Once the container starts, access the Kestra UI at http://localhost:8080.

To shut down Kestra:

```bash
docker compose down
```

## Step 2: Obtain API Keys

**Gemini API Key (Required)**

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key" and copy your key

The free tier has a generous quota suitable for learning (rate limits apply).

**Tavily API Key (Optional, for web search examples)**

1. Visit [Tavily](https://tavily.com/)
2. Sign up for the free tier
3. Get your API key from the dashboard

The free tier includes 1,000 searches/month.

## Step 3: Configure API Keys in Kestra

Kestra reads secrets from environment variables prefixed with `SECRET_` where the value is base64-encoded. Export your keys before starting Kestra:

```bash
export SECRET_GEMINI_API_KEY=$(echo -n "your-gemini-api-key-here" | base64)
export SECRET_TAVILY_API_KEY=$(echo -n "your-tavily-api-key-here" | base64)  # optional
```

Then start (or restart) Kestra:

```bash
docker compose up -d
```

In flows, reference secrets with `{{ secret('GEMINI_API_KEY') }}` — omit the `SECRET_` prefix when calling `secret()`.

> [!WARNING]
> Never commit API keys to Git!

## Step 4: Import Example Flows

```bash
cd 03-orchestration

# Adjust username and password to match your Kestra setup
curl -X POST -u 'admin@kestra.io:Admin1234!' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/1_chat_without_rag.yaml
curl -X POST -u 'admin@kestra.io:Admin1234!' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/2_chat_with_rag.yaml
curl -X POST -u 'admin@kestra.io:Admin1234!' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/3_simple_agent.yaml
curl -X POST -u 'admin@kestra.io:Admin1234!' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/4_web_research_agent.yaml
curl -X POST -u 'admin@kestra.io:Admin1234!' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/5_multi_agent_research.yaml
```

Alternatively, copy-paste the flow YAML directly into Kestra's UI.

## Step 5: Configure AI Copilot (Optional)

The `docker-compose.yml` in this module already includes the AI Copilot configuration. To enable it, set your Gemini API key and restart Kestra:

```bash
export GEMINI_API_KEY="your-api-key-here"
docker compose up -d
```

## Step 6: Run Your First Agent

1. Open Kestra UI at http://localhost:8080
2. Navigate to the `zoomcamp` namespace
3. Find the `3_simple_agent` flow and click "Execute"
4. Leave default inputs or customize them
5. Watch the execution and review the outputs
6. Then run `4_web_research_agent` and `5_multi_agent_research` and analyze the logs and outputs

[← Multi-Agent Systems](06-multi-agent.md) | [Best Practices →](08-best-practices.md)
