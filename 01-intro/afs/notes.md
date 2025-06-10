# Notes. Module 1

LLM is a model that predicts the next word in a sequence.

Promt -> LLM -> Answer

Question: How do I enroll in the course?
Context: ...
Answer: ...

## RAG

RAG = Retrieval Augmented Generation

Retrieval = search for relevant documents
Generation = generate answer

Example of RAG: Look up in google how to enroll in data engineering zoomcamp and tell me the answer.

User asks a question, then knowledge base is added to the question and finally it is sent to the LLM.

## Environment configuration

First variant is to make a new repo on github and create a codespace with it.

Let's try a local variant.

## Prompting

```txt
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT: 
{context}
```

Such a prompt starting sentence is working with slightly complex LLMs for helping get a good result.
