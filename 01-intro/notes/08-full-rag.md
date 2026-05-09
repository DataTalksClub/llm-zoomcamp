# Full RAG

Now we have all three components: search, prompt, and LLM. Let's wire
them together.


## The RAG function

```python
def rag(query, model="gpt-4o-mini"):
    search_results = search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(prompt, model=model)
    return answer
```

This is the same three-line function we saw in the RAG conceptual
section. Now it's real.

Try it:

```python
query = "How do I run Docker on Windows?"
answer = rag(query)
print(answer)
```

The answer should be based on the FAQ documents - not on the LLM's
general knowledge. The LLM read the search results and generated a
response grounded in our data.


## Try more questions

```python
rag("Can I still join the course after it started?")
```

```python
rag("How do I get a certificate?")
```

```python
rag("What's the best way to store API keys?")
```

Notice how the answers reference specific courses and sections.
That's RAG in action - the LLM is reading from our knowledge base.


## What happens without RAG

For comparison, let's ask the LLM the same question without the
search results:

```python
llm("Can I still join the course after it started?")
```

The answer will be generic - the LLM doesn't know about our specific
courses. With RAG, it answers based on real FAQ data.

This is the core difference: without RAG the LLM relies on its
training data (which doesn't include our courses). With RAG, it
reads from our knowledge base and gives a specific, correct answer.


## The complete pipeline

Let's review the full code we've written:

```python
import requests
from minsearch import Index
from openai import OpenAI

# --- Data ---

docs_url = 'https://datatalks.club/faq/json/courses.json'
response = requests.get(docs_url)
courses_raw = response.json()

documents = []
for course in courses_raw:
    course_url = f'https://datatalks.club/faq{course["path"]}'
    course_response = requests.get(course_url)
    course_data = course_response.json()
    for doc in course_data:
        doc['course_name'] = course['course_name']
        documents.append(doc)

# --- Search ---

index = Index(
    text_fields=["question", "section", "answer"],
    keyword_fields=["course"]
)
index.fit(documents)

def search(query, num_results=5):
    boost_dict = {"question": 3.0, "section": 0.5}
    return index.search(
        query,
        num_results=num_results,
        boost_dict=boost_dict
    )

# --- Prompt ---

PROMPT_TEMPLATE = """
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

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

# --- LLM ---

openai_client = OpenAI()

def llm(prompt, model="gpt-4o-mini"):
    response = openai_client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# --- RAG ---

def rag(query, model="gpt-4o-mini"):
    search_results = search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(prompt, model=model)
    return answer
```

That's a complete RAG system in about 60 lines of Python. No
frameworks, no vector databases, no embedding models. Just search,
prompt, and LLM.

The three components are independent and replaceable:

- Swap `search` for a different backend (Elasticsearch, vector search)
- Swap `build_prompt` for a different prompt template
- Swap `llm` for a different model or provider

Each function is independent. You can plug and play. Later when we
want to replace minsearch with sqlitesearch, all we need to do is
change the `search` function - the rest stays the same.

This modularity is what makes RAG so flexible.
