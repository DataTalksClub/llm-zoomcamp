# Data Ingestion

So far, our RAG pipeline loads data and builds the search index at
startup. With minsearch, this is fine - our FAQ dataset is small, so
indexing takes less than a second. The entire pipeline runs in one
process.

But what happens when the dataset grows? If you have millions of
documents, or if fetching the data takes time (calling APIs, parsing
files, cleaning text), the startup becomes slow. You don't want to
wait minutes every time your service restarts.

The solution: separate ingestion from querying. One process writes
the data to a persistent search index. Another process reads from it.
The index survives restarts, so you only ingest once.

You can use any persistent search backend for this - Elasticsearch,
OpenSearch, Qdrant, and so on. In this workshop, we'll use
[sqlitesearch](https://github.com/alexeygrigorev/sqlitesearch) - a
lightweight search library backed by SQLite FTS5. It has the same API
as minsearch, so switching is straightforward.

Install it:

```bash
uv add sqlitesearch
```


## The ingestion script

Let's create a separate script that fetches the data and writes it to
a persistent index. This is the ingestion process - it runs once (or
on a schedule when the data changes) and populates the search index.

Create a file called `ingest.py`:

```python
import requests
from sqlitesearch import TextSearchIndex

docs_url = 'https://datatalks.club/faq/json/courses.json'
response = requests.get(docs_url)
courses_raw = response.json()

documents = []
for course in courses_raw:
    course_url = f'https://datatalks.club/faq{course["path"]}'
    course_response = requests.get(course_url)
    course_data = course_response.json()
    for doc in course_data:
        doc['course_name'] = course['course_name']
        documents.append(doc)

print(f"Loaded {len(documents)} documents")

index = TextSearchIndex(
    text_fields=["question", "section", "answer"],
    keyword_fields=["course"],
    id_field="id",
    db_path="faq.db"
)

index.fit(documents)
index.close()

print("Done. Index saved to faq.db")
```

Run it:

```bash
uv run python ingest.py
```

You should see:

```
Loaded 1154 documents
Done. Index saved to faq.db
```

Now there's a `faq.db` file on disk with the entire index. This file
persists across restarts. You can run this script again when the FAQ
data changes - it will rebuild the index.

What happened behind the scenes:

- sqlitesearch created a SQLite database at `faq.db`
- It created a table for the documents and an FTS5 virtual table
  for full-text search
- It inserted all documents and indexed the text fields
- The index is now on disk, ready to be queried by any process


## The query process

Now let's use the index from a separate process. This is the RAG
service - it reads from the index without needing to fetch or process
the raw data.

Open a new notebook (or a new Python file). The only thing we need
is to connect to the existing index:

```python
from sqlitesearch import TextSearchIndex

sqlite_index = TextSearchIndex(
    text_fields=["question", "section", "answer"],
    keyword_fields=["course"],
    id_field="id",
    db_path="faq.db"
)
```

Notice: we don't call `fit`. The index is already populated by the
ingestion script. We just connect to the database file and start
searching.

Let's try a search:

```python
query = "How do I run Docker on Windows?"
results = sqlite_index.search(query, num_results=5)
```

Look at the results:

```python
results[0]
```

Let's see all the questions from the top results:

```python
[doc['question'] for doc in results]
```

The results look similar to what minsearch returned. The ranking may
differ slightly because sqlitesearch uses BM25 while minsearch uses
TF-IDF, but the top results are usually the same.


## Filtering and boosting

Filtering and boosting work the same way as in minsearch:

```python
results = sqlite_index.search(
    query="How do I run Docker on Windows?",
    num_results=5,
    filter_dict={"course": "mlops-zoomcamp"}
)
```

```python
results = sqlite_index.search(
    query="How do I run Docker on Windows?",
    num_results=5,
    boost_dict={"question": 3.0, "section": 0.5}
)
```

Same parameters, same behavior. The only thing that changed is where
the data comes from.


## RAG with sqlitesearch

Now wire it into the RAG pipeline. The prompt and LLM functions are
the same - only the search changes:

```python
def sqlite_search(query, num_results=5):
    boost_dict = {"question": 3.0, "section": 0.5}
    return sqlite_index.search(
        query,
        num_results=num_results,
        boost_dict=boost_dict
    )

def rag_sqlite(query, model="gpt-4o-mini"):
    search_results = sqlite_search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(prompt, model=model)
    return answer
```

Try it:

```python
query = "How do I run Docker on Windows?"
answer = rag_sqlite(query)
print(answer)
```

The answer should be similar to what we got with minsearch. But now
the data comes from a persistent index - no fetching, no processing,
no indexing at startup.


## Comparing the two approaches

With minsearch (single process):

```
Startup: fetch data -> parse -> index -> ready
Every restart: repeat all steps
```

With sqlitesearch (two processes):

```
Ingestion (runs once): fetch data -> parse -> write to faq.db
Query (runs every time): open faq.db -> search -> ready
```

The results may differ slightly because minsearch uses TF-IDF while
sqlitesearch uses BM25. Both are standard text ranking algorithms, but
they weight terms differently.

TF-IDF (Term Frequency - Inverse Document Frequency) rewards terms
that appear often in a document but rarely across all documents.

BM25 is a refinement of TF-IDF that also considers document length.
It tends to handle short and long documents more fairly.

For our FAQ dataset, both produce good results. The difference
matters more at scale with diverse document lengths.


## When to use what

| | minsearch | sqlitesearch |
|---|---|---|
| Architecture | Single process | Ingestion + query |
| Persistence | In-memory only | File-based (SQLite) |
| Startup time | Index every time | Open existing index |
| Scale | Thousands of docs | Millions of docs |
| When to use | Small data, fast startup | Large data, slow ingestion |

The principle: use minsearch when you can load and index the data on
startup without noticeable delay. Switch to a persistent backend when
ingestion takes too long or when you need the index to survive
restarts.

For larger production systems, you'd use the same pattern but with
Elasticsearch, OpenSearch, or a vector database like Qdrant or
Weaviate instead of sqlitesearch. The architecture stays the same:
one process ingests, another queries.


## Cleaning up

When you're done, close the database connection:

```python
sqlite_index.close()
```

Or just let Python clean it up when the notebook kernel shuts down.
