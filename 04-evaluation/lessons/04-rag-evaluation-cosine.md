# RAG Evaluation: Cosine Similarity

In the previous lesson, we evaluated search quality -- whether the right
documents show up in the results. But good search doesn't guarantee good
answers. The LLM might ignore the context, hallucinate, or produce a
poor response.

In this lesson, we evaluate the entire RAG pipeline: search + prompt +
LLM. The question is: how good are the answers?


## The A->Q->A' approach

We already have ground truth data with questions generated from FAQ
documents. Each FAQ document has an original answer. Here's the idea:

1. Take a question from the ground truth (generated from document D)
2. Run the RAG pipeline to get an LLM answer
3. Compare the LLM answer with the original answer from document D

This is sometimes called the A->Q->A' evaluation:

- A = original answer in the FAQ
- Q = generated question (from A)
- A' = LLM answer (from Q through RAG)

If the LLM answer is similar to the original answer, the RAG pipeline
is working well.


## Generating RAG answers

Let's run the RAG pipeline on our ground truth data. First, set up the
search and LLM functions:

```python
from openai import OpenAI
openai_client = OpenAI()

INSTRUCTIONS = """
You're a course teaching assistant.
Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.
""".strip()

PROMPT_TEMPLATE = """
QUESTION: {question}

CONTEXT:
{context}
""".strip()

def build_context(search_results):
    context = ""
    for doc in search_results:
        context += f"section: {doc['section']}\n"
        context += f"question: {doc['question']}\n"
        context += f"answer: {doc['answer']}\n"
        context += "\n"
    return context.strip()

def build_prompt(query, search_results):
    context = build_context(search_results)
    return PROMPT_TEMPLATE.format(question=query, context=context)

def llm(instructions, user_prompt, model="gpt-5.4-mini"):
    input_messages = [
        {"role": "developer", "content": instructions},
        {"role": "user", "content": user_prompt}
    ]
    response = openai_client.responses.create(
        model=model,
        input=input_messages
    )
    return response.output_text

def rag(query, course="data-engineering-zoomcamp", model="gpt-5.4-mini"):
    search_results = search(query, course=course)
    prompt = build_prompt(query, search_results)
    answer = llm(INSTRUCTIONS, prompt, model=model)
    return answer
```

Now run RAG on all ground truth questions and collect both the LLM
answer and the original answer:

```python
doc_idx = {d['id']: d for d in documents}

answers = {}

for i, rec in enumerate(tqdm(ground_truth_flat)):
    if i in answers:
        continue

    answer_llm = rag(rec['question'], course=rec['course'])
    doc_id = rec['document']
    original_doc = doc_idx[doc_id]
    answer_orig = original_doc['answer']

    answers[i] = {
        'answer_llm': answer_llm,
        'answer_orig': answer_orig,
        'document': doc_id,
        'question': rec['question'],
        'course': rec['course'],
    }
```

This takes a while because we're calling the LLM for each question.
We can speed it up with `ThreadPoolExecutor` the same way we did for
data generation.


## Cosine similarity

To compare the LLM answer with the original answer, we compute cosine
similarity. First, we turn both answers into vectors using an embedding
model:

```python
from sentence_transformers import SentenceTransformer

model_name = 'multi-qa-MiniLM-L6-cos-v1'
embedding_model = SentenceTransformer(model_name)
```

Then for each answer pair, we encode both and compute the dot product:

```python
import numpy as np

results = []

for i, rec in answers.items():
    v_llm = embedding_model.encode(rec['answer_llm'])
    v_orig = embedding_model.encode(rec['answer_orig'])
    score = v_llm.dot(v_orig)

    results.append({
        'answer_llm': rec['answer_llm'],
        'answer_orig': rec['answer_orig'],
        'cosine': score,
        'document': rec['document'],
        'question': rec['question'],
        'course': rec['course'],
    })

df_results = pd.DataFrame(results)
```

The cosine similarity ranges from -1 to 1. Higher values mean the
answers are more similar. Let's check the average:

```python
df_results['cosine'].describe()
```

A typical result for a working RAG system might be around 0.7-0.8.
Lower values suggest the LLM is not using the context well, or the
search is returning irrelevant documents.


## Comparing models

With this framework, we can compare different LLMs:

```python
models = ['gpt-5.4-mini']

for model_name in models:
    answers_model = {}

    for i, rec in enumerate(tqdm(ground_truth_flat)):
        answer_llm = rag(rec['question'], course=rec['course'], model=model_name)
        doc_id = rec['document']
        original_doc = doc_idx[doc_id]
        answer_orig = original_doc['answer']

        answers_model[i] = {
            'answer_llm': answer_llm,
            'answer_orig': answer_orig,
        }

    cosines = []
    for rec in answers_model.values():
        v_llm = embedding_model.encode(rec['answer_llm'])
        v_orig = embedding_model.encode(rec['answer_orig'])
        cosines.append(v_llm.dot(v_orig))

    print(f"{model_name}: mean cosine = {np.mean(cosines):.3f}")
```

This gives you a number you can use to decide which model produces
better answers for your use case.

Cosine similarity is a good starting point, but it has limitations. Two
answers can be semantically similar but have different wording, and the
score might not reflect the true quality. In the next lesson, we'll use
an LLM to judge answer quality directly.


[<< Previous: Search Evaluation](03-search-evaluation)
|
[Next: LLM as a Judge >>](05-llm-as-judge)
