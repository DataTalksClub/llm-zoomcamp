# Best Practices

## When to Use What

| Scenario | Use This | Why |
|----------|----------|-----|
| Creating/editing flows | AI Copilot | Fastest way to generate YAML flow code |
| Answering questions about your data | RAG | Grounds responses in real data |
| Fixed, repeatable ETL pipelines | Traditional workflows | Deterministic, predictable, compliant |
| Research and analysis tasks | AI Agents | Can adapt to findings and make decisions |
| Complex, multi-step objectives | Multi-agent systems | Specialized agents working together |

## Cost Considerations

AI features use LLM APIs, which have costs based on token usage.

Pricing per 1M tokens ([full pricing page](https://ai.google.dev/gemini-api/docs/pricing)):

| Model | Tier | Input | Output |
|-------|------|-------|--------|
| Gemini 2.5 Flash | Free | $0.00 | $0.00 |
| Gemini 2.5 Flash | Batch / Flex | $0.15 | $1.25 |
| Gemini 3.5 Flash | Free | $0.00 | $0.00 |
| Gemini 3.5 Flash | Standard | $1.50 | $9.00 |
| Gemini 3.5 Flash | Batch / Flex | $0.75 | $4.50 |
| Gemini 3.5 Flash | Priority | $2.70 | $16.20 |

Use Gemini 2.5 Flash for most workflows — it's cheaper and free for standard inference. Step up to Gemini 3.5 Flash when you need stronger reasoning for complex agent tasks.

Cost-saving tips:

1. Start with the free tier for learning and development
2. Use smaller/cheaper models for simple tasks — check the [pricing page](https://ai.google.dev/gemini-api/docs/pricing)
3. Set `maxOutputTokens` to limit response size
4. Monitor token usage in execution outputs
5. Use traditional workflows when determinism is needed

## Security

Never commit API keys to Git. Always use secrets:

```yaml
# ❌ Wrong
apiKey: "sk-abc123def456"

# ✅ Correct
apiKey: "{{ secret('GEMINI_API_KEY') }}"
```

Export base64-encoded keys as `SECRET_`-prefixed environment variables before starting Kestra. Rotate keys regularly (e.g., every 90 days) and monitor usage. Read more about secrets in the [Kestra documentation](https://kestra.io/docs/concepts/secret).

## Observability and Debugging

Enable detailed logging when troubleshooting:

```yaml
- id: my_agent_task
  type: io.kestra.plugin.ai.agent.AIAgent
  provider:
    # ...
    # provider settings
    # ...
  configuration:
    logRequests: true
    logResponses: true
```

Monitor token usage per execution, agent tool calls and decisions, execution time and costs, and output quality.

Debugging tips:

1. Start with simple prompts and iterate
2. Check logs for LLM reasoning
3. Verify tool execution outputs

## Production Readiness

Before deploying AI workflows to production:

1. Test thoroughly — run multiple times with different inputs, verify outputs are consistent and accurate
2. Add fallbacks — handle API failures with retries and configure alerts on failure
3. Set limits — cap `maxOutputTokens` to control costs
4. Document behavior — explain what the agent does in your flow and task descriptions

[← Multi-Agent Systems](07-multi-agent.md) | [Next Steps →](09-next-steps.md)
