# Part 1: Local logs to pipeline

With the workspace scaffolded, we now build a dlt pipeline that
reads the JSONL session transcripts from `~/.claude/projects/` and
loads them into DuckDB. We don't write the code by hand. We tell
the agent what to build, and it uses the dltHub AI workbench to
write the pipeline.

## Look at the raw logs

Open `~/.claude/projects/` and pick a `.jsonl` file. Every session
is one file with one JSON object per line.

The `type` values vary across lines. Some common ones:

- `user`
- `assistant`
- `attachment`
- `file-history-snapshot`

The data is deeply nested, with usage objects holding token counts
and message objects holding content arrays.

This is real, valuable data - models used, tokens spent, and tools
called. But it's trapped in a format that's painful to query
manually.

## Build the pipeline

Tell the agent to build a dlt pipeline for the local logs:

> build a dlt pipeline, load data from local Claude logs as raw JSONs
> into DuckDB

The agent starts with the dltHub router skill, which figures out that
the data lives in files on disk. It installs the filesystem-pipeline
toolkit on demand - this toolkit didn't exist in the project when you
started. The router pulls it in based on the data source.

The toolkit walks the agent through the standard workflow:

- confirm the plan
- scaffold the pipeline
- configure credentials
- run it

## The pipeline the agent builds

The pipeline uses dlt's `filesystem` source with the `read_jsonl`
reader. The source lists files matching a glob, and the reader opens
each one and yields parsed JSON records.

dlt connects them with the pipe operator:
pipe operator:

```python
from dlt.sources.filesystem import filesystem, read_jsonl

reader = (
    filesystem(file_glob="**/*.jsonl")
    | read_jsonl()
).with_name("messages")
```

The full pipeline (see [code/filesystem_pipeline.py](../code/filesystem_pipeline.py))
defines a `load` function that creates the pipeline and runs it:

```python
pipeline = dlt.pipeline(
    pipeline_name="agent_logs",
    destination="duckdb",
    dataset_name="agent_logs",
    dev_mode=True,
)
load_info = pipeline.run(reader, write_disposition="replace")
```

A few things to notice.

`dev_mode=True` adds a timestamp to the dataset name on every run, so
each run starts fresh. That's convenient during development but
wasteful in production - we'll switch it off later.

`write_disposition="replace"` drops and reloads the table each time.

## Normalization: 78 tables

When the pipeline runs, dlt doesn't just dump the raw JSON into one
table. It normalizes the data by inferring types, flattening nested
objects, and creating child tables for nested arrays, linked by
`_dlt_id` and `_dlt_parent_id`.

The first run created 78 tables. The agent logs are heavily nested,
so dlt unnested every array into its own child table. That's correct
behavior, but 78 tables is a lot to work with. We'll fix that in the
next step.

## View the data locally

dlt ships with a built-in dashboard. Run it from the command line,
not from the agent session.

Make sure your pipeline ran successfully first:

```bash
uv run dlthub local show
```

This opens a marimo dashboard that reads from the local DuckDB file.
You can browse the schema, see how many tables exist, look at the data
in each table, and run SQL queries. This is where you validate that the
pipeline loaded what you expected.

[← Overview](01-overview.md) | [Debug and dashboard →](03-debug-and-dashboard.md)
