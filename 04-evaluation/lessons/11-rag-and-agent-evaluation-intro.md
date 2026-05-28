# RAG and Agent Evaluation

So far, we evaluated retrieval. We checked whether search returns the
document that should answer the question.

That is only the first step. A complete application still needs to
produce a final answer. For RAG, this means checking the generated
answer. For agents, it also means looking at the tool calls the model
made before producing the answer.

In this part, we'll evaluate:

- RAG answers with cosine similarity
- RAG answers with an LLM judge
- Agent answers and tool-call trajectories

We won't go deep into agent evaluation frameworks here. We'll use the
agent from module 01, save the final answer, and also save the tool
calls. Then we can look at whether the answer is good and whether the
trajectory looks reasonable.

Next, we'll start with the RAG case and generate answers for the ground
truth questions.

[← Search Evaluation Metrics](05-search-metrics.md) | [Generating RAG Answers →](12-rag-answers.md)
