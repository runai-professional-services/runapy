# coding: utf-8

"""
Run:ai API

# Introduction  The Run:ai Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: latest
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from runai.api.workspaces_api import WorkspacesApi


class TestWorkspacesApi(unittest.TestCase):
    """WorkspacesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = WorkspacesApi()

    def tearDown(self) -> None:
        pass

    def test_create_workspace1(self) -> None:
        """Test case for create_workspace1

        Create a workspace.
        """
        pass

    def test_delete_workspace(self) -> None:
        """Test case for delete_workspace

        Delete a workspace.
        """
        pass

    def test_get_workspace(self) -> None:
        """Test case for get_workspace

        Get workspace data.
        """
        pass

    def test_resume_workspace(self) -> None:
        """Test case for resume_workspace

        Resume a workspace.
        """
        pass

    def test_suspend_workspace(self) -> None:
        """Test case for suspend_workspace

        Suspend a workspace.
        """
        pass


if __name__ == "__main__":
    unittest.main()
