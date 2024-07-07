import os
import ast
import pandas as pd
from datasets import Dataset

from documents_database import (
    setup_es_client_and_index, 
    dump_doc_embeddings_to_db,
    extend_ground_truth_dataset
)
from metrics_database import (
    create_metrics_db,
    create_metrics_table
)


ES_INDEX_NAME = "course_questions"
POSTGRES_DB_PARAMS = {
    'user': 'admin',
    'password': 'admin',
    'host': os.getenv('POSTGRES_HOST', 'localhost'),
    'dbname': 'metrics_db',
    'port': '5432'
}

OPEN_API_KEY = os.environ['OPENAI_API_KEY']


def compute_metrics(ground_truth_data: pd.DataFrame):
    # (1) semantic similarity (cosine) https://docs.evidentlyai.com/reference/all-metrics, https://www.evidentlyai.com/blog/llm-testing-tutorial#3-define-the-test-suite
    # (2) LLM-as-a-judge: toxicity https://docs.evidentlyai.com/user-guide/customization/huggingface_descriptor
    # (3) LLM-as-a-judge: ask anything, i.e. if answer makes sense https://docs.evidentlyai.com/user-guide/customization/llm_as_a_judge
    ground_truth_data["contexts"] = ground_truth_data["contexts"].apply(ast.literal_eval)
    ground_truth_data = ground_truth_data.rename(columns={"text": "ground_truth"})

    metrics_df.to_csv("results.csv")


if __name__ == "__main__":
    es_client = setup_es_client_and_index(index_name=ES_INDEX_NAME)
    # dump_doc_embeddings_to_db(es_client=es_client, index_name=ES_INDEX_NAME)
    extend_ground_truth_dataset(es_client=es_client, index_name=ES_INDEX_NAME)
    # compute_metrics(pd.read_csv("ground-truth-data.csv", usecols=["question", "contexts", "text"]))
    # create_metrics_db(postgres_db_params=POSTGRES_DB_PARAMS)
    # create_metrics_table(postgres_db_params=POSTGRES_DB_PARAMS)
    # store_metrics(DB_PARAMS, metrics_df)
