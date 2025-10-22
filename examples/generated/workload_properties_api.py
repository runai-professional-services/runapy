"""
Examples for using the WorkloadPropertiesApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import WorkloadPropertiesApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = WorkloadPropertiesApi(api_client)


def example_create_workload_type():
    """
    Example of using create_workload_type

    Create a workload type.
    Create a new workload type in the system by providing its identification details and configuration, making it available for use and management within the platform.
    """
    try:
        # Prepare the request parameters

        # Create example data for WorkloadTypeCreateFields
        workload_type_create_fields = models.WorkloadTypeCreateFields()

        # Make the API call
        api_response = api_instance.create_workload_type(
            workload_type_create_fields=workload_type_create_fields,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_workload_type: {e}")


def example_delete_workload_type():
    """
    Example of using delete_workload_type

    Delete a workload type by id.
    Deletes a specific workload type by its ID.
    """
    try:
        # Prepare the request parameters
        workload_type_id = "example_workload_type_id"

        # Make the API call
        api_instance.delete_workload_type(
            workload_type_id=workload_type_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_workload_type: {e}")


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

        filter_by = ["example_item_1", "example_item_2"]

        # Make the API call
        api_response = api_instance.list_workload_types(
            external_types_only=external_types_only,
            filter_by=filter_by,
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

        # Create example data for WorkloadTypeUpdateFields
        workload_type_update_fields = models.WorkloadTypeUpdateFields()

        # Make the API call
        api_response = api_instance.update_workload_type(
            workload_type_id=workload_type_id,
            workload_type_update_fields=workload_type_update_fields,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_workload_type: {e}")
