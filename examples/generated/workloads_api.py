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


def example_get_category_by_id():
    """
    Example of using get_category_by_id

    Get workload category by id.
    Retrieves a specific workload category by its ID. Workload categories are used to classify and monitor different types of workloads within the NVIDIA Run:ai platform.
    """
    try:
        # Prepare the request parameters
        category_id = "example_category_id"

        # Make the API call
        api_response = api_instance.get_category_by_id(
            category_id=category_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_category_by_id: {e}")


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


def example_get_workload_type():
    """
    Example of using get_workload_type

    List workload type by id.
    Retrieves a specific workload type by its ID.
    """
    try:
        # Prepare the request parameters
        workload_type_id = "example_workload_type_id"

        # Make the API call
        api_response = api_instance.get_workload_type(
            workload_type_id=workload_type_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_workload_type: {e}")


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


def example_list_categories():
    """
    Example of using list_categories

    List workload categories.
    Retrieves a list of workload categories. These categories are used to classify and monitor different types of workloads within the NVIDIA Run:ai platform.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.list_categories()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_categories: {e}")


def example_list_workload_types():
    """
    Example of using list_workload_types

    List workload types.
    Retrieves a list of workload types with their configurations - their corresponding workload categories and priorities.
    """
    try:
        # Prepare the request parameters

        external_types_only = True

        # Make the API call
        api_response = api_instance.list_workload_types(
            external_types_only=external_types_only,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_workload_types: {e}")


def example_update_workload_type():
    """
    Example of using update_workload_type

    Update a workload type by id.
    Update the default category or priority assigned to a workload type.
    """
    try:
        # Prepare the request parameters
        workload_type_id = "example_workload_type_id"

        # Create example data for WorkloadTypeConfigUpdateFields
        workload_type_config_update_fields = models.WorkloadTypeConfigUpdateFields(
            category_id="", priority_id=""
        )

        # Make the API call
        api_response = api_instance.update_workload_type(
            workload_type_id=workload_type_id,
            workload_type_config_update_fields=workload_type_config_update_fields,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_workload_type: {e}")
