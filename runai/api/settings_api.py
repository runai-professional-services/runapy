from typing import Optional, List
from datetime import datetime

from runai import models
from runai.api.runai_api_service import RunaiAPIService, deprecated_message


class SettingsApi(RunaiAPIService):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        self._api_client = api_client

    def get_idm_setting_by_key(
        self,
        key: models.SettingsKeyEnum,
    ):
        r"""


        ### Description
        Get idm setting by key

        ### Parameters:
        ```python
        key: models.SettingsKeyEnum
        ```
        key: The settings key

        ### Example:
        ```python
        SettingsApi(
            key=runai.SettingsKeyEnum()
        )
        ```
        """

        resource_path = f"/api/v1/security/settings/{key}".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
        )

    def get_idm_settings(
        self,
    ):
        r"""


        ### Description
        Get idm settings

        ### Parameters:
        ```python
        ```

        ### Example:
        ```python
        SettingsApi(

        )
        ```
        """

        resource_path = f"/api/v1/security/settings".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
        )

    def update_idm_setting_by_key(
        self,
        key: models.SettingsKeyEnum,
        update_idm_setting_by_key_request: models.UpdateIdmSettingByKeyRequest,
    ):
        r"""


        ### Description
        Update idm setting by key

        ### Parameters:
        ```python
        key: models.SettingsKeyEnum
        update_idm_setting_by_key_request: UpdateIdmSettingByKeyRequest
        ```
        key: The settings key
        update_idm_setting_by_key_request: See model UpdateIdmSettingByKeyRequest for more information.

        ### Example:
        ```python
        SettingsApi(
            key=runai.SettingsKeyEnum(),
                        update_idm_setting_by_key_request={"enabled":false,"idpAlias":"oidc"}
        )
        ```
        """

        # Body params:
        body_params = update_idm_setting_by_key_request

        resource_path = f"/api/v1/security/settings/{key}".replace("_", "-")
        method = "PUT"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
            body=body_params,
        )
