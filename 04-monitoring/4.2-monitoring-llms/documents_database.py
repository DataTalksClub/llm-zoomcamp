import json
from tqdm.auto import tqdm
from elasticsearch import Elasticsearch
import pandas as pd
from sentence_transformers import SentenceTransformer
import logging
from datetime import datetime
from utils.llm_utils import ask_llm, build_prompt


def setup_es_client_and_index(index_name: str) -> Elasticsearch:
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
                },
                "cosine_similarity_text_llm_answer": {"type": "double"},
                "negative_llm_answer": {"type": "keyword"},
                "llm_as_a_judge": {"type": "keyword"}
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


def elastic_search_knn(field: str, vector, course: str, es_client: Elasticsearch, index_name: str) -> list:
    knn = {
        "field": field,
        "query_vector": vector,
        "k": 3,
        "num_candidates": 1000,
        "filter": {"term": {"course": course}}
    }

    search_query = {
        "knn": knn,
        "_source": ["text"]
    }

    es_results = es_client.search(
        index=index_name,
        body=search_query
    )

    result_docs = []

    for hit in tqdm(es_results['hits']['hits']):
        result_docs.append(hit['_source'])

    return result_docs


def extend_ground_truth_dataset(es_client: Elasticsearch, index_name: str):
    with open('documents-with-ids.json', 'rt') as f_in:
        docs_raw = json.load(f_in)
    df_ground_truth = pd.read_csv('ground-truth-data.csv', index_col=0)
    model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')
    id_to_text = {doc["id"]: doc["text"] for doc in docs_raw}
    df_ground_truth["text"] = df_ground_truth["document"].map(id_to_text)
    df_ground_truth['contexts'] = None

    found = 0
    not_found = 0
    i = 0
    for idx, row in tqdm(df_ground_truth.iterrows(), total=df_ground_truth.shape[0]):
        # retrieve context data based on question and text vector embedding from elastic search
        question_vector = model.encode(row["question"])
        text_results = elastic_search_knn(
            "text_vector", question_vector, "data-engineering-zoomcamp", es_client, index_name)
        text_results = [result["text"] for result in text_results]
        df_ground_truth.at[idx, 'contexts'] = text_results

        # generate llm answer and store in elastic search
        prompt = build_prompt(row["question"], text_results)
        llm_answer = ask_llm(
            "gpt-3.5-turbo-0125", [{"role": "user", "content": prompt}], mock_answer=False
        )
        df_ground_truth.at[idx, "llm_answer"] = llm_answer
        llm_answer_vector = model.encode(llm_answer)
        result = es_client.search(
            index=index_name,
            body={"query": {"match": {"id": row["document"]}}}
        )
        if len(result["hits"]["hits"]) > 0:
            es_client.update(
                index=index_name,
                id=result["hits"]["hits"][0]["_id"],
                doc={
                    "llm_answer_vector": llm_answer_vector,
                    "llm_answer": llm_answer
                }
            )
            logging.info(f'updated id {result["hits"]["hits"][0]["_id"]} with {llm_answer_vector[:5]}')
            found += 1
        else:
            logging.error(f'Was not able to find doc for {row["document"]}')
            not_found += 1

    es_client.indices.refresh(index=index_name)
