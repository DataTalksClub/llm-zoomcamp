# RAG with Vector Search

In module 1, we built a RAG pipeline with three steps: search, build
prompt, send to LLM. The search step used keyword search (minsearch or
sqlitesearch).

Now we can replace the keyword search with vector search. Because our
`RAGBase` class takes any index with a `search` method, we just swap the
index.


## The keyword search RAG

In module 1, we used `RAGBase` with a minsearch `Index` (keyword search):

```python
from rag_helper import RAGBase, load_faq_data
from minsearch import Index
from openai import OpenAI

documents = load_faq_data()

index = Index(
    text_fields=["question", "section", "answer"],
    keyword_fields=["course"]
)
index.fit(documents)

openai_client = OpenAI()

instructions = """
You're a course teaching assistant.
Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.
""".strip()

rag = RAGBase(
    index=index,
    llm_client=openai_client,
    instructions=instructions,
)
```

Now let's swap the keyword index for a vector search index.


## Setting up vector search

We already have `documents` and `vectors` from the previous section.
Let's create the vector search index:

```python
from minsearch import VectorSearch

vindex = VectorSearch(keyword_fields=["course"])
vindex.fit(vectors, documents)
```


## Swapping into RAG

Create a new `RAGBase` instance with the vector index:

```python
rag_vector = RAGBase(
    index=vindex,
    llm_client=openai_client,
    instructions=instructions,
)
```

The only change is `index=index` became `index=vindex`. Everything else
stays the same.


## Vector search queries

Vector search takes a vector, not a string. We need a small wrapper:

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def vector_rag(query, course="data-engineering-zoomcamp", num_results=5):
    query_vector = model.encode(query)
    search_results = vindex.search(
        query_vector,
        filter_dict={"course": course},
        num_results=num_results
    )
    prompt = rag_vector.build_prompt(query, search_results)
    answer = rag_vector.llm(prompt)
    return answer
```

We use `build_prompt` and `llm` from `RAGBase` but do the search
manually because vector search requires embedding the query first.


## Testing

Try it:

```python
vector_rag("how do I run kafka?")
```

```python
vector_rag("the course has already started, can I still enroll?")
```

The answers should be similar to what we got with keyword search, but
vector search may handle rephrased questions better.


## Keyword search vs vector search for RAG

With keyword search, we use a minsearch `Index`:

```python
rag = RAGBase(index=index, llm_client=openai_client, instructions=instructions)
```

With vector search, we use a minsearch `VectorSearch`:

```python
rag_vector = RAGBase(index=vindex, llm_client=openai_client, instructions=instructions)
```

Same RAG class, different search index. The modular design lets you swap
search methods without touching the prompt or LLM code.

[← Vector Search with MinSearch](03-minsearch-vector.md) | [Vector Search with sqlitesearch →](05-sqlitesearch-vector.md)
