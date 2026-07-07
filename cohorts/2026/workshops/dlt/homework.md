<!-- DRAFT - not final. Homework content is a placeholder based on
     the 2024/2025 dlt workshop patterns, not confirmed by the
     instructor. -->

# Homework: dlt workshop

> Draft. The homework will be finalized based on the workshop content.

In this homework, we load data with dlt and answer questions about
what landed in DuckDB.

> It's possible your answers won't match exactly. If so, select the
closest one.

## Setup

Prepare your environment the same way as in the
[Overview and setup](lessons/01-overview.md) lesson.

Install dlt with DuckDB support:

```bash
pip install -q "dlt[duckdb]" duckdb
```

## Question 1. dlt version

What's the version of dlt that you installed?

## Question 2. dlt resource

Annotate this helper function with `@dlt.resource` so dlt knows it
yields records:

```python
def zoomcamp_data():
    docs_url = 'https://github.com/alexeygrigorev/llm-rag-workshop/raw/main/notebooks/documents.json'
    docs_response = requests.get(docs_url)
    documents_raw = docs_response.json()

    for course in documents_raw:
        course_name = course['course']
        for doc in course['documents']:
            doc['course'] = course_name
            yield doc
```

We'll use it when creating a dlt pipeline.

## Question 3. dlt pipeline

Create a pipeline that loads the `zoomcamp_data` resource into
DuckDB:

```python
pipeline = dlt.pipeline(
    pipeline_name="zoomcamp_pipeline",
    destination="duckdb",
    dataset_name="zoomcamp_tagged_data",
)
load_info = pipeline.run(zoomcamp_data())
print(pipeline.last_trace)
```

How many rows were inserted into the `zoomcamp_data` collection?

Look for `Normalized data for the following tables:` in the trace
output.

## Question 4. REST API pagination

In the [REST API pipeline](lessons/04-rest-api-pipeline.md), we
configured an offset paginator. The API returns 1,000,000 total
records. If `page_size` is 1000, how many requests does dlt make to
load all records (not counting the final request that returns an
empty page)?

## Submit the results

* Submit your results here: https://courses.datatalks.club/llm-zoomcamp-2026/homework/dlt
