# coding: utf-8

"""
    Test file for ClustersApi
    Generated by OpenAPI Generator with custom template
"""

import pytest
import unittest.mock as mock
from datetime import datetime, timezone
import json

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.models import *
from runai.exceptions import ApiException


class TestClustersApi:
    """Test cases for ClustersApi"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures"""
        self.configuration = Configuration(
            client_id="test-client",
            client_secret="test-secret",
            runai_base_url="https://test.run.ai",
        )
        self.api_client = ApiClient(self.configuration)
        self.api = ClustersApi(self.api_client)

        # Mock the request method
        self.request_patcher = mock.patch.object(self.api_client.rest_client, "request")
        self.mock_request = self.request_patcher.start()
        yield
        self.request_patcher.stop()

    def test_create_cluster(self):
        """Test case for create_cluster

        Create a cluster. Use to create a Kubernetes cluster.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        cluster_creation_request = (
            runai.ClusterCreationRequest()
        )  # ClusterCreationRequest | The cluster to create.

        # Make request
        response = self.api.create_cluster(
            cluster_creation_request=cluster_creation_request,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "POST"
        assert "/api/v1/clusters" in kwargs["url"]

        # Verify body
        assert kwargs["body"] is not None

        # Verify response
        assert isinstance(response, DisplayedCluster)

    def test_create_cluster_error(self):
        """Test error handling for create_cluster"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        cluster_creation_request = runai.ClusterCreationRequest()

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.create_cluster(
                cluster_creation_request=cluster_creation_request,
            )
        assert exc_info.value.status == 400

    def test_delete_cluster(self):
        """Test case for delete_cluster

        Delete a cluster. Use to delete a cluster by Universally Unique Identifier (UUID).
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({})
        self.mock_request.return_value = mock_response

        # Test parameters
        cluster_uuid = "9f55255e-11ed-47c7-acef-fc4054768dbc"  # str | The Universally Unique Identifier (UUID) of the cluster.

        # Make request
        self.api.delete_cluster(
            cluster_uuid=cluster_uuid,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "DELETE"
        assert "/api/v1/clusters/{clusterUuid}" in kwargs["url"]

    def test_delete_cluster_error(self):
        """Test error handling for delete_cluster"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        cluster_uuid = "9f55255e-11ed-47c7-acef-fc4054768dbc"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.delete_cluster(
                cluster_uuid=cluster_uuid,
            )
        assert exc_info.value.status == 400

    def test_get_cluster_by_uuid(self):
        """Test case for get_cluster_by_uuid

        Get cluster by id. Retrieve cluster details by Universally Unique Identifier (UUID).
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        cluster_uuid = "9f55255e-11ed-47c7-acef-fc4054768dbc"  # str | The Universally Unique Identifier (UUID) of the cluster.
        verbosity = full  # str | response verbosity level.

        # Make request
        response = self.api.get_cluster_by_uuid(
            cluster_uuid=cluster_uuid,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/clusters/{clusterUuid}" in kwargs["url"]

        # Verify query parameters
        assert "verbosity=" in kwargs["url"]

        # Verify response
        assert isinstance(response, DisplayedCluster)

    def test_get_cluster_by_uuid_error(self):
        """Test error handling for get_cluster_by_uuid"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        cluster_uuid = "9f55255e-11ed-47c7-acef-fc4054768dbc"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_cluster_by_uuid(
                cluster_uuid=cluster_uuid,
            )
        assert exc_info.value.status == 400

    def test_get_cluster_install_info_by_uuid(self):
        """Test case for get_cluster_install_info_by_uuid

        Retrieve the installation instructions of a cluster by ID. Use to retrieve installation instruction for a cluster by Universally Unique Identifier (UUID).  Supports clusters version 2.15 or above.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        cluster_uuid = "9f55255e-11ed-47c7-acef-fc4054768dbc"  # str | The Universally Unique Identifier (UUID) of the cluster.
        version = "2.16"  # str | The cluster version to install
        remote_cluster_url = (
            "https://cluster.runai"  # str | The remote URL of the runai cluster
        )

        # Make request
        response = self.api.get_cluster_install_info_by_uuid(
            cluster_uuid=cluster_uuid,
            version=version,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/clusters/{clusterUuid}/cluster-install-info" in kwargs["url"]

        # Verify query parameters
        assert "version=" in kwargs["url"]
        # Verify query parameters
        assert "remoteClusterUrl=" in kwargs["url"]

        # Verify response
        assert isinstance(response, ClusterInstallationInfoResponse)

    def test_get_cluster_install_info_by_uuid_error(self):
        """Test error handling for get_cluster_install_info_by_uuid"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        cluster_uuid = "9f55255e-11ed-47c7-acef-fc4054768dbc"
        version = "2.16"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_cluster_install_info_by_uuid(
                cluster_uuid=cluster_uuid,
                version=version,
            )
        assert exc_info.value.status == 400

    def test_get_cluster_metrics(self):
        """Test case for get_cluster_metrics

        Get the cluster metrics data. Retrieve the metrics data for a Kubernetes cluster by Universally Unique Identifier (UUID).
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        cluster_uuid = "9f55255e-11ed-47c7-acef-fc4054768dbc"  # str | The Universally Unique Identifier (UUID) of the cluster.
        start = "2023-06-06T12:09:18.211Z"  # datetime | Start date of time range to fetch data in ISO 8601 timestamp format.
        end = "2023-06-07T12:09:18.211Z"  # datetime | End date of time range to fetch data in ISO 8601 timestamp format.
        metric_type = [
            runai.MetricsType()
        ]  # List[MetricsType] | specifies what data to request
        number_of_samples = (
            20  # int | The number of samples to take in the specified time range.
        )

        # Make request
        response = self.api.get_cluster_metrics(
            cluster_uuid=cluster_uuid,
            start=start,
            end=end,
            metric_type=metric_type,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/clusters/{clusterUuid}/metrics" in kwargs["url"]

        # Verify query parameters
        assert "start=" in kwargs["url"]
        # Verify query parameters
        assert "end=" in kwargs["url"]
        # Verify query parameters
        assert "numberOfSamples=" in kwargs["url"]
        # Verify query parameters
        assert "metricType=" in kwargs["url"]

        # Verify response
        assert isinstance(response, MetricsResponse)

    def test_get_cluster_metrics_error(self):
        """Test error handling for get_cluster_metrics"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        cluster_uuid = "9f55255e-11ed-47c7-acef-fc4054768dbc"
        start = "2023-06-06T12:09:18.211Z"
        end = "2023-06-07T12:09:18.211Z"
        metric_type = [runai.MetricsType()]

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_cluster_metrics(
                cluster_uuid=cluster_uuid,
                start=start,
                end=end,
                metric_type=metric_type,
            )
        assert exc_info.value.status == 400

    def test_get_cluster_metrics_0(self):
        """Test case for get_cluster_metrics_0

        Get cluster metrics. Get current cluster metrics. If time range query parameters supplied, then historical data will be returned as well. Deprecated - please use api/v1/clusters/{clusterUuid}/metrics
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        cluster_uuid = "9f55255e-11ed-47c7-acef-fc4054768dbc"  # str | The Universally Unique Identifier (UUID) of the cluster.
        start = "2013-10-20T19:20:30+01:00"  # datetime | Start of time range to fetch data from in UTC format.
        end = "2013-10-20T19:20:30+01:00"  # datetime | End of time range to fetch data from in UTC format.
        number_of_samples = (
            20  # int | The number of samples to take in the specified time range.
        )
        nodepool_name = "default"  # str | Filter by unique nodepool name.

        # Make request
        response = self.api.get_cluster_metrics_0(
            cluster_uuid=cluster_uuid,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/v1/k8s/clusters/{clusterUuid}/metrics" in kwargs["url"]

        # Verify query parameters
        assert "start=" in kwargs["url"]
        # Verify query parameters
        assert "end=" in kwargs["url"]
        # Verify query parameters
        assert "numberOfSamples=" in kwargs["url"]
        # Verify query parameters
        assert "nodepoolName=" in kwargs["url"]

        # Verify response
        assert isinstance(response, Cluster)

    def test_get_cluster_metrics_0_error(self):
        """Test error handling for get_cluster_metrics_0"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        cluster_uuid = "9f55255e-11ed-47c7-acef-fc4054768dbc"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_cluster_metrics_0(
                cluster_uuid=cluster_uuid,
            )
        assert exc_info.value.status == 400

    def test_get_clusters(self):
        """Test case for get_clusters

        Get a list of clusters. Retrieve a list of clusters with details.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        verbosity = full  # str | response verbosity level.

        # Make request
        response = self.api.get_clusters()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/clusters" in kwargs["url"]

        # Verify query parameters
        assert "verbosity=" in kwargs["url"]

        # Verify response
        assert isinstance(response, List[DisplayedCluster])

    def test_get_clusters_error(self):
        """Test error handling for get_clusters"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_clusters()
        assert exc_info.value.status == 400

    def test_get_install_file(self):
        """Test case for get_install_file

        Get cluster installation file by id. Retrieve the installation values file of a cluster by Retrieve the installation values file of a given cluster by ID.  Supports clusters 2.13 and lower.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        cluster_uuid = "cluster_uuid_example"  # str | Unique identifier of the cluster.
        cloud = "cloud_example"  # str | Cloud type identifier.
        clusterip = "clusterip_example"  # str | Comma-separated list of IP addresses that provide access to the cluster.
        format = yaml  # str | Format of the output file.

        # Make request
        response = self.api.get_install_file(
            cluster_uuid=cluster_uuid,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/v1/k8s/clusters/{cluster_uuid}/installfile" in kwargs["url"]

        # Verify query parameters
        assert "cloud=" in kwargs["url"]
        # Verify query parameters
        assert "clusterip=" in kwargs["url"]
        # Verify query parameters
        assert "format=" in kwargs["url"]

        # Verify response
        assert isinstance(response, str)

    def test_get_install_file_error(self):
        """Test error handling for get_install_file"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        cluster_uuid = "cluster_uuid_example"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_install_file(
                cluster_uuid=cluster_uuid,
            )
        assert exc_info.value.status == 400

    def test_update_cluster(self):
        """Test case for update_cluster

        Update a cluster by id. Use to update the details of a Kubernetes cluster by Universally Unique Identifier (UUID).
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({})
        self.mock_request.return_value = mock_response

        # Test parameters
        cluster_uuid = "9f55255e-11ed-47c7-acef-fc4054768dbc"  # str | The Universally Unique Identifier (UUID) of the cluster.
        cluster_update_request = (
            runai.ClusterUpdateRequest()
        )  # ClusterUpdateRequest | The cluster details to update

        # Make request
        self.api.update_cluster(
            cluster_uuid=cluster_uuid,
            cluster_update_request=cluster_update_request,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "PUT"
        assert "/api/v1/clusters/{clusterUuid}" in kwargs["url"]

        # Verify body
        assert kwargs["body"] is not None

    def test_update_cluster_error(self):
        """Test error handling for update_cluster"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        cluster_uuid = "9f55255e-11ed-47c7-acef-fc4054768dbc"
        cluster_update_request = runai.ClusterUpdateRequest()

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.update_cluster(
                cluster_uuid=cluster_uuid,
                cluster_update_request=cluster_update_request,
            )
        assert exc_info.value.status == 400
