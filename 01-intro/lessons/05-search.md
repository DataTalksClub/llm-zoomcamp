# Search

## Indexing with minsearch

We already have the `documents` list from the previous section. Now
let's index it.

Why do we need search? We have around 1100 documents. We don't want to
send all of them to the LLM - it would be expensive, slow, and the LLM
would get confused with too much data. Instead, we find the most
relevant documents and only send those.

There are many search libraries you can use - Apache Lucene,
Elasticsearch, Solr, and others. But these are somewhat heavy. For
example, to run Elasticsearch, you need to start a Docker container.

[minsearch](https://github.com/alexeygrigorev/minsearch) is a simple
in-memory search engine. It's a toy implementation - not production
ready - but it illustrates how search engines work and it gives good
results.

I implemented this library for the first edition of LLM Zoomcamp. 
Initially it was just a python file that we implemented together as
a part of the [Build a Search Engine](https://www.youtube.com/watch?v=nMrGK5QgPVE) workshop 
(see the [code](https://github.com/alexeygrigorev/build-your-own-search-engine) here).

The concepts in minsearch (text fields, keyword fields, boosting,
filtering) are the same concepts used by Elasticsearch, which in
turn comes from Lucene. So what you learn here transfers directly.

We'll index the `question`, `section`, and `answer` fields as text
(they'll be tokenized and ranked), and the `course` field as a
keyword (for filtering):

What's the difference between text fields and keyword fields?

Text fields are the fields you search through. When you type a query,
the search engine looks at these fields, tokenizes them (splits into
words, lowercases, removes stop words), and ranks the results by
relevance. So `question`, `section`, and `answer` are text fields.

Keyword fields are for exact matching. Think of a SQL query like
`SELECT * FROM index WHERE course = 'data-engineering-zoomcamp'`. No
matter what ranking or boosting you do for text fields, the results
must come from the specified course. You use keyword fields to
restrict the search space to a particular subset. In our case, we have
four courses, and if you're taking the LLM course, you don't want
results from other courses.

This terminology (text fields, keyword fields) comes from
Elasticsearch, which in turn comes from Apache Lucene. What you learn
here with minsearch transfers directly to production search engines.

```python
from minsearch import Index

index = Index(
    text_fields=['question', 'section', 'answer'],
    keyword_fields=['course']
)

index.fit(documents)
```

That's it. The index is built.


## Trying a search

Let's try a search with the question we used before:

```python
question = 'I just discovered the course. Can I join now?'

search_results = index.search(
    question,
    boost_dict={'question': 2.0, 'section': 0.5},
    filter_dict={'course': 'llm-zoomcamp'},
    num_results=5
)

search_results
```

We get back 5 results from the LLM Zoomcamp FAQ. The top result is
the one that matches best - it's the FAQ entry "I just discovered the
course. Can I still join?" which is exactly what we need.

Let's see all the questions:

```python
[doc['question'] for doc in search_results]
```

We see questions about joining the course, registration, certificates,
and more. These are the candidate documents we'll send to the LLM.

We used `boost_dict` to give the `question` field more weight (2.0
instead of the default 1.0) and `section` less weight (0.5). This means
if the query words appear in the question field, that's a stronger
signal than if they appear in the section name.

We used `filter_dict` to only return results from the LLM Zoomcamp
course. Without this filter, we'd get results from all four courses.


## Boosting fields

Not all fields are equally important. The `question` field is usually
more relevant than `section` for matching - if the query words appear
in the question, that's a stronger signal than if they appear in the
section name.

minsearch supports field boosting to reflect this:

```python
results = index.search(
    question,
    num_results=5,
    boost_dict={'question': 2.0, 'section': 0.5}
)
```

All fields have a default boost of 1. Giving `question` a boost of 2
means it counts two times as much. Giving `section` 0.5 means it
counts half as much. This is the same boosting mechanism used by
Elasticsearch and Lucene.

Try different boost values and see how the results change.


## Filtering by course

Sometimes you want to restrict the search to a specific course.
minsearch supports keyword filtering:

```python
results = index.search(
    question,
    num_results=5,
    filter_dict={'course': 'mlops-zoomcamp'}
)
```

This only returns documents from the MLOps Zoomcamp. Try a few
different queries and courses to get a feel for the results.

```python
[doc['question'] for doc in results]
```


## Wrapping it in a function

Let's wrap the search in a `search` function. This is the first
component of our RAG pipeline:

```python
def search(question, course='llm-zoomcamp'):
    boost_dict = {'question': 2.0, 'section': 0.5}
    filter_dict = {'course': course}

    return index.search(
        question,
        boost_dict=boost_dict,
        filter_dict=filter_dict,
        num_results=5
    )
```

By default it searches the LLM Zoomcamp FAQ. You can pass a
different course slug to search other courses:

```python
search_results = search(question)
```

Code: [notebook.ipynb](../code/notebook.ipynb)

[← The Course FAQ Dataset](04-dataset.md) | [Building the Prompt →](06-building-prompt.md)
