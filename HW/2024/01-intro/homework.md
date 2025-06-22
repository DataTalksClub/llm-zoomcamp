## Домашнє завдання: Вступ

У цьому домашньому завданні ми дізнаємось більше про пошук і використаємо Elastic Search для практики.

## Q1. Запуск Elastic

Запустіть Elastic Search 8.4.3 і отримайте інформацію про кластер. Якщо ви запускаєте його на localhost, ось як це зробити:

```bash
curl localhost:9200
```

Яке значення `version.build_hash`?

## Отримання даних

Тепер давайте отримаємо дані FAQ. Ви можете запустити цей фрагмент коду:

```python
import requests 

docs_url = 'https://github.com/DataTalksClub/llm-zoomcamp/blob/main/01-intro/documents.json?raw=1'
docs_response = requests.get(docs_url)
documents_raw = docs_response.json()

documents = []

for course in documents_raw:
    course_name = course['course']

    for doc in course['documents']:
        doc['course'] = course_name
        documents.append(doc)
```

Зверніть увагу, що вам потрібно мати бібліотеку `requests`:

```bash
pip install requests
```

## Q2. Індексація даних

Проіндексуйте дані так само, як було показано у відео курсу. Зробіть поле `course` ключовим словом, а решту - текстом.

Не забудьте встановити клієнт ElasticSearch для Python:

```bash
pip install elasticsearch
```

Яку функцію ви використовуєте для додавання даних до Elastic?

* `insert`
* `index`
* `put`
* `add`

## Q3. Пошук

Тепер давайте пошукаємо у нашому індексі.

Для запиту "How do I execute a command in a running docker container?", який бал у топового результату?

Використовуйте лише поля `question` та `text` і дайте полю `question` вагу 4

* 94.05
* 84.05
* 74.05
* 64.05

Подивіться на поле `_score`.

## Q4. Фільтрація

Тепер давайте обмежимо питання до `machine-learning-zoomcamp`.

Поверніть 3 результати. Яке 3-тє питання, повернуте пошуковою системою?

* Як я можу відлагодити контейнер Docker?
* Як я можу скопіювати файли з іншої папки у робочу директорію контейнера Docker?
* Як працюють образи контейнерів Lambda?
* Як я можу анотувати графік?

## Q5. Створення підказки

Тепер ми готові створити підказку для відправлення до LLM. Давайте використаємо ці шаблони:


```python
context_template = """
Q: {question}
A: {text}
""".strip()

prompt_template = """

You're a course teaching assistant. Answer the QUESTION based on the CONTEXT from the FAQ database.
Use only the facts from the CONTEXT when answering the QUESTION.

QUESTION: {question}

CONTEXT:
{context}
""".strip()
```

Як я можу відлагодити контейнер Docker?


Як я можу скопіювати файли з іншої папки у робочу директорію контейнера Docker?


Як працюють образи контейнерів Lambda?


Як я можу анотувати графік?


Яка довжина результату? (використовуйте функцію `len`)

* 962
* 1462
* 1962
* 2462

## Q6. Токени

Коли ми використовуємо платформу OpenAI, з нас стягується плата за кількість токенів, які ми надсилаємо в нашому запиті та отримуємо у відповіді.

Пакет OpenAI для Python використовує `tiktoken` для токенізації:

```bash
pip install tiktoken
```

Давайте розрахуємо кількість токенів у нашому запиті:

```python
encoding = tiktoken.encoding_for_model("gpt-4o")
```

Використовуйте функцію `encode`. Скільки токенів має наша підказка?

* 122
* 222
* 322
* 422

Примітка: щоб декодувати токен назад у слово, ви можете використовувати функцію `decode_single_token_bytes`:

```python
encoding.decode_single_token_bytes(63842)
```

## Бонус: генерування відповіді (неградоване)

Відправимо підказку до OpenAI. Яка відповідь?

Примітка: ви можете замінити OpenAI на Ollama. Дивіться модуль 2.

## Бонус: розрахунок вартості (неградоване)

Припустимо, що в середньому за запит ми відправляємо 150 токенів і отримуємо 250 токенів.

Скільки буде коштувати виконання 1000 запитів?

Ви можете переглянути ціни [тут](https://openai.com/api/pricing/)

На 17 червня ціни для gpt4o:

* Вхід: $0.005 / 1K токенів
* Вихід: $0.015 / 1K токенів

Ви можете перерахувати розрахунки з отриманими значеннями в Q6 і Q7.

## Надіслати результати

* Надішліть свої результати сюди: https://courses.datatalks.club/llm-zoomcamp-2024/homework/hw1
* Можливо, ваші відповіді не будуть точно збігатися. Якщо це так, виберіть найближчу.