"""Phoenix + OpenInference tracing bootstrap.
Install deps:
  pip install arize-phoenix openinference-semantic-conventions opentelemetry-api opentelemetry-sdk

Environment:
- PHOENIX_PORT (optional, default 6006)
- PHOENIX_HOST (optional, default 127.0.0.1)
- PHOENIX_PROJECT_NAME (optional, default "course-ta")
If you're using Phoenix Cloud, set PHOENIX_API_KEY in your environment; phoenix.otel.register will pick it up.
This setup targets a local Phoenix instance by default.
"""
from phoenix.otel import register # type: ignore
from config import PROJECT_NAME



def _init_tracer():
    # If endpoint not provided, phoenix.register uses sensible defaults.
    tp = register(project_name=PROJECT_NAME, auto_instrument=True)
    return tp.get_tracer(PROJECT_NAME)

tracer = _init_tracer()
