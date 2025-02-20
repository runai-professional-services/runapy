"""
Examples for using the SubscriptionsApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import SubscriptionsApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = SubscriptionsApi(api_client)


def example_create_subscription():
    """
    Example of using create_subscription

    Create user subscription
    Create user subscription
    """
    try:
        # Prepare the request parameters

        # Create example data for Subscription
        subscription = models.Subscription()

        # Make the API call
        api_response = api_instance.create_subscription(
            subscription=subscription,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_subscription: {e}")


def example_delete_subscription():
    """
    Example of using delete_subscription

    Delete user subscription
    Delete user subscription
    """
    try:
        # Prepare the request parameters
        id = "example_id"

        # Make the API call
        api_instance.delete_subscription(
            id=id,
        )

    except Exception as e:
        print(f"Exception when calling delete_subscription: {e}")


def example_get_my_subscriptions():
    """
    Example of using get_my_subscriptions

    Get current users subscriptions
    Get current users subscriptions
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_my_subscriptions()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_my_subscriptions: {e}")


def example_update_subscription():
    """
    Example of using update_subscription

    Update user subscription
    Update user subscription
    """
    try:
        # Prepare the request parameters
        id = "example_id"

        # Create example data for SubscriptionForPut
        subscription_for_put = models.SubscriptionForPut(
            events=[
                runai.models.subscription_event.SubscriptionEvent(
                    category="",
                    types=[""],
                )
            ],
            channels=[""],
        )

        # Make the API call
        api_response = api_instance.update_subscription(
            id=id,
            subscription_for_put=subscription_for_put,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_subscription: {e}")
