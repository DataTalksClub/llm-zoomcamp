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

import asyncio
import logging
from typing import (
    Any,
    AsyncIterable,
    AsyncIterator,
    Callable,
    Collection,
    Dict,
    Iterable,
    List,
    MutableMapping,
    Optional,
    Tuple,
    TypeVar,
    Union,
)

from ..exceptions import ApiError, NotFoundError, TransportError
from ..helpers.actions import (
    _TYPE_BULK_ACTION,
    _TYPE_BULK_ACTION_BODY,
    _TYPE_BULK_ACTION_HEADER,
    _TYPE_BULK_ACTION_HEADER_AND_BODY,
    _ActionChunker,
    _process_bulk_chunk_error,
    _process_bulk_chunk_success,
    expand_action,
)
from ..helpers.errors import ScanError
from ..serializer import Serializer
from .client import AsyncElasticsearch  # noqa

logger = logging.getLogger("elasticsearch.helpers")

T = TypeVar("T")


async def _chunk_actions(
    actions: AsyncIterable[_TYPE_BULK_ACTION_HEADER_AND_BODY],
    chunk_size: int,
    max_chunk_bytes: int,
    serializer: Serializer,
) -> AsyncIterable[
    Tuple[
        List[
            Union[
                Tuple[_TYPE_BULK_ACTION_HEADER],
                Tuple[_TYPE_BULK_ACTION_HEADER, _TYPE_BULK_ACTION_BODY],
            ]
        ],
        List[bytes],
    ]
]:
    """
    Split actions into chunks by number or size, serialize them into strings in
    the process.
    """
    chunker = _ActionChunker(
        chunk_size=chunk_size, max_chunk_bytes=max_chunk_bytes, serializer=serializer
    )
    async for action, data in actions:
        ret = chunker.feed(action, data)
        if ret:
            yield ret
    ret = chunker.flush()
    if ret:
        yield ret


async def _process_bulk_chunk(
    client: AsyncElasticsearch,
    bulk_actions: List[bytes],
    bulk_data: List[
        Union[
            Tuple[_TYPE_BULK_ACTION_HEADER],
            Tuple[_TYPE_BULK_ACTION_HEADER, _TYPE_BULK_ACTION_BODY],
        ]
    ],
    raise_on_exception: bool = True,
    raise_on_error: bool = True,
    ignore_status: Union[int, Collection[int]] = (),
    *args: Any,
    **kwargs: Any,
) -> AsyncIterable[Tuple[bool, Dict[str, Any]]]:
    """
    Send a bulk request to elasticsearch and process the output.
    """
    if isinstance(ignore_status, int):
        ignore_status = (ignore_status,)

    try:
        # send the actual request
        resp = await client.bulk(*args, operations=bulk_actions, **kwargs)  # type: ignore[arg-type]
    except ApiError as e:
        gen = _process_bulk_chunk_error(
            error=e,
            bulk_data=bulk_data,
            ignore_status=ignore_status,
            raise_on_exception=raise_on_exception,
            raise_on_error=raise_on_error,
        )
    else:
        gen = _process_bulk_chunk_success(
            resp=resp.body,
            bulk_data=bulk_data,
            ignore_status=ignore_status,
            raise_on_error=raise_on_error,
        )
    for item in gen:
        yield item


def aiter(x: Union[Iterable[T], AsyncIterable[T]]) -> AsyncIterator[T]:
    """Turns an async iterable or iterable into an async iterator"""
    if hasattr(x, "__anext__"):
        return x  # type: ignore[return-value]
    elif hasattr(x, "__aiter__"):
        return x.__aiter__()

    async def f() -> AsyncIterable[T]:
        nonlocal x
        ix: Iterable[T] = x
        for item in ix:
            yield item

    return f().__aiter__()


async def azip(
    *iterables: Union[Iterable[T], AsyncIterable[T]]
) -> AsyncIterable[Tuple[T, ...]]:
    """Zips async iterables and iterables into an async iterator
    with the same behavior as zip()
    """
    aiters = [aiter(x) for x in iterables]
    try:
        while True:
            yield tuple([await x.__anext__() for x in aiters])
    except StopAsyncIteration:
        pass


