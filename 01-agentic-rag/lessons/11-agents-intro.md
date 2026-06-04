# Agents

Video: [Watch this lesson](https://www.youtube.com/watch?v=6uG4_Ivv60E&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

In Part 1 of this module we built RAG pipelines.

Every pipeline we wrote followed the same flow:

- search the FAQ,
- build a prompt with the results,
- send it to the LLM.

This returns good answers when the user's query matches the documents.
The search finds the right entry, the LLM reads it, and you get a
helpful reply.

Often, though, the search returns nothing useful.

- Maybe the user made a typo.
- Maybe they asked the question in an unusual way.
- Maybe they need information from two different searches.

We use lexical search here, so the search looks for an exact match.
One typo and it misses the entry it needed. In our pipeline there's
no recovery. The search runs once, and if it returns garbage the LLM
gets garbage. Our pipeline always does the same thing, no matter what.

Instead of routing the user question straight to search, we can hand
control to the LLM and let it drive.

The LLM is in charge now, and it can:

- fix typos
- search again with different terms
- ask the user a clarifying question

A fixed flow can't do any of this. Once we put the LLM in control,
our system becomes agentic, so it's flexible rather than rigid.

An agent uses an LLM to decide which actions to take and in which
order. Instead of a fixed flow, the LLM chooses what to do at each
step.

In Part 2 of this module, we'll cover:

- Function calling, so we can give the LLM tools it can use
- The agentic loop, where the LLM decides when to call a tool, when
  to call another one, and when to stop and answer
- Frameworks, the libraries that run this loop for you

We build on top of the RAG pipeline from Part 1, which used keyword
search with minsearch. If you skipped Part 1, the next lesson does a
quick revision and walks you through downloading the helpers.

[← Back to module](../) | [Quick RAG Revision →](12-rag-revision.md)
