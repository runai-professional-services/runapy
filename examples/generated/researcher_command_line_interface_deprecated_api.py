"""
Examples for using the ResearcherCommandLineInterfaceDeprecatedApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import ResearcherCommandLineInterfaceDeprecatedApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = ResearcherCommandLineInterfaceDeprecatedApi(api_client)


def example_get_binary_deprecated():
    """
    Example of using get_binary_deprecated

    Download RunAI Researcher command line binary
    This endpoint returns a binary file that run the Run:ai CLI.
    """
    try:
        # Prepare the request parameters
        operating_system = "example_operating_system"

        architecture = "example_architecture"

        # Make the API call
        api_response = api_instance.get_binary_deprecated(
            operating_system=operating_system,
            architecture=architecture,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_binary_deprecated: {e}")


def example_get_installer_linux_commands_deprecated():
    """
    Example of using get_installer_linux_commands_deprecated

    Get Linux installer script commands
    This endpoint returns a linux script commands that can be used to install the Run:ai CLI.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_installer_linux_commands_deprecated()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_installer_linux_commands_deprecated: {e}")


def example_get_installer_linux_deprecated():
    """
    Example of using get_installer_linux_deprecated

    Download Linux installer script
    This endpoint returns a Linux script that can be used to install the Run:ai CLI.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_installer_linux_deprecated()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_installer_linux_deprecated: {e}")


def example_get_installer_mac_commands_deprecated():
    """
    Example of using get_installer_mac_commands_deprecated

    Get Mac installer script commands
    This endpoint returns a Mac script commands that can be used to install the Run:ai CLI.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_installer_mac_commands_deprecated()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_installer_mac_commands_deprecated: {e}")


def example_get_installer_mac_deprecated():
    """
    Example of using get_installer_mac_deprecated

    Download Mac installer script
    This endpoint returns a Mac script that can be used to install the Run:ai CLI.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_installer_mac_deprecated()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_installer_mac_deprecated: {e}")


def example_get_installer_unix_commands_deprecated():
    """
    Example of using get_installer_unix_commands_deprecated

    Get Unix installer script commands
    This endpoint returns a unix script commands that can be used to install the Run:ai CLI.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_installer_unix_commands_deprecated()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_installer_unix_commands_deprecated: {e}")


def example_get_installer_unix_deprecated():
    """
    Example of using get_installer_unix_deprecated

    Download Unix installer script
    This endpoint returns a unix script that can be used to install the Run:ai CLI.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_installer_unix_deprecated()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_installer_unix_deprecated: {e}")


def example_get_installer_windows_commands_deprecated():
    """
    Example of using get_installer_windows_commands_deprecated

    Get Windows MSI installer script commands
    This endpoint returns a windows script commands that can be used to install the Run:ai CLI.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_installer_windows_commands_deprecated()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_installer_windows_commands_deprecated: {e}")


def example_get_manual_document_deprecated():
    """
    Example of using get_manual_document_deprecated

    Get CLI document by name
    This endpoint returns a document of help for the Run:ai CLI.
    """
    try:
        # Prepare the request parameters
        document_name = "example_document_name"

        # Make the API call
        api_response = api_instance.get_manual_document_deprecated(
            document_name=document_name,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_manual_document_deprecated: {e}")