async def async_streaming_bulk(
    client: AsyncElasticsearch,
    actions: Union[Iterable[_TYPE_BULK_ACTION], AsyncIterable[_TYPE_BULK_ACTION]],
    chunk_size: int = 500,
    max_chunk_bytes: int = 100 * 1024 * 1024,
    raise_on_error: bool = True,
    expand_action_callback: Callable[
        [_TYPE_BULK_ACTION], _TYPE_BULK_ACTION_HEADER_AND_BODY
    ] = expand_action,
    raise_on_exception: bool = True,
    max_retries: int = 0,
    initial_backoff: float = 2,
    max_backoff: float = 600,
    yield_ok: bool = True,
    ignore_status: Union[int, Collection[int]] = (),
    *args: Any,
    **kwargs: Any,
) -> AsyncIterable[Tuple[bool, Dict[str, Any]]]:
    """
    Streaming bulk consumes actions from the iterable passed in and yields
    results per action. For non-streaming usecases use
    :func:`~elasticsearch.helpers.async_bulk` which is a wrapper around streaming
    bulk that returns summary information about the bulk operation once the
    entire input is consumed and sent.

    If you specify ``max_retries`` it will also retry any documents that were
    rejected with a ``429`` status code. To do this it will wait (**by calling
    asyncio.sleep**) for ``initial_backoff`` seconds and then,
    every subsequent rejection for the same chunk, for double the time every
    time up to ``max_backoff`` seconds.

    :arg client: instance of :class:`~elasticsearch.AsyncElasticsearch` to use
    :arg actions: iterable or async iterable containing the actions to be executed
    :arg chunk_size: number of docs in one chunk sent to es (default: 500)
    :arg max_chunk_bytes: the maximum size of the request in bytes (default: 100MB)
    :arg raise_on_error: raise ``BulkIndexError`` containing errors (as `.errors`)
        from the execution of the last chunk when some occur. By default we raise.
    :arg raise_on_exception: if ``False`` then don't propagate exceptions from
        call to ``bulk`` and just report the items that failed as failed.
    :arg expand_action_callback: callback executed on each action passed in,
        should return a tuple containing the action line and the data line
        (`None` if data line should be omitted).
    :arg max_retries: maximum number of times a document will be retried when
        ``429`` is received, set to 0 (default) for no retries on ``429``
    :arg initial_backoff: number of seconds we should wait before the first
        retry. Any subsequent retries will be powers of ``initial_backoff *
        2**retry_number``
    :arg max_backoff: maximum number of seconds a retry will wait
    :arg yield_ok: if set to False will skip successful documents in the output
    :arg ignore_status: list of HTTP status code that you want to ignore
    """

    client = client.options()
    client._client_meta = (("h", "bp"),)

    async def map_actions() -> AsyncIterable[_TYPE_BULK_ACTION_HEADER_AND_BODY]:
        async for item in aiter(actions):
            yield expand_action_callback(item)

    serializer = client.transport.serializers.get_serializer("application/json")

    bulk_data: List[
        Union[
            Tuple[_TYPE_BULK_ACTION_HEADER],
            Tuple[_TYPE_BULK_ACTION_HEADER, _TYPE_BULK_ACTION_BODY],
        ]
    ]
    bulk_actions: List[bytes]
    async for bulk_data, bulk_actions in _chunk_actions(
        map_actions(), chunk_size, max_chunk_bytes, serializer
    ):
        for attempt in range(max_retries + 1):
            to_retry: List[bytes] = []
            to_retry_data: List[
                Union[
                    Tuple[_TYPE_BULK_ACTION_HEADER],
                    Tuple[_TYPE_BULK_ACTION_HEADER, _TYPE_BULK_ACTION_BODY],
                ]
            ] = []
            if attempt:
                await asyncio.sleep(
                    min(max_backoff, initial_backoff * 2 ** (attempt - 1))
                )

            try:
                data: Union[
                    Tuple[_TYPE_BULK_ACTION_HEADER],
                    Tuple[_TYPE_BULK_ACTION_HEADER, _TYPE_BULK_ACTION_BODY],
                ]
                ok: bool
                info: Dict[str, Any]
                async for data, (ok, info) in azip(  # type: ignore
                    bulk_data,
                    _process_bulk_chunk(
                        client,
                        bulk_actions,
                        bulk_data,
                        raise_on_exception,
                        raise_on_error,
                        ignore_status,
                        *args,
                        **kwargs,
                    ),
                ):
                    if not ok:
                        action, info = info.popitem()
                        # retry if retries enabled, we get 429, and we are not
                        # in the last attempt
                        if (
                            max_retries
                            and info["status"] == 429
                            and (attempt + 1) <= max_retries
                        ):
                            # _process_bulk_chunk expects strings so we need to
                            # re-serialize the data
                            to_retry.extend(map(serializer.dumps, data))
                            to_retry_data.append(data)
                        else:
                            yield ok, {action: info}
                    elif yield_ok:
                        yield ok, info

            except ApiError as e:
                # suppress 429 errors since we will retry them
                if attempt == max_retries or e.status_code != 429:
                    raise
            else:
                if not to_retry:
                    break
                # retry only subset of documents that didn't succeed
                bulk_actions, bulk_data = to_retry, to_retry_data


