import os
import pandas as pd
from datetime import datetime

from ragas.metrics import (
    faithfulness,
    context_precision
)
from ragas import evaluate

from documents_database import (
    setup_es_client_and_index, 
    fill_document_db,
    retrieve_n_docs_from_db
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


def compute_metrics_with_ragas():
    dataset = retrieve_n_docs_from_db(es_client, ES_INDEX_NAME, query={"match_all": {}}, n=10)
    ground_truths = []
    for row in dataset:
        query = {
            "more_like_this": {
                "fields": ["text"],
                "like": row["question"],
                "min_term_freq": 1,
                "max_query_terms": 12,
                "min_doc_freq": 1
            }
        }
        ground_truth = retrieve_n_docs_from_db(es_client, ES_INDEX_NAME, query=query, n=10)
        ground_truths.append(ground_truth)
        print("#")
        print(row["question"])
        print(pd.DataFrame(ground_truth))

    dataset = dataset.add_column("ground_truth", ground_truths)
    print(dataset)
    print(dataset[1])

    # retrieve context from elastic search
    # get answer from OpenAI LLM
    # finally, compute 2x chosen metrics with ragas
    metrics = {
        'timestamp': [datetime.now(), datetime.now(), datetime.now()],
        'metric_a': [0.95, 0.93, 0.92],
        'metric_b': [0.85, 0.93, 0.92],
        'metric_c': [0.95, 0.94, 0.90],
    }

    result = evaluate(
        dataset=dataset,
        metrics=[
            context_precision,
            faithfulness
        ],
    )

    metrics_df = pd.DataFrame(metrics)


if __name__ == "__main__":
    es_client = setup_es_client_and_index(index_name=ES_INDEX_NAME)
    fill_document_db(es_client=es_client, index_name=ES_INDEX_NAME)
    create_metrics_db(postgres_db_params=POSTGRES_DB_PARAMS)
    create_metrics_table(postgres_db_params=POSTGRES_DB_PARAMS)
    compute_metrics_with_ragas()
    # store_metrics(DB_PARAMS, metrics_df)
