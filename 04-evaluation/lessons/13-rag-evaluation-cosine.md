# RAG Evaluation: Cosine Similarity

In the previous lesson, we generated RAG answers for the ground truth
questions.

Now we compare each RAG answer with the original FAQ answer. We'll use
cosine similarity as a simple first metric.

## Loading RAG answers

Load the answers from the previous notebook:

```python
import pandas as pd

df_answers = pd.read_csv("data/rag-answers.csv")
```

Each row contains:

- `question`: the generated question
- `answer_llm`: the answer from our RAG system
- `answer_orig`: the original FAQ answer
- `document`: the FAQ document ID

## Computing similarity

First, load an embedding model:

```python
from sentence_transformers import SentenceTransformer

model_name = "multi-qa-MiniLM-L6-cos-v1"
embedding_model = SentenceTransformer(model_name)
```

Compute the similarity for one answer pair:

```python
rec = df_answers.iloc[0]

v_llm = embedding_model.encode(rec["answer_llm"])
v_orig = embedding_model.encode(rec["answer_orig"])

score = v_llm.dot(v_orig)
score
```

The score is between `-1` and `1`. Higher values mean the answers are
more similar.

Now compute the score for every answer:

```python
cosines = []

for _, rec in df_answers.iterrows():
    v_llm = embedding_model.encode(rec["answer_llm"])
    v_orig = embedding_model.encode(rec["answer_orig"])
    score = v_llm.dot(v_orig)
    cosines.append(score)
```

Add the scores to the dataframe:

```python
df_answers["cosine"] = cosines
```

Check the distribution:

```python
df_answers["cosine"].describe()
```

A typical result for a working RAG system might be around `0.7` to
`0.8`. Lower values suggest that the answer differs from the original
FAQ answer.

## Looking at examples

Look at low-scoring answers:

```python
df_answers.sort_values("cosine").head()
```

Then open one example:

```python
rec = df_answers.sort_values("cosine").iloc[0]

print("Question:")
print(rec["question"])
print()
print("RAG answer:")
print(rec["answer_llm"])
print()
print("Original answer:")
print(rec["answer_orig"])
```

Cosine similarity is useful as a starting point, but it has
limitations. Two correct answers can use different wording, and a
similar-looking answer can still miss an important detail.

In the next lesson, we'll use an LLM to judge answer quality directly.

[← Generating RAG Answers](12-rag-answers.md) | [LLM as a Judge →](14-llm-as-judge.md)
