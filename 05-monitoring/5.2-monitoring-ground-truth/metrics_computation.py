import os
import ast
import pandas as pd
from datasets import Dataset

from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    answer_similarity
)
from ragas import evaluate

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


def compute_metrics_with_ragas(ground_truth_data: pd.DataFrame):
    ground_truth_data["contexts"] = ground_truth_data["contexts"].apply(ast.literal_eval)
    ground_truth_data = ground_truth_data.rename(columns={"text": "ground_truth"})
    ground_truth_data["answer"] = "bla"
    # get answer from OpenAI LLM instead

    dataset = Dataset.from_pandas(ground_truth_data)

    result = evaluate(
        dataset=dataset,
        metrics=[
            answer_relevancy,
            faithfulness,
            answer_similarity
        ],
    )
    print(result)
    metrics_df = pd.DataFrame([result], index=0)
    metrics_df.to_csv("results.csv")


if __name__ == "__main__":
    es_client = setup_es_client_and_index(index_name=ES_INDEX_NAME)
    dump_doc_embeddings_to_db(es_client=es_client, index_name=ES_INDEX_NAME)
    extend_ground_truth_dataset(es_client=es_client, index_name=ES_INDEX_NAME)
    # compute_metrics_with_ragas(pd.read_csv("ground-truth-data.csv", usecols=["question", "contexts", "text"]))
    # create_metrics_db(postgres_db_params=POSTGRES_DB_PARAMS)
    # create_metrics_table(postgres_db_params=POSTGRES_DB_PARAMS)
    # store_metrics(DB_PARAMS, metrics_df)
