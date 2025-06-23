## Homework: Vector Search

In this homework, we will learn more about vector search
and embedding. Like in the module, we will use Qdrant and
fastembed

> It's possible that your answers won't match exactly. If it's the case, select the closest one.

Note: if you want to learn how vector search works under
the hood, check 
[homework 3 from 2024 cohort (questions 1-4)](../../2024/03-vector-search/homework.md)

## Embeddings

Qdrant uses [fastembed](https://github.com/qdrant/fastembed)
under the hood to turn text into vectors. 

We will now explore this library

Make sure it's installed:

```bash
pip install fastembed
```

Import it: 

```python
from fastembed import TextEmbedding
```

## Q1. Embedding the query

Embed the query: `'I just discovered the course. Can I join now?'`.
Use the `'jinaai/jina-embeddings-v2-small-en'` model. 

You should get a numpy array of size 512.

What's the minimal value in this array?

* -0.51
* -0.11
* 0
* 0.51

## Cosine similarity

The vectors that our embedding model returns are already normalized: their length is 1.0.

You can check that by using the `norm` function:

```python
import numpy as np
np.linalg.norm(q)
```

Which means that we can simply compute the dot product between
two vectors to learn the cosine similarity between them.

For example, if you compute the cosine of the query vector with itself, the result will be 1.0:

```python
q.dot(q)
```

## Q2. Cosine similarity with another vector

Now let's embed this document:

```python
doc = 'Can I still join the course after the start date?'
```

What's the cosine similarity between the vector for the query
and the vector for the document?

* 0.3
* 0.5
* 0.7
* 0.9

## Q3. Ranking by cosine

For Q3 and Q4 we will use these documents:

```python
documents = [{'text': "Yes, even if you don't register, you're still eligible to submit the homeworks.\nBe aware, however, that there will be deadlines for turning in the final projects. So don't leave everything for the last minute.",
  'section': 'General course-related questions',
  'question': 'Course - Can I still join the course after the start date?',
  'course': 'data-engineering-zoomcamp'},
 {'text': 'Yes, we will keep all the materials after the course finishes, so you can follow the course at your own pace after it finishes.\nYou can also continue looking at the homeworks and continue preparing for the next cohort. I guess you can also start working on your final capstone project.',
  'section': 'General course-related questions',
  'question': 'Course - Can I follow the course after it finishes?',
  'course': 'data-engineering-zoomcamp'},
 {'text': "The purpose of this document is to capture frequently asked technical questions\nThe exact day and hour of the course will be 15th Jan 2024 at 17h00. The course will start with the first  “Office Hours'' live.1\nSubscribe to course public Google Calendar (it works from Desktop only).\nRegister before the course starts using this link.\nJoin the course Telegram channel with announcements.\nDon’t forget to register in DataTalks.Club's Slack and join the channel.",
  'section': 'General course-related questions',
  'question': 'Course - When will the course start?',
  'course': 'data-engineering-zoomcamp'},
 {'text': 'You can start by installing and setting up all the dependencies and requirements:\nGoogle cloud account\nGoogle Cloud SDK\nPython 3 (installed with Anaconda)\nTerraform\nGit\nLook over the prerequisites and syllabus to see if you are comfortable with these subjects.',
  'section': 'General course-related questions',
  'question': 'Course - What can I do before the course starts?',
  'course': 'data-engineering-zoomcamp'},
 {'text': 'Star the repo! Share it with friends if you find it useful ❣️\nCreate a PR if you see you can improve the text or the structure of the repository.',
  'section': 'General course-related questions',
  'question': 'How can we contribute to the course?',
  'course': 'data-engineering-zoomcamp'}]
```

Compute the embeddings for the text field, and compute the 
cosine between the query vector and all the documents.

What's the document index with the highest similarity? (Indexing starts from 0):

- 0
- 1
- 2
- 3
- 4

Hint: if you put all the embeddings of the text field in one matrix `V` (a single 2-dimensional numpy array), then
computing the cosine becomes a matrix multiplication:

```python
V.dot(q)
```

If this hint is rather confusing you than helping, feel free
to ignore it.

## Q4. Ranking by cosine, version two

Now let's calculate a new field, which is a concatenation of
`question` and `text`:

```python
full_text = doc['question'] + ' ' + doc['text']
``` 

Embed this field and compute the cosine between it and the
query vector. What's the highest scoring document?

- 0
- 1
- 2
- 3
- 4

Is it different from Q3? If yes, why?

## Q5. Selecting the embedding model

Now let's select a smaller embedding model.
What's the smallest dimensionality for models in fastembed?

- 128
- 256
- 384
- 512

One of these models is `BAAI/bge-small-en`. Let's use it.


## Q6. Indexing with qdrant (2 points)

For the last question, we will use more documents.

We will select only FAQ records from our ml zoomcamp:

```python
import requests 

docs_url = 'https://github.com/alexeygrigorev/llm-rag-workshop/raw/main/notebooks/documents.json'
docs_response = requests.get(docs_url)
documents_raw = docs_response.json()


documents = []

for course in documents_raw:
    course_name = course['course']
    if course_name != 'machine-learning-zoomcamp':
        continue

    for doc in course['documents']:
        doc['course'] = course_name
        documents.append(doc)
```

Add them to qdrant using the model form Q5.

When adding the data, use both question and answer fields:

```python
text = doc['question'] + ' ' + doc['text']
```

After the data is inserted, use the question from Q1 for querying the collection.

What's the highest score in the results?
(The score for the first returned record):

- 0.97
- 0.87
- 0.77
- 0.67




## Submit the results

* Submit your results here: https://courses.datatalks.club/llm-zoomcamp-2025/homework/hw2
* It's possible that your answers won't match exactly. If it's the case, select the closest one.
