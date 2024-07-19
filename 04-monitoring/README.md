# Module 4: Monitoring

In this module, we will learn how to monitor our LLM and RAG system. We will collect, store and visualize metrics to assess the answer quality of LLMs as well as chat history and user feedback. 

## Prerequisites

Add `OPENAI_API_KEY` as environment variable

```bash
export OPENAI_API_KEY="your-api-key-here"
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


## 4.2 Offline vs Online (RAG) evaluation

https://www.loom.com/share/32dc487bf01a464a88fcd73a405f40a8

* Modules recap
* Online vs offline evaluation
* Offline evaluation metrics 


## 4.3 Generating data for offline RAG evaluation

Videos

* https://www.loom.com/share/5060441af07e4e48b95e27f547e0d2de
* https://www.loom.com/share/c48191701c614e7cb4293bd83c2d9175



## 4.4 Offline RAG evaluation: cosine similarity

Videos 

* https://www.loom.com/share/0c11d5ff380c4435b39c85c3c22b5485
* https://www.loom.com/share/ae945cb4cce1467f8d70f57365b0f2e3

Content

* A->Q->A' cosine similarity
* Evaluating gpt-4o
* Evaluating gpt-3.5-turbo
* Evaluating gpt-4o-mini


## 4.5 Offline RAG evaluation: LLM as a judge

* LLM as a judge

## 4.6 Capturing user feedback

Videos

* https://www.loom.com/share/4fceb69e42404865b4b1b5ecf2c68a51
* https://www.loom.com/share/eea246d55ec142d7b16ff7ce892ab9cf
Content

* Adding +1 and -1 buttons
* Setting up a postgres database
* Putting everything in docker compose

```bash
pip install pgcli
pgcli -h localhost -U your_username -d course_assistant -W
```


### 4.6.1 Capturing user feedback part 2 

https://www.loom.com/share/6fe890a7b5cb478cba9ccc05db35851e

* adding vector search
* adding OpenAI


## 4.7 Monitoring answer quality

* Setting up Grafana
* Sentiment analysis
* LLM as a judge



## Homework

tbd.
