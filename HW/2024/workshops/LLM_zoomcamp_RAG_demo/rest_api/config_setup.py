from copy import copy
from typing import (
    Type,
    Any,
    Dict,
    Tuple,
    List,
    Optional,
    Union,
    Callable,
    cast,
    NamedTuple,
)
import graphlib  # type: ignore[import,unused-ignore]
import string

import dlt
from dlt.common import logger
from dlt.common.configuration import resolve_configuration
from dlt.common.schema.utils import merge_columns
from dlt.common.utils import update_dict_nested
from dlt.common import jsonpath

from dlt.extract.incremental import Incremental
from dlt.extract.utils import ensure_table_schema_columns

from dlt.sources.helpers.requests import Response
from dlt.sources.helpers.rest_client.paginators import (
    BasePaginator,
    SinglePagePaginator,
    HeaderLinkPaginator,
    JSONResponsePaginator,
    JSONResponseCursorPaginator,
    OffsetPaginator,
    PageNumberPaginator,
)
from dlt.sources.helpers.rest_client.detector import single_entity_path
from dlt.sources.helpers.rest_client.exceptions import IgnoreResponseException
from dlt.sources.helpers.rest_client.auth import (
    AuthConfigBase,
    HttpBasicAuth,
    BearerTokenAuth,
    APIKeyAuth,
)

from .typing import (
    EndpointResourceBase,
    PaginatorType,
    AuthType,
    AuthConfig,
    IncrementalConfig,
    PaginatorConfig,
    ResolvedParam,
    ResponseAction,
    ResponseActionDict,
    Endpoint,
    EndpointResource,
)
from .utils import exclude_keys


PAGINATOR_MAP: Dict[PaginatorType, Type[BasePaginator]] = {
    "json_response": JSONResponsePaginator,
    "header_link": HeaderLinkPaginator,
    "auto": None,
    "single_page": SinglePagePaginator,
    "cursor": JSONResponseCursorPaginator,
    "offset": OffsetPaginator,
    "page_number": PageNumberPaginator,
}

AUTH_MAP: Dict[AuthType, Type[AuthConfigBase]] = {
    "bearer": BearerTokenAuth,
    "api_key": APIKeyAuth,
    "http_basic": HttpBasicAuth,
}


class IncrementalParam(NamedTuple):
    start: str
    end: Optional[str]


def get_paginator_class(paginator_type: PaginatorType) -> Type[BasePaginator]:
    try:
        return PAGINATOR_MAP[paginator_type]
    except KeyError:
        available_options = ", ".join(PAGINATOR_MAP.keys())
        raise ValueError(
            f"Invalid paginator: {paginator_type}. "
            f"Available options: {available_options}"
        )


def create_paginator(
    paginator_config: Optional[PaginatorConfig],
) -> Optional[BasePaginator]:
    if isinstance(paginator_config, BasePaginator):
        return paginator_config

    if isinstance(paginator_config, str):
        paginator_class = get_paginator_class(paginator_config)
        try:
            # `auto` has no associated class in `PAGINATOR_MAP`
            return paginator_class() if paginator_class else None
        except TypeError:
            raise ValueError(
                f"Paginator {paginator_config} requires arguments to create an instance. Use {paginator_class} instance instead."
            )

    if isinstance(paginator_config, dict):
        paginator_type = paginator_config.get("type", "auto")
        paginator_class = get_paginator_class(paginator_type)
        return (
            paginator_class(**exclude_keys(paginator_config, {"type"}))
            if paginator_class
            else None
        )

    return None


def get_auth_class(auth_type: AuthType) -> Type[AuthConfigBase]:
    try:
        return AUTH_MAP[auth_type]
    except KeyError:
        available_options = ", ".join(AUTH_MAP.keys())
        raise ValueError(
            f"Invalid authentication: {auth_type}. "
            f"Available options: {available_options}"
        )


def create_auth(auth_config: Optional[AuthConfig]) -> Optional[AuthConfigBase]:
    auth: AuthConfigBase = None
    if isinstance(auth_config, AuthConfigBase):
        auth = auth_config

    if isinstance(auth_config, str):
        auth_class = get_auth_class(auth_config)
        auth = auth_class()

    if isinstance(auth_config, dict):
        auth_type = auth_config.get("type", "bearer")
        auth_class = get_auth_class(auth_type)
        auth = auth_class(**exclude_keys(auth_config, {"type"}))

    if auth:
        # TODO: provide explicitly (non-default) values as explicit explicit_value=dict(auth)
        # this will resolve auth which is a configuration using current section context
        return resolve_configuration(auth)

    return None


