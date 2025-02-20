"""
Examples for using the AdministratorCommandLineInterfaceApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import AdministratorCommandLineInterfaceApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = AdministratorCommandLineInterfaceApi(api_client)


def example_get_admin_cli_release():
    """
    Example of using get_admin_cli_release

    Get Administrator Command Line Interface release.
    Retrieve the Administrator Command Line Interface version.
    """
    try:
        # Prepare the request parameters
        os = "example_os"

        # Make the API call
        api_response = api_instance.get_admin_cli_release(
            os=os,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_admin_cli_release: {e}")


def example_get_admin_cli_release_by_version():
    """
    Example of using get_admin_cli_release_by_version

    Get Administrator Command Line Interface release by version.
    Retrieve the Administrator Command Line Interface release by version.
    """
    try:
        # Prepare the request parameters
        os = "example_os"

        version = "example_version"

        # Make the API call
        api_response = api_instance.get_admin_cli_release_by_version(
            os=os,
            version=version,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_admin_cli_release_by_version: {e}")


def example_get_admin_cli_release_by_version_checksum():
    """
    Example of using get_admin_cli_release_by_version_checksum

    Get Administrator Command Line Interface release checksums.
    Retrieve the checksums of the Administrator Command Line Interface release.
    """
    try:
        # Prepare the request parameters
        os = "example_os"

        version = "example_version"

        # Make the API call
        api_response = api_instance.get_admin_cli_release_by_version_checksum(
            os=os,
            version=version,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_admin_cli_release_by_version_checksum: {e}")


def example_get_admin_cli_release_checksum():
    """
    Example of using get_admin_cli_release_checksum

    Get Administrator Command Line Interface release details.
    Retrieve the details of the Administrator Command Line Interface release.
    """
    try:
        # Prepare the request parameters
        os = "example_os"

        # Make the API call
        api_response = api_instance.get_admin_cli_release_checksum(
            os=os,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_admin_cli_release_checksum: {e}")
