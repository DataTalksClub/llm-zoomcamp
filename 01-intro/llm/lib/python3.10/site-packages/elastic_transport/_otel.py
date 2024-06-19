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

from typing import TYPE_CHECKING, Mapping

if TYPE_CHECKING:
    from typing import Literal

    from opentelemetry.trace import Span


# A list of the Elasticsearch endpoints that qualify as "search" endpoints. The search query in
# the request body may be captured for these endpoints, depending on the body capture strategy.
SEARCH_ENDPOINTS = (
    "search",
    "async_search.submit",
    "msearch",
    "eql.search",
    "esql.query",
    "terms_enum",
    "search_template",
    "msearch_template",
    "render_search_template",
)


class OpenTelemetrySpan:
    def __init__(
        self,
        otel_span: Span | None,
        endpoint_id: str | None = None,
        # TODO import Literal at the top-level when dropping Python 3.7
        body_strategy: 'Literal["omit", "raw"]' = "omit",
    ):
        self.otel_span = otel_span
        self.body_strategy = body_strategy
        self.endpoint_id = endpoint_id

    def set_node_metadata(
        self, host: str, port: int, base_url: str, target: str
    ) -> None:
        if self.otel_span is None:
            return

        # url.full does not contain auth info which is passed as headers
        self.otel_span.set_attribute("url.full", base_url + target)
        self.otel_span.set_attribute("server.address", host)
        self.otel_span.set_attribute("server.port", port)

    def set_elastic_cloud_metadata(self, headers: Mapping[str, str]) -> None:
        if self.otel_span is None:
            return

        cluster_name = headers.get("X-Found-Handling-Cluster")
        if cluster_name is not None:
            self.otel_span.set_attribute("db.elasticsearch.cluster.name", cluster_name)
        node_name = headers.get("X-Found-Handling-Instance")
        if node_name is not None:
            self.otel_span.set_attribute("db.elasticsearch.node.name", node_name)

    def set_db_statement(self, serialized_body: bytes) -> None:
        if self.otel_span is None:
            return

        if self.body_strategy == "omit":
            return
        elif self.body_strategy == "raw" and self.endpoint_id in SEARCH_ENDPOINTS:
            self.otel_span.set_attribute(
                "db.statement", serialized_body.decode("utf-8")
            )