def setup_incremental_object(
    request_params: Dict[str, Any],
    incremental_config: Optional[IncrementalConfig] = None,
) -> Tuple[
    Optional[Incremental[Any]], Optional[IncrementalParam], Optional[Callable[..., Any]]
]:
    incremental_params: List[str] = []
    for key, value in request_params.items():
        if isinstance(value, dict) and value.get("type") == "incremental":
            incremental_params.append(key)
    if len(incremental_params) > 1:
        raise ValueError(
            f"Only a single incremental parameter is allower per endpoint. Found: {incremental_params}"
        )
    transform: Optional[Callable[..., Any]]
    for key, value in request_params.items():
        if isinstance(value, dlt.sources.incremental):
            return value, IncrementalParam(start=key, end=None), None
        if isinstance(value, dict) and value.get("type") == "incremental":
            transform = value.get("transform", None)
            config = exclude_keys(value, {"type", "transform"})
            # TODO: implement param type to bind incremental to
            return (
                dlt.sources.incremental(**config),
                IncrementalParam(start=key, end=None),
                transform,
            )
    if incremental_config:
        transform = incremental_config.get("transform", None)
        config = exclude_keys(
            incremental_config, {"start_param", "end_param", "transform"}
        )
        return (
            dlt.sources.incremental(**config),
            IncrementalParam(
                start=incremental_config["start_param"],
                end=incremental_config.get("end_param"),
            ),
            transform,
        )

    return None, None, None


def make_parent_key_name(resource_name: str, field_name: str) -> str:
    return f"_{resource_name}_{field_name}"


def build_resource_dependency_graph(
    resource_defaults: EndpointResourceBase,
    resource_list: List[Union[str, EndpointResource]],
) -> Tuple[Any, Dict[str, EndpointResource], Dict[str, Optional[ResolvedParam]]]:
    dependency_graph = graphlib.TopologicalSorter()
    endpoint_resource_map: Dict[str, EndpointResource] = {}
    resolved_param_map: Dict[str, ResolvedParam] = {}

    # expand all resources and index them
    for resource_kwargs in resource_list:
        if isinstance(resource_kwargs, dict):
            # clone resource here, otherwise it needs to be cloned in several other places
            # note that this clones only dict structure, keeping all instances without deepcopy
            resource_kwargs = update_dict_nested({}, resource_kwargs)  # type: ignore

        endpoint_resource = _make_endpoint_resource(resource_kwargs, resource_defaults)
        assert isinstance(endpoint_resource["endpoint"], dict)
        _setup_single_entity_endpoint(endpoint_resource["endpoint"])
        _bind_path_params(endpoint_resource)

        resource_name = endpoint_resource["name"]
        assert isinstance(
            resource_name, str
        ), f"Resource name must be a string, got {type(resource_name)}"

        if resource_name in endpoint_resource_map:
            raise ValueError(f"Resource {resource_name} has already been defined")
        endpoint_resource_map[resource_name] = endpoint_resource

    # create dependency graph
    for resource_name, endpoint_resource in endpoint_resource_map.items():
        assert isinstance(endpoint_resource["endpoint"], dict)
        # connect transformers to resources via resolved params
        resolved_params = _find_resolved_params(endpoint_resource["endpoint"])
        if len(resolved_params) > 1:
            raise ValueError(
                f"Multiple resolved params for resource {resource_name}: {resolved_params}"
            )
        elif len(resolved_params) == 1:
            resolved_param = resolved_params[0]
            predecessor = resolved_param.resolve_config["resource"]
            if predecessor not in endpoint_resource_map:
                raise ValueError(
                    f"A transformer resource {resource_name} refers to non existing parent resource {predecessor} on {resolved_param}"
                )
            dependency_graph.add(resource_name, predecessor)
            resolved_param_map[resource_name] = resolved_param
        else:
            dependency_graph.add(resource_name)
            resolved_param_map[resource_name] = None

    return dependency_graph, endpoint_resource_map, resolved_param_map


def _make_endpoint_resource(
    resource: Union[str, EndpointResource], default_config: EndpointResourceBase
) -> EndpointResource:
    """
    Creates an EndpointResource object based on the provided resource
    definition and merges it with the default configuration.

    This function supports defining a resource in multiple formats:
    - As a string: The string is interpreted as both the resource name
        and its endpoint path.
    - As a dictionary: The dictionary must include `name` and `endpoint`
        keys. The `endpoint` can be a string representing the path,
        or a dictionary for more complex configurations. If the `endpoint`
        is missing the `path` key, the resource name is used as the `path`.
    """
    if isinstance(resource, str):
        resource = {"name": resource, "endpoint": {"path": resource}}
        return _merge_resource_endpoints(default_config, resource)

    if "endpoint" in resource:
        if isinstance(resource["endpoint"], str):
            resource["endpoint"] = {"path": resource["endpoint"]}
    else:
        # endpoint is optional
        resource["endpoint"] = {}

    if "path" not in resource["endpoint"]:
        resource["endpoint"]["path"] = resource["name"]  # type: ignore

    return _merge_resource_endpoints(default_config, resource)


