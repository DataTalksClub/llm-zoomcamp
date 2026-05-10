# Next Steps

In this module, we covered evaluation at three levels:

1. Search evaluation: Hit Rate and MRR to measure retrieval quality
2. RAG evaluation: cosine similarity and LLM-as-a-judge for answer quality
3. Agent evaluation: trajectory and instruction following for tool-using agents

Evaluation is not a one-time activity. As you change your system --
tune search parameters, switch models, modify prompts -- you re-run
evaluation to make sure things are getting better, not worse.


## Evaluation frameworks

For production systems, consider using evaluation frameworks that make
it easier to manage test datasets, run evaluations, and track results:

- Ragas: a framework for evaluating RAG systems with metrics like
  faithfulness, answer relevance, and context precision
- DeepEval: provides built-in metrics for RAG evaluation including
  hallucination detection and answer relevance
- TruLens: instruments your LLM app and tracks quality metrics

These frameworks implement many of the concepts we covered here and
add visualizations and experiment tracking.


## Monitoring

Online evaluation (monitoring) is what you do after deploying your
system. Key approaches:

- User feedback: thumbs up/down buttons to collect signal
- Logging: record queries, retrieved documents, and answers
- Dashboards: track metrics over time to spot degradation
- Alerts: get notified when metrics drop below a threshold

Monitoring is covered in more detail in module 05.


## Further reading

- Cohorts and materials:
  - 2024 cohort evaluation module (uses Elasticsearch):
    [2024/04-monitoring](../cohorts/2024/04-monitoring/)
  - 2025 cohort evaluation module:
    [2025/03-evaluation](../cohorts/2025/03-evaluation/)


[<< Previous: Instruction Following](08-instruction-following.md)
|
[Back to module](../)
