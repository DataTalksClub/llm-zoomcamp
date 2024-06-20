# Elastic Search 

This document contains useful things about Elasticsearch

# `multi_match` Query in Elasticsearch

The `multi_match` query is used to search for a given text across multiple fields in an Elasticsearch index.

It provides various types to control how the matching is executed and scored. 

There are multiple types of `multi_match` queries:

- `best_fields`: Returns the highest score from any one field.
- `most_fields`: Combines the scores from all fields.
- `cross_fields`: Treats fields as one big field for scoring.
- `phrase`: Searches for the query as an exact phrase.
- `phrase_prefix`: Searches for the query as a prefix of a phrase.


## `best_fields`

The `best_fields` type searches each field separately and returns the highest score from any one of the fields.

This type is useful when you want to find documents where at least one field matches the query well.


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

The `most_fields` type searches each field and combines the scores from all fields.

This is useful when the relevance of a document increases with more matching fields.

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

The `cross_fields` type treats fields as though they were one big field.

It is suitable for cases where you have fields representing the same text in different ways, such as synonyms.

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

The `phrase` type looks for the query as an exact phrase within the fields.

It is useful for exact match searches.

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

The `phrase_prefix` type searches for documents that contain the query as a prefix of a phrase.

This is useful for autocomplete or typeahead functionality.


```json
{
    "multi_match": {
        "query": "How do I run docker on Windows?",
        "fields": ["question", "text"],
        "type": "phrase_prefix"
    }
}
```