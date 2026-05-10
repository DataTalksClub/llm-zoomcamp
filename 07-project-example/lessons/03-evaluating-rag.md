# Evaluating RAG

<a href="https://www.youtube.com/watch?v=lxpW2mR7dGk&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/lxpW2mR7dGk">
</a>

Retrieval evaluation tells us if we're finding the right documents.
RAG evaluation tells us if the generated answers are actually good.
We use the LLM-as-a-judge approach from module 04.


## LLM-as-a-Judge for RAG

Since we don't have reference answers for every question, we use
the LLM to evaluate relevance. This is the same Q->A evaluation
we did in module 04:

```python
def evaluate_relevance(question, answer):
    prompt = f"""
    You are an expert evaluator for a RAG system.
    Analyze the relevance of the generated answer to the given question.
    Classify it as "NON_RELEVANT", "PARTLY_RELEVANT", or "RELEVANT".

    Question: {question}
    Generated Answer: {answer}

    Provide your evaluation as JSON:
    {{
      "Relevance": "NON_RELEVANT" | "PARTLY_RELEVANT" | "RELEVANT",
      "Explanation": "Brief explanation"
    }}
    """.strip()

    response = openai_client.responses.create(
        model="gpt-5.4-mini",
        input=[{"role": "user", "content": prompt}]
    )
    return response.output_text
```

Run this over all ground truth questions and count the percentage
of RELEVANT, PARTLY_RELEVANT, and NON_RELEVANT answers.


## Comparing models

You can also use evaluation to compare different LLMs. For example,
compare GPT-4o-mini vs GPT-4o:

```python
models = ['gpt-4o-mini', 'gpt-4o']

for model in models:
    relevance_counts = {'RELEVANT': 0, 'PARTLY_RELEVANT': 0, 'NON_RELEVANT': 0}

    for q in ground_truth:
        answer = rag(q['question'], model=model)
        eval_result = evaluate_relevance(q['question'], answer)
        # parse and count...

    print(f"Model: {model}")
    print(relevance_counts)
```

This gives you a concrete way to decide if a more expensive model
is worth the cost.


[<< Previous: Evaluating Retrieval](02-evaluating-retrieval)
|
[Next: Interface and Ingestion >>](04-interface)
