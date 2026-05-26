# AI Copilot

Kestra's AI Copilot is specifically designed to generate and modify Kestra flows with full context about the latest plugins, syntax, and best practices.

## Setup

Before using AI Copilot, you need to configure Gemini API access in your Kestra instance.

**Get your Gemini API key:**

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key" and copy the generated key

> [!WARNING]
> Never commit API keys to Git. Always use environment variables.

**Configure Kestra:**

The `docker-compose.yml` in this module already includes the AI configuration. Set your API key and restart Kestra:

```bash
cd 03-orchestration
export GEMINI_API_KEY="your-api-key-here"
docker compose up -d
```

**Access AI Copilot:**

1. Open Kestra UI at http://localhost:8080
2. Create a new flow or open an existing one
3. Click the **AI Copilot** button (sparkle icon ✨) in the top-right corner of the Flow Editor

## Hands-On: Compare Copilot vs. Raw ChatGPT

Use the same prompt from the previous lesson, but this time with AI Copilot:

1. **Click the AI Copilot button** in Kestra's Flow Editor
2. **Enter:**
   ```
   Create a Kestra flow that loads NYC taxi data from a CSV file to BigQuery. The flow should extract data, upload to GCS, and load to BigQuery.
   ```
3. **Observe the results** — correct, up-to-date plugin types, valid property names, and working executable YAML.

## Why Does Copilot Work Better?

Kestra's AI Copilot has access to current plugin documentation (all available plugins and their exact syntax), the flow context of whatever you're already editing, best practices recommended by Kestra, and version-specific details for your running instance.

This is **context engineering** in action: by giving the AI the right context, we get reliable, production-ready results.

## Iterative Refinement

AI Copilot helps with both creating new flows and refining existing ones. The conversation is cumulative — each follow-up preserves the existing flow structure and only modifies what's needed.

**Example conversation:**

1. "Create a flow that downloads a CSV file and loads it to BigQuery" → Copilot generates a basic flow
2. "Add a task that checks data quality in BigQuery" → Copilot adds SQL validation tasks
3. "Schedule the flow to run daily at 9 AM UTC" → Copilot adds a `Schedule` trigger
4. "Send a Slack notification if it fails" → Copilot adds a `SlackIncomingWebhook` task in an `errors` branch

You're collaborating with AI, not starting from scratch each time.

## Example Use Cases

- **Generate new flows**: "Create a flow that syncs data from Postgres to GCS"
- **Add tasks**: "Add an If-task performing conditional branching"
- **Configure triggers**: "Add a webhook trigger"
- **Add error handling**: "Add retry logic with exponential backoff"

[← Context Engineering](02-context-engineering.md) | [RAG →](04-rag.md)
