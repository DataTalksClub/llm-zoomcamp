import json 
from tqdm.auto import tqdm
from elasticsearch import Elasticsearch
import pandas as pd
from sentence_transformers import SentenceTransformer

from llm_utils import ask_llm, build_prompt


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
                "course": {"type": "keyword"},
                "id": {"type": "keyword"},
                "text_vector": {
                    "type": "dense_vector",
                    "dims": 384,
                    "index": True,
                    "similarity": "cosine"
                }
            }
        }
    }

    es_client.indices.delete(index=index_name, ignore_unavailable=True)
    es_client.indices.create(index=index_name, body=index_settings)

    return es_client


def dump_doc_embeddings_to_db(es_client: Elasticsearch, index_name: str):
    with open('../../03-vector-search/documents-with-ids.json', 'rt') as f_in:
        documents = json.load(f_in)

    model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')
    for doc in tqdm(documents):
        if doc["course"] == "data-engineering-zoomcamp":
            doc["text_vector"] = model.encode(doc["text"])
            es_client.index(index=index_name, document=doc)


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
    with open('../../03-vector-search/documents-with-ids.json', 'rt') as f_in:
        docs_raw = json.load(f_in)
    
    df_ground_truth = pd.read_csv('../../03-vector-search/ground-truth-data.csv')

    model = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')
    
    id_to_text = {doc["id"]: doc["text"] for doc in docs_raw}
    df_ground_truth["text"] = df_ground_truth["document"].map(id_to_text)
    df_ground_truth['contexts'] = None 
    
    for idx, row in tqdm(df_ground_truth.iterrows(), total=df_ground_truth.shape[0]):
        question_vector = model.encode(row["question"])
        text_results = elastic_search_knn("text_vector", question_vector, "data-engineering-zoomcamp", es_client, index_name)
        df_ground_truth.at[idx, 'contexts'] = [result["text"] for result in text_results]
    
        prompt = build_prompt(row["question"], row["contexts"])
        df_ground_truth.at[idx, "llm_answer"] = ask_llm([{"role": "user", "content": prompt}], mock_answer=False)

    df_ground_truth.to_csv("ground-truth-data.csv")
