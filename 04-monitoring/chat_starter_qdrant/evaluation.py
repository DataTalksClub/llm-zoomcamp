import nest_asyncio
import phoenix as px
from phoenix.client import Client
from phoenix.evals import (HallucinationEvaluator, OpenAIModel, QAEvaluator,
                           RelevanceEvaluator, run_evals)
from phoenix.session.evaluation import (get_qa_with_reference,
                                        get_retrieved_documents)

from config import PROJECT_NAME
from phoenix.trace import DocumentEvaluations
import pandas as pd
nest_asyncio.apply()

def get_retrieval_df(client):

    all_spans_df = client.spans.get_spans_dataframe(project_identifier=PROJECT_NAME)
    columns_of_interest = ['attributes.input.value','attributes.retrieval', 'context.trace_id', 'context.span_id']
    
    # Filter to only 'retrieve' spans and extract relevant info
    df = all_spans_df[all_spans_df['name'] == 'qdrant_hybrid_search'][columns_of_interest]
    df['retrieval'] = [{} if doc is None else doc['document'] for doc in df["attributes.retrieval"]]
    df = df.explode(column='retrieval').copy()
    df['document_score'] = df['retrieval'].apply(lambda x: x['document.score'] if isinstance(x, dict) and 'document.score' in x else None)
    df['reference'] = df['retrieval'].apply(lambda x: x['document.content'] if isinstance(x, dict) and 'document.content' in x else None)
    df['input'] = df['attributes.input.value']
    df.dropna(subset=['document_score'],inplace=True)
    df.index.name = None
    df['document_position'] = df.groupby('context.span_id')['document_score'].rank(
        method='first', 
        ascending=False
        ).astype(int)
    
    retrieved_documents_df = df[['context.span_id', 'context.trace_id', 'input', 'document_score', 'reference', 'document_position']].copy()
    retrieved_documents_df.set_index(['context.span_id', 'document_position'], inplace=True)
    return retrieved_documents_df

def get_qa_df(client):
    all_spans_df = client.spans.get_spans_dataframe(project_identifier=PROJECT_NAME)
    df = all_spans_df[all_spans_df['span_kind'] == 'LLM'].copy()
    columns_of_interest = ['attributes.input.value', 'attributes.output.value', 'attributes.search']
    df['input'] = df['attributes.input.value'].apply(lambda x: x if isinstance(x, str) else None)
    df['output'] = df['attributes.output.value'].apply(lambda x: x if isinstance(x, str) else None)
    df['reference'] = df['attributes.search'].apply(lambda x: x['result']['text'] if isinstance(x, dict) and 'result' in x and 'text' in x['result'] else None)
    df.dropna(subset=['reference'], inplace=True)

    return df[['input', 'output', 'reference']]


def main():
    eval_model = OpenAIModel(model="gpt-4.1-nano")
    relevance_evaluator = RelevanceEvaluator(eval_model)
    hallucination_evaluator = HallucinationEvaluator(eval_model)
    qa_evaluator = QAEvaluator(eval_model)
    client = Client()

    retrieved_documents_df = get_retrieval_df(client)
    retrieved_documents_relevance = run_evals(
        evaluators=[relevance_evaluator],
        dataframe=retrieved_documents_df,
        provide_explanation=True,
        concurrency=20,
    )

    queries_df = get_qa_df(client)
    qa_evaluations, halluncinations_evaluation = run_evals(
        evaluators=[qa_evaluator, hallucination_evaluator],
        dataframe=queries_df,
        provide_explanation=True,
        concurrency=10,
    )


    retrieved_documents_relevance_df = pd.DataFrame(retrieved_documents_relevance[0])
    qa_evaluations_df = pd.DataFrame(qa_evaluations)
    hallucinations_evaluation_df = pd.DataFrame(halluncinations_evaluation)

    client.spans.log_span_annotations_dataframe(
        dataframe=retrieved_documents_relevance_df,
        annotation_name="Relevance",
        annotator_kind="LLM"
    )
    client.spans.log_span_annotations_dataframe(
        dataframe=qa_evaluations_df,
        annotation_name="QA Evaluation",
        annotator_kind="LLM"
    )
    
    client.spans.log_span_annotations_dataframe(
        dataframe=hallucinations_evaluation_df,
        annotation_name="Hallucination Evaluation",
        annotator_kind="LLM"
    )

if __name__ == "__main__":
    main()
