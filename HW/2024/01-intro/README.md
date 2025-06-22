# Модуль 1: Вступ

У цьому модулі ми дізнаємося, що таке LLM і RAG, а також реалізуємо простий RAG конвеєр для відповіді на запитання щодо FAQ документів з наших Zoomcamp курсів.

Що ми будемо робити:

* Індексація документів FAQ Zoomcamp:
  * DE Zoomcamp: https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit
  * ML Zoomcamp: https://docs.google.com/document/d/1LpPanc33QJJ6BSsyxVg-pWNMplal84TdZtq10naIhD8/edit
  * MLOps Zoomcamp: https://docs.google.com/document/d/12TlBfhIiKtyBv8RnsoJR6F72bkPDGEvPOItJIxaEzE0/edit
* Створення системи Q&A для відповіді на запитання щодо цих документів

## 1.1 Вступ до LLM і RAG

<a href="https://www.youtube.com/watch?v=Q75JgLEXMsM&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/Q75JgLEXMsM">
</a>

* LLM
* RAG
* Архітектура RAG
* Результат курсу

## 1.2 Підготовка середовища

<a href="https://www.youtube.com/watch?v=ozCpmkbJNJE&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/ozCpmkbJNJE">
</a>

* Встановлення бібліотек
* Альтернатива: встановлення Anaconda або Miniconda

```bash
pip install tqdm notebook==7.1.2 openai elasticsearch pandas scikit-learn
```

## 1.3 Пошук

<a href="https://www.youtube.com/watch?v=olvem333Bqo&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/olvem333Bqo">
</a>

* Ми будемо використовувати пошукову систему, яку створили в [майстерні зі створення власної пошукової системи](https://github.com/alexeygrigorev/build-your-own-search-engine): [minsearch](https://github.com/alexeygrigorev/minsearch)
* Індексація документів
* Виконання пошуку

## 1.4 Генерація з OpenAI

<a href="https://www.youtube.com/watch?v=qz316T3U49Q&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/qz316T3U49Q">
</a>

* Виклик OpenAI API
* Створення промпта
* Отримання відповіді

Якщо ви не хочете використовувати сервіс, ви можете запустити LLM локально. Дивіться [модуль 2](../02-open-source/) для деталей.

Зокрема, перевірте "2.7 Ollama - Запуск LLM на CPU" - він може працювати з OpenAI API, тому для того, щоб приклад з 1.4 працював локально, вам потрібно лише змінити кілька рядків коду.

## 1.4.2 Альтернативи OpenAI API

<a href="https://www.youtube.com/watch?v=HObjFso2UJE&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/HObjFso2UJE">
</a>

[Альтернативи OpenAI](open-ai-alternatives.md)

## 1.5 Очищений потік RAG

<a href="https://www.youtube.com/watch?v=vkTiVwwch6A&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/vkTiVwwch6A">
</a>

* Очищення коду, який ми написали досі
* Створення модульності

## 1.6 Пошук за допомогою ElasticSearch

<a href="https://www.youtube.com/watch?v=1lgbR5wMvsI&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/1lgbR5wMvsI">
</a>

* Запуск ElasticSearch за допомогою Docker
* Індексація документів
* Замінити MinSearch на ElasticSearch

Запуск ElasticSearch:

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

Налаштування індексації:

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

Запит:

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

# Нотатки

* Замість цього додайте посилання
* Ви робили нотатки? Додайте їх вище цієї лінії (надішліть PR з *посиланнями* на ваші нотатки)
