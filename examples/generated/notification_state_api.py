"""
Examples for using the NotificationStateApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import NotificationStateApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = NotificationStateApi(api_client)


def example_get_notification_state():
    """
    Example of using get_notification_state

    Get notification state
    Get notification state
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_notification_state()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_notification_state: {e}")


def example_update_notification_state():
    """
    Example of using update_notification_state

    Update notification state
    Update tenant notifications state
    """
    try:
        # Prepare the request parameters

        # Create example data for NotificationState
        notification_state = models.NotificationState(
            enabled=True,
            email=runai.models.email_notifications_state.EmailNotificationsState(
                enabled=True,
            ),
            slack=runai.models.slack_notifications_state.SlackNotificationsState(
                enabled=True,
                workspace_name="",
            ),
        )

        # Make the API call
        api_response = api_instance.update_notification_state(
            notification_state=notification_state,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_notification_state: {e}")
