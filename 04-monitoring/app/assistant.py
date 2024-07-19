import os

from openai import OpenAI

from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer


ELASTIC_URL = os.getenv("ELASTIC_URL", "http://elasticsearch:9200")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://ollama:11434/v1/")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-api-key-here")


es_client = Elasticsearch(ELASTIC_URL)
ollama_client = OpenAI(base_url=OLLAMA_URL, api_key="ollama")
openai_client = OpenAI(api_key=OPENAI_API_KEY)

model = SentenceTransformer("multi-qa-MiniLM-L6-cos-v1")


def elastic_search_text(query, course, index_name="course-questions"):
    search_query = {
        "size": 5,
        "query": {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": query,
                        "fields": ["question^3", "text", "section"],
                        "type": "best_fields",
                    }
                },
                "filter": {"term": {"course": course}},
            }
        },
    }

    response = es_client.search(index=index_name, body=search_query)
    return [hit["_source"] for hit in response["hits"]["hits"]]


def elastic_search_knn(field, vector, course, index_name="course-questions"):
    knn = {
        "field": field,
        "query_vector": vector,
        "k": 5,
        "num_candidates": 10000,
        "filter": {"term": {"course": course}},
    }

    search_query = {
        "knn": knn,
        "_source": ["text", "section", "question", "course", "id"],
    }

    es_results = es_client.search(index=index_name, body=search_query)

    return [hit["_source"] for hit in es_results["hits"]["hits"]]


def build_prompt(query, search_results):
    prompt_template = """
You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT: 
{context}
""".strip()

    context = "\n\n".join(
        [
            f"section: {doc['section']}\nquestion: {doc['question']}\nanswer: {doc['text']}"
            for doc in search_results
        ]
    )
    return prompt_template.format(question=query, context=context).strip()


def llm(prompt, model_choice):
    if model_choice == "ollama":
        response = ollama_client.chat.completions.create(
            model="phi3", messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    elif model_choice == "openai":
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content


def get_answer(query, course, model_choice, search_type):
    if search_type == "vector":
        vector = model.encode(query)
        search_results = elastic_search_knn("question_text_vector", vector, course)
    else:
        search_results = elastic_search_text(query, course)

    prompt = build_prompt(query, search_results)
    answer = llm(prompt, model_choice)
    return answer
