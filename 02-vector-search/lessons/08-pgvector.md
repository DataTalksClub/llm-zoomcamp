# Vector Search with PGVector

Video: [Watch this lesson](https://www.youtube.com/watch?v=0P54MFyz-mc&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)

Many real databases can do vector search. Elasticsearch has it, and
there are dedicated stores like Qdrant and Chroma. We'll go with
Postgres. Most of us already run it at work, and the data engineering
course uses it too. The concept is the same as with sqlitesearch, only
the database under the hood changes.

[pgvector](https://github.com/pgvector/pgvector) is the PostgreSQL
extension that makes this work. Install it and Postgres can do vector
similarity search. On top of that you get the usual production features,
like concurrent access, transactions, and large datasets.

We'll run Postgres with pgvector in Docker.

## Starting Postgres with pgvector

Pull the image and start a container:

```bash
docker run -it \
    --name pgvector \
    -e POSTGRES_USER=user \
    -e POSTGRES_PASSWORD=pswd \
    -e POSTGRES_DB=faq \
    -v pgvector_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    pgvector/pgvector:pg17
```

This image has the pgvector extension pre-installed. The `-v` flag
creates a named volume so data persists across container restarts.

## Installing the Python client

Install the driver:

```bash
uv add psycopg[binary]
```

Note: if using Zshell use `uv add 'psycopg[binary]'`

We'll use `psycopg` (v3) to connect and run queries. Note: this is
different from `psycopg2` - psycopg v3 supports `conn.execute()`
directly without creating a cursor.

## Preparing the data

We need the FAQ documents and their embeddings.

Here's what we did in previous units as one script:

```python
from tqdm.auto import tqdm

from ingest import load_faq_data
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = load_faq_data()
texts = [doc["question"] + " " + doc["answer"] for doc in documents]

batch_size = 50
vectors = []

for i in tqdm(range(0, len(texts), batch_size)):
    batch = texts[i:i + batch_size]
    batch_vectors = model.encode(batch)
    vectors.extend(batch_vectors)
```


Now we connect to Postgres:

```python
import psycopg

conn = psycopg.connect(
    "postgresql://user:pswd@localhost:5432/faq"
)
conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
```

The second line activates pgvector. The Docker image we started isn't
plain Postgres, it ships the extension inside, and this turns it on. It
adds the `vector` column type and the similarity search operators.

## Creating a table

Create a table for storing documents with their embeddings:

```python
conn.execute("""
    DROP TABLE IF EXISTS documents
""")

conn.execute("""
    CREATE TABLE documents (
        id SERIAL PRIMARY KEY,
        course TEXT,
        section TEXT,
        question TEXT,
        answer TEXT,
        embedding vector(384)
    )
""")
```

The `vector(384)` column stores our 384-dimensional embeddings from
`all-MiniLM-L6-v2`.

## Inserting documents with embeddings

Let's insert the documents and their vectors into PGVector:

```python
def vec_to_str(vector):
    return "[" + ",".join(str(x) for x in vector) + "]"

for doc, vec in tqdm(zip(documents, vectors), total=len(documents)):
    conn.execute(
        """
        INSERT INTO documents (course, section, question, answer, embedding)
        VALUES (%s, %s, %s, %s, %s::vector)
        """,
        (doc["course"], doc["section"], doc["question"], doc["answer"],
         vec_to_str(vec))
    )

conn.commit()
```

We loop over the documents and insert each one with its embedding. We
hand Postgres the vector as text, so the `::vector` cast tells it to
parse that string back into a vector. We call `conn.commit()` to persist
the changes.

## Searching with cosine similarity

Search with a query:

```python
query = "I just discovered the course. Can I still join it?"
query_vector = model.encode(query)
query_str = vec_to_str(query_vector)
```

Search for the most similar documents:

```python
results = conn.execute(
    """
    SELECT course, question, answer,
           1 - (embedding <=> %s::vector) AS similarity
    FROM documents
    ORDER BY embedding <=> %s::vector
    LIMIT 5
    """,
    (query_str, query_str)
).fetchall()

for row in results:
    print(f"[{row[0]}] {row[1]} (similarity: {row[3]:.4f})")
```

The `<=>` operator computes cosine distance (1 - cosine similarity).
We order by ascending distance, so the closest vectors come first.

## Filtering by course

Because this is plain SQL, filtering by course is one extra `WHERE`
clause:

```python
results = conn.execute(
    """
    SELECT course, question, answer,
           1 - (embedding <=> %s::vector) AS similarity
    FROM documents
    WHERE course = %s
    ORDER BY embedding <=> %s::vector
    LIMIT 5
    """,
    (query_str, "llm-zoomcamp", query_str)
).fetchall()
```

## Creating an index for faster search

So far this runs brute-force search, comparing our query against every
row. For our small dataset that's fine.

For a larger one, create an HNSW index to switch to approximate search:

```python
conn.execute("""
    CREATE INDEX ON documents
    USING hnsw (embedding vector_cosine_ops)
""")
```

This builds an HNSW (Hierarchical Navigable Small World) index, the
same state-of-the-art algorithm dedicated vector databases use. It makes
search faster, at the cost of a small accuracy trade-off.

## Wrapping it in a function

Let's wrap the search logic in a reusable function:

```python
def pgvector_search(query, course="llm-zoomcamp", num_results=5):
    query_vector = model.encode(query)
    query_str = vec_to_str(query_vector)
    rows = conn.execute(
        """
        SELECT course, section, question, answer
        FROM documents
        WHERE course = %s
        ORDER BY embedding <=> %s::vector
        LIMIT %s
        """,
        (course, query_str, num_results)
    ).fetchall()

    return [
        {"course": r[0], "section": r[1], "question": r[2], "answer": r[3]}
        for r in rows
    ]
```

Try it:

```python
results = pgvector_search("How do I join the course?")
```

## Using it in RAG

We take the same `search` function from above and move it into a class.
We pass the Postgres connection instead of an index. We set `index=None`
because `RAGBase` expects an index and would complain otherwise.

The class overrides `search` to query PGVector:

```python
from rag_helper import RAGBase

class RAGPgVector(RAGBase):

    def __init__(self, embedder, conn, **kwargs):
        super().__init__(index=None, **kwargs)
        self.embedder = embedder
        self.conn = conn

    def search(self, query, num_results=5):
        query_vector = self.embedder.encode(query)
        query_str = vec_to_str(query_vector)

        rows = self.conn.execute(
            """
            SELECT course, section, question, answer
            FROM documents
            WHERE course = %s
            ORDER BY embedding <=> %s::vector
            LIMIT %s
            """,
            (self.course, query_str, num_results)
        ).fetchall()

        return [
            {"course": r[0], "section": r[1], "question": r[2], "answer": r[3]}
            for r in rows
        ]
```

Initialize OpenAI client:

```python
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
openai_client = OpenAI()
```

Create the vector assistant:

```python
vector_assistant = RAGPgVector(
    embedder=model,
    conn=conn,
    llm_client=openai_client,
)
```

Try it:

```python
vector_assistant.rag("the program has already begun, can I still sign up?")
```

## Using PGVector

Here's how PGVector compares with the two tools we used earlier:

- minsearch: no setup, in-memory, best for notebooks and experiments
- sqlitesearch: no setup, SQLite file persistence, best for pet projects
- PGVector: requires Docker, Postgres database with concurrent access,
  handles millions of records, best for production systems

Reach for PGVector when you need production features:

- concurrent reads and writes
- transactions
- integration with an existing Postgres-based application

[← Vector Search with sqlitesearch](07-sqlitesearch-vector.md) | [Using ONNX Runtime →](09-onnx-embedder.md)
