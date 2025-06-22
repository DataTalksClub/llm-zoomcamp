# Підготовка даних у RAG

## Початок роботи

1. Клонуйте [репозиторій](https://github.com/mage-ai/rag-project):
```bash
git clone https://github.com/mage-ai/rag-project
cd rag-project
```
2. Перейдіть до директорії `rag-project/llm`, додайте `spacy` до файлу `requirements.txt`.
3. Потім оновіть файл `Dockerfile`, який знаходиться в директорії `rag-project`, додавши наступне:
```YAML
RUN python -m spacy download en_core_web_sm
```
4. Запустіть:
```bash
./scripts/start.sh
```

Після запуску перейдіть до [http://localhost:6789/](http://localhost:6789/).

Для отримання додаткової інформації про налаштування, ознайомтеся з [інструкціями](https://docs.mage.ai/getting-started/setup#docker-compose-template).


## 0. Огляд модуля

<a href="https://www.youtube.com/watch?v=gP2ZOsG9Umg&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/gP2ZOsG9Umg">
</a>

## 1. Інтеграція

У цьому розділі ми розглянемо інтеграцію документів з одного джерела даних.

<a href="https://www.youtube.com/watch?v=9BJppvgLINc&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/9BJppvgLINc">
</a>

* [Код](https://github.com/mage-ai/rag-project/blob/master/llm/rager/data_loaders/runic_oblivion.py)
* [Посилання на документ для API Data Loader](https://raw.githubusercontent.com/DataTalksClub/llm-zoomcamp/main/01-intro/documents.json)

## 2. Розбиття на частини

Після того, як дані інтегровані, ми ділимо їх на керовані частини.

Дані Q&A вже поділені на частини – тексти невеликі, і їх легко обробляти та індексувати. Але інші набори даних можуть бути не такими (тексти книг, транскрипти тощо).

У цьому відео ми обговоримо перетворення великих текстів на менші документи – тобто розбиття на частини.

<a href="https://www.youtube.com/watch?v=H2oq5GSCKhM&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/H2oq5GSCKhM">
</a>

[Код](https://github.com/mage-ai/rag-project/blob/master/llm/rager/transformers/radiant_photon.py)

## 3. Токенізація

Токенізація є важливим кроком в обробці тексту та підготовці даних для ефективного пошуку.

<a href="https://www.youtube.com/watch?v=hrMrqRgZryg&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/hrMrqRgZryg">
</a>

[Код](https://github.com/mage-ai/rag-project/blob/master/llm/rager/transformers/vivid_nexus.py)

## 4. Вбудовування

Вбудовування даних перекладає текст у числові вектори, які можна обробляти моделями.

Раніше для цього ми використовували трансформери речень. У цьому відео ми покажемо іншу стратегію.

<a href="https://www.youtube.com/watch?v=8wrArv0DEKc&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/8wrArv0DEKc">
</a>

[Код](https://github.com/mage-ai/rag-project/blob/master/llm/rager/transformers/prismatic_axiom.py)

## 5. Експорт

Після обробки дані потрібно експортувати для зберігання, щоб їх можна було отримати для кращого контекстуалізації запитів користувачів.

Тут ми збережемо вбудовування в Elasticsearch.

Будь ласка, переконайтеся, що використовуєте ім’я, яке ви дали своєму сервісу Elasticsearch у вашому файлі docker-compose, а також порт як рядок підключення, наприклад, нижче:

`<docker-compose-service-name><port>` http://elasticsearch:9200

<a href="https://www.youtube.com/watch?v=cHrphSoRBX4&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/cHrphSoRBX4">
</a>

[Код](https://github.com/mage-ai/rag-project/blob/master/llm/rager/data_exporters/numinous_fission.py)

## 6. Витягування: тестовий пошуковий запит

Після експортування частин і вбудованих векторів, ми можемо протестувати пошуковий запит, щоб отримати відповідні документи на приклад запитів.

<a href="https://www.youtube.com/watch?v=z5NqDcaBglY&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/z5NqDcaBglY">
</a>

[Код](code/06_retrieval.py)

## 7. Автоматизація щоденних запусків

Автоматизація є ключовим моментом для підтримки та оновлення вашої системи. У цьому розділі показано, як налаштувати та автоматично запускати щоденні запуски ваших даних, щоб забезпечити актуальність та узгодженість обробки даних.

<a href="https://www.youtube.com/watch?v=nuk7_soKMUA&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  <img src="https://markdown-videos-api.jorgenkh.no/youtube/nuk7_soKMUA">
</a>

## Домашнє завдання

У цьому домашньому завданні ми побудуємо наскрізний конвеєр висновків з додатковою генерацією пошуку (RAG) і дамо відповідь на кілька запитань про повернення.

### Q1: Запуск Mage

Спочатку запустимо Mage за допомогою наведеного нижче коду.
```Bash
git clone https://github.com/mage-ai/rag-project
cd rag-project
./scripts/start.sh
```
Яку версію Mage ми запускаємо?

Вам потрібно буде встановити/запустити наступне у вашому терміналі в Mage:
```Python
pip install spacy
pip install python-docx
pip install spacy-embedding
pip install sentence-transformers
python -m spacy download en_core_web_sm
```

### Q2: Ініціалізація оркестраційного конвеєра RAG

Створіть новий конвеєр RAG у Mage і імпортуйте документи FAQ, використовуючи методи, які ви вивчили в модулі 1.

*Підказка, використовуйте метод `fetch`, щоб імпортувати документи, включайте функцію `clean_lines` та функцію `parse_document` у завантажувач даних.*

Скільки документів FAQ було імпортовано?

1. [ ] 2
1. [ ] 3
1. [ ] 4
1. [ ] 5

### Q3: Поділ документів на фрагменти

Скопіюйте наведений нижче код у блок перетворювача (Transformer) фрагментації

```Python
import re
from typing import Any, Dict, List

@transformer
def chunk_documents(data: List[Dict[str, Any]], *args, **kwargs):
    documents = []

    for idx, item in enumerate(data):
        course = item['course']

        for info in item['documents']:
            section = info['section']
            question = info['question']
            answer = info['text']

            # Generate a unique document ID
            document_id = ':'.join([re.sub(r'\W', '_', part) 
	            for part in [course, section, question]]).lower()

            # Format the document string
            chunk = '\n'.join([
                f'course:\n{course}\n',
                f'section:\n{section}\n',
                f'question:\n{question}\n',
                f'answer:\n{answer}\n',
            ])

            documents.append(dict(
                chunk=chunk,
                document=info,
	            document_id=document_id,
            ))

    print(f'Documents:', len(documents))

    return [documents]
```

Скільки запитань було повернуто з цього блоку?

1. [ ] 900
1. [ ] 948
1. [ ] 1026
1. [ ] 1445

### Q4: Лематизація документів

Скопіюйте наведений нижче код у блок токенізації (лемматизації Spacy).

```Python
from typing import Dict, List

import spacy

@transformer
def lemmatize_text(documents: List[Dict], *args, **kwargs) -> List[Dict]:
    count = len(documents)
    print('Documents', count)

    nlp = spacy.load('en_core_web_sm')

    data = []

    for idx, document in enumerate(documents):
        document_id = document['document_id']
        if idx % 100 == 0:
            print(f'{idx + 1}/{count}')

        # Process the text chunk using spaCy
        chunk = document['chunk']
        doc = nlp(chunk)
        tokens = [token.lemma_ for token in doc]

        data.append(
            dict(
                chunk=chunk,
                document_id=document_id,
                tokens=tokens,
            )
        )

    print('\nData', len(data))

    return [data]
```

Виходячи з результатів функції `lemmatize_text`, яка основна мета списку `tokens`, що повертається, у кожному словнику?

**Варіанти:**

1. [ ] Щоб зберігати оригінальні фрагменти тексту без будь-яких змін.
1. [ ] Щоб зберігати ідентифікатори документів та їх відповідні метадані.
1. [ ] Щоб зберігати лематизовані форми кожного токена в текстовому фрагменті.
1. [ ] Щоб зберігати речення з оригінального текстового фрагмента.

### Q5: Вбудовування за допомогою перетворювачів речень

Скопіюйте наведений нижче код і запустіть його в налаштуванні перетворювача коду перетворювача

```Python
from typing import Any, Dict, List
import spacy
from sentence_transformers import SentenceTransformer
import numpy as np

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(documents: List[Dict], *args, **kwargs) -> Dict[str, Any]:

    # Load the SpaCy model once
    nlp = spacy.load('en_core_web_sm')

    # Load the Sentence Transformers model once
    model = SentenceTransformer('all-mpnet-base-v2')

    data = []
    count = len(documents)
    print('Documents', count)

    for idx, document in enumerate(documents):
        if idx % 100 == 0:
            print(f'{idx + 1}/{count}')

        tokens = document['tokens']

        # Lemmatize tokens using SpaCy
        lemmas = [token.lemma_ for token in nlp(' '.join(tokens))]

        # Combine lemmas back into a single string of text used for embedding
        text = ' '.join(lemmas)

        # Generate embeddings using Sentence Transformers
        embedding = model.encode(text).tolist()

        data.append(dict(
            chunk=document['chunk'],
            document_id=document['document_id'],
            embedding=embedding,
        ))

    # Compute and report the average embedding length
    embeddings = [doc['embedding'] for doc in data]
    avg_embedding_length = np.mean([len(emb) for emb in embeddings])
    print("Average embedding length:", avg_embedding_length)

    return {
        'documents': data,
        'avg_embedding_length': avg_embedding_length
    }
```

Яка середня довжина вбудовування?

1. [ ] 750
1. [ ] 768
1. [ ] 775
1. [ ] 810

### Q6: Завантаження вбудовувань у Elasticsearch

Скопіюйте наведений нижче код у блок бази даних Vector (Elasticsearch) і запустіть код.

```Python
from typing import Dict, List, Tuple, Union, Any
import json
import numpy as np
from elasticsearch import Elasticsearch

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_to_elasticsearch(data: Dict[str, Any], *args, **kwargs):
    """
    Export the processed data to an Elasticsearch index.
    Args:
        data (Dict[str, Any]): The data to be exported, which includes processed documents and average embedding length.
    """
    connection_string = kwargs.get('connection_string', 'http://localhost:9200')
    index_name = kwargs.get('index_name', 'documents')
    number_of_shards = kwargs.get('number_of_shards', 1)
    number_of_replicas = kwargs.get('number_of_replicas', 0)
    documents = data['documents']
    dimensions = kwargs.get('dimensions')

    if dimensions is None:
        for document in documents:
            if 'embedding' in document:
                dimensions = len(document['embedding'])
                break

    if dimensions is None:
        raise ValueError("No embeddings found in documents to determine dimensions")

    es_client = Elasticsearch(connection_string)

    print(f'Connecting to Elasticsearch at {connection_string}')

    index_settings = {
        "settings": {
            "number_of_shards": number_of_shards,
            "number_of_replicas": number_of_replicas,
        },
        "mappings": {
            "properties": {
                "chunk": {"type": "text"},
                "document_id": {"type": "text"},
                "embedding": {"type": "dense_vector", "dims": dimensions}
            }
        }
    }

    # Recreate the index by deleting if it exists and then creating with new settings
    if es_client.indices.exists(index=index_name):
        es_client.indices.delete(index=index_name)
        print(f'Index {index_name} deleted')

    es_client.indices.create(index=index_name, body=index_settings)
    print('Index created with properties:')
    print(json.dumps(index_settings, indent=2))
    print('Embedding dimensions:', dimensions)

    count = len(documents)
    print(f'Indexing {count} documents to Elasticsearch index {index_name}')
    for idx, document in enumerate(documents):
        if idx % 100 == 0:
            print(f'{idx + 1}/{count}')

        if isinstance(document['embedding'], np.ndarray):
            document['

embedding'] = document['embedding'].tolist()

        es_client.index(index=index_name, document=document)

    return [[d['embedding'] for d in documents[:10]]]
```

Який тип даних було використано для зберігання вбудовувань під час експорту конвеєра RAG (Retrieval-Augmented Generation) до Elasticsearch?

1. [ ] текст
1. [ ] ключове слово
1. [ ] dense_vector
1. [ ] float

### Q7: Ітеративний запит на пошук

Перейдіть до конвеєра висновків і виберіть блок ітеративного пошуку (спеціальний код). Скопіюйте наведений нижче код і запустіть блок.

```Python
from typing import Dict, List, Union

import numpy as np
from elasticsearch import Elasticsearch, exceptions

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def tokenize(text: str) -> List[str]:
    # Dummy tokenize function - replace with actual tokenization logic
    return text.split()

def embed(tokens: List[str]) -> np.ndarray:
    # Dummy embed function - replace with actual embedding logic
    return np.random.rand(768)  # Assuming 768 is the embedding dimension

@data_loader
def search(*args, **kwargs) -> List[Dict]:
    """
    query_embedding: Union[List[int], np.ndarray]
    """

    connection_string = kwargs.get('connection_string', 'http://host.docker.internal:9200')
    index_name = kwargs.get('index_name', 'documents')
    source = kwargs.get('source', "cosineSimilarity(params.query_vector, 'embedding') + 1.0")
    top_k = kwargs.get('top_k', 5)
    chunk_column = kwargs.get('chunk_column')#, 'content')

    user_query = "When is the next LLM Zoomcamp?"
    tokens = tokenize(user_query)
    query_embedding = embed(tokens)

    if isinstance(query_embedding, np.ndarray):
        query_embedding = query_embedding.tolist()

    script_query = {
        "script_score": {
            "query": {"match_all": {}},
            "script": {
                "source": source,
                "params": {"query_vector": query_embedding},
            }
        }
    }

    print("Sending script query:", script_query)

    es_client = Elasticsearch(connection_string)

    try:
        response = es_client.search(
            index=index_name,
            body={
                "size": top_k,
                "query": script_query,
                "_source": [chunk_column],
            },
        )

        print("Raw response from Elasticsearch:", response)

        results = []
        for hit in response['hits']['hits']:
            source = hit.get('_source', {})
            if chunk_column in source:
                results.append(source[chunk_column])
            else:
                print(f"Warning: '{chunk_column}' not found in document ID {hit['_id']}. Available fields: {list(source.keys())}")

        return results

    except exceptions.BadRequestError as e:
        print(f"BadRequestError: {e.info}")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        return []
```

Який максимальний бал ви отримали після виконання запиту?

1. [ ] 1.036011
1. [ ] 1.045001
1. [ ] 1.054201
1. [ ] Якщо жоден із наведених вище, введіть свій максимальний бал, що повернувся

# Примітки

Якщо у вас виникнуть додаткові запитання або вам потрібні роз’яснення щодо коду, наданого у вправі, не соромтеся звертатися по допомогу!