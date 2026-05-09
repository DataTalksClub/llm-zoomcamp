# The Use Case: Course FAQ

Throughout this workshop, our knowledge base is the
[DataTalks.Club FAQ](https://datatalks.club/faq) - a collection of
questions and answers from our Zoomcamp courses (machine learning,
data engineering, MLOps, LLM).

We'll build a RAG system that can answer questions about these
courses by searching the FAQ and feeding the results to an LLM.


## Why we need RAG for this

Let's first try asking an LLM a course-specific question without any
context:

```python
from openai import OpenAI

openai_client = OpenAI()

def ask(prompt):
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
```

```python
ask("Can I still join the course after it started?")
```

The LLM will give a generic answer - something like "it depends on
the course" or "check the course website". It doesn't know about our
specific Zoomcamp courses, their enrollment policies, or their
schedules.

```python
ask("How do I get a certificate?")
```

Same problem. The LLM doesn't know the specific requirements for our
certificates - that you need to submit a capstone project and
peer-review three other projects.

The issue: the LLM's training data doesn't contain our FAQ. It has
general knowledge about courses and certificates, but not the
specific answers to these specific questions.

We need a way to give the LLM access to our data. That's what RAG
does - and we'll build it step by step in the following sections.


## The FAQ dataset

The FAQ data is available as JSON from the DataTalks.Club website.
Let's look at it.

First, we get the list of courses:

```python
import requests

docs_url = 'https://datatalks.club/faq/json/courses.json'
response = requests.get(docs_url)
courses_raw = response.json()

courses_raw
```

This returns a list of courses. Each course has a `path` field that
points to its FAQ data. For example:

```python
courses_raw[0]
```

The `path` field gives us the URL for that course's FAQ entries.

Let's fetch one course to see the structure:

```python
course = courses_raw[0]
course_url = f'https://datatalks.club/faq{course["path"]}'
course_response = requests.get(course_url)
course_data = course_response.json()

course_data[0]
```

Each entry has:

- `id` - unique identifier
- `course` - course slug (e.g., `machine-learning-zoomcamp`)
- `section` - which section of the course
- `question` - the FAQ question
- `answer` - the FAQ answer

This is our knowledge base. In the next sections, we'll index this
data for search and use it to answer questions with an LLM.
