from typing import Optional, List
from datetime import datetime

from runai import models
from runai.api.runai_api_service import RunaiAPIService, deprecated_message


class RolesApi(RunaiAPIService):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        self._api_client = api_client

    def get_role_v1(
        self,
        role_id_path: int,
    ):
        r"""


        ### Description
        Get a role by id.

        ### Parameters:
        ```python
        role_id_path: int
        ```
        role_id_path: The id of the role to retrieve

        ### Example:
        ```python
        RolesApi(
            role_id_path=32
        )
        ```
        """

        resource_path = f"/api/v1/authorization/roles/{role_id_path}".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
        )

    def get_roles_v1(
        self,
    ):
        r"""


        ### Description
        Get a list of roles.

        ### Parameters:
        ```python
        ```

        ### Example:
        ```python
        RolesApi(

        )
        ```
        """

        resource_path = f"/api/v1/authorization/roles".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
        )
