"""
Examples for using the ApplicationsApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import ApplicationsApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = ApplicationsApi(api_client)


def example_create_application():
    """
    Example of using create_application

    Create an application.
    Used to create an application.
    """
    try:
        # Prepare the request parameters

        # Create example data for ApplicationCreationRequest
        application_creation_request = models.ApplicationCreationRequest(
            name="awat5ikwowtta-3mh2lcafqw3zhes0"
        )

        # Make the API call
        api_response = api_instance.create_application(
            application_creation_request=application_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_application: {e}")


def example_delete_application_by_id():
    """
    Example of using delete_application_by_id

    Delete an application by id.
    Use to delete an application by id.
    """
    try:
        # Prepare the request parameters
        app_id = "example_app_id"

        # Make the API call
        api_instance.delete_application_by_id(
            app_id=app_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_application_by_id: {e}")


def example_get_application_by_id():
    """
    Example of using get_application_by_id

    Get application by id.
    Retrieve the details of an application by id.
    """
    try:
        # Prepare the request parameters
        app_id = "example_app_id"

        # Make the API call
        api_response = api_instance.get_application_by_id(
            app_id=app_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_application_by_id: {e}")


def example_get_applications():
    """
    Example of using get_applications

    Get a list of applications.
    Retrieve a list of applications.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_applications()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_applications: {e}")


def example_regenerate_application_secret():
    """
    Example of using regenerate_application_secret

    Regenerate an application secret.
    Use to regenerate the application secret by id.
    """
    try:
        # Prepare the request parameters
        app_id = "example_app_id"

        # Make the API call
        api_response = api_instance.regenerate_application_secret(
            app_id=app_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling regenerate_application_secret: {e}")


def example_update_application_by_id():
    """
    Example of using update_application_by_id

    Update application details by id.
    Use to update the details of an application by id.
    """
    try:
        # Prepare the request parameters
        app_id = "example_app_id"

        # Create example data for ApplicationPatchRequest
        application_patch_request = models.ApplicationPatchRequest(enabled=True)

        # Make the API call
        api_instance.update_application_by_id(
            app_id=app_id,
            application_patch_request=application_patch_request,
        )

    except Exception as e:
        print(f"Exception when calling update_application_by_id: {e}")
