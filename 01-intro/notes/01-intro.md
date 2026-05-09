# Introduction

This workshop is the first module of the
[LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) -
a free course about building LLM applications.

In this hands-on session, you'll build a working Retrieval-Augmented
Generation (RAG) system from scratch, step by step. No frameworks, no
magic - just Python, a search index, and an LLM.

Places where you can find me:

- Alexey On Data substack: https://alexeyondata.substack.com/
- LinkedIn: https://www.linkedin.com/in/agrigorev/
- X: https://x.com/Al_Grigor


## Large Language Models

A Large Language Model (LLM) is a neural network trained on massive
amounts of text. Given a prompt, it generates a continuation - a
plausible next piece of text.

LLMs are good at:

- Answering general knowledge questions
- Summarizing, translating, and rewriting text
- Writing code
- Following instructions

But they have important limitations:

- Knowledge cutoff: they only know what was in their training data.
  If you ask about something that happened after training, they won't
  know - or worse, they'll make something up.
- No access to your data: they can't see your documents, databases,
  or internal systems unless you provide that information.
- Hallucinations: they sometimes produce confident-sounding answers
  that are simply wrong.


## RAG

RAG solves these problems by giving the LLM relevant documents at
question time. Instead of hoping the model memorized the answer, we
retrieve the right information and hand it to the LLM to generate
a grounded response.

In this module, we will:

- Understand what RAG is and how it works
- Build a search engine over a real FAQ dataset
- Write a prompt that combines the user's question with search results
- Wire it all together into a working RAG pipeline
- Split ingestion and query into separate processes
- Discuss what comes next (agents, vector search, Elasticsearch)
