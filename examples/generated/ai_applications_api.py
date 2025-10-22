"""
Examples for using the AIApplicationsApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import AIApplicationsApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = AIApplicationsApi(api_client)


def example_get_application():
    """
    Example of using get_application

    Get AI application.
    Get AI application.
    """
    try:
        # Prepare the request parameters
        ai_application_id = "example_ai_application_id"

        # Make the API call
        api_response = api_instance.get_application(
            ai_application_id=ai_application_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_application: {e}")


def example_list_applications():
    """
    Example of using list_applications

    List AI applications.
    List AI applications.
    """
    try:
        # Prepare the request parameters

        offset = 42

        limit = 42

        sort_order = "example_sort_order"

        sort_by = "example_sort_by"

        filter_by = ["example_item_1", "example_item_2"]

        # Make the API call
        api_response = api_instance.list_applications(
            verbosity=verbosity,
            offset=offset,
            limit=limit,
            sort_order=sort_order,
            sort_by=sort_by,
            filter_by=filter_by,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_applications: {e}")
