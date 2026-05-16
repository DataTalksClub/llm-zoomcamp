# Agents

In modules 1 and 2, we built RAG pipelines. We used keyword search
with minsearch and sqlitesearch, and vector search with the same tools
plus PGVector. The idea was always the same: search the FAQ, build a
prompt with the results, and send it to the LLM.

This works well when the user's query matches the documents. The search
finds the right answer, the LLM reads it, and the response is good.

But what happens when the search doesn't find anything useful? Maybe the
user made a typo. Maybe they asked the question in an unusual way. Maybe
they need information from two different searches.

In our RAG pipeline, there's no recovery. The search runs once. If it
returns garbage, the LLM gets garbage. The pipeline is rigid: it
always does the same thing, no matter what.

Sometimes the LLM needs to decide what to do. Maybe it should search
with different terms. Maybe it should try a different course. Maybe it
should ask the user a clarifying question. A fixed pipeline can't do
any of this.

That's what agents are for. An agent gives the LLM the ability to take
actions and make decisions. Instead of a fixed pipeline, the LLM
chooses what to do at each step.

In this module, we'll cover:

- Function calling: how to give the LLM tools it can use
- The agentic loop: how the LLM decides when to call a tool, when to
  call another one, and when to stop and give the final answer
- Frameworks: libraries that handle the loop for you

We'll build on top of the RAG pipeline from module 1, keyword search
with minsearch. If you haven't completed module 1, that's fine. We'll
do a quick revision in the next lesson.

[← Back to module](../) | [Quick RAG Revision →](02-rag-revision.md)
