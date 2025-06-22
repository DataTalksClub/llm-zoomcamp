# Створення власного пошукового двигуна

Код для семінару "Створення власного пошукового двигуна"

Відео: https://www.youtube.com/watch?v=nMrGK5QgPVE

Що ми зробимо:

- Використання документів з FAQ Zoomcamp:
  - [DE Zoomcamp](https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit)
  - [ML Zoomcamp](https://docs.google.com/document/d/1LpPanc33QJJ6BSsyxVg-pWNMplal84TdZtq10naIhD8/edit)
  - [MLOps Zoomcamp](https://docs.google.com/document/d/12TlBfhIiKtyBv8RnsoJR6F72bkPDGEvPOItJIxaEzE0/edit)
- Створення пошукового двигуна для отримання цих документів
- Пізніше результати можна буде використовувати для [Q&A RAG системи](https://github.com/alexeygrigorev/llm-rag-workshop)
- [Референсна імплементація для текстового пошуку](https://github.com/alexeygrigorev/minsearch)

## План семінару

1. **Підготовка середовища**
2. **Основи текстового пошуку**
   - Основи інформаційного пошуку
   - Вступ до векторних просторів, bag of words та TF-IDF
3. **Реалізація базового текстового пошуку**
   - TF-IDF скоринг з sklearn
   - Фільтрація за ключовими словами за допомогою pandas
   - Створення класу для пошуку за релевантністю
4. **Ембедінги та векторний пошук**
   - Векторні ембедінги
   - Word2Vec та інші підходи для word embeddings
   - LSA (Latent Semantic Analysis) для ембедінгів документів
   - Реалізація векторного пошуку за допомогою LSA
   - BERT ембедінги
5. **Комбінування текстового та векторного пошуку** (5 хвилин)
6. **Практичні аспекти імплементації та інструменти** (10 хвилин)
   - Інструменти для реальної імплементації:
     - інвертовані індекси для текстового пошуку
     - LSH для векторного пошуку (використовуючи випадкові проєкції)
   - Технології:
     - Lucene/Elasticsearch для текстового пошуку
     - FAISS та інші векторні бази даних

## 1. Підготовка середовища

На семінарі ми будемо використовувати Github Codespaces, але ви можете використовувати будь-яке середовище.

Необхідно встановити наступні бібліотеки:

```bash
pip install requests pandas scikit-learn jupyter
```

Запуск jupyter:

```bash
jupyter notebook
```

Завантаження даних:

```python
import requests

docs_url = 'https://github.com/alexeygrigorev/llm-rag-workshop/raw/main/notebooks/documents.json'
docs_response = requests.get(docs_url)
documents_raw = docs_response.json()

documents = []

for course in documents_raw:
    course_name = course['course']

    for doc in course['documents']:
        doc['course'] = course_name
        documents.append(doc)
```

Створення DataFrame:

```python
import pandas as pd

df = pd.DataFrame(documents, columns=['course', 'section', 'question', 'text'])
df.head()
```

## 2. Основи текстового пошуку

- **Інформаційний пошук** - Процес отримання релевантної інформації з великих наборів даних на основі запитів користувача.
- **Векторні простори** - Математичне представлення, де текст перетворюється у вектори (точки в просторі), що дозволяє кількісне порівняння.
- **Bag of Words** - Простий модель представлення тексту, яка розглядає кожен документ як набір слів, не враховуючи граматику та порядок слів, але зберігаючи їх частоту.
- **TF-IDF (Term Frequency-Inverse Document Frequency)** - Статистична міра, що використовується для оцінки важливості слова у документі в колекції або корпусі. Вона збільшується з кількістю разів, коли слово з'являється у документі, але зменшується з частотою слова в корпусі.

## 3. Реалізація базового текстового пошуку

Реалізуємо його самостійно.

### Фільтрація за ключовими словами

Спочатку фільтрація за ключовими словами:

```python
df[df.course == 'data-engineering-zoomcamp'].head()
```

### Векторизація

Для Count Vectorizer та TF-IDF спочатку використаємо простий приклад

```python
documents = [
    "Course starts on 15th Jan 2024",
    "Prerequisites listed on GitHub",
    "Submit homeworks after start date",
    "Registration not required for participation",
    "Setup Google Cloud and Python before course"
]
```

Спочатку використаємо Count Vectorizer:

```python
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(stop_words='english')
X = cv.fit_transform(documents)

names = cv.get_feature_names_out()

df_docs = pd.DataFrame(X.toarray(), columns=names).T
df_docs
```

Це представлення називається "bag of words" - тут ми ігноруємо порядок слів, зосереджуючись лише на самих словах. У багатьох випадках цього достатньо і результати вже є досить хорошими.

Тепер замінимо його на `TfidfVectorizer`:

```python
from sklearn.feature_extraction.text import TfidfVectorizer

cv = TfidfVectorizer(stop_words='english')
X = cv.fit_transform(documents)

names = cv.get_feature_names_out()

df_docs = pd.DataFrame(X.toarray(), columns=names).T
df_docs.round(2)
```

### Схожість запиту та документу

Ми представляємо запит у тому ж векторному просторі - тобто використовуючи той же векторизатор:

```python
query = "Do I need to know python to sign up for the January course?"

q = cv.transform([query])
q.toarray()
```

Ми можемо бачити слова запиту та слова деякого документа:

```python
query_dict = dict(zip(names, q.toarray()[0]))
query_dict

doc_dict = dict(zip(names, X.toarray()[1]))
doc_dict
```

Чим більше спільних слів - тим кращий результат пошуку. Давайте порахуємо це:

```python
df_qd = pd.DataFrame([query_dict, doc_dict], index=['query', 'doc']).T

(df_qd['query'] * df_qd['doc']).sum()
```

Це є скалярний добуток. Тому ми можемо використати матричне множення для обчислення результату:

```python
X.dot(q.T).toarray()
```

Перегляньте [це оновлення з лінійної алгебри](https://github.com/DataTalksClub/machine-learning-zoomcamp/blob/master/01-intro/08-linear-algebra.md), якщо вам потрібно освіжити знання з матричного множення (не хвилюйтеся - це розробникозручне)

Висновок: це дуже швидкий та ефективний метод обчислення схожості.

На практиці ми зазвичай використовуємо косинусну схожість:

```python
cosine_similarity(X, q)
```

TF-IDF векторизатор вже видає нормалізовані вектори, тому результати ідентичні. Ми не будемо вдаватися в деталі, як це працює, але ви можете ознайомитися з "Introduction to Information Retrieval", якщо хочете дізнатися більше.

### Векторизація всіх документів

Тепер зробимо це для всіх документів:

```python
fields = ['section', 'question', 'text']
transformers = {}
matrices = {}

for field in fields:
    cv = TfidfVectorizer(stop_words='english', min_df=3)
    X = cv.fit_transform(df[field])

    transformers[field] = cv
    matrices[field] = X

transformers['text'].get_feature_names_out()
matrices['text']
```

### Пошук

Тепер зробимо пошук за полем text:

```python
query = "I just signed up. Is it too late to join the course?"

q = transformers['text'].transform([query])
score = cosine_similarity(matrices['text'], q).flatten()
```

Подивіться на результати пошуку:

```python
df['score'] = score
df.sort_values(by='score', ascending=False).head(5)
```

### Зробимо це як клас

```python
class SearchEngine:
    def __init__(self, fields):
        self.fields = fields
        self.transformers = {}
        self.matrices = {}

    def fit(self, df):
        for field in self.fields:
            cv = TfidfVectorizer(stop_words='english', min_df=3)
            X = cv.fit_transform(df[field])

            self.transformers[field] = cv
            self.matrices[field] = X

    def search(self, df, query, field='text'):
        q = self.transformers[field].transform([query])
        score = cosine_similarity(self.matrices[field], q).flatten()

        df['score'] = score
        return df.sort_values(by='score', ascending=False)


se = SearchEngine(fields)
se.fit(df)
```

```python
query = "I just signed up. Is it too late to join the course?"

results = se.search(df, query, field='text')
results.head(5)
```

### Завдання 1

Реалізуйте функціонал для пошуку за іншими полями:

```python
query = "Join the course"

results = se.search(df, query, field='question')
results.head(5)
```

```python
query = "Join the course"

results = se.search(df, query, field='section')
results.head(5)
```

## 4. Ембедінги та векторний пошук

Векторні ембедінги представляють текст у високорозмірному векторному просторі. Це дозволяє порівнювати документи, запити та слова на основі їхніх векторних представлень, що дозволяє більш складні та глибокі пошуки за змістом.

Ми можемо використовувати такі підходи як Word2Vec та LSA (Latent Semantic Analysis).

### Latent Semantic Analysis (LSA)

Ми будемо використовувати LSA для векторних ембедінгів документів.

Спочатку тренуємо LSA:

```python
from sklearn.decomposition import TruncatedSVD

lsa = TruncatedSVD(n_components=100)
lsa.fit(matrices['text'])
```

Після тренування ми можемо отримати LSA-ембедінги для документів:

```python
lsa_matrices = {}

for field in fields:
    X = matrices[field]
    lsa_matrices[field] = lsa.transform(X)
```

### Реалізація векторного пошуку за допомогою LSA

Тепер ми можемо використовувати LSA-ембедінги для пошуку.

Спочатку отримуємо LSA-ембедінги для запиту:

```python
q = transformers['text'].transform([query])
q_lsa = lsa.transform(q)
```

Тепер можемо використовувати ці ембедінги для пошуку:

```python
score = cosine_similarity(lsa_matrices['text'], q_lsa).flatten()
```

Переглядаємо результати:

```python
df['score'] = score
df.sort_values(by='score', ascending=False).head(5)
```

### BERT ембедінги

Ми також можемо використовувати BERT для ембедінгів. Для цього нам потрібно буде використовувати бібліотеку transformers.

```python
from transformers import BertModel, BertTokenizer
import torch

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

def embed_text(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, max_length=512)
    outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).detach().numpy()
```

Тепер можемо отримати ембедінги для документів та запиту:

```python
embeddings = np.array([embed_text(text) for text in df['text']])
query_embedding = embed_text(query)
```

І можемо використовувати ці ембедінги для пошуку:

```python
score = cosine_similarity(embeddings, query_embedding).flatten()
```

## 5. Комбінування текстового та векторного пошуку

Ми можемо комбінувати результати текстового та векторного пошуку, щоб отримати більш точні результати.

```python
text_score = cosine_similarity(matrices['text'], q).flatten()
vector_score = cosine_similarity(lsa_matrices['text'], q_lsa).flatten()

combined_score = 0.5 * text_score + 0.5 * vector_score

df['score'] = combined_score
df.sort_values(by='score', ascending=False).head(5)
```

## 6. Практичні аспекти імплементації та інструменти

Для реальної імплементації ми можемо використовувати такі інструменти як Lucene/Elasticsearch для текстового пошуку та FAISS для векторного пошуку.

```python
pip install elasticsearch
pip install faiss-cpu
```

Ці інструменти дозволяють швидко та ефективно імплементувати пошукові системи, які можуть обробляти великі обсяги даних та забезпечувати високу точність пошуку.
