# Module 5: Monitoring and Guardrails

In this module, we will learn how to monitor our LLM and RAG system. We will compute metrics during the ingestion pipeline as well as regarding the chat behavior and history. 

## Prerequisites

Add OPENAI_API_KEY as environment variable
```
Mac/Linux: export OPENAI_API_KEY="your-api-key-here"
```

## 5.1 Introduction to monitoring answer quality 
< placeholder for youtube video >
* Why monitoring LLM systems?
* Monitoring answer quality of LLMs <br>
  * Compute different types of quality metrics
  * Store computed metrics in relational database
  * Use Grafana to visualize metrics over time
* Monitoring answer quality with user feedback
  * Store chat sessions and collect user feedback in database 
  * Connect database to Grafana to visualize user feedback and corresponding chat sessions
* What else to monitor, that is not covered by this module? 

## 5.2 Monitoring answer quality of LLMs
### 5.2.1 Creating ground-truth dataset
< placeholder for youtube visdeo >

Partly recap from [3.3 Evaluating Retrieval](../03-vector-search/)
* Setting up Elastic Search database as docker-compose service
* Storing documents-with-ids.json in Elastic Search database
* Extending ground-truth-data.csv with retrieved context data from Elastic Search and llm answer

### 5.2.2 Computing and storing metrics
< placeholder for youtube video >

* Compute evaluation metrics (i.e. semantic similarity, LLM-as-a-judge) from groud-truth-data.csv
* Setting up Postgres database as docker-compose service
* Store evaluation metrics in Postgres

### 5.2.3 Retrieving and visualizing metrics
< placeholder for youtube video >

* Setting up Grafana frontend as docker-compose service and connect to Postgres datasource
* Retrieve metrics from Postgres and visualize on Grafana dashboard

## 5.3 Monitoring answer quality with user feedback
### 5.3.1 Setting up chat frontend
< placeholder for youtube video >

* Setting up Streamlit as docker-compose service
* Create Streamlit dashboard to mimic live chat frontend including feedback button
* Generate answer with ChatGPT from OpenAI 

### 5.3.2 Storing chat history and feedback metrics
< placeholder for youtube video >

* Setting up Postgres as docker-compose service
* Store chat history and feedback metrics in Postgres

### 5.3.3 Retrieving and visualizing metrics
< placeholder for youtube video >

* Setting up Grafana frontend as docker-compose service and connect to Postgres datasource
* Retrieve feedback metrics from Postgres and visualize on Grafana dashboard

## 5.4 Homework
