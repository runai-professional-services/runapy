"""
Examples for using the PermissionsApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import PermissionsApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = PermissionsApi(api_client)


def example_get_permissions():
    """
    Example of using get_permissions

    Get a summary of user permissions.
    Retrieve a summary of user permissions.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_permissions()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_permissions: {e}")


def example_get_permitted_scopes():
    """
    Example of using get_permitted_scopes

    Calculate permitted scopes.
    Use to calculate user permitted scopes for an action on a resource.
    """
    try:
        # Prepare the request parameters

        # Create example data for GetPermittedScopesRequest
        get_permitted_scopes_request = models.GetPermittedScopesRequest(
            resource_type="department", action="create"
        )

        # Make the API call
        api_response = api_instance.get_permitted_scopes(
            get_permitted_scopes_request=get_permitted_scopes_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_permitted_scopes: {e}")
