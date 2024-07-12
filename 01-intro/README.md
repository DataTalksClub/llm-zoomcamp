# Module 1: Introduction
 
In this module, we will learn what LLM and RAG are and
implement a simple RAG pipeline to answer questions about 
the FAQ Documents from our Zoomcamp courses

What we will do: 

* Index Zoomcamp FAQ documents
    * DE Zoomcamp: https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit
    * ML Zoomcamp: https://docs.google.com/document/d/1LpPanc33QJJ6BSsyxVg-pWNMplal84TdZtq10naIhD8/edit
    * MLOps Zoomcamp: https://docs.google.com/document/d/12TlBfhIiKtyBv8RnsoJR6F72bkPDGEvPOItJIxaEzE0/edit
* Create a Q&A system for answering questions about these documents 

## 1.1 Introduction to LLM and RAG

<a href="https://www.youtube.com/watch?v=Q75JgLEXMsM&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/Q75JgLEXMsM">
</a>

* LLM
* RAG
* RAG architecture
* Course outcome


## 1.2 Preparing the Environment

<a href="https://www.youtube.com/watch?v=ozCpmkbJNJE&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/ozCpmkbJNJE">
</a>

* Installing libraries
* Alternative: installing anaconda or miniconda

```bash
pip install tqdm notebook==7.1.2 openai elasticsearch pandas scikit-learn ipywidgets
```

## 1.3 Retrieval

<a href="https://www.youtube.com/watch?v=olvem333Bqo&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/olvem333Bqo">
</a>

* We will use the search engine we build in the [build-your-own-search-engine workshop](https://github.com/alexeygrigorev/build-your-own-search-engine): [minsearch](https://github.com/alexeygrigorev/minsearch)
* Indexing the documents
* Peforming the search


## 1.4 Generation with OpenAI

<a href="https://www.youtube.com/watch?v=qz316T3U49Q&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/qz316T3U49Q">
</a>

* Invoking OpenAI API
* Building the prompt
* Getting the answer


If you don't want to use a service, you can run an LLM locally
refer to [module 2](../02-open-source/) for more details.

In particular, check "2.7 Ollama - Running LLMs on a CPU" - 
it can work with OpenAI API, so to make the example from 1.4 
work locally, you only need to change a few lines of code.


## 1.4.2 OpenAI API Alternatives

<a href="https://www.youtube.com/watch?v=HObjFso2UJE&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/HObjFso2UJE">
</a>

[Open AI Alternatives](../awesome-llms.md#openai-api-alternatives)


## 1.5 Cleaned RAG flow

<a href="https://www.youtube.com/watch?v=vkTiVwwch6A&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/vkTiVwwch6A">
</a>

* Cleaning the code we wrote so far
* Making it modular

## 1.6 Searching with ElasticSearch

<a href="https://www.youtube.com/watch?v=1lgbR5wMvsI&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/1lgbR5wMvsI">
</a>

* Run ElasticSearch with Docker
* Index the documents
* Replace MinSearch with ElasticSearch

Running ElasticSearch:

```bash
docker run -it \
    --rm \
    --name elasticsearch \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    docker.elastic.co/elasticsearch/elasticsearch:8.4.3
```

If the previous command doesn't work (i.e. you see "error pulling image configuration"), try to run ElasticSearch directly from Docker Hub:

```bash
docker run -it \
    --rm \
    --name elasticsearch \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    elasticsearch:8.4.3
```

Index settings:

```python
{
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
        "properties": {
            "text": {"type": "text"},
            "section": {"type": "text"},
            "question": {"type": "text"},
            "course": {"type": "keyword"} 
        }
    }
}
```

Query:

```python
{
    "size": 5,
    "query": {
        "bool": {
            "must": {
                "multi_match": {
                    "query": query,
                    "fields": ["question^3", "text", "section"],
                    "type": "best_fields"
                }
            },
            "filter": {
                "term": {
                    "course": "data-engineering-zoomcamp"
                }
            }
        }
    }
}
```

We use `"type": "best_fields"`. You can read more about 
different types of `multi_match` search in [elastic-search.md](elastic-search.md).

# 1.7 Homework
More information [here](../cohorts/2024/01-intro/homework.md).


# Extra materials

* If you're curious to know how the code for parsing the FAQ works, check [this video](https://www.loom.com/share/ff54d898188b402d880dbea2a7cb8064)

# Notes

* [Notes by slavaheroes](https://github.com/slavaheroes/llm-zoomcamp/blob/homeworks/01-intro/notes.md)
* [Notes by Pham Nguyen Hung](https://hung.bearblog.dev/llm-zoomcamp-1-rag/)
* [Notes by dimzachar](https://github.com/dimzachar/llm_zoomcamp/blob/master/notes/01-intro/README.md)
* [Notes by Olawale Ogundeji](https://github.com/presiZHai/LLM-Zoomcamp/blob/main/01-intro/notes.md)
* [Notes by Uchechukwu](https://medium.com/@njokuuchechi/an-intro-to-large-language-models-llms-0c51c09abe10)
* [Notes by Kamal](https://github.com/mk-hassan/llm-zoomcamp/blob/main/Module-1%3A%20Introduction%20to%20LLMs%20and%20RAG/README.md)
* [Notes by Marat](https://machine-mind-ml.medium.com/discovering-semantic-search-and-rag-with-large-language-models-be7d9ba5bef4)
* [Notes by Waleed](https://waleedayoub.com/post/llmzoomcamp_week1-intro_notes/)
* Did you take notes? Add them above this line (Send a PR with *links* to your notes)
