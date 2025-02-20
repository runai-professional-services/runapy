"""
Examples for using the UserApplicationsApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import UserApplicationsApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = UserApplicationsApi(api_client)


def example_create_user_application():
    """
    Example of using create_user_application

    Create a user application.
    Used to create a user application.
    """
    try:
        # Prepare the request parameters

        # Create example data for UserAppCreationRequest
        user_app_creation_request = models.UserAppCreationRequest(
            name="awat5ikwowtta-3mh2lcafqw3zhes0"
        )

        # Make the API call
        api_response = api_instance.create_user_application(
            user_app_creation_request=user_app_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_user_application: {e}")


def example_delete_user_application_by_id():
    """
    Example of using delete_user_application_by_id

    Delete a user application byid.
    Use to user a user application by id.
    """
    try:
        # Prepare the request parameters
        app_id = "example_app_id"

        # Make the API call
        api_instance.delete_user_application_by_id(
            app_id=app_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_user_application_by_id: {e}")


def example_delete_user_application_by_id_administration():
    """
    Example of using delete_user_application_by_id_administration

    Delete a user application by id for adminstrations.
    Use to delete a user application by id for adminstrations.
    """
    try:
        # Prepare the request parameters
        app_id = "example_app_id"

        # Make the API call
        api_instance.delete_user_application_by_id_administration(
            app_id=app_id,
        )

    except Exception as e:
        print(
            f"Exception when calling delete_user_application_by_id_administration: {e}"
        )


def example_get_user_application_by_id():
    """
    Example of using get_user_application_by_id

    Get user application by id.
    Retrieve the details of a user&#39;s application by app id.
    """
    try:
        # Prepare the request parameters
        app_id = "example_app_id"

        # Make the API call
        api_response = api_instance.get_user_application_by_id(
            app_id=app_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_user_application_by_id: {e}")


def example_get_user_applications():
    """
    Example of using get_user_applications

    Get a list of users applications.
    Retrieve a list of the users applications.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_user_applications()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_user_applications: {e}")


def example_get_user_applications_administration():
    """
    Example of using get_user_applications_administration

    Get a list of all users applications.
    Retrieve a list of all users applications.
    """
    try:
        # Prepare the request parameters
        client_id = "example_client_id"

        created_by = "example_created_by"

        # Make the API call
        api_response = api_instance.get_user_applications_administration(
            client_id=client_id,
            created_by=created_by,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_user_applications_administration: {e}")


def example_regenerate_user_application_secret():
    """
    Example of using regenerate_user_application_secret

    Regenerate a user application secret.
    Use to regenerate the user application secret by id.
    """
    try:
        # Prepare the request parameters
        app_id = "example_app_id"

        # Make the API call
        api_response = api_instance.regenerate_user_application_secret(
            app_id=app_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling regenerate_user_application_secret: {e}")
