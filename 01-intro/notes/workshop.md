# Introduction to RAG

This workshop is the first module of the
[LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp) -
a free course about building LLM applications.

In this hands-on session, you'll build a working Retrieval-Augmented
Generation (RAG) system from scratch, step by step. No frameworks, no
magic - just Python, a search index, and an LLM.

If you want the full course (agents, vector search, evaluation,
monitoring, capstone project), check
[the repo](https://github.com/DataTalksClub/llm-zoomcamp).

To see my other tutorials, check [AI Shipping Labs](https://aishippinglabs.com/) - a community of AI Builders.

Places where you can find me:

- Alexey On Data substack: https://alexeyondata.substack.com/
- LinkedIn: https://www.linkedin.com/in/agrigorev/
- X: https://x.com/Al_Grigor


## Introduction

Large Language Models (LLMs) are powerful, but they have limitations:

- They don't know about your private data.
- Their training data has a cutoff date.
- They sometimes hallucinate - make things up that sound plausible.

RAG solves these problems by giving the LLM relevant documents at
question time. Instead of hoping the model memorized the answer, we
retrieve the right information and hand it to the LLM to generate
a grounded response.

In this workshop, we will:

- Understand what RAG is and how it works
- Build a search engine over a real FAQ dataset
- Write a prompt that combines the user's question with search results
- Wire it all together into a working RAG pipeline
- Swap the search backend from an in-memory index to a persistent one
- Discuss what comes next (agents, vector search, Elasticsearch)


## Prerequisites

- Python (3.13 or later)
- An [OpenAI account](https://openai.com/) or alternative
- Basic familiarity with Python and the command line


## Environment

For this workshop, all you need is Python with Jupyter.

I use GitHub Codespaces to run it, but you can use whatever
environment you like.

### Setting up Github Codespaces

GitHub Codespaces is the recommended environment for this workshop.

But you can use any other environment with Jupyter Notebook.
If you want to do it on your laptop, that's perfectly fine.

- Open this repository in GitHub Codespaces, or copy the
  `01-intro` folder into your own repository
- Add the OpenAI key:
    - Go to Settings -> Secrets and Variables (under Security) -> Codespaces
    - Click "New repository secret"
    - Name: `OPENAI_API_KEY`, Secret: your key
    - Click "Add secret"
- Create a codespace
    - Click "Code"
    - Select the "Codespaces" tab
    - "Create codespace on main"

In case you use it on your laptop, set the API key before you start
Jupyter:

```bash
export OPENAI_API_KEY='YOUR_KEY'
```

### Workshop files

This folder contains the code we'll write during the workshop:

- `notebook.py` - the follow-along version, split into notebook
  cells with `# %%`. Copy each cell into Jupyter as we go, or open
  it directly in VS Code/Jupyter.

During the live workshop, we'll write the code ourselves. The files
are here so the workshop is still useful stand-alone after the
session.

### Installing required libraries

Install the dependencies:

```bash
cd 01-intro
uv sync
```

Start Jupyter:

```bash
uv run jupyter notebook
```

Open Jupyter, create a notebook, and copy the cells from
`notebook.py` as we go. Check that the OpenAI client works:

```python
from openai import OpenAI
openai_client = OpenAI()
```

For Groq or other OpenAI-compatible providers:

```python
from openai import OpenAI
import os

openai_client = OpenAI(
    api_key=os.getenv('GROQ_API_KEY'),
    base_url='https://api.groq.com/openai/v1'
)
```

If you see an error, make sure you set the key correctly.


## The use case: Course FAQ

Throughout this workshop, our knowledge base is the
[DataTalks.Club FAQ](https://datatalks.club/faq) - a collection of
questions and answers from our Zoomcamp courses (machine learning,
data engineering, MLOps, LLM).

The dataset is available as JSON. Each entry looks like this:

```json
{
  "course": "machine-learning-zoomcamp",
  "course_name": "ML Zoomcamp",
  "section": "Module 1: Introduction",
  "question": "How do I install Python?",
  "answer": "Download it from python.org..."
}
```

We'll build a RAG system that can answer questions about these
courses by searching the FAQ and feeding the results to an LLM.


## Part 1: What is RAG?

### Large Language Models

A Large Language Model (LLM) is a neural network trained on massive
amounts of text. Given a prompt, it generates a continuation - a
plausible next piece of text.

You've probably used ChatGPT, which is powered by GPT-4o. Other
popular models include Claude, Gemini, and Llama.

LLMs are good at:

- Answering general knowledge questions
- Summarizing, translating, and rewriting text
- Writing code
- Following instructions

But they have important limitations:

- Knowledge cutoff: they only know what was in their training data.
  If you ask about something that happened after training, they won't
  know - or worse, they'll make something up.
- No access to your data: they can't see your documents, databases,
  or internal systems unless you provide that information.
- Hallucinations: they sometimes produce confident-sounding answers
  that are simply wrong.

### The RAG idea

RAG (Retrieval-Augmented Generation) is a simple but powerful idea:
instead of hoping the LLM knows the answer, we give it the answer
by attaching relevant documents to the prompt.

The flow:

1. The user asks a question.
2. We search our knowledge base for documents relevant to the question.
3. We build a prompt that includes the question and the retrieved documents.
4. We send the prompt to the LLM, which generates an answer based
   on the documents we provided.

In code, it looks like this:

```python
def rag(question):
    search_results = search(question)
    user_prompt = build_prompt(question, search_results)
    return llm(user_prompt)
```

That's the entire architecture. Three components: search, prompt, LLM.

The key insight: the LLM only sees the documents we hand it. So its
answers are grounded in our data. If the right document is retrieved,
the answer is good. If it's not, the answer suffers. Search quality
is the backbone of RAG.

### RAG vs fine-tuning

A common question: why not fine-tune the model on our data instead?

Fine-tuning changes the model's behavior (how it responds, what
style it uses), but it's not great for injecting knowledge. You'd
need to retrain every time your data changes.

RAG keeps the model frozen and brings fresh data to it at query time.
It's simpler, cheaper, and always up-to-date.

In practice, they complement each other - fine-tune for style, RAG
for knowledge.


## Part 2: Preparing the Dataset with minsearch

### Fetching the data

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

### Understanding the data

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

### Indexing with minsearch

[minsearch](https://github.com/alexeygrigorev/minsearch) is a simple
in-memory search engine. It uses TF-IDF for text fields and supports
exact-match filtering on keyword fields.

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

### Trying a search

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

### Filtering by course

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

### Boosting fields

Not all fields are equally important. The `question` field is usually
more relevant than `section` for matching. minsearch supports field
boosting:

```python
results = index.search(
    query="How do I run Docker on Windows?",
    num_results=5,
    boost_dict={"question": 3.0, "section": 0.5}
)
```

Here we boost `question` by 3x (it counts three times as much) and
de-boost `section` by 0.5x. This gives more weight to documents
where the query matches the question text.

Try different boost values and see how the results change.

### Wrapping it in a function

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
entries. We'll use this in Part 4 when we wire everything together.


## Part 3: Building the Prompt

The LLM doesn't see our documents unless we pass them in. So we need
to build a prompt that includes the user's question and the search
results.

### Prompt template

A good RAG prompt has two parts:

1. Instructions - tell the LLM how to behave
2. Context - the retrieved documents + the user's question

Let's define both:

```python
PROMPT_TEMPLATE = """
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT:
{context}
""".strip()
```

The prompt tells the LLM to only use information from the CONTEXT.
This is what grounds the answer in our data and reduces hallucinations.

### Building the context

The `context` is a formatted string with all the search results:

```python
def build_context(search_results):
    context = ""
    for doc in search_results:
        context += f"section: {doc['section']}\n"
        context += f"question: {doc['question']}\n"
        context += f"answer: {doc['answer']}\n"
        context += "\n"
    return context.strip()
```

Each document becomes a block with the section, question, and answer.
This format makes it easy for the LLM to read.

### Putting it together

Now the `build_prompt` function combines the template with the search
results:

```python
def build_prompt(query, search_results):
    context = build_context(search_results)
    return PROMPT_TEMPLATE.format(question=query, context=context)
```

Let's try it:

```python
query = "How do I run Docker on Windows?"
search_results = search(query)
prompt = build_prompt(query, search_results)

print(prompt)
```

You should see a prompt with the question at the top and several
FAQ entries below it. This is exactly what we'll send to the LLM.

The prompt looks something like:

```
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: How do I run Docker on Windows?

CONTEXT:
section: Module 5: Monitoring
question: How can I remove all Docker containers, images, and volumes, and builds from the terminal?
answer: 1. Delete all containers (including running ones): ...

section: ...
question: ...
answer: ...
```

### Why the prompt matters

The prompt is the bridge between search and the LLM. A bad prompt
means the LLM ignores the context and hallucinates. A good prompt
keeps the answer grounded.

Key principles:

- Be explicit: tell the LLM to use only the provided context.
- Be structured: format the context clearly so the LLM can parse it.
- Be concise: don't pad the prompt with unnecessary instructions.

We'll keep this prompt simple. In a real system you might add more
instructions, but the structure stays the same.


## Part 4: Doing RAG

Now we have all three components. Let's wire them together.

### The LLM function

First, the `llm` function. It takes a prompt and sends it to the
OpenAI API:

```python
from openai import OpenAI

openai_client = OpenAI()

def llm(prompt, model="gpt-4o-mini"):
    response = openai_client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
```

Test it with a simple prompt:

```python
llm("What is 2 + 2?")
```

If you get an error, check your API key.

We're using the chat completions API with a single user message. The
`model` parameter defaults to `gpt-4o-mini` which is cheap and fast.
You can use any model you like.

### The full RAG pipeline

Now put it all together:

```python
def rag(query, model="gpt-4o-mini"):
    search_results = search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(prompt, model=model)
    return answer
```

This is the same three-line function we saw in Part 1. Now it's real.

Try it:

```python
query = "How do I run Docker on Windows?"
answer = rag(query)
print(answer)
```

The answer should be based on the FAQ documents - not on the LLM's
general knowledge. The LLM read the search results and generated a
response grounded in our data.

### Try more questions

```python
rag("Can I still join the course after it started?")
```

```python
rag("How do I get a certificate?")
```

```python
rag("What's the best way to store API keys?")
```

Notice how the answers reference specific courses and sections.
That's RAG in action - the LLM is reading from our knowledge base.

### What happens without RAG?

For comparison, let's ask the LLM the same question without the
search results:

```python
llm("Can I still join the course after it started?")
```

The answer will be generic - the LLM doesn't know about our specific
courses. With RAG, it answers based on real FAQ data.

This is the core difference: without RAG the LLM relies on its
training data (which doesn't include our courses). With RAG, it
reads from our knowledge base and gives a specific, correct answer.

### The complete pipeline

Let's review the full code we've written so far:

```python
import requests
from minsearch import Index
from openai import OpenAI

# --- Data ---

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

# --- Search ---

index = Index(
    text_fields=["question", "section", "answer"],
    keyword_fields=["course"]
)
index.fit(documents)

def search(query, num_results=5):
    boost_dict = {"question": 3.0, "section": 0.5}
    return index.search(
        query,
        num_results=num_results,
        boost_dict=boost_dict
    )

# --- Prompt ---

PROMPT_TEMPLATE = """
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT:
{context}
""".strip()

def build_context(search_results):
    context = ""
    for doc in search_results:
        context += f"section: {doc['section']}\n"
        context += f"question: {doc['question']}\n"
        context += f"answer: {doc['answer']}\n"
        context += "\n"
    return context.strip()

def build_prompt(query, search_results):
    context = build_context(search_results)
    return PROMPT_TEMPLATE.format(question=query, context=context)

# --- LLM ---

openai_client = OpenAI()

def llm(prompt, model="gpt-4o-mini"):
    response = openai_client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# --- RAG ---

def rag(query, model="gpt-4o-mini"):
    search_results = search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(prompt, model=model)
    return answer
```

That's a complete RAG system in about 60 lines of Python. No
frameworks, no vector databases, no embedding models. Just search,
prompt, and LLM.

The three components are independent and replaceable:

- Swap `search` for a different backend (Elasticsearch, vector search)
- Swap `build_prompt` for a different prompt template
- Swap `llm` for a different model or provider

This modularity is what makes RAG so flexible.


## Part 5: Data Ingestion

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

### The ingestion script

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

### The query process

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

### Filtering and boosting

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

### RAG with sqlitesearch

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

### Comparing the two approaches

Let's compare the two architectures:

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

### When to use what

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

### Cleaning up

When you're done, close the database connection:

```python
sqlite_index.close()
```

Or just let Python clean it up when the notebook kernel shuts down.


## Part 6: What Comes Next

We built a working RAG system. But this is just the beginning. Here's
what you'd explore next to make it production-ready.

### Vector search

Our search uses TF-IDF/BM25 - keyword-based matching. If the user
asks "How do I deploy my model?" but the FAQ says "serving
predictions in production", keyword search might miss it because the
words don't overlap.

Vector search (also called semantic search) solves this by encoding
the meaning of the text into vectors (arrays of numbers). Questions
and answers with similar meaning end up close together in vector
space, even if they use different words.

How it works:

- An embedding model (like OpenAI's `text-embedding-3-small` or
  open-source models from Sentence Transformers) converts each
  document into a vector.
- The user's question is also converted to a vector.
- We find the documents whose vectors are closest to the question
  vector (using cosine similarity or dot product).
- The closest documents are the search results.

You store the vectors in a vector database (Qdrant, Weaviate, Milvus,
Pinecone) and query with the vector of the user's question.

In the LLM Zoomcamp, Module 3 covers vector search in detail.

### Elasticsearch

Elasticsearch is the industry standard for text search. It supports:

- Full-text search with BM25
- Filtering, aggregations, and faceting
- Vector search (dense and sparse)
- Distributed scaling
- Real-time indexing

It's heavier than sqlitesearch but handles production workloads at
scale. If you're building a real RAG system, Elasticsearch (or
OpenSearch) is a common choice for the search backend.

In the LLM Zoomcamp, we cover Elasticsearch in the supplementary
materials for Module 1.

### Agents

In our RAG pipeline, the flow is fixed: search once, then generate.
But sometimes one search isn't enough. The user's question might be
ambiguous, or the first search might return irrelevant results.

An agent puts the LLM in the driver's seat. Instead of a fixed
pipeline, the LLM decides what to do:

- It can search multiple times with different queries.
- It can open and read specific documents.
- It can decide when it has enough information to answer.
- It can use multiple tools (search, database lookup, API calls).

The key shift: from a hardcoded pipeline to an LLM that chooses
what to do next based on what it sees.

In the LLM Zoomcamp, Module 2 covers agents in detail.

### Evaluation

How do you know if your RAG system is good? You need to measure:

- Retrieval quality: Is the right document in the top results?
  Metrics like hit rate and MRR (Mean Reciprocal Rank) answer this.
- Generation quality: Is the answer correct and grounded in the
  documents? LLM-as-judge evaluation can help.
- End-to-end quality: Does the full pipeline produce good answers?

Without evaluation, you're flying blind. Any change you make to the
search, the prompt, or the model could make things worse without you
knowing.

In the LLM Zoomcamp, Module 4 covers evaluation in detail.

### Monitoring

Once your RAG system is live, you need to track:

- How many questions it answers
- User feedback (thumbs up/down)
- Retrieval quality over time (is the index getting stale?)
- LLM cost and latency

Monitoring helps you catch issues before users complain and guides
where to invest in improvements.

In the LLM Zoomcamp, Module 5 covers monitoring in detail.


## Summary

In this workshop, we:

- Learned what RAG is and why it matters: retrieve documents, build a
  prompt, let the LLM generate a grounded answer
- Built a search engine over a real FAQ dataset using minsearch
- Created a prompt template that combines the user's question with
  search results
- Wired search + prompt + LLM into a working RAG pipeline
- Split ingestion and query into separate processes with sqlitesearch
- Discussed what comes next: vector search, Elasticsearch, agents,
  evaluation, and monitoring

You now have a working RAG system and a clear mental model for how
each piece fits together. The rest is making each piece better.


## Next Steps

- Try different prompts and see how the answers change
- Add more data sources to the knowledge base
- Experiment with different LLM models (GPT-4o, Claude, Gemini, local
  models via Ollama)
- Implement vector search with embeddings
- Try Elasticsearch as a search backend
- Build an agent that can search multiple times

For the full course with structured exercises, code, homework, and a
capstone project, see
[LLM Zoomcamp](https://github.com/DataTalksClub/llm-zoomcamp).
