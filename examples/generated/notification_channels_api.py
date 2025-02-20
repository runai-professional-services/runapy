"""
Examples for using the NotificationChannelsApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import NotificationChannelsApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = NotificationChannelsApi(api_client)


def example_create_notification_channel_config():
    """
    Example of using create_notification_channel_config

    Create configuration of notification channel
    Create configuration of notification channel
    """
    try:
        # Prepare the request parameters

        # Create example data for NotificationChannel
        notification_channel = models.NotificationChannel()

        # Make the API call
        api_instance.create_notification_channel_config(
            notification_channel=notification_channel,
        )

    except Exception as e:
        print(f"Exception when calling create_notification_channel_config: {e}")


def example_delete_notification_channel_config():
    """
    Example of using delete_notification_channel_config

    Delete configuration of Notification Channel
    Delete configuration of Notification Channel
    """
    try:
        # Prepare the request parameters
        name = "example_name"

        # Make the API call
        api_instance.delete_notification_channel_config(
            name=name,
        )

    except Exception as e:
        print(f"Exception when calling delete_notification_channel_config: {e}")


def example_get_notification_channel_config():
    """
    Example of using get_notification_channel_config

    Get configuration of notification channel
    Get configuration of notification channel
    """
    try:
        # Prepare the request parameters
        name = "example_name"

        # Make the API call
        api_response = api_instance.get_notification_channel_config(
            name=name,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_notification_channel_config: {e}")


def example_get_notification_channels():
    """
    Example of using get_notification_channels

    Get supported Notification Channels
    Get supported Notification Channels
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_notification_channels()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_notification_channels: {e}")


def example_patch_notification_channel_config():
    """
    Example of using patch_notification_channel_config

    Patch configuration of Notification Channel
    Patch configuration of Notification Channel
    """
    try:
        # Prepare the request parameters
        name = "example_name"

        # Create example data for NotificationChannelForPatch
        notification_channel_for_patch = models.NotificationChannelForPatch(
            type="email",
            config=runai.models.notification_channel_config.NotificationChannelConfig(),
        )

        # Make the API call
        api_instance.patch_notification_channel_config(
            name=name,
            notification_channel_for_patch=notification_channel_for_patch,
        )

    except Exception as e:
        print(f"Exception when calling patch_notification_channel_config: {e}")


def example_update_notification_channel_config():
    """
    Example of using update_notification_channel_config

    Update configuration of Notification Channel
    Update configuration of Notification Channel
    """
    try:
        # Prepare the request parameters
        name = "example_name"

        # Create example data for NotificationChannel
        notification_channel = models.NotificationChannel()

        # Make the API call
        api_instance.update_notification_channel_config(
            name=name,
            notification_channel=notification_channel,
        )

    except Exception as e:
        print(f"Exception when calling update_notification_channel_config: {e}")


def example_validate_notification_channel():
    """
    Example of using validate_notification_channel

    Validate configuration of Notification Channel
    Validate configuration of Notification Channel
    """
    try:
        # Prepare the request parameters

        # Create example data for NotificationChannelForValidate
        notification_channel_for_validate = models.NotificationChannelForValidate()

        # Make the API call
        api_response = api_instance.validate_notification_channel(
            notification_channel_for_validate=notification_channel_for_validate,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling validate_notification_channel: {e}")
