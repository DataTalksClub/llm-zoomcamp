# Introduction to RAG

This workshop is the first module of the
[LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) -
a free course about building LLM applications.

In this hands-on session, you'll build a working Retrieval-Augmented
Generation (RAG) system from scratch, step by step. No frameworks, no
magic - just Python, a search index, and an LLM.

If you want the full course (agents, vector search, evaluation,
monitoring, capstone project), check
[the repo](https://github.com/DataTalksClub/llm-zoomcamp).

To see my other tutorials, check [AI Shipping Labs](https://aishippinglabs.com/) - a community of AI Builders.

Places where you can find me:

- Alexey On Data substack: https://alexeyondata.substack.com/
- LinkedIn: https://www.linkedin.com/in/agrigorev/
- X: https://x.com/Al_Grigor


## Introduction

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


## Workshop sections

1. [Introduction](01-intro.md) - What we'll cover
2. [Environment](02-environment.md) - Prerequisites, setup, installing libraries
3. [Use Case](03-use-case.md) - The Course FAQ dataset
4. [What is RAG](04-rag.md) - LLMs, the RAG idea, RAG vs fine-tuning
5. [Search](05-search.md) - Fetching data, minsearch index, filtering, boosting
6. [Building the Prompt](06-building-prompt.md) - Prompt template, context, build_prompt
7. [The LLM](07-llm.md) - The LLM function, OpenAI API
8. [Full RAG](08-full-rag.md) - Wiring it together, the complete pipeline
9. [Data Ingestion](09-data-ingestion.md) - Ingestion script, sqlitesearch, two-process architecture
10. [Next Steps](10-next-steps.md) - Vector search, Elasticsearch, agents, evaluation, monitoring
