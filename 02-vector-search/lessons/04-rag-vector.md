# RAG with Vector Search

In module 1, we built a RAG pipeline with three steps: search, build
prompt, send to LLM. The search step used keyword search (minsearch or
sqlitesearch).

Now we can replace the keyword search with vector search. The modular
structure of our RAG function makes this easy - we just swap the search
function.


## The keyword search RAG

Here's the RAG function from module 1:

```python
def rag(query, model="gpt-5.4-mini"):
    search_results = search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(INSTRUCTIONS, prompt, model=model)
    return answer
```

The `search` function does keyword search with minsearch. Since we have
this modular structure, we can easily replace it with a different
function. We saw this previously when we swapped minsearch with
sqlitesearch. Now let's swap keyword search for vector search.


## Setting up vector search

We already have `documents` and `vectors` from the previous section.
Let's create the vector search index:

```python
from minsearch import VectorSearch

vindex = VectorSearch(keyword_fields=["course"])
vindex.fit(vectors, documents)
```


## The vector search function

```python
def vector_search(query, course="data-engineering-zoomcamp", num_results=5):
    query_vector = model.encode(query)
    return vindex.search(
        query_vector,
        filter_dict={"course": course},
        num_results=num_results
    )
```


## Swapping into RAG

Now replace keyword search with vector search in the RAG function:

```python
def rag(query, model="gpt-5.4-mini"):
    search_results = vector_search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(INSTRUCTIONS, prompt, model=model)
    return answer
```

The only change is `search(query)` became `vector_search(query)`. The
prompt building and LLM calling stay the same.

Let's set up the prompt and LLM functions (same as module 1):

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
```


## Testing

Try it:

```python
rag("how do I run kafka?")
```

```python
rag("the course has already started, can I still enroll?")
```

The answers should be similar to what we got with keyword search, but
vector search may handle rephrased questions better.


## Keyword search vs vector search for RAG

With keyword search:

```python
def rag(query, model="gpt-5.4-mini"):
    search_results = keyword_search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(INSTRUCTIONS, prompt, model=model)
    return answer
```

With vector search:

```python
def rag(query, model="gpt-5.4-mini"):
    search_results = vector_search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(INSTRUCTIONS, prompt, model=model)
    return answer
```

Same pipeline, different search. The modular design lets you swap
search methods without touching the rest of the code.

[← Vector Search with MinSearch](03-minsearch-vector.md) | [Vector Search with sqlitesearch →](05-sqlitesearch-vector.md)
