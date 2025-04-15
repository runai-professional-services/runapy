from typing import Optional, List
from datetime import datetime

from runai import models
from runai.api.runai_api_service import RunaiAPIService, deprecated_message


class MeApi(RunaiAPIService):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        self._api_client = api_client

    def count_me_access_rules(
        self,
        search: Optional[str] = None,
    ):
        r"""


        ### Description
        Count the access rules assigned to the requesting user.

        ### Parameters:
        ```python
        search: Optional[str]
        ```
        search: Filter results by a free text search.

        ### Example:
        ```python
        MeApi(
            search='test project'
        )
        ```
        """

        # Query params:
        query_params = [
            ("search", search),
        ]
        resource_path = f"/api/v1/authorization/me/access_rules/count".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path, method=method, query_params=query_params
        )

    def get_me_access_rules(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        search: Optional[str] = None,
    ):
        r"""


        ### Description
        List the access rules assigned to the requesting user.

        ### Parameters:
        ```python
        limit: Optional[int]
        offset: Optional[int]
        search: Optional[str]
        ```
        limit: The maximum number of entries to return. - Default: 50
        offset: The offset of the first item returned in the collection.
        search: Filter results by a free text search.

        ### Example:
        ```python
        MeApi(
            limit=50,
                        offset=100,
                        search='test project'
        )
        ```
        """

        # Query params:
        query_params = [
            ("limit", limit),
            ("offset", offset),
            ("search", search),
        ]
        resource_path = f"/api/v1/authorization/me/access_rules".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path, method=method, query_params=query_params
        )
