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

TBA

# Notes

* First link goes here
* Did you take notes? Add them above this line (Send a PR with *links* to your notes)
