"""
Examples for using the ServiceAccountsApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import ServiceAccountsApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = ServiceAccountsApi(api_client)


def example_create_service_account():
    """
    Example of using create_service_account

    Create a service account.
    Used to create a service account.
    """
    try:
        # Prepare the request parameters

        # Create example data for ServiceAccountCreationRequest
        service_account_creation_request = models.ServiceAccountCreationRequest(
            name="awat5ikwowtta-3mh2lcafqw3zhes0"
        )

        # Make the API call
        api_response = api_instance.create_service_account(
            service_account_creation_request=service_account_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_service_account: {e}")


def example_delete_service_account_by_id():
    """
    Example of using delete_service_account_by_id

    Delete a service account by id.
    Use to delete a service account by id.
    """
    try:
        # Prepare the request parameters
        service_account_id = "example_service_account_id"

        # Make the API call
        api_instance.delete_service_account_by_id(
            service_account_id=service_account_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_service_account_by_id: {e}")


def example_get_service_account_by_id():
    """
    Example of using get_service_account_by_id

    Get service account by id.
    Retrieve the details of a service account by id.
    """
    try:
        # Prepare the request parameters
        service_account_id = "example_service_account_id"

        # Make the API call
        api_response = api_instance.get_service_account_by_id(
            service_account_id=service_account_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_service_account_by_id: {e}")


def example_get_service_accounts():
    """
    Example of using get_service_accounts

    Get a list of service accounts.
    Retrieve a list of service accounts.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_service_accounts()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_service_accounts: {e}")


def example_regenerate_service_account_secret():
    """
    Example of using regenerate_service_account_secret

    Regenerate a service account secret.
    Use to regenerate the service account secret by id.
    """
    try:
        # Prepare the request parameters
        service_account_id = "example_service_account_id"

        # Make the API call
        api_response = api_instance.regenerate_service_account_secret(
            service_account_id=service_account_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling regenerate_service_account_secret: {e}")


def example_update_service_account_by_id():
    """
    Example of using update_service_account_by_id

    Update service account details by id.
    Use to update the details of a service account by id.
    """
    try:
        # Prepare the request parameters
        service_account_id = "example_service_account_id"

        # Create example data for ServiceAccountPatchRequest
        service_account_patch_request = models.ServiceAccountPatchRequest(enabled=True)

        # Make the API call
        api_instance.update_service_account_by_id(
            service_account_id=service_account_id,
            service_account_patch_request=service_account_patch_request,
        )

    except Exception as e:
        print(f"Exception when calling update_service_account_by_id: {e}")
