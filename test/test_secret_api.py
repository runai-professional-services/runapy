# coding: utf-8

"""
Runai API

# Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: 2.19
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from runai.api.secret_api import SecretApi


class TestSecretApi(unittest.TestCase):
    """SecretApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SecretApi()

    def tearDown(self) -> None:
        pass

    def test_create_secret_asset(self) -> None:
        """Test case for create_secret_asset

        Create a Secret datasource asset.
        """
        pass

    def test_delete_secret_asset_by_id(self) -> None:
        """Test case for delete_secret_asset_by_id

        Delete a Secret asset.
        """
        pass

    def test_get_secret_asset_by_id(self) -> None:
        """Test case for get_secret_asset_by_id

        Get a Secret asset.
        """
        pass

    def test_list_secret_assets(self) -> None:
        """Test case for list_secret_assets

        List Secret datasource assets.
        """
        pass

    def test_update_secret_asset_by_id(self) -> None:
        """Test case for update_secret_asset_by_id

        Update a Secret asset.
        """
        pass


if __name__ == "__main__":
    unittest.main()
