"""
Examples for using the SlackApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import SlackApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = SlackApi(api_client)


def example_connect_slack_workspace():
    """
    Example of using connect_slack_workspace

    Connect Slack workspace
    Connect Slack workspace
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.connect_slack_workspace()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling connect_slack_workspace: {e}")


def example_create_slack_app():
    """
    Example of using create_slack_app

    Create Slack app
    Create Slack app
    """
    try:
        # Prepare the request parameters

        # Create example data for CreateSlackAppRequestBody
        create_slack_app_request_body = models.CreateSlackAppRequestBody(
            access_token=""
        )

        # Make the API call
        api_response = api_instance.create_slack_app(
            create_slack_app_request_body=create_slack_app_request_body,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_slack_app: {e}")


def example_create_slack_app_deprecated():
    """
    Example of using create_slack_app_deprecated

    Create Slack app
    Create Slack app
    """
    try:
        # Prepare the request parameters

        # Create example data for CreateSlackAppRequestBody
        create_slack_app_request_body = models.CreateSlackAppRequestBody(
            access_token=""
        )

        # Make the API call
        api_response = api_instance.create_slack_app_deprecated(
            create_slack_app_request_body=create_slack_app_request_body,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_slack_app_deprecated: {e}")


def example_delete_slack_app():
    """
    Example of using delete_slack_app

    Delete Slack app
    Delete Slack app
    """
    try:
        # Make the API call with no parameters
        api_instance.delete_slack_app()

    except Exception as e:
        print(f"Exception when calling delete_slack_app: {e}")


def example_disconnect_slack_workspace():
    """
    Example of using disconnect_slack_workspace

    Disconnect Slack workspace
    Disconnect Slack workspace
    """
    try:
        # Make the API call with no parameters
        api_instance.disconnect_slack_workspace()

    except Exception as e:
        print(f"Exception when calling disconnect_slack_workspace: {e}")


def example_get_slack():
    """
    Example of using get_slack

    Get slack notification channel
    Get slack notification channel
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_slack()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_slack: {e}")


def example_get_slack_notification_state():
    """
    Example of using get_slack_notification_state

    Get slack notification state
    Get slack notification state
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_slack_notification_state()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_slack_notification_state: {e}")


def example_patch_slack():
    """
    Example of using patch_slack

    Patch slack notification channel
    Patch slack notification channel
    """
    try:
        # Prepare the request parameters

        # Create example data for SlackNotificationChannelPatchRequest
        slack_notification_channel_patch_request = models.SlackNotificationChannelPatchRequest(
            name="",
            config=runai.models.slack_notification_channel_patch_request_config.SlackNotificationChannelPatchRequest_config(
                recipients=[""],
                direct_notifications=True,
            ),
        )

        # Make the API call
        api_response = api_instance.patch_slack(
            slack_notification_channel_patch_request=slack_notification_channel_patch_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling patch_slack: {e}")


def example_update_slack_notification_state():
    """
    Example of using update_slack_notification_state

    Update slack notification state
    Update tenant slack notification state
    """
    try:
        # Prepare the request parameters

        # Create example data for NotificationStateStatus
        notification_state_status = models.NotificationStateStatus(enabled=True)

        # Make the API call
        api_response = api_instance.update_slack_notification_state(
            notification_state_status=notification_state_status,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_slack_notification_state: {e}")


def example_validate_slack():
    """
    Example of using validate_slack

    Validate configuration of Slack Channel
    Validate configuration of Slack Channel
    """
    try:
        # Prepare the request parameters

        # Create example data for SlackNotificationChannelConfig
        slack_notification_channel_config = models.SlackNotificationChannelConfig(
            recipients=[""], direct_notifications=True, api_token=""
        )

        # Make the API call
        api_response = api_instance.validate_slack(
            slack_notification_channel_config=slack_notification_channel_config,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling validate_slack: {e}")
