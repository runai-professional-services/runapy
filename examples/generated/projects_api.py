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


def example_create_project_0():
    """
    Example of using create_project_0

    Create a new project.
    Creates a new project in a specific cluster. Deprecated - use &#x60;/api/v1/org-unit/projects&#x60; instead.
    """
    try:
        # Prepare the request parameters
        cluster_id = "example_cluster_id"

        # Create example data for ProjectCreateRequest
        project_create_request = models.ProjectCreateRequest()

        exclude_permissions = True

        # Make the API call
        api_response = api_instance.create_project_0(
            cluster_id=cluster_id,
            project_create_request=project_create_request,
            exclude_permissions=exclude_permissions,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_project_0: {e}")


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


def example_delete_project_0():
    """
    Example of using delete_project_0

    Delete a project.
    Deletes a project from a specific cluster. Deprecated - use &#x60;/api/v1/org-unit/projects/{projectId}&#x60; instead.
    """
    try:
        # Prepare the request parameters
        cluster_id = "example_cluster_id"

        id = 42

        # Make the API call
        api_response = api_instance.delete_project_0(
            cluster_id=cluster_id,
            id=id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling delete_project_0: {e}")


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


def example_get_project_0():
    """
    Example of using get_project_0

    List details of a specific project.
    Retrieves the details of a specific project from a specific cluster. Use for project analysis. **Requires &#x60;view&#x60; permissions to the queried project**. Deprecated - use &#x60;/api/v1/org-unit/projects/{projectId}&#x60; instead.
    """
    try:
        # Prepare the request parameters
        cluster_id = "example_cluster_id"

        id = "example_id"

        exclude_permissions = True

        # Make the API call
        api_response = api_instance.get_project_0(
            cluster_id=cluster_id,
            id=id,
            exclude_permissions=exclude_permissions,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_project_0: {e}")


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


def example_get_project_metrics_0():
    """
    Example of using get_project_metrics_0

    Get metrics data for a specific project.
    Retrieves data from the metrics database. \\n Use in reporting and analysis tools. \\n Use a time range to return historical data (optional). If you use a &#x60;start&#x60; date, an &#x60;end&#x60; date is required.
    """
    try:
        # Prepare the request parameters
        cluster_uuid = "example_cluster_uuid"

        project_id = "example_project_id"

        start = "2024-12-29T12:00:00Z"

        end = "2024-12-29T12:00:00Z"

        number_of_samples = 42

        nodepool_name = "example_nodepool_name"

        # Make the API call
        api_response = api_instance.get_project_metrics_0(
            cluster_uuid=cluster_uuid,
            project_id=project_id,
            start=start,
            end=end,
            number_of_samples=number_of_samples,
            nodepool_name=nodepool_name,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_project_metrics_0: {e}")


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


def example_get_projects_0():
    """
    Example of using get_projects_0

    List all projects and their details.
    Retrieves a list of all projects and details from a specific cluster. Use in reporting and analysis tools. Deprecated - use &#x60;/api/v1/org-unit/projects&#x60; instead.
    """
    try:
        # Prepare the request parameters
        cluster_id = "example_cluster_id"

        exclude_permissions = True

        memory_unit_mb = True

        # Make the API call
        api_response = api_instance.get_projects_0(
            cluster_id=cluster_id,
            exclude_permissions=exclude_permissions,
            memory_unit_mb=memory_unit_mb,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_projects_0: {e}")


def example_get_projects_metrics():
    """
    Example of using get_projects_metrics

    Get metrics data for all projects.
    Retrieves data from the metrics database. \\n Use in reporting and analysis tools. \\n Use a time range to return historical data (optional). If you use a &#x60;start&#x60; date, an &#x60;end&#x60; date is required.
    """
    try:
        # Prepare the request parameters
        cluster_uuid = "example_cluster_uuid"

        start = "2024-12-29T12:00:00Z"

        end = "2024-12-29T12:00:00Z"

        number_of_samples = 42

        nodepool_name = "example_nodepool_name"

        # Make the API call
        api_response = api_instance.get_projects_metrics(
            cluster_uuid=cluster_uuid,
            start=start,
            end=end,
            number_of_samples=number_of_samples,
            nodepool_name=nodepool_name,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_projects_metrics: {e}")


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


def example_update_project_0():
    """
    Example of using update_project_0

    Update a project.
    Updates a project&#39;s details in a specific cluster. For example, node pool resources, and others. Deprecated - use &#x60;/api/v1/org-unit/projects/{projectId}&#x60; instead.
    """
    try:
        # Prepare the request parameters
        id = "example_id"

        cluster_id = "example_cluster_id"

        # Create example data for ProjectUpdateRequest1
        project_update_request1 = models.ProjectUpdateRequest1()

        exclude_permissions = True

        # Make the API call
        api_response = api_instance.update_project_0(
            id=id,
            cluster_id=cluster_id,
            project_update_request1=project_update_request1,
            exclude_permissions=exclude_permissions,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_project_0: {e}")


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
