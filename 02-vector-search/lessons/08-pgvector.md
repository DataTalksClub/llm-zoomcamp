# Vector Search with PGVector

[pgvector](https://github.com/pgvector/pgvector) is a PostgreSQL
extension that adds vector similarity search to PostgreSQL. It's a
good choice when you already use Postgres in your stack or when you
need a production-grade solution that handles concurrent access,
transactions, and large datasets.

We'll run PostgreSQL with pgvector in Docker.


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
uv add psycopg2-binary
```

We'll use `psycopg2` to connect and run queries.

Let's connect to it:

```python
import psycopg

conn = psycopg.connect(
    'postgresql://user:pswd@localhost:5432/faq'
)
conn.execute("CREATE EXTENSION IF NOT EXISTS vector")
```

The `vector` extension adds the `vector` column type and similarity
search operators.


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

We already have `documents` and `vectors` from the previous sections.
Let's insert them into PGVector:

```python
def vec_to_str(vector):
    return '[' + ','.join(str(x) for x in vector) + ']'

for doc, vec in zip(documents, vectors):
    conn.execute(
        """
        INSERT INTO documents (course, section, question, answer, embedding)
        VALUES (%s, %s, %s, %s, %s::vector)
        """,
        (doc['course'], doc['section'], doc['question'], doc['answer'],
         vec_to_str(vec))
    )

conn.commit()
```

This inserts each document along with its embedding vector. The `::vector`
cast tells PostgreSQL to parse the string as a vector. We call
`conn.commit()` to persist the changes.


## Searching with cosine similarity

Search with a query:

```python
query = 'I just discovered the course. Can I still join it?'
query_vector = model.encode(query)
query_str = vec_to_str(query_vector)

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
    print(f'[{row[0]}] {row[1]} (similarity: {row[3]:.4f})')
```

The `<=>` operator computes cosine distance (1 - cosine similarity).
We order by ascending distance, so the closest vectors come first.


## Filtering by course

Add a `WHERE` clause:

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
    (query_str, 'data-engineering-zoomcamp', query_str)
).fetchall()
```


## Creating an index for faster search

For small datasets, exact search is fine. For larger datasets, create
an HNSW index for approximate nearest neighbor search:

```python
conn.execute("""
    CREATE INDEX ON documents
    USING hnsw (embedding vector_cosine_ops)
""")
```

This builds an HNSW (Hierarchical Navigable Small World) index, the
same algorithm used by dedicated vector databases. It makes search
faster at the cost of a small accuracy trade-off.


## Wrapping it in a function

Let's wrap the search logic in a reusable function:

```python
def pgvector_search(query, course='data-engineering-zoomcamp', num_results=5):
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
        {'course': r[0], 'section': r[1], 'question': r[2], 'answer': r[3]}
        for r in rows
    ]
```

Try it:

```python
results = pgvector_search('How do I run Kafka?')
```


## Using PGVector

| | minsearch | sqlitesearch | PGVector |
|---|---|---|---|
| Setup | None | None | Docker container |
| Persistence | In-memory | SQLite file | Postgres database |
| Concurrent access | No | Limited | Yes |
| Scale | Thousands | Hundreds of thousands | Millions |
| Best for | Notebooks, experiments | Pet projects | Production systems |

PGVector is the right choice when you need production features:
concurrent reads and writes, transactions, or integration with an
existing Postgres-based application.

[← Vector Search with sqlitesearch](07-sqlitesearch-vector.md) | [Text Search vs Vector Search →](09-text-vs-vector.md)