async def async_bulk(
    client: AsyncElasticsearch,
    actions: Union[Iterable[_TYPE_BULK_ACTION], AsyncIterable[_TYPE_BULK_ACTION]],
    stats_only: bool = False,
    ignore_status: Union[int, Collection[int]] = (),
    *args: Any,
    **kwargs: Any,
) -> Tuple[int, Union[int, List[Any]]]:
    """
    Helper for the :meth:`~elasticsearch.AsyncElasticsearch.bulk` api that provides
    a more human friendly interface - it consumes an iterator of actions and
    sends them to elasticsearch in chunks. It returns a tuple with summary
    information - number of successfully executed actions and either list of
    errors or number of errors if ``stats_only`` is set to ``True``. Note that
    by default we raise a ``BulkIndexError`` when we encounter an error so
    options like ``stats_only`` only+ apply when ``raise_on_error`` is set to
    ``False``.

    When errors are being collected original document data is included in the
    error dictionary which can lead to an extra high memory usage. If you need
    to process a lot of data and want to ignore/collect errors please consider
    using the :func:`~elasticsearch.helpers.async_streaming_bulk` helper which will
    just return the errors and not store them in memory.


    :arg client: instance of :class:`~elasticsearch.AsyncElasticsearch` to use
    :arg actions: iterator containing the actions
    :arg stats_only: if `True` only report number of successful/failed
        operations instead of just number of successful and a list of error responses
    :arg ignore_status: list of HTTP status code that you want to ignore

    Any additional keyword arguments will be passed to
    :func:`~elasticsearch.helpers.async_streaming_bulk` which is used to execute
    the operation, see :func:`~elasticsearch.helpers.async_streaming_bulk` for more
    accepted parameters.
    """
    success, failed = 0, 0

    # list of errors to be collected is not stats_only
    errors = []

    # make streaming_bulk yield successful results so we can count them
    kwargs["yield_ok"] = True
    async for ok, item in async_streaming_bulk(
        client, actions, ignore_status=ignore_status, *args, **kwargs  # type: ignore[misc]
    ):
        # go through request-response pairs and detect failures
        if not ok:
            if not stats_only:
                errors.append(item)
            failed += 1
        else:
            success += 1

    return success, failed if stats_only else errors


