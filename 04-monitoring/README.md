# Module 4: Evaluation and Monitoring

In this module, we will learn how to evaluate and monitor our LLM and RAG system.

In the evaluation part, we assess the quality of our entire RAG
system before it goes live.

In the monitoring part, we collect, store and visualize
metrics to assess the answer quality of a deployed LLM. We also
collect chat history and user feedback.


## 4.1 Introduction to monitoring answer quality 

<a href="https://www.youtube.com/watch?v=OWqinqemCmk&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/OWqinqemCmk">
</a>

* Why monitoring LLM systems?
* Monitoring answer quality of LLMs 
* Monitoring answer quality with user feedback
* What else to monitor, that is not covered by this module? 


## 4.2 Offline vs Online (RAG) evaluation

<a href="https://www.youtube.com/watch?v=yTKGSqkhgI4&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/yTKGSqkhgI4">
</a>

* Modules recap
* Online vs offline evaluation
* Offline evaluation metrics 


## 4.3 Generating data for offline RAG evaluation

<a href="https://www.youtube.com/watch?v=yTO5sRw6x78&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/yTO5sRw6x78">
</a>

Links:

* [notebook](offline-rag-evaluation.ipynb)
* [results-gpt4o.csv](data/results-gpt4o.csv) (answers from GPT-4o)
* [results-gpt35.csv](data/results-gpt35.csv) (answers from GPT-3.5-Turbo)


## 4.4 Offline RAG evaluation: cosine similarity

<a href="https://www.youtube.com/watch?v=LlXclbD3pms&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/LlXclbD3pms">
</a>

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

<a href="https://www.youtube.com/watch?v=IB6jePK1s58&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/IB6jePK1s58">
</a>

* LLM as a judge
* A->Q->A' evaluation
* Q->A evaluation


Links:

* [notebook](offline-rag-evaluation.ipynb)
* [evaluations-aqa.csv](data/evaluations-aqa.csv) (A->Q->A evaluation results)
* [evaluations-qa.csv](data/evaluations-qa.csv) (Q->A evaluation results)
https://youtu.be/


## 4.6 Capturing user feedback

<a href="https://www.youtube.com/watch?v=XapKKBUMQ4M&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/XapKKBUMQ4M">
</a>

> You can see the prompts and the output from claude [here](code.md)

Content

* Adding +1 and -1 buttons
* Setting up a postgres database
* Putting everything in docker compose

```bash
pip install pgcli
pgcli -h localhost -U your_username -d course_assistant -W
```


Links:

* [final code](app/)
* [intermediate code from claude](code.md#46-capturing-user-feedback)


### 4.6.2 Capturing user feedback: part 2 

<a href="https://www.youtube.com/watch?v=BG8MlbidatA&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/BG8MlbidatA">
</a>

* adding vector search
* adding OpenAI

Links:

* [final code](app/)
* [intermediate code from claude](code.md#462-capturing-user-feedback-part-2)


## 4.7 Monitoring the system

<a href="https://www.youtube.com/watch?v=BQN0TOi2Rew&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/BQN0TOi2Rew">
</a>

* Setting up Grafana
* Tokens and costs
* QA relevance
* User feedback
* Other metrics

Links:

* [final code](app/)
* [SQL queries for Grafana](grafana.md)
* [intermediate code from claude](code.md#47-monitoring)

### 4.7.2 Extra Grafana video

<a href="https://www.youtube.com/watch?v=qGFAX5ra1G8&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/qGFAX5ra1G8">
</a>

* Grafana variables
* Exporting and importing dashboards

Links:

* [SQL queries for Grafana](grafana.md)
* [Grafana dashboard](dashboard.json)

## Homework

See [here](../cohorts/2024/04-monitoring/homework.md)


## Extra resources

### Overview of the module

![image](https://github.com/user-attachments/assets/0c5e932b-4fca-4d51-8b1c-93f4600861dc)

https://www.loom.com/share/1dd375ec4b0d458fabdfc2b841089031

# Notes

* First link goes here
* Did you take notes? Add them above this line (Send a PR with *links* to your notes)
