"""
Examples for using the WorkloadsPrioritiesApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import WorkloadsPrioritiesApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = WorkloadsPrioritiesApi(api_client)


def example_get_workload_priorities():
    """
    Example of using get_workload_priorities

    Get workload priorities.
    Retrieve the list of all workload priorities available in the system
    """
    try:
        # Prepare the request parameters
        sort_order = "example_sort_order"

        sort_by = "example_sort_by"

        filter_by = ["example_item_1", "example_item_2"]

        # Make the API call
        api_response = api_instance.get_workload_priorities(
            sort_order=sort_order,
            sort_by=sort_by,
            filter_by=filter_by,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_workload_priorities: {e}")
