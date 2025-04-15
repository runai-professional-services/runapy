# coding: utf-8

"""
Runai API

# Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: 2.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from runai.api.researcher_command_line_interface_deprecated_api import (
    ResearcherCommandLineInterfaceDeprecatedApi,
)


class TestResearcherCommandLineInterfaceDeprecatedApi(unittest.TestCase):
    """ResearcherCommandLineInterfaceDeprecatedApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ResearcherCommandLineInterfaceDeprecatedApi()

    def tearDown(self) -> None:
        pass

    def test_get_binary_deprecated(self) -> None:
        """Test case for get_binary_deprecated

        Download RunAI Researcher command line binary
        """
        pass

    def test_get_installer_linux_commands_deprecated(self) -> None:
        """Test case for get_installer_linux_commands_deprecated

        Get Linux installer script commands
        """
        pass

    def test_get_installer_linux_deprecated(self) -> None:
        """Test case for get_installer_linux_deprecated

        Download Linux installer script
        """
        pass

    def test_get_installer_mac_commands_deprecated(self) -> None:
        """Test case for get_installer_mac_commands_deprecated

        Get Mac installer script commands
        """
        pass

    def test_get_installer_mac_deprecated(self) -> None:
        """Test case for get_installer_mac_deprecated

        Download Mac installer script
        """
        pass

    def test_get_installer_unix_commands_deprecated(self) -> None:
        """Test case for get_installer_unix_commands_deprecated

        Get Unix installer script commands
        """
        pass

    def test_get_installer_unix_deprecated(self) -> None:
        """Test case for get_installer_unix_deprecated

        Download Unix installer script
        """
        pass

    def test_get_installer_windows_commands_deprecated(self) -> None:
        """Test case for get_installer_windows_commands_deprecated

        Get Windows MSI installer script commands
        """
        pass

    def test_get_manual_document_deprecated(self) -> None:
        """Test case for get_manual_document_deprecated

        Get CLI document by name
        """
        pass


if __name__ == "__main__":
    unittest.main()
