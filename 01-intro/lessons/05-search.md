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

What happened: minsearch tokenized each text field (split into words,
lowercased, removed stop words), computed TF-IDF scores, and built
an inverted index. When we search, it ranks documents by how well
their terms match the query.


## Trying a search

Let's try a search:

```python
query = 'How do I run Docker on Windows?'
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
    query='How do I run Docker on Windows?',
    num_results=5,
    filter_dict={'course': 'mlops-zoomcamp'}
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
    query='How do I run Docker on Windows?',
    num_results=5,
    boost_dict={'question': 3.0, 'section': 0.5}
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
def search(query, course='llm-zoomcamp', num_results=5):
    boost_dict = {'question': 3.0, 'section': 0.5}
    return index.search(
        query,
        num_results=num_results,
        boost_dict=boost_dict,
        filter_dict={'course': course}
    )
```

By default it searches the LLM Zoomcamp FAQ. You can pass a
different course slug to search other courses:

```python
search('How do I run Docker?', course='mlops-zoomcamp')
```

[← The Course FAQ Dataset](04-dataset.md) | [Building the Prompt →](06-building-prompt.md)
