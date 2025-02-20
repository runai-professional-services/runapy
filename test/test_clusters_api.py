# coding: utf-8

"""
Runai API

# Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: 2.19
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from runai.api.clusters_api import ClustersApi


class TestClustersApi(unittest.TestCase):
    """ClustersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ClustersApi()

    def tearDown(self) -> None:
        pass

    def test_create_cluster(self) -> None:
        """Test case for create_cluster

        Create a cluster.
        """
        pass

    def test_delete_cluster(self) -> None:
        """Test case for delete_cluster

        Delete a cluster by id.
        """
        pass

    def test_get_cluster_by_uuid(self) -> None:
        """Test case for get_cluster_by_uuid

        Get cluster by id.
        """
        pass

    def test_get_cluster_install_info_by_uuid(self) -> None:
        """Test case for get_cluster_install_info_by_uuid

        Retrieve the installation instructions of a cluster by ID.
        """
        pass

    def test_get_cluster_metrics(self) -> None:
        """Test case for get_cluster_metrics

        Get the cluster metrics data.
        """
        pass

    def test_get_cluster_metrics_0(self) -> None:
        """Test case for get_cluster_metrics_0

        Get cluster metrics.
        """
        pass

    def test_get_clusters(self) -> None:
        """Test case for get_clusters

        Get a list of clusters.
        """
        pass

    def test_get_install_file(self) -> None:
        """Test case for get_install_file

        Get cluster installation file by id.
        """
        pass

    def test_update_cluster(self) -> None:
        """Test case for update_cluster

        Update a cluster by id.
        """
        pass


if __name__ == "__main__":
    unittest.main()
