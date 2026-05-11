# Introduction

In this module, you'll build a working Retrieval-Augmented
Generation (RAG) system from scratch, step by step.

No frameworks, no magic - just Python, a search index, and an LLM.

Places where you can find me:

- Alexey On Data substack: https://alexeyondata.substack.com/
- LinkedIn: https://www.linkedin.com/in/agrigorev/
- X: https://x.com/Al_Grigor


## What are LLMs

An LLM (Large Language Model) is a neural network trained on massive
amounts of text. Given a prompt, it generates a continuation - a
plausible next piece of text.

Think of your phone. When you type "how are" in WhatsApp, it
suggests "you" as the next word - because "how are you" is the most
common continuation. Your phone uses a simple language model for
that. It predicts the next word based on what you typed so far.

A large language model does the same thing, but at a much larger
scale. It has billions of parameters, is trained on tons of data,
and when it predicts the next word, it feels like you're talking to
an intelligent being. It understands what you ask and gives
meaningful answers.

In this course, we treat LLMs as black boxes. We won't look inside
or cover the theory. For us, an LLM is a box: text goes in, text
comes out.

But LLMs have limitations:

- Knowledge cutoff: they only know what was in their training data.
  If you ask about something that happened after training, they won't
  know - or worse, they'll make something up.
- No access to your data: they can't see your documents, databases,
  or internal systems unless you provide that information.
- Hallucinations: they sometimes produce confident-sounding answers
  that are simply wrong.


## What we'll build

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

The final code from this module is available in the
[code/](../code/) directory.

[← Back to module](../) | [Environment →](02-environment.md)
