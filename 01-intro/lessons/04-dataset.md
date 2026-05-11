# The Course FAQ Dataset

Before we build the RAG pipeline, let's get familiar with the data
we'll use as our knowledge base.

The FAQ data is available as JSON from the DataTalks.Club website.
Let's fetch it:

```python
import requests

docs_url = 'https://datatalks.club/faq/json/courses.json'
response = requests.get(docs_url)
courses_raw = response.json()
```

This returns a list of courses. Each course has a `path` field that
points to its FAQ data. Let's fetch all the FAQ documents from all
courses:

```python
documents = []
url_prefix = 'https://datatalks.club/faq'

for course in courses_raw:
    course_url = f'{url_prefix}{course['path']}'

    course_response = requests.get(course_url)
    course_response.raise_for_status()
    course_data = course_response.json()

    documents.extend(course_data)

len(documents)
```

Each entry has:

- `id` - unique identifier
- `course` - course slug (e.g., `machine-learning-zoomcamp`)
- `section` - which section of the course
- `question` - the FAQ question
- `answer` - the FAQ answer

Let's look at one:

```python
documents[0]
```

You should see something like:

```python
{
    'id': '0e38656cfb',
    'course': 'machine-learning-zoomcamp',
    'section': 'General Course-Related Questions',
    'question': 'How do I submit homework?',
    'answer': '- Do the tasks locally\n- Publish your code ...'
}
```

Each course has a slug - a short identifier used in URLs. For example,
`machine-learning-zoomcamp`, `data-engineering-zoomcamp`, etc. We'll
use these slugs for filtering in search.


## How we'll use this data

In the RAG pipeline, this dataset serves as our knowledge base:

1. We index all the documents (the search step)
2. When a student asks a question, we search the index
3. The search returns the most relevant FAQ entries
4. We give those entries to the LLM as context
5. The LLM generates an answer based on the context

The `question` and `answer` fields contain the text we'll search
through. The `course` field lets us filter by course - if a student
is asking about the data engineering course, we don't need results
from the ML course. The `section` field helps with ranking - knowing
which part of the course a question belongs to is useful context.


## A note on data preparation

In our case, the data is already prepared - I maintain this FAQ
website, so I made sure the data is available in a convenient JSON
format. We don't need to do much to prepare it.

In reality, data preparation is often the most time-consuming part of
building a RAG system. You may need to scrape websites, parse PDFs,
clean text, chunk documents, and more. This step is often not visible
but requires considerable effort. In this course we focus on the GenAI
side, but keep in mind that in your projects you will likely spend a
lot of time on data preparation.

In the next section, we'll build the search index.

Code: [notebook.ipynb](../code/notebook.ipynb)

[← What is RAG](03-rag.md) | [Search →](05-search.md)
