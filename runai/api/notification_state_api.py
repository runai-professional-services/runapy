from typing import Optional, List
from datetime import datetime

from runai import models
from runai.api.runai_api_service import RunaiAPIService, deprecated_message


class NotificationStateApi(RunaiAPIService):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        self._api_client = api_client

    def get_notification_state(
        self,
    ):
        r"""


        ### Description
        Get notification state

        ### Parameters:
        ```python
        ```

        ### Example:
        ```python
        NotificationStateApi(

        )
        ```
        """

        resource_path = f"/api/v1/notification_state".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
        )

    def update_notification_state(
        self,
        notification_state: Optional[models.NotificationState] = None,
    ):
        r"""


        ### Description
        Update notification state

        ### Parameters:
        ```python
        notification_state: NotificationState
        ```
        notification_state: See model NotificationState for more information.

        ### Example:
        ```python
        NotificationStateApi(
            notification_state=runai.NotificationState()
        )
        ```
        """

        # Body params:
        body_params = notification_state

        resource_path = f"/api/v1/notification_state".replace("_", "-")
        method = "PATCH"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
            body=body_params,
        )
