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


## What we'll cover

Large Language Models (LLMs) are powerful, but they have limitations:

- They don't know about your private data.
- Their training data has a cutoff date.
- They sometimes hallucinate - make things up that sound plausible.

RAG solves these problems by giving the LLM relevant documents at
question time. Instead of hoping the model memorized the answer, we
retrieve the right information and hand it to the LLM to generate
a grounded response.

In this workshop, we will:

- Understand what RAG is and how it works
- Build a search engine over a real FAQ dataset
- Write a prompt that combines the user's question with search results
- Wire it all together into a working RAG pipeline
- Split ingestion and query into separate processes
- Discuss what comes next (agents, vector search, Elasticsearch)