async def async_scan(
    client: AsyncElasticsearch,
    query: Optional[Any] = None,
    scroll: str = "5m",
    raise_on_error: bool = True,
    preserve_order: bool = False,
    size: int = 1000,
    request_timeout: Optional[float] = None,
    clear_scroll: bool = True,
    scroll_kwargs: Optional[MutableMapping[str, Any]] = None,
    **kwargs: Any,
) -> AsyncIterable[Dict[str, Any]]:
    """
    Simple abstraction on top of the
    :meth:`~elasticsearch.AsyncElasticsearch.scroll` api - a simple iterator that
    yields all hits as returned by underlining scroll requests.

    By default scan does not return results in any pre-determined order. To
    have a standard order in the returned documents (either by score or
    explicit sort definition) when scrolling, use ``preserve_order=True``. This
    may be an expensive operation and will negate the performance benefits of
    using ``scan``.

    :arg client: instance of :class:`~elasticsearch.AsyncElasticsearch` to use
    :arg query: body for the :meth:`~elasticsearch.AsyncElasticsearch.search` api
    :arg scroll: Specify how long a consistent view of the index should be
        maintained for scrolled search
    :arg raise_on_error: raises an exception (``ScanError``) if an error is
        encountered (some shards fail to execute). By default we raise.
    :arg preserve_order: don't set the ``search_type`` to ``scan`` - this will
        cause the scroll to paginate with preserving the order. Note that this
        can be an extremely expensive operation and can easily lead to
        unpredictable results, use with caution.
    :arg size: size (per shard) of the batch send at each iteration.
    :arg request_timeout: explicit timeout for each call to ``scan``
    :arg clear_scroll: explicitly calls delete on the scroll id via the clear
        scroll API at the end of the method on completion or error, defaults
        to true.
    :arg scroll_kwargs: additional kwargs to be passed to
        :meth:`~elasticsearch.AsyncElasticsearch.scroll`

    Any additional keyword arguments will be passed to the initial
    :meth:`~elasticsearch.AsyncElasticsearch.search` call:

    .. code-block:: python

        async_scan(
            client,
            query={"query": {"match": {"title": "python"}}},
            index="orders-*"
        )
    """
    scroll_kwargs = scroll_kwargs or {}

    if not preserve_order:
        query = query.copy() if query else {}
        query["sort"] = "_doc"

    def pop_transport_kwargs(kw: MutableMapping[str, Any]) -> MutableMapping[str, Any]:
        # Grab options that should be propagated to every
        # API call within this helper instead of just 'search()'
        transport_kwargs = {}
        for key in ("headers", "api_key", "http_auth", "basic_auth", "bearer_auth"):
            try:
                value = kw.pop(key)
                if key == "http_auth":
                    key = "basic_auth"
                transport_kwargs[key] = value
            except KeyError:
                pass
        return transport_kwargs

    client = client.options(
        request_timeout=request_timeout, **pop_transport_kwargs(kwargs)
    )
    client._client_meta = (("h", "s"),)

    # Setting query={"from": ...} would make 'from' be used
    # as a keyword argument instead of 'from_'. We handle that here.
    def normalize_from_keyword(kw: MutableMapping[str, Any]) -> None:
        if "from" in kw:
            kw["from_"] = kw.pop("from")

    normalize_from_keyword(kwargs)
    try:
        search_kwargs = query.copy() if query else {}
        normalize_from_keyword(search_kwargs)
        search_kwargs.update(kwargs)
        search_kwargs["scroll"] = scroll
        search_kwargs["size"] = size
        resp = await client.search(**search_kwargs)

    # Try the old deprecated way if we fail immediately on parameters.
    except TypeError:
        search_kwargs = kwargs.copy()
        search_kwargs["scroll"] = scroll
        search_kwargs["size"] = size
        resp = await client.search(body=query, **search_kwargs)

    scroll_id: Optional[str] = resp.get("_scroll_id")
    scroll_transport_kwargs = pop_transport_kwargs(scroll_kwargs)
    if scroll_transport_kwargs:
        scroll_client = client.options(**scroll_transport_kwargs)
    else:
        scroll_client = client

    try:
        while scroll_id and resp["hits"]["hits"]:
            for hit in resp["hits"]["hits"]:
                yield hit

            # Default to 0 if the value isn't included in the response
            shards_info: Dict[str, int] = resp["_shards"]
            shards_successful = shards_info.get("successful", 0)
            shards_skipped = shards_info.get("skipped", 0)
            shards_total = shards_info.get("total", 0)

            # check if we have any errors
            if (shards_successful + shards_skipped) < shards_total:
                shards_message = "Scroll request has only succeeded on %d (+%d skipped) shards out of %d."
                logger.warning(
                    shards_message,
                    shards_successful,
                    shards_skipped,
                    shards_total,
                )
                if raise_on_error:
                    raise ScanError(
                        scroll_id,
                        shards_message
                        % (
                            shards_successful,
                            shards_skipped,
                            shards_total,
                        ),
                    )
            resp = await scroll_client.scroll(
                scroll_id=scroll_id, scroll=scroll, **scroll_kwargs
            )
            scroll_id = resp.get("_scroll_id")

    finally:
        if scroll_id and clear_scroll:
            await client.options(ignore_status=404).clear_scroll(scroll_id=scroll_id)


