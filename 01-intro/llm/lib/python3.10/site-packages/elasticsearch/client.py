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

import warnings

from ._sync.client import Elasticsearch as Elasticsearch  # noqa: F401
from ._sync.client.async_search import (  # noqa: F401
    AsyncSearchClient as AsyncSearchClient,
)
from ._sync.client.autoscaling import (  # noqa: F401
    AutoscalingClient as AutoscalingClient,
)
from ._sync.client.cat import CatClient as CatClient  # noqa: F401
from ._sync.client.ccr import CcrClient as CcrClient  # noqa: F401
from ._sync.client.cluster import ClusterClient as ClusterClient  # noqa: F401
from ._sync.client.dangling_indices import (  # noqa: F401
    DanglingIndicesClient as DanglingIndicesClient,
)
from ._sync.client.enrich import EnrichClient as EnrichClient  # noqa: F401
from ._sync.client.eql import EqlClient as EqlClient  # noqa: F401
from ._sync.client.esql import EsqlClient as EsqlClient  # noqa: F401
from ._sync.client.features import FeaturesClient as FeaturesClient  # noqa: F401
from ._sync.client.fleet import FleetClient as FleetClient  # noqa: F401
from ._sync.client.graph import GraphClient as GraphClient  # noqa: F401
from ._sync.client.ilm import IlmClient as IlmClient  # noqa: F401
from ._sync.client.indices import IndicesClient as IndicesClient  # noqa: F401
from ._sync.client.inference import InferenceClient as InferenceClient  # noqa: F401
from ._sync.client.ingest import IngestClient as IngestClient  # noqa: F401
from ._sync.client.license import LicenseClient as LicenseClient  # noqa: F401
from ._sync.client.logstash import LogstashClient as LogstashClient  # noqa: F401
from ._sync.client.migration import MigrationClient as MigrationClient  # noqa: F401
from ._sync.client.ml import MlClient as MlClient  # noqa: F401
from ._sync.client.monitoring import MonitoringClient as MonitoringClient  # noqa: F401
from ._sync.client.nodes import NodesClient as NodesClient  # noqa: F401
from ._sync.client.query_ruleset import (  # noqa: F401
    QueryRulesetClient as QueryRulesetClient,
)
from ._sync.client.rollup import RollupClient as RollupClient  # noqa: F401
from ._sync.client.search_application import (  # noqa: F401
    SearchApplicationClient as SearchApplicationClient,
)
from ._sync.client.searchable_snapshots import (  # noqa: F401
    SearchableSnapshotsClient as SearchableSnapshotsClient,
)
from ._sync.client.security import SecurityClient as SecurityClient  # noqa: F401
from ._sync.client.shutdown import ShutdownClient as ShutdownClient  # noqa: F401
from ._sync.client.slm import SlmClient as SlmClient  # noqa: F401
from ._sync.client.snapshot import SnapshotClient as SnapshotClient  # noqa: F401
from ._sync.client.sql import SqlClient as SqlClient  # noqa: F401
from ._sync.client.ssl import SslClient as SslClient  # noqa: F401
from ._sync.client.synonyms import SynonymsClient as SynonymsClient  # noqa: F401
from ._sync.client.tasks import TasksClient as TasksClient  # noqa: F401
from ._sync.client.text_structure import (  # noqa: F401
    TextStructureClient as TextStructureClient,
)
from ._sync.client.transform import TransformClient as TransformClient  # noqa: F401
from ._sync.client.watcher import WatcherClient as WatcherClient  # noqa: F401
from ._sync.client.xpack import XPackClient as XPackClient  # noqa: F401
from ._utils import fixup_module_metadata

# This file exists for backwards compatibility.
warnings.warn(
    "Importing from the 'elasticsearch.client' module is deprecated. "
    "Instead use 'elasticsearch' module for importing the client.",
    category=DeprecationWarning,
    stacklevel=2,
)

__all__ = [
    "AsyncSearchClient",
    "AutoscalingClient",
    "CatClient",
    "CcrClient",
    "ClusterClient",
    "DanglingIndicesClient",
    "Elasticsearch",
    "EnrichClient",
    "EqlClient",
    "FeaturesClient",
    "FleetClient",
    "GraphClient",
    "IlmClient",
    "IndicesClient",
    "IngestClient",
    "LicenseClient",
    "LogstashClient",
    "MigrationClient",
    "MlClient",
    "MonitoringClient",
    "NodesClient",
    "RollupClient",
    "SearchApplicationClient",
    "SearchableSnapshotsClient",
    "SecurityClient",
    "ShutdownClient",
    "SlmClient",
    "SnapshotClient",
    "SqlClient",
    "SslClient",
    "TasksClient",
    "TextStructureClient",
    "TransformClient",
    "WatcherClient",
    "XPackClient",
]

fixup_module_metadata(__name__, globals())
del fixup_module_metadata
