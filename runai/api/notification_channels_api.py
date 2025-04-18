from typing import Optional, List
from datetime import datetime

from runai import models
from runai.api.runai_api_service import RunaiAPIService, deprecated_message


class NotificationChannelsApi(RunaiAPIService):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        self._api_client = api_client

    def create_notification_channel_config(
        self,
        notification_channel: Optional[models.NotificationChannel] = None,
    ):
        r"""


        ### Description
        Create configuration of notification channel

        ### Parameters:
        ```python
        notification_channel: NotificationChannel
        ```
        notification_channel: See model NotificationChannel for more information.

        ### Example:
        ```python
        NotificationChannelsApi(
            notification_channel=runai.NotificationChannel()
        )
        ```
        """

        # Body params:
        body_params = notification_channel

        resource_path = f"/api/v1/notification_channels".replace("_", "-")
        method = "POST"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
            body=body_params,
        )

    def create_slack_app(
        self,
        create_slack_app_request_body: Optional[
            models.CreateSlackAppRequestBody
        ] = None,
    ):
        r"""


        ### Description
        Create Slack app

        ### Parameters:
        ```python
        create_slack_app_request_body: CreateSlackAppRequestBody
        ```
        create_slack_app_request_body: See model CreateSlackAppRequestBody for more information.

        ### Example:
        ```python
        NotificationChannelsApi(
            create_slack_app_request_body=runai.CreateSlackAppRequestBody()
        )
        ```
        """

        # Body params:
        body_params = create_slack_app_request_body

        resource_path = f"/api/v1/notification_channels/slack/create_app".replace(
            "_", "-"
        )
        method = "POST"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
            body=body_params,
        )

    def delete_notification_channel_config(
        self,
        name: str,
    ):
        r"""


        ### Description
        Delete configuration of Notification Channel

        ### Parameters:
        ```python
        name: str
        ```
        name: Notification Channel name

        ### Example:
        ```python
        NotificationChannelsApi(
            name='name_example'
        )
        ```
        """

        resource_path = f"/api/v1/notification_channels/{name}".replace("_", "-")
        method = "DELETE"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
        )

    def get_notification_channel_config(
        self,
        name: str,
    ):
        r"""


        ### Description
        Get configuration of notification channel

        ### Parameters:
        ```python
        name: str
        ```
        name: Notification Channel name

        ### Example:
        ```python
        NotificationChannelsApi(
            name='name_example'
        )
        ```
        """

        resource_path = f"/api/v1/notification_channels/{name}".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
        )

    def get_notification_channels(
        self,
    ):
        r"""


        ### Description
        Get supported Notification Channels

        ### Parameters:
        ```python
        ```

        ### Example:
        ```python
        NotificationChannelsApi(

        )
        ```
        """

        resource_path = f"/api/v1/notification_channels".replace("_", "-")
        method = "GET"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
        )

    def patch_notification_channel_config(
        self,
        name: str,
        notification_channel_for_patch: Optional[
            models.NotificationChannelForPatch
        ] = None,
    ):
        r"""


        ### Description
        Patch configuration of Notification Channel

        ### Parameters:
        ```python
        name: str
        notification_channel_for_patch: NotificationChannelForPatch
        ```
        name: Notification Channel name
        notification_channel_for_patch: See model NotificationChannelForPatch for more information.

        ### Example:
        ```python
        NotificationChannelsApi(
            name='name_example',
                        notification_channel_for_patch=runai.NotificationChannelForPatch()
        )
        ```
        """

        # Body params:
        body_params = notification_channel_for_patch

        resource_path = f"/api/v1/notification_channels/{name}".replace("_", "-")
        method = "PATCH"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
            body=body_params,
        )

    def update_notification_channel_config(
        self,
        name: str,
        notification_channel: Optional[models.NotificationChannel] = None,
    ):
        r"""


        ### Description
        Update configuration of Notification Channel

        ### Parameters:
        ```python
        name: str
        notification_channel: NotificationChannel
        ```
        name: Notification Channel name
        notification_channel: See model NotificationChannel for more information.

        ### Example:
        ```python
        NotificationChannelsApi(
            name='name_example',
                        notification_channel=runai.NotificationChannel()
        )
        ```
        """

        # Body params:
        body_params = notification_channel

        resource_path = f"/api/v1/notification_channels/{name}".replace("_", "-")
        method = "PUT"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
            body=body_params,
        )

    def validate_notification_channel(
        self,
        notification_channel_for_validate: Optional[
            models.NotificationChannelForValidate
        ] = None,
    ):
        r"""


        ### Description
        Validate configuration of Notification Channel

        ### Parameters:
        ```python
        notification_channel_for_validate: NotificationChannelForValidate
        ```
        notification_channel_for_validate: See model NotificationChannelForValidate for more information.

        ### Example:
        ```python
        NotificationChannelsApi(
            notification_channel_for_validate=runai.NotificationChannelForValidate()
        )
        ```
        """

        # Body params:
        body_params = notification_channel_for_validate

        resource_path = f"/api/v1/validate_notification_channel".replace("_", "-")
        method = "POST"
        return self._api_client.call_api(
            resource_path=resource_path,
            method=method,
            body=body_params,
        )
