# Next steps and recap

## Recap

We built two dlt pipelines and two dashboards, then deployed them to
the cloud:

- A filesystem pipeline loading local Claude Code logs into DuckDB
- A marimo dashboard over that data
- A REST API pipeline pulling traces from a hosted API
- A scheduled deployment on the dltHub Platform with a shareable
  dashboard

You described what you wanted in plain English, and the coding agent
used the dltHub AI workbench to write the pipelines. The workbench's
toolkits, skills, and MCP tools handled the dlt-specific knowledge so
you didn't have to.

## Incremental loading

Both pipelines use `write_disposition="replace"` with `dev_mode=True`,
which means they drop and reload everything on each run. That's fine
for development but doesn't scale once you have millions of rows.

dlt tracks the last loaded value of a cursor column and uses it as a
filter on subsequent runs. The cursor is stored in pipeline state, so
it persists across runs.

For the filesystem pipeline, filter by file modification date:

```python
files = filesystem(
    bucket_url="...",
    file_glob="...",
    incremental=dlt.sources.incremental("modification_date"),
)
```

For the REST API pipeline, use a sequential id:

```python
"resources": [
    {
        "name": "logs",
        "endpoint": {"path": "/logs", "data_selector": "logs"},
        "primary_key": "index",
        "incremental": dlt.sources.incremental("index"),
    },
]
```

Switch `write_disposition` to `"merge"` so existing rows are updated
and new rows are inserted, without dropping anything. Remove
`dev_mode` from the pipeline so data persists.

## Other sources

dlt has many built-in sources beyond filesystem and REST API:

- `sql_database` - incremental loads from Postgres, MySQL, and others
- `google_sheets` - pull data straight from a spreadsheet
- `notion` - load Notion pages and databases
- `hubspot`, `salesforce`, `stripe` - vendor-specific sources with
  auth handled for you

The workflow is always the same: configure the source, create a
pipeline, run it.

## Other destinations

The same pipeline code works with Postgres, BigQuery, Snowflake, and
Redshift. Only the destination string and credentials change.

## Key concepts

Here's where each concept showed up in the workshop:

- Toolkits: filesystem, rest-api, data-exploration,
  dlthub-platform - installed on demand, each a guided workflow
- MCP tools: look at pipelines, schemas, row counts, and previews
- dlt normalization: nested JSON becomes typed tables and child
  tables
- REST API source: offset pagination, `data_selector`,
  `maximum_offset`
- Named destinations: `playground` is duckdb for dev or S3 lake for
  prod, one code path
- marimo: reactive notebooks with SQL-first data cells and altair
  chart cells
- Scheduling and triggers: cron `schedule` and `job.success` followup
  chains, declared in decorators

## Artifacts you produced

You produced these files:

```text
filesystem_pipeline.py              # Part 1: local Claude logs -> DuckDB
claude_logs_dashboard.py            # Part 1: usage report
rest_api_pipeline.py                # Part 2: agent_traces API -> lake
agent_traces_dashboard.py           # Part 2: agent_traces report
__deployment__.py                   # deployment manifest (jobs + triggers)
```

## To learn more

These resources go deeper on each topic:

- [dlt documentation](https://dlthub.com/docs) - the full reference
- [dltHub AI workbench](https://dlthub.com/docs/dlt-ecosystem/llm-tooling/llm-native-workflow) -
  toolkits, skills, and the MCP server
- [Deploy and schedule on the runtime](https://dlthub.com/docs/hub/getting-started/runtime-tutorial) -
  jobs, schedules, triggers
- [marimo documentation](https://docs.marimo.io) - reactive notebooks
- [Altair encodings](https://altair-viz.github.io/user_guide/encodings/channels.html)

[← Dashboard and scheduling](06-dashboard-deploy.md)
