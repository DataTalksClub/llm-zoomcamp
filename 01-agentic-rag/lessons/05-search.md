# Search

Video: [Watch this lesson](https://www.youtube.com/watch?v=GYgpNKiuCJU&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

## Search basics

At its core, every search engine does the same thing. It takes a query,
scores every document for similarity, and returns the top results.

Formally, there is a similarity function:

```python
score = sim(query, document)
```

For each document in the database, you compute this score. Then you
rank all documents by score and return the top N. What makes a search
engine different from another search engine is what `sim` actually
computes.

- text/lexical search (covered in this section): `sim` counts how
  many words the query and the document share. It looks at the surface
  form, the actual words, and matches them exactly.

- vector/semantic search (covered in [module 2](../../02-vector-search/)):
  `sim` compares the meaning of the query and the document. Same
  function, different similarity measure.

Consider these two questions:

- "Can I still join the course after the start date?"
- "Is it possible to enroll late?"

They mean the same thing, but share almost no keywords. "Join" is not
"enroll", "course" is absent, "start date" is not "late". A text search
engine would struggle to match them, because it only sees words.

We'll see how vector search solves this later. For now, let's build text
search with minsearch.

## Indexing with minsearch

We already have the `documents` list from the previous section. Now
let's index it.

Searching matters because we have around 1100 documents. Sending all
of them to the LLM would be expensive and slow. The model would get
confused with too much data. Search finds the most relevant documents
to send instead.

There are many search libraries you can use - Apache Lucene,
Elasticsearch, Solr, and others. But these are somewhat heavy. For
example, to run Elasticsearch, you need to start a Docker container.

[minsearch](https://github.com/alexeygrigorev/minsearch) is a simple
in-memory search engine. It's lightweight, so it runs anywhere Python
runs, including Google Colab where you can't start a Docker container.
It's a toy implementation, not production ready, but it illustrates how
search engines work and it gives good results.

I should add a disclaimer: I wrote this library and I maintain it. It
started as a single Python file in the first edition of LLM Zoomcamp. I
wanted to show that keyword search isn't magic. We wrote it together as
part of the [Build a Search Engine](https://www.youtube.com/watch?v=nMrGK5QgPVE) workshop
(see the [code](https://github.com/alexeygrigorev/build-your-own-search-engine)).

It turned out useful beyond teaching. After two years across many
projects, it's pretty reliable for small datasets.

The concepts in minsearch are the same as in Elasticsearch (which
comes from Lucene): text fields, keyword fields, boosting, filtering. I
borrowed those terms from Elasticsearch on purpose, since I wanted a
lightweight stand-in for it. So what you learn here transfers directly.

We'll index the `question`, `section`, and `answer` fields as text
(they'll be tokenized and ranked), and the `course` field as a
keyword (for filtering).

The index tokenizes text fields and treats keyword fields as exact strings.

Text fields are the fields you search through. When you type a query,
the search engine looks at these fields and tokenizes them. It splits
text into words, lowercases them, removes stop words, and ranks the
results by relevance. So `question`, `section`, and `answer` are text
fields.

Keyword fields are for exact matching. Think of a SQL query like
`SELECT * FROM index WHERE course = 'data-engineering-zoomcamp'`. The
results must come from the specified course, no matter what ranking or
boosting you do for text fields.

You use keyword fields to restrict the search space to a particular
subset. In our case, we have four courses. Say you're taking the LLM
course and ask a question. You don't want answers from the MLOps or
machine learning courses mixed in.

```python
from minsearch import Index

index = Index(
    text_fields=["question", "section", "answer"],
    keyword_fields=["course"]
)

index.fit(documents)
```

That's it, the index is built. The `fit` name comes from scikit-learn,
where you fit a model on data. Here we fit an index on our documents.

## Trying a search

Let's try a search with the question we used before:

```python
question = "I just discovered the course. Can I join now?"

search_results = index.search(
    question,
    boost_dict={"question": 2.0, "section": 0.5},
    filter_dict={"course": "llm-zoomcamp"},
    num_results=5
)

search_results
```

We get back 5 results from the LLM Zoomcamp FAQ. The best match is the FAQ
entry "I just discovered the course. Can I still join?" which is exactly what
we need.

Here are all the questions:

```python
[doc["question"] for doc in search_results]
```

We see questions about joining the course, registration, certificates,
and more. These are the candidate documents we'll send to the LLM.

We used `boost_dict` to give the `question` field more weight (2.0
instead of the default 1.0) and `section` less weight (0.5). Query
words appearing in the question field is a stronger signal than them
appearing in the section name.

We used `filter_dict` to only return results from the LLM Zoomcamp
course. Without this filter, we'd get results from all four courses.

## Boosting fields

Not all fields are equally important. The `question` field is usually
more relevant than `section` for matching. Query words appearing in the
question is a stronger signal than them appearing in the section name.

minsearch supports field boosting to reflect this:

```python
results = index.search(
    question,
    num_results=5,
    boost_dict={"question": 2.0, "section": 0.5}
)
```

All fields have a default boost of 1. Giving `question` a boost of 2
means it counts two times as much. Take a question about certificates.
The word "certificate" in the question field now weighs twice what it
does in the answer.

Giving `section` 0.5 means it counts half as much, since a match there
tells us less. This is the same boosting mechanism used by
Elasticsearch and Lucene.

Try different boost values and see how the results change.

## Filtering by course

Sometimes you want to restrict the search to a specific course.

minsearch supports keyword filtering:

```python
results = index.search(
    question,
    num_results=5,
    filter_dict={"course": "mlops-zoomcamp"}
)
```

This only returns documents from the MLOps Zoomcamp. Try a few
different queries and courses to get a feel for the results.

```python
[doc["question"] for doc in results]
```

## Wrapping it in a function

Let's wrap the search in a `search` function - the first component of
our RAG pipeline:

```python
def search(question, course="llm-zoomcamp"):
    boost_dict = {"question": 2.0, "section": 0.5}
    filter_dict = {"course": course}

    return index.search(
        question,
        boost_dict=boost_dict,
        filter_dict=filter_dict,
        num_results=5
    )
```

By default it searches the LLM Zoomcamp FAQ.

You can pass a
different course slug to search other courses:

```python
search_results = search(question)
```

Code: [notebook.ipynb](../code/notebook.ipynb)

[← The Course FAQ Dataset](04-dataset.md) | [Building the Prompt →](06-building-prompt.md)
