# coding: utf-8

"""
Run:ai API

# Introduction  The Run:ai Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: latest
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from runai.api.pods_api import PodsApi


class TestPodsApi(unittest.TestCase):
    """PodsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PodsApi()

    def tearDown(self) -> None:
        pass

    def test_count_pods(self) -> None:
        """Test case for count_pods

        Get pods count.
        """
        pass

    def test_get_pods(self) -> None:
        """Test case for get_pods

        get all pods from a specific cluster. Deprecated - please use api/v1/workloads/pods instead
        """
        pass

    def test_get_revision_pods(self) -> None:
        """Test case for get_revision_pods

        Get revision pods by id. [Experimental]
        """
        pass

    def test_get_workload_pod_metrics(self) -> None:
        """Test case for get_workload_pod_metrics

        Get pod metrics data.
        """
        pass

    def test_get_workload_pods(self) -> None:
        """Test case for get_workload_pods

        Get workload pods by id.
        """
        pass

    def test_list_pods(self) -> None:
        """Test case for list_pods

        List pods.
        """
        pass


if __name__ == "__main__":
    unittest.main()
