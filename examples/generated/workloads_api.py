"""
Examples for using the WorkloadsApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import WorkloadsApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = WorkloadsApi(api_client)


def example_count_workloads():
    """
    Example of using count_workloads

    Count workloads.
    Retrieve the number of workloads.
    """
    try:
        # Prepare the request parameters

        deleted = True

        filter_by = ["example_item_1", "example_item_2"]

        search = "example_search"

        # Make the API call
        api_response = api_instance.count_workloads(
            deleted=deleted,
            filter_by=filter_by,
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling count_workloads: {e}")


def example_get_workload():
    """
    Example of using get_workload

    Get a workload.
    Retrieve workload data using a &#x60;workloadId&#x60;.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        # Make the API call
        api_response = api_instance.get_workload(
            workload_id=workload_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_workload: {e}")


def example_get_workload_metrics():
    """
    Example of using get_workload_metrics

    Get workload metrics data.
    Retrieves workloads data metrics from the metrics database. Use in reporting and analysis tools.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        metric_type = ["example_item_1", "example_item_2"]

        start = "2024-12-29T12:00:00Z"

        end = "2024-12-29T12:00:00Z"

        number_of_samples = 42

        # Make the API call
        api_response = api_instance.get_workload_metrics(
            workload_id=workload_id,
            metric_type=metric_type,
            start=start,
            end=end,
            number_of_samples=number_of_samples,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_workload_metrics: {e}")


def example_get_workloads():
    """
    Example of using get_workloads

    List workloads.
    Retrieve a list of active workloads with details.
    """
    try:
        # Prepare the request parameters

        deleted = True

        offset = 42

        limit = 42

        sort_order = "example_sort_order"

        sort_by = "example_sort_by"

        filter_by = ["example_item_1", "example_item_2"]

        search = "example_search"

        # Make the API call
        api_response = api_instance.get_workloads(
            deleted=deleted,
            offset=offset,
            limit=limit,
            sort_order=sort_order,
            sort_by=sort_by,
            filter_by=filter_by,
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_workloads: {e}")


def example_get_workloads_telemetry():
    """
    Example of using get_workloads_telemetry

    Get the workloads telemetry.
    Retrieves workload data by telemetry type.
    """
    try:
        # Prepare the request parameters

        cluster_id = "example_cluster_id"

        nodepool_name = "example_nodepool_name"

        department_id = "example_department_id"

        group_by = ["example_item_1", "example_item_2"]

        # Make the API call
        api_response = api_instance.get_workloads_telemetry(
            telemetry_type=telemetry_type,
            cluster_id=cluster_id,
            nodepool_name=nodepool_name,
            department_id=department_id,
            group_by=group_by,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_workloads_telemetry: {e}")
