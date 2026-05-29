# Evaluating RAG

<a href="https://www.youtube.com/watch?v=lxpW2mR7dGk&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/lxpW2mR7dGk">
</a>

Retrieval evaluation tells us if we're finding the right documents.
RAG evaluation tells us if the generated answers are actually good.
We use the LLM-as-a-judge approach from module 04.

## LLM-as-a-Judge for RAG

Since we don't have reference answers for every question, we use
the LLM to evaluate the relevance of generated answers:

```python
prompt2_template = """
You are an expert evaluator for a RAG system.
Your task is to analyze the relevance of the generated answer to the given question.
Based on the relevance of the generated answer, you will classify it
as 'NON_RELEVANT', 'PARTLY_RELEVANT', or 'RELEVANT'.

Here is the data for evaluation:

Question: {question}
Generated Answer: {answer_llm}

Please analyze the content and context of the generated answer in relation to the question
and provide your evaluation in parsable JSON without using code blocks:

{{
  'Relevance': 'NON_RELEVANT' | 'PARTLY_RELEVANT' | 'RELEVANT',
  'Explanation': '[Provide a brief explanation for your evaluation]'
}}
""".strip()
```

Take a sample of ground truth questions, generate answers, and
evaluate:

```python
import json
from tqdm.auto import tqdm

df_sample = df_question.sample(n=200, random_state=1)
sample = df_sample.to_dict(orient="records")

evaluations = []

for record in tqdm(sample):
    question = record["question"]
    answer_llm = rag(question)

    prompt = prompt2_template.format(
        question=question,
        answer_llm=answer_llm
    )

    evaluation = llm(prompt)
    evaluation = json.loads(evaluation)

    evaluations.append((record, answer_llm, evaluation))
```

Analyze the results:

```python
df_eval = pd.DataFrame(evaluations, columns=["record", "answer", "evaluation"])

df_eval["id"] = df_eval.record.apply(lambda d: d["id"])
df_eval["question"] = df_eval.record.apply(lambda d: d["question"])
df_eval["relevance"] = df_eval.evaluation.apply(lambda d: d["Relevance"])
df_eval["explanation"] = df_eval.evaluation.apply(lambda d: d["Explanation"])

df_eval.relevance.value_counts(normalize=True)
```

You'll see something like:

```text
RELEVANT          0.85
PARTLY_RELEVANT   0.12
NON_RELEVANT      0.03
```

Save the results:

```python
df_eval.to_csv("data/rag-eval-gpt-5.4-mini.csv", index=False)
```

## Comparing models

You can also use evaluation to compare different LLMs.

For example,
compare gpt-5.4-mini with gpt-4o:

```python
evaluations_gpt4o = []

for record in tqdm(sample):
    question = record["question"]
    answer_llm = rag(question, model="gpt-4o")

    prompt = prompt2_template.format(
        question=question,
        answer_llm=answer_llm
    )

    evaluation = llm(prompt)
    evaluation = json.loads(evaluation)

    evaluations_gpt4o.append((record, answer_llm, evaluation))

df_eval = pd.DataFrame(evaluations_gpt4o, columns=["record", "answer", "evaluation"])
df_eval["relevance"] = df_eval.evaluation.apply(lambda d: d["Relevance"])
df_eval.relevance.value_counts(normalize=True)

df_eval.to_csv("data/rag-eval-gpt-4o.csv", index=False)
```

This gives you a concrete way to decide if a more expensive model
is worth the cost. Typically, the cheaper model gives similar
results for most questions.

[← Evaluating Retrieval](02-evaluating-retrieval.md) | [Interface and Ingestion Pipeline →](04-interface.md)
