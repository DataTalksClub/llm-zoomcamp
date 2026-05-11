# RAG Helper

In the previous lessons, we built the RAG flow piece by piece:
search, prompt building, and the LLM call. Now we have a working
pipeline. But every time we want to use it, we need to repeat the
same code.

We'll use this code throughout the course, so let's put it into two
reusable files:

- `ingest.py` - loading data and building the search index
- `rag_helper.py` - the RAG logic (search, prompt, LLM)

Then in notebooks, we just import from these files and use them.


## ingest.py

This file handles data loading and index creation - everything we
need before we can search.

Create `ingest.py` with two functions:

```python
import requests
from minsearch import Index


def load_faq_data():
    docs_url = 'https://datatalks.club/faq/json/courses.json'
    response = requests.get(docs_url)
    courses_raw = response.json()

    documents = []
    url_prefix = 'https://datatalks.club/faq'

    for course in courses_raw:
        course_url = f'{url_prefix}{course["path"]}'
        course_response = requests.get(course_url)
        course_response.raise_for_status()
        course_data = course_response.json()

        documents.extend(course_data)

    return documents


def build_index(documents):
    index = Index(
        text_fields=['question', 'section', 'answer'],
        keyword_fields=['course']
    )
    index.fit(documents)
    return index
```

We'll use `load_faq_data()` to fetch the documents and `build_index()`
to create the minsearch index. Later, we'll add sqlitesearch support
to this same file.


## rag_helper.py

This file contains the RAG logic - the same functions we wrote in the
previous lessons, now organized as a class.

Create `rag_helper.py`:

```python
from openai import OpenAI


PROMPT_TEMPLATE = '''
QUESTION: {question}

CONTEXT:
{context}
'''.strip()
```

```python
class RAGBase:

    def __init__(
        self,
        index,
        llm_client,
        instructions,
        course='llm-zoomcamp',
        prompt_template=PROMPT_TEMPLATE,
        model='gpt-5.4-mini'
    ):
        self.index = index
        self.llm_client = llm_client
        self.instructions = instructions
        self.course = course
        self.prompt_template = prompt_template
        self.model = model
```

The `index` parameter is anything with a `search` method - minsearch,
sqlitesearch, or something else. We'll swap it later without changing
any of the RAG code.

The `search` method delegates to the index:

```python
    def search(self, query, num_results=5):
        boost_dict = {'question': 3.0, 'section': 0.5}
        filter_dict = {'course': self.course}

        return self.index.search(
            query,
            num_results=num_results,
            boost_dict=boost_dict,
            filter_dict=filter_dict
        )
```

The `build_context` and `build_prompt` methods format the search
results:

```python
    def build_context(self, search_results):
        lines = []

        for doc in search_results:
            lines.append(doc['section'])
            lines.append('Q: ' + doc['question'])
            lines.append('A: ' + doc['answer'])
            lines.append('')

        return '\n'.join(lines).strip()

    def build_prompt(self, query, search_results):
        context = self.build_context(search_results)
        return self.prompt_template.format(
            question=query, context=context
        )
```

The `llm` method sends the prompt to the LLM:

```python
    def llm(self, prompt):
        input_messages = [
            {'role': 'developer', 'content': self.instructions},
            {'role': 'user', 'content': prompt}
        ]

        response = self.llm_client.responses.create(
            model=self.model,
            input=input_messages
        )

        return response.output_text
```

And the `rag` method wires it all together:

```python
    def rag(self, query):
        search_results = self.search(query)
        prompt = self.build_prompt(query, search_results)
        answer = self.llm(prompt)
        return answer
```


## Using it in a notebook

Now in a notebook, import from both files and put everything together:

```python
from ingest import load_faq_data, build_index
from rag_helper import RAGBase
from openai import OpenAI

documents = load_faq_data()
index = build_index(documents)

instructions = '''
You're a course teaching assistant.
Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.
'''.strip()

assistant = RAGBase(
    index=index,
    llm_client=OpenAI(),
    instructions=instructions,
)

answer = assistant.rag('How do I run Docker on Windows?')
print(answer)
```

Try more questions:

```python
assistant.rag('How do I get a certificate?')
```

```python
assistant.rag('Can I still join the course after it started?')
```

We'll use these two files throughout the course. In the next lesson,
we'll see how to add sqlitesearch support to `ingest.py` for a
persistent search index.

[← The LLM](07-llm.md) | [Data Ingestion →](09-data-ingestion.md)
