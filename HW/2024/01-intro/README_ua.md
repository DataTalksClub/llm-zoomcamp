# Семінар LLM RAG

Спілкування з вашими власними даними - семінар LLM+RAG

Вам потрібно: 

- Docker
- Python 3.10
- Обліковий запис OpenAI
- За бажанням, обліковий запис GitHub


# LLM і RAG

Я згенерував це за допомогою ChatGPT:

## Великі мовні моделі (LLMs)
- **Призначення:** Генерувати та розуміти текст у манері, схожій на людську.
- **Структура:** Побудовані з використанням методів глибинного навчання, особливо архітектур Transformer.
- **Розмір:** Характеризуються великою кількістю параметрів (мільярди до трильйонів), що дозволяє їм тонко розуміти та генерувати текст.
- **Навчання:** Попередньо навчені на великих наборах текстових даних для здобуття широкого розуміння мови, а потім точно налаштовані для конкретних завдань.
- **Застосування:** Використовуються в чат-ботах, сервісах перекладу, створенні контенту та інших галузях.

## Генерація з додаванням інформації (RAG)
- **Призначення:** Підвищення якості відповідей мовної моделі за допомогою інформації, отриманої з зовнішніх джерел.
- **Як це працює:** Поєднує мовну модель з системою пошуку, зазвичай базою даних документів або пошуковою системою.
- **Процес:** 
  - Здійснює запит до зовнішнього джерела знань на основі введеного запиту.
  - Інтегрує отриману інформацію у процес генерації для надання контекстуально насичених і точних відповідей.
- **Переваги:** Покращує фактичну точність і релевантність згенерованого тексту.
- **Використання:** Перевірка фактів, завдання, що вимагають великих знань, як-от допомога в медичній діагностиці, і створення детального контенту, де точність має вирішальне значення.

Використовуйте ChatGPT, щоб показати різницю між генерацією і RAG.


Що ми будемо робити: 

* Індексація документів FAQ для Zoomcamp
    * DE Zoomcamp: https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit
    * ML Zoomcamp: https://docs.google.com/document/d/1LpPanc33QJJ6BSsyxVg-pWNMplal84TdZtq10naIhD8/edit
    * MLOps Zoomcamp: https://docs.google.com/document/d/12TlBfhIiKtyBv8RnsoJR6F72bkPDGEvPOItJIxaEzE0/edit
* Створення системи Q&A для відповіді на питання про ці документи 


# Підготовка середовища

Ми будемо використовувати codespaces, але це працюватиме будь-де

* Створіть репозиторій, наприклад, "llm-zoomcamp-rag-workshop"
* Запустіть codespace там

Ми будемо використовувати pipenv для керування залежностями. Встановімо його: 

```bash
pip install pipenv
```

Встановіть пакети

```bash
pipenv install tqdm notebook==7.1.2 openai elasticsearch
```

Якщо ви використовуєте OpenAI, додайте ключ до змінної середовища:

```bash
export OPENAI_API_KEY="TOKEN"
```

Отримання ключа

* Зареєструйтесь на https://platform.openai.com/ якщо у вас немає облікового запису
* Перейдіть на https://platform.openai.com/api-keys
* Створіть новий ключ і скопіюйте його


Для керування ключами можна використовувати direnv:

```bash
sudo apt update
sudo apt install direnv 
direnv hook bash >> ~/.bashrc
```

Створіть / відредагуйте `.envrc` у каталозі вашого проєкту:

```bash
export OPENAI_API_KEY='sk-proj-key'
```

Дозвольте direnv працювати:

```bash
direnv allow
```

Запустіть новий термінал і там запустіть jupyter:

```bash
pipenv run jupyter notebook
```

В іншому терміналі запустіть elasticsearch за допомогою docker:

```bash
docker run -it \
    --name elasticsearch \
    -p 9200:9200 \
    -p 9300:9300 \
    -e "discovery.type=single-node" \
    -e "xpack.security.enabled=false" \
    docker.elastic.co/elasticsearch/elasticsearch:8.4.3
```

Перевірте, що ES працює

```bash
curl http://localhost:9200
```

Ви повинні отримати щось таке:

```json
{
  "name" : "63d0133fc451",
  "cluster_name" : "docker-cluster",
  "cluster_uuid" : "AKW1gxdRTuSH8eLuxbqH6A",
  "version" : {
    "number" : "8.4.3",
    "build_flavor" : "default",
    "build_type" : "docker",
    "build_hash" : "42f05b9372a9a4a470db3b52817899b99a76ee73",
    "build_date" : "2022-10-04T07:17:24.662462378Z",
    "build_snapshot" : false,
    "lucene_version" : "9.3.0",
    "minimum_wire_compatibility_version" : "7.17.0",
    "minimum_index_compatibility_version" : "7.0.0"
  },
  "tagline" : "You Know, for Search"
}
```

# Пошук

RAG складається з кількох компонентів, і перший - це R - "пошук". Для пошуку нам потрібна пошукова система. У нашому прикладі ми будемо використовувати elasticsearch для пошуку.

## Пошук у документах

Створіть ноутбук "elastic-rag" або щось подібне. Ми будемо використовувати його для наших експериментів

Спочатку нам потрібно завантажити документи:

```bash
wget https://github.com/alexeygrigorev/llm-rag-workshop/raw/main/notebooks/documents.json
```

Завантажимо документи

