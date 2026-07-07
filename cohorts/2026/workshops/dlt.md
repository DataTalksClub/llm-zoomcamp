# Workshop: From local Claude logs to a scheduled data platform with dltHub + AI

Recording: https://www.youtube.com/live/A0LmmZf-ggM?si=9Mb226_V9-Gxq7wo

Event: https://luma.com/3sint80a

In this workshop you'll build real data pipelines, dashboards, and a scheduled
cloud deployment, driven almost entirely by natural-language prompts in Claude
Code, using the **[dltHub AI workbench](https://dlthub.com/docs/dlt-ecosystem/llm-tooling/llm-native-workflow)**
(dlt + toolkits + MCP), **DuckDB**, **marimo**, and the **dltHub Platform**.

## Who this is for

Data engineers / data analytics / ML engineers / AI engineers who want to see how an AI agent + dlt turns a
messy data source into an ingested, modeled, visualized, and *scheduled*
data product, without hand-writing boilerplate.

## What you'll build

By the end you will have:

1. A dlt pipeline loading your **local Claude Code logs** (raw JSONL) into DuckDB.
2. A dlt **REST API** pipeline loading agent logs from a hosted API.
3. Interactive **marimo** dashboards over each dataset.
4. A **scheduled deployment** on the dltHub Platform: an ingestion pipeline and
   an interactive dashboard.

## Prerequisites

- `uv` (the runner installs it if missing)
- Claude Code (or another supported AI coding agent)
- A dltHub Platform account (free): [app.dlthub.com](https://app.dlthub.com/) 
- Some local Claude Code (or other agents) usage so `~/.claude/projects/` has logs to load

## How to follow along

Each step gives you the **prompt** to paste into Claude (in `> quote` blocks) or
the **command** to run, tells you **what to look at**, and notes the **concept**
you just used. When you send a prompt, the agent pulls in a dltHub
*[toolkit](https://dlthub.com/docs/dlt-ecosystem/llm-tooling/llm-native-workflow)*:
an installable workflow (skills + rules) that walks it through the task and hands
off to the next one, so you don't have to know the dlt API by heart.

---

# Part 1: Local logs → pipeline → dashboard

**Goal:** you *can* analyze your local Claude logs by hand, but with dlt + AI
you'll make it structured, repeatable, and fast.

### 1. Look at your local Claude logs
Open `~/.claude/projects/`. Every session is a `*.jsonl` file: one JSON object
per line, with heterogeneous `type` values (`user`, `assistant`, `attachment`,
`file-history-snapshot`, …), deeply nested.
> Notice: this is real, valuable data (models used, tokens, tools, projects)
> trapped in an awkward nested format.

### 2. Why not just parse it by hand?
You *could* parse these files with a notebook, but it's expensive and
time-consuming: schema drift between record types, nested arrays, no types.
> Instead, you'll let dlt do normalization + typing + incremental loading for you.

### 3. Set up the workspace
```bash
uvx dlthub-init@latest
```
It scaffolds a dltHub workspace with AI support
(`.dlt/`, MCP config, toolkits). Then, in Claude, confirm it worked with
`uv run dlthub ai status`.

### 4. Build your first pipeline (prompt)
> **build a dlt pipeline, load data from local Claude logs as raw JSONs into DuckDB**

The agent installs the **filesystem-pipeline** toolkit and writes
`filesystem_pipeline.py`: `filesystem(file_glob="**/*.jsonl") | read_jsonl()`
reading `~/.claude/projects/` and loading a `logs` table into DuckDB.
See the [filesystem source docs](https://dlthub.com/docs/dlt-ecosystem/verified-sources/filesystem).

### 5. See how the AI workbench works
While it runs, notice three things:
- **Toolkits**: the agent installed `filesystem-pipeline` on demand and followed
  its workflow rule (gather inputs → scaffold → configure → run).
- **MCP server** (`dlt-workspace-mcp`): tools like `list_pipelines`,
  `list_tables`, `get_row_counts`, `preview_table`, `export_schema` let the agent
  inspect pipelines and data directly.
- **Skills**: each step (create / debug / validate) is a guided skill.

### 6. Open the local dashboard and look at the data
dlt fully unnests the raw JSON into a main `logs` table + many child tables
(`logs__message__content`, etc.), linked by `_dlt_id` / `_dlt_parent_id`. Browse
it with the MCP tools or run `uv run dlthub local show`. See how dlt builds these
[nested/child tables](https://dlthub.com/docs/general-usage/destination-tables).

### 7. Walk through the pipeline to see how dlt works
Open `filesystem_pipeline.py` and look for the dlt model
([how dlt works](https://dlthub.com/docs/reference/explainers/how-dlt-works)):
- **extract → normalize → load** stages
- **resources** and the `filesystem | reader` pipe
- **schema inference**, nested-table normalization, `write_disposition="replace"`
- config (`bucket_url` in `.dlt/config.toml`) vs code (`file_glob` inline)

### 8. Build a marimo report (prompt)
> **create a marimo report with detailed information about my Claude Code usage**

The agent installs the **data-exploration** toolkit, profiles the data, writes an
`analysis_plan.md`, then assembles `claude_logs_dashboard.py` and launches it.
See [exploring data with marimo](https://dlthub.com/docs/general-usage/dataset-access/marimo).

### 9. Walk through the report to see how marimo works
Open `claude_logs_dashboard.py`:
- marimo is a **reactive** Python notebook: cells form a dependency graph, with
  no hidden execution order; edit a query and its dependents re-run.
- the connection cell uses `dlt.attach(...).dataset()`, never raw duckdb.
- each chart = a **data cell** (SQL → `.df()`) + a **chart cell** (altair).
- you get KPIs, activity-over-time, models, tokens, tools, projects.

---

# Part 2: Ingest from a hosted API, then deploy to the cloud

**Goal:** most logs live in a cloud logger behind an API. You'll ingest from one,
then take the whole thing to production on the dltHub Platform.

> Note: for this workshop we built the API ourselves: a Claude Code logs
> endpoint that serves logs in the **real, structured shape** you saw in Part 1,
> but with **fake data**. So there's nothing sensitive to worry about, and
> everyone gets the same 1m rows to work with.

### 1. A note on cloud loggers
Datadog, Logfire, CloudWatch, etc. all expose logs via paginated REST APIs. The
pattern is always the same: paginate, select the records array, load, schedule.

### 2. Build a REST API pipeline (prompt)
> **build a dlt pipeline for https://test-agent-traces-api-xt2e7ottma-ew.a.run.app/docs, for /logs endpoint, load 20k logs into DuckDB, and build a similar marimo report**

The agent installs **rest-api-pipeline**, inspects the OpenAPI spec, and writes
`rest_api_pipeline.py` (pipeline `agent_traces`, dataset `agent_logs`).
See the [REST API source docs](https://dlthub.com/docs/dlt-ecosystem/verified-sources/rest_api/basic).

### 3. Walk through the pipeline to see the REST API source
Open `rest_api_pipeline.py`:
- `RESTAPIConfig` with `client.base_url` + `paginator`.
- an **[offset paginator](https://dlthub.com/docs/api_reference/dlt/sources/helpers/rest_client/paginators)**
  (`offset`/`limit`, `total_path`, `maximum_offset=20000`) caps the load at 20k
  rows without you hand-rolling pagination loops.
- `data_selector: "logs"` picks the records array out of the envelope.
- `primary_key` for dedupe/merge.

### 4. Walk through the marimo report
The agent builds `agent_traces_dashboard.py`, the same shape as Part 1 but over
the API data (activity, models, tokens, top tools, git branches, projects).

### 5. Deploy to DuckDB on the platform (prompt + login)
> **deploy this on the dlthub platform, use duckdb as destination**

The agent installs **dlthub-platform** and runs `setup-runtime`
(see the [deploy & schedule tutorial](https://dlthub.com/docs/hub/getting-started/runtime-tutorial)).
Then you log in:
```bash
uv run dlthub login              # device-code OAuth in the browser
uv run dlthub workspace connect  # pick/create a workspace
```
It decorates the run with `@run.pipeline("agent_traces")`, registers it in
`__deployment__.py`, deploys, and runs it on the cloud.

> Notice: the cloud run writes DuckDB to **ephemeral `/tmp`**, so the data doesn't
> persist. That's why you'll switch to a real lake destination next.

### 6. Add DeltaLake, switch to the Playground destination, run
Add the DeltaLake extra to `pyproject.toml` (`deltalake`), then switch the
pipeline `destination` to the **`playground`** named destination (your workspace's
managed S3 lake). Now the data persists in the lake across runs.

Any time you change the project (code, config, or dependencies), push the new
version to the platform and run it again:
```bash
uv run dlthub deploy              # ship the current project as a new version
uv run dlthub run   # run the pipeline on the cloud
```
> Repeat this `deploy` → `run` cycle after **every** change you make in the rest
> of Part 2, so the cloud always reflects your latest code.

### 7. Point the marimo report at Playground
Update the dashboard's connection to read from the lake:
```python
dlt.attach("agent_traces", destination="playground", dataset_name="agent_logs")
```
> Note: deployed notebooks must pass `destination` + `dataset_name` explicitly to
> `dlt.attach()`.

### 8. Add the marimo report to deployments and show it
Import the dashboard module in `__deployment__.py` and add it to `__all__`. It
registers as an **interactive** job. Deploy it and open it in the platform UI.

### 9. Share it: colleagues / Users & Roles
```bash
uv run dlthub job publish agent_traces_dashboard   # public URL
```
Or share it within the workspace via the platform's **Users & Roles**.

### 10. Schedule it
Add a cron trigger to the decorator and redeploy:
```python
from dlt.hub.run import trigger

@run.pipeline("agent_traces", trigger=trigger.schedule("0 12 * * *"))
def ingest_agent_logs(): ...
```
Run `uv run dlthub job list` to confirm the schedule.

---

## Key concepts recap

| Concept | Where you used it |
|---|---|
| **Toolkits** | filesystem, rest-api, data-exploration, dlthub-platform (installed on demand, each a guided workflow) |
| **MCP tools** | inspect pipelines, schemas, row counts, previews during the whole session |
| **dlt normalization** | nested JSON → typed tables + child tables |
| **REST API source** | offset pagination, `data_selector`, `maximum_offset` |
| **Named destinations** | `playground` = duckdb (dev) / S3 lake (prod), one code path |
| **marimo** | reactive notebooks, SQL-first data cells + altair chart cells |
| **Scheduling & triggers** | cron `schedule` + `job.success` followup chains, declared in decorators |

## Artifacts you produced

```
filesystem_pipeline.py              # Part 1: local Claude logs -> DuckDB
claude_logs_dashboard.py            # Part 1: usage report
rest_api_pipeline.py                # Part 2: agent_traces API -> lake
agent_traces_dashboard.py           # Part 2: agent_traces report
__deployment__.py                   # deployment manifest (jobs + triggers)
```

## Further reading

- [dltHub AI workbench (LLM-native workflow)](https://dlthub.com/docs/dlt-ecosystem/llm-tooling/llm-native-workflow): toolkits, skills, and the MCP server
- [Agents can write, run & deploy dlt pipelines](https://dlthub.com/blog/ai-workbench): the AI workbench announcement
- [How dlt works](https://dlthub.com/docs/reference/explainers/how-dlt-works): extract → normalize → load
- [Destination tables & lineage](https://dlthub.com/docs/general-usage/destination-tables): nested/child tables, `_dlt_id` / `_dlt_parent_id`
- [Filesystem source](https://dlthub.com/docs/dlt-ecosystem/verified-sources/filesystem): read local files (`read_jsonl`, `file_glob`)
- [REST API source](https://dlthub.com/docs/dlt-ecosystem/verified-sources/rest_api/basic): `RESTAPIConfig`, `data_selector`, `primary_key`
- [Paginators](https://dlthub.com/docs/api_reference/dlt/sources/helpers/rest_client/paginators): offset pagination, `maximum_offset`
- [Explore data with marimo](https://dlthub.com/docs/general-usage/dataset-access/marimo): reactive notebooks over your datasets
- [Deploy & schedule on the runtime](https://dlthub.com/docs/hub/getting-started/runtime-tutorial): jobs, schedules, triggers
