# Part 2: Ingest from a hosted API

Part 1 loaded local logs from disk. But in a real organization, your
agents run in the cloud and their logs live behind an API. Think
Logfire, Langfuse, Datadog, or the Anthropic API. You can't read files
from disk. You have to request the data over HTTP.

For this workshop, Alena built a test API that serves one million
fake Claude Code traces in the same structure as real logs. No
authentication is required, and the data is safe to share. The base
URL is:

```text
https://test-agent-traces-api-xt2e7ottma-ew.a.run.app
```

## Cloud loggers

When you build an agent, its logs live in a cloud logger. Services like
Logfire and Langfuse collect metadata similar to the local Claude
traces: usage, models, tool calls, skills used. To analyze this data,
you request it through the logger's REST API and load it into a
database.

Each logger produces a different trace format with different keys,
different nesting, different field order. That's always a problem when
you have several agents. dlt handles the normalization for you.

## Build the pipeline

Continue working in the same repo and tell the agent:

> build a dlt pipeline for https://test-agent-traces-api-xt2e7ottma-ew.a.run.app/docs, for /logs endpoint, load 20k logs into DuckDB, and build a similar marimo report

The agent installs the rest-api-pipeline toolkit. This toolkit
contains skills for creating pipelines, debugging, exploring data,
and applying incremental loading.

The agent inspects the OpenAPI spec at the `/docs` URL, figures out
the base URL, the pagination type, and the data selector, and writes
the pipeline. If you've ever built a data pipeline against an API
by hand, you know how much work this saves. You need to know how to
request the data, how to paginate, and what the output
looks like.
request the data, how to paginate, and what the output looks like.

## The REST API source

The pipeline (see [code/rest_api_pipeline.py](../code/rest_api_pipeline.py))
describes the API as a config dictionary:

```python
config: RESTAPIConfig = {
    "client": {
        "base_url": base_url,
        "paginator": {
            "type": "offset",
            "limit": page_size,
            "offset": 0,
            "limit_param": "limit",
            "offset_param": "offset",
            "total_path": "total",
        },
    },
    "resources": [
        {
            "name": "logs",
            "endpoint": {
                "path": "/logs",
                "data_selector": "logs",
            },
            "primary_key": "index",
        },
    ],
}
```

The `data_selector` tells dlt that the records live under the `logs`
key in the response envelope, not at the top level. The paginator uses
offset-based pagination: each request sends `limit` and `offset` query
params, and dlt reads the total count from the `total` key to know when
to stop. A `maximum_offset` of 20000 caps the load at 20k rows without
you hand-rolling pagination loops.

## Run it

Run the pipeline with a sample first, then a full load:

```bash
uv run python code/rest_api_pipeline.py          # one page, 1000 records
uv run python code/rest_api_pipeline.py --full   # all 1 million records
```

The same normalization happens: dlt infers types, flattens nested
objects like `message.content` into child tables linked by
`_dlt_parent_id`. The nested `usage` object becomes columns like
`usage__output_tokens` with double-underscore separators.

[← Debug and dashboard](03-debug-and-dashboard.md) | [Deploy to the cloud →](05-deploy.md)
