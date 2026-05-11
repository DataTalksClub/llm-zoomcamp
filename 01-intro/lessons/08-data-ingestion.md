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
OpenSearch, Qdrant, and so on. In this module, we'll use
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
import time
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
    db_path="faq.db"
)

for doc in documents:
    index.add([doc])
    time.sleep(0.5)

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

We intentionally put a `time.sleep(0.5)` in the loop to simulate adding
records with a delay.

Start the ingestion script:

```bash
uv run python ingest.py
```

While it's running, open a new notebook. Connect to the index:

```python
from sqlitesearch import TextSearchIndex

sqlite_index = TextSearchIndex(
    text_fields=["question", "section", "answer"],
    keyword_fields=["course"],
    db_path="faq.db"
)
```

Check how many documents are in the index:

```python
len(sqlite_index.search("", num_results=10000))
```

Run it a few times - you'll see the number growing as ingestion
progresses.

Try a search:

```python
results = sqlite_index.search("How do I run Docker on Windows?", num_results=5)
[doc['question'] for doc in results]
```

Run this again after a few seconds - the results change as more
documents are ingested.

This is normal database behavior: one process writes, another reads.
With minsearch, this is impossible because the index lives in one
process's memory.

Close the index when done:

```python
sqlite_index.close()
```


## RAG with sqlitesearch

Since ingestion and querying are separate notebooks, the RAG notebook
only needs to open the database and call OpenAI. Connect to the index:

```python
from sqlitesearch import TextSearchIndex

sqlite_index = TextSearchIndex(
    text_fields=["question", "section", "answer"],
    keyword_fields=["course"],
    db_path="faq.db"
)
```

Notice: no `fit` call. The index is already populated by the ingestion
script. We just connect to the database file and start searching.

The search function:

```python
def sqlite_search(query, num_results=5):
    boost_dict = {"question": 3.0, "section": 0.5}
    return sqlite_index.search(
        query,
        num_results=num_results,
        boost_dict=boost_dict
    )
```

And the RAG function (same prompt and LLM as before):

```python
def rag_sqlite(query, model="gpt-5.4-mini"):
    search_results = sqlite_search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(INSTRUCTIONS, prompt, model=model)
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

[← The LLM](07-llm.md) | [Next Steps →](09-next-steps.md)
