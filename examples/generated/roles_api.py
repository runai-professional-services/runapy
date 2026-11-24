"""
Examples for using the RolesApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import RolesApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = RolesApi(api_client)


def example_create_role():
    """
    Example of using create_role

    Create a role.
    Creates a custom role with the specified permission sets.
    """
    try:
        # Prepare the request parameters

        # Create example data for RoleCreationFieldsInternal
        role_creation_fields_internal = models.RoleCreationFieldsInternal()

        # Make the API call
        api_response = api_instance.create_role(
            role_creation_fields_internal=role_creation_fields_internal,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_role: {e}")


def example_delete_role():
    """
    Example of using delete_role

    Delete a role by id.
    Deletes a custom role. Use this endpoint to permanently remove roles that are no longer needed. NVIDIA Run:ai predefined roles cannot be deleted.
    """
    try:
        # Prepare the request parameters

        role_id_path = 42

        # Make the API call
        api_instance.delete_role(
            role_id_path=role_id_path,
        )

    except Exception as e:
        print(f"Exception when calling delete_role: {e}")


def example_get_role():
    """
    Example of using get_role

    Get a role by id.
    Retrieves details for a specific role, including its name, description, scope, and associated permission sets.
    """
    try:
        # Prepare the request parameters

        role_id_path = 42

        # Make the API call
        api_response = api_instance.get_role(
            role_id_path=role_id_path,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_role: {e}")


def example_get_role_v1():
    """
    Example of using get_role_v1

    Get a role by id.
    Retrieve the details of a role by id. This endpoint is deprecated and will be removed in a future release. Use GET /api/v2/authorization/roles/{roleIdPath} instead.
    """
    try:
        # Prepare the request parameters

        role_id_path = 42

        # Make the API call
        api_response = api_instance.get_role_v1(
            role_id_path=role_id_path,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_role_v1: {e}")


def example_get_roles():
    """
    Example of using get_roles

    Get a list of roles.
    Retrieves a list of all available roles, including both NVIDIA Run:ai predefined roles and custom roles. Use this endpoint to review role configurations, permission sets and permissions.
    """
    try:
        # Prepare the request parameters

        limit = 42

        offset = 42

        sort_order = "example_sort_order"

        filter_by = ["example_item_1", "example_item_2"]

        search = "example_search"

        # Make the API call
        api_response = api_instance.get_roles(
            limit=limit,
            offset=offset,
            sort_order=sort_order,
            sort_by=sort_by,
            filter_by=filter_by,
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_roles: {e}")


def example_get_roles_v1():
    """
    Example of using get_roles_v1

    Get a list of roles.
    Use to retrieve a list of roles. This endpoint is deprecated and will be removed in a future release. Use GET /api/v2/authorization/roles instead.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_roles_v1()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_roles_v1: {e}")


def example_role_disable():
    """
    Example of using role_disable

    Disable a role by id.
    Disables a specific role. Disabled roles cannot be assigned to users and do not grant any permissions.
    """
    try:
        # Prepare the request parameters

        role_id_path = 42

        # Make the API call
        api_instance.role_disable(
            role_id_path=role_id_path,
            body=body,
        )

    except Exception as e:
        print(f"Exception when calling role_disable: {e}")


def example_role_enable():
    """
    Example of using role_enable

    Enable a role by id.
    Enables a specific role. Disabled roles cannot be assigned to users and do not grant any permissions.
    """
    try:
        # Prepare the request parameters

        role_id_path = 42

        # Make the API call
        api_instance.role_enable(
            role_id_path=role_id_path,
            body=body,
        )

    except Exception as e:
        print(f"Exception when calling role_enable: {e}")


def example_update_role():
    """
    Example of using update_role

    Update a role by id.
    Updates a custom role, including its name, description, or associated permission sets. NVIDIA Run:ai predefined roles cannot be updated.
    """
    try:
        # Prepare the request parameters

        role_id_path = 42

        # Create example data for RoleCreationFieldsInternal
        role_creation_fields_internal = models.RoleCreationFieldsInternal()

        # Make the API call
        api_response = api_instance.update_role(
            role_id_path=role_id_path,
            role_creation_fields_internal=role_creation_fields_internal,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_role: {e}")
