# coding: utf-8

"""
Runai API

# Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: 2.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from runai.api.reports_api import ReportsApi


class TestReportsApi(unittest.TestCase):
    """ReportsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ReportsApi()

    def tearDown(self) -> None:
        pass

    def test_are_reports_available(self) -> None:
        """Test case for are_reports_available

        Reports availability
        """
        pass

    def test_count_reports(self) -> None:
        """Test case for count_reports

        Count reports
        """
        pass

    def test_create_report(self) -> None:
        """Test case for create_report

        Create a new report request.
        """
        pass

    def test_delete_report_by_id(self) -> None:
        """Test case for delete_report_by_id

        Delete report
        """
        pass

    def test_download_report_by_id(self) -> None:
        """Test case for download_report_by_id

        Download report
        """
        pass

    def test_get_report_by_id(self) -> None:
        """Test case for get_report_by_id

        Get report
        """
        pass

    def test_list_reports(self) -> None:
        """Test case for list_reports

        List reports
        """
        pass


if __name__ == "__main__":
    unittest.main()
