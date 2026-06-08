# RAG with Vector Search

Video: [Watch this lesson](https://www.youtube.com/watch?v=-GBW3g3PVTM&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

In module 1, we built a RAG pipeline with three steps:

```python
def rag(question):
    search_results = search(question)
    user_prompt = build_prompt(question, search_results)
    return llm(user_prompt)
```

The search step used keyword search. Now we swap in vector search.
Because RAG is modular, search is the only step we touch. Build prompt
and the LLM call stay exactly as they were.

## Using RAGBase

In [module 1](../../01-agentic-rag/) we put all the RAG logic into a
[`RAGBase`](../../01-agentic-rag/code/rag_helper.py) helper class. It
has `search`, `build_prompt`, and `llm` methods, so we only need to
override `search`.

Download `rag_helper.py` (and `ingest.py` if you didn't get it earlier)
into your project:

```bash
wget https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/01-agentic-rag/code/rag_helper.py
wget https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/01-agentic-rag/code/ingest.py
```

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

Then use the `RAGBase` class:

```python
from rag_helper import RAGBase

assistant = RAGBase(
    index=index,
    llm_client=openai_client,
)
```

Ask it a question:

```python
query = "I just found out about the program, can I still sign up?"
assistant.rag(query)
```

This still uses keyword search. Text search isn't bad here, so the
answer may already look right. Next we replace search with vector
search.

We already have:

- All the indexed documents `documents`
- The embeddings matrix `X` with all these documents
- The vector search engine `vindex`

We can't pass `vindex` to RAG as-is. Text search takes the query string
directly, but vector search needs the query as a vector first. So we
subclass `RAGBase` and override `search` to encode the query before
searching.

The subclass overrides `search`:

```python

class RAGVector(RAGBase):

    def __init__(self, embedder, **kwargs):
        super().__init__(**kwargs)
        self.embedder = embedder

    def search(self, query, num_results=5):
        query_vector = self.embedder.encode(query)
        filter_dict = {"course": self.course}

        return self.index.search(
            query_vector,
            num_results=num_results,
            filter_dict=filter_dict
        )
```

The `__init__` method adds one extra argument, `embedder`, for the
sentence transformer. Inside `search` we use it to turn the query into a
vector. Then we query `vindex` with that vector instead of the raw text.
Everything else is inherited from `RAGBase`.

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
vector_assistant.rag("the program has already begun, can I still sign up?")
```

The answers should be close to what we got with keyword search, but
vector search handles rephrased questions better. The swap was trivial
because RAG has three clear steps. The same trick lets us change the LLM
provider later by overriding just the `llm` step.

[← Vector Search with minsearch](05-minsearch-vector.md) | [Vector Search with sqlitesearch →](07-sqlitesearch-vector.md)
