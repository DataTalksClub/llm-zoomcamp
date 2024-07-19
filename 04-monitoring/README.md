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

Video https://www.loom.com/share/5060441af07e4e48b95e27f547e0d2de

Links:

* [notebook](offline-rag-evaluation.ipynb)
* [results-gpt4o.csv](data/results-gpt4o.csv) (answers from GPT-4o)
* [results-gpt35.csv](data/results-gpt35.csv) (answers from GPT-3.5-Turbo)


## 4.4 Offline RAG evaluation: cosine similarity

Video https://www.loom.com/share/0c11d5ff380c4435b39c85c3c22b5485


Content

* A->Q->A' cosine similarity
* Evaluating gpt-4o
* Evaluating gpt-3.5-turbo
* Evaluating gpt-4o-mini



Links:

* [notebook](offline-rag-evaluation.ipynb)
* [results-gpt4o-cosine.csv](data/results-gpt4o-cosine.csv) (answers with cosine calculated from GPT-4o)
* [results-gpt35-cosine.csv](data/results-gpt35-cosine.csv) (answers with cosine calculated from GPT-3.5-Turbo)
* [results-gpt4o-mini.csv](data/results-gpt4o-mini.csv) (answers from GPT-4o-mini)
* [results-gpt4o-mini-cosine.csv](data/results-gpt4o-mini-cosine.csv) (answers with cosine calculated from GPT-4o-mini)


## 4.5 Offline RAG evaluation: LLM as a judge

Video https://www.loom.com/share/23182538903d4de695d0ddd62716ce2c

* LLM as a judge
* A->Q->A' evaluation
* Q->A evaluation


Links:

* [notebook](offline-rag-evaluation.ipynb)
* [evaluations-aqa.csv](data/evaluations-aqa.csv) (A->Q->A evaluation results)
* [evaluations-qa.csv](data/evaluations-qa.csv) (Q->A evaluation results)


## 4.6 Capturing user feedback

Video https://www.loom.com/share/4fceb69e42404865b4b1b5ecf2c68a51


Content

* Adding +1 and -1 buttons
* Setting up a postgres database
* Putting everything in docker compose

```bash
pip install pgcli
pgcli -h localhost -U your_username -d course_assistant -W
```

Links:

* [code](app/)


### 4.6.2 Capturing user feedback: part 2 

Video https://www.loom.com/share/6fe890a7b5cb478cba9ccc05db35851e

* adding vector search
* adding OpenAI

Links:

* [code](app/)


## 4.7 Monitoring answer quality

* Setting up Grafana
* Sentiment analysis
* LLM as a judge


## Homework

tbd.
