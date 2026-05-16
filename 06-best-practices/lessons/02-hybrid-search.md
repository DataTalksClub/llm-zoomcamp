# Hybrid Search

<a href="https://www.youtube.com/watch?v=TQ_ck6Q9gSQ">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/TQ_ck6Q9gSQ">
</a>

Vector search finds documents by semantic meaning. Keyword search
finds documents by exact word matches. Hybrid search combines both.

The approach is simple: run both searches and merge the scores.

Each
search produces a ranked list with scores, and we combine them
with a weighted sum:

```text
score = alpha * vector_score + (1 - alpha) * keyword_score
```

When `alpha = 1`, it's pure vector search. When `alpha = 0`,
it's pure keyword search. Values in between give a mix.

## Setting up Elasticsearch

We'll use Elasticsearch, which supports both vector (KNN) and
keyword search natively.

Start it in Docker:

```bash
docker run -it \
    --rm \
    --name elasticsearch \
    -m 4GB \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    docker.elastic.co/elasticsearch/elasticsearch:8.9.0
```

Install the Python client:

```bash
uv add elasticsearch sentence-transformers tqdm
```

## Indexing documents

We use the same FAQ documents from module 02, but this time we
create three types of embeddings per document:

```python
import json
from tqdm.auto import tqdm
from sentence_transformers import SentenceTransformer
from elasticsearch import Elasticsearch

with open('documents-with-ids.json') as f:
    documents = json.load(f)

model_name = 'multi-qa-MiniLM-L6-cos-v1'
model = SentenceTransformer(model_name)

for doc in tqdm(documents):
    question = doc['question']
    text = doc['text']
    qt = question + ' ' + text

    doc['question_vector'] = model.encode(question)
    doc['text_vector'] = model.encode(text)
    doc['question_text_vector'] = model.encode(qt)
```

Then create the index with vector fields and index all documents:

```python
es_client = Elasticsearch('http://localhost:9200')

index_settings = {
    'settings': {
        'number_of_shards': 1,
        'number_of_replicas': 0
    },
    'mappings': {
        "properties": {
            "text": {"type": "text"},
            "section": {"type": "text"},
            "question": {"type": "text"},
            "course": {"type": "keyword"},
            "id": {"type": "keyword"},
            'question_vector': {
                "type": "dense_vector",
                'dims': 384,
                'index': True,
                'similarity': 'cosine'
            },
            'text_vector': {
                "type": "dense_vector",
                'dims': 384,
                'index': True,
                'similarity': 'cosine'
            },
            'question_text_vector': {
                "type": "dense_vector",
                'dims': 384,
                'index': True,
                'similarity': 'cosine'
            }
        }
    }
}

index_name = 'course-questions'

es_client.indices.delete(index=index_name, ignore_unavailable=True)
es_client.indices.create(index=index_name, body=index_settings)
```

Now index all documents:

```python
for doc in tqdm(documents):
    es_client.index(index=index_name, document=doc)
```

## Hybrid search query

A hybrid search in Elasticsearch combines a KNN query (vector)
with a standard query (keyword):

```python
def elastic_search_hybrid(field, query, vector, course):
    knn_query = {
        'field': field,
        'query_vector': vector,
        'k': 5,
        'num_candidates': 10000,
        'boost': 0.5,
        'filter': {
            'term': {
                'course': course
            }
        }
    }

    keyword_query = {
        'bool': {
            'must': {
                'multi_match': {
                    'query': query,
                    'fields': ['question^3', 'text', 'section'],
                    "type": "best_fields",
                    'boost': 0.5,
                }
            },
            'filter': {
                'term': {
                    'course': course
                }
            }
        }
    }

    response = es_client.search(
        index=index_name,
        query=keyword_query,
        knn=knn_query,
        size=5
    )

    return [hit['_source'] for hit in response['hits']['hits']]
```

The `boost` parameter controls the weight. Both are set to `0.5`
here, giving equal weight to vector and keyword results.

## Evaluating hybrid search

We use the same Hit Rate and MRR metrics from module 04:

```python
import pandas as pd

df_ground_truth = pd.read_csv('ground-truth-data.csv')
ground_truth = df_ground_truth.to_dict(orient='records')

def hit_rate(relevance_total):
    cnt = 0
    for line in relevance_total:
        if True in line:
            cnt += 1
    return cnt / len(relevance_total)

def mrr(relevance_total):
    total_score = 0.0
    for line in relevance_total:
        for rank in range(len(line)):
            if line[rank]:
                total_score += 1 / (rank + 1)
                break
    return total_score / len(relevance_total)

def evaluate(ground_truth, search_function):
    relevance_total = []
    for q in tqdm(ground_truth):
        doc_id = q['document']
        results = search_function(q)
        relevance = [d['id'] == doc_id for d in results]
        relevance_total.append(relevance)
    return {
        'hit_rate': hit_rate(relevance_total),
        'mrr': mrr(relevance_total)
    }
```

Test with question-only embeddings:

```python
def question_hybrid(q):
    question = q['question']
    course = q['course']
    v_q = model.encode(question)
    return elastic_search_hybrid('question_vector', question, v_q, course)

evaluate(ground_truth, question_hybrid)
```

Results compared to pure vector search:

| Approach | Hit Rate | MRR |
|---|---|---|
| ES KNN on questions | 0.773 | 0.667 |
| Hybrid on questions | 0.828 | 0.706 |
| Hybrid on question+text | 0.917 | 0.824 |

Hybrid search improves both metrics. Using question+text embeddings
gives the best results.

The full notebook is in
[hybrid-search-and-reranking-es.ipynb](../hybrid-search-and-reranking-es.ipynb).

To learn more:

- [Hybrid search - Elasticsearch Guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/knn-search.html#_combine_approximate_knn_with_other_features)
- [Hybrid search - Tutorial](https://www.elastic.co/search-labs/tutorials/search-tutorial/vector-search/hybrid-search)

[← Best Practices for RAG](01-intro.md) | [Document Reranking →](03-reranking.md)
