# Next Steps

Video: [Watch this lesson](https://www.youtube.com/watch?v=TlKPBjItUw8&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

In this module, we covered evaluation at three levels:

1. Search evaluation: Hit Rate and MRR to measure retrieval quality
2. RAG evaluation: LLM-as-a-judge for answer quality
3. Agent evaluation: final answers plus tool-call trajectories

Evaluation is not a one-time activity. As you tune search parameters,
switch models, or modify prompts, re-run evaluation. Make sure the
system is getting better, not worse.

Evaluation is the most important part of building AI systems. It is also
the most time-consuming. Only after evaluation can you be confident
that your system works. Validate every change against your evaluation
framework before going to production. This applies to prompt updates,
model swaps, and agent modifications.

## From synthetic data to real data

The evaluation workflow in practice:

1. Start with synthetic data. Use an LLM to generate questions from
   your FAQ or documentation. This gives you a baseline without needing
   real users.
2. Tune the data generation. If the metrics look suspiciously good,
   the synthetic questions may be too close to the source text. Adjust
   the generation prompt to produce more realistic questions.
3. Deploy and collect real data. Once the system is in production, start
   collecting actual user queries and feedback.
4. Label real data. Have humans label whether the retrieved documents
   and generated answers are correct. This produces the most reliable
   ground truth.
5. Tune synthetic generation to match real data. Use the patterns from
   real queries to improve your synthetic data generator. The closer
   your synthetic data is to real data, the more useful the metrics
   become.

Nothing beats manual evaluation. Try the system yourself, think about
edge cases, and collect examples of where it fails. This is especially
important in the early stages when you don't have automated evaluation
set up yet.

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
system.

Key approaches:

- User feedback: thumbs up/down buttons to collect signal
- Logging: record queries, retrieved documents, and answers
- Dashboards: track metrics over time to spot degradation
- Alerts: get notified when metrics drop below a threshold

Monitoring is covered in more detail in module 05.

## To learn more

See also:

- Cohorts and materials:
  - 2024 cohort evaluation module (uses Elasticsearch):
    [2024/04-monitoring](../../cohorts/2024/04-monitoring/)
  - 2025 cohort evaluation module:
    [2025/03-evaluation](../../cohorts/2025/03-evaluation/)

[← Agent Evaluation](14-agent-evaluation.md) | [Back to module →](../)
