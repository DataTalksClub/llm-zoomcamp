# Data Preparation in RAG

## Getting started

1. Clone [repository](https://github.com/mage-ai/rag-project)
```bash
git clone https://github.com/mage-ai/rag-project
cd rag-project
```
3. navigate to the `rag-project/llm` directory, add `spacy` to the requirements.txt.
4. Then update the `Dockerfile` found in the `rag-project` directory with the following:
```YAML
RUN python -m spacy download en_core_web_sm
```
4. Run

```bash
`./scripts/start.sh`
```

Once started, go to [http://localhost:6789/](http://localhost:6789/)

For more setup information, refer to these [instructions](https://docs.mage.ai/getting-started/setup#docker-compose-template)


## 0. Module overview

<a href="https://www.youtube.com/watch?v=gP2ZOsG9Umg&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/gP2ZOsG9Umg">
</a>

## 1. Ingest

In this section, we cover the ingestion of documents from a single data source.

<a href="https://www.youtube.com/watch?v=9BJppvgLINc&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/9BJppvgLINc">
</a>

* [Code](https://github.com/mage-ai/rag-project/blob/master/llm/rager/data_loaders/runic_oblivion.py)
* [Document link for API Data Loader](https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/01-intro/documents.json)

## 2. Chunk

Once data is ingested, we break it into manageable chunks.

The Q&A data is already chunked - the texts are small
and easy to process and index. But other datasets might
not be (book texts, transcripts, etc). 

In this video, we will talk about turning large texts
into smaller documents - i.e. chunking.

<a href="https://www.youtube.com/watch?v=H2oq5GSCKhM&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/H2oq5GSCKhM">
</a>


[Code](https://github.com/mage-ai/rag-project/blob/master/llm/rager/transformers/radiant_photon.py)

## 3. Tokenization

Tokenization is a crucial step in text processing and preparing the data for effective retrieval.

<a href="https://www.youtube.com/watch?v=hrMrqRgZryg&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/hrMrqRgZryg">
</a>

[Code](https://github.com/mage-ai/rag-project/blob/master/llm/rager/transformers/vivid_nexus.py)

## 4. Embed

Embedding data translates text into numerical vectors that can be processed by models.

Previously we used sentence transformers for that. In this video we show a different strategy for it.


<a href="https://www.youtube.com/watch?v=8wrArv0DEKc&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/8wrArv0DEKc">
</a>


[Code](https://github.com/mage-ai/rag-project/blob/master/llm/rager/transformers/prismatic_axiom.py)


## 5. Export

After processing, data needs to be exported for storage so that it can be retrieved for better contextualization of user queries.

Here we will save the embeddings to elasticsearch

please make sure to use the name given to your elasticsearch service in your docker compose file followed by the port as the connection string, e.g below

`<docker-compose-service-name><port>` http://elasticsearch:9200


<a href="https://www.youtube.com/watch?v=cHrphSoRBX4&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/cHrphSoRBX4">
</a>

[Code](https://github.com/mage-ai/rag-project/blob/master/llm/rager/data_exporters/numinous_fission.py)

## 6. Retrieval: Test Vector Search Query

After exporting the chunks and embeddings, we can test the search query to retrieve relevant documents on sample queries.

<a href="https://www.youtube.com/watch?v=z5NqDcaBglY&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/z5NqDcaBglY">
</a>

[Code](code/06_retrieval.py)

## 7. Trigger Daily Runs

Automation is key to maintaining and updating your system.
This section demonstrates how to schedule and trigger daily runs for your data pipelines, ensuring up-to-date and consistent data processing.

<a href="https://www.youtube.com/watch?v=nuk7_soKMUA&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/nuk7_soKMUA">
</a>

## Homework

In this homework we will build an end to end Retrieval-Augmented Generation inference pipeline and answer some questions about the returns 

### Q1: Run Mage

First, let's run Mage using the code below.
```Bash
git clone https://github.com/mage-ai/rag-project
cd rag-project
./scripts/start.sh
```
What's the version of Mage we run?

You will need to install / run the following from your terminal in Mage:
```Python
pip install spacy
pip install python-docx
pip install spacy-embedding
pip install sentence-transformers
python -m spacy download en_core_web_sm
```
### Q2: Initialize a RAG orchestration pipeline

Create a new RAG pipeline in Mage and import the FAQ documents using methods you learned from module 1. 

*Hint, use the `fetch` method to import the documents, include the `clean_lines` function and the `parse_document` function in the data loader*

How many FAQ documents were imported?
1. [ ] 2
1. [ ] 3
1. [ ] 4
1. [ ] 5

### Q3: Chunk the documents

Copy the code below into a Transformer chunking block

```Python
import re
from typing import Any, Dict, List


@transformer
def chunk_documents(data: List[Dict[str, Any]], *args, **kwargs):
    documents = []
    
    for idx, item in enumerate(data):
        course = item['course']
        
        for info in item['documents']:
            section = info['section']
            question = info['question']
            answer = info['text']
            
            # Generate a unique document ID
            document_id = ':'.join([re.sub(r'\W', '_', part) 
	            for part in [course, section, question]]).lower()
            
            # Format the document string
            chunk = '\n'.join([
                f'course:\n{course}\n',
                f'section:\n{section}\n',
                f'question:\n{question}\n',
                f'answer:\n{answer}\n',
            ])
            
            documents.append(dict(
                chunk=chunk,
                document=info,
	            document_id=document_id,
            ))

    print(f'Documents:', len(documents))
            
    return [documents]
```
Report the number of questions that were returned from this block?
1. [ ] 900
1. [ ] 948
1. [ ] 1026
1. [ ] 1445

### Q4: Lemmatize Documents

Copy the code below into a tokenization (Lemmatization Spacy) block

```Python
from typing import Dict, List

import spacy


@transformer
def lemmatize_text(documents: List[Dict], *args, **kwargs) -> List[Dict]:
    count = len(documents)
    print('Documents', count)

    nlp = spacy.load('en_core_web_sm')

    data = []

    for idx, document in enumerate(documents):
        document_id = document['document_id']
        if idx % 100 == 0:
            print(f'{idx + 1}/{count}')

        # Process the text chunk using spaCy
        chunk = document['chunk']
        doc = nlp(chunk)
        tokens = [token.lemma_ for token in doc]

        data.append(
            dict(
                chunk=chunk,
                document_id=document_id,
                tokens=tokens,
            )
        )

    print('\nData', len(data))

    return [data]
```
Based on the output of the `lemmatize_text` function, what is the main purpose of the returned `tokens` list in each dictionary?

**Options:**
1. [ ] To store the original text chunks without any modifications.
1. [ ] To store the document IDs and their corresponding metadata.
1. [ ] To store the lemmatized forms of each token in the text chunk.
1. [ ] To store the sentences from the original text chunk.

### Q5 Embeddings using sentence transformers

Copy the code below and run it in an custom code embedding transformer
```Python
from typing import Any, Dict, List
import spacy
from sentence_transformers import SentenceTransformer
import numpy as np

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(documents: List[Dict], *args, **kwargs) -> Dict[str, Any]:

    # Load the SpaCy model once
    nlp = spacy.load('en_core_web_sm')
    
    # Load the Sentence Transformers model once
    model = SentenceTransformer('all-mpnet-base-v2')
    
    data = []
    count = len(documents)
    print('Documents', count)
    
    for idx, document in enumerate(documents):
        if idx % 100 == 0:
            print(f'{idx + 1}/{count}')
        
        tokens = document['tokens']
    
        # Lemmatize tokens using SpaCy
        lemmas = [token.lemma_ for token in nlp(' '.join(tokens))]
        
        # Combine lemmas back into a single string of text used for embedding
        text = ' '.join(lemmas)
        
        # Generate embeddings using Sentence Transformers
        embedding = model.encode(text).tolist()
    
        data.append(dict(
            chunk=document['chunk'],
            document_id=document['document_id'],
            embedding=embedding,
        ))
    
    # Compute and report the average embedding length
    embeddings = [doc['embedding'] for doc in data]
    avg_embedding_length = np.mean([len(emb) for emb in embeddings])
    print("Average embedding length:", avg_embedding_length)
    
    return {
        'documents': data,
        'avg_embedding_length': avg_embedding_length
    }
```
What is the average embedding length ?

1. [ ] 750
1. [ ] 768
1. [ ] 775
1. [ ] 810

### Q6 Load embeddings to Elasticsearch

Copy the code below into an Vector Database (Elasticsearch) block and run the code.
```Python
from typing import Dict, List, Tuple, Union, Any
import json
import numpy as np
from elasticsearch import Elasticsearch

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_to_elasticsearch(data: Dict[str, Any], *args, **kwargs):
    """
    Export the processed data to an Elasticsearch index.

    Args:
        data (Dict[str, Any]): The data to be exported, which includes processed documents and average embedding length.
    """
    connection_string = kwargs.get('connection_string', 'http://localhost:9200')
    index_name = kwargs.get('index_name', 'documents')
    number_of_shards = kwargs.get('number_of_shards', 1)
    number_of_replicas = kwargs.get('number_of_replicas', 0)
    documents = data['documents']
    dimensions = kwargs.get('dimensions')

    if dimensions is None:
        for document in documents:
            if 'embedding' in document:
                dimensions = len(document['embedding'])
                break

    if dimensions is None:
        raise ValueError("No embeddings found in documents to determine dimensions")

    es_client = Elasticsearch(connection_string)

    print(f'Connecting to Elasticsearch at {connection_string}')

    index_settings = {
        "settings": {
            "number_of_shards": number_of_shards,
            "number_of_replicas": number_of_replicas,
        },
        "mappings": {
            "properties": {
                "chunk": {"type": "text"},
                "document_id": {"type": "text"},
                "embedding": {"type": "dense_vector", "dims": dimensions}
            }
        }
    }

    # Recreate the index by deleting if it exists and then creating with new settings
    if es_client.indices.exists(index=index_name):
        es_client.indices.delete(index=index_name)
        print(f'Index {index_name} deleted')

    es_client.indices.create(index=index_name, body=index_settings)
    print('Index created with properties:')
    print(json.dumps(index_settings, indent=2))
    print('Embedding dimensions:', dimensions)

    count = len(documents)
    print(f'Indexing {count} documents to Elasticsearch index {index_name}')
    for idx, document in enumerate(documents):
        if idx % 100 == 0:
            print(f'{idx + 1}/{count}')

        if isinstance(document['embedding'], np.ndarray):
            document['embedding'] = document['embedding'].tolist()

        es_client.index(index=index_name, document=document)

    return [[d['embedding'] for d in documents[:10]]]
```
When exporting your Retrieval-Augmented Generation (RAG) pipeline to Elasticsearch, what data type was used to store the embeddings?

1. [ ] text
1. [ ] keyword
1. [ ] dense_vector
1. [ ] float

### Q7 Iterative retrieval query

Navigation to the inference pipeline and select the iterative retrieval (custom code) block. Copy the code below and run the block
```Python

from typing import Dict, List, Union

import numpy as np
from elasticsearch import Elasticsearch, exceptions

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def tokenize(text: str) -> List[str]:
    # Dummy tokenize function - replace with actual tokenization logic
    return text.split()

def embed(tokens: List[str]) -> np.ndarray:
    # Dummy embed function - replace with actual embedding logic
    return np.random.rand(768)  # Assuming 768 is the embedding dimension

@data_loader
def search(*args, **kwargs) -> List[Dict]:
    """
    query_embedding: Union[List[int], np.ndarray]
    """
    
    connection_string = kwargs.get('connection_string', 'http://host.docker.internal:9200')
    index_name = kwargs.get('index_name', 'documents')
    source = kwargs.get('source', "cosineSimilarity(params.query_vector, 'embedding') + 1.0")
    top_k = kwargs.get('top_k', 5)
    chunk_column = kwargs.get('chunk_column')#, 'content')

    user_query = "When is the next LLM Zoomcamp?"
    tokens = tokenize(user_query)
    query_embedding = embed(tokens)

    if isinstance(query_embedding, np.ndarray):
        query_embedding = query_embedding.tolist()

    script_query = {
        "script_score": {
            "query": {"match_all": {}},
            "script": {
                "source": source,
                "params": {"query_vector": query_embedding},
            }
        }
    }

    print("Sending script query:", script_query)

    es_client = Elasticsearch(connection_string)
    
    try:
        response = es_client.search(
            index=index_name,
            body={
                "size": top_k,
                "query": script_query,
                "_source": [chunk_column],
            },
        )

        print("Raw response from Elasticsearch:", response)

        results = []
        for hit in response['hits']['hits']:
            source = hit.get('_source', {})
            if chunk_column in source:
                results.append(source[chunk_column])
            else:
                print(f"Warning: '{chunk_column}' not found in document ID {hit['_id']}. Available fields: {list(source.keys())}")

        return results
    
    except exceptions.BadRequestError as e:
        print(f"BadRequestError: {e.info}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
```
What is the max score you returned after running the query?

1. [ ] 1.036011
1. [ ] 1.045001
1. [ ] 1.054201
1. [ ] If none of the above please enter your returned max score

# Notes

* First link goes here
* Did you take notes? Add them above this line (Send a PR with *links* to your notes)
