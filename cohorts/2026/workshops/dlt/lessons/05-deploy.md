# Part 2: Deploy to the cloud

Both pipelines work locally, but you can't share local dashboards with
your team. The dltHub Platform lets you deploy pipelines and dashboards
to the cloud, schedule them, and share them with colleagues.

## Log in

Connect your local workspace to the dltHub Platform:

```bash
uv run dlthub login              # device-code OAuth in the browser
uv run dlthub workspace connect  # pick or create a workspace
```

After connecting, open the platform UI:

```bash
uv run dlthub show
```

Every new account has a playground workspace. Your local workspace
connects to it automatically, so anything you run locally syncs to
the platform.

## Deploy the pipeline

Tell the agent to deploy the REST API pipeline:

> deploy this on the dlthub platform, use duckdb as destination

The agent installs the dlthub-platform toolkit. It goes through a
five-step checklist before deploying, then registers the pipeline in
`__deployment__.py` and deploys it.

You can also do it manually:

```bash
uv run dlthub deploy   # ship the current project as a new version
uv run dlthub run      # run the pipeline on the cloud
```

Repeat this deploy-and-run cycle after every code change so the cloud
always reflects your latest version.

## Ephemeral storage

When you deploy with DuckDB as the destination, the data goes to
ephemeral storage. The platform runs your pipeline in a container,
and when the job finishes, the local files are removed. The data
doesn't persist across runs.

## Switch to the Playground destination

To persist data, switch from `duckdb` to the `playground` destination,
which is a managed S3 lake that keeps data across runs.

In `rest_api_pipeline.py`, change the destination:

```python
# was:
#   destination="duckdb"
# now:
destination="playground"
```


The playground destination requires the `deltalake` package, so
after changing the destination, redeploy and run it.

Then run the pipeline again:
```bash
uv run dlthub deploy
uv run dlthub run
```

If the run fails because `deltalake` is missing, the deploy step adds
the dependency to `pyproject.toml` automatically. Redeploy and run
again.

[← REST API pipeline](04-rest-api-pipeline.md) | [Dashboard and scheduling →](06-dashboard-deploy.md)
