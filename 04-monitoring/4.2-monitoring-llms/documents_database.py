import logging
import json
from tqdm.auto import tqdm
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer
from datetime import datetime
from utils.llm_utils import ask_llm, build_prompt

logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)


def setup_es_client_and_index(index_name: str) -> Elasticsearch:
    logging.info(f"Setup Elastic Search client and index {index_name}")
    es_client = Elasticsearch("http://documents-db:9200")

    index_settings = {
        "settings": {
            "number_of_shards": 1,
            "number_of_replicas": 0
        },
        "mappings": {
            "properties": {
                "timestamp": {"type": "date"},
                "text": {"type": "text"},
                "section": {"type": "text"},
                "question": {"type": "text"},
                "course": {"type": "keyword"},
                "id": {"type": "keyword"},
                "text_vector": {
                    "type": "dense_vector",
                    "dims": 384,
                    "index": True,
                    "similarity": "cosine"
                },
                "llm_answer": {"type": "text"},
                "llm_answer_vector": {
                    "type": "dense_vector",
                    "dims": 384,
                    "index": True,
                    "similarity": "cosine"
                }
            }
        }
    }

    if not es_client.indices.exists(index=index_name):
        es_client.indices.create(index=index_name, body=index_settings)
        logging.info(f"Created new index '{index_name}'.")
    else:
        logging.info(f"Index '{index_name}' already exists.")

    return es_client


def dump_doc_embeddings_to_db(es_client: Elasticsearch, index_name: str):
    logging.info(f"Storing documents in Elastic Search index {index_name}")
    with open('documents-with-ids.json', 'rt') as f_in:
        documents = json.load(f_in)

    model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')
    for doc in tqdm(documents):
        if doc["course"] == "data-engineering-zoomcamp":
            doc["text_vector"] = model.encode(doc["text"])
            doc["timestamp"] = datetime.now()
            es_client.index(index=index_name, document=doc)


def elastic_search_fields(es_client: Elasticsearch, index_name: str, search_query: dict) -> dict:
    result = es_client.search(
        index=index_name,
        body=search_query
    )
    source = [doc for doc in result['hits']['hits']]
    return source


def extend_ground_truth_dataset(es_client: Elasticsearch, index_name: str):
    logging.info(f"Extending documents ground truth with llm answer.")
    with open('documents-with-ids.json', 'rt') as f_in:
        docs = json.load(f_in)
    model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')

    for doc in tqdm(docs):
        # retrieve context data based on question and text vector embedding from elastic search
        question_vector = model.encode(doc["question"])
        text_results = elastic_search_fields(es_client, index_name, {
            "knn": {
                "field": "text_vector",
                "query_vector": question_vector,
                "k": 3,
                "num_candidates": 1000,
                "filter": {"term": {"course": "data-engineering-zoomcamp"}}
            },
            "_source": ["text"]
        })
        contexts = [result["_source"]["text"] for result in text_results]

        # generate llm answer and store in elastic search
        prompt = build_prompt(doc["question"], contexts)
        llm_answer = ask_llm(
            "gpt-3.5-turbo-0125", [{"role": "user", "content": prompt}], mock_answer=False
        )
        llm_answer_vector = model.encode(llm_answer)
        result = elastic_search_fields(es_client, index_name, {
            "query": {"match": {"id": doc["id"]}}}
        )
        es_client.update(
            index=index_name,
            id=result[0]["_id"],
            doc={
                "llm_answer_vector": llm_answer_vector,
                "llm_answer": llm_answer
            }
        )
