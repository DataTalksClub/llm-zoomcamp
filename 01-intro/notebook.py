# %%
# Follow-along code for "Introduction to RAG" workshop.
#
# This file is intentionally written like a notebook. During the workshop,
# copy each cell into Jupyter and run it in order.

# %%
# Setup

import os

from openai import OpenAI

MODEL_NAME = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
openai_client = OpenAI()

# %%
# Part 2: Fetch the FAQ data

import requests

docs_url = 'https://datatalks.club/faq/json/courses.json'
response = requests.get(docs_url)
courses_raw = response.json()

courses_raw[:3]

# %%
# Part 2: Fetch all FAQ documents from all courses

documents = []

for course in courses_raw:
    course_url = f'https://datatalks.club/faq{course["path"]}'
    course_response = requests.get(course_url)
    course_data = course_response.json()

    for doc in course_data:
        doc['course_name'] = course['course_name']
        documents.append(doc)

len(documents)

# %%
# Part 2: Look at a document

documents[0]

# %%
# Part 2: Check documents per course

from collections import Counter

course_counts = Counter(doc['course'] for doc in documents)
course_counts

# %%
# Part 2: Build a minsearch index

from minsearch import Index

index = Index(
    text_fields=["question", "section", "answer"],
    keyword_fields=["course"]
)

index.fit(documents)

# %%
# Part 2: Try a search

query = "How do I run Docker on Windows?"
results = index.search(query, num_results=5)

results[0]

# %%
# Part 2: See all questions from results

[doc['question'] for doc in results]

# %%
# Part 2: Filter by course

results = index.search(
    query="How do I run Docker on Windows?",
    num_results=5,
    filter_dict={"course": "mlops-zoomcamp"}
)

[doc['question'] for doc in results]

# %%
# Part 2: Boost fields

results = index.search(
    query="How do I run Docker on Windows?",
    num_results=5,
    boost_dict={"question": 3.0, "section": 0.5}
)

[doc['question'] for doc in results]

# %%
# Part 2: Wrap in a search function


def search(query, num_results=5):
    boost_dict = {"question": 3.0, "section": 0.5}
    return index.search(
        query,
        num_results=num_results,
        boost_dict=boost_dict
    )


# %%
# Part 3: Define the prompt template

PROMPT_TEMPLATE = """
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT:
{context}
""".strip()

# %%
# Part 3: Build the context


def build_context(search_results):
    context = ""
    for doc in search_results:
        context += f"section: {doc['section']}\n"
        context += f"question: {doc['question']}\n"
        context += f"answer: {doc['answer']}\n"
        context += "\n"
    return context.strip()

# %%
# Part 3: Build the prompt


def build_prompt(query, search_results):
    context = build_context(search_results)
    return PROMPT_TEMPLATE.format(question=query, context=context)


# %%
# Part 3: Try building a prompt

query = "How do I run Docker on Windows?"
search_results = search(query)
prompt = build_prompt(query, search_results)

print(prompt)

# %%
# Part 4: Define the LLM function


def llm(prompt, model=MODEL_NAME):
    response = openai_client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


# %%
# Part 4: Test the LLM

# llm("What is 2 + 2?")

# %%
# Part 4: The full RAG pipeline


def rag(query, model=MODEL_NAME):
    search_results = search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(prompt, model=model)
    return answer


# %%
# Part 4: Try RAG

# query = "How do I run Docker on Windows?"
# answer = rag(query)
# print(answer)

# %%
# Part 4: Try more questions

# rag("Can I still join the course after it started?")

# %%
# rag("How do I get a certificate?")

# %%
# rag("What's the best way to store API keys?")

# %%
# Part 4: Without RAG (for comparison)

# llm("Can I still join the course after it started?")

# %%
# Part 5: Data Ingestion - run the ingestion script first
#
#   uv run python ingest.py
#
# This creates faq.db with the indexed documents.
# After that, we can query it from a separate process.

# %%
# Part 5: Connect to the existing index (no fit needed)

from sqlitesearch import TextSearchIndex

sqlite_index = TextSearchIndex(
    text_fields=["question", "section", "answer"],
    keyword_fields=["course"],
    id_field="id",
    db_path="faq.db"
)

# %%
# Part 5: Try sqlitesearch

query = "How do I run Docker on Windows?"
results = sqlite_index.search(query, num_results=5)

results[0]

# %%
# Part 5: All questions from sqlitesearch results

[doc['question'] for doc in results]

# %%
# Part 5: Filter by course

results = sqlite_index.search(
    query="How do I run Docker on Windows?",
    num_results=5,
    filter_dict={"course": "mlops-zoomcamp"}
)

[doc['question'] for doc in results]

# %%
# Part 5: Boost fields

results = sqlite_index.search(
    query="How do I run Docker on Windows?",
    num_results=5,
    boost_dict={"question": 3.0, "section": 0.5}
)

[doc['question'] for doc in results]

# %%
# Part 5: Wrap sqlitesearch in a search function


def sqlite_search(query, num_results=5):
    boost_dict = {"question": 3.0, "section": 0.5}
    return sqlite_index.search(
        query,
        num_results=num_results,
        boost_dict=boost_dict
    )


# %%
# Part 5: RAG with sqlitesearch


def rag_sqlite(query, model=MODEL_NAME):
    search_results = sqlite_search(query)
    prompt = build_prompt(query, search_results)
    answer = llm(prompt, model=model)
    return answer


# %%
# Part 5: Try sqlitesearch RAG

# query = "How do I run Docker on Windows?"
# answer = rag_sqlite(query)
# print(answer)

# %%
# Part 5: Clean up

sqlite_index.close()
