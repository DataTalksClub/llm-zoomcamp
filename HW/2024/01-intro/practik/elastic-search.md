# Elastic Search

Цей документ містить корисну інформацію про Elasticsearch

# Запит `multi_match` в Elasticsearch

Запит `multi_match` використовується для пошуку заданого тексту в кількох полях індексу Elasticsearch.

Він надає різні типи для контролю того, як здійснюється і оцінюється пошук.

Існує кілька типів запитів `multi_match`:

- `best_fields`: Повертає найвищий бал з будь-якого одного поля.
- `most_fields`: Об'єднує бали з усіх полів.
- `cross_fields`: Вважає поля одним великим полем для оцінки.
- `phrase`: Шукає запит як точну фразу.
- `phrase_prefix`: Шукає запит як префікс фрази.


## `best_fields`

Тип `best_fields` шукає кожне поле окремо і повертає найвищий бал з будь-якого одного з полів.

Цей тип корисний, коли ви хочете знайти документи, де принаймні одне поле добре відповідає запиту.

```json
{
    "size": 5,
    "query": {
        "bool": {
            "must": {
                "multi_match": {
                    "query": "How do I run docker on Windows?",
                    "fields": ["question", "text"],
                    "type": "best_fields"
                }
            }
        }
    }
}
```

## `most_fields`

Тип `most_fields` шукає кожне поле і об'єднує бали з усіх полів.

Це корисно, коли релевантність документа збільшується з більшою кількістю відповідних полів.

```json
{
    "multi_match": {
        "query": "How do I run docker on Windows?",
        "fields": ["question^4", "text"],
        "type": "most_fields"
    }
}
```

## `cross_fields`

Тип `cross_fields` розглядає поля як одне велике поле.

Він підходить для випадків, коли у вас є поля, що представляють один і той самий текст по-різному, наприклад, синоніми.

```json
{
    "multi_match": {
        "query": "How do I run docker on Windows?",
        "fields": ["question", "text"],
        "type": "cross_fields"
    }
}
```

## `phrase`

Тип `phrase` шукає запит як точну фразу в полях.

Він корисний для пошуку точних відповідностей.

```json
{
    "multi_match": {
        "query": "How do I run docker on Windows?",
        "fields": ["question", "text"],
        "type": "phrase"
    }
}
```

## `phrase_prefix`

Тип `phrase_prefix` шукає документи, що містять запит як префікс фрази.

Це корисно для автозаповнення або функціоналу підказок.

```json
{
    "multi_match": {
        "query": "How do I run docker on Windows?",
        "fields": ["question", "text"],
        "type": "phrase_prefix"
    }
}
```