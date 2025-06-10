# Vector Search 

Notebook: [sematic_search.ipynb](sematic_search.ipynb)

## 2.1 Getting Started with Vector Search and Qdrant

<a href="https://www.youtube.com/watch?v=cX2vO1q2BGE&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/cX2vO1q2BGE">
</a>

Install qdrant and fastembed:

```bash
pip install qdrant-client fastembed
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

TBA

## 2.6 Hybrid Search

TBA


## Homework

See [here](../cohorts/2025/02-vector-search/homework.md)


# Notes

* Notes from [2024 edition](../cohorts/2024/03-vector-search/)
* Did you take notes? Add them above this line (Send a PR with *links* to your notes)
