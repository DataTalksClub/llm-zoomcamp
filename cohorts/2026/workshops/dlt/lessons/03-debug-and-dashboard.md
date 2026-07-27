# Part 1: Debug and build a dashboard

The pipeline runs and loads data, but it created 78 tables. Before we
build a dashboard, we want to make sure the pipeline is correct and the
schema is manageable.

## Debug the pipeline

The agent already ran the pipeline and it works, but we want to be
explicit. Tell the agent:

> debug my pipeline

The agent finds the debug-pipeline skill in the rest-api-pipeline
toolkit and installs it. Debugging means the agent runs the pipeline,
inspects the trace, checks for errors, and fixes them until it works.

As Alena explains in the workshop, debugging makes sure the pipeline
doesn't fail and loads some data. But it can't tell you whether the
data is correct. That's a judgment only you can make by looking at the
output.

## Schema pollution fix

During debugging, the agent noticed that 78 tables was excessive. It
identified this as schema pollution - the deeply nested JSON was
exploding into too many child tables.

The agent fixed it by setting some columns to the JSON data type instead of
unnesting them into child tables. Not all data was unnested. Instead
of 78 tables, the pipeline now creates 40. The deeply nested fields
stay as JSON columns that you can query later with DuckDB's JSON
functions.

## Build a marimo report

Now that the pipeline is clean, tell the agent to build a dashboard:

> build a marimo report with detailed information about my Claude Code
> usage

The agent installs the data-exploration toolkit. This toolkit contains
skills for profiling data, planning charts, and assembling marimo
notebooks.

First the agent profiles the data: row counts, schemas, column stats.
It writes an analysis plan - a markdown file listing the questions to
answer, the SQL queries, and the Altair chart code for each one. Then
it assembles the notebook.

## marimo reactive notebooks

marimo is a reactive Python notebook. Every notebook is a plain Python
script, not a JSON blob. Each cell is a Python function. When you
change a cell, every cell that depends on it re-runs automatically.

Unlike Jupyter, you can't run cells in random order, so there's
always a defined order, which prevents variable mix-ups. This
strictness makes marimo better for dashboards, because the state is
always consistent.

The dashboard (see [code/claude_logs_dashboard.py](../code/claude_logs_dashboard.py))
connects to the pipeline and queries the data with SQL:

```python
pipeline = dlt.attach("agent_logs")
dataset = pipeline.dataset()

df = dataset("""
    SELECT agent, COUNT(*) AS records
    FROM log_records
    GROUP BY 1
    ORDER BY records DESC
""").df()
```

Each chart is a data cell that runs SQL and returns a DataFrame, paired
with a chart cell that builds an Altair visualization:

```python
chart = alt.Chart(df).mark_bar().encode(
    x=alt.X("agent:N", sort="-y"),
    y="records:Q",
    color="agent:N",
    tooltip=["agent:N", "records:Q"],
).properties(title="Total Log Records by Agent")
```

The dashboard shows activity over time, messages by type, models,
token usage, and top projects. In the live session, Alena could
see her vacation week as a gap in activity.

Opus was her most-used model.

Run the dashboard:

```bash
uv run marimo edit code/claude_logs_dashboard.py
```

[← Filesystem pipeline](02-filesystem-pipeline.md) | [REST API pipeline →](04-rest-api-pipeline.md)
