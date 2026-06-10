## Homework: AI Orchestration with Kestra

ATTENTION: At the end of the submission form, you will be required to include a link to your GitHub repository or other public code-hosting site. This repository should contain your code for solving the homework. If your solution includes code that is not in file format, please include these directly in the README file of your repository.

> In case you don't get one option exactly, select the closest one

## Prerequisites

Before starting this homework, ensure you have:

1. Kestra running locally (see the [Getting Started](../../../03-orchestration/lessons/02-setup.md) lesson)
2. Google Gemini API key (get it from https://aistudio.google.com/app/apikey)
3. (Optional) Tavily API key for web search examples (get it from https://tavily.com/)
4. Imported all flows from the `03-orchestration/flows/` directory

## Assignment Overview

This homework explores AI workflows and agents in Kestra. You'll experiment with:
- Context engineering and why it matters
- RAG (Retrieval Augmented Generation) for grounded AI responses
- AI Agents for autonomous task execution
- Multi-agent systems for complex AI workflows

## Setup Instructions

Configure your API keys as Kestra secrets:

⚠️ Important: Never commit API keys to Git! Always use environment variables.

Kestra reads secrets from environment variables prefixed with `SECRET_` where the value is base64-encoded. Export your keys before starting Kestra:

```bash
export SECRET_GEMINI_API_KEY=$(echo -n "your-gemini-api-key-here" | base64)
export SECRET_TAVILY_API_KEY=$(echo -n "your-tavily-api-key-here" | base64)  # optional
```

Then start (or restart) Kestra:

```bash
cd 03-orchestration
docker compose up -d
```

In flows, secrets are referenced with `{{ secret('GEMINI_API_KEY') }}` — omit the `SECRET_` prefix when calling `secret()`.

Import the homework flows:

```bash
cd 03-orchestration

# Adjust username and password to match your Kestra setup
curl -X POST -u 'admin@kestra.io:Admin1234!' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/1_chat_without_rag.yaml
curl -X POST -u 'admin@kestra.io:Admin1234!' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/2_chat_with_rag.yaml
curl -X POST -u 'admin@kestra.io:Admin1234!' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/3_simple_agent.yaml
curl -X POST -u 'admin@kestra.io:Admin1234!' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/4_web_research_agent.yaml
curl -X POST -u 'admin@kestra.io:Admin1234!' http://localhost:8080/api/v1/flows/import -F fileUpload=@flows/5_multi_agent_research.yaml
```

## Question 1: Context Engineering

Try the following experiment:

1. Open ChatGPT in a private browser window: https://chatgpt.com
2. Enter this prompt: "Create a Kestra flow that loads NYC taxi data from CSV to BigQuery"
3. Then, use Kestra's AI Copilot with the same prompt

After trying the same prompt in ChatGPT vs Kestra's AI Copilot, what is the primary reason Copilot generates better Kestra flows?

- Copilot uses a more powerful model
- Copilot has access to current Kestra plugin documentation
- Copilot uses more tokens
- Copilot has internet access

## Question 2: RAG Comparison

Run both `1_chat_without_rag.yaml` and `2_chat_with_rag.yaml` and compare their outputs. Both ask: "Which features were released in Kestra 1.1?"

What difference do you observe?

- RAG version provides specific, accurate feature details grounded in the documentation
- Both produce identical results
- Non-RAG version is more detailed and accurate
- RAG version hallucinates more features than the non-RAG version

## Question 3: Token Usage

Run `3_simple_agent.yaml` twice:

1. First with `summary_length` = `short`
2. Second with `summary_length` = `long`

Check the token usage logged at the end of each execution. How does token usage differ between short and long summaries for the `multilingual_agent` task?

- No significant difference (within 10% variance)
- Long summary uses 2-4x more output tokens than short summary
- Short summary uses more tokens due to compression complexity
- Token usage is identical regardless of length

## Question 4: Agent Autonomy

Run `4_web_research_agent.yaml` with the default research topic about data orchestration trends.

In this flow, who decides when to use the web search tool?

- The workflow designer specifies exact tool usage order in YAML
- The agent autonomously decides based on the prompt and system message
- Tools are called randomly by the LLM
- Web search runs on every agent execution automatically

## Question 5: Multi-Agent Collaboration

Examine `5_multi_agent_research.yaml` and run it with the default company (kestra.io).

What is the role of the research agent in this multi-agent system?

- It makes final decisions about company analysis and structures the output
- It serves as a tool for the main agent to gather web data
- It summarizes the main agent's findings into a report
- It validates the main agent's output for accuracy

## Question 6: Best Practices

Based on what you learned in this module, for production workflows requiring deterministic, repeatable results with strict compliance requirements (e.g., financial reporting, workflows in highly regulated industries), which approach is most appropriate?

- Always use AI agents for maximum flexibility and adaptation
- Use traditional task-based workflows for predictability and auditability
- Use only RAG without agents for better performance
- Use web search tools exclusively to ensure current data

## Learning in Public

We encourage everyone to share what they learned. This is called "learning in public".

Read more about the benefits [here](https://alexeyondata.substack.com/p/benefits-of-learning-in-public-and) and in the [course's learning in public guide](https://datatalks.club/docs/courses/zoomcamp-logistics/learning-in-public/).

### Example post for LinkedIn

Tag [@Alexey Grigorev](https://www.linkedin.com/in/agrigorev/) and [@DataTalksClub](https://www.linkedin.com/company/datatalks-club/) in your post - we'll like and comment to give your post more reach.

```
🚀 Module 3 of LLM Zoomcamp by @DataTalksClub complete!

Just finished Module 3 - AI Orchestration with @Kestra. Learned how to:

✅ Engineer context so the LLM gets the right information
✅ Ground answers in real data with RAG
✅ Build AI agents that decide which tools to call
✅ Orchestrate multi-agent systems

Here's my homework solution: <LINK>

Following along with this amazing free course by @Alexey Grigorev - who else is learning to build with LLMs?

You can sign up here: https://github.com/DataTalksClub/llm-zoomcamp/
```

### Example post for X

```
🤖 Module 3 of LLM Zoomcamp done!

- AI orchestration with @kestra_io
- Context engineering
- RAG-grounded answers
- AI agents & multi-agent systems

My solution: <LINK>

Free course by @Al_Grigor & @DataTalksClub: https://github.com/DataTalksClub/llm-zoomcamp/
```

## Submitting the Solutions

* Form for submitting: https://courses.datatalks.club/llm-zoomcamp-2026/homework/hw3
* Check the link above to see the due date

## Tips for Success

1. API Keys: Make sure your Gemini API key is correctly stored in the KV Store
2. Free Tier Limits: If you hit rate limits, wait a few minutes and try again
3. Debugging: Enable `logRequests` and `logResponses` in your provider configuration to see what's being sent to the LLM
4. Cost Monitoring: Check token usage in execution logs to understand costs
5. Community: Ask questions in the course Slack if you get stuck

## Additional Resources

- [Kestra AI Documentation](https://kestra.io/docs/ai-tools)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [Kestra Slack Community](https://kestra.io/slack)
