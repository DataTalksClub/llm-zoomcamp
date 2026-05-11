# RAG Helper

In the previous lessons, we built the RAG flow piece by piece:
search, prompt building, and the LLM call. Now we have a working
pipeline. But every time we want to use it, we need to repeat the
same code.

Let's put it all into a reusable class so we don't have to repeat
ourselves.


## Loading the data

First, a function to load the FAQ documents:

```python
import requests

def load_faq_data():
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

    return documents
```

We used this same code in lesson 03 to explore the data, and again
in lesson 08 for the ingestion script. Now it lives in one place.


## The RAGBase class

Here's the class that combines search, prompt building, and the LLM:

```python
from minsearch import Index
from openai import OpenAI

class RAGBase:

    def __init__(self, index, llm_client, instructions, model="gpt-5.4-mini"):
        self.index = index
        self.llm_client = llm_client
        self.instructions = instructions
        self.model = model

    def search(self, query, num_results=5, boost_dict=None, filter_dict=None):
        return self.index.search(
            query,
            num_results=num_results,
            boost_dict=boost_dict or {},
            filter_dict=filter_dict or {}
        )

    def build_prompt(self, query, search_results):
        context = ""

        for doc in search_results:
            context += f"section: {doc['section']}\n"
            context += f"question: {doc['question']}\n"
            context += f"answer: {doc['answer']}\n"
            context += "\n"

        context = context.strip()

        prompt = f"""
QUESTION: {query}

CONTEXT:
{context}
""".strip()

        return prompt

    def llm(self, prompt):
        input_messages = [
            {"role": "developer", "content": self.instructions},
            {"role": "user", "content": prompt}
        ]

        response = self.llm_client.responses.create(
            model=self.model,
            input=input_messages
        )

        return response.output_text

    def rag(self, query, **search_kwargs):
        search_results = self.search(query, **search_kwargs)
        prompt = self.build_prompt(query, search_results)
        answer = self.llm(prompt)
        return answer
```

The class takes:
- `index` - any search index (minsearch, sqlitesearch, or something else)
- `llm_client` - the OpenAI client
- `instructions` - the system prompt for the LLM
- `model` - the model to use (default: gpt-5.4-mini)


## Using RAGBase

Create an instance and use it:

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

answer = rag.rag("How do I run Docker on Windows?")
print(answer)
```

Filter by course:

```python
rag.rag(
    "How do I run Docker on Windows?",
    filter_dict={"course": "mlops-zoomcamp"}
)
```


## Swapping the search backend

The `index` parameter is just something with a `search` method. You
can swap it without changing any of the RAG code. For example,
when we switch to sqlitesearch in the next lesson:

```python
from sqlitesearch import TextSearchIndex

sqlite_index = TextSearchIndex(
    text_fields=["question", "section", "answer"],
    keyword_fields=["course"],
    db_path="faq.db"
)

rag = RAGBase(
    index=sqlite_index,
    llm_client=openai_client,
    instructions=instructions,
)

rag.rag("How do I run Docker on Windows?")
```

Same RAG code, different search backend. This is the power of
keeping search, prompt building, and the LLM in one reusable
class.


## Save it as rag_helper.py

Create a file called `rag_helper.py` in your project folder with
the `load_faq_data` function and the `RAGBase` class. Then import
it in any notebook:

```python
from rag_helper import RAGBase, load_faq_data
```

We'll use this across all modules in the course.

[← The LLM](07-llm.md) | [Data Ingestion →](09-data-ingestion.md)
