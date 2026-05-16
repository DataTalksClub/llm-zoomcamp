# Hybrid Search

Vector search captures semantic meaning. Keyword search captures exact
term matches. Both have strengths:

- Vector search finds "Can I enroll late?" when the document says
  "Registration after the start date" - different words, same meaning
- Keyword search finds "pandas" when the user searches for "pandas"
  - no confusion with similar-sounding but unrelated concepts

Hybrid search combines both approaches. The idea: run both searches,
merge the results, and rank them together.

## Implementing hybrid search

We already have `keyword_search` and `vector_search` functions from the
previous sections.

The simplest way to combine them: run both and
concatenate the results:

```python
def hybrid_search(query, course='data-engineering-zoomcamp', num_results=10):
    keyword_results = keyword_search(query, course=course, num_results=num_results)
    vector_results = vector_search(query, course=course, num_results=num_results)

    combined = keyword_results + vector_results
    return combined
```

This works, but it's naive. Documents from keyword search always come
first, and duplicates appear twice. Plus we return more than the user requested.

There's a better way to merge them.


## Combining results

There are multiple approaches to combining search results.
We'll use fusion: merge the ranked lists from each search method and
compute a combined score based on rankings.

Reciprocal Rank Fusion (RRF) is a simple fusion method. The score
for each document is the sum of `1 / (k + rank + 1)` across all
lists where it appears.

Let's see how it works with an example.

- text search: `[A, B, C, D, E]`
- vector search: `[C, B, F, G, A]`
- they have 3 documents in common (A, B, C)

With `k = 1`:

```
Keyword ranks: A=0, B=1, C=2, D=3, E=4
Vector ranks:  C=0, B=1, F=2, G=3, A=4

RRF scores:
  A = 1/(1+0+1) + 1/(1+4+1) = 0.500 + 0.167 = 0.667
  B = 1/(1+1+1) + 1/(1+1+1) = 0.333 + 0.333 = 0.667
  C = 1/(1+2+1) + 1/(1+0+1) = 0.250 + 0.500 = 0.750
  D = 1/(1+3+1)              = 0.200
  E = 1/(1+4+1)              = 0.167
  F =              1/(1+2+1) = 0.250
  G =              1/(1+3+1) = 0.200

Final ranking: C, A/B (tie), F, D/G (tie), E
```

C wins because it ranks high in both lists. Documents that only
appear in one list get lower scores.


The parameter `k` smooths the
differences between ranks - higher `k` means rank position matters
less.

This algorithm works with any number of ranked lists, not just two.
So in our implementation we can generalize to an arbitrary number
of ranked results.

Let's implement it:

```python
def rrf(search_results, k=1, num_results=10):
    scores = {}
    doc_map = {}

    for results in search_results:
        for rank, doc in enumerate(results):
            key = doc['question']
            if key not in scores:
                scores[key] = 0
                doc_map[key] = doc
            scores[key] += 1 / (k + rank + 1)

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [doc_map[key] for key, _ in ranked[:num_results]]
```

Let's put everything together:


```python
def hybrid_search(query, course='data-engineering-zoomcamp', num_results=10):
    keyword_results = keyword_search(query, course=course, num_results=num_results)
    vector_results = vector_search(query, course=course, num_results=num_results)
    return rrf([keyword_results, vector_results], num_results=num_results)
```


## Using hybrid search in RAG

Set up `RAGBase`:

```python
from rag_helper import RAGBase
from openai import OpenAI

openai_client = OpenAI()

instructions = """
You're a course teaching assistant.
Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.
""".strip()

assistant = RAGBase(
    index=index,
    llm_client=openai_client,
    instructions=instructions,
)
```

Now use hybrid search with the RAG pipeline:

```python
def hybrid_rag(query, course='data-engineering-zoomcamp', num_results=10):
    search_results = hybrid_search(query, course=course, num_results=num_results)
    prompt = assistant.build_prompt(query, search_results)
    answer = assistant.llm(prompt)
    return answer
```

Try it:

```python
hybrid_rag('How do I run Kafka?')
```

```python
hybrid_rag('uploading to S3 fails')
```

[← Text Search vs Vector Search](08-text-vs-vector.md) | [Using ONNX Runtime →](10-onnx-embedder.md)
