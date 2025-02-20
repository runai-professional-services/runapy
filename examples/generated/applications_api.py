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

    Create a new app.
    Create a new app and assign it with a client secret. This endpoint requires ADMIN role. Deprecated in favor of the new endpoint api/v1/apps.
    """
    try:
        # Prepare the request parameters

        # Create example data for App
        app = models.App()

        # Make the API call
        api_response = api_instance.create_application(
            app=app,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_application: {e}")


def example_create_application_0():
    """
    Example of using create_application_0

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
        api_response = api_instance.create_application_0(
            application_creation_request=application_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_application_0: {e}")


def example_delete_application_by_id():
    """
    Example of using delete_application_by_id

    Delete a App.
    Delete the given app from the tenant. This endpoint requires ADMIN role. Deprecated in favor of the new endpoint api/v1/apps/{clientId}.
    """
    try:
        # Prepare the request parameters
        client_id = "example_client_id"

        # Make the API call
        api_instance.delete_application_by_id(
            client_id=client_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_application_by_id: {e}")


def example_delete_application_by_id_0():
    """
    Example of using delete_application_by_id_0

    Delete an application by id.
    Use to delete an application by id.
    """
    try:
        # Prepare the request parameters
        app_id = "example_app_id"

        # Make the API call
        api_instance.delete_application_by_id_0(
            app_id=app_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_application_by_id_0: {e}")


def example_get_application_by_id():
    """
    Example of using get_application_by_id

    Get app details.
    Get the details of a given app. This endpoint requires ADMIN, EDITOR or VIEWER role. Deprecated in favor of the new endpoint api/v1/apps/{clientId}.
    """
    try:
        # Prepare the request parameters
        client_id = "example_client_id"

        # Make the API call
        api_response = api_instance.get_application_by_id(
            client_id=client_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_application_by_id: {e}")


def example_get_application_by_id_0():
    """
    Example of using get_application_by_id_0

    Get application by id.
    Retrieve the details of an application by id.
    """
    try:
        # Prepare the request parameters
        app_id = "example_app_id"

        # Make the API call
        api_response = api_instance.get_application_by_id_0(
            app_id=app_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_application_by_id_0: {e}")


def example_get_applications():
    """
    Example of using get_applications

    Get Apps list.
    Return the list of apps of the tenant. Deprecated in favor of the new endpoint api/v1/apps.
    """
    try:
        # Prepare the request parameters

        roles = ["example_item_1", "example_item_2"]

        only_created_by_me = True

        # Make the API call
        api_response = api_instance.get_applications(
            roles=roles,
            only_created_by_me=only_created_by_me,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_applications: {e}")


def example_get_applications_0():
    """
    Example of using get_applications_0

    Get a list of applications.
    Retrieve a list of applications.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_applications_0()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_applications_0: {e}")


def example_get_installer_app():
    """
    Example of using get_installer_app

    Get a list of installer applications.
    Retrieve a list of installer applications.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_installer_app()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_installer_app: {e}")


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


def example_reset_app_secret():
    """
    Example of using reset_app_secret

    Re-generate secret of application.
    Generate a new secret for a given application. This endpoint requires ADMIN role. Deprecated in favor of the new endpoint api/v1/apps/{clientId}/secret.
    """
    try:
        # Prepare the request parameters
        client_id = "example_client_id"

        # Make the API call
        api_response = api_instance.reset_app_secret(
            client_id=client_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling reset_app_secret: {e}")


def example_update_application_by_id():
    """
    Example of using update_application_by_id

    Update app details.
    Update the details of a given app. This endpoint requires ADMIN role. Deprecated in favor of the new endpoint api/v1/apps/{clientId}.
    """
    try:
        # Prepare the request parameters
        client_id = "example_client_id"

        # Create example data for App
        app = models.App()

        # Make the API call
        api_response = api_instance.update_application_by_id(
            client_id=client_id,
            app=app,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_application_by_id: {e}")


def example_update_application_by_id_0():
    """
    Example of using update_application_by_id_0

    Update application details by id.
    Use to update the details of an application by id.
    """
    try:
        # Prepare the request parameters
        app_id = "example_app_id"

        # Create example data for ApplicationPatchRequest
        application_patch_request = models.ApplicationPatchRequest(enabled=True)

        # Make the API call
        api_instance.update_application_by_id_0(
            app_id=app_id,
            application_patch_request=application_patch_request,
        )

    except Exception as e:
        print(f"Exception when calling update_application_by_id_0: {e}")
