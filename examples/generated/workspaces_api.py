"""
Examples for using the WorkspacesApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import WorkspacesApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = WorkspacesApi(api_client)


def example_create_workspace1():
    """
    Example of using create_workspace1

    Create a workspace [Experimental]
    Create a new workspace in a specific project in the cluster.
    """
    try:
        # Prepare the request parameters

        # Create example data for WorkspaceCreationRequest
        workspace_creation_request = models.WorkspaceCreationRequest()

        # Make the API call
        api_response = api_instance.create_workspace1(
            workspace_creation_request=workspace_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_workspace1: {e}")


def example_delete_workspace():
    """
    Example of using delete_workspace

    Delete a workspace [Experimental]
    Delete a workspace using the workspace id.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        # Make the API call
        api_instance.delete_workspace(
            workload_id=workload_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_workspace: {e}")


def example_get_workspace():
    """
    Example of using get_workspace

    Get workspace data [Experimental]
    Retrieve workspace details using a workload id.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        # Make the API call
        api_response = api_instance.get_workspace(
            workload_id=workload_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_workspace: {e}")


def example_resume_workspace():
    """
    Example of using resume_workspace

    Resume a workspace [Experimental]
    Resume the workspace operation using the workspace id.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        # Make the API call
        api_response = api_instance.resume_workspace(
            workload_id=workload_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling resume_workspace: {e}")


def example_suspend_workspace():
    """
    Example of using suspend_workspace

    Suspend a workspace [Experimental]
    Suspend a workspace using the workspace id.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        # Make the API call
        api_response = api_instance.suspend_workspace(
            workload_id=workload_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling suspend_workspace: {e}")
