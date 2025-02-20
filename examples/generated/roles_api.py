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


def example_get_role():
    """
    Example of using get_role

    Get a role by id.
    Retrieve the details of a role by id.
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


def example_get_roles():
    """
    Example of using get_roles

    Get a list of roles.
    Use to retrieve a list of roles.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_roles()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_roles: {e}")
