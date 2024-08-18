# Module 6: Best practices

In this module, we'll cover the techniques that could improve your RAG pipeline.

## 6.1 Techniques to Improve RAG Pipeline

<a href="https://www.youtube.com/watch?v=Tq9Vbm_2z3o">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/Tq9Vbm_2z3o">
</a>

* Small-to-Big chunk retrieval
* Leveraging document metadata
* Hybrid search
* User query rewriting
* Document reranking

Links:
* Slides (TBD)
* [Five Techniques for Improving RAG Chatbots - Nikita Kozodoi [Video]](https://www.youtube.com/watch?v=xPYmClWk5O8)
* [Survey on RAG techniques [Article]](https://arxiv.org/abs/2312.10997)


## 6.2 Hybrid search

<a href="https://www.youtube.com/watch?v=TQ_ck6Q9gSQ">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/TQ_ck6Q9gSQ">
</a>



Links:
* [Notebook](hybrid-search-and-reranking-es.ipynb)
* [Hybrid search [Elasticsearch Guide]](https://www.elastic.co/guide/en/elasticsearch/reference/current/knn-search.html#_combine_approximate_knn_with_other_features)
* [Hybrid search [Tutorial]](https://www.elastic.co/search-labs/tutorials/search-tutorial/vector-search/hybrid-search)


## 6.3 Document Reranking

<a href="https://www.youtube.com/watch?v=H4M55Ptc5cM">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/H4M55Ptc5cM">
</a>

Links:
* [Reciprocal Rank Fusion (RRF) method [Elasticsearch Guide]](https://www.elastic.co/guide/en/elasticsearch/reference/current/rrf.html)
* [RRF method [Article]](https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf)
* [Elasticsearch subscription plans](https://www.elastic.co/subscriptions)

We should pull and run a docker container with Elasticsearch 8.9.0 or higher in order to use reranking based on RRF algorithm:

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


## 6.4 TBD


## Homework

TBD