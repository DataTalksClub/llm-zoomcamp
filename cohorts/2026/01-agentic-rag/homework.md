## Homework: Agentic RAG

In this homework, we build a RAG system from scratch and then make it
agentic — the same path as the module.

Instead of the course FAQ, our knowledge base is the course lessons
themselves.

The course repository is organized by module. Each module is a top-level
folder with a `lessons/` subfolder of numbered markdown pages:

```
01-agentic-rag/
└── lessons/
    ├── 01-intro.md
    ├── 02-environment.md
    ├── ...
    └── 16-other-frameworks.md
```

There are seven modules:

- `01-agentic-rag`
- `02-vector-search`
- `03-orchestration`
- `04-evaluation`
- `05-monitoring`
- `06-best-practices`
- `07-project-example`

Each lesson page is a single markdown file. These pages are exactly what you
read as you go through the course.

We'll fetch this data from GitHub and use it as the knowledge base for our
RAG system.

> It's possible your answers won't match exactly. If so, select the closest one.

## Setup

Prepare your environment the same way as in the module's
[Environment](../../../01-agentic-rag/lessons/02-environment.md) lesson.

This homework needs one extra library: `gitsource`, which downloads files
from a GitHub repository.

Install it:

```bash
uv add gitsource
```

## Preparation

This step isn't scored — it just gets the data ready.

We pull the lesson pages straight from the course repository, pinned to a
fixed commit so everyone works with the exact same data:

```python
from gitsource import GithubRepositoryDataReader

reader = GithubRepositoryDataReader(
    repo_owner="DataTalksClub",
    repo_name="llm-zoomcamp",
    commit_id="8c1834d",
    allowed_extensions={"md"},
    filename_filter=lambda path: "/lessons/" in path,
)

files = reader.read()
```

`GithubRepositoryDataReader` downloads the whole repository (as a zip, no
git required) and goes over all the files in it. With
`allowed_extensions={"md"}` it keeps only the markdown files.

We also pass a `filename_filter` so we don't grab every markdown file in the
repo — the top-level README, module READMEs, notes under `cohorts/`, and so
on. The lesson pages all live under a module's `lessons/` folder, so
filtering on `/lessons/` keeps just those.

`commit_id="8c1834d"` pins the download to one exact commit, so the data
doesn't change under us and everyone gets the same answers.

Each file has a `parse()` method that returns a dictionary with its
`filename` and `content`. That's all we need — we search over the `content`
and use the `filename` to tell the lessons apart:

```python
documents = []

for file in files:
    doc = file.parse()
    documents.append(doc)
```

## Q1. How many lesson pages

How many lesson pages are in the dataset?

* 24
* 72
* 200
* 600

## Q2. Indexing and searching

Index the documents with minsearch — make `content` a text field and
`filename` a keyword field. Then search with this query:

> How does the agentic loop keep calling the model until it stops?

What's the `filename` of the first result?

* `01-agentic-rag/lessons/03-rag.md`
* `01-agentic-rag/lessons/14-agentic-loop.md`
* `04-evaluation/lessons/13-llm-as-judge.md`
* `06-best-practices/lessons/02-hybrid-search.md`

## Q3. RAG without chunking

Now let's answer the query, not just retrieve. Instead of building the
prompt by hand, reuse the `rag_helper.py` we wrote in the module (the
`RAGBase` class):

```bash
wget https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/01-agentic-rag/code/rag_helper.py
```

`RAGBase` was written for the FAQ schema (`section`/`question`/`answer`),
while our documents have `filename` and `content`. So either implement the
RAG flow yourself, or take `RAGBase` and change the parts that assume the
FAQ schema — `search` (to use our index) and `build_context` (to format each
result as its `filename` followed by its `content`).

Build a RAG over the index from Q2 and answer the query:

> How does the agentic loop keep calling the model until it stops?

To find the cost you also need the token usage, but the helper hides it —
`llm` returns only the text and `rag` only the answer. So change the code a
bit more: have `llm` return the raw response, and have `rag` return both the
answer and the usage (a small result object works well).

gpt-5.4-mini costs $0.75 per 1M input tokens and $4.50 per 1M output tokens.
What's the cost of answering this query without chunking?

> Note: the output length varies between runs, so the exact cost differs a
> little each time — pick the closest option.

* $0.0006
* $0.006
* $0.06
* $0.6

## Q4. Chunking

The lesson pages are long — some are thousands of characters. Long documents
make retrieval less precise: a match deep inside a page still pulls in the
whole page. A common fix is chunking: split each page into smaller,
overlapping pieces and index those instead.

gitsource has a helper for this. `chunk_documents` slides a fixed-size
window over each document's `content` field and emits one chunk per window:

```python
from gitsource import chunk_documents

chunks = chunk_documents(documents, size=2000, step=1000)
```

What it does (you can see the implementation
[here](https://github.com/alexeygrigorev/gitsource/blob/main/gitsource/chunking.py)):

- It walks the text from the start, taking `size` characters at a time.
- After each chunk it advances by `step` characters, not by `size`. With
  `size=2000` and `step=1000` each chunk overlaps the previous one by 1000
  characters, so a passage split across a boundary still appears whole in
  one of the chunks.
- Every chunk keeps the original fields (`filename`) and adds `start` (the
  offset in the page) and `content` (the chunk text).

How many chunks do you get?

* 70
* 295
* 1100
* 4500

## Q5. RAG with chunking

Chunking makes each answer cheaper, because we send a smaller context to the
LLM. Let's measure that.

Index the chunks from Q4 (same as before: `content` as a text field,
`filename` as a keyword field), point your RAG at the chunk index, and
answer the same query again — computing the cost the same way as in Q3.

About how many times cheaper is the chunked version than Q3?

> Note: the output length varies between runs, so the exact ratio differs a
> little each time — pick the closest option.

* about the same
* 3× cheaper
* 10× cheaper
* 30× cheaper

## Q6. Turning it into an agent

So far search runs once, with the exact query. Let's make it agentic: give
the LLM a `search` tool and let it decide when (and what) to search. We'll
use [toyaikit](https://github.com/alexeygrigorev/toyaikit), the small agent
library from the module:

```bash
uv add toyaikit
```

Write a `search` function over the chunk index, and give it a type hint and
a docstring — toyaikit reads them to build the tool schema for you, so you
don't have to write the JSON by hand:

```python
def search(query: str) -> list[dict]:
    """
    Search the course lessons for entries matching the query.
    """
    return chunk_index.search(query, num_results=5)
```

Register it and look at the schema toyaikit generated:

```python
from toyaikit.tools import Tools

agent_tools = Tools()
agent_tools.add_tool(search)

agent_tools.get_tools()
```

What is the parameter name in the generated tool schema?

* `query`
* `question`
* `text`
* `input`

## Submit the results

* Submit your results here: https://courses.datatalks.club/llm-zoomcamp-2026/hw1
* It's possible your answers won't match exactly. If so, select the closest one.
