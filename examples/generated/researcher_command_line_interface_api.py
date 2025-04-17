"""
Examples for using the ResearcherCommandLineInterfaceApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import ResearcherCommandLineInterfaceApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = ResearcherCommandLineInterfaceApi(api_client)


def example_get_binary():
    """
    Example of using get_binary

    Download RunAI Researcher command line binary
    This endpoint returns a binary file that run the Run:ai CLI.
    """
    try:
        # Prepare the request parameters
        operating_system = "example_operating_system"

        architecture = "example_architecture"

        # Make the API call
        api_response = api_instance.get_binary(
            operating_system=operating_system,
            architecture=architecture,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_binary: {e}")


def example_get_installer_linux():
    """
    Example of using get_installer_linux

    Download Linux installer script
    This endpoint returns a Linux script that can be used to install the Run:ai CLI.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_installer_linux()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_installer_linux: {e}")


def example_get_installer_linux_commands():
    """
    Example of using get_installer_linux_commands

    Get Linux installer script commands
    This endpoint returns a linux script commands that can be used to install the Run:ai CLI.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_installer_linux_commands()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_installer_linux_commands: {e}")


def example_get_installer_mac():
    """
    Example of using get_installer_mac

    Download Mac installer script
    This endpoint returns a Mac script that can be used to install the Run:ai CLI.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_installer_mac()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_installer_mac: {e}")


def example_get_installer_mac_commands():
    """
    Example of using get_installer_mac_commands

    Get Mac installer script commands
    This endpoint returns a Mac script commands that can be used to install the Run:ai CLI.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_installer_mac_commands()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_installer_mac_commands: {e}")


def example_get_installer_unix():
    """
    Example of using get_installer_unix

    Download Unix installer script
    This endpoint returns a unix script that can be used to install the Run:ai CLI.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_installer_unix()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_installer_unix: {e}")


def example_get_installer_unix_commands():
    """
    Example of using get_installer_unix_commands

    Get Unix installer script commands
    This endpoint returns a unix script commands that can be used to install the Run:ai CLI.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_installer_unix_commands()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_installer_unix_commands: {e}")


def example_get_installer_windows_commands():
    """
    Example of using get_installer_windows_commands

    Get Windows MSI installer script commands
    This endpoint returns a windows script commands that can be used to install the Run:ai CLI.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_installer_windows_commands()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_installer_windows_commands: {e}")


def example_get_manual_document():
    """
    Example of using get_manual_document

    Get CLI document by name
    This endpoint returns a document of help for the Run:ai CLI.
    """
    try:
        # Prepare the request parameters
        document_name = "example_document_name"

        # Make the API call
        api_response = api_instance.get_manual_document(
            document_name=document_name,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_manual_document: {e}")
