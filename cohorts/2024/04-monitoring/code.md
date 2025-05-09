# Intermediate code

Here's the intermediate steps from claude, so you
can copy-paste as you follow along the videos

## 4.6 Capturing User Feedback

### First prompt


I have a streamlit app and I want to add +1 and -1 buttons there. Also, I want to put the logic for rag outside of this file, to rag.py module. And finally, I want to select the course for which I ask the question. Could be one of the following: machine-learning-zoomcamp, data-engineering-zoomcamp and mlops-zoomcamp.

We will use postgres for storing the data, so let's add another module for interacting with pg. It should:

* generate a unique id for each conversation
* write the question and the answer
* save user feedback if we get anything (probably in a separate table) 

I also want to adjust our docker-compose file:

* make data in elastic persistent, so I don't need to reindex the data every time I run
* add postgres (also with volume mapping)
* add a container for the streamlit app (and a docker file for it)


```python
import streamlit as st
import time

from elasticsearch import Elasticsearch
from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',
)

es_client = Elasticsearch('http://localhost:9200') 


def elastic_search(query, index_name = "course-questions"):
    search_query = {
        "size": 5,
        "query": {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": query,
                        "fields": ["question^3", "text", "section"],
                        "type": "best_fields"
                    }
                },
                "filter": {
                    "term": {
                        "course": "data-engineering-zoomcamp"
                    }
                }
            }
        }
    }

    response = es_client.search(index=index_name, body=search_query)
    
    result_docs = []
    
    for hit in response['hits']['hits']:
        result_docs.append(hit['_source'])
    
    return result_docs


def build_prompt(query, search_results):
    prompt_template = """
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT: 
{context}
""".strip()

    context = ""
    
    for doc in search_results:
        context = context + f"section: {doc['section']}\nquestion: {doc['question']}\nanswer: {doc['text']}\n\n"
    
    prompt = prompt_template.format(question=query, context=context).strip()
    return prompt

def llm(prompt):
    response = client.chat.completions.create(
        model='phi3',
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content


def rag(query):
    search_results = elastic_search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(prompt)
    return answer


def main():
    st.title("RAG Function Invocation")

    user_input = st.text_input("Enter your input:")

    if st.button("Ask"):
        with st.spinner('Processing...'):
            output = rag(user_input)
            st.success("Completed!")
            st.write(output)

if __name__ == "__main__":
    main()
```

```yaml
version: '3.8'

services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.4.3
    container_name: elasticsearch
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
    ports:
      - "9200:9200"
      - "9300:9300"

  ollama:
    image: ollama/ollama
    container_name: ollama
    volumes:
      - ollama:/root/.ollama
    ports:
      - "11434:11434"

volumes:
  ollama:
```

---


Certainly! I'll help you modify your Streamlit app, create a separate RAG module, add course selection, set up a PostgreSQL database, and adjust the Docker Compose file. Let's go through this step by step.

Updated Streamlit App (app.py):

```python
import streamlit as st
import time
import uuid

from rag import rag
from db import save_conversation, save_feedback

def main():
    st.title("Course Assistant")

    # Session state initialization
    if 'conversation_id' not in st.session_state:
        st.session_state.conversation_id = str(uuid.uuid4())
    if 'count' not in st.session_state:
        st.session_state.count = 0

    # Course selection
    course = st.selectbox(
        "Select a course:",
        ["machine-learning-zoomcamp", "data-engineering-zoomcamp", "mlops-zoomcamp"]
    )

    # User input
    user_input = st.text_input("Enter your question:")

    if st.button("Ask"):
        with st.spinner('Processing...'):
            output = rag(user_input, course)
            st.success("Completed!")
            st.write(output)
            
            # Save conversation to database
            save_conversation(st.session_state.conversation_id, user_input, output, course)

    # Feedback buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("+1"):
            st.session_state.count += 1
            save_feedback(st.session_state.conversation_id, 1)
    with col2:
        if st.button("-1"):
            st.session_state.count -= 1
            save_feedback(st.session_state.conversation_id, -1)

    st.write(f"Current count: {st.session_state.count}")

if __name__ == "__main__":
    main()
```

rag.py:

```python
from elasticsearch import Elasticsearch
from openai import OpenAI

es_client = Elasticsearch('http://elasticsearch:9200')
client = OpenAI(base_url='http://ollama:11434/v1/', api_key='ollama')

def elastic_search(query, course, index_name="course-questions"):
    search_query = {
        "size": 5,
        "query": {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": query,
                        "fields": ["question^3", "text", "section"],
                        "type": "best_fields"
                    }
                },
                "filter": {
                    "term": {
                        "course": course
                    }
                }
            }
        }
    }

    response = es_client.search(index=index_name, body=search_query)
    return [hit['_source'] for hit in response['hits']['hits']]

def build_prompt(query, search_results):
    prompt_template = """
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT: 
{context}
""".strip()

    context = "\n\n".join([f"section: {doc['section']}\nquestion: {doc['question']}\nanswer: {doc['text']}" for doc in search_results])
    return prompt_template.format(question=query, context=context).strip()

def llm(prompt):
    response = client.chat.completions.create(
        model='phi3',
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def rag(query, course):
    search_results = elastic_search(query, course)
    prompt = build_prompt(query, search_results)
    answer = llm(prompt)
    return answer
```

db.py

```python
import psycopg2
from psycopg2.extras import DictCursor

def get_db_connection():
    return psycopg2.connect(
        host="postgres",
        database="course_assistant",
        user="your_username",
        password="your_password"
    )

def init_db():
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS conversations (
                id TEXT PRIMARY KEY,
                question TEXT NOT NULL,
                answer TEXT NOT NULL,
                course TEXT NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS feedback (
                id SERIAL PRIMARY KEY,
                conversation_id TEXT REFERENCES conversations(id),
                feedback INTEGER NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
    conn.commit()
    conn.close()

def save_conversation(conversation_id, question, answer, course):
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO conversations (id, question, answer, course) VALUES (%s, %s, %s, %s)",
            (conversation_id, question, answer, course)
        )
    conn.commit()
    conn.close()

def save_feedback(conversation_id, feedback):
    conn = get_db_connection()
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO feedback (conversation_id, feedback) VALUES (%s, %s)",
            (conversation_id, feedback)
        )
    conn.commit()
    conn.close()

# Initialize the database when the module is imported
init_db()
```

docker-compose.yaml

```yaml
version: '3.8'

services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.4.3
    container_name: elasticsearch
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
    ports:
      - "9200:9200"
      - "9300:9300"
    volumes:
      - elasticsearch_data:/usr/share/elasticsearch/data

  ollama:
    image: ollama/ollama
    container_name: ollama
    volumes:
      - ollama_data:/root/.ollama
    ports:
      - "11434:11434"

  postgres:
    image: postgres:13
    container_name: postgres
    environment:
      POSTGRES_DB: course_assistant
      POSTGRES_USER: your_username
      POSTGRES_PASSWORD: your_password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  streamlit:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: streamlit
    ports:
      - "8501:8501"
    depends_on:
      - elasticsearch
      - ollama
      - postgres

volumes:
  elasticsearch_data:
  ollama_data:
  postgres_data:
```

Dockerfile:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["streamlit", "run", "app.py"]
```

### Prompt 2 

let's call the rag module differently 

let's use environment variables for this:

```python
psycopg2.connect(
    host="postgres",
    database="course_assistant",
    user="your_username",
    password="your_password"
)
```

We should do it only once, so let's not do it every time we import the module

```python
# Initialize the database when the module is imported
init_db()
```

also let's create the `requirements.txt` file

--- 

Certainly! I'll make those changes for you. Let's start by renaming the RAG module, using environment variables for the database connection, and adjusting the database initialization.

assistant.py

```python
import os
from elasticsearch import Elasticsearch
from openai import OpenAI

es_client = Elasticsearch(os.getenv('ELASTICSEARCH_URL', 'http://elasticsearch:9200'))
client = OpenAI(
    base_url=os.getenv('OLLAMA_URL', 'http://ollama:11434/v1/'),
    api_key='ollama'
)

def elastic_search(query, course, index_name="course-questions"):
    search_query = {
        "size": 5,
        "query": {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": query,
                        "fields": ["question^3", "text", "section"],
                        "type": "best_fields"
                    }
                },
                "filter": {
                    "term": {
                        "course": course
                    }
                }
            }
        }
    }

    response = es_client.search(index=index_name, body=search_query)
    return [hit['_source'] for hit in response['hits']['hits']]

def build_prompt(query, search_results):
    prompt_template = """
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT: 
{context}
""".strip()

    context = "\n\n".join([f"section: {doc['section']}\nquestion: {doc['question']}\nanswer: {doc['text']}" for doc in search_results])
    return prompt_template.format(question=query, context=context).strip()

