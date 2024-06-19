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

import logging
import uuid
from typing import Any, Callable, Dict, List, Optional

from elasticsearch import Elasticsearch
from elasticsearch._version import __versionstr__ as lib_version
from elasticsearch.helpers import BulkIndexError, bulk
from elasticsearch.helpers.vectorstore import EmbeddingService, RetrievalStrategy
from elasticsearch.helpers.vectorstore._utils import maximal_marginal_relevance

logger = logging.getLogger(__name__)


class VectorStore:
    """
    VectorStore is a higher-level abstraction of indexing and search.
    Users can pick from available retrieval strategies.

    Documents have up to 3 fields:
      - text_field: the text to be indexed and searched.
      - metadata: additional information about the document, either schema-free
        or defined by the supplied metadata_mappings.
      - vector_field (usually not filled by the user): the embedding vector of the text.

    Depending on the strategy, vector embeddings are
      - created by the user beforehand
      - created by this AsyncVectorStore class in Python
      - created in-stack by inference pipelines.
    """

    def __init__(
        self,
        client: Elasticsearch,
        *,
        index: str,
        retrieval_strategy: RetrievalStrategy,
        embedding_service: Optional[EmbeddingService] = None,
        num_dimensions: Optional[int] = None,
        text_field: str = "text_field",
        vector_field: str = "vector_field",
        metadata_mappings: Optional[Dict[str, Any]] = None,
        user_agent: str = f"elasticsearch-py-vs/{lib_version}",
    ) -> None:
        """
        :param user_header: user agent header specific to the 3rd party integration.
            Used for usage tracking in Elastic Cloud.
        :param index: The name of the index to query.
        :param retrieval_strategy: how to index and search the data. See the strategies
            module for availble strategies.
        :param text_field: Name of the field with the textual data.
        :param vector_field: For strategies that perform embedding inference in Python,
            the embedding vector goes in this field.
        :param client: Elasticsearch client connection. Alternatively specify the
            Elasticsearch connection with the other es_* parameters.
        """
        # Add integration-specific usage header for tracking usage in Elastic Cloud.
        # client.options preserves existing (non-user-agent) headers.
        client = client.options(headers={"User-Agent": user_agent})

        if hasattr(retrieval_strategy, "text_field"):
            retrieval_strategy.text_field = text_field
        if hasattr(retrieval_strategy, "vector_field"):
            retrieval_strategy.vector_field = vector_field

        self.client = client
        self.index = index
        self.retrieval_strategy = retrieval_strategy
        self.embedding_service = embedding_service
        self.num_dimensions = num_dimensions
        self.text_field = text_field
        self.vector_field = vector_field
        self.metadata_mappings = metadata_mappings

    def close(self) -> None:
        return self.client.close()

    def add_texts(
        self,
        texts: List[str],
        *,
        metadatas: Optional[List[Dict[str, Any]]] = None,
        vectors: Optional[List[List[float]]] = None,
        ids: Optional[List[str]] = None,
        refresh_indices: bool = True,
        create_index_if_not_exists: bool = True,
        bulk_kwargs: Optional[Dict[str, Any]] = None,
    ) -> List[str]:
        """Add documents to the Elasticsearch index.

        :param texts: List of text documents.
        :param metadata: Optional list of document metadata. Must be of same length as
            texts.
        :param vectors: Optional list of embedding vectors. Must be of same length as
            texts.
        :param ids: Optional list of ID strings. Must be of same length as texts.
        :param refresh_indices: Whether to refresh the index after deleting documents.
            Defaults to True.
        :param create_index_if_not_exists: Whether to create the index if it does not
            exist. Defaults to True.
        :param bulk_kwargs: Arguments to pass to the bulk function when indexing
            (for example chunk_size).

        :return: List of IDs of the created documents, either echoing the provided one
            or returning newly created ones.
        """
        bulk_kwargs = bulk_kwargs or {}
        ids = ids or [str(uuid.uuid4()) for _ in texts]
        requests = []

        if create_index_if_not_exists:
            self._create_index_if_not_exists()

        if self.embedding_service and not vectors:
            vectors = self.embedding_service.embed_documents(texts)

        for i, text in enumerate(texts):
            metadata = metadatas[i] if metadatas else {}

            request: Dict[str, Any] = {
                "_op_type": "index",
                "_index": self.index,
                self.text_field: text,
                "metadata": metadata,
                "_id": ids[i],
            }

            if vectors:
                request[self.vector_field] = vectors[i]

            requests.append(request)

        if len(requests) > 0:
            try:
                success, failed = bulk(
                    self.client,
                    requests,
                    stats_only=True,
                    refresh=refresh_indices,
                    **bulk_kwargs,
                )
                logger.debug(f"added texts {ids} to index")
                return ids
            except BulkIndexError as e:
                logger.error(f"Error adding texts: {e}")
                firstError = e.errors[0].get("index", {}).get("error", {})
                logger.error(f"First error reason: {firstError.get('reason')}")
                raise e

        else:
            logger.debug("No texts to add to index")
            return []

    def delete(  # type: ignore[no-untyped-def]
        self,
        *,
        ids: Optional[List[str]] = None,
        query: Optional[Dict[str, Any]] = None,
        refresh_indices: bool = True,
        **delete_kwargs,
    ) -> bool:
        """Delete documents from the Elasticsearch index.

        :param ids: List of IDs of documents to delete.
        :param refresh_indices: Whether to refresh the index after deleting documents.
            Defaults to True.

        :return: True if deletion was successful.
        """
        if ids is not None and query is not None:
            raise ValueError("one of ids or query must be specified")
        elif ids is None and query is None:
            raise ValueError("either specify ids or query")

        try:
            if ids:
                body = [
                    {"_op_type": "delete", "_index": self.index, "_id": _id}
                    for _id in ids
                ]
                bulk(
                    self.client,
                    body,
                    refresh=refresh_indices,
                    ignore_status=404,
                    **delete_kwargs,
                )
                logger.debug(f"Deleted {len(body)} texts from index")

            else:
                self.client.delete_by_query(
                    index=self.index,
                    query=query,
                    refresh=refresh_indices,
                    **delete_kwargs,
                )

        except BulkIndexError as e:
            logger.error(f"Error deleting texts: {e}")
            firstError = e.errors[0].get("index", {}).get("error", {})
            logger.error(f"First error reason: {firstError.get('reason')}")
            raise e

        return True

    def search(
        self,
        *,
        query: Optional[str],
        query_vector: Optional[List[float]] = None,
        k: int = 4,
        num_candidates: int = 50,
        fields: Optional[List[str]] = None,
        filter: Optional[List[Dict[str, Any]]] = None,
        custom_query: Optional[
            Callable[[Dict[str, Any], Optional[str]], Dict[str, Any]]
        ] = None,
    ) -> List[Dict[str, Any]]:
        """
        :param query: Input query string.
        :param query_vector: Input embedding vector. If given, input query string is
            ignored.
        :param k: Number of returned results.
        :param num_candidates: Number of candidates to fetch from data nodes in knn.
        :param fields: List of field names to return.
        :param filter: Elasticsearch filters to apply.
        :param custom_query: Function to modify the Elasticsearch query body before it is
            sent to Elasticsearch.

        :return: List of document hits. Includes _index, _id, _score and _source.
        """
        if fields is None:
            fields = []
        if "metadata" not in fields:
            fields.append("metadata")
        if self.text_field not in fields:
            fields.append(self.text_field)

        if self.embedding_service and not query_vector:
            if not query:
                raise ValueError("specify a query or a query_vector to search")
            query_vector = self.embedding_service.embed_query(query)

        query_body = self.retrieval_strategy.es_query(
            query=query,
            query_vector=query_vector,
            text_field=self.text_field,
            vector_field=self.vector_field,
            k=k,
            num_candidates=num_candidates,
            filter=filter or [],
        )

        if custom_query is not None:
            query_body = custom_query(query_body, query)
            logger.debug(f"Calling custom_query, Query body now: {query_body}")

        response = self.client.search(
            index=self.index,
            **query_body,
            size=k,
            source=True,
            source_includes=fields,
        )
        hits: List[Dict[str, Any]] = response["hits"]["hits"]

        return hits

    def _create_index_if_not_exists(self) -> None:
        exists = self.client.indices.exists(index=self.index)
        if exists.meta.status == 200:
            logger.debug(f"Index {self.index} already exists. Skipping creation.")
            return

        if self.retrieval_strategy.needs_inference():
            if not self.num_dimensions and not self.embedding_service:
                raise ValueError(
                    "retrieval strategy requires embeddings; either embedding_service "
                    "or num_dimensions need to be specified"
                )
            if not self.num_dimensions and self.embedding_service:
                vector = self.embedding_service.embed_query("get num dimensions")
                self.num_dimensions = len(vector)

        mappings, settings = self.retrieval_strategy.es_mappings_settings(
            text_field=self.text_field,
            vector_field=self.vector_field,
            num_dimensions=self.num_dimensions,
        )
        if self.metadata_mappings:
            metadata = mappings["properties"].get("metadata", {"properties": {}})
            for key in self.metadata_mappings.keys():
                if key in metadata:
                    raise ValueError(f"metadata key {key} already exists in mappings")

            metadata = dict(**metadata["properties"], **self.metadata_mappings)
            mappings["properties"]["metadata"] = {"properties": metadata}

        self.retrieval_strategy.before_index_creation(
            client=self.client,
            text_field=self.text_field,
            vector_field=self.vector_field,
        )
        self.client.indices.create(
            index=self.index, mappings=mappings, settings=settings
        )

    def max_marginal_relevance_search(
        self,
        *,
        embedding_service: EmbeddingService,
        query: str,
        vector_field: str,
        k: int = 4,
        num_candidates: int = 20,
        lambda_mult: float = 0.5,
        fields: Optional[List[str]] = None,
        custom_query: Optional[
            Callable[[Dict[str, Any], Optional[str]], Dict[str, Any]]
        ] = None,
    ) -> List[Dict[str, Any]]:
        """Return docs selected using the maximal marginal relevance.

        Maximal marginal relevance optimizes for similarity to query AND diversity
            among selected documents.

        :param query (str): Text to look up documents similar to.
        :param k (int): Number of Documents to return. Defaults to 4.
        :param fetch_k (int): Number of Documents to fetch to pass to MMR algorithm.
        :param lambda_mult (float): Number between 0 and 1 that determines the degree
            of diversity among the results with 0 corresponding
            to maximum diversity and 1 to minimum diversity.
            Defaults to 0.5.
        :param fields: Other fields to get from elasticsearch source. These fields
            will be added to the document metadata.

        :return: A list of Documents selected by maximal marginal relevance.
        """
        remove_vector_query_field_from_metadata = True
        if fields is None:
            fields = [vector_field]
        elif vector_field not in fields:
            fields.append(vector_field)
        else:
            remove_vector_query_field_from_metadata = False

        # Embed the query
        query_embedding = embedding_service.embed_query(query)

        # Fetch the initial documents
        got_hits = self.search(
            query=None,
            query_vector=query_embedding,
            k=num_candidates,
            fields=fields,
            custom_query=custom_query,
        )

        # Get the embeddings for the fetched documents
        got_embeddings = [hit["_source"][vector_field] for hit in got_hits]

        # Select documents using maximal marginal relevance
        selected_indices = maximal_marginal_relevance(
            query_embedding, got_embeddings, lambda_mult=lambda_mult, k=k
        )
        selected_hits = [got_hits[i] for i in selected_indices]

        if remove_vector_query_field_from_metadata:
            for hit in selected_hits:
                del hit["_source"][vector_field]

        return selected_hits
