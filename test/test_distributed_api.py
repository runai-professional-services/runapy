# coding: utf-8

"""
Run:ai API

# Introduction  The Run:ai Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: latest
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from runai.api.distributed_api import DistributedApi


class TestDistributedApi(unittest.TestCase):
    """DistributedApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DistributedApi()

    def tearDown(self) -> None:
        pass

    def test_create_distributed(self) -> None:
        """Test case for create_distributed

        Create a distributed training.
        """
        pass

    def test_delete_distributed(self) -> None:
        """Test case for delete_distributed

        Delete a distributed training by id.
        """
        pass

    def test_get_distributed(self) -> None:
        """Test case for get_distributed

        Get distributed training's data. [Experimental]
        """
        pass

    def test_resume_distributed(self) -> None:
        """Test case for resume_distributed

        Resume a distributed training.
        """
        pass

    def test_suspend_distributed(self) -> None:
        """Test case for suspend_distributed

        Suspend a distributed training.
        """
        pass


if __name__ == "__main__":
    unittest.main()
