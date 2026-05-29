# Hybrid Search with LangChain

So far we've been working with Elasticsearch directly. LangChain
provides wrappers that simplify the code. In this lesson, we'll
rewrite our hybrid search using LangChain's ElasticsearchRetriever.

The indexing stage stays the same - we still use the same
Elasticsearch index from the previous lesson. Only the retrieval
code changes.

## Installing LangChain

Install the LangChain packages:

```bash
uv add langchain langchain-elasticsearch langchain-huggingface
```

## Setting up the retriever

LangChain provides `ElasticsearchRetriever`, a wrapper around the
Elasticsearch client.

We configure it with a hybrid query function:

```python
from langchain_huggingface import HuggingFaceEmbeddings
from typing import Dict
from langchain_elasticsearch import ElasticsearchRetriever

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/multi-qa-MiniLM-L6-cos-v1"
)

es_url = "http://localhost:9200"
```

Define a hybrid query function that combines keyword and vector search:

```python
def hybrid_query(search_query: str) -> Dict:
    vector = embedding.embed_query(search_query)
    return {
        "query": {
            "bool": {
                "must": {
                    "multi_match": {
                        "query": search_query,
                        "fields": ["question^3", "text", "section"],
                        "type": "best_fields",
                    }
                },
                "filter": {
                    "term": {
                        "course": "data-engineering-zoomcamp"
                    }
                }
            }
        },
        "knn": {
            "field": "question_text_vector",
            "query_vector": vector,
            "k": 5,
            "num_candidates": 10000,
        },
        "size": 5
    }
```

Create the retriever from the query function:

```python
hybrid_retriever = ElasticsearchRetriever.from_es_params(
    url=es_url,
    index_name="course-questions",
    body_func=hybrid_query,
    content_field="text"
)
```

Now we can search:

```python
query = "I just discovered the course. Can I still join it?"
results = hybrid_retriever.invoke(query)

for result in results:
    print(result.metadata["_source"]["question"])
    print(result.metadata["_score"])
```

## Evaluating with LangChain

To evaluate, we wrap the retriever in a function that works with
our ground truth data:

```python
def elastic_search_hybrid(field, query, course):
    def hybrid_query(search_query: str) -> Dict:
        vector = embedding.embed_query(search_query)
        return {
            "query": {
                "bool": {
                    "must": {
                        "multi_match": {
                            "query": search_query,
                            "fields": ["question^3", "text", "section"],
                            "type": "best_fields",
                        }
                    },
                    "filter": {
                        "term": {
                            "course": course
                        }
                    }
                }
            },
            "knn": {
                "field": field,
                "query_vector": vector,
                "k": 5,
                "num_candidates": 10000,
            },
            "size": 5
        }

    retriever = ElasticsearchRetriever.from_es_params(
        url=es_url,
        index_name="course-questions",
        body_func=hybrid_query,
        content_field="text"
    )
```

Run the retriever and format the results:

```python
    results = retriever.invoke(query)
    return [
        {
            "id": r.metadata["_source"]["id"],
            "question": r.metadata["_source"]["question"],
            "text": r.metadata["_source"]["text"],
        }
        for r in results
    ]

def question_text_hybrid(q):
    return elastic_search_hybrid("question_text_vector", q["question"], q["course"])

evaluate(ground_truth, question_text_hybrid)
```

The results match what we got with direct Elasticsearch queries:
Hit Rate 0.925 and MRR 0.851.

The full notebook is in
[hybrid-search-langchain.ipynb](../hybrid-search-langchain.ipynb).

LangChain doesn't change what's happening under the hood - it's
the same Elasticsearch query. But it provides a cleaner interface,
especially when you want to chain retrieval with LLM calls in a
larger pipeline.

To learn more:

- [ElasticsearchRetriever - LangChain Docs](https://python.langchain.com/v0.2/docs/integrations/retrievers/elasticsearch_retriever/)
- [Chatbot Implementation - Elastic Tutorial](https://www.elastic.co/search-labs/tutorials/chatbot-tutorial/implementation)

[← Document Reranking](03-reranking.md) | [Next Steps →](05-next-steps.md)
