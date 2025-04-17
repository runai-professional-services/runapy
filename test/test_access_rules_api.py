# coding: utf-8

"""
Run:ai API

# Introduction  The Run:ai Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: latest
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from runai.api.access_rules_api import AccessRulesApi


class TestAccessRulesApi(unittest.TestCase):
    """AccessRulesApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AccessRulesApi()

    def tearDown(self) -> None:
        pass

    def test_access_rules_batch(self) -> None:
        """Test case for access_rules_batch

        Access Rules batch delete operation.
        """
        pass

    def test_count_access_rules(self) -> None:
        """Test case for count_access_rules

        Count access rules.
        """
        pass

    def test_create_access_rule(self) -> None:
        """Test case for create_access_rule

        Create an access rule.
        """
        pass

    def test_delete_access_rule(self) -> None:
        """Test case for delete_access_rule

        Delete an access rule.
        """
        pass

    def test_get_access_rule(self) -> None:
        """Test case for get_access_rule

        Get an access rule.
        """
        pass

    def test_get_access_rules(self) -> None:
        """Test case for get_access_rules

        List the access rules.
        """
        pass


if __name__ == "__main__":
    unittest.main()
