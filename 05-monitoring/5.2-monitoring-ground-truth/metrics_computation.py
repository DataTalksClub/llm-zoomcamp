import os
import ast
import pandas as pd

from evidently import ColumnMapping
from evidently.report import Report
from evidently.metrics import ColumnSummaryMetric
from evidently.metric_preset import TextEvals
from evidently.descriptors import SemanticSimilarity, OpenAIPrompting

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
    column_mapping = ColumnMapping(
        text_features=["text", "llm_answer"]
    )

    # (1) semantic similarity (cosine) https://docs.evidentlyai.com/reference/all-metrics, https://www.evidentlyai.com/blog/llm-testing-tutorial#3-define-the-test-suite
    # report = Report(metrics=[
    #     ColumnSummaryMetric(
    #         column_name=SemanticSimilarity(display_name="Bla").on(["text", "llm_answer"])
    # )])
    # ground_truth_data_sample = ground_truth_data.sample(5)
    # print(ground_truth_data_sample[["text", "llm_answer"]])
    # print(ground_truth_data_sample.info())
    # report.run(reference_data=None, current_data=ground_truth_data_sample, column_mapping=column_mapping)
    # report_df = report.as_dataframe()

    print(report)
    # (2) LLM-as-a-judge: toxicity https://docs.evidentlyai.com/user-guide/customization/huggingface_descriptor
    # (3) LLM-as-a-judge: ask anything, i.e. if answer makes sense https://docs.evidentlyai.com/user-guide/customization/llm_as_a_judge
    # need to find out if this can only be applied on one column or on two as well to compare expected answer vs. actual answer
    report = Report(metricss=[
        TextEvals(column_name="llm_answer", descriptors=[
            OpenAIPrompting()
        ])
    ])

    report_df.to_csv("metrics_report.csv")


if __name__ == "__main__":
    # es_client = setup_es_client_and_index(index_name=ES_INDEX_NAME)
    # dump_doc_embeddings_to_db(es_client=es_client, index_name=ES_INDEX_NAME)
    # extend_ground_truth_dataset(es_client=es_client, index_name=ES_INDEX_NAME)
    compute_metrics(pd.read_csv("ground-truth-data.csv", usecols=["question", "contexts", "text", "llm_answer"]))
    # create_metrics_db(postgres_db_params=POSTGRES_DB_PARAMS)
    # create_metrics_table(postgres_db_params=POSTGRES_DB_PARAMS)
    # store_metrics(DB_PARAMS, metrics_df)
