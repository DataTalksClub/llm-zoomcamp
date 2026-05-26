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

**Gemini 2.5 Flash Pricing (as of late 2025):**
- **Free Tier**: Free for both input and output (with rate limits)
- **Paid Tier** (per 1M tokens): $0.30 input / $2.50 output

**Cost-saving tips:**

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

Export base64-encoded keys as `SECRET_`-prefixed environment variables before starting Kestra. Rotate keys regularly (e.g., every 90 days) and monitor usage.

## Observability and Debugging

Enable detailed logging when troubleshooting:

```yaml
provider:
  configuration:
    logRequests: true
    logResponses: true
```

Monitor token usage per execution, agent tool calls and decisions, execution time and costs, and output quality.

**Debugging tips:**

1. Start with simple prompts and iterate
2. Check logs for LLM reasoning
3. Verify tool execution outputs

## Production Readiness

Before deploying AI workflows to production:

1. **Test thoroughly** — run multiple times with different inputs, verify outputs are consistent and accurate
2. **Add fallbacks** — handle API failures with retries and configure alerts on failure
3. **Set limits** — cap `maxOutputTokens` to control costs
4. **Document behavior** — explain what the agent does in your flow and task descriptions

[← Getting Started](07-setup.md) | [Back to module →](../)