async def async_reindex(
    client: AsyncElasticsearch,
    source_index: Union[str, Collection[str]],
    target_index: str,
    query: Any = None,
    target_client: Optional[AsyncElasticsearch] = None,
    chunk_size: int = 500,
    scroll: str = "5m",
    op_type: Optional[str] = None,
    scan_kwargs: MutableMapping[str, Any] = {},
    bulk_kwargs: MutableMapping[str, Any] = {},
) -> Tuple[int, Union[int, List[Any]]]:
    """
    Reindex all documents from one index that satisfy a given query
    to another, potentially (if `target_client` is specified) on a different cluster.
    If you don't specify the query you will reindex all the documents.

    Since ``2.3`` a :meth:`~elasticsearch.AsyncElasticsearch.reindex` api is
    available as part of elasticsearch itself. It is recommended to use the api
    instead of this helper wherever possible. The helper is here mostly for
    backwards compatibility and for situations where more flexibility is
    needed.

    .. note::

        This helper doesn't transfer mappings, just the data.

    :arg client: instance of :class:`~elasticsearch.AsyncElasticsearch` to use (for
        read if `target_client` is specified as well)
    :arg source_index: index (or list of indices) to read documents from
    :arg target_index: name of the index in the target cluster to populate
    :arg query: body for the :meth:`~elasticsearch.AsyncElasticsearch.search` api
    :arg target_client: optional, is specified will be used for writing (thus
        enabling reindex between clusters)
    :arg chunk_size: number of docs in one chunk sent to es (default: 500)
    :arg scroll: Specify how long a consistent view of the index should be
        maintained for scrolled search
    :arg op_type: Explicit operation type. Defaults to '_index'. Data streams must
        be set to 'create'. If not specified, will auto-detect if target_index is a
        data stream.
    :arg scan_kwargs: additional kwargs to be passed to
        :func:`~elasticsearch.helpers.async_scan`
    :arg bulk_kwargs: additional kwargs to be passed to
        :func:`~elasticsearch.helpers.async_bulk`
    """
    target_client = client if target_client is None else target_client
    docs = async_scan(
        client, query=query, index=source_index, scroll=scroll, **scan_kwargs
    )

    async def _change_doc_index(
        hits: AsyncIterable[Dict[str, Any]],
        index: str,
        op_type: Optional[str],
    ) -> AsyncIterable[Dict[str, Any]]:
        async for h in hits:
            h["_index"] = index
            if op_type is not None:
                h["_op_type"] = op_type
            if "fields" in h:
                h.update(h.pop("fields"))
            yield h

    kwargs = {"stats_only": True}
    kwargs.update(bulk_kwargs)

    is_data_stream = False
    try:
        # Verify if the target_index is data stream or index
        data_streams = await target_client.indices.get_data_stream(
            name=target_index, expand_wildcards="all"
        )
        is_data_stream = any(
            data_stream["name"] == target_index
            for data_stream in data_streams["data_streams"]
        )
    except (TransportError, KeyError, NotFoundError):
        # If its not data stream, might be index
        pass

    if is_data_stream:
        if op_type not in (None, "create"):
            raise ValueError("Data streams must have 'op_type' set to 'create'")
        else:
            op_type = "create"

    return await async_bulk(
        target_client,
        _change_doc_index(docs, target_index, op_type),
        chunk_size=chunk_size,
        **kwargs,
    )
