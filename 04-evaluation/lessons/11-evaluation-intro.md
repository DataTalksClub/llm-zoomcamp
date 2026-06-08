# RAG and Agent Evaluation

Video: [Watch this lesson](https://www.youtube.com/watch?v=VKHBP0QSCFo&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

So far, we evaluated retrieval. We checked whether search returns the
document that should answer the question.

That is only the first step. A complete application still needs to
produce a final answer. For RAG, this means checking the generated
answer. For agents, it also means looking at the tool calls the model
made before producing the answer.

RAG evaluation checks the whole flow together.

This includes:

- search
- prompt
- LLM

If the final answer is bad, the problem can come from any of these
steps. The search might retrieve the wrong document, the prompt might
omit important context, or the LLM might ignore the context.

In this part, we'll evaluate:

- RAG answers with an LLM judge
- Agent answers and tool-call trajectories

We won't go deep into agent evaluation frameworks here. We'll use the
agent from module 01, save the final answer, and also save the tool
calls. Then we can look at whether the answer is good and whether the
trajectory looks reasonable.

## LLM as a judge

For RAG and agent evaluation, we compare the generated answer with the
original answer. The generated answer won't use the same words as the
original. It's a generative model, so the phrasing will be different
even when the meaning is the same.

This is why we use another LLM to do the comparison. We show the judge
the question, the original answer, and the generated answer. Then we ask
it to decide if they are semantically equivalent.

This approach is called LLM-as-a-judge. The evaluating LLM is the
judge. It classifies each answer as good or bad and explains its
reasoning. Asking the judge to explain why it made a decision generally
produces better classifications than asking for just the verdict.

Next, we'll start with the RAG case and generate answers for the ground
truth questions.

[← Search Parameter Tuning](06-search-tuning.md) | [Generating RAG Answers →](12-rag-answers.md)
