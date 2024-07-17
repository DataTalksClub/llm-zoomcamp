# Module 4: Monitoring

In this module, we will learn how to monitor our LLM and RAG system. We will collect, store and visualize metrics to assess the answer quality of LLMs as well as chat history and user feedback. 

## Prerequisites

Add OPENAI_API_KEY as environment variable
```
Mac/Linux: export OPENAI_API_KEY="your-api-key-here"
```
## 4.1 Introduction to monitoring answer quality 

<a href="https://www.youtube.com/watch?v=OWqinqemCmk&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/OWqinqemCmk">
</a>

* Why monitoring LLM systems?
* Monitoring answer quality of LLMs 
  * Compute different types of quality metrics
  * Store computed metrics in relational database
  * Use Grafana to visualize metrics over time
* Monitoring answer quality with user feedback
  * Store chat sessions and collect user feedback in database 
  * Connect database to Grafana to visualize user feedback and corresponding chat sessions
* What else to monitor, that is not covered by this module? 

## 4.2 Monitoring answer quality of LLMs
### 4.2.1 Creating ground-truth dataset
< placeholder for youtube video >

Partly recap from [3.3 Evaluating Retrieval](../03-vector-search/)
* Setting up Elastic Search database as docker-compose service
* Storing documents-with-ids.json in Elastic Search database
* Extending documents data with llm answer and corresponding vector

### 4.2.2 Computing and storing metrics
< placeholder for youtube video >

* Compute evaluation metrics (i.e. semantic similarity, negativity, LLM-as-a-judge) 
* Storing evaluation metrics in Postgres database

### 4.2.3 Retrieving and visualizing metrics
< placeholder for youtube video >

* Setting up Grafana frontend as docker-compose service and connect to Elastic Search datasource
* Retrieve metrics from Postgres database and visualize on Grafana dashboard

## 4.3 Monitoring answer quality with user feedback
### 4.3.1 Setting up chat frontend
<a href="https://www.youtube.com/watch?v=YNvVoLJh-9w&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/YNvVoLJh-9w">
</a>

* Setting up Streamlit as docker-compose service
* Create Streamlit dashboard to mimic live chat frontend including feedback button
* Generate answer with ChatGPT from OpenAI 

### 4.3.2 Storing chat history and feedback metrics
<a href="https://www.youtube.com/watch?v=u-4BixHyrG4&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/u-4BixHyrG4">
</a>

* Setting up Postgres as docker-compose service
* Store chat history and feedback in Postgres

### 4.3.3 Retrieving and visualizing metrics
<a href="https://www.youtube.com/watch?v=VWn0E4Apf9U&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/VWn0E4Apf9U">
</a>

* Setting up Grafana frontend as docker-compose service and connect to Postgres datasource
* Retrieve feedback metrics from Postgres and visualize on Grafana dashboard

## 4.4 Homework

tbd.
