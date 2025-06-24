# Vector Search 

## 2.1 Getting Started with Vector Search and Qdrant

<a href="https://www.youtube.com/watch?v=cX2vO1q2BGE&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/cX2vO1q2BGE">
</a>

Links: 

* Notebook: [sematic_search.ipynb](sematic_search.ipynb)


Install qdrant and fastembed:

```bash
pip install -q "qdrant-client[fastembed]>=1.14.2"
```

Run in Docker:

```bash
docker pull qdrant/qdrant

docker run -p 6333:6333 -p 6334:6334 \
   -v "$(pwd)/qdrant_storage:/qdrant/storage:z" \
   qdrant/qdrant
```


## 2.2 Embedding Text Data

<a href="https://www.youtube.com/watch?v=4lX6sbdrs84&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/4lX6sbdrs84">
</a>


## 2.3 Indexing

<a href="https://www.youtube.com/watch?v=TM5WxZ9EqoQ&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/TM5WxZ9EqoQ">
</a>


## 2.4 Search

<a href="https://www.youtube.com/watch?v=VX-jMVN5ZQI&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/VX-jMVN5ZQI">
</a>

## 2.5 RAG with Vector Search

<a href="https://www.youtube.com/watch?v=ZV905K81sE4&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/ZV905K81sE4">
</a>

Links: 

* Starter notebook: [rag-starter.ipynb](rag-starter.ipynb)
* Finished notebook: [rag.ipynb](rag.ipynb) 

## 2.6 Hybrid Search

<a href="https://www.youtube.com/watch?v=ZdbIk8AltDU&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/ZdbIk8AltDU">
</a>


Links:

* Notebook: [hybrid_search.ipynb](hybrid_search.ipynb)


## Homework

See [here](../cohorts/2025/02-vector-search/homework.md)


# Notes

* Notes from [2024 edition](../cohorts/2024/03-vector-search/)
* [Cohort 2025| Vector Search using Qdrant study guide & FAQ by Nitin Gupta](https://github.com/niting9881/llm-zoomcamp/blob/main/02-vector-search/README.md)
* Did you take notes? Add them above this line (Send a PR with *links* to your notes)
