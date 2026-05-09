# Search

## Fetching the data

Our FAQ data lives at a public URL. Let's fetch it.

First, we get the list of courses:

```python
import requests

docs_url = 'https://datatalks.club/faq/json/courses.json'
response = requests.get(docs_url)
courses_raw = response.json()

courses_raw[:3]
```

This returns a list of courses. Each course has a `path` field that
points to its FAQ JSON. For example:

```python
courses_raw[0]
```

The `path` field gives us the URL for that course's FAQ data.

Now let's fetch all the FAQ documents from all courses:

```python
documents = []

for course in courses_raw:
    course_url = f'https://datatalks.club/faq{course["path"]}'
    course_response = requests.get(course_url)
    course_data = course_response.json()

    for doc in course_data:
        doc['course_name'] = course['course_name']
        documents.append(doc)

len(documents)
```

Each document has these fields:

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

You should see a document with a question, an answer, a section,
and a course. This is one row in our knowledge base.


## Understanding the data

Let's check how many documents we have per course:

```python
from collections import Counter

course_counts = Counter(doc['course'] for doc in documents)
course_counts
```

And which sections exist:

```python
sections = set(doc['section'] for doc in documents)
len(sections)
```

Understanding the data helps us design better search. For example,
if we know the most common sections, we can decide whether to filter
by section or course.


## Indexing with minsearch

[minsearch](https://github.com/alexeygrigorev/minsearch) is a simple
in-memory search engine. It's a toy implementation - not production
ready - but it illustrates how search engines work and it gives good
results. We'll start with it and later replace it with sqlitesearch
for a persistent backend.

The concepts in minsearch (text fields, keyword fields, boosting,
filtering) are the same concepts used by Elasticsearch, which in
turn comes from Lucene. So what you learn here transfers directly.

We'll index the `question`, `section`, and `answer` fields as text
(they'll be tokenized and ranked), and the `course` field as a
keyword (for filtering):

```python
from minsearch import Index

index = Index(
    text_fields=["question", "section", "answer"],
    keyword_fields=["course"]
)

index.fit(documents)
```

That's it. The index is built.

What happened: minsearch tokenized each text field (split into words,
lowercased, removed stop words), computed TF-IDF scores, and built
an inverted index. When we search, it ranks documents by how well
their terms match the query.


## Trying a search

Let's try a search:

```python
query = "How do I run Docker on Windows?"
results = index.search(query, num_results=5)
```

Look at the results:

```python
results[0]
```

Each result is a document from our dataset, ranked by relevance to
the query. The top result should contain an answer about running
Docker on Windows.

Let's see all the questions from the top results:

```python
[doc['question'] for doc in results]
```


## Filtering by course

Sometimes you want to restrict the search to a specific course.
minsearch supports keyword filtering:

```python
results = index.search(
    query="How do I run Docker on Windows?",
    num_results=5,
    filter_dict={"course": "mlops-zoomcamp"}
)
```

This only returns documents from the MLOps Zoomcamp. Try a few
different queries and courses to get a feel for the results.

```python
[doc['question'] for doc in results]
```


## Boosting fields

Not all fields are equally important. The `question` field is usually
more relevant than `section` for matching - if the query words appear
in the question, that's a stronger signal than if they appear in the
section name.

minsearch supports field boosting to reflect this:

```python
results = index.search(
    query="How do I run Docker on Windows?",
    num_results=5,
    boost_dict={"question": 3.0, "section": 0.5}
)
```

All fields have a default boost of 1. Giving `question` a boost of 3
means it counts three times as much. Giving `section` 0.5 means it
counts half as much. This is the same boosting mechanism used by
Elasticsearch and Lucene.

Try different boost values and see how the results change.


## Wrapping it in a function

Let's wrap the search in a `search` function. This is the first
component of our RAG pipeline:

```python
def search(query, num_results=5):
    boost_dict = {"question": 3.0, "section": 0.5}
    return index.search(
        query,
        num_results=num_results,
        boost_dict=boost_dict
    )
```

Now `search("How do I sign up?")` returns the most relevant FAQ
entries. We'll use this when we wire everything together.
