# Quick RAG Revision

Before we talk about agents, let's set up the RAG pipeline from module
1. We'll use it as the foundation for everything else in this module.

If you completed module 1, this will be a quick recap. If you skipped
it, follow along -- the code is self-contained.


## Loading the data

First, let's fetch the FAQ data. We'll get the list of courses and then
load the FAQ for each one:

```python
import requests

docs_url = 'https://datatalks.club/faq/json/courses.json'
response = requests.get(docs_url)
courses_raw = response.json()

documents = []
url_prefix = 'https://datatalks.club/faq'

for course in courses_raw:
    course_url = f'{url_prefix}{course["path"]}'
    course_response = requests.get(course_url)
    course_data = course_response.json()

    for doc in course_data:
        doc['course_name'] = course['course_name']
        documents.append(doc)
```

Each document has `question`, `section`, `answer`, `course` (the slug),
and `course_name` (the human-readable name). We'll use `course` for
filtering and `answer` for building the context.


## Building the search index

Now let's index the documents with minsearch:

```python
from minsearch import Index

index = Index(
    text_fields=["question", "section", "answer"],
    keyword_fields=["course"]
)

index.fit(documents)
```

We index `question`, `section`, and `answer` as text fields for full-text
search, and `course` as a keyword field for filtering.


## The search function

Let's wrap the search in a function. We'll boost the `question` field
and filter by course:

```python
def search(query):
    boost_dict = {"question": 3.0, "section": 0.5}
    results = index.search(
        query,
        boost_dict=boost_dict,
        filter_dict={"course": "data-engineering-zoomcamp"},
        num_results=5
    )
    return results
```

This searches the Data Engineering Zoomcamp FAQ by default. We can
change the filter later if we need to search a different course.


## The RAG function

Now the LLM part. We'll use the OpenAI Responses API with
`gpt-4o-mini`:

```python
from openai import OpenAI

openai_client = OpenAI()
```

The instructions tell the LLM how to behave:

```python
INSTRUCTIONS = """
You're a course teaching assistant.
Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.
""".strip()
```

The prompt template combines the question with the search results:

```python
PROMPT_TEMPLATE = """
QUESTION: {question}

CONTEXT:
{context}
""".strip()
```

The `build_context` function formats the search results into a string
the LLM can read:

```python
def build_context(search_results):
    context = ""
    for doc in search_results:
        context += f"section: {doc['section']}\n"
        context += f"question: {doc['question']}\n"
        context += f"answer: {doc['answer']}\n"
        context += "\n"
    return context.strip()
```

We combine the context with the question:

```python
def build_prompt(query, search_results):
    context = build_context(search_results)
    return PROMPT_TEMPLATE.format(question=query, context=context)
```

The LLM function sends the instructions and the user prompt to OpenAI:

```python
def llm(instructions, user_prompt, model="gpt-4o-mini"):
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

And the RAG function ties it all together:

```python
def rag(query, model="gpt-4o-mini"):
    search_results = search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(INSTRUCTIONS, prompt, model=model)
    return answer
```


## Testing it

Let's try a question:

```python
rag("How do I run Docker on Windows?")
```

This should work fine. The search finds relevant FAQ entries about
Docker, and the LLM gives a good answer.

Now let's try something slightly different:

```python
rag("How do I run ducker on windows?")
```

The word "ducker" doesn't match "Docker" in our index. The search
returns poor results -- maybe some unrelated documents about other
topics. The LLM gets these bad results and either says "I don't know"
or tries to answer with irrelevant information.

This is the limitation of a fixed pipeline. The search runs once with
the exact query the user typed. There's no second chance. The pipeline
can't adapt -- it doesn't know the search failed, and it can't try
again with a corrected query.

We need something smarter. We need an agent.

---

[<- Previous](01-intro.md) | [Next ->](03-agents-concept.md)
