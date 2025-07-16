"""
Examples for using the PodsApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import PodsApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = PodsApi(api_client)


def example_count_pods():
    """
    Example of using count_pods

    Get pods count.
    Retrieve the number of pods from a cluster.
    """
    try:
        # Prepare the request parameters

        deleted = True

        filter_by = ["example_item_1", "example_item_2"]

        search = "example_search"

        # Make the API call
        api_response = api_instance.count_pods(
            deleted=deleted,
            filter_by=filter_by,
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling count_pods: {e}")


def example_get_revision_pods():
    """
    Example of using get_revision_pods

    Get revision pods by id. [Experimental]
    Retrieve the details of revision pods by revision id. Supported for clusters v2.21+.
    """
    try:
        # Prepare the request parameters
        revision_id = "example_revision_id"

        deleted = True

        # Make the API call
        api_response = api_instance.get_revision_pods(
            revision_id=revision_id,
            deleted=deleted,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_revision_pods: {e}")


def example_get_workload_pod_metrics():
    """
    Example of using get_workload_pod_metrics

    Get pod metrics data.
    Retrieve pod&#39;s metrics data for use in analysis applications.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        pod_id = "example_pod_id"

        metric_type = ["example_item_1", "example_item_2"]

        start = "2024-12-29T12:00:00Z"

        end = "2024-12-29T12:00:00Z"

        number_of_samples = 42

        # Make the API call
        api_response = api_instance.get_workload_pod_metrics(
            workload_id=workload_id,
            pod_id=pod_id,
            metric_type=metric_type,
            start=start,
            end=end,
            number_of_samples=number_of_samples,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_workload_pod_metrics: {e}")


def example_get_workload_pods():
    """
    Example of using get_workload_pods

    Get workload pods by id.
    Retrieve the details of workload pods by workload id.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        deleted = True

        offset = 42

        limit = 42

        search = "example_search"

        # Make the API call
        api_response = api_instance.get_workload_pods(
            workload_id=workload_id,
            deleted=deleted,
            offset=offset,
            limit=limit,
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_workload_pods: {e}")


def example_list_pods():
    """
    Example of using list_pods

    List pods.
    Retrieve a list of pods from a cluster.
    """
    try:
        # Prepare the request parameters

        deleted = True

        offset = 42

        limit = 42

        sort_order = "example_sort_order"

        sort_by = "example_sort_by"

        filter_by = ["example_item_1", "example_item_2"]

        completed = "example_completed"

        search = "example_search"

        # Make the API call
        api_response = api_instance.list_pods(
            deleted=deleted,
            offset=offset,
            limit=limit,
            sort_order=sort_order,
            sort_by=sort_by,
            filter_by=filter_by,
            verbosity=verbosity,
            completed=completed,
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_pods: {e}")
