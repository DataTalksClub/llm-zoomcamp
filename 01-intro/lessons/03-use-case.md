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

We'll build that system in this module.

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
    course_url = f'{url_prefix}{course["path"]}'
    course_response = requests.get(course_url)
    course_data = course_response.json()

    for doc in course_data:
        doc['course_name'] = course['course_name']
        documents.append(doc)

len(documents)
```

Each entry has:

- `id` - unique identifier
- `course` - course slug (e.g., `machine-learning-zoomcamp`)
- `section` - which section of the course
- `question` - the FAQ question
- `answer` - the FAQ answer
- `course_name` - human-readable name

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
    'answer': '- Do the tasks locally\n- Publish your code ...',
    'course_name': 'ML Zoomcamp'
}
```

This is our knowledge base. In the next sections, we'll index this
data for search and use it to answer questions with an LLM.

[← Environment](02-environment.md) | [What is RAG →](04-rag.md)
