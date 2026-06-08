# Introduction

Video: [Watch this lesson](https://www.youtube.com/watch?v=rQYyFxf1FWw&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

In this module, we'll build a working Retrieval-Augmented
Generation (RAG) system from scratch, step by step.

We write everything in plain Python. We build a small search index by
hand and call the LLM ourselves. I want you to see every piece first.
That way you know what a framework does for you before you reach for
one.

Before you start, it's important to go through the course documentation:

- [Zoomcamp Logistics](https://datatalks.club/docs/courses/zoomcamp-logistics/)
- [LLM Zoomcamp](https://datatalks.club/docs/courses/llm-zoomcamp/)

Places where you can find me:

- [My substack](https://alexeyondata.substack.com/)
- [LinkedIn](https://www.linkedin.com/in/agrigorev/)
- [X](https://x.com/Al_Grigor)

## LLMs

An LLM (Large Language Model) is a neural network trained on massive
amounts of text. Given a prompt, it generates a continuation - a
plausible next piece of text.

Think of your phone. When you type "how are" in WhatsApp, it suggests
"you" as the next word. "How are you" is the most common continuation.
Your phone uses a simple language model for that. It predicts the next
word based on what you typed so far.

A large language model does the same thing, but at a much larger scale.
It has billions of parameters and is trained on most of the text on the
internet. When it predicts the next word, it feels like you're talking
to an intelligent being. It understands what you ask and gives
meaningful answers.

In this course, we treat LLMs as black boxes. We won't look inside or
cover the theory, and we won't host a model ourselves. We use an LLM
provider and call it over an API. For us, an LLM is a box: text goes in,
text comes out.

But LLMs have limitations:

- Knowledge cutoff: they only know what was in their training data.
  If you ask about something that happened after training, they won't
  know - or worse, they'll make something up.
- No access to your data: they can't see your documents, databases,
  or internal systems unless you provide that information.
- Hallucinations: they sometimes produce confident-sounding answers
  that are simply wrong.

## The project

RAG solves these problems by giving the LLM relevant documents at
question time. We don't hope the model memorized the answer. We
retrieve the right information and hand it to the LLM, and the model
generates a grounded response. This lets us inject knowledge the model
never saw during training. That's why RAG is still the most common way
people use LLMs in the industry.

To make this concrete, we build a FAQ agent for our course. A student
asks something like "when does the course start?" and the agent answers
from the FAQ data we prepared.

This module has two parts.

In Part 1 (the next 9 lessons) we will:

- Understand what RAG is and how it works
- Build a search engine over a real FAQ dataset
- Write a prompt that combines the user's question with search results
- Wire it all together into a working RAG pipeline
- Split ingestion and query into separate processes

In Part 2, we make the pipeline agentic. The LLM decides when and
what to search, instead of running the same fixed flow every time.

The final code from this module is available in the
[code/](../code/) directory.

[← Back to module](../) | [Environment →](02-environment.md)
