"""
Examples for using the WorkloadsAPIApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import WorkloadsAPIApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = WorkloadsAPIApi(api_client)


def example_count_workload_elements():
    """
    Example of using count_workload_elements

    Count workload structure elements.
    Returns the total count of structure elements reported by the cluster and the count of elements stored in the database for the given workload. Requires cluster version &gt;&#x3D; 2.25.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        # Make the API call
        api_response = api_instance.count_workload_elements(
            workload_id=workload_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling count_workload_elements: {e}")


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


def example_get_workload_elements():
    """
    Example of using get_workload_elements

    Get workload structure elements by workload id.
    Retrieve the hierarchy structure elements for a workload. Returns a flat list ordered by level. Requires cluster version &gt;&#x3D; 2.25.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        offset = 42

        limit = 42

        # Make the API call
        api_response = api_instance.get_workload_elements(
            workload_id=workload_id,
            offset=offset,
            limit=limit,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_workload_elements: {e}")


def example_get_workload_endpoints():
    """
    Example of using get_workload_endpoints

    Get workload endpoints.
    Retrieve the network endpoints exposed by a workload using a workload ID.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        # Make the API call
        api_response = api_instance.get_workload_endpoints(
            workload_id=workload_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_workload_endpoints: {e}")


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
    Retrieves workload data by telemetry type. Optionally filter by specific workload phases.  Telemetry Types: - WORKLOADS_COUNT: Count of workloads - GPU_ALLOCATION: GPU allocation metrics - PENDING_TIME_DISTRIBUTION: Distribution of workloads by current pending time (time since entering Pending phase).         For this type, results are automatically grouped by 4 time buckets and any additional groupBy parameters. - IDLE_ALLOCATED_GPUS: Sum of idle allocated GPU devices across workloads
    """
    try:
        # Prepare the request parameters

        cluster_id = "example_cluster_id"

        nodepool_name = "example_nodepool_name"

        department_id = "example_department_id"

        group_by = ["example_item_1", "example_item_2"]

        filter_by_phases = ["example_item_1", "example_item_2"]

        # Make the API call
        api_response = api_instance.get_workloads_telemetry(
            telemetry_type=telemetry_type,
            cluster_id=cluster_id,
            nodepool_name=nodepool_name,
            department_id=department_id,
            group_by=group_by,
            filter_by_phases=filter_by_phases,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_workloads_telemetry: {e}")
