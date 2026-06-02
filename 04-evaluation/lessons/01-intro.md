# Evaluation

In the previous modules, we built search engines and RAG pipelines.
We tried different approaches: keyword search with minsearch, vector
search, agents with function calling. Now we need a way to decide which
one is actually better.

We could try a few queries by hand and see what looks good. That works
for a quick sanity check, but it doesn't scale. We need a systematic
way to compare approaches.

That's what evaluation is for.

## The evaluation setup

For search evaluation, we need a dataset of questions where we know
which document is the correct answer. We'll use an LLM to generate
these questions from our FAQ data.

The approach works like this:

- A = the original answer in the FAQ
- Q* = a question generated from that answer by an LLM
- We send Q* through our search and check if the original document
  appears in the results

For RAG evaluation, we go one step further:

- A = the original answer in the FAQ
- Q* = a question generated from that answer by an LLM
- A' = the answer produced by our RAG system when given Q*
- We compare A' with A to see if the system produced the right answer

This is the A → Q* → A' pattern. We know the answer for each generated
question because we created the question from that answer.

With evaluation, we can:

- Compare different search methods (minsearch vs vector search vs hybrid)
- Tune parameters (boost values, number of results, prompt templates)
- Compare different LLMs (gpt-5.4-mini vs others)
- Track improvements over time

There are two types of evaluation:

- Offline evaluation: run the system on a test dataset and compute metrics
- Online evaluation: collect feedback from real users in production

Offline evaluation is what we do before putting changes in front of
users. It lets us compare search settings, prompts, or models on the
same dataset. Online evaluation happens after deployment. It uses real
traffic, feedback, logs, and dashboards to monitor quality.

In this module, we focus on offline evaluation. We'll generate a test
dataset, run our search and RAG systems on it, and measure how well they
perform.

Synthetic data is a good starting point when you don't have real user
data. But generated questions can be too similar to the original FAQ
text, which inflates the metrics. As soon as you can, start collecting
real user queries and use them to validate your evaluation framework.

We'll cover three levels of evaluation:

1. Search evaluation: does the search return the right documents?
2. RAG evaluation: does the LLM generate good answers?
3. Agent evaluation: does the agent use tools efficiently?

For search, we'll use two metrics: Hit Rate and MRR (Mean Reciprocal
Rank). For RAG quality, we'll use LLM-as-a-judge. For agents, we'll
look at the final answer and the tool-call trajectory.

Let's start with generating the test data we need.

[← Back to module](../) | [Generating Ground Truth Data →](02-ground-truth.md)
