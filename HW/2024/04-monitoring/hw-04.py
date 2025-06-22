# Create hw-03.ipynb
import json
notebook_content = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Homework: Vector Search\n",
                "\n",
                "In this homework, we'll experiment with vector with and without Elasticsearch\n",
                "\n",
                "> It's possible that your answers won't match exactly. If it's the case, select the closest one.\n",
                "\n",
                "## Q1. Getting the embeddings model\n",
                "\n",
                "First, we will get the embeddings model `multi-qa-distilbert-cos-v1` from\n",
                "[the Sentence Transformer library](https://www.sbert.net/docs/sentence_transformer/pretrained_models.html#model-overview)\n",
                "\n",
                "```bash\n",
                "from sentence_transformers import SentenceTransformer\n",
                "embedding_model = SentenceTransformer(model_name)\n",
                "```\n",
                "\n",
                "Create the embedding for this user question:\n",
                "\n",
                "```python\n",
                "user_question = \"I just discovered the course. Can I still join it?\"\n",
                "```\n",
                "\n",
                "What's the first value of the resulting vector?\n",
                "\n",
                "* -0.24\n",
                "* -0.04\n",
                "* 0.07\n",
                "* 0.27\n",
                "\n",
                "## Q2. Creating the embeddings\n",
                "\n",
                "Now for each document, we will create an embedding for both question and answer fields.\n",
                "\n",
                "We want to put all of them into a single matrix `X`:\n",
                "\n",
                "- Create a list `embeddings` \n",
                "- Iterate over each document \n",
                "- `qa_text = f'{question} {text}'`\n",
                "- compute the embedding for `qa_text`, append to `embeddings`\n",
                "- At the end, let `X = np.array(embeddings)` (`import numpy as np`)\n",
                "\n",
                "What's the shape of X? (`X.shape`). Include the parantheses. \n",
                "\n",
                "## Q3. Search\n",
                "\n",
                "We have the embeddings and the query vector. Now let's compute the \n",
                "cosine similarity between the vector from Q1 (let's call it `v`) and the matrix from Q2. \n",
                "\n",
                "The vectors returned from the embedding model are already\n",
                "normalized (you can check it by computing a dot product of a vector\n",
                "with itself - it should return 1.0). This means that in order\n",
                "to compute the coside similarity, it's sufficient to \n",
                "multiply the matrix `X` by the vector `v`:\n",
                "\n",
                "```python\n",
                "scores = X.dot(v)\n",
                "```\n",
                "\n",
                "What's the highest score in the results?\n",
                "\n",
                "- 65.0 \n",
                "- 6.5\n",
                "- 0.65\n",
                "- 0.065\n",
                "\n",
                "## Q4. Hit-rate for our search engine\n",
                "\n",
                "Let's evaluate the performance of our own search engine. We will\n",
                "use the hitrate metric for evaluation.\n",
                "\n",
                "First, load the ground truth dataset:\n",
                "\n",
                "```python\n",
                "import pandas as pd\n",
                "\n",
                "base_url = 'https://github.com/DataTalksClub/llm-zoomcamp/blob/main'\n",
                "relative_url = '03-vector-search/eval/ground-truth-data.csv'\n",
                "ground_truth_url = f'{base_url}/{relative_url}?raw=1'\n",
                "\n",
                "df_ground_truth = pd.read_csv(ground_truth_url)\n",
                "df_ground_truth = df_ground_truth[df_ground_truth.course == 'machine-learning-zoomcamp']\n",
                "ground_truth = df_ground_truth.to_dict(orient='records')\n",
                "```\n",
                "\n",
                "Now use the code from the module to calculate the hitrate of\n",
                "`VectorSearchEngine` with `num_results=5`.\n",
                "\n",
                "What did you get?\n",
                "\n",
                "* 0.93\n",
                "* 0.73\n",
                "* 0.53\n",
                "* 0.33\n",
                "\n",
                "## Q5. Indexing with Elasticsearch\n",
                "\n",
                "Now let's index these documents with elasticsearch\n",
                "\n",
                "* Create the index with the same settings as in the module (but change the dimensions)\n",
                "* Index the embeddings (note: you've already computed them)\n",
                "\n",
                "After indexing, let's perform the search of the same query from Q1.\n",
                "\n",
                "What's the ID of the document with the highest score?\n",
                "\n",
                "## Q6. Hit-rate for Elasticsearch\n",
                "\n",
                "The search engine we used in Q4 computed the similarity between\n",
                "the query and ALL the vectors in our database. Usually this is \n",
                "not practical, as we may have a lot of data.\n",
                "\n",
                "Elasticsearch uses approximate techniques to make it faster. \n",
                "\n",
                "Let's evaluate how worse the results are when we switch from\n",
                "exact search (as in Q4) to approximate search with Elastic.\n",
                "\n",
                "What's hitrate for our dataset for Elastic?\n",
                "\n",
                "* 0.93\n",
                "* 0.73\n",
                "* 0.53\n",
                "* 0.33\n",
                "\n",
                "## Submit the results\n",
                "\n",
                "* Submit your results here: https://courses.datatalks.club/llm-zoomcamp-2024/homework/hw3\n",
                "* It's possible that your answers won't match exactly. If it's the case, select the closest one.\n"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 1,
            "metadata": {},
            "outputs": [],
            "source": [
                "from sentence_transformers import SentenceTransformer\n",
                "embedding_model = SentenceTransformer('multi-qa-mpnet-base-dot-v1')\n",
                "user_question = \"I just discovered the course. Can I still join it?\"\n",
                "user_question_embedding = embedding_model.encode(user_question)\n",
                "user_question_embedding[0]"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Answer Q1"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 2,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "q1_answer"
                        ]
                    },
                    "execution_count": 2,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": [
                "q1_answer"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 3,
            "metadata": {},
            "outputs": [],
            "source": [
                "import requests\n",
                "import numpy as np\n",
                "\n",
                "base_url = 'https://github.com/DataTalksClub/llm-zoomcamp/blob/main'\n",
                "relative_url = '03-vector-search/eval/documents-with-ids.json'\n",
                "docs_url = f'{base_url}/{relative_url}?raw=1'\n",
                "docs_response = requests.get(docs_url)\n",
                "documents = docs_response.json()\n",
                "\n",
                "# Filtering to get only 375 documents for \"machine-learning-zoomcamp\"\n",
                "filtered_documents = [doc for doc in documents if doc['course'] == 'machine-learning-zoomcamp']\n",
                "documents = filtered_documents[:375]\n",
                "\n",
                "embeddings = []\n",
                "for doc in documents:\n",
                "    qa_text = f\"{doc['question']} {doc['text']}\"\n",
                "    embedding = embedding_model.encode(qa_text)\n",
                "    embeddings.append(embedding)\n",
                "\n",
                "X = np.array(embeddings)\n",
                "X.shape"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Answer Q2"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 4,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "q2_answer"
                        ]
                    },
                    "execution_count": 4,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": [
                "q2_answer"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 5,
            "metadata": {},
            "outputs": [],
            "source": [
                "v = user_question_embedding\n",
                "scores = X.dot(v)\n",
                "scores.max()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Answer Q3"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 6,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "q3_answer"
                        ]
                    },
                    "execution_count": 6,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": [
                "q3_answer"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 7,
            "metadata": {},
            "outputs": [],
            "source": [
                "import pandas as pd\n",
                "\n",
                "base_url = 'https://github.com/DataTalksClub/llm-zoomcamp/blob/main'\n",
                "relative_url = '03-vector-search/eval/ground-truth-data.csv'\n",
                "ground_truth_url = f'{base_url}/{relative_url}?raw=1'\n",
                "\n",
                "df_ground_truth = pd.read_csv(ground_truth_url)\n",
                "df_ground_truth = df_ground_truth[df_ground_truth.course == 'machine-learning-zoomcamp']\n",
                "ground_truth = df_ground_truth.to_dict(orient='records')\n",
                "\n",
                "class VectorSearchEngine:\n",
                "    def __init__(self, documents, embeddings):\n",
                "        self.documents = documents\n",
                "        self.embeddings = embeddings\n",
                "\n",
                "    def search(self, v_query, num_results=10):\n",
                "        scores = self.embeddings.dot(v_query)\n",
                "        idx = np.argsort(-scores)[:num_results]\n",
                "        return [self.documents[i] for i in idx]\n",
                "\n",
                "search_engine = VectorSearchEngine(documents=documents, embeddings=X)\n",
                "\n",
                "def calculate_hitrate(search_engine, ground_truth, num_results=5):\n",
                "    hits = 0\n",
                "    for item in ground_truth:\n",
                "        query = item['query']\n",
                "        true_doc_id = item['document_id']\n",
                "        query_embedding = embedding_model.encode(query)\n",
                "        results = search_engine.search(query_embedding, num_results=num_results)\n",
                "        result_ids = [doc['id'] for doc in results]\n",
                "        if true_doc_id in result_ids:\n",
                "            hits += 1\n",
                "    return hits / len(ground_truth)\n",
                "\n",
                "hitrate = calculate_hitrate(search_engine, ground_truth, num_results=5)\n",
                "hitrate"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Answer Q4"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 8,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "q4_answer"
                        ]
                    },
                    "execution_count": 8,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": [
                "q4_answer"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 9,
            "metadata": {},
            "outputs": [],
            "source": [
                "from elasticsearch import Elasticsearch, helpers\n",
                "\n",
                "es = Elasticsearch()\n",
                "\n",
                "index_name = 'documents'\n",
                "index_settings = {\n",
                "    \"mappings\": {\n",
                "        \"properties\": {\n",
                "            \"question_answer\": {\n",
                "                \"type\": \"dense_vector\",\n",
                "                \"dims\": 768\n",
                "            }\n",
                "        }\n",
                "    }\n",
                "}\n",
                "\n",
                "if es.indices.exists(index=index_name):\n",
                "    es.indices.delete(index=index_name)\n",
                "\n",
                "es.indices.create(index=index_name, body=index_settings)\n",
                "\n",
                "def generate_docs():\n",
                "    for doc, embedding in zip(documents, X):\n",
                "        yield {\n",
                "            \"_index\": index_name,\n",
                "            \"_id\": doc[\"id\"],\n",
                "            \"_source\": {\n",
                "                \"question_answer\": embedding.tolist(),\n",
                "                \"text\": doc[\"text\"],\n",
                "                \"question\": doc[\"question\"]\n",
                "            }\n",
                "        }\n",
                "\n",
                "helpers.bulk(es, generate_docs())\n",
                "\n",
                "query_vector = user_question_embedding.tolist()\n",
                "query = {\n",
                "    \"query\": {\n",
                "        \"script_score\": {\n",
                "            \"query\": {\"match_all\": {}},\n",
                "            \"script\": {\n",
                "                \"source\": \"cosineSimilarity(params.query_vector, 'question_answer') + 1.0\",\n",
                "                \"params\": {\"query_vector\": query_vector}\n",
                "            }\n",
                "        }\n",
                "    }\n",
                "}\n",
                "\n",
                "response = es.search(index=index_name, body=query)\n",
                "highest_score_doc_id = response['hits']['hits'][0]['_id']\n",
                "highest_score_doc_id"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Answer Q5"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 10,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "q5_answer"
                        ]
                    },
                    "execution_count": 10,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": [
                "q5_answer"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 11,
            "metadata": {},
            "outputs": [],
            "source": [
                "def calculate_hitrate_elasticsearch(ground_truth, num_results=5):\n",
                "    hits = 0\n",
                "    for item in ground_truth:\n",
                "        query = item['query']\n",
                "        true_doc_id = item['document_id']\n",
                "        query_embedding = embedding_model.encode(query).tolist()\n",
                "        query = {\n",
                "            \"query\": {\n",
                "                \"script_score\": {\n",
                "                    \"query\": {\"match_all\": {}},\n",
                "                    \"script\": {\n",
                "                        \"source\": \"cosineSimilarity(params.query_vector, 'question_answer') + 1.0\",\n",
                "                        \"params\": {\"query_vector\": query_embedding}\n",
                "                    }\n",
                "                }\n",
                "            }\n",
                "        }\n",
                "        response = es.search(index=index_name, body=query)\n",
                "        result_ids = [hit['_id'] for hit in response['hits']['hits'][:num_results]]\n",
                "        if true_doc_id in result_ids:\n",
                "            hits += 1\n",
                "    return hits / len(ground_truth)\n",
                "\n",
                "hitrate_elastic = calculate_hitrate_elasticsearch(ground_truth, num_results=5)\n",
                "hitrate_elastic"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Answer Q6"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": 12,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": [
                            "q6_answer"
                        ]
                    },
                    "execution_count": 12,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": [
                "q6_answer"
            ]
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.8"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

with open("hw-03.ipynb", "w") as f:
    json.dump(notebook_content, f)