# RAG with Vector Search

In module 1, we built a RAG pipeline with three steps:

```python
def rag(question):
    search_results = search(question)
    user_prompt = build_prompt(question, search_results)
    return llm(user_prompt)
```

The search step used keyword search. Now we can replace it with vector search.

## The keyword search RAG

In module 1, we put all the RAG logic into a
[RAGBase](../../01-intro/code/rag_helper.py)
helper class.

If you don't have it, let's download it: 

```bash
wget https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/01-intro/code/rag_helper.py
```

Let's quickly go over what we did previously.

First, create the OpenAI client:

```python
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_client = OpenAI()
```

Next, download and index the data:

```python
from ingest import load_faq_data, build_index

documents = load_faq_data()
index = build_index(documents)
```

Finally, use the `RAGBase` class:

```python
from rag_helper import RAGBase

assistant = RAGBase(
    index=index,
    llm_client=openai_client,
)
```

Ask it a question:

```python
assistant.rag(query)
```

## Swapping into RAG

We already have:

- All the indexed documents `documents`
- The embeddings matrix `X` with all these documents
- The vector search engine `vindex` 

To add vector search to our RAG, we need to put `vindex` in RAG.
But we cannot just pass `vindex` there directly. We need to update
the `search` method to first transform the user query into a vector.

We will do it by creating a subclass of `RAGBase` that overrides the `search` method:

```python

class RAGVector(RAGBase):

    def __init__(self, embedder, **kwargs):
        super().__init__(**kwargs)
        self.embedder = embedder

    def search(self, query, num_results=5):
        query_vector = self.embedder.encode(query)
        filter_dict = {'course': self.course}

        return self.index.search(
            query_vector,
            num_results=num_results,
            filter_dict=filter_dict
        )
```

Here in `__init__` we add a new argument: `embedder` for our sentence tranformer, 
which we later use in `search` for turning the query into a vector.

## Using it

Let's init it:

```python
vector_assistant = RAGVector(
    embedder=model,
    index=vindex,
    llm_client=openai_client,
)
```

Try it with different queries:

```python
vector_assistant.rag('the program has already begun, can I still sign up?')
```

The answers should be similar to what we got with keyword search, but
vector search may handle rephrased questions better.

[← Vector Search with minsearch](05-minsearch-vector.md) | [Vector Search with sqlitesearch →](07-sqlitesearch-vector.md)
