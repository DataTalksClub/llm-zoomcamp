## Homework: Vector Search

In this homework, we'll implement an end to end semantic search engine

> It's possible that your answers won't match exactly. If it's the case, select the closest one.

## Q1. Prepare Documents

Import documents.json, read the file and prepare the dataset:

```bash
import json

with open('documents.json', 'rt') as f_in:
    docs_raw = json.load(f_in)

documents = []

for course_dict in docs_raw:
    for doc in course_dict['documents']:
        doc['course'] = course_dict['course']
        documents.append(doc)

len(documents)
```
How many records we have in the pre-processed "documents"?
* 1000
* 1051
* 901
* 948


## Q2. Create Embeddings using Pretrained Models

Import sentence transformer library. Please review the Sentence Transformer pretrained documentation here: https://www.sbert.net/docs/sentence_transformer/pretrained_models.html#model-overview

```bash
# This is a new library compared to the previous modules. 
# Please perform "pip install sentence_transformers==2.7.0"

from sentence_transformers import SentenceTransformer

# if you get an error do the following:
# 1. Uninstall numpy 
# 2. Uninstall torch
# 3. pip install numpy==1.26.4
# 4. pip install torch
# run the above cell, it should work
model = SentenceTransformer("all-MiniLM-L12-v2")
```

What is the model size (in MB) and average performance?

* [420, 63.30]
* [120, 59.76]
* [290, 59.84]
* [420, 51.72]


## Q3. Get the dimension for model embedding

```bash
len(model.encode("This is a simple sentence"))
```

What is the dimension of the model embedding?

* 768
* 265
* 384
* 1056

```bash
#created the dense vector using the pre-trained model
operations = []
for doc in documents:
    # Transforming the title into an embedding using the model
    doc["question_vector"] = model.encode(doc["question"]).tolist()
    operations.append(doc)
```


Establish connection to Elasticsearch 

```bash
from elasticsearch import Elasticsearch
es_client = Elasticsearch('http://localhost:9200') 

es_client.info()
```

## Q4: Create Mappings and Index

In the mappings, change "section" to "keyword" type

```bash
index_settings = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
        "properties": {
            "text": {"type": "text"},
            "section": {"type": "keyword"},
            "question": {"type": "text"},
            "course": {"type": "keyword"} ,
            "question_vector":{"type":"dense_vector","dims": 384,"index":True,"similarity": "cosine"
        },
        }
    }
}

index_name = "course-questions"

es_client.indices.delete(index=index_name, ignore_unavailable=True)
es_client.indices.create(index=index_name, body=index_settings)
```

Add documents into index

```bash
for doc in operations:
    try:
        es_client.index(index=index_name, document=doc)
    except Exception as e:
        print(e)
```

In the es_client.indices.delete statement, what does "ignore_unavailable" mean?
* If the pre-trained model in unavailable, skip this statement
* If the index is unavailable, skip this statement
* If the pre-trained model in unavailable, don't skip this statement
* If the index is unavailable, don't skip this statement


## Q5: Create end user query and perform semantic search

Use the search term "how to enrol to course?" and perform semantic search

```bash
search_term = "how to enrol to course?"
vector_search_term = model.encode(search_term)

query = {
    "field" : "question_vector",
    "query_vector" :  vector_search_term,
    "k" : 5,
    "num_candidates" : 10000, 
}

res = es_client.search(index=index_name, knn=query,source=["text","section","question","course"])
res["hits"]["hits"]
```
What is the similarity score, section and course for the first result?

* [0.78, 'Module 1: Introduction', 'mlops-zoomcamp']
* [0.74, 'General course-related questions', 'data-engineering-zoomcamp']
* [0.72, 'Projects (Midterm and Capstone)', 'machine-learning-zoomcamp']
* [0.71, 'General course-related questions', 'machine-learning-zoomcamp']


## Q6: Perform Semantic Search & Filtering

Filter the results to "General course-related questions" section only

```bash
knn_query = {
    "field" : "text_vector",
    "query_vector" :  vector_search_term,
    "k" : 5,
    "num_candidates" : 10000
}

response = es_client.search(
    index=index_name,
    query={
        "match": {
                "section": "General course-related questions"
            },
        },
        
    knn=knn_query,
    size=5
)

response["hits"]["hits"]
```
Do you see the results filtered only to "General course-related questions" section?

* Yes
* No


## Submit the results

* Submit your results here: https://courses.datatalks.club/llm-zoomcamp-2024/homework/hw3 (to be created)
* It's possible that your answers won't match exactly. If it's the case, select the closest one.
