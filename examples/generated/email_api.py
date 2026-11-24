"""
Examples for using the EmailApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import EmailApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = EmailApi(api_client)


def example_create_email():
    """
    Example of using create_email

    Create email notification channel
    Create email notification channel
    """
    try:
        # Prepare the request parameters

        # Create example data for EmailChannel
        email_channel = models.EmailChannel(
            config=runai.models.email_channel_config.EmailChannelConfig()
        )

        # Make the API call
        api_response = api_instance.create_email(
            email_channel=email_channel,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_email: {e}")


def example_delete_email():
    """
    Example of using delete_email

    Delete email notification channel
    Delete email notification channel
    """
    try:
        # Make the API call with no parameters
        api_instance.delete_email()

    except Exception as e:
        print(f"Exception when calling delete_email: {e}")


def example_get_email():
    """
    Example of using get_email

    Get email notification channel
    Get email notification channel
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_email()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_email: {e}")


def example_get_email_notification_state():
    """
    Example of using get_email_notification_state

    Get email notification state
    Get email notification state
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_email_notification_state()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_email_notification_state: {e}")


def example_patch_email():
    """
    Example of using patch_email

    Patch email notification channel
    Patch email notification channel
    """
    try:
        # Prepare the request parameters

        # Create example data for EmailChannelForPatch
        email_channel_for_patch = models.EmailChannelForPatch(
            config=runai.models.email_channel_config_for_patch.EmailChannelConfigForPatch()
        )

        # Make the API call
        api_response = api_instance.patch_email(
            email_channel_for_patch=email_channel_for_patch,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling patch_email: {e}")


def example_update_email():
    """
    Example of using update_email

    Update email notification channel
    Update email notification channel
    """
    try:
        # Prepare the request parameters

        # Create example data for EmailChannel
        email_channel = models.EmailChannel(
            config=runai.models.email_channel_config.EmailChannelConfig()
        )

        # Make the API call
        api_response = api_instance.update_email(
            email_channel=email_channel,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_email: {e}")


def example_update_email_notification_state():
    """
    Example of using update_email_notification_state

    Update email notification state
    Update tenant email notification state
    """
    try:
        # Prepare the request parameters

        # Create example data for NotificationStateStatus
        notification_state_status = models.NotificationStateStatus(enabled=True)

        # Make the API call
        api_response = api_instance.update_email_notification_state(
            notification_state_status=notification_state_status,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_email_notification_state: {e}")


def example_validate_email():
    """
    Example of using validate_email

    Validate configuration of Email Channel
    Validate configuration of Email Channel
    """
    try:
        # Prepare the request parameters

        # Create example data for EmailChannelConfig
        email_channel_config = models.EmailChannelConfig()

        # Make the API call
        api_response = api_instance.validate_email(
            email_channel_config=email_channel_config,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling validate_email: {e}")
