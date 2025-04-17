"""
Examples for using the DepartmentsApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import DepartmentsApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = DepartmentsApi(api_client)


def example_count_departments():
    """
    Example of using count_departments

    Count departments
    count departments
    """
    try:
        # Prepare the request parameters

        filter_by = ["example_item_1", "example_item_2"]

        # Make the API call
        api_response = api_instance.count_departments(
            filter_by=filter_by,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling count_departments: {e}")


def example_create_department():
    """
    Example of using create_department

    Create department
    Create Department
    """
    try:
        # Prepare the request parameters

        # Create example data for DepartmentCreationRequest
        department_creation_request = models.DepartmentCreationRequest()

        # Make the API call
        api_response = api_instance.create_department(
            department_creation_request=department_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_department: {e}")


def example_create_department_0():
    """
    Example of using create_department_0

    Create a new department.
    Creates a new department in the cluster.
    """
    try:
        # Prepare the request parameters
        cluster_id = "example_cluster_id"

        # Create example data for DepartmentCreateRequest
        department_create_request = models.DepartmentCreateRequest()

        # Make the API call
        api_response = api_instance.create_department_0(
            cluster_id=cluster_id,
            department_create_request=department_create_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_department_0: {e}")


def example_delete_department():
    """
    Example of using delete_department

    Delete department
    Delete department by Id
    """
    try:
        # Prepare the request parameters
        department_id = "example_department_id"

        # Make the API call
        api_instance.delete_department(
            department_id=department_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_department: {e}")


def example_delete_department_0():
    """
    Example of using delete_department_0

    Delete a department.
    Deletes a department from a specific cluster.
    """
    try:
        # Prepare the request parameters
        cluster_id = "example_cluster_id"

        department_id = 42

        # Make the API call
        api_response = api_instance.delete_department_0(
            cluster_id=cluster_id,
            department_id=department_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling delete_department_0: {e}")


def example_get_department():
    """
    Example of using get_department

    Get department
    Get department by Id
    """
    try:
        # Prepare the request parameters
        department_id = "example_department_id"

        # Make the API call
        api_response = api_instance.get_department(
            department_id=department_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_department: {e}")


def example_get_department_0():
    """
    Example of using get_department_0

    Get a specific department.
    Retrieves the details of a specific department. Requires  the&#x60;view&#x60; permission for the department.
    """
    try:
        # Prepare the request parameters
        cluster_id = "example_cluster_id"

        department_id = 42

        exclude_permissions = True

        # Make the API call
        api_response = api_instance.get_department_0(
            cluster_id=cluster_id,
            department_id=department_id,
            exclude_permissions=exclude_permissions,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_department_0: {e}")


def example_get_department_metrics():
    """
    Example of using get_department_metrics

    Get department metrics data.
    Retrieves department data metrics from the metrics database. Use in reporting and analysis tools.
    """
    try:
        # Prepare the request parameters
        department_id = "example_department_id"

        metric_type = ["example_item_1", "example_item_2"]

        start = "2024-12-29T12:00:00Z"

        end = "2024-12-29T12:00:00Z"

        number_of_samples = 42

        nodepool_name = "example_nodepool_name"

        # Make the API call
        api_response = api_instance.get_department_metrics(
            department_id=department_id,
            metric_type=metric_type,
            start=start,
            end=end,
            number_of_samples=number_of_samples,
            nodepool_name=nodepool_name,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_department_metrics: {e}")


def example_get_department_metrics_0():
    """
    Example of using get_department_metrics_0

    Get metrics for a specific department.
    Get metrics for a specific department in the cluster.  Use a time range to return historical data (optional). If you use a &#x60;start&#x60; date, an &#x60;end&#x60; date is required.
    """
    try:
        # Prepare the request parameters
        cluster_uuid = "example_cluster_uuid"

        department_id = "example_department_id"

        start = "2024-12-29T12:00:00Z"

        end = "2024-12-29T12:00:00Z"

        number_of_samples = 42

        nodepool_name = "example_nodepool_name"

        # Make the API call
        api_response = api_instance.get_department_metrics_0(
            cluster_uuid=cluster_uuid,
            department_id=department_id,
            start=start,
            end=end,
            number_of_samples=number_of_samples,
            nodepool_name=nodepool_name,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_department_metrics_0: {e}")


def example_get_departments():
    """
    Example of using get_departments

    Get departments
    list departments
    """
    try:
        # Prepare the request parameters

        filter_by = ["example_item_1", "example_item_2"]

        sort_order = "example_sort_order"

        offset = 42

        limit = 42

        # Make the API call
        api_response = api_instance.get_departments(
            filter_by=filter_by,
            sort_by=sort_by,
            verbosity=verbosity,
            sort_order=sort_order,
            offset=offset,
            limit=limit,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_departments: {e}")


def example_get_departments_0():
    """
    Example of using get_departments_0

    List all departments.
    List all the departments managed by the tenant on a specific cluster.
    """
    try:
        # Prepare the request parameters
        cluster_id = "example_cluster_id"

        exclude_permissions = True

        memory_unit_mb = True

        # Make the API call
        api_response = api_instance.get_departments_0(
            cluster_id=cluster_id,
            exclude_permissions=exclude_permissions,
            memory_unit_mb=memory_unit_mb,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_departments_0: {e}")


def example_get_departments_metrics():
    """
    Example of using get_departments_metrics

    Get metrics for all departments.
    Get metrics for all departments in the cluster. Use a time range to return historical data (optional).  If you use a &#x60;start&#x60; date, an &#x60;end&#x60; date is required.
    """
    try:
        # Prepare the request parameters
        cluster_uuid = "example_cluster_uuid"

        start = "2024-12-29T12:00:00Z"

        end = "2024-12-29T12:00:00Z"

        number_of_samples = 42

        nodepool_name = "example_nodepool_name"

        # Make the API call
        api_response = api_instance.get_departments_metrics(
            cluster_uuid=cluster_uuid,
            start=start,
            end=end,
            number_of_samples=number_of_samples,
            nodepool_name=nodepool_name,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_departments_metrics: {e}")


def example_get_departments_telemetry():
    """
    Example of using get_departments_telemetry

    Get departments telemetry

    """
    try:
        # Prepare the request parameters

        cluster_id = "example_cluster_id"

        nodepool_name = "example_nodepool_name"

        department_id = "example_department_id"

        group_by = ["example_item_1", "example_item_2"]

        # Make the API call
        api_response = api_instance.get_departments_telemetry(
            telemetry_type=telemetry_type,
            cluster_id=cluster_id,
            nodepool_name=nodepool_name,
            department_id=department_id,
            group_by=group_by,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_departments_telemetry: {e}")


def example_patch_department_resources():
    """
    Example of using patch_department_resources

    Patch department resources
    Partial updates to specific items in the list. Should be used for update one or more attributes of an item without modifying the entire resource.
    """
    try:
        # Prepare the request parameters
        department_id = "example_department_id"

        resources_nullable = ["example_item_1", "example_item_2"]

        # Make the API call
        api_response = api_instance.patch_department_resources(
            department_id=department_id,
            resources_nullable=resources_nullable,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling patch_department_resources: {e}")


def example_update_department():
    """
    Example of using update_department

    Update department
    Update department by Id
    """
    try:
        # Prepare the request parameters
        department_id = "example_department_id"

        # Create example data for DepartmentUpdateRequest
        department_update_request = models.DepartmentUpdateRequest()

        # Make the API call
        api_response = api_instance.update_department(
            department_id=department_id,
            department_update_request=department_update_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_department: {e}")


def example_update_department_0():
    """
    Example of using update_department_0

    Update a department.
    Updates a department&#39;s details in the cluster. \\n For example, node pools and other details.
    """
    try:
        # Prepare the request parameters
        cluster_id = "example_cluster_id"

        department_id = 42

        # Create example data for DepartmentUpdateRequest1
        department_update_request1 = models.DepartmentUpdateRequest1()

        # Make the API call
        api_response = api_instance.update_department_0(
            cluster_id=cluster_id,
            department_id=department_id,
            department_update_request1=department_update_request1,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_department_0: {e}")


def example_update_department_admins():
    """
    Example of using update_department_admins

    Set the department admins.
    Deprecated. Instead, use the accessrules API to add the department-admin permissions to a specific subject.
    """
    try:
        # Prepare the request parameters
        cluster_id = "example_cluster_id"

        department_id = 42

        # Create example data for DepartmentAccessControl
        department_access_control = models.DepartmentAccessControl(
            department_id=2, department_admins=[""]
        )

        # Make the API call
        api_response = api_instance.update_department_admins(
            cluster_id=cluster_id,
            department_id=department_id,
            department_access_control=department_access_control,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_department_admins: {e}")


def example_update_department_resources():
    """
    Example of using update_department_resources

    Update department resources
    Update department resources by Id
    """
    try:
        # Prepare the request parameters
        department_id = "example_department_id"

        resources_nullable = ["example_item_1", "example_item_2"]

        # Make the API call
        api_response = api_instance.update_department_resources(
            department_id=department_id,
            resources_nullable=resources_nullable,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_department_resources: {e}")
