# Модуль 4: Оцінка та моніторинг

У цьому модулі ми навчимося оцінювати та моніторити наші LLM та RAG системи.

У частині оцінки ми аналізуємо якість всієї нашої RAG системи перед тим, як вона запуститься в дію.

У частині моніторингу ми збираємо, зберігаємо та візуалізуємо метрики для оцінки якості відповідей розгорнутої LLM. Ми також збираємо історію чатів та відгуки користувачів.


## 4.1 Вступ до моніторингу якості відповідей 

<a href="https://www.youtube.com/watch?v=OWqinqemCmk&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/OWqinqemCmk">
</a>

* Чому потрібно моніторити системи LLM?
* Моніторинг якості відповідей LLM 
* Моніторинг якості відповідей через відгуки користувачів
* Що ще потрібно моніторити, але не охоплюється в цьому модулі?


## 4.2 Офлайн та онлайн (RAG) оцінка

<a href="https://www.youtube.com/watch?v=yTKGSqkhgI4&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/yTKGSqkhgI4">
</a>

* Підсумок модулів
* Онлайн vs офлайн оцінка
* Метрики офлайн оцінки 


## 4.3 Генерація даних для офлайн оцінки RAG

<a href="https://www.youtube.com/watch?v=yTO5sRw6x78&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/yTO5sRw6x78">
</a>

Посилання:

* [ноутбук](offline-rag-evaluation.ipynb)
* [results-gpt4o.csv](data/results-gpt4o.csv) (відповіді GPT-4o)
* [results-gpt35.csv](data/results-gpt35.csv) (відповіді GPT-3.5-Turbo)


## 4.4 Офлайн оцінка RAG: косинусна схожість

<a href="https://www.youtube.com/watch?v=LlXclbD3pms&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/LlXclbD3pms">
</a>

Зміст:

* Косинусна схожість A->Q->A'
* Оцінка gpt-4o
* Оцінка gpt-3.5-turbo
* Оцінка gpt-4o-mini

Посилання:

* [ноутбук](offline-rag-evaluation.ipynb)
* [results-gpt4o-cosine.csv](data/results-gpt4o-cosine.csv) (відповіді з розрахованою косинусною схожістю від GPT-4o)
* [results-gpt35-cosine.csv](data/results-gpt35-cosine.csv) (відповіді з розрахованою косинусною схожістю від GPT-3.5-Turbo)
* [results-gpt4o-mini.csv](data/results-gpt4o-mini.csv) (відповіді від GPT-4o-mini)
* [results-gpt4o-mini-cosine.csv](data/results-gpt4o-mini-cosine.csv) (відповіді з розрахованою косинусною схожістю від GPT-4o-mini)


## 4.5 Офлайн оцінка RAG: LLM як суддя

<a href="https://www.youtube.com/watch?v=IB6jePK1s58&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/IB6jePK1s58">
</a>

* LLM як суддя
* Оцінка A->Q->A'
* Оцінка Q->A

Посилання:

* [ноутбук](offline-rag-evaluation.ipynb)
* [evaluations-aqa.csv](data/evaluations-aqa.csv) (результати оцінки A->Q->A)
* [evaluations-qa.csv](data/evaluations-qa.csv) (результати оцінки Q->A)


## 4.6 Збір відгуків користувачів

<a href="https://www.youtube.com/watch?v=XapKKBUMQ4M&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/XapKKBUMQ4M">
</a>

> Ви можете переглянути запити та відповіді від claude [тут](code.md)

Зміст:

* Додавання кнопок +1 і -1
* Налаштування бази даних postgres
* Збирання всього в docker compose

```bash
pip install pgcli
pgcli -h localhost -U your_username -d course_assistant -W
```

Посилання:

* [фінальний код](app/)
* [проміжний код від claude](code.md#46-capturing-user-feedback)


### 4.6.2 Збір відгуків користувачів: частина 2 

<a href="https://www.youtube.com/watch?v=BG8MlbidatA&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/BG8MlbidatA">
</a>

* додавання пошуку за векторами
* додавання OpenAI

Посилання:

* [фінальний код](app/)
* [проміжний код від claude](code.md#462-capturing-user-feedback-part-2)


## 4.7 Моніторинг системи

<a href="https://www.youtube.com/watch?v=BQN0TOi2Rew&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/BQN0TOi2Rew">
</a>

* Налаштування Grafana
* Токени та витрати
* Актуальність відповідей
* Відгуки користувачів
* Інші метрики

Посилання:

* [фінальний код](app/)
* [SQL запити для Grafana](grafana.md)
* [проміжний код від claude](code.md#47-monitoring)

### 4.7.2 Додаткове відео про Grafana

<a href="https://www.youtube.com/watch?v=qGFAX5ra1G8&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/qGFAX5ra1G8">
</a>

* Змінні в Grafana
* Експорт та імпорт дашбордів

Посилання:

* [SQL запити для Grafana](grafana.md)
* [дашборд Grafana](dashboard.json)

## Домашнє завдання

Дивіться [тут](../cohorts/2024/04-monitoring/homework.md)


## Додаткові ресурси

### Огляд модуля

![image](https://github.com/user-attachments/assets/0c5e932b-4fca-4d51-8b1c-93f4600861dc)

https://www.loom.com/share/1dd375ec4b0d458fabdfc2b841089031

# Нотатки

* [Нотатки від slavaheroes](https://github.com/slavaheroes/llm-zoomcamp/blob/homeworks/04-monitoring/notes.md)
* Ви робили нотатки? Додайте їх вище цієї лінії (Надішліть PR з *посиланнями* на ваші нотатки)

# Module 4: Evaluation and Monitoring

In this module, we will learn how to evaluate and monitor our LLM and RAG system.

In the evaluation part, we assess the quality of our entire RAG
system before it goes live.

In the monitoring part, we collect, store and visualize
metrics to assess the answer quality of a deployed LLM. We also
collect chat history and user feedback.

## Homework

See Homework [here](homework/homework.md)

See Homework [Notebook](homework/homework.ipynb)

## 4.1 Introduction to monitoring answer quality 
* Why monitoring LLM systems?
* Monitoring answer quality of LLMs 
* Monitoring answer quality with user feedback
* What else to monitor, that is not covered by this module? 


## 4.2 Offline vs Online (RAG) evaluation
* Modules recap
* Online vs offline evaluation
* Offline evaluation metrics 


## 4.3 Generating data for offline RAG evaluation
Links:

* [notebook](offline-rag-evaluation.ipynb)
* [results-gpt4o.csv](data/results-gpt4o.csv) (answers from GPT-4o)
* [results-gpt35.csv](data/results-gpt35.csv) (answers from GPT-3.5-Turbo)


## 4.4 Offline RAG evaluation: cosine similarity
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
* LLM as a judge
* A->Q->A' evaluation
* Q->A evaluation


Links:

* [notebook](offline-rag-evaluation.ipynb)
* [evaluations-aqa.csv](data/evaluations-aqa.csv) (A->Q->A evaluation results)
* [evaluations-qa.csv](data/evaluations-qa.csv) (Q->A evaluation results)

## 4.6 Capturing user feedback
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
* adding vector search
* adding OpenAI

Links:

* [final code](app/)
* [intermediate code from claude](code.md#462-capturing-user-feedback-part-2)


## 4.7 Monitoring the system
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
* Grafana variables
* Exporting and importing dashboards

Links:

* [SQL queries for Grafana](grafana.md)
* [Grafana dashboard](dashboard.json)


# Notes

* [Notes by slavaheroes](https://github.com/slavaheroes/llm-zoomcamp/blob/homeworks/04-monitoring/notes.md)
