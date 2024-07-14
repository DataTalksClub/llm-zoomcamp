import os
import logging
from sklearn.metrics.pairwise import cosine_similarity
from transformers import AutoModelForSequenceClassification, AutoTokenizer, TextClassificationPipeline

from documents_database import (
    setup_es_client_and_index,
    dump_doc_embeddings_to_db,
    extend_ground_truth_dataset,
    elastic_search_fields
)

from utils.llm_utils import ask_llm, build_prompt

ES_INDEX_NAME = "course_questions"

OPEN_API_KEY = os.environ['OPENAI_API_KEY']


def compute_cosine_similarity(result: list, index_name: str):
    for entry in result:
        cosine_similarity_value = cosine_similarity(
            [entry["_source"]["text_vector"]],
            [entry["_source"]["llm_answer_vector"]]
        )[0][0]
        es_client.update(
            index=index_name,
            id=entry["_id"],
            doc={"cosine_similarity_text_llm_answer": cosine_similarity_value}
        )


def compute_sentiment(result: list, hugginface_model_path: str, index_name: str):
    tokenizer = AutoTokenizer.from_pretrained(hugginface_model_path)
    model = AutoModelForSequenceClassification.from_pretrained(hugginface_model_path)
    pipeline =  TextClassificationPipeline(model=model, tokenizer=tokenizer, truncation=True)

    for entry in result:
        sentiment = pipeline(entry["_source"]["llm_answer"])[0]["label"]
        negative = True if sentiment == "NEG" else False
        es_client.update(
            index=index_name,
            id=entry["_id"],
            doc={"negative_llm_answer": negative}
        )


def compute_llm_as_a_judge(result: list, openai_model_name: str, index_name: str):
    for entry in result:
        prompt = f"""
            Please assess if the answer generated by an LLM "{entry['_source']['llm_answer']}" is suitable to answer a given question: "{entry['_source']['question']}"

            Use the following categories to judge the quality:
            good if the llm_answer is suitable to answer the question
            ok if the llm_answer is partly suitable to answer the question
            bad if the llm_answer is not suitable to answer the question
            Return only one category.
        """
        result = ask_llm(openai_model_name, [{"role": "user", "content": prompt}], mock_answer=False).lower()
        judge = result if result in ["good", "ok", "bad"] else "unknown"
        es_client.update(
            index=index_name,
            id=entry["_id"],
            doc={"llm_as_a_judge": judge}
        )   


if __name__ == "__main__":
    es_client = setup_es_client_and_index(index_name=ES_INDEX_NAME)
    # dump_doc_embeddings_to_db(es_client=es_client, index_name=ES_INDEX_NAME)
    # extend_ground_truth_dataset(es_client=es_client, index_name=ES_INDEX_NAME)
    result = elastic_search_fields(es_client=es_client, index_name=ES_INDEX_NAME, search_query={
        "query": {
            "bool": {
                "must": [
                    {"exists": {"field": "text_vector"}},
                    {"exists": {"field": "llm_answer_vector"}}
                ]
            }
        }
    })
    
    compute_cosine_similarity(result, index_name=ES_INDEX_NAME)
    compute_sentiment(result, hugginface_model_path="finiteautomata/bertweet-base-sentiment-analysis", index_name=ES_INDEX_NAME)
    compute_llm_as_a_judge(result, openai_model_name="gpt-3.5-turbo-0125", index_name=ES_INDEX_NAME)


# TODOs:
    # Must: show metrics on grafana dashboard over time  
    # Must: think about 1x quick win how we can speed up "extend_ground_truth_dataset"
    # Must: improve code quality in documents_database.py
    # Must: check if chatgpt 4 gives better answers and meaningful cosine similarity (picking 3x examples for near, far away etc is enough!) 
    # optional: put 3x metrics to nested 
    # optional: show corresponding question, llm_answer to "bad" answers
