# AI Copilot

Video: [AI Copilot](https://www.youtube.com/watch?v=OTiOdt17hZg&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

Building workflows manually can be slow. You need to know which plugin to use, look up the exact property names, remember the right syntax, and connect each task together in the correct order. For a non-trivial flow, this can take a long time before you even run it once. While Kestra's autocomplete helps, you still have to build each task one at a time.

AI Copilot changes the approach. Instead of building each step manually, you describe your inputs and your goal — and the AI Copilot generates the flow structure for you. You then tweak the last 5% to get the exact behaviour you want. The AI Copilot handles the boilerplate; you focus on the logic that's specific to your use case.

This works reliably because Kestra's AI Copilot is grounded in the current plugin documentation, valid property names, and best practices for your running version of Kestra — unlike a generic AI assistant, which guesses.

## Setup

> Note: In Kestra's Open Source edition, the AI Copilot only supports Gemini as its AI provider.

Before using AI Copilot, you need to configure Gemini API access in your Kestra instance. If you haven't done this yet, follow the [setup instructions](03-setup.md) to obtain your Gemini API key and configure it as a secret.

Access AI Copilot:

1. Open Kestra UI at http://localhost:8080
2. Create a new flow or open an existing one
3. Click the AI Copilot button (sparkle icon ✨) in the top-right corner of the Flow Editor

## Hands-On: Compare Copilot vs. Raw ChatGPT

Use the same prompt from the previous lesson, but this time with AI Copilot:

1. Click the AI Copilot button in Kestra's Flow Editor
2. Enter:
   ```
   Create a Kestra flow that loads NYC taxi data from a CSV file to BigQuery. The flow should extract data, upload to GCS, and load to BigQuery.
   ```
3. Observe the results — correct, up-to-date plugin types, valid property names, and working executable YAML.

## The 5% Rule

Copilot gets you to a working flow quickly, but it won't know everything about your environment. After generation, review the output and make the small adjustments that are specific to your setup - your environment variables, your secrets, your error handling preferences, or a task that needs a slightly different configuration than the default.

The bulk of the structure is done. You're just closing the gap between a general solution and your exact requirements.

## Iterative Refinement

AI Copilot helps with both creating new flows and refining existing ones. The conversation is cumulative — each follow-up preserves the existing flow structure and only modifies what's needed.

Example conversation:

1. "Create a flow that downloads a CSV file and loads it to BigQuery" → Copilot generates a basic flow
2. "Add a task that checks data quality in BigQuery" → Copilot adds SQL validation tasks
3. "Schedule the flow to run daily at 9 AM UTC" → Copilot adds a `Schedule` trigger
4. "Send a Slack notification if it fails" → Copilot adds a `SlackIncomingWebhook` task in an `errors` branch

Then you make the final tweaks manually - adjusting the SQL query, setting your specific Slack channel, or adding a retry count that matches your SLA. You're collaborating with AI, not starting from scratch each time.

## Example Use Cases

- Generate new flows: "Create a flow that syncs data from Postgres to GCS"
- Add tasks: "Add an If-task performing conditional branching"
- Configure triggers: "Add a webhook trigger"
- Add error handling: "Add retry logic with exponential backoff"

## Alternative: Agent Skills

If you're using an AI coding assistant (such as Claude or Cursor), Kestra's [agent-skills](https://github.com/kestra-io/agent-skills) repository gives your AI assistant the same grounding that AI Copilot has inside the UI — current plugin documentation, valid property names, and best practices. This means you can generate reliable, correct Kestra flows directly from your editor without switching to the Kestra UI.

[← Setting up Kestra](03-setup.md) | [RAG →](05-rag.md)