def _bind_path_params(resource: EndpointResource) -> None:
    """Binds params declared in path to params available in `params`. Pops the
    bound params but. Params of type `resolve` and `incremental` are skipped
    and bound later.
    """
    path_params: Dict[str, Any] = {}
    assert isinstance(resource["endpoint"], dict)  # type guard
    resolve_params = [r.param_name for r in _find_resolved_params(resource["endpoint"])]
    path = resource["endpoint"]["path"]
    for format_ in string.Formatter().parse(path):
        name = format_[1]
        if name:
            params = resource["endpoint"].get("params", {})
            if name not in params and name not in path_params:
                raise ValueError(
                    f"The path {path} defined in resource {resource['name']} requires param with name {name} but it is not found in {params}"
                )
            if name in resolve_params:
                resolve_params.remove(name)
            if name in params:
                if not isinstance(params[name], dict):
                    # bind resolved param and pop it from endpoint
                    path_params[name] = params.pop(name)
                else:
                    param_type = params[name].get("type")
                    if param_type != "resolve":
                        raise ValueError(
                            f"The path {path} defined in resource {resource['name']} tries to bind param {name} with type {param_type}. Paths can only bind 'resource' type params."
                        )
                    # resolved params are bound later
                    path_params[name] = "{" + name + "}"

    if len(resolve_params) > 0:
        raise NotImplementedError(
            f"Resource {resource['name']} defines resolve params {resolve_params} that are not bound in path {path}. Resolve query params not supported yet."
        )

    resource["endpoint"]["path"] = path.format(**path_params)


def _setup_single_entity_endpoint(endpoint: Endpoint) -> Endpoint:
    """Tries to guess if the endpoint refers to a single entity and when detected:
    * if `data_selector` was not specified (or is None), "$" is selected
    * if `paginator` was not specified (or is None), SinglePagePaginator is selected

    Endpoint is modified in place and returned
    """
    # try to guess if list of entities or just single entity is returned
    if single_entity_path(endpoint["path"]):
        if endpoint.get("data_selector") is None:
            endpoint["data_selector"] = "$"
        if endpoint.get("paginator") is None:
            endpoint["paginator"] = SinglePagePaginator()
    return endpoint


def _find_resolved_params(endpoint_config: Endpoint) -> List[ResolvedParam]:
    """
    Find all resolved params in the endpoint configuration and return
    a list of ResolvedParam objects.

    Resolved params are of type ResolveParamConfig (bound param with a key "type" set to "resolve".)
    """
    return [
        ResolvedParam(key, value)  # type: ignore[arg-type]
        for key, value in endpoint_config.get("params", {}).items()
        if (isinstance(value, dict) and value.get("type") == "resolve")
    ]


def _action_type_unless_custom_hook(
    action_type: Optional[str], custom_hook: Optional[List[Callable[..., Any]]]
) -> Union[
    Tuple[str, Optional[List[Callable[..., Any]]]],
    Tuple[None, List[Callable[..., Any]]],
]:
    if custom_hook:
        return (None, custom_hook)
    return (action_type, None)


def _handle_response_action(response: Response, action: ResponseAction) -> Union[
    Tuple[str, Optional[List[Callable[..., Any]]]],
    Tuple[None, List[Callable[..., Any]]],
    Tuple[None, None],
]:
    """
    Checks, based on the response, if the provided action applies.
    """
    content: str = response.text
    status_code = None
    content_substr = None
    action_type = None
    custom_hooks = None
    response_action = None
    if callable(action):
        custom_hooks = [action]
    else:
        action = cast(ResponseActionDict, action)
        status_code = action.get("status_code")
        content_substr = action.get("content")
        response_action = action.get("action")
        if isinstance(response_action, str):
            action_type = response_action
        elif callable(response_action):
            custom_hooks = [response_action]
        elif isinstance(response_action, list) and all(
            callable(action) for action in response_action
        ):
            custom_hooks = response_action
        else:
            raise ValueError(
                f"Action {response_action} does not conform to expected type. Expected: str or Callable or List[Callable]. Found: {type(response_action)}"
            )

    if status_code is not None and content_substr is not None:
        if response.status_code == status_code and content_substr in content:
            return _action_type_unless_custom_hook(action_type, custom_hooks)

    elif status_code is not None:
        if response.status_code == status_code:
            return _action_type_unless_custom_hook(action_type, custom_hooks)

    elif content_substr is not None:
        if content_substr in content:
            return _action_type_unless_custom_hook(action_type, custom_hooks)

    elif status_code is None and content_substr is None and custom_hooks is not None:
        return (None, custom_hooks)

    return (None, None)