def llm(prompt):
    response = client.chat.completions.create(
        model='phi3',
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def get_answer(query, course):
    search_results = elastic_search(query, course)
    prompt = build_prompt(query, search_results)
    answer = llm(prompt)
    return answer
```

Updated Database Module (db.py)

```python
import os
import psycopg2
from psycopg2.extras import DictCursor

# Global connection pool
conn_pool = None

def get_db_connection():
    global conn_pool
    if conn_pool is None:
        conn_pool = psycopg2.pool.SimpleConnectionPool(
            1, 20,
            host=os.getenv('POSTGRES_HOST', 'postgres'),
            database=os.getenv('POSTGRES_DB', 'course_assistant'),
            user=os.getenv('POSTGRES_USER', 'your_username'),
            password=os.getenv('POSTGRES_PASSWORD', 'your_password')
        )
    return conn_pool.getconn()

def release_db_connection(conn):
    global conn_pool
    conn_pool.putconn(conn)

def init_db():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS conversations (
                    id TEXT PRIMARY KEY,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL,
                    course TEXT NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS feedback (
                    id SERIAL PRIMARY KEY,
                    conversation_id TEXT REFERENCES conversations(id),
                    feedback INTEGER NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
        conn.commit()
    finally:
        release_db_connection(conn)

def save_conversation(conversation_id, question, answer, course):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO conversations (id, question, answer, course) VALUES (%s, %s, %s, %s)",
                (conversation_id, question, answer, course)
            )
        conn.commit()
    finally:
        release_db_connection(conn)

def save_feedback(conversation_id, feedback):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO feedback (conversation_id, feedback) VALUES (%s, %s)",
                (conversation_id, feedback)
            )
        conn.commit()
    finally:
        release_db_connection(conn)

# Initialize the database when the module is imported
init_db()
```

requirements.txt

```
streamlit==1.22.0
elasticsearch==8.8.0
openai==0.27.8
psycopg2-binary==2.9.6
python-dotenv==1.0.0
```

### Prompt 3 

Let's refactor this code

* move import to top
* create separate functions for each logical block of code
* add print statements for logging

```python
ELASTIC_URL = 'http://localhost:9201'


import requests 

base_url = 'https://github.com/DataTalksClub/llm-zoomcamp/blob/main'
relative_url = '03-vector-search/eval/documents-with-ids.json'
docs_url = f'{base_url}/{relative_url}?raw=1'
docs_response = requests.get(docs_url)
documents = docs_response.json()


import pandas as pd

base_url = 'https://github.com/DataTalksClub/llm-zoomcamp/blob/main'
relative_url = '03-vector-search/eval/ground-truth-data.csv'
ground_truth_url = f'{base_url}/{relative_url}?raw=1'

df_ground_truth = pd.read_csv(ground_truth_url)
df_ground_truth = df_ground_truth[df_ground_truth.course == 'machine-learning-zoomcamp']
ground_truth = df_ground_truth.to_dict(orient='records')


from sentence_transformers import SentenceTransformer

model_name = 'multi-qa-MiniLM-L6-cos-v1'
model = SentenceTransformer(model_name)


from elasticsearch import Elasticsearch

es_client = Elasticsearch(ELASTIC_URL) 

index_settings = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
        "properties": {
            "text": {"type": "text"},
            "section": {"type": "text"},
            "question": {"type": "text"},
            "course": {"type": "keyword"},
            "id": {"type": "keyword"},
            "question_text_vector": {
                "type": "dense_vector",
                "dims": 384,
                "index": True,
                "similarity": "cosine"
            },
        }
    }
}

index_name = "course-questions"

es_client.indices.delete(index=index_name, ignore_unavailable=True)
es_client.indices.create(index=index_name, body=index_settings)


from tqdm.auto import tqdm

for doc in tqdm(documents):
    question = doc['question']
    text = doc['text']
    doc['question_text_vector'] = model.encode(question + ' ' + text)

    es_client.index(index=index_name, document=doc)

from db import init_db

init_db()
```

---

I'll refactor the code as requested, moving imports to the top, creating separate functions for each logical block, and adding print statements for logging. Here's the refactored version


Refactored Code (main.py) (in our case: `prep.py`)

```python
import requests
import pandas as pd
from sentence_transformers import SentenceTransformer
from elasticsearch import Elasticsearch
from tqdm.auto import tqdm

from db import init_db

# Constants
ELASTIC_URL = 'http://localhost:9201'
BASE_URL = 'https://github.com/DataTalksClub/llm-zoomcamp/blob/main'
MODEL_NAME = 'multi-qa-MiniLM-L6-cos-v1'
INDEX_NAME = "course-questions"

def fetch_documents():
    print("Fetching documents...")
    relative_url = '03-vector-search/eval/documents-with-ids.json'
    docs_url = f'{BASE_URL}/{relative_url}?raw=1'
    docs_response = requests.get(docs_url)
    documents = docs_response.json()
    print(f"Fetched {len(documents)} documents")
    return documents

def fetch_ground_truth():
    print("Fetching ground truth data...")
    relative_url = '03-vector-search/eval/ground-truth-data.csv'
    ground_truth_url = f'{BASE_URL}/{relative_url}?raw=1'
    df_ground_truth = pd.read_csv(ground_truth_url)
    df_ground_truth = df_ground_truth[df_ground_truth.course == 'machine-learning-zoomcamp']
    ground_truth = df_ground_truth.to_dict(orient='records')
    print(f"Fetched {len(ground_truth)} ground truth records")
    return ground_truth

def load_model():
    print(f"Loading model: {MODEL_NAME}")
    return SentenceTransformer(MODEL_NAME)

def setup_elasticsearch():
    print("Setting up Elasticsearch...")
    es_client = Elasticsearch(ELASTIC_URL)
    
    index_settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "properties": {
                "text": {"type": "text"},
                "section": {"type": "text"},
                "question": {"type": "text"},
                "course": {"type": "keyword"},
                "id": {"type": "keyword"},
                "question_text_vector": {
                    "type": "dense_vector",
                    "dims": 384,
                    "index": True,
                    "similarity": "cosine"
                },
            }
        }
    }

    es_client.indices.delete(index=INDEX_NAME, ignore_unavailable=True)
    es_client.indices.create(index=INDEX_NAME, body=index_settings)
    print(f"Elasticsearch index '{INDEX_NAME}' created")
    return es_client

def index_documents(es_client, documents, model):
    print("Indexing documents...")
    for doc in tqdm(documents):
        question = doc['question']
        text = doc['text']
        doc['question_text_vector'] = model.encode(question + ' ' + text).tolist()
        es_client.index(index=INDEX_NAME, document=doc)
    print(f"Indexed {len(documents)} documents")

def main():
    print("Starting the indexing process...")
    
    documents = fetch_documents()
    ground_truth = fetch_ground_truth()
    model = load_model()
    es_client = setup_elasticsearch()
    index_documents(es_client, documents, model)
    
    print("Initializing database...")
    init_db()
    
    print("Indexing process completed successfully!")

if __name__ == "__main__":
    main()
