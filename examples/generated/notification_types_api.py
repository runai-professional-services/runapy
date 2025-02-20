"""
Examples for using the NotificationTypesApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import NotificationTypesApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = NotificationTypesApi(api_client)


def example_get_notification_types():
    """
    Example of using get_notification_types

    Get notification types
    Get list of available notification types
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_notification_types()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_notification_types: {e}")
