# Vector Search 

## 3.1 Introduction to Vector Search

<a href="https://www.youtube.com/watch?v=C5AWdL3kg1Q&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/C5AWdL3kg1Q">
</a>

* [Slides](https://github.com/dataML007/elastic_search/blob/main/Introduction%20to%20Vector%20DB.pdf)


## 3.2 Semantic Search with Elasticsearch

<a href="https://www.youtube.com/watch?v=ptByfB_YcEg&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/ptByfB_YcEg">
</a>

* Notebook: [demo_es.ipynb](demo_es.ipynb)


## 3.3 Evaluating Retrieval 

### 3.3.1 Introduction

<a href="https://www.youtube.com/watch?v=APMrUnC_dy0&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/APMrUnC_dy0">
</a>

Plan for the section:

* Why do we need evaluation
* [Evaluation metrics](evaluation-metrics.md)
* Ground truth / gold standard data
* Generating ground truth with LLM
* Evaluating the search resuls


### 3.3.2 Getting ground truth data

<a href="https://www.youtube.com/watch?v=bpxi6fKcyLw&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/bpxi6fKcyLw">
</a>

* Approaches for getting evaluation data
* Using OpenAI to generate evaluation data

### 3.3.3 Ranking evaluation: text search

<a href="https://www.youtube.com/watch?v=fdIV4xCsp0c&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/fdIV4xCsp0c">
</a>

* Elasticsearch with text results
* minsearch

### 3.3.4 Ranking evaluation: vector search

<a href="https://www.youtube.com/watch?v=VRprIm9-VV8&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/VRprIm9-VV8">
</a>

* Elasticsearch with vector search
* Ranking with question, answer, question+answer embeddings


## Homework

See [here](../cohorts/2024/03-vector-search/homework.md)


# Notes

* Did you take notes? Add them above this line (Send a PR with *links* to your notes)
