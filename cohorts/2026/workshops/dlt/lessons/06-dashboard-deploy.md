# Part 2: Deploy the dashboard and schedule

The pipeline is deployed and writing to the playground lake. Now we
deploy the marimo dashboard alongside it and set up a schedule.

## Add the dashboard to the deployment

Import the dashboard module in `__deployment__.py` and add it to
`__all__`:

```python
from agent_traces_dashboard import app as agent_traces_dashboard
```

This registers the dashboard as an interactive job. The platform can
run pipelines and interactive applications like marimo notebooks or
Streamlit apps.

The dashboard also needs to point at the playground destination, not
DuckDB.

Update the connection:

```python
dlt.attach("agent_traces", destination="playground", dataset_name="agent_logs")
```

When deploying notebooks, you must pass `destination` and `dataset_name`
explicitly to `dlt.attach()`.

Deploy and run:

```bash
uv run dlthub deploy
uv run dlthub run
```

## Run mode

Open the notebook in the platform UI. It runs in run mode, not edit
mode, so all the code is hidden and you see only the reports and
visuals. This is the view you share with your team.

The data lives in the playground destination. It could just as well
be MotherDuck, BigQuery, Snowflake, or a vector database like
LanceDB. dlt writes to all of them with the same pipeline code.

## Share it

Publish the dashboard to get a public URL:

```bash
uv run dlthub job publish agent_traces_dashboard
```

Or share it within the workspace via the platform's Users and Roles.

## Scheduling


To keep the data fresh, schedule the pipeline to run on a cron
trigger.

Add it to the decorator in `__deployment__.py`:

```python
from dlt.hub.run import trigger

@run.pipeline("agent_traces", trigger=trigger.schedule("0 12 * * *"))
def ingest_agent_logs(): ...
```

Confirm the schedule:

```bash
uv run dlthub job list
```

You can also create followup chains: run the ingestion pipeline, and
on success, run the dashboard to refresh the report. The platform
supports `job.success` triggers that chain jobs together.

You can manage jobs from the platform UI too - start runs, cancel
runs, and manage schedules.

[← Deploy to the cloud](05-deploy.md) | [Where to go from here →](07-where-to-go.md)
