# Setting up Kestra

Video: [Setting up Kestra](https://www.youtube.com/watch?v=ghkf93rfb2w&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

Here's how to set up everything you need to run the example flows in this module.

## Prerequisites

This module requires [Docker](https://docs.docker.com/get-started/get-docker/) with Docker Compose to run Kestra locally. [Docker Desktop](https://www.docker.com/products/docker-desktop/) is the easiest way to get both on Mac and Windows. If you don't have Docker installed, set that up before proceeding.

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

The free tier is sufficient for light use, but rate limits are relatively low — you may hit quota quickly if you run the agent and multi-agent flows repeatedly. If you run into `429 Resource Exhausted` errors, wait a minute before retrying, or consider upgrading to a paid tier.

**OpenAI API Key (Required for flow 3)**

1. Visit [platform.openai.com](https://platform.openai.com/home) and sign in or create an account
2. Go to **API keys** and create a new key

**Tavily API Key (Required for web search: flows 3, 5, and 6)**

1. Visit [Tavily](https://tavily.com/)
2. Sign up for the free tier
3. Get your API key from the dashboard

The free tier includes 1,000 searches/month.

## Step 3: Configure API Keys in Kestra

Kestra reads secrets from environment variables prefixed with `SECRET_` where the value is base64-encoded. Export your keys before starting Kestra:

```bash
export GEMINI_API_KEY="your-gemini-api-key-here" # required
export SECRET_GEMINI_API_KEY=$(echo -n $GEMINI_API_KEY | base64) # required
export SECRET_OPENAI_API_KEY=$(echo -n "your-openai-api-key-here" | base64)   # required for flow 3
export SECRET_TAVILY_API_KEY=$(echo -n "your-tavily-api-key-here" | base64)   # optional
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
curl -X POST -u 'admin@kestra.io:Admin1234!' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/3_rag_with_websearch.yaml
curl -X POST -u 'admin@kestra.io:Admin1234!' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/4_simple_agent.yaml
curl -X POST -u 'admin@kestra.io:Admin1234!' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/5_web_research_agent.yaml
curl -X POST -u 'admin@kestra.io:Admin1234!' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/6_multi_agent_research.yaml
```

Alternatively, copy-paste the flow YAML directly into Kestra's UI.

## Step 5: Run Your First Agent

1. Open Kestra UI at http://localhost:8080
2. Navigate to the `zoomcamp` namespace
3. Find the `4_simple_agent` flow and click "Execute"
4. Leave default inputs or customize them
5. Watch the execution and review the outputs
6. Then run `5_web_research_agent` and `6_multi_agent_research` and analyze the logs and outputs

[← Context Engineering](02-context-engineering.md) | [AI Copilot →](04-ai-copilot.md)
