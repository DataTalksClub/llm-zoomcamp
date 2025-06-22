from typing import Any

import dlt
from rest_api import (
    RESTAPIConfig,
    check_connection,
    rest_api_source,
    rest_api_resources,
)


@dlt.source
def github_source(github_token: str = dlt.secrets.value) -> Any:
    # Create a REST API configuration for the GitHub API
    # Use RESTAPIConfig to get autocompletion and type checking
    config: RESTAPIConfig = {
        "client": {
            "base_url": "https://api.github.com/repos/dlt-hub/dlt/",
            "auth": {
                "type": "bearer",
                "token": github_token,
            },
        },
        # The default configuration for all resources and their endpoints
        "resource_defaults": {
            "primary_key": "id",
            "write_disposition": "merge",
            "endpoint": {
                "params": {
                    "per_page": 100,
                },
            },
        },
        "resources": [
            # This is a simple resource definition,
            # that uses the endpoint path as a resource name:
            # "pulls",
            # Alternatively, you can define the endpoint as a dictionary
            # {
            #     "name": "pulls", # <- Name of the resource
            #     "endpoint": "pulls",  # <- This is the endpoint path
            # }
            # Or use a more detailed configuration:
            {
                "name": "issues",
                "endpoint": {
                    "path": "issues",
                    # Query parameters for the endpoint
                    "params": {
                        "sort": "updated",
                        "direction": "desc",
                        "state": "open",
                        # Define `since` as a special parameter
                        # to incrementally load data from the API.
                        # This works by getting the updated_at value
                        # from the previous response data and using this value
                        # for the `since` query parameter in the next request.
                        "since": {
                            "type": "incremental",
                            "cursor_path": "updated_at",
                            "initial_value": "2024-01-25T11:21:28Z",
                        },
                    },
                },
            },
            # The following is an example of a resource that uses
            # a parent resource (`issues`) to get the `issue_number`
            # and include it in the endpoint path:
            {
                "name": "issue_comments",
                "endpoint": {
                    # The placeholder {issue_number} will be resolved
                    # from the parent resource
                    "path": "issues/{issue_number}/comments",
                    "params": {
                        # The value of `issue_number` will be taken
                        # from the `number` field in the `issues` resource
                        "issue_number": {
                            "type": "resolve",
                            "resource": "issues",
                            "field": "number",
                        }
                    },
                },
                # Include data from `id` field of the parent resource
                # in the child data. The field name in the child data
                # will be called `_issues_id` (_{resource_name}_{field_name})
                "include_from_parent": ["id"],
            },
        ],
    }

    yield from rest_api_resources(config)


def load_github() -> None:
    pipeline = dlt.pipeline(
        pipeline_name="rest_api_github",
        destination='lancedb',
        dataset_name="rest_api_data",
    )

    load_info = pipeline.run(github_source())
    print(load_info)


def load_pokemon() -> None:
    pipeline = dlt.pipeline(
        pipeline_name="rest_api_pokemon",
        destination='lancedb',
        dataset_name="rest_api_data",
    )

    pokemon_source = rest_api_source(
        {
            "client": {
                "base_url": "https://pokeapi.co/api/v2/",
                # If you leave out the paginator, it will be inferred from the API:
                # paginator: "json_response",
            },
            "resource_defaults": {
                "endpoint": {
                    "params": {
                        "limit": 1000,
                    },
                },
            },
            "resources": [
                "pokemon",
                "berry",
                "location",
            ],
        }
    )

    def check_network_and_authentication() -> None:
        (can_connect, error_msg) = check_connection(
            pokemon_source,
            "not_existing_endpoint",
        )
        if not can_connect:
            pass  # do something with the error message

    check_network_and_authentication()

    load_info = pipeline.run(pokemon_source)
    print(load_info)


if __name__ == "__main__":
    load_github()
    load_pokemon()
