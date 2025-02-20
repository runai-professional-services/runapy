from typing import Optional, List
from datetime import datetime

from runai import models
from runai.api.runai_api_service import RunaiAPIService, deprecated_message


class TenantApi(RunaiAPIService):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        self._api_client = api_client

    def get_tenant_settings(
        self,
    ):
        r"""


        ### Description
        Get all tenant settings.

        ### Parameters:
        ```python
        ```

        ### Example:
        ```python
        TenantApi(

        )
        ```
        """

        resource_path = f"/v1/k8s/setting".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
        )

    def get_tenant_settings_by_key(
        self,
        setting_key: str,
    ):
        r"""


        ### Description
        Get a tenant setting by key.

        ### Parameters:
        ```python
        setting_key: str
        ```
        setting_key: See model str for more information.

        ### Example:
        ```python
        TenantApi(
            setting_key='setting_key_example'
        )
        ```
        """

        resource_path = f"/v1/k8s/setting/{setting_key}".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
        )

    def update_tenant_setting(
        self,
        tenant_setting_creation_request: Optional[
            models.TenantSettingCreationRequest
        ] = None,
    ):
        r"""


        ### Description
        Update a tenant setting.

        ### Parameters:
        ```python
        tenant_setting_creation_request: TenantSettingCreationRequest
        ```
        tenant_setting_creation_request: See model TenantSettingCreationRequest for more information.

        ### Example:
        ```python
        TenantApi(
            tenant_setting_creation_request=runai.TenantSettingCreationRequest()
        )
        ```
        """

        # Body params:
        body_params = tenant_setting_creation_request

        resource_path = f"/v1/k8s/setting".replace("_", "-")
        method = "PUT"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
            body=body_params,
        )
