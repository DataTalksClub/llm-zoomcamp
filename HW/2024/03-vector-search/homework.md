## Домашнє завдання: Пошук за векторами

У цьому домашньому завданні ми експериментуватимемо з векторами з Elasticsearch та без нього.

> Ваші відповіді можуть не збігатися точно. Якщо це так, виберіть найближчу відповідь.

## Q1. Отримання моделі для embeddings

Спочатку ми отримаємо модель embeddings `multi-qa-distilbert-cos-v1` з
[бібліотеки Sentence Transformer](https://www.sbert.net/docs/sentence_transformer/pretrained_models.html#model-overview)

```python
from sentence_transformers import SentenceTransformer
embedding_model = SentenceTransformer(model_name)
```

Створіть embedding для цього питання користувача:

```python
user_question = "Я только что узнал об этом курсе. Могу ли я еще присоединиться к нему?"
```

Яке значення має перший елемент отриманого вектора?

- -0.24
- -0.04
- 0.07
- 0.27

Q1: 0.07822264

```python
from sentence_transformers import SentenceTransformer

# Отримання моделі векторизації
model_name = "multi-qa-distilbert-cos-v1"
embedding_model = SentenceTransformer(model_name)

# Створення вектору для запиту користувача
user_question = "I just discovered the course. Can I still join it?"
user_question_embedding = embedding_model.encode(user_question)

# Перший елемент отриманого вектора
first_value = user_question_embedding[0]
print(first_value)
```

## Підготовка документів

Тепер ми створимо embeddings для документів.

Завантажте документи з id, які ми підготували в модулі:

```python
import requests

base_url = 'https://github.com/DataTalksClub/llm-zoomcamp/blob/main'
relative_url = '03-vector-search/eval/documents-with-ids.json'
docs_url = f'{base_url}/{relative_url}?raw=1'
docs_response = requests.get(docs_url)
documents = docs_response.json()
```

Ми використовуватимемо лише підмножину питань - питання
для `"machine-learning-zoomcamp"`. Після фільтрації у вас має залишитися лише 375 документів.

## Q2. Створення embeddings

Тепер для кожного документа ми створимо embedding для полів question і answer.

Ми хочемо помістити всі їх у одну матрицю `X`:

- Створіть список `embeddings`
- Ітеруйтеся по кожному документу
- `qa_text = f'{question} {text}'`
- обчисліть embedding для `qa_text`, додайте до `embeddings`
- В кінці, нехай `X = np.array(embeddings)` (`import numpy as np`)

Яка форма матриці X? (`X.shape`). Включіть дужки.

Q2:  (375, 768)

```python
import requests
import numpy as np

# Завантаження документів
base_url = 'https://github.com/DataTalksClub/llm-zoomcamp/blob/main'
relative_url = '03-vector-search/eval/documents-with-ids.json'
docs_url = f'{base_url}/{relative_url}?raw=1'
docs_response = requests.get(docs_url)
documents = docs_response.json()

# Фільтрація документів для "machine-learning-zoomcamp"
filtered_documents = [doc for doc in documents if doc['course'] == 'machine-learning-zoomcamp']

# Створення векторів для питань і відповідей документів
embeddings = []
for doc in filtered_documents:
    question = doc['question']
    answer = doc['answer']
    qa_text = f'{question} {answer}'
    embedding = embedding_model.encode(qa_text)
    embeddings.append(embedding)

# Перетворення векторів на матрицю X
X = np.array(embeddings)
print(X.shape)
```

## Q3. Пошук

У нас є embeddings та вектор запиту. Тепер давайте обчислимо
косинусну схожість між вектором з Q1 (назвемо його `v`) та матрицею з Q2.

Вектори, що повертаються з моделі embeddings, вже
нормалізовані (можна перевірити це, обчисливши скалярний добуток вектора
із самим собою - має повернутися 1.0). Це означає, що для
обчислення косинусної схожості достатньо
помножити матрицю `X` на вектор `v`:

```python
scores = X.dot(v)
```

Який найвищий бал у результатах?

- 65.0
- 6.5
- 0.65
- 0.065

Q3: 0.6506574

```python
# Вектор запиту користувача з питання 1
v = user_question_embedding

# Обчислення косинусної подібності між вектором запиту та матрицею X
scores = X.dot(v)

# Найвищий результат у результатах
highest_score = scores.max()
print(highest_score)
```

## Пошук за векторами

Тепер ми можемо обчислити схожість між вектором запиту та всіма embeddings.

Давайте використаємо це для реалізації власного пошуку за векторами:

```python
class VectorSearchEngine():
    def __init__(self, documents, embeddings):
        self.documents = documents
        self.embeddings = embeddings

    def search(self, v_query, num_results=10):
        scores = self.embeddings.dot(v_query)
        idx = np.argsort(-scores)[:num_results]
        return [self.documents[i] for i in idx]

search_engine = VectorSearchEngine(documents=documents, embeddings=X)
search_engine.search(v, num_results=5)
```

Якщо ви не розумієте, як працює функція `search`:

- Запитайте у ChatGPT або будь-якої іншої LLM на ваш вибір, щоб пояснив код
- Перевірте наш передкурсовий воркшоп про реалізацію пошукового двигуна [тут](https://github.com/alexeygrigorev/build-your-own-search-engine)

(Примітка: ви можете замінити `argsort` на `argpartition`, щоб значно прискорити роботу)

## Q4. Hit-rate для нашого пошукового двигуна

Давайте оцінимо продуктивність нашого пошукового двигуна. Ми будемо використовувати метрику hitrate для оцінки.

Спочатку завантажте датасет з ground truth:

```python
import pandas as pd

base_url = 'https://github.com/DataTalksClub/llm-zoomcamp/blob/main'
relative_url = '03-vector-search/eval/ground-truth-data.csv'
ground_truth_url = f'{base_url}/{relative_url}?raw=1'

df_ground_truth = pd.read_csv(ground_truth_url)
df_ground_truth = df_ground_truth[df_ground_truth.course == 'machine-learning-zoomcamp']
ground_truth = df_ground_truth.to_dict(orient='records')
```

Тепер використовуйте код з модуля, щоб обчислити hitrate для
`VectorSearchEngine` з `num_results=5`.

Що ви отримали?

- 0.93
- 0.73
- 0.53
- 0.33

Q4: 0.9398907103825137

```python
import pandas as pd

# Завантаження набору даних із загальною кількістю влучень
base_url = 'https://github.com/DataTalksClub/llm-zoomcamp/blob/main'
relative_url = '03-vector-search/eval/ground-truth-data.csv'
ground_truth_url = f'{base_url}/{relative_url}?raw=1'

df_ground_truth = pd.read_csv(ground_truth_url)
df_ground_truth = df_ground_truth[df_ground_truth.course == 'machine-learning-zoomcamp']
ground_truth = df_ground_truth.to_dict(orient='records')

class VectorSearchEngine:
    def __init__(self, documents, embeddings):
        self.documents = documents
        self.embeddings = embeddings

    def search(self, v_query, num_results=10):
        scores = self.embeddings.dot(v_query)
        idx = np.argsort(-scores)[:num_results]
        return [self.documents[i] for i in idx]

# Ініціалізація пошукової системи з векторами документів
search_engine = VectorSearchEngine(documents=documents, embeddings=X)

# Функція для оцінки точності
def calculate_hitrate(search_engine, ground_truth, num_results=5):
    hits = 0
    for item in ground_truth:
        query = item['query']
        true_doc_id = item['document_id']
        query_embedding = embedding_model.encode(query)
        results = search_engine.search(query_embedding, num_results=num_results)
        result_ids = [doc['id'] for doc in results]
        if true_doc_id in result_ids:
            hits += 1
    return hits / len(ground_truth)

hitrate = calculate_hitrate(search_engine, ground_truth, num_results=5)
print(f'Hitrate: {hitrate}')
```

## Q5. Індексування за допомогою Elasticsearch

Тепер давайте індексувати ці документи за допомогою Elasticsearch

- Створіть індекс з такими ж налаштуваннями, як у модулі (але змініть розміри)
- Індексувати embeddings (примітка: ви вже їх обчислили)

Після індексування виконайте пошук того ж запиту з Q1.

Який ID документа з найвищим балом?

Q5: ee58a693

```python
from elasticsearch import Elasticsearch, helpers

# Підключення до Elasticsearch
es = Elasticsearch()

# Створення індексу з відповідними налаштуваннями
index_name = 'documents'
index_settings = {
    "mappings": {
        "properties": {
            "question_answer": {
                "type": "dense_vector",
                "dims": 768
            }
        }
    }
}

# Видалення індексу, якщо він існує
if es.indices.exists(index=index_name):
    es.indices.delete(index=index_name)

# Створення нового індексу
es.indices.create(index=index_name, body=index_settings)

# Індексація документів з обчисленими векторами
def generate_docs():
    for doc, embedding in zip(documents, X):
        yield {
            "_index": index_name,
            "_id": doc["id"],
            "_source": {
                "question_answer": embedding.tolist(),
                "text": doc["text"],
                "question": doc["question"]
            }
        }

helpers.bulk(es, generate_docs())

# Пошук за допомогою векторного запиту з питання 1
query_vector = user_question_embedding.tolist()
query = {
    "query": {
        "script_score": {
            "query": {"match_all": {}},
            "script": {
                "source": "cosineSimilarity(params.query_vector, 'question_answer') + 1.0",
                "params": {"query_vector": query_vector}
            }
        }
    }
}

# Виконання пошуку
response = es.search(index=index_name, body=query)

# Виведення ID документа з найвищим результатом
highest_score_doc_id = response['hits']['hits'][0]['_id']
print(f'ID документа з найвищим результатом: {highest_score_doc_id}')
```

## Q6. Hit-rate для Elasticsearch

Пошуковий двигун, який ми використовували в Q4, обчислював схожість між
запитом та ВСІМА векторами у нашій базі даних. Зазвичай це
не практично, оскільки ми можемо мати багато даних.

Elasticsearch використовує приблизні техніки для пришвидшення.

Давайте оцінимо, наскільки гірші результати, коли ми переходимо від
точного пошуку (як у Q4) до приблизного пошуку за допомогою Elasticsearch.

Який hitrate для нашого датасету для Elasticsearch?

- 0.93
- 0.73
- 0.53
- 0.33

Q6: 0.9398907103825137

```python
# Функція для оцінки точності в Elasticsearch
def calculate_hitrate_elasticsearch(ground_truth, num_results=5):
    hits = 0
    for item in ground_truth:
        query = item['query']
        true_doc_id = item['document_id']
        query_embedding = embedding_model.encode(query).tolist()
        query = {
            "query": {
                "script_score": {
                    "query": {"match_all": {}},
                    "script": {
                        "source": "cosineSimilarity(params.query_vector, 'question_answer') + 1.0",
                        "params": {"query_vector": query_embedding}
                    }
                }
            }
        }
        response = es.search(index=index_name, body=query)
        result_ids = [hit['_id'] for hit in response['hits']['hits'][:num_results]]
        if true_doc_id in result_ids:
            hits += 1
    return hits / len(ground_truth)

# Обчислення точності для Elasticsearch
hitrate_elastic = calculate_hitrate_elasticsearch(ground_truth, num_results=5)
print(f'Hitrate для Elasticsearch: {hitrate_elastic}')
```
Q6: 0.93
## Надішліть результати

- Надішліть свої результати тут: https://courses.datatalks.club/llm-zoomcamp-2024/homework/hw3
- Ваші відповіді можуть не збігатися точно. Якщо це так, виберіть найближчу відповідь.

```

```
