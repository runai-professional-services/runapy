"""
Examples for using the AccessKeysApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import AccessKeysApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = AccessKeysApi(api_client)


def example_create_access_key1():
    """
    Example of using create_access_key1

    Create an access key.
    Used to create an access key.
    """
    try:
        # Prepare the request parameters

        # Create example data for AccessKeyCreationRequest1
        access_key_creation_request1 = models.AccessKeyCreationRequest1(
            name="awat5ikwowtta-3mh2lcafqw3zhes0"
        )

        # Make the API call
        api_response = api_instance.create_access_key1(
            access_key_creation_request1=access_key_creation_request1,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_access_key1: {e}")


def example_delete_access_key_by_id():
    """
    Example of using delete_access_key_by_id

    Delete an access key by id.
    Use to delete an access key by id.
    """
    try:
        # Prepare the request parameters
        access_key_id = "example_access_key_id"

        # Make the API call
        api_instance.delete_access_key_by_id(
            access_key_id=access_key_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_access_key_by_id: {e}")


def example_delete_access_key_by_id_administration():
    """
    Example of using delete_access_key_by_id_administration

    Delete an access key by id for administrations.
    Use to delete an access key by id for administrations.
    """
    try:
        # Prepare the request parameters
        access_key_id = "example_access_key_id"

        # Make the API call
        api_instance.delete_access_key_by_id_administration(
            access_key_id=access_key_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_access_key_by_id_administration: {e}")


def example_get_access_key_by_id1():
    """
    Example of using get_access_key_by_id1

    Get access key by id.
    Retrieve the details of an access key by id.
    """
    try:
        # Prepare the request parameters
        access_key_id = "example_access_key_id"

        # Make the API call
        api_response = api_instance.get_access_key_by_id1(
            access_key_id=access_key_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_access_key_by_id1: {e}")


def example_get_access_keys():
    """
    Example of using get_access_keys

    Get a list of access keys.
    Retrieve a list of the user&#39;s access keys.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_access_keys()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_access_keys: {e}")


def example_get_access_keys_administration():
    """
    Example of using get_access_keys_administration

    Get a list of all access keys.
    Retrieve a list of all access keys.
    """
    try:
        # Prepare the request parameters
        client_id = "example_client_id"

        created_by = "example_created_by"

        # Make the API call
        api_response = api_instance.get_access_keys_administration(
            client_id=client_id,
            created_by=created_by,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_access_keys_administration: {e}")


def example_regenerate_access_key_secret():
    """
    Example of using regenerate_access_key_secret

    Regenerate an access key secret.
    Use to regenerate the access key secret by id.
    """
    try:
        # Prepare the request parameters
        access_key_id = "example_access_key_id"

        # Make the API call
        api_response = api_instance.regenerate_access_key_secret(
            access_key_id=access_key_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling regenerate_access_key_secret: {e}")