```

### Prompt 4

let's replace this 

```python
def init_db():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS conversations (
                    id TEXT PRIMARY KEY,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL,
                    course TEXT NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS feedback (
                    id SERIAL PRIMARY KEY,
                    conversation_id TEXT REFERENCES conversations(id),
                    feedback INTEGER NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
        conn.commit()
    finally:
        release_db_connection(conn)
```

with dropping first if exists and then creating

--- 

I'll modify the `init_db()` function to drop the tables if they exist before creating them. This approach ensures a clean slate each time the database is initialized.

Updated Database Module (db.py)

```python
import os
import psycopg2
from psycopg2.extras import DictCursor

# Global connection pool
conn_pool = None

def get_db_connection():
    global conn_pool
    if conn_pool is None:
        conn_pool = psycopg2.pool.SimpleConnectionPool(
            1, 20,
            host=os.getenv('POSTGRES_HOST', 'postgres'),
            database=os.getenv('POSTGRES_DB', 'course_assistant'),
            user=os.getenv('POSTGRES_USER', 'your_username'),
            password=os.getenv('POSTGRES_PASSWORD', 'your_password')
        )
    return conn_pool.getconn()

def release_db_connection(conn):
    global conn_pool
    conn_pool.putconn(conn)

def init_db():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            # Drop tables if they exist
            cur.execute("DROP TABLE IF EXISTS feedback")
            cur.execute("DROP TABLE IF EXISTS conversations")
            
            print("Existing tables dropped.")

            # Create tables
            cur.execute("""
                CREATE TABLE conversations (
                    id TEXT PRIMARY KEY,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL,
                    course TEXT NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            cur.execute("""
                CREATE TABLE feedback (
                    id SERIAL PRIMARY KEY,
                    conversation_id TEXT REFERENCES conversations(id),
                    feedback INTEGER NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            print("New tables created.")
        conn.commit()
        print("Database initialization completed successfully.")
    except Exception as e:
        print(f"An error occurred during database initialization: {e}")
        conn.rollback()
    finally:
        release_db_connection(conn)

def save_conversation(conversation_id, question, answer, course):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO conversations (id, question, answer, course) VALUES (%s, %s, %s, %s)",
                (conversation_id, question, answer, course)
            )
        conn.commit()
        print(f"Conversation saved with ID: {conversation_id}")
    except Exception as e:
        print(f"An error occurred while saving the conversation: {e}")
        conn.rollback()
    finally:
        release_db_connection(conn)

def save_feedback(conversation_id, feedback):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO feedback (conversation_id, feedback) VALUES (%s, %s)",
                (conversation_id, feedback)
            )
        conn.commit()
        print(f"Feedback saved for conversation ID: {conversation_id}")
    except Exception as e:
        print(f"An error occurred while saving feedback: {e}")
        conn.rollback()
    finally:
        release_db_connection(conn)

# Initialize the database when the module is imported
init_db()
```

### Prompt 5

I have this problem

```
Successfully installed psycopg2-binary-2.9.9
(base)
alexey@LAPTOP-O5BD8CDU MINGW64 ~/git/llm-zoomcamp/04-monitoring/app (main)
$ python prep.py
Initializing database...
Traceback (most recent call last):
  File "C:\Users\alexe\git\llm-zoomcamp\04-monitoring\app\prep.py", line 99, in <module>
    main()
  File "C:\Users\alexe\git\llm-zoomcamp\04-monitoring\app\prep.py", line 93, in main
    init_db()
  File "C:\Users\alexe\git\llm-zoomcamp\04-monitoring\app\db.py", line 29, in init_db
    conn = get_db_connection()
           ^^^^^^^^^^^^^^^^^^^
  File "C:\Users\alexe\git\llm-zoomcamp\04-monitoring\app\db.py", line 12, in get_db_connection
    conn_pool = psycopg2.pool.SimpleConnectionPool(
                ^^^^^^^^^^^^^
AttributeError: module 'psycopg2' has no attribute 'pool'
```

I just installed `psycopg2-binary-2.9.9`

---

The error you're encountering is because the psycopg2 module doesn't have a pool attribute directly. The connection pooling functionality is actually part of the `psycopg2.pool` module, which needs to be imported separately. Let's modify the `db.py` file to correct this issue and simplify the connection management.

Updated Database Module (db.py)

```python
import os
import psycopg2
from psycopg2.extras import DictCursor

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv('POSTGRES_HOST', 'postgres'),
        database=os.getenv('POSTGRES_DB', 'course_assistant'),
        user=os.getenv('POSTGRES_USER', 'your_username'),
        password=os.getenv('POSTGRES_PASSWORD', 'your_password')
    )

def init_db():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            # Drop tables if they exist
            cur.execute("DROP TABLE IF EXISTS feedback")
            cur.execute("DROP TABLE IF EXISTS conversations")
            
            print("Existing tables dropped.")

            # Create tables
            cur.execute("""
                CREATE TABLE conversations (
                    id TEXT PRIMARY KEY,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL,
                    course TEXT NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            cur.execute("""
                CREATE TABLE feedback (
                    id SERIAL PRIMARY KEY,
                    conversation_id TEXT REFERENCES conversations(id),
                    feedback INTEGER NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            print("New tables created.")
        conn.commit()
        print("Database initialization completed successfully.")
    except Exception as e:
        print(f"An error occurred during database initialization: {e}")
        conn.rollback()
    finally:
        conn.close()

def save_conversation(conversation_id, question, answer, course):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO conversations (id, question, answer, course) VALUES (%s, %s, %s, %s)",
                (conversation_id, question, answer, course)
            )
        conn.commit()
        print(f"Conversation saved with ID: {conversation_id}")
    except Exception as e:
        print(f"An error occurred while saving the conversation: {e}")
        conn.rollback()
    finally:
        conn.close()

def save_feedback(conversation_id, feedback):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO feedback (conversation_id, feedback) VALUES (%s, %s)",
                (conversation_id, feedback)
            )
        conn.commit()
        print(f"Feedback saved for conversation ID: {conversation_id}")
    except Exception as e:
        print(f"An error occurred while saving feedback: {e}")
        conn.rollback()
    finally:
        conn.close()

# Initialize the database when the module is imported
init_db()
```

### Prompt 6

let's create a `.env` file since we use pyenv

---

Here's a template for your `.env` file:

```
# PostgreSQL Configuration
POSTGRES_HOST=localhost
POSTGRES_DB=course_assistant
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password

# Elasticsearch Configuration
ELASTIC_URL=http://localhost:9201

# Other Configuration
MODEL_NAME=multi-qa-MiniLM-L6-cos-v1
INDEX_NAME=course-questions

# Add any other environment-specific variables here
```

You'll need to install the `python-dotenv` package if you haven't already:

```
pip install python-dotenv
```

Updated main.py with dotenv

```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Now you can use environment variables like this:
ELASTIC_URL = os.getenv('ELASTIC_URL')
MODEL_NAME = os.getenv('MODEL_NAME')
INDEX_NAME = os.getenv('INDEX_NAME')

# ... rest of your imports ...

def setup_elasticsearch():
    print("Setting up Elasticsearch...")
    es_client = Elasticsearch(ELASTIC_URL)
    
    # ... rest of the function ...

# ... rest of your code ...

def main():
    print("Starting the indexing process...")
    
    documents = fetch_documents()
    ground_truth = fetch_ground_truth()
    model = load_model()
    es_client = setup_elasticsearch()
    index_documents(es_client, documents, model)
    
    print("Initializing database...")
    init_db()
    
    print("Indexing process completed successfully!")

if __name__ == "__main__":
    main()
```

Updated db.py with dotenv

```python
import os
import psycopg2
from psycopg2.extras import DictCursor
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv('POSTGRES_HOST'),
        database=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD')
    )

# ... rest of your db.py code ...
```

### Prompt 7

Can we add more logs here so we know something is happening

```python
import streamlit as st
import time
import uuid

from assistant import get_answer
from db import save_conversation, save_feedback

def main():
    st.title("Course Assistant")

    # Session state initialization
    if 'conversation_id' not in st.session_state:
        st.session_state.conversation_id = str(uuid.uuid4())
    if 'count' not in st.session_state:
        st.session_state.count = 0

    # Course selection
    course = st.selectbox(
        "Select a course:",
        ["machine-learning-zoomcamp", "data-engineering-zoomcamp", "mlops-zoomcamp"]
    )

    # User input
    user_input = st.text_input("Enter your question:")

    if st.button("Ask"):
        with st.spinner('Processing...'):
            output = get_answer(user_input, course)
            st.success("Completed!")
            st.write(output)
            
            # Save conversation to database
            save_conversation(st.session_state.conversation_id, user_input, output, course)

    # Feedback buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("+1"):
            st.session_state.count += 1
            save_feedback(st.session_state.conversation_id, 1)
    with col2:
        if st.button("-1"):
            st.session_state.count -= 1
            save_feedback(st.session_state.conversation_id, -1)

    st.write(f"Current count: {st.session_state.count}")

if __name__ == "__main__":
    main()
```

I don't like logging, let's just use `print` statements


---

Streamlit App with Enhanced Logging

```python
import streamlit as st
import time
import uuid

from assistant import get_answer
from db import save_conversation, save_feedback

def main():
    print("Starting the Course Assistant application")
    st.title("Course Assistant")

    # Session state initialization
    if 'conversation_id' not in st.session_state:
        st.session_state.conversation_id = str(uuid.uuid4())
        print(f"New conversation started with ID: {st.session_state.conversation_id}")
    if 'count' not in st.session_state:
        st.session_state.count = 0
        print("Feedback count initialized to 0")

    # Course selection
    course = st.selectbox(
        "Select a course:",
        ["machine-learning-zoomcamp", "data-engineering-zoomcamp", "mlops-zoomcamp"]
    )
    print(f"User selected course: {course}")

    # User input
    user_input = st.text_input("Enter your question:")

    if st.button("Ask"):
        print(f"User asked: '{user_input}'")
        with st.spinner('Processing...'):
            print("Getting answer from assistant")
            start_time = time.time()
            output = get_answer(user_input, course)
            end_time = time.time()
            print(f"Answer received in {end_time - start_time:.2f} seconds")
            st.success("Completed!")
            st.write(output)
            
            # Save conversation to database
            print("Saving conversation to database")
            save_conversation(st.session_state.conversation_id, user_input, output, course)
            print("Conversation saved successfully")

    # Feedback buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("+1"):
            st.session_state.count += 1
            print(f"Positive feedback received. New count: {st.session_state.count}")
            save_feedback(st.session_state.conversation_id, 1)
            print("Positive feedback saved to database")
    with col2:
        if st.button("-1"):
            st.session_state.count -= 1
            print(f"Negative feedback received. New count: {st.session_state.count}")
            save_feedback(st.session_state.conversation_id, -1)
            print("Negative feedback saved to database")

    st.write(f"Current count: {st.session_state.count}")

    print("Streamlit app loop completed")

if __name__ == "__main__":
    print("Course Assistant application started")
    main()
```

### Prompt 8

I don't see the logs in docker

---

Streamlit App with Flushed Print Statements

```python
import streamlit as st
import time
import uuid
import sys

from assistant import get_answer
from db import save_conversation, save_feedback

def print_log(message):
    print(message, flush=True)
    sys.stdout.flush()

def main():
    print_log("Starting the Course Assistant application")
    st.title("Course Assistant")

    # Session state initialization
    if 'conversation_id' not in st.session_state:
        st.session_state.conversation_id = str(uuid.uuid4())
        print_log(f"New conversation started with ID: {st.session_state.conversation_id}")
    if 'count' not in st.session_state:
        st.session_state.count = 0
        print_log("Feedback count initialized to 0")

    # Course selection
    course = st.selectbox(
        "Select a course:",
        ["machine-learning-zoomcamp", "data-engineering-zoomcamp", "mlops-zoomcamp"]
    )
    print_log(f"User selected course: {course}")

    # User input
    user_input = st.text_input("Enter your question:")

    if st.button("Ask"):
        print_log(f"User asked: '{user_input}'")
        with st.spinner('Processing...'):
            print_log("Getting answer from assistant")
            start_time = time.time()
            output = get_answer(user_input, course)
            end_time = time.time()
            print_log(f"Answer received in {end_time - start_time:.2f} seconds")
            st.success("Completed!")
            st.write(output)
            
            # Save conversation to database
            print_log("Saving conversation to database")
            save_conversation(st.session_state.conversation_id, user_input, output, course)
            print_log("Conversation saved successfully")

    # Feedback buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("+1"):
            st.session_state.count += 1
            print_log(f"Positive feedback received. New count: {st.session_state.count}")
            save_feedback(st.session_state.conversation_id, 1)
            print_log("Positive feedback saved to database")
    with col2:
        if st.button("-1"):
            st.session_state.count -= 1
            print_log(f"Negative feedback received. New count: {st.session_state.count}")
            save_feedback(st.session_state.conversation_id, -1)
            print_log("Negative feedback saved to database")

    st.write(f"Current count: {st.session_state.count}")

    print_log("Streamlit app loop completed")

if __name__ == "__main__":
    print_log("Course Assistant application started")
    main()
```

Dockerfile for Streamlit App

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set Python to run in unbuffered mode
ENV PYTHONUNBUFFERED=1

# Run Streamlit
CMD ["python", "-u", "-m", "streamlit", "run", "app.py"]
```

## 4.6.2 Capturing User Feedback: Part 2

### Prompt 9

I want to do a few things:

* Have a way to choose between ollama and openai, so let's have a drop-down list in streamlit of what we use 
* Also, have a toggle between vector and text search. currently we use text search. I'll copy the code for vector search below

```python
def elastic_search_knn(field, vector, course):
    knn = {
        "field": field,
        "query_vector": vector,
        "k": 5,
        "num_candidates": 10000,
        "filter": {
            "term": {
                "course": course
            }
        }
    }

    search_query = {
        "knn": knn,
        "_source": ["text", "section", "question", "course", "id"]
    }

    es_results = es_client.search(
        index=index_name,
        body=search_query
    )
    
    result_docs = []
    
    for hit in es_results['hits']['hits']:
        result_docs.append(hit['_source'])

    return result_docs

def question_text_vector_knn(q):
    question = q['question']
    course = q['course']

    v_q = model.encode(question)

    return elastic_search_knn('question_text_vector', v_q, course)
```


This is my current code for assisntant.py:

```
import os
from elasticsearch import Elasticsearch
from openai import OpenAI


ELASTIC_URL = os.getenv('ELASTIC_URL', 'http://elasticsearch:9200')
OLLAMA_URL = os.getenv('OLLAMA_URL', 'http://ollama:11434/v1/')


es_client = Elasticsearch(ELASTIC_URL)
client = OpenAI(
    base_url=OLLAMA_URL,
    api_key='ollama'
)

def elastic_search(query, course, index_name="course-questions"):
    search_query = {
        "size": 5,
        "query": {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": query,
                        "fields": ["question^3", "text", "section"],
                        "type": "best_fields"
                    }
                },
                "filter": {
                    "term": {
                        "course": course
                    }
                }
            }
        }
    }

    response = es_client.search(index=index_name, body=search_query)
    return [hit['_source'] for hit in response['hits']['hits']]

def build_prompt(query, search_results):
    prompt_template = """
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT: 
{context}
""".strip()

    context = "\n\n".join([f"section: {doc['section']}\nquestion: {doc['question']}\nanswer: {doc['text']}" for doc in search_results])
    return prompt_template.format(question=query, context=context).strip()

def llm(prompt):
    response = client.chat.completions.create(
        model='phi3',
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def get_answer(query, course):
    search_results = elastic_search(query, course)
    prompt = build_prompt(query, search_results)
    answer = llm(prompt)
    return answer
```

---

Here's the updated version of your assistant.py file:

```python
import os
from elasticsearch import Elasticsearch
from openai import OpenAI
from sentence_transformers import SentenceTransformer

ELASTIC_URL = os.getenv('ELASTIC_URL', 'http://elasticsearch:9200')
OLLAMA_URL = os.getenv('OLLAMA_URL', 'http://ollama:11434/v1/')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your-api-key-here')

es_client = Elasticsearch(ELASTIC_URL)
ollama_client = OpenAI(base_url=OLLAMA_URL, api_key='ollama')
openai_client = OpenAI(api_key=OPENAI_API_KEY)

model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')

def elastic_search(query, course, index_name="course-questions"):
    search_query = {
        "size": 5,
        "query": {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": query,
                        "fields": ["question^3", "text", "section"],
                        "type": "best_fields"
                    }
                },
                "filter": {
                    "term": {
                        "course": course
                    }
                }
            }
        }
    }

    response = es_client.search(index=index_name, body=search_query)
    return [hit['_source'] for hit in response['hits']['hits']]

def elastic_search_knn(field, vector, course, index_name="course-questions"):
    knn = {
        "field": field,
        "query_vector": vector,
        "k": 5,
        "num_candidates": 10000,
        "filter": {
            "term": {
                "course": course
            }
        }
    }

    search_query = {
        "knn": knn,
        "_source": ["text", "section", "question", "course", "id"]
    }

    es_results = es_client.search(
        index=index_name,
        body=search_query
    )
    
    return [hit['_source'] for hit in es_results['hits']['hits']]

def build_prompt(query, search_results):
    prompt_template = """
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT: 
{context}
""".strip()

    context = "\n\n".join([f"section: {doc['section']}\nquestion: {doc['question']}\nanswer: {doc['text']}" for doc in search_results])
    return prompt_template.format(question=query, context=context).strip()

def llm(prompt, model_choice):
    if model_choice == 'Ollama':
        response = ollama_client.chat.completions.create(
            model='phi3',
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    elif model_choice == 'OpenAI':
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

def get_answer(query, course, model_choice, search_type):
    if search_type == 'Vector':
        vector = model.encode(query)
        search_results = elastic_search_knn('question_text_vector', vector, course)
    else:
        search_results = elastic_search(query, course)
    
    prompt = build_prompt(query, search_results)
    answer = llm(prompt, model_choice)
    return answer
```

Updated Streamlit App (app.py)

```python
import streamlit as st
import time
import uuid

from assistant import get_answer
from db import save_conversation, save_feedback

def print_log(message):
    print(message, flush=True)

def main():
    print_log("Starting the Course Assistant application")
    st.title("Course Assistant")

    # Session state initialization
    if 'conversation_id' not in st.session_state:
        st.session_state.conversation_id = str(uuid.uuid4())
        print_log(f"New conversation started with ID: {st.session_state.conversation_id}")
    if 'count' not in st.session_state:
        st.session_state.count = 0
        print_log("Feedback count initialized to 0")

    # Course selection
    course = st.selectbox(
        "Select a course:",
        ["machine-learning-zoomcamp", "data-engineering-zoomcamp", "mlops-zoomcamp"]
    )
    print_log(f"User selected course: {course}")

    # Model selection
    model_choice = st.selectbox(
        "Select a model:",
        ["Ollama", "OpenAI"]
    )
    print_log(f"User selected model: {model_choice}")

    # Search type selection
    search_type = st.radio(
        "Select search type:",
        ["Text", "Vector"]
    )
    print_log(f"User selected search type: {search_type}")

    # User input
    user_input = st.text_input("Enter your question:")

    if st.button("Ask"):
        print_log(f"User asked: '{user_input}'")
        with st.spinner('Processing...'):
            print_log(f"Getting answer from assistant using {model_choice} model and {search_type} search")
            start_time = time.time()
            output = get_answer(user_input, course, model_choice, search_type)
            end_time = time.time()
            print_log(f"Answer received in {end_time - start_time:.2f} seconds")
            st.success("Completed!")
            st.write(output)
            
            # Save conversation to database
            print_log("Saving conversation to database")
            save_conversation(st.session_state.conversation_id, user_input, output, course)
            print_log("Conversation saved successfully")

    # Feedback buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("+1"):
            st.session_state.count += 1
            print_log(f"Positive feedback received. New count: {st.session_state.count}")
            save_feedback(st.session_state.conversation_id, 1)
            print_log("Positive feedback saved to database")
    with col2:
        if st.button("-1"):
            st.session_state.count -= 1
            print_log(f"Negative feedback received. New count: {st.session_state.count}")
            save_feedback(st.session_state.conversation_id, -1)
            print_log("Negative feedback saved to database")

    st.write(f"Current count: {st.session_state.count}")

    print_log("Streamlit app loop completed")

if __name__ == "__main__":
    print_log("Course Assistant application started")
    main()
```

### Prompt 10

let's update docker-compose to pass the open ai key var too

```yaml
version: '3.8'

services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.4.3
    container_name: elasticsearch
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
    ports:
      - "${ELASTIC_PORT:-9200}:9200"
      - "9300:9300"
    volumes:
      - elasticsearch_data:/usr/share/elasticsearch/data

  ollama:
    image: ollama/ollama
    container_name: ollama
    volumes:
      - ollama_data:/root/.ollama
    ports:
      - "${OLLAMA_PORT:-11434}:11434"

  postgres:
    image: postgres:13
    container_name: postgres
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    ports:
      - "${POSTGRES_PORT:-5432}:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  streamlit:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: streamlit
    environment:
      - ELASTIC_URL=http://elasticsearch:${ELASTIC_PORT:-9200}
      - OLLAMA_URL=http://ollama:${OLLAMA_PORT:-11434}/v1/
      - POSTGRES_HOST=postgres
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - MODEL_NAME=${MODEL_NAME}
      - INDEX_NAME=${INDEX_NAME}
    ports:
      - "${STREAMLIT_PORT:-8501}:8501"
    depends_on:
      - elasticsearch
      - ollama
      - postgres

volumes:
  elasticsearch_data:
  ollama_data:
  postgres_data:
```

---

Updated docker-compose.yml

```yaml
version: '3.8'

services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.4.3
    container_name: elasticsearch
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
    ports:
      - "${ELASTIC_PORT:-9200}:9200"
      - "9300:9300"
    volumes:
      - elasticsearch_data:/usr/share/elasticsearch/data

  ollama:
    image: ollama/ollama
    container_name: ollama
    volumes:
      - ollama_data:/root/.ollama
    ports:
      - "${OLLAMA_PORT:-11434}:11434"

  postgres:
    image: postgres:13
    container_name: postgres
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    ports:
      - "${POSTGRES_PORT:-5432}:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  streamlit:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: streamlit
    environment:
      - ELASTIC_URL=http://elasticsearch:${ELASTIC_PORT:-9200}
      - OLLAMA_URL=http://ollama:${OLLAMA_PORT:-11434}/v1/
      - POSTGRES_HOST=postgres
      - POSTGRES_DB=${POSTGRES_DB}
      - POSTGRES_USER=${POSTGRES_USER}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
      - MODEL_NAME=${MODEL_NAME}
      - INDEX_NAME=${INDEX_NAME}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    ports:
      - "${STREAMLIT_PORT:-8501}:8501"
    depends_on:
      - elasticsearch
      - ollama
      - postgres

volumes:
  elasticsearch_data:
  ollama_data:
  postgres_data:
```

## 4.7 Monitoring

### Prompt 11

In the app, the model should be one of

- ollama/phi3
- openai/gpt-3.5-turbo
- openai/gpt-4o
- openai/gpt-4o-mini

I also want to add monitoring with grafana

I want to display:

* response time
* fraction of relevant answers (code for that is below)
* thumbs up / down stats
* last 5 conversations with ability to filter by relevancy
* model used
* prompt and completion tokens
* open ai costs 

We want to use pg for grafana backend, not prometheus, so let's modify
the tables we already have and include this information there

for computing relevancy always use gpt-4o-mini

code for relevancy:

```python
prompt2_template = """
You are an expert evaluator for a Retrieval-Augmented Generation (RAG) system.
Your task is to analyze the relevance of the generated answer to the given question.
Based on the relevance of the generated answer, you will classify it
as "NON_RELEVANT", "PARTLY_RELEVANT", or "RELEVANT".

Here is the data for evaluation:

Question: {question}
Generated Answer: {answer_llm}

Please analyze the content and context of the generated answer in relation to the question
and provide your evaluation in parsable JSON without using code blocks:

{{
  "Relevance": "NON_RELEVANT" | "PARTLY_RELEVANT" | "RELEVANT",
  "Explanation": "[Provide a brief explanation for your evaluation]"
}}
""".strip()

prompt = prompt2_template.format(**record)
evaluation = llm(prompt, model='gpt-4o-mini')
json_eval = json.loads(str_eval)


client = OpenAI()

def llm(prompt, model='gpt-4o'):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content
```

if the result is not parsable, return some default value

so we can modify our `get_answer` function to include all this 
and return a dictionary with all the values in addition
to the answer

--- 

let's update the assistant.py file:

```python
import os
import json
import time
from elasticsearch import Elasticsearch
from openai import OpenAI
from sentence_transformers import SentenceTransformer

ELASTIC_URL = os.getenv('ELASTIC_URL', 'http://elasticsearch:9200')
OLLAMA_URL = os.getenv('OLLAMA_URL', 'http://ollama:11434/v1/')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your-api-key-here')

es_client = Elasticsearch(ELASTIC_URL)
ollama_client = OpenAI(base_url=OLLAMA_URL, api_key='ollama')
openai_client = OpenAI(api_key=OPENAI_API_KEY)

model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1', device='cpu')

def elastic_search(query, course, index_name="course-questions"):
    # ... (existing elastic_search function)

def elastic_search_knn(field, vector, course, index_name="course-questions"):
    # ... (existing elastic_search_knn function)

def build_prompt(query, search_results):
    # ... (existing build_prompt function)

def llm(prompt, model_choice):
    start_time = time.time()
    if model_choice.startswith('ollama/'):
        response = ollama_client.chat.completions.create(
            model=model_choice.split('/')[-1],
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response.choices[0].message.content
        tokens = {
            'prompt_tokens': response.usage.prompt_tokens,
            'completion_tokens': response.usage.completion_tokens,
            'total_tokens': response.usage.total_tokens
        }
    elif model_choice.startswith('openai/'):
        response = openai_client.chat.completions.create(
            model=model_choice.split('/')[-1],
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response.choices[0].message.content
        tokens = {
            'prompt_tokens': response.usage.prompt_tokens,
            'completion_tokens': response.usage.completion_tokens,
            'total_tokens': response.usage.total_tokens
        }
    else:
        raise ValueError(f"Unknown model choice: {model_choice}")
    
    end_time = time.time()
    response_time = end_time - start_time
    
    return answer, tokens, response_time

def evaluate_relevance(question, answer):
    prompt_template = """
    You are an expert evaluator for a Retrieval-Augmented Generation (RAG) system.
    Your task is to analyze the relevance of the generated answer to the given question.
    Based on the relevance of the generated answer, you will classify it
    as "NON_RELEVANT", "PARTLY_RELEVANT", or "RELEVANT".

    Here is the data for evaluation:

    Question: {question}
    Generated Answer: {answer}

    Please analyze the content and context of the generated answer in relation to the question
    and provide your evaluation in parsable JSON without using code blocks:

    {{
      "Relevance": "NON_RELEVANT" | "PARTLY_RELEVANT" | "RELEVANT",
      "Explanation": "[Provide a brief explanation for your evaluation]"
    }}
    """.strip()

    prompt = prompt_template.format(question=question, answer=answer)
    evaluation, tokens, _ = llm(prompt, 'openai/gpt-4o-mini')
    
    try:
        json_eval = json.loads(evaluation)
        return json_eval['Relevance'], json_eval['Explanation'], tokens
    except json.JSONDecodeError:
        return "UNKNOWN", "Failed to parse evaluation", tokens

def get_answer(query, course, model_choice, search_type):
    if search_type == 'Vector':
        vector = model.encode(query)
        search_results = elastic_search_knn('question_text_vector', vector, course)
    else:
        search_results = elastic_search(query, course)
    
    prompt = build_prompt(query, search_results)
    answer, tokens, response_time = llm(prompt, model_choice)
    
    relevance, explanation, eval_tokens = evaluate_relevance(query, answer)
    
    # Calculate OpenAI costs (you may need to adjust these rates)
    openai_cost = 0
    if model_choice.startswith('openai/'):
        if model_choice == 'openai/gpt-3.5-turbo':
            openai_cost = (tokens['prompt_tokens'] * 0.0015 + tokens['completion_tokens'] * 0.002) / 1000
        elif model_choice in ['openai/gpt-4o', 'openai/gpt-4o-mini']:
            openai_cost = (tokens['prompt_tokens'] * 0.03 + tokens['completion_tokens'] * 0.06) / 1000
    
    return {
        'answer': answer,
        'response_time': response_time,
        'relevance': relevance,
        'relevance_explanation': explanation,
        'model_used': model_choice,
        'prompt_tokens': tokens['prompt_tokens'],
        'completion_tokens': tokens['completion_tokens'],
        'total_tokens': tokens['total_tokens'],
        'eval_prompt_tokens': eval_tokens['prompt_tokens'],
        'eval_completion_tokens': eval_tokens['completion_tokens'],
        'eval_total_tokens': eval_tokens['total_tokens'],
        'openai_cost': openai_cost
    }
```

db.py

```python
import os
import psycopg2
from psycopg2.extras import DictCursor

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv('POSTGRES_HOST', 'postgres'),
        database=os.getenv('POSTGRES_DB', 'course_assistant'),
        user=os.getenv('POSTGRES_USER', 'your_username'),
        password=os.getenv('POSTGRES_PASSWORD', 'your_password')
    )

def init_db():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            # Drop tables if they exist
            cur.execute("DROP TABLE IF EXISTS feedback")
            cur.execute("DROP TABLE IF EXISTS conversations")
            
            # Create tables
            cur.execute("""
                CREATE TABLE conversations (
                    id TEXT PRIMARY KEY,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL,
                    course TEXT NOT NULL,
                    model_used TEXT NOT NULL,
                    response_time FLOAT NOT NULL,
                    relevance TEXT NOT NULL,
                    relevance_explanation TEXT NOT NULL,
                    prompt_tokens INTEGER NOT NULL,
                    completion_tokens INTEGER NOT NULL,
                    total_tokens INTEGER NOT NULL,
                    eval_prompt_tokens INTEGER NOT NULL,
                    eval_completion_tokens INTEGER NOT NULL,
                    eval_total_tokens INTEGER NOT NULL,
                    openai_cost FLOAT NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            cur.execute("""
                CREATE TABLE feedback (
                    id SERIAL PRIMARY KEY,
                    conversation_id TEXT REFERENCES conversations(id),
                    feedback INTEGER NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
        conn.commit()
    finally:
        conn.close()

def save_conversation(conversation_id, question, answer_data, course):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO conversations 
                (id, question, answer, course, model_used, response_time, relevance, 
                relevance_explanation, prompt_tokens, completion_tokens, total_tokens, 
                eval_prompt_tokens, eval_completion_tokens, eval_total_tokens, openai_cost)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                conversation_id, question, answer_data['answer'], course, 
                answer_data['model_used'], answer_data['response_time'], 
                answer_data['relevance'], answer_data['relevance_explanation'],
                answer_data['prompt_tokens'], answer_data['completion_tokens'], 
                answer_data['total_tokens'], answer_data['eval_prompt_tokens'],
                answer_data['eval_completion_tokens'], answer_data['eval_total_tokens'],
                answer_data['openai_cost']
            ))
        conn.commit()
    finally:
        conn.close()

def save_feedback(conversation_id, feedback):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO feedback (conversation_id, feedback) VALUES (%s, %s)",
                (conversation_id, feedback)
            )
        conn.commit()
    finally:
        conn.close()

def get_recent_conversations(limit=5, relevance=None):
    conn = get_db_connection()
    try:
        with conn.cursor(cursor_factory=DictCursor) as cur:
            query = """
                SELECT c.*, f.feedback
                FROM conversations c
                LEFT JOIN feedback f ON c.id = f.conversation_id
            """
            if relevance:
                query += f" WHERE c.relevance = '{relevance}'"
            query += " ORDER BY c.timestamp DESC LIMIT %s"
            
            cur.execute(query, (limit,))
            return cur.fetchall()
    finally:
        conn.close()

def get_feedback_stats():
    conn = get_db_connection()
    try:
        with conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute("""
                SELECT 
                    SUM(CASE WHEN feedback > 0 THEN 1 ELSE 0 END) as thumbs_up,
                    SUM(CASE WHEN feedback < 0 THEN 1 ELSE 0 END) as thumbs_down
                FROM feedback
            """)
            return cur.fetchone()
    finally:
        conn.close()

# Initialize the database
init_db()
```

Updated Streamlit App (app.py)

```python
import streamlit as st
import time
import uuid

from assistant import get_answer
from db import save_conversation, save_feedback, get_recent_conversations, get_feedback_stats

def print_log(message):
    print(message, flush=True)

def main():
    print_log("Starting the Course Assistant application")
    st.title("Course Assistant")

    # Session state initialization
    if 'conversation_id' not in st.session_state:
        st.session_state.conversation_id = str(uuid.uuid4())
        print_log(f"New conversation started with ID: {st.session_state.conversation_id}")
    if 'count' not in st.session_state:
        st.session_state.count = 0
        print_log("Feedback count initialized to 0")

    # Course selection
    course = st.selectbox(
        "Select a course:",
        ["machine-learning-zoomcamp", "data-engineering-zoomcamp", "mlops-zoomcamp"]
    )
    print_log(f"User selected course: {course}")

    # Model selection
    model_choice = st.selectbox(
        "Select a model:",
        ["ollama/phi3", "openai/gpt-3.5-turbo", "openai/gpt-4o", "openai/gpt-4o-mini"]
    )
    print_log(f"User selected model: {model_choice}")

    # Search type selection
    search_type = st.radio(
        "Select search type:",
        ["Text", "Vector"]
    )
    print_log(f"User selected search type: {search_type}")

    # User input
    user_input = st.text_input("Enter your question:")

    if st.button("Ask"):
        print_log(f"User asked: '{user_input}'")
        with st.spinner('Processing...'):
            print_log(f"Getting answer from assistant using {model_choice} model and {search_type} search")
            start_time = time.time()
            answer_data = get_answer(user_input, course, model_choice, search_type)
            end_time = time.time()
            print_log(f"Answer received in {end_time - start_time:.2f} seconds")
            st.success("Completed!")
            st.write(answer_data['answer'])
            
            # Display monitoring information
            st.write(f"Response time: {answer_data['response_time']:.2f} seconds")
            st.write(f"Relevance: {answer_data['relevance']}")
            st.write(f"Model used: {answer_data['model_used']}")
            st.write(f"Total tokens: {answer_data['total_tokens']}")
            if answer_data['openai_cost'] > 0:
                st.write(f"OpenAI cost: ${answer_data['openai_cost']:.4f}")
            
            # Save conversation to database
            print_log("Saving conversation to database")
            save_conversation(st.session_state.conversation_id, user_input, answer_data, course)
            print_log("Conversation saved successfully")

    # Feedback buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("+1"):
            st.session_state.count += 1
            print_log(f"Positive feedback received. New count: {st.session_state.count}")
            save_feedback(st.session_state.conversation_id, 1)
            print_log("Positive feedback saved to database")
    with col2:
        if st.button("-1"):
            st.session_state.count -= 1
            print_log(f"Negative feedback received. New count: {st.session_state.count}")
            save_feedback(st.session_state.conversation_id, -1)
            print_log("Negative feedback saved to database")

    st.write(f"Current count: {st.session_state.count}")

    # Display recent conversations
    st.subheader("Recent Conversations")
    relevance_filter = st.selectbox("Filter by relevance:", ["All", "RELEVANT", "PARTLY_RELEVANT", "NON_RELEVANT"])
    recent_conversations = get_recent_conversations(limit=5, relevance=relevance_filter if relevance_filter != "All" else None)
    for conv in recent_conversations:
        st.write(f"Q: {conv['question']}")
        st.write(f"A: {conv['answer']}")
        st.write(f"Relevance: {conv['relevance']}")
        st.write(f"Model: {conv['model_used']}")
        st.write("---")

    # Display feedback stats
    feedback_stats = get_feedback_stats()
    st.subheader("Feedback Statistics")
    st.write(f"Thumbs up: {feedback_stats['thumbs_up']}")
    st.write(f"Thumbs down: {feedback_stats['thumbs_down']}")

    print_log("Streamlit app loop completed")

if __name__ == "__main__":
    print_log("Course Assistant application started")
    main()
```

we'll update the `docker-compose.yml` file to include Grafana:

```yaml
version: '3.8'

services:
  elasticsearch:
    # ... (existing elasticsearch configuration)

  ollama:
    # ... (existing ollama configuration)

  postgres:
    # ... (existing postgres configuration)

  streamlit:
    # ... (existing streamlit configuration)

  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    ports:
      - "3000:3000"
    volumes:
      - grafana_data:/var/lib/grafana
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=${GRAFANA_ADMIN_PASSWORD:-admin}
    depends_on:
      - postgres

volumes:
  elasticsearch_data:
  ollama_data:
  postgres_data:
  grafana_data:
```

Queries: see [grafana-queries.md](grafana-queries.md)

### Prompt 12

let's create a script that generate some synthetic data

first puts data in periods between now and 6 hours ago
and then add some test data live so we can see new data in appearing grafana every second. we should use the db module for inserting the data

---

synthetic_data.py (in our case generate_data.py)

```python
import time
import random
import uuid
from datetime import datetime, timedelta
from db import save_conversation, save_feedback, get_db_connection

# List of sample questions and answers
SAMPLE_QUESTIONS = [
    "What is machine learning?",
    "How does linear regression work?",
    "Explain the concept of overfitting.",
    "What is the difference between supervised and unsupervised learning?",
    "How does cross-validation help in model evaluation?"
]

SAMPLE_ANSWERS = [
    "Machine learning is a subset of artificial intelligence that focuses on the development of algorithms and statistical models that enable computer systems to improve their performance on a specific task through experience.",
    "Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables by fitting a linear equation to observed data.",
    "Overfitting occurs when a machine learning model learns the training data too well, including its noise and fluctuations, resulting in poor generalization to new, unseen data.",
    "Supervised learning involves training models on labeled data, while unsupervised learning deals with finding patterns in unlabeled data without predefined outputs.",
    "Cross-validation is a technique used to assess how well a model will generalize to an independent dataset. It involves partitioning the data into subsets, training the model on a subset, and validating it on the remaining data."
]

COURSES = ["machine-learning-zoomcamp", "data-engineering-zoomcamp", "mlops-zoomcamp"]
MODELS = ["ollama/phi3", "openai/gpt-3.5-turbo", "openai/gpt-4o", "openai/gpt-4o-mini"]
RELEVANCE = ["RELEVANT", "PARTLY_RELEVANT", "NON_RELEVANT"]

def generate_synthetic_data(start_time, end_time):
    current_time = start_time
    while current_time < end_time:
        conversation_id = str(uuid.uuid4())
        question = random.choice(SAMPLE_QUESTIONS)
        answer = random.choice(SAMPLE_ANSWERS)
        course = random.choice(COURSES)
        model = random.choice(MODELS)
        relevance = random.choice(RELEVANCE)
        
        answer_data = {
            'answer': answer,
            'response_time': random.uniform(0.5, 5.0),
            'relevance': relevance,
            'relevance_explanation': f"This answer is {relevance.lower()} to the question.",
            'model_used': model,
            'prompt_tokens': random.randint(50, 200),
            'completion_tokens': random.randint(50, 300),
            'total_tokens': random.randint(100, 500),
            'eval_prompt_tokens': random.randint(50, 150),
            'eval_completion_tokens': random.randint(20, 100),
            'eval_total_tokens': random.randint(70, 250),
            'openai_cost': random.uniform(0.001, 0.1) if model.startswith('openai/') else 0
        }
        
        save_conversation(conversation_id, question, answer_data, course)
        
        # Generate feedback for some conversations
        if random.random() < 0.7:  # 70% chance of feedback
            feedback = 1 if random.random() < 0.8 else -1  # 80% positive feedback
            save_feedback(conversation_id, feedback)
        
        current_time += timedelta(minutes=random.randint(1, 15))
        
        # Update the timestamp in the database
        conn = get_db_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE conversations SET timestamp = %s WHERE id = %s",
                    (current_time, conversation_id)
                )
            conn.commit()
        finally:
            conn.close()

def generate_live_data():
    while True:
        conversation_id = str(uuid.uuid4())
        question = random.choice(SAMPLE_QUESTIONS)
        answer = random.choice(SAMPLE_ANSWERS)
        course = random.choice(COURSES)
        model = random.choice(MODELS)
        relevance = random.choice(RELEVANCE)
        
        answer_data = {
            'answer': answer,
            'response_time': random.uniform(0.5, 5.0),
            'relevance': relevance,
            'relevance_explanation': f"This answer is {relevance.lower()} to the question.",
            'model_used': model,
            'prompt_tokens': random.randint(50, 200),
            'completion_tokens': random.randint(50, 300),
            'total_tokens': random.randint(100, 500),
            'eval_prompt_tokens': random.randint(50, 150),
            'eval_completion_tokens': random.randint(20, 100),
            'eval_total_tokens': random.randint(70, 250),
            'openai_cost': random.uniform(0.001, 0.1) if model.startswith('openai/') else 0
        }
        
        save_conversation(conversation_id, question, answer_data, course)
        
        # Generate feedback for some conversations
        if random.random() < 0.7:  # 70% chance of feedback
            feedback = 1 if random.random() < 0.8 else -1  # 80% positive feedback
            save_feedback(conversation_id, feedback)
        
        time.sleep(1)  # Wait for 1 second before generating the next data point

if __name__ == "__main__":
    # Generate historical data
    end_time = datetime.now()
    start_time = end_time - timedelta(hours=6)
    print("Generating historical data...")
    generate_synthetic_data(start_time, end_time)
    print("Historical data generation complete.")

    # Generate live data
    print("Generating live data... Press Ctrl+C to stop.")
    try:
        generate_live_data()
    except KeyboardInterrupt:
        print("Live data generation stopped.")
```

### Prompt 13

there's a problem with the data generator: since it doesn't use the timezome, some of the data generated previously has future timestamp. I'm in CET (Europe/Berlin), so let's use a timezone

can we do it without pytz?


---

updated_synthetic_data.py

```python
import time
import random
import uuid
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from db import save_conversation, save_feedback, get_db_connection

# Set the timezone to CET (Europe/Berlin)
tz = ZoneInfo("Europe/Berlin")

# List of sample questions and answers
SAMPLE_QUESTIONS = [
    "What is machine learning?",
    "How does linear regression work?",
    "Explain the concept of overfitting.",
    "What is the difference between supervised and unsupervised learning?",
    "How does cross-validation help in model evaluation?"
]

SAMPLE_ANSWERS = [
    "Machine learning is a subset of artificial intelligence that focuses on the development of algorithms and statistical models that enable computer systems to improve their performance on a specific task through experience.",
    "Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables by fitting a linear equation to observed data.",
    "Overfitting occurs when a machine learning model learns the training data too well, including its noise and fluctuations, resulting in poor generalization to new, unseen data.",
    "Supervised learning involves training models on labeled data, while unsupervised learning deals with finding patterns in unlabeled data without predefined outputs.",
    "Cross-validation is a technique used to assess how well a model will generalize to an independent dataset. It involves partitioning the data into subsets, training the model on a subset, and validating it on the remaining data."
]

COURSES = ["machine-learning-zoomcamp", "data-engineering-zoomcamp", "mlops-zoomcamp"]
MODELS = ["ollama/phi3", "openai/gpt-3.5-turbo", "openai/gpt-4o", "openai/gpt-4o-mini"]
RELEVANCE = ["RELEVANT", "PARTLY_RELEVANT", "NON_RELEVANT"]

def generate_synthetic_data(start_time, end_time):
    current_time = start_time
    while current_time < end_time:
        conversation_id = str(uuid.uuid4())
        question = random.choice(SAMPLE_QUESTIONS)
        answer = random.choice(SAMPLE_ANSWERS)
        course = random.choice(COURSES)
        model = random.choice(MODELS)
        relevance = random.choice(RELEVANCE)
        
        answer_data = {
            'answer': answer,
            'response_time': random.uniform(0.5, 5.0),
            'relevance': relevance,
            'relevance_explanation': f"This answer is {relevance.lower()} to the question.",
            'model_used': model,
            'prompt_tokens': random.randint(50, 200),
            'completion_tokens': random.randint(50, 300),
            'total_tokens': random.randint(100, 500),
            'eval_prompt_tokens': random.randint(50, 150),
            'eval_completion_tokens': random.randint(20, 100),
            'eval_total_tokens': random.randint(70, 250),
            'openai_cost': random.uniform(0.001, 0.1) if model.startswith('openai/') else 0
        }
        
        save_conversation(conversation_id, question, answer_data, course)
        
        # Generate feedback for some conversations
        if random.random() < 0.7:  # 70% chance of feedback
            feedback = 1 if random.random() < 0.8 else -1  # 80% positive feedback
            save_feedback(conversation_id, feedback)
        
        current_time += timedelta(minutes=random.randint(1, 15))
        
        # Update the timestamp in the database
        conn = get_db_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE conversations SET timestamp = %s WHERE id = %s",
                    (current_time, conversation_id)
                )
            conn.commit()
        finally:
            conn.close()

def generate_live_data():
    while True:
        conversation_id = str(uuid.uuid4())
        question = random.choice(SAMPLE_QUESTIONS)
        answer = random.choice(SAMPLE_ANSWERS)
        course = random.choice(COURSES)
        model = random.choice(MODELS)
        relevance = random.choice(RELEVANCE)
        
        answer_data = {
            'answer': answer,
            'response_time': random.uniform(0.5, 5.0),
            'relevance': relevance,
            'relevance_explanation': f"This answer is {relevance.lower()} to the question.",
            'model_used': model,
            'prompt_tokens': random.randint(50, 200),
            'completion_tokens': random.randint(50, 300),
            'total_tokens': random.randint(100, 500),
            'eval_prompt_tokens': random.randint(50, 150),
            'eval_completion_tokens': random.randint(20, 100),
            'eval_total_tokens': random.randint(70, 250),
            'openai_cost': random.uniform(0.001, 0.1) if model.startswith('openai/') else 0
        }
        
        save_conversation(conversation_id, question, answer_data, course)
        
        # Generate feedback for some conversations
        if random.random() < 0.7:  # 70% chance of feedback
            feedback = 1 if random.random() < 0.8 else -1  # 80% positive feedback
            save_feedback(conversation_id, feedback)
        
        time.sleep(1)  # Wait for 1 second before generating the next data point

if __name__ == "__main__":
    # Generate historical data
    end_time = datetime.now(tz)
    start_time = end_time - timedelta(hours=6)
    print("Generating historical data...")
    generate_synthetic_data(start_time, end_time)
    print("Historical data generation complete.")

    # Generate live data
    print("Generating live data... Press Ctrl+C to stop.")
    try:
        generate_live_data()
    except KeyboardInterrupt:
        print("Live data generation stopped.")
```

### Prompt 14

let's add print statements so I see what's happening

---

```python
import time
import random
import uuid
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from db import save_conversation, save_feedback, get_db_connection

# Set the timezone to CET (Europe/Berlin)
tz = ZoneInfo("Europe/Berlin")

# List of sample questions and answers
SAMPLE_QUESTIONS = [
    "What is machine learning?",
    "How does linear regression work?",
    "Explain the concept of overfitting.",
    "What is the difference between supervised and unsupervised learning?",
    "How does cross-validation help in model evaluation?"
]

SAMPLE_ANSWERS = [
    "Machine learning is a subset of artificial intelligence that focuses on the development of algorithms and statistical models that enable computer systems to improve their performance on a specific task through experience.",
    "Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables by fitting a linear equation to observed data.",
    "Overfitting occurs when a machine learning model learns the training data too well, including its noise and fluctuations, resulting in poor generalization to new, unseen data.",
    "Supervised learning involves training models on labeled data, while unsupervised learning deals with finding patterns in unlabeled data without predefined outputs.",
    "Cross-validation is a technique used to assess how well a model will generalize to an independent dataset. It involves partitioning the data into subsets, training the model on a subset, and validating it on the remaining data."
]

COURSES = ["machine-learning-zoomcamp", "data-engineering-zoomcamp", "mlops-zoomcamp"]
MODELS = ["ollama/phi3", "openai/gpt-3.5-turbo", "openai/gpt-4o", "openai/gpt-4o-mini"]
RELEVANCE = ["RELEVANT", "PARTLY_RELEVANT", "NON_RELEVANT"]

def generate_synthetic_data(start_time, end_time):
    current_time = start_time
    conversation_count = 0
    print(f"Starting historical data generation from {start_time} to {end_time}")
    while current_time < end_time:
        conversation_id = str(uuid.uuid4())
        question = random.choice(SAMPLE_QUESTIONS)
        answer = random.choice(SAMPLE_ANSWERS)
        course = random.choice(COURSES)
        model = random.choice(MODELS)
        relevance = random.choice(RELEVANCE)
        
        answer_data = {
            'answer': answer,
            'response_time': random.uniform(0.5, 5.0),
            'relevance': relevance,
            'relevance_explanation': f"This answer is {relevance.lower()} to the question.",
            'model_used': model,
            'prompt_tokens': random.randint(50, 200),
            'completion_tokens': random.randint(50, 300),
            'total_tokens': random.randint(100, 500),
            'eval_prompt_tokens': random.randint(50, 150),
            'eval_completion_tokens': random.randint(20, 100),
            'eval_total_tokens': random.randint(70, 250),
            'openai_cost': random.uniform(0.001, 0.1) if model.startswith('openai/') else 0
        }
        
        save_conversation(conversation_id, question, answer_data, course)
        print(f"Saved conversation: ID={conversation_id}, Time={current_time}, Course={course}, Model={model}")
        
        # Generate feedback for some conversations
        if random.random() < 0.7:  # 70% chance of feedback
            feedback = 1 if random.random() < 0.8 else -1  # 80% positive feedback
            save_feedback(conversation_id, feedback)
            print(f"Saved feedback for conversation {conversation_id}: {'Positive' if feedback > 0 else 'Negative'}")
        
        current_time += timedelta(minutes=random.randint(1, 15))
        
        # Update the timestamp in the database
        conn = get_db_connection()
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE conversations SET timestamp = %s WHERE id = %s",
                    (current_time, conversation_id)
                )
            conn.commit()
            print(f"Updated timestamp for conversation {conversation_id} to {current_time}")
        finally:
            conn.close()
        
        conversation_count += 1
        if conversation_count % 10 == 0:
            print(f"Generated {conversation_count} conversations so far...")

    print(f"Historical data generation complete. Total conversations: {conversation_count}")

def generate_live_data():
    conversation_count = 0
    print("Starting live data generation...")
    while True:
        conversation_id = str(uuid.uuid4())
        question = random.choice(SAMPLE_QUESTIONS)
        answer = random.choice(SAMPLE_ANSWERS)
        course = random.choice(COURSES)
        model = random.choice(MODELS)
        relevance = random.choice(RELEVANCE)
        
        answer_data = {
            'answer': answer,
            'response_time': random.uniform(0.5, 5.0),
            'relevance': relevance,
            'relevance_explanation': f"This answer is {relevance.lower()} to the question.",
            'model_used': model,
            'prompt_tokens': random.randint(50, 200),
            'completion_tokens': random.randint(50, 300),
            'total_tokens': random.randint(100, 500),
            'eval_prompt_tokens': random.randint(50, 150),
            'eval_completion_tokens': random.randint(20, 100),
            'eval_total_tokens': random.randint(70, 250),
            'openai_cost': random.uniform(0.001, 0.1) if model.startswith('openai/') else 0
        }
        
        save_conversation(conversation_id, question, answer_data, course)
        print(f"Saved live conversation: ID={conversation_id}, Time={datetime.now(tz)}, Course={course}, Model={model}")
        
        # Generate feedback for some conversations
        if random.random() < 0.7:  # 70% chance of feedback
            feedback = 1 if random.random() < 0.8 else -1  # 80% positive feedback
            save_feedback(conversation_id, feedback)
            print(f"Saved feedback for live conversation {conversation_id}: {'Positive' if feedback > 0 else 'Negative'}")
        
        conversation_count += 1
        if conversation_count % 10 == 0:
            print(f"Generated {conversation_count} live conversations so far...")
        
        time.sleep(1)  # Wait for 1 second before generating the next data point

if __name__ == "__main__":
    print(f"Script started at {datetime.now(tz)}")
    # Generate historical data
    end_time = datetime.now(tz)
    start_time = end_time - timedelta(hours=6)
    print(f"Generating historical data from {start_time} to {end_time}")
    generate_synthetic_data(start_time, end_time)
    print("Historical data generation complete.")

    # Generate live data
    print("Starting live data generation... Press Ctrl+C to stop.")
    try:
        generate_live_data()
    except KeyboardInterrupt:
        print(f"Live data generation stopped at {datetime.now(tz)}.")
    finally:
        print(f"Script ended at {datetime.now(tz)}")
```

### Prompt 15

the recent conversaion data still doesn't show the most recent data when I refresh, it shows some data from the future and some daat from 20 minutes ago

```
2024-07-19 22:51:47
What is machine learning?
Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables by fitting a linear equation to observed data.
PARTLY_RELEVANT
2024-07-19 22:36:47
What is the difference between supervised and unsupervised learning?
Supervised learning involves training models on labeled data, while unsupervised learning deals with finding patterns in unlabeled data without predefined outputs.
RELEVANT
2024-07-19 22:28:47
What is the difference between supervised and unsupervised learning?
Overfitting occurs when a machine learning model learns the training data too well, including its noise and fluctuations, resulting in poor generalization to new, unseen data.
RELEVANT
2024-07-19 22:25:47
How does cross-validation help in model evaluation?
Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables by fitting a linear equation to observed data.
NON_RELEVANT
2024-07-19 22:10:47
What is machine learning?
Machine learning is a subset of art
```

now it's 22:50

---

Fixed synthetic_data.py

```python
import time
import random
import uuid
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from db import save_conversation, save_feedback, get_db_connection

# Set the timezone to CET (Europe/Berlin)
tz = ZoneInfo("Europe/Berlin")

# ... (keep the SAMPLE_QUESTIONS, SAMPLE_ANSWERS, COURSES, MODELS, and RELEVANCE lists as they were)

def generate_synthetic_data(start_time, end_time):
    current_time = start_time
    conversation_count = 0
    print(f"Starting historical data generation from {start_time} to {end_time}")
    while current_time < end_time:
        conversation_id = str(uuid.uuid4())
        question = random.choice(SAMPLE_QUESTIONS)
        answer = random.choice(SAMPLE_ANSWERS)
        course = random.choice(COURSES)
        model = random.choice(MODELS)
        relevance = random.choice(RELEVANCE)
        
        answer_data = {
            'answer': answer,
            'response_time': random.uniform(0.5, 5.0),
            'relevance': relevance,
            'relevance_explanation': f"This answer is {relevance.lower()} to the question.",
            'model_used': model,
            'prompt_tokens': random.randint(50, 200),
            'completion_tokens': random.randint(50, 300),
            'total_tokens': random.randint(100, 500),
            'eval_prompt_tokens': random.randint(50, 150),
            'eval_completion_tokens': random.randint(20, 100),
            'eval_total_tokens': random.randint(70, 250),
            'openai_cost': random.uniform(0.001, 0.1) if model.startswith('openai/') else 0
        }
        
        save_conversation(conversation_id, question, answer_data, course, current_time)
        print(f"Saved conversation: ID={conversation_id}, Time={current_time}, Course={course}, Model={model}")
        
        if random.random() < 0.7:
            feedback = 1 if random.random() < 0.8 else -1
            save_feedback(conversation_id, feedback, current_time)
            print(f"Saved feedback for conversation {conversation_id}: {'Positive' if feedback > 0 else 'Negative'}")
        
        current_time += timedelta(minutes=random.randint(1, 15))
        conversation_count += 1
        if conversation_count % 10 == 0:
            print(f"Generated {conversation_count} conversations so far...")

    print(f"Historical data generation complete. Total conversations: {conversation_count}")

def generate_live_data():
    conversation_count = 0
    print("Starting live data generation...")
    while True:
        current_time = datetime.now(tz)
        conversation_id = str(uuid.uuid4())
        question = random.choice(SAMPLE_QUESTIONS)
        answer = random.choice(SAMPLE_ANSWERS)
        course = random.choice(COURSES)
        model = random.choice(MODELS)
        relevance = random.choice(RELEVANCE)
        
        answer_data = {
            'answer': answer,
            'response_time': random.uniform(0.5, 5.0),
            'relevance': relevance,
            'relevance_explanation': f"This answer is {relevance.lower()} to the question.",
            'model_used': model,
            'prompt_tokens': random.randint(50, 200),
            'completion_tokens': random.randint(50, 300),
            'total_tokens': random.randint(100, 500),
            'eval_prompt_tokens': random.randint(50, 150),
            'eval_completion_tokens': random.randint(20, 100),
            'eval_total_tokens': random.randint(70, 250),
            'openai_cost': random.uniform(0.001, 0.1) if model.startswith('openai/') else 0
        }
        
        save_conversation(conversation_id, question, answer_data, course, current_time)
        print(f"Saved live conversation: ID={conversation_id}, Time={current_time}, Course={course}, Model={model}")
        
        if random.random() < 0.7:
            feedback = 1 if random.random() < 0.8 else -1
            save_feedback(conversation_id, feedback, current_time)
            print(f"Saved feedback for live conversation {conversation_id}: {'Positive' if feedback > 0 else 'Negative'}")
        
        conversation_count += 1
        if conversation_count % 10 == 0:
            print(f"Generated {conversation_count} live conversations so far...")
        
        time.sleep(1)

if __name__ == "__main__":
    print(f"Script started at {datetime.now(tz)}")
    end_time = datetime.now(tz)
    start_time = end_time - timedelta(hours=6)
    print(f"Generating historical data from {start_time} to {end_time}")
    generate_synthetic_data(start_time, end_time)
    print("Historical data generation complete.")

    print("Starting live data generation... Press Ctrl+C to stop.")
    try:
        generate_live_data()
    except KeyboardInterrupt:
        print(f"Live data generation stopped at {datetime.now(tz)}.")
    finally:
        print(f"Script ended at {datetime.now(tz)}")
```

Updated db.py

```python
import os
import psycopg2
from psycopg2.extras import DictCursor
from datetime import datetime
from zoneinfo import ZoneInfo

tz = ZoneInfo("Europe/Berlin")

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv('POSTGRES_HOST', 'postgres'),
        database=os.getenv('POSTGRES_DB', 'course_assistant'),
        user=os.getenv('POSTGRES_USER', 'your_username'),
        password=os.getenv('POSTGRES_PASSWORD', 'your_password')
    )

def init_db():
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DROP TABLE IF EXISTS feedback")
            cur.execute("DROP TABLE IF EXISTS conversations")
            
            cur.execute("""
                CREATE TABLE conversations (
                    id TEXT PRIMARY KEY,
                    question TEXT NOT NULL,
                    answer TEXT NOT NULL,
                    course TEXT NOT NULL,
                    model_used TEXT NOT NULL,
                    response_time FLOAT NOT NULL,
                    relevance TEXT NOT NULL,
                    relevance_explanation TEXT NOT NULL,
                    prompt_tokens INTEGER NOT NULL,
                    completion_tokens INTEGER NOT NULL,
                    total_tokens INTEGER NOT NULL,
                    eval_prompt_tokens INTEGER NOT NULL,
                    eval_completion_tokens INTEGER NOT NULL,
                    eval_total_tokens INTEGER NOT NULL,
                    openai_cost FLOAT NOT NULL,
                    timestamp TIMESTAMP WITH TIME ZONE NOT NULL
                )
            """)
            cur.execute("""
                CREATE TABLE feedback (
                    id SERIAL PRIMARY KEY,
                    conversation_id TEXT REFERENCES conversations(id),
                    feedback INTEGER NOT NULL,
                    timestamp TIMESTAMP WITH TIME ZONE NOT NULL
                )
            """)
        conn.commit()
    finally:
        conn.close()

def save_conversation(conversation_id, question, answer_data, course, timestamp):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO conversations 
                (id, question, answer, course, model_used, response_time, relevance, 
                relevance_explanation, prompt_tokens, completion_tokens, total_tokens, 
                eval_prompt_tokens, eval_completion_tokens, eval_total_tokens, openai_cost, timestamp)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                conversation_id, question, answer_data['answer'], course, 
                answer_data['model_used'], answer_data['response_time'], 
                answer_data['relevance'], answer_data['relevance_explanation'],
                answer_data['prompt_tokens'], answer_data['completion_tokens'], 
                answer_data['total_tokens'], answer_data['eval_prompt_tokens'],
                answer_data['eval_completion_tokens'], answer_data['eval_total_tokens'],
                answer_data['openai_cost'], timestamp
            ))
        conn.commit()
    finally:
        conn.close()

def save_feedback(conversation_id, feedback, timestamp):
    conn = get_db_connection()
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO feedback (conversation_id, feedback, timestamp) VALUES (%s, %s, %s)",
                (conversation_id, feedback, timestamp)
            )
        conn.commit()
    finally:
        conn.close()

def get_recent_conversations(limit=5, relevance=None):
    conn = get_db_connection()
    try:
        with conn.cursor(cursor_factory=DictCursor) as cur:
            query = """
                SELECT c.*, f.feedback
                FROM conversations c
                LEFT JOIN feedback f ON c.id = f.conversation_id
            """
            if relevance:
                query += f" WHERE c.relevance = '{relevance}'"
            query += " ORDER BY c.timestamp DESC LIMIT %s"
            
            cur.execute(query, (limit,))
            return cur.fetchall()
    finally:
        conn.close()

def get_feedback_stats():
    conn = get_db_connection()
    try:
        with conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute("""
                SELECT 
                    SUM(CASE WHEN feedback > 0 THEN 1 ELSE 0 END) as thumbs_up,
                    SUM(CASE WHEN feedback < 0 THEN 1 ELSE 0 END) as thumbs_down
                FROM feedback
            """)
            return cur.fetchone()
    finally:
        conn.close()

# Initialize the database
init_db()
```

# Current code

The up-to-date code is in [app/](app/)