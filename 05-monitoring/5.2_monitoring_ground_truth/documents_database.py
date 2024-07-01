import json 
from tqdm.auto import tqdm
from elasticsearch import Elasticsearch
import pandas as pd
from datasets import Dataset


def setup_es_client_and_index(index_name: str) -> Elasticsearch:
    es_client = Elasticsearch("http://localhost:9200")

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
                "course": {"type": "keyword"} 
            }
        }
    }

    if not es_client.indices.exists(index=index_name):
        es_client.indices.create(index=index_name, body=index_settings)

    return es_client


def fill_document_db(es_client: Elasticsearch, index_name: str):
    with open('../../01-intro/documents.json', 'rt') as f_in:
        docs_raw = json.load(f_in)

    documents = []

    for course_dict in docs_raw:
        for doc in tqdm(course_dict['documents']):
            doc['course'] = course_dict['course']
            es_client.index(index=index_name, document=doc)
            documents.append(doc)


def retrieve_all_docs_from_db(es_client: Elasticsearch, index_name: str) -> Dataset:
    search_result = es_client.search(index=index_name, body={"query": {"match_all": {}}}, size=1000)
    dataset = Dataset.from_pandas(pd.DataFrame([hit["_source"] for hit in search_result["hits"]["hits"]]))

    return dataset
