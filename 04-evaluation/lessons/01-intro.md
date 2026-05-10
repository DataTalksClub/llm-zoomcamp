# Evaluation

In the previous modules, we built search engines and RAG pipelines.
We tried different approaches: keyword search with minsearch, vector
search, agents with function calling. But how do we know which one is
actually better?

We could try a few queries by hand and see what looks good. That works
for a quick sanity check, but it doesn't scale. We need a systematic
way to compare approaches.

That's what evaluation is for. With evaluation, we can:

- Compare different search methods (minsearch vs vector search vs hybrid)
- Tune parameters (boost values, number of results, prompt templates)
- Compare different LLMs (gpt-5.4-mini vs others)
- Track improvements over time

There are two types of evaluation:

- Offline evaluation: run the system on a test dataset and compute metrics
- Online evaluation: collect feedback from real users in production

In this module, we focus on offline evaluation. We'll generate a test
dataset, run our search and RAG systems on it, and measure how well they
perform.

We'll cover three levels of evaluation:

1. Search evaluation: does the search return the right documents?
2. RAG evaluation: does the LLM generate good answers?
3. Agent evaluation: does the agent use tools efficiently?

For search, we'll use two metrics: Hit Rate and MRR (Mean Reciprocal
Rank). For RAG quality, we'll use cosine similarity and LLM-as-a-judge.
For agents, we'll look at trajectory evaluation and instruction following.

Let's start with generating the test data we need.


[<< Back to module](../)
|
[Next: Generating Ground Truth >>](02-generating-ground-truth)
