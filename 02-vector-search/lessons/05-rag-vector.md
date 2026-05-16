# RAG with Vector Search

In module 1, we built a RAG pipeline with three steps: search, build
prompt, send to LLM. The search step used keyword search (minsearch or
sqlitesearch).

Now we can replace the keyword search with vector search. Because our
`RAGBase` class takes any index with a `search` method, we just swap the
index.


## The keyword search RAG

In module 1, we used `RAGBase` with a minsearch `Index` (keyword search).
First, the imports and data loading:

```python
from rag_helper import RAGBase
from ingest import load_faq_data
from minsearch import Index
from openai import OpenAI

documents = load_faq_data()
```

Then, create the keyword search index:

```python
index = Index(
    text_fields=['question', 'section', 'answer'],
    keyword_fields=['course']
)
index.fit(documents)
```

And set up the RAG assistant:

```python
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

Now let's swap the keyword index for a vector search index.


## Setting up vector search

We already have `documents` and `vectors` from the previous section.
Let's create the vector search index:

```python
from minsearch import VectorSearch

vindex = VectorSearch(keyword_fields=['course'])
vindex.fit(vectors, documents)
```


## Swapping into RAG

We can't just pass `vindex` to `RAGBase` directly, because `RAGBase.search`
passes the query as a string and includes `boost_dict` - parameters that
only work with keyword search. Vector search needs the query as a vector.

So we create a subclass that overrides the `search` method to embed the
query first:

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')


class RAGVector(RAGBase):

    def __init__(self, model, **kwargs):
        super().__init__(**kwargs)
        self.model = model

    def search(self, query, num_results=5):
        query_vector = self.model.encode(query)
        filter_dict = {'course': self.course}

        return self.index.search(
            query_vector,
            num_results=num_results,
            filter_dict=filter_dict
        )
```

Now create the vector search RAG assistant:

```python
assistant = RAGVector(
    model=model,
    index=vindex,
    llm_client=openai_client,
    instructions=instructions,
)
```

The only change is `RAGBase` became `RAGVector`, and we pass the
embedding `model`. Everything else stays the same.


## Testing

Try it:

```python
assistant.rag('how do I run kafka?')
```

```python
assistant.rag('the course has already started, can I still enroll?')
```

The answers should be similar to what we got with keyword search, but
vector search may handle rephrased questions better.


## Keyword search vs vector search for RAG

With keyword search, we use `RAGBase` with a minsearch `Index`:

```python
assistant = RAGBase(index=index, llm_client=openai_client, instructions=instructions)
```

With vector search, we use `RAGVector` with a minsearch `VectorSearch`:

```python
assistant = RAGVector(model=model, index=vindex, llm_client=openai_client, instructions=instructions)
```

Same RAG logic, different search backend. The modular design lets you swap
search methods without touching the prompt or LLM code.

[← Vector Search with minsearch](04-minsearch-vector.md) | [Vector Search with sqlitesearch →](06-sqlitesearch-vector.md)
