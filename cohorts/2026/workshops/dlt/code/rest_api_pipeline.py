"""dlt REST API pipeline: Claude Code Agent Logs API -> DuckDB.

Source: https://test-agent-traces-api-xt2e7ottma-ew.a.run.app
Endpoint: GET /logs — offset/limit pagination, records under `logs`, the
response envelope carries `total` (1,000,000). No auth.

Distinct pipeline_name ("agent_traces") and dataset_name ("traces") keep the
DuckDB catalog name different from the schema name, avoiding DuckDB's ambiguous
catalog/schema resolution error.
"""

import dlt
from dlt.sources.rest_api import RESTAPIConfig, rest_api_resources

BASE_URL = "https://test-agent-traces-api-xt2e7ottma-ew.a.run.app"


@dlt.source(name="agent_logs_api")
def agent_logs_source(base_url: str = dlt.config.value, page_size: int = 1000):
    """Claude Code Agent Logs API.

    Args:
        base_url: API base URL. Auto-loaded from config.toml ([sources.agent_logs_api]).
        page_size: records per page for the offset paginator.
    """
    config: RESTAPIConfig = {
        "client": {
            "base_url": base_url,
            "paginator": {
                "type": "offset",
                "limit": page_size,
                "offset": 0,
                "limit_param": "limit",
                "offset_param": "offset",
                "total_path": "total",  # read total record count from the envelope
            },
        },
        "resource_defaults": {
            "write_disposition": "replace",
        },
        "resources": [
            {
                "name": "logs",
                "endpoint": {
                    "path": "/logs",
                    "data_selector": "logs",  # records live under the "logs" key
                },
                "primary_key": "index",
            },
        ],
    }
    yield from rest_api_resources(config)


def load(full: bool = False) -> None:
    pipeline = dlt.pipeline(
        pipeline_name="agent_traces",
        destination="duckdb",
        dataset_name="traces",  # persistent dataset (distinct from catalog name)
    )
    source = agent_logs_source(base_url=BASE_URL)
    if not full:
        source.add_limit(1)  # one page = 1000 records; pass --full for all 1M
    info = pipeline.run(source)
    print(info)
    print(pipeline.last_trace.last_normalize_info)


if __name__ == "__main__":
    import sys

    load(full="--full" in sys.argv)
