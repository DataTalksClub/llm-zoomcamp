# What is RAG

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


## The RAG idea

RAG stands for Retrieval-Augmented Generation. There are two key
words here: generation and retrieval. Generation is the LLM - it
generates text. Retrieval is search. We use search to augment the
LLM's generation.

In other words: we retrieve relevant documents from our knowledge
base, and use them to augment what the LLM generates.

The flow:

1. The user asks a question.
2. We search our knowledge base for documents relevant to the question.
3. We build a prompt that includes the question and the retrieved documents.
4. We send the prompt to the LLM, which generates an answer based
   on the documents we provided.

In code, it looks like this:

```python
def rag(question):
    search_results = search(question)
    user_prompt = build_prompt(question, search_results)
    return llm(user_prompt)
```

That's the entire architecture. Three components:

- search
- prompt
- LLM

The LLM only sees the documents we hand it. So its answers are
grounded in our data. If the right document is retrieved, the answer
is good. If it's not, the answer suffers. Search quality is the
backbone of RAG.

The database and the LLM can be anything. In this workshop we'll
use minsearch and then sqlitesearch for search, and OpenAI for the
LLM. But you can swap any component and see what works better. That's
what makes RAG so flexible - plug and play.


## RAG vs fine-tuning

A common question: why not fine-tune the model on our data instead?

Fine-tuning changes the model's behavior (how it responds, what
style it uses), but it's not great for injecting knowledge. You'd
need to retrain every time your data changes.

RAG keeps the model frozen and brings fresh data to it at query time.
It's simpler, cheaper, and always up-to-date.

In practice, they complement each other - fine-tune for style, RAG
for knowledge.
