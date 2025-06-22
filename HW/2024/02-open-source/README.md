# 2. Відкриті LLM

У попередньому модулі ми використовували OpenAI через API OpenAI. Це дуже зручний спосіб використовувати LLM, але за використання доводиться платити, і ви не маєте контролю над моделлю, яку використовуєте.

У цьому модулі ми розглянемо використання відкритих LLM.

## 2.1 Відкриті LLM - Вступ

<a href="https://www.youtube.com/watch?v=ATchkIRsH4g&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/ATchkIRsH4g">
</a>

* Відкриті LLM
* Заміна LLM у потоці RAG

## 2.2 Використання GPU в Saturn Cloud

<a href="https://www.youtube.com/watch?v=E0cAqBWfJYY&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/E0cAqBWfJYY">
</a>

* Реєстрація в Saturn Cloud
* Налаштування секретів і git
* Створення інстансу з GPU

```bash
pip install -U transformers accelerate bitsandbytes sentencepiece
```

Посилання:

* https://saturncloud.io/
* https://github.com/DataTalksClub/llm-zoomcamp-saturncloud

Google Colab як альтернатива:

* [Відео](https://www.loom.com/share/591f39e4e231486bbfc3fbd316ec03c5)
* [Ноутбук](https://colab.research.google.com/drive/1XmxUZutZXoAEdQZU45EXWPseBX9s2NRd)

## 2.3 FLAN-T5

<a href="https://www.youtube.com/watch?v=a86iTyxnFE4&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/a86iTyxnFE4">
</a>

* Модель: `google/flan-t5-xl`
* Ноутбук: [huggingface-flan-t5.ipynb](huggingface-flan-t5.ipynb)

```bash
import os
os.environ['HF_HOME'] = '/run/cache/'
```

Посилання:

* https://huggingface.co/google/flan-t5-xl
* https://huggingface.co/docs/transformers/en/model_doc/flan-t5

Пояснення параметрів:

* `max_length`: Встановіть це значення вище, якщо ви хочете довші відповіді. Наприклад, `max_length=300`.
* `num_beams`: Збільшення цього значення може призвести до більш ретельного дослідження можливих послідовностей. Типові значення знаходяться в межах від 5 до 10.
* `do_sample`: Встановіть це значення на `True`, щоб використовувати методи вибірки. Це може призвести до більш різноманітних відповідей.
* `temperature`: Зниження цього значення робить модель більш впевненою та детермінованою, а підвищення - збільшує різноманітність. Типові значення знаходяться в межах від 0.7 до 1.5.
* `top_k` і `top_p`: Ці параметри контролюють вибірку nucleus. `top_k` обмежує вибірковий пул до топ `k` токенів, тоді як `top_p` використовує накопичувальну ймовірність для відсіювання вибіркового пулу. Налаштуйте їх на основі бажаного рівня випадковості.

## 2.4 Phi 3 Mini

<a href="https://www.youtube.com/watch?v=8KH6AS2PqWk&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/8KH6AS2PqWk">
</a>

* Модель: `microsoft/Phi-3-mini-128k-instruct`
* Ноутбук: [huggingface-phi3.ipynb](huggingface-phi3.ipynb)

Посилання:

* https://huggingface.co/microsoft/Phi-3-mini-128k-instruct

## 2.5 Mistral-7B та аутентифікація на HuggingFace Hub

<a href="https://www.youtube.com/watch?v=TdVEOzSoUCs&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/TdVEOzSoUCs">
</a>

* Модель: `mistralai/Mistral-7B-v0.1`
* Ноутбук: [huggingface-mistral-7b.ipynb](huggingface-mistral-7b.ipynb)

[Інструкції для ChatGPT щодо запуску](serving-hugging-face-models.md)

Посилання:

* https://huggingface.co/docs/transformers/en/llm_tutorial
* https://huggingface.co/settings/tokens
* https://huggingface.co/mistralai/Mistral-7B-v0.1

## 2.6 Інші моделі

<a href="https://www.youtube.com/watch?v=GzPV_HTmCkc&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/GzPV_HTmCkc">
</a>

* [`LLM360/Amber`](https://huggingface.co/LLM360/Amber)
* [Gemma-7B](https://huggingface.co/blog/gemma)
* [SaulLM-7B](https://huggingface.co/papers/2403.03883)
* [Granite-7B](https://huggingface.co/ibm-granite/granite-7b-base)
* [MPT-7B](https://huggingface.co/mosaicml/mpt-7b)
* [OpenLLaMA-7B](https://huggingface.co/openlm-research/open_llama_7b)

Де їх знайти:

* Лідерборди
* Google
* ChatGPT

Посилання:

* https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard
* https://huggingface.co/spaces/optimum/llm-perf-leaderboard

## 2.7 Ollama - запуск LLM на CPU

<a href="https://www.youtube.com/watch?v=PVpBGs_iSjY&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/PVpBGs_iSjY">
</a>

* Найпростіший спосіб запустити LLM без GPU - використовувати [Ollama](https://github.com/ollama/ollama)
* Ноутбук: [ollama.ipynb](ollama.ipynb)

Для Linux:

```bash
curl -fsSL https://ollama.com/install.sh | sh

ollama start
ollama pull phi3
ollama run phi3
```

[Приклад промпту](prompt.md)

Підключення до нього за допомогою API OpenAI:

```python
from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',
)
```

Docker

```bash
docker run -it \
    -v ollama:/root/.ollama \
    -p 11434:11434 \
    --name ollama \
    ollama/ollama
```

Витягування моделі

```bash
docker exec -it ollama bash
ollama pull phi3
```

## 2.8 Ollama & Phi3 + Elastic в Docker-Compose

<a href="https://www.youtube.com/watch?v=4juoo_jk96U&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/4juoo_jk96U">
</a>

* Створення файлу Docker-Compose
* Повторний запуск ноутбука модуля 1

* Ноутбук: [rag-intro.ipynb](rag-intro.ipynb)

## 2.9 UI для RAG

<a href="https://www.youtube.com/watch?v=R6L8PZ

<a href="https://www.youtube.com/watch?v=R6L8PZ-7bGo&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/R6L8PZ-7bGo">
</a>

* Використання Streamlit
* [Code](qa_faq.py)

If you want to learn more about streamlit, you can
use [this material](https://github.com/DataTalksClub/project-of-the-week/blob/main/2022-08-14-frontend.md)
from [our repository with projects of the week](https://github.com/DataTalksClub/project-of-the-week/tree/main).

## Homework

See [here](../cohorts/2024/02-open-source/homework.md)

# Примітки

* [Обхідний шлях від Pham Nguyen Hung для використання контейнера ElasticSearch з Saturn Cloud і Google Colab замість minsearch](https://hung.bearblog.dev/llm-zoomcamp-zrok/)
* [Примітки від slavaheroes](https://github.com/slavaheroes/llm-zoomcamp/blob/homeworks/02-open-source/notes.md)
* [Примітки від Pham Nguyen Hung](https://hung.bearblog.dev/llm-zoomcamp-2-os/)
* [Примітки від Marat про відкриті та закриті моделі і способи їх запуску](https://machine-mind-ml.medium.com/open-sourced-vs-closed-sourced-llms-2392c7db6e10)
* Ви зробили примітки? Додайте їх вище цієї лінії (надішліть PR з *посиланнями* на ваші примітки)
