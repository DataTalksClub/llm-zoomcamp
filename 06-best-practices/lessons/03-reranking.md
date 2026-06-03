# Document Reranking

When we retrieve documents, they're ranked by cosine similarity.
But cosine similarity doesn't always reflect true relevance to the
user's question. The most relevant document might be at position
six, and we only return the top five.

Reranking re-orders retrieved documents by a better relevance
score. It sits at the end of the search pipeline, after the
initial retrieval.

## Reciprocal Rank Fusion (RRF)

One popular reranking method is Reciprocal Rank Fusion (RRF). It
combines rankings from multiple search methods (vector, keyword,
etc.

) into a single score:

```text
RRF(d) = sum(1 / (k + rank(d))) for each ranking
```

where `k` is a constant (typically 60). Documents that appear
high in multiple rankings get a higher combined score.

## RRF in Elasticsearch

Elasticsearch 8.9+ supports RRF natively:

```python
def elastic_search_hybrid_rrf(field, query, vector, course):
    knn_query = {
        "field": field,
        "query_vector": vector,
        "k": 5,
        "num_candidates": 10000,
        "boost": 0.5,
        "filter": {
            "term": {
                "course": course
            }
        }
    }

    keyword_query = {
        "bool": {
            "must": {
                "multi_match": {
                    "query": query,
                    "fields": ["question^3", "text", "section"],
                    "type": "best_fields",
                    "boost": 0.5,
                }
            },
            "filter": {
                "term": {
                    "course": course
                }
            }
        }
    }
```

Then execute the search with RRF ranking:

```python
    response = es_client.search(
        index=index_name,
        query=keyword_query,
        knn=knn_query,
        size=5,
        rank={"rrf": {}}
    )

    return [hit["_source"] for hit in response["hits"]["hits"]]
```

Note: the built-in RRF requires a paid Elasticsearch subscription.
If you're using the free tier, you'll get an error.

## Implementing RRF ourselves

We can implement RRF manually.

The approach is to run vector and
keyword searches separately, compute RRF scores, and merge:

```python
def compute_rrf(rank, k=60):
    return 1 / (k + rank)

def elastic_search_hybrid_rrf(field, query, vector, course, k=60):
    knn_query = {
        "field": field,
        "query_vector": vector,
        "k": 5,
        "num_candidates": 10000,
        "filter": {
            "term": {
                "course": course
            }
        }
    }
```

Define the keyword query and run both searches:

```python
    keyword_query = {
        "bool": {
            "must": {
                "multi_match": {
                    "query": query,
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
    }

    knn_response = es_client.search(
        index=index_name,
        knn=knn_query,
        size=5
    )

    keyword_response = es_client.search(
        index=index_name,
        query=keyword_query,
        size=5
    )
```

Now compute RRF scores from both result sets:

```python
    rrf_scores = {}

    for rank, hit in enumerate(knn_response["hits"]["hits"]):
        doc_id = hit["_source"]["id"]
        rrf_scores[doc_id] = rrf_scores.get(doc_id, 0) + compute_rrf(rank, k)

    for rank, hit in enumerate(keyword_response["hits"]["hits"]):
        doc_id = hit["_source"]["id"]
        rrf_scores[doc_id] = rrf_scores.get(doc_id, 0) + compute_rrf(rank, k)

    all_docs = {
        hit["_source"]["id"]: hit["_source"]
        for hit in knn_response["hits"]["hits"] + keyword_response["hits"]["hits"]
    }

    sorted_docs = sorted(rrf_scores.items(), key=lambda x: x[1], reverse=True)

    return [all_docs[doc_id] for doc_id, _ in sorted_docs[:5]]
```

When the same document appears in both search results, its RRF
scores are summed, giving it a higher rank.

## Evaluation

We evaluate RRF with the same ground truth data:

```python
def question_text_hybrid_rrf(q):
    question = q["question"]
    course = q["course"]
    v_q = model.encode(question)
    return elastic_search_hybrid_rrf("question_text_vector", question, v_q, course)

evaluate(ground_truth, question_text_hybrid_rrf)
```

Results with all approaches:

- Hybrid without reranking: Hit Rate 0.917, MRR 0.824
- Hybrid with RRF: Hit Rate 0.925, MRR 0.851

Reranking improves both metrics by a few percent. The gain is
modest here. In production systems with more data and noisier queries,
reranking can make a bigger difference.

To learn more:

- [Reciprocal Rank Fusion - Elasticsearch Guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/rrf.html)
- [RRF method - Original Paper](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf)
- [Elasticsearch subscription plans](https://www.elastic.co/subscriptions)

[← Hybrid Search](02-hybrid-search.md) | [Hybrid Search with LangChain →](04-langchain.md)
