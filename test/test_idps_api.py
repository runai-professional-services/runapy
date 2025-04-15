# coding: utf-8

"""
Runai API

# Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: 2.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from runai.api.idps_api import IdpsApi


class TestIdpsApi(unittest.TestCase):
    """IdpsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = IdpsApi()

    def tearDown(self) -> None:
        pass

    def test_create_idp(self) -> None:
        """Test case for create_idp

        Configure external idp
        """
        pass

    def test_delete_idp(self) -> None:
        """Test case for delete_idp

        Delete external idp by alias
        """
        pass

    def test_get_idp(self) -> None:
        """Test case for get_idp

        Get external idp by alias
        """
        pass

    def test_get_idp_mappers(self) -> None:
        """Test case for get_idp_mappers

        Get idp mappers
        """
        pass

    def test_get_idps(self) -> None:
        """Test case for get_idps

        Get external idps list
        """
        pass

    def test_update_idp(self) -> None:
        """Test case for update_idp

        Update external idp by alias
        """
        pass

    def test_update_idp_mappers(self) -> None:
        """Test case for update_idp_mappers

        Update idp mappers
        """
        pass


if __name__ == "__main__":
    unittest.main()
