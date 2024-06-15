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
pip install tqdm notebook==7.1.2 openai elasticsearch pandas scikit-learn
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

[Open AI Alternatives](open-ai-alternatives.md)


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
    --name elasticsearch \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    docker.elastic.co/elasticsearch/elasticsearch:8.4.3
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



# Notes

## Highlights Module 1
### Module 1.1
* Introduction to LLM and RAG frameworks🎓
*  Understanding language models and their predictive nature🔍
*  Exploring the retrieval-generation framework for enhanced answers📚
*  Using search to augment text generation in RAG🧠
*  Implementing the RAG framework with different tools⚙️
*  Building your own Q&A system in the course🛠️

### Module 1.2
*  Setting up GitHub Codespaces for environment configuration🛠️
*  Installing required libraries like Jupyter Notebook and OpenAI📦
* Setting up API keys for OpenAI🗝️
*  Committing changes to GitHub📝
*  Installing Anaconda as an alternative environment setup🚀
*  Ensuring security by managing API keys and sensitive information🛡️ 
### Module 1.3
*  Implementing a search engine from a previous workshop for data retrieval🔍
*  Indexing FAQ documents to the search engine for search functionality📦 
*  Performing a search query with boosts and filtering for relevant results📝
*  Utilising retrieved documents to build a context for an LLM prompt🧠
### Module 1.4
*  Indexing documents in a search engine to retrieve answers 📚
*  Using OpenAI GPT 4.0 for generating context-based responses 🤖
*  Creating a prompt template to enhance answer quality 🎨
*  Iterating over documents to build context for the prompt ⚙️
*  Sending the prompt to OpenAI GPT 4.0 for accurate answers ✉️
*  Improving modularity for easy database and LLM replacements 🔄
*  Focus on clean code and logic for future scalability 🧹
### Module 1.5
*  Modularizing code for easier use and component replacement 🛠️
*  Demonstrating the search, prompt building, and LM answer flow 🔄
*  Creating functions for search, prompt building, and LM interaction 🧩
*  Testing and refining the code for accuracy and functionality 🧪
*  Simplifying the process with a single “rock” function 🪨
*  Easily swapping components like search engines or LMs for flexibility 🔄
*  Showing the power of modular code for adaptability and efficiency 💡
### Module 1.6
*  Using Elasticsearch to replace a toy search engine for better performance🚀
*  Importance of persistent data storage in Elasticsearch compared to in-memory search engines💡 
*  Running Elasticsearch in Docker for easy deployment🐳
* Adding a progress bar for indexing data in Elasticsearch📊
* Modularity allows easy swapping of components like the search engine🤖 
* Understanding the complex query syntax and filtering in Elasticsearch🧠 
* Creating functions to interact with Elasticsearch for efficient search operations🛠️ 



* Replace it with a link
* Did you take notes? Add them above this line
