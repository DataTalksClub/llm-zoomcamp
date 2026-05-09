# The Use Case: Course FAQ

In our community at DataTalks.Club, we run multiple Zoomcamp courses.
For each course, we maintain a FAQ document with common questions and
answers - things that aren't covered in the videos or aren't easy to
find.

The problem: some of these documents have over 300 questions. How do
you find the information you need? It's not trivial. We ask students
to check the FAQ before posting in Slack, but scrolling through
hundreds of entries is tedious.

What we want instead: take all this knowledge, put it in a search
engine, and let students ask questions in natural language. Under the
hood, the system searches the FAQ, retrieves relevant entries, and
gives a specific answer - not a generic one.

We'll build that system in this workshop.


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
schedules. It says "I can help you, but I need to know more details."

This is different from a question like "how do I cook salmon?" - the
LLM knows the answer because cooking salmon is common knowledge. But
our courses are not in the training data.

```python
ask("How do I get a certificate?")
```

Same problem. The LLM doesn't know the specific requirements for our
certificates - that you need to submit a capstone project and
peer-review three other projects.

The issue: the LLM's training data doesn't contain our FAQ. It has
general knowledge about courses and certificates, but not the
specific answers to these specific questions.

The reason we use search (retrieval) is to give the LLM more
information, more context, so it can give the right answer. That's
what RAG does - and we'll build it step by step in the following
sections.


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