def _create_response_action_hook(
    response_action: ResponseAction,
) -> Callable[[Response, Any, Any], None]:
    def response_action_hook(response: Response, *args: Any, **kwargs: Any) -> None:
        """
        This is the hook executed by the requests library
        """
        (action_type, custom_hooks) = _handle_response_action(response, response_action)
        if custom_hooks:
            for hook in custom_hooks:
                hook(response)
        elif action_type == "ignore":
            logger.info(
                f"Ignoring response with code {response.status_code} "
                f"and content '{response.json()}'."
            )
            raise IgnoreResponseException

        # If there are hooks, then the REST client does not raise for status
        # If no action has been taken and the status code indicates an error,
        # raise an HTTP error based on the response status
        elif not action_type:
            response.raise_for_status()

    return response_action_hook


def create_response_hooks(
    response_actions: Optional[List[ResponseAction]],
) -> Optional[Dict[str, Any]]:
    """Create response hooks based on the provided response actions. Note
    that if the error status code is not handled by the response actions,
    the default behavior is to raise an HTTP error.

    Example:
        def set_encoding(response, *args, **kwargs):
            response.encoding = 'windows-1252'
            return response

        def remove_field(response: Response, *args, **kwargs) -> Response:
            payload = response.json()
            for record in payload:
                record.pop("email", None)
            modified_content: bytes = json.dumps(payload).encode("utf-8")
            response._content = modified_content
            return response

        response_actions = [
            set_encoding,
            {"status_code": 404, "action": "ignore"},
            {"content": "Not found", "action": "ignore"},
            {"status_code": 200, "content": "some text", "action": "ignore"},
            {"status_code": 200, "action": remove_field},
        ]
        hooks = create_response_hooks(response_actions)
    """
    if response_actions:
        hooks = [_create_response_action_hook(action) for action in response_actions]
        return {"response": hooks}
    return None


def process_parent_data_item(
    path: str,
    item: Dict[str, Any],
    resolved_param: ResolvedParam,
    include_from_parent: List[str],
) -> Tuple[str, Dict[str, Any]]:
    parent_resource_name = resolved_param.resolve_config["resource"]

    field_values = jsonpath.find_values(resolved_param.field_path, item)

    if not field_values:
        field_path = resolved_param.resolve_config["field"]
        raise ValueError(
            f"Transformer expects a field '{field_path}' to be present in the incoming data from resource {parent_resource_name} in order to bind it to path param {resolved_param.param_name}. Available parent fields are {', '.join(item.keys())}"
        )
    bound_path = path.format(**{resolved_param.param_name: field_values[0]})

    parent_record: Dict[str, Any] = {}
    if include_from_parent:
        for parent_key in include_from_parent:
            child_key = make_parent_key_name(parent_resource_name, parent_key)
            if parent_key not in item:
                raise ValueError(
                    f"Transformer expects a field '{parent_key}' to be present in the incoming data from resource {parent_resource_name} in order to include it in child records under {child_key}. Available parent fields are {', '.join(item.keys())}"
                )
            parent_record[child_key] = item[parent_key]

    return bound_path, parent_record


def _merge_resource_endpoints(
    default_config: EndpointResourceBase, config: EndpointResource
) -> EndpointResource:
    """Merges `default_config` and `config`, returns new instance of EndpointResource"""
    # NOTE: config is normalized and always has "endpoint" field which is a dict
    # TODO: could deep merge paginators and auths of the same type

    default_endpoint = default_config.get("endpoint", Endpoint())
    assert isinstance(default_endpoint, dict)
    config_endpoint = config["endpoint"]
    assert isinstance(config_endpoint, dict)

    merged_endpoint: Endpoint = {
        **default_endpoint,
        **{k: v for k, v in config_endpoint.items() if k not in ("json", "params")},  # type: ignore[typeddict-item]
    }
    # merge endpoint, only params and json are allowed to deep merge
    if "json" in config_endpoint:
        merged_endpoint["json"] = {
            **(merged_endpoint.get("json", {})),
            **config_endpoint["json"],
        }
    if "params" in config_endpoint:
        merged_endpoint["params"] = {
            **(merged_endpoint.get("json", {})),
            **config_endpoint["params"],
        }
    # merge columns
    if (default_columns := default_config.get("columns")) and (
        columns := config.get("columns")
    ):
        # merge only native dlt formats, skip pydantic and others
        if isinstance(columns, (list, dict)) and isinstance(
            default_columns, (list, dict)
        ):
            # normalize columns
            columns = ensure_table_schema_columns(columns)
            default_columns = ensure_table_schema_columns(default_columns)
            # merge columns with deep merging hints
            config["columns"] = merge_columns(
                copy(default_columns), columns, merge_columns=True
            )

    # no need to deep merge resources
    merged_resource: EndpointResource = {
        **default_config,
        **config,
        "endpoint": merged_endpoint,
    }
    return merged_resource
