# coding: utf-8

"""
Run:ai API

# Introduction  The Run:ai Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: latest
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from runai.api.notification_state_api import NotificationStateApi


class TestNotificationStateApi(unittest.TestCase):
    """NotificationStateApi unit test stubs"""

    def setUp(self) -> None:
        self.api = NotificationStateApi()

    def tearDown(self) -> None:
        pass

    def test_get_notification_state(self) -> None:
        """Test case for get_notification_state

        Get notification state
        """
        pass

    def test_update_notification_state(self) -> None:
        """Test case for update_notification_state

        Update notification state
        """
        pass


if __name__ == "__main__":
    unittest.main()
