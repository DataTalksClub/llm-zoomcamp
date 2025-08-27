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
import os
from phoenix.otel import register # type: ignore

def _init_tracer():
    project_name = os.getenv("PHOENIX_PROJECT_NAME", "our-rag-project")
    # If endpoint not provided, phoenix.register uses sensible defaults.
    tp = register(protocol="http/protobuf", project_name=project_name)
    return tp.get_tracer("course-ta")

tracer = _init_tracer()
