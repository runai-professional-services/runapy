"""
Examples for using the MeApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import MeApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = MeApi(api_client)


def example_count_me_access_rules():
    """
    Example of using count_me_access_rules

    Count the access rules assigned to the requesting user.
    Use to retrieve the number of access rules assigned to the requesting user.
    """
    try:
        # Prepare the request parameters
        search = "example_search"

        # Make the API call
        api_response = api_instance.count_me_access_rules(
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling count_me_access_rules: {e}")


def example_get_me_access_rules():
    """
    Example of using get_me_access_rules

    List the access rules assigned to the requesting user.
    Retrieve the access rules assigned to the requesting user.
    """
    try:
        # Prepare the request parameters

        limit = 42

        offset = 42

        search = "example_search"

        # Make the API call
        api_response = api_instance.get_me_access_rules(
            limit=limit,
            offset=offset,
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_me_access_rules: {e}")