```python
import json

with open('./documents.json', 'rt') as f_in:
    documents_file = json.load(f_in)

documents = []

for course in documents_file:
    course_name = course['course']

    for doc in course['documents']:
        doc['course'] = course_name
        documents.append(doc)
```

Тепер ми проіндексуємо ці документи за допомогою elasticsearch

Спочатку ініціалізуйте підключення і перевірте, що воно працює:

```python
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")
es.info()
```

Ви повинні побачити ту саму відповідь, що і раніше з `curl`.

Перш ніж ми зможемо проіндексувати документи, нам потрібно створити індекс (індекс в elasticsearch схожий на таблицю в "звичайних" базах даних):

```python
index_settings = {
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

index_name = "course-questions"
response = es.indices.create(index=index_name, body=index_settings)

response
```

Тепер ми готові проіндексувати всі документи:

```python
from tqdm.auto import tqdm

for doc in tqdm(documents):
    es.index(index=index_name, document=doc)
```

## Отримання документів

```python
user_question = "How do I join the course after it has started?"

search_query = {
    "size": 5,
    "query": {
        "bool": {
            "must": {
                "multi_match": {
                    "query": user_question,
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

Цей запит:

* Отримує топ

-5 відповідних документів.
* Шукає в полях "question", "text", "section", надаючи пріоритет "question".
* Підходить під запит користувача "How do I join the course after it has started?".
* Показує результати тільки для курсу "data-engineering-zoomcamp".

Давайте подивимось на результат:

```python
response = es.search(index=index_name, body=search_query)

for hit in response['hits']['hits']:
    doc = hit['_source']
    print(f"Section: {doc['section']}\nQuestion: {doc['question']}\nAnswer: {doc['text']}\n\n")
```

## Очищення

Ми можемо зробити це чистішим, помістивши це у функцію:

```python
def retrieve_documents(query, index_name="course-questions", max_results=5):
    es = Elasticsearch("http://localhost:9200")
    
    search_query = {
        "size": max_results,
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
    
    response = es.search(index=index_name, body=search_query)
    documents = [hit['_source'] for hit in response['hits']['hits']]
    return documents
```

І вивести відповіді:

```python
user_question = "How do I join the course after it has started?"

response = retrieve_documents(user_question)

for doc in response:
    print(f"Section: {doc['section']}\nQuestion: {doc['question']}\nAnswer: {doc['text']}\n\n")
```

# Генерація - Відповідь на питання

Тепер давайте зробимо частину "G" - генерація на основі результатів "R"

## OpenAI

Сьогодні ми будемо використовувати OpenAI (це найпростіше для початку). У курсі ми навчимося використовувати моделі з відкритим кодом 

Переконайтеся, що SDK встановлено та ключ налаштовано.

Ось як ми спілкуємося з ChatGPT3.5:

```python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "What's the formula for Energy?"}]
)
print(response.choices[0].message.content)
```

## Створення підказки

Тепер створимо підказку. Спочатку зберемо всі 
документи в один рядок:

```python
context_docs = retrieve_documents(user_question)

context = ""

for doc in context_docs:
    doc_str = f"Section: {doc['section']}\nQuestion: {doc['question']}\nAnswer: {doc['text']}\n\n"
    context += doc_str

context = context.strip()
print(context)
```

Тепер створимо власне підказку:

```python
prompt = f"""
Ви асистент викладача курсу. Відповідайте на питання користувача, базуючись на КОНТЕКСТІ - документах, отриманих з нашої бази FAQ. 
Використовуйте лише факти з КОНТЕКСТУ. Якщо КОНТЕКСТ не містить відповіді, поверніть "NONE"

ПИТАННЯ: {user_question}

КОНТЕКСТ:

{context}
""".strip()
```

Тепер ми можемо передати це до API OpenAI:

```python
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)
answer = response.choices[0].message.content
answer
```

Примітка: існують системні та користувацькі підказки, ми також можемо експериментувати з ними, щоб зробити дизайн підказки чистішим.

## Очищення

Тепер давайте зберемо все разом у одну функцію:

```python
def build_context(documents):
    context = ""

    for doc in documents:
        doc_str = f"Section: {doc['section']}\nQuestion: {doc['question']}\nAnswer: {doc['text']}\n\n"
        context += doc_str
    
    context = context.strip()
    return context


def build_prompt(user_question, documents):
    context = build_context(documents)
    return f"""
Ви асистент викладача курсу.
Відповідайте на питання користувача, базуючись на КОНТЕКСТІ - документах, отриманих з нашої бази FAQ.
Не використовуйте іншу інформацію поза наданим КОНТЕКСТОМ.

ПИТАННЯ: {user_question}

КОНТЕКСТ:

{context}
""".strip()

def ask_openai(prompt, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    answer = response.choices[0].message.content
    return answer

def qa_bot(user_question):
    context_docs = retrieve_documents(user_question)
    prompt = build_prompt(user_question, context_docs)
    answer = ask_openai(prompt)
    return answer
```

Тепер ми можемо запитати це:

```python
qa_bot("I'm getting invalid reference format: repository name must be lowercase")

qa_bot("I can't connect to postgres port 5432, my password doesn't work")

qa_bot("how can I run kafka?")
```

# Що далі

* Використовуйте моделі з відкритим кодом
* Створіть інтерфейс, наприклад, streamlit
* Розгорніть його