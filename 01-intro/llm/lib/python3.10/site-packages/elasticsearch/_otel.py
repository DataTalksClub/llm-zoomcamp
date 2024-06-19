#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

from __future__ import annotations

import contextlib
import os
from typing import TYPE_CHECKING, Generator, Mapping

if TYPE_CHECKING:
    from typing import Literal

try:
    from opentelemetry import trace

    _tracer: trace.Tracer | None = trace.get_tracer("elasticsearch-api")
except ModuleNotFoundError:
    _tracer = None

from elastic_transport import OpenTelemetrySpan

# Valid values for the enabled config are 'true' and 'false'. Default is 'true'.
ENABLED_ENV_VAR = "OTEL_PYTHON_INSTRUMENTATION_ELASTICSEARCH_ENABLED"
# Describes how to handle search queries in the request body when assigned to
# a span attribute.
# Valid values are 'omit' and 'raw'.
# Default is 'omit' as 'raw' has security implications.
BODY_STRATEGY_ENV_VAR = "OTEL_PYTHON_INSTRUMENTATION_ELASTICSEARCH_CAPTURE_SEARCH_QUERY"
DEFAULT_BODY_STRATEGY = "omit"


class OpenTelemetry:
    def __init__(
        self,
        enabled: bool | None = None,
        tracer: trace.Tracer | None = None,
        # TODO import Literal at the top-level when dropping Python 3.7
        body_strategy: 'Literal["omit", "raw"]' | None = None,
    ):
        if enabled is None:
            enabled = os.environ.get(ENABLED_ENV_VAR, "true") == "true"
        self.tracer = tracer or _tracer
        self.enabled = enabled and self.tracer is not None

        if body_strategy is not None:
            self.body_strategy = body_strategy
        else:
            self.body_strategy = os.environ.get(
                BODY_STRATEGY_ENV_VAR, DEFAULT_BODY_STRATEGY
            )  # type: ignore[assignment]
            assert self.body_strategy in ("omit", "raw")

    @contextlib.contextmanager
    def span(
        self,
        method: str,
        *,
        endpoint_id: str | None,
        path_parts: Mapping[str, str],
    ) -> Generator[OpenTelemetrySpan, None, None]:
        if not self.enabled or self.tracer is None:
            yield OpenTelemetrySpan(None)
            return

        span_name = endpoint_id or method
        with self.tracer.start_as_current_span(span_name) as otel_span:
            otel_span.set_attribute("http.request.method", method)
            otel_span.set_attribute("db.system", "elasticsearch")
            if endpoint_id is not None:
                otel_span.set_attribute("db.operation", endpoint_id)
            for key, value in path_parts.items():
                otel_span.set_attribute(f"db.elasticsearch.path_parts.{key}", value)

            yield OpenTelemetrySpan(
                otel_span,
                endpoint_id=endpoint_id,
                body_strategy=self.body_strategy,
            )
