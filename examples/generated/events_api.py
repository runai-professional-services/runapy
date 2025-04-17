"""
Examples for using the EventsApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import EventsApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = EventsApi(api_client)


def example_get_revision_events():
    """
    Example of using get_revision_events

    Get revision events by id. [Experimental]
    Retrieve all the revision events using a revision id. Supported for clusters v2.21+.
    """
    try:
        # Prepare the request parameters
        revision_id = "example_revision_id"

        offset = 42

        limit = 42

        sort_order = "example_sort_order"

        # Make the API call
        api_response = api_instance.get_revision_events(
            revision_id=revision_id,
            offset=offset,
            limit=limit,
            sort_order=sort_order,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_revision_events: {e}")


def example_get_revision_history():
    """
    Example of using get_revision_history

    Get the revision history. [Experimental]
    Retrieve revision history details, including events, using a revision id. Supported for clusters v2.21+.
    """
    try:
        # Prepare the request parameters
        revision_id = "example_revision_id"

        offset = 42

        limit = 42

        # Make the API call
        api_response = api_instance.get_revision_history(
            revision_id=revision_id,
            offset=offset,
            limit=limit,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_revision_history: {e}")


def example_get_workload_events():
    """
    Example of using get_workload_events

    Get the workload events.
    Retrieve all the workload events using a workload id.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        offset = 42

        limit = 42

        sort_order = "example_sort_order"

        # Make the API call
        api_response = api_instance.get_workload_events(
            workload_id=workload_id,
            offset=offset,
            limit=limit,
            sort_order=sort_order,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_workload_events: {e}")


def example_get_workload_history():
    """
    Example of using get_workload_history

    Get the workload history.
    Retrieve workload history details, including events, using a workload id.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        offset = 42

        limit = 42

        # Make the API call
        api_response = api_instance.get_workload_history(
            workload_id=workload_id,
            offset=offset,
            limit=limit,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_workload_history: {e}")
