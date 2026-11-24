"""
Examples for using the ProjectsApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import ProjectsApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = ProjectsApi(api_client)


def example_batch_patch_project_node_pool_resources():
    """
    Example of using batch_patch_project_node_pool_resources

    Patch multiple projects node pool resources in batch.
    Partially updates node pool resource quotas for multiple projects in a single request.
    """
    try:
        # Prepare the request parameters

        # Create example data for BatchPatchNodePoolResourcesRequest
        batch_patch_node_pool_resources_request = models.BatchPatchNodePoolResourcesRequest(
            patch_requests=[
                runai.models.node_pool_resources_patch_request.NodePoolResourcesPatchRequest(
                    org_unit_id="",
                    node_pool_id="",
                    rank="",
                    resources=runai.models.resources_per_node_pool_nullable.ResourcesPerNodePoolNullable(
                        gpu=runai.models.gpu.gpu(),
                        cpu=runai.models.cpu.cpu(),
                        memory=runai.models.resources_memory.Resources_memory(),
                    ),
                )
            ]
        )

        # Make the API call
        api_response = api_instance.batch_patch_project_node_pool_resources(
            batch_patch_node_pool_resources_request=batch_patch_node_pool_resources_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling batch_patch_project_node_pool_resources: {e}")


def example_count_project_node_pool_resources():
    """
    Example of using count_project_node_pool_resources

    Count projects node pool resources
    Count projects node pool resources
    """
    try:
        # Prepare the request parameters

        filter_by = ["example_item_1", "example_item_2"]

        search = "example_search"

        # Make the API call
        api_response = api_instance.count_project_node_pool_resources(
            filter_by=filter_by,
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling count_project_node_pool_resources: {e}")


def example_count_projects():
    """
    Example of using count_projects

    Count projects
    count projects
    """
    try:
        # Prepare the request parameters

        filter_by = ["example_item_1", "example_item_2"]

        search = "example_search"

        # Make the API call
        api_response = api_instance.count_projects(
            filter_by=filter_by,
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling count_projects: {e}")


def example_create_project():
    """
    Example of using create_project

    Create project
    Create a project
    """
    try:
        # Prepare the request parameters

        # Create example data for ProjectCreationRequest
        project_creation_request = models.ProjectCreationRequest()

        # Make the API call
        api_response = api_instance.create_project(
            project_creation_request=project_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_project: {e}")


def example_delete_project():
    """
    Example of using delete_project

    Delete project
    Delete a project
    """
    try:
        # Prepare the request parameters
        project_id = "example_project_id"

        # Make the API call
        api_instance.delete_project(
            project_id=project_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_project: {e}")


def example_get_project():
    """
    Example of using get_project

    Get project
    Get a project by id
    """
    try:
        # Prepare the request parameters
        project_id = "example_project_id"

        # Make the API call
        api_response = api_instance.get_project(
            project_id=project_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_project: {e}")


def example_get_project_metrics():
    """
    Example of using get_project_metrics

    Get project metrics data.
    Retrieves project data metrics from the metrics database. Use in reporting and analysis tools.
    """
    try:
        # Prepare the request parameters
        project_id = "example_project_id"

        metric_type = ["example_item_1", "example_item_2"]

        start = "2024-12-29T12:00:00Z"

        end = "2024-12-29T12:00:00Z"

        number_of_samples = 42

        nodepool_name = "example_nodepool_name"

        # Make the API call
        api_response = api_instance.get_project_metrics(
            project_id=project_id,
            metric_type=metric_type,
            start=start,
            end=end,
            number_of_samples=number_of_samples,
            nodepool_name=nodepool_name,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_project_metrics: {e}")


def example_get_project_node_pool_resources():
    """
    Example of using get_project_node_pool_resources

    Get projects node pool resources
    List projects node pool resources
    """
    try:
        # Prepare the request parameters

        filter_by = ["example_item_1", "example_item_2"]

        sort_order = "example_sort_order"

        offset = 42

        limit = 42

        search = "example_search"

        # Make the API call
        api_response = api_instance.get_project_node_pool_resources(
            filter_by=filter_by,
            sort_by=sort_by,
            sort_order=sort_order,
            offset=offset,
            limit=limit,
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_project_node_pool_resources: {e}")


def example_get_projects():
    """
    Example of using get_projects

    Get projects
    List projects
    """
    try:
        # Prepare the request parameters

        filter_by = ["example_item_1", "example_item_2"]

        sort_order = "example_sort_order"

        offset = 42

        limit = 42

        search = "example_search"

        # Make the API call
        api_response = api_instance.get_projects(
            filter_by=filter_by,
            sort_by=sort_by,
            sort_order=sort_order,
            offset=offset,
            limit=limit,
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_projects: {e}")


def example_get_projects_telemetry():
    """
    Example of using get_projects_telemetry

    Get projects telemetry
    Get projects telemetry data by the given query parameters
    """
    try:
        # Prepare the request parameters

        cluster_id = "example_cluster_id"

        nodepool_id = "example_nodepool_id"

        department_id = "example_department_id"

        group_by = ["example_item_1", "example_item_2"]

        # Make the API call
        api_response = api_instance.get_projects_telemetry(
            telemetry_type=telemetry_type,
            cluster_id=cluster_id,
            nodepool_id=nodepool_id,
            department_id=department_id,
            group_by=group_by,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_projects_telemetry: {e}")


def example_patch_project_resources():
    """
    Example of using patch_project_resources

    Patch project resources
    Partial updates to specific items in the list. Should be used for update one or more attributes of an item without modifying the entire resource.
    """
    try:
        # Prepare the request parameters
        project_id = "example_project_id"

        resources_nullable = ["example_item_1", "example_item_2"]

        # Make the API call
        api_response = api_instance.patch_project_resources(
            project_id=project_id,
            resources_nullable=resources_nullable,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling patch_project_resources: {e}")


def example_update_project():
    """
    Example of using update_project

    Update project
    Update project by Id
    """
    try:
        # Prepare the request parameters
        project_id = "example_project_id"

        # Create example data for ProjectUpdateRequest
        project_update_request = models.ProjectUpdateRequest()

        # Make the API call
        api_response = api_instance.update_project(
            project_id=project_id,
            project_update_request=project_update_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_project: {e}")


def example_update_project_resources():
    """
    Example of using update_project_resources

    Update project resources
    Update projects resources
    """
    try:
        # Prepare the request parameters
        project_id = "example_project_id"

        resources_nullable = ["example_item_1", "example_item_2"]

        # Make the API call
        api_response = api_instance.update_project_resources(
            project_id=project_id,
            resources_nullable=resources_nullable,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_project_resources: {e}")
