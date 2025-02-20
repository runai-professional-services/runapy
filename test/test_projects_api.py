# coding: utf-8

"""
    Runai API

    # Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token). 

    The version of the OpenAPI document: 2.18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from runai.api.projects_api import ProjectsApi


class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ProjectsApi()

    def tearDown(self) -> None:
        pass

    def test_create_project(self) -> None:
        """Test case for create_project

        Create project
        """
        pass

    def test_create_project_0(self) -> None:
        """Test case for create_project_0

        Create a new project.
        """
        pass

    def test_delete_project(self) -> None:
        """Test case for delete_project

        Delete project
        """
        pass

    def test_delete_project_0(self) -> None:
        """Test case for delete_project_0

        Delete a project.
        """
        pass

    def test_get_project(self) -> None:
        """Test case for get_project

        Get project
        """
        pass

    def test_get_project_0(self) -> None:
        """Test case for get_project_0

        List details of a specific project.
        """
        pass

    def test_get_project_metrics(self) -> None:
        """Test case for get_project_metrics

        Get metrics data for a specific project.
        """
        pass

    def test_get_projects(self) -> None:
        """Test case for get_projects

        Get projects
        """
        pass

    def test_get_projects_0(self) -> None:
        """Test case for get_projects_0

        List all projects and their details.
        """
        pass

    def test_get_projects_metrics(self) -> None:
        """Test case for get_projects_metrics

        Get metrics data for all projects.
        """
        pass

    def test_patch_project_resources(self) -> None:
        """Test case for patch_project_resources

        Patch project resources
        """
        pass

    def test_update_project(self) -> None:
        """Test case for update_project

        Update project
        """
        pass

    def test_update_project_0(self) -> None:
        """Test case for update_project_0

        Update a project.
        """
        pass

    def test_update_project_resources(self) -> None:
        """Test case for update_project_resources

        Update project resources
        """
        pass


if __name__ == "__main__":
    unittest.main()
