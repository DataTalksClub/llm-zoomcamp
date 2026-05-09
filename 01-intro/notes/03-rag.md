# What is RAG

## Large Language Models

A Large Language Model (LLM) is a neural network trained on massive
amounts of text. Given a prompt, it generates a continuation - a
plausible next piece of text.

You've probably used ChatGPT, which is powered by GPT-4o. Other
popular models include Claude, Gemini, and Llama.

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


## The RAG idea

RAG (Retrieval-Augmented Generation) is a simple but powerful idea:
instead of hoping the LLM knows the answer, we give it the answer
by attaching relevant documents to the prompt.

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

That's the entire architecture. Three components: search, prompt, LLM.

The key insight: the LLM only sees the documents we hand it. So its
answers are grounded in our data. If the right document is retrieved,
the answer is good. If it's not, the answer suffers. Search quality
is the backbone of RAG.


## RAG vs fine-tuning

A common question: why not fine-tune the model on our data instead?

Fine-tuning changes the model's behavior (how it responds, what
style it uses), but it's not great for injecting knowledge. You'd
need to retrain every time your data changes.

RAG keeps the model frozen and brings fresh data to it at query time.
It's simpler, cheaper, and always up-to-date.

In practice, they complement each other - fine-tune for style, RAG
for knowledge.
