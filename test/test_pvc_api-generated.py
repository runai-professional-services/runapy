# coding: utf-8

"""
Test file for PVCApi
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


class TestPVCApi:
    """Test cases for PVCApi"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures"""
        self.configuration = Configuration(
            client_id="test-client",
            client_secret="test-secret",
            runai_base_url="https://test.run.ai",
        )
        self.api_client = ApiClient(self.configuration)
        self.api = PVCApi(self.api_client)

        # Mock the request method
        self.request_patcher = mock.patch.object(self.api_client.rest_client, "request")
        self.mock_request = self.request_patcher.start()
        yield
        self.request_patcher.stop()

    def test_create_pvc_asset(self):
        """Test case for create_pvc_asset

        Create a PVC asset. Use to create a PVC datasource asset.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        pvc_creation_request = runai.PVCCreationRequest()  # PVCCreationRequest |

        # Make request
        response = self.api.create_pvc_asset()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "POST"
        assert "/api/v1/asset/datasource/pvc" in kwargs["url"]

        # Verify body
        assert kwargs["body"] is not None

        # Verify response
        assert isinstance(response, PVCAsset)

    def test_create_pvc_asset_error(self):
        """Test error handling for create_pvc_asset"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.create_pvc_asset()
        assert exc_info.value.status == 400

    def test_delete_pvc_asset_by_id(self):
        """Test case for delete_pvc_asset_by_id

        Delete a PVC asset. Use to delete a PVC datasource asset by id.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        asset_id = "asset_id_example"  # str | Unique identifier of the asset.

        # Make request
        response = self.api.delete_pvc_asset_by_id(
            asset_id=asset_id,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "DELETE"
        assert "/api/v1/asset/datasource/pvc/{AssetId}" in kwargs["url"]

        # Verify response
        assert isinstance(response, HttpResponse)

    def test_delete_pvc_asset_by_id_error(self):
        """Test error handling for delete_pvc_asset_by_id"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        asset_id = "asset_id_example"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.delete_pvc_asset_by_id(
                asset_id=asset_id,
            )
        assert exc_info.value.status == 400

    def test_get_pvc_asset_by_id(self):
        """Test case for get_pvc_asset_by_id

        Get a PVC asset. Retrieve the details of a PVC datasource asset by id.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        asset_id = "asset_id_example"  # str | Unique identifier of the asset.
        usage_info = True  # bool | Whether the query should include asset usage information as part of the response.
        comply_to_project = 56  # int | Include workload creation compliance information of an asset, for a given project, as part of the response. To check compliance, you need to provide both project id and workload type.
        comply_to_workload_type = "comply_to_workload_type_example"  # str | Include workload creation compliance information of an asset, for a given workload type, as part of the response. To check compliance, you need to provide both project id and workload type.
        status_info = True  # bool | Whether the query should include asset status information as part of the response.
        comply_to_replica_type = "comply_to_replica_type_example"  # str | Include workload creation compliance information of an asset, for a given replica type, as part of the response. To check compliance, you need to provide both project id and workload type. For distributed, replica type should be provided as well.

        # Make request
        response = self.api.get_pvc_asset_by_id(
            asset_id=asset_id,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/asset/datasource/pvc/{AssetId}" in kwargs["url"]

        # Verify query parameters
        assert "usageInfo=" in kwargs["url"]
        # Verify query parameters
        assert "complyToProject=" in kwargs["url"]
        # Verify query parameters
        assert "complyToWorkloadType=" in kwargs["url"]
        # Verify query parameters
        assert "statusInfo=" in kwargs["url"]
        # Verify query parameters
        assert "complyToReplicaType=" in kwargs["url"]

        # Verify response
        assert isinstance(response, PVCAsset)

    def test_get_pvc_asset_by_id_error(self):
        """Test error handling for get_pvc_asset_by_id"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        asset_id = "asset_id_example"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_pvc_asset_by_id(
                asset_id=asset_id,
            )
        assert exc_info.value.status == 400

    def test_list_pvc_assets(self):
        """Test case for list_pvc_assets

        List PVC assets. Retrieves a list of PVC datasource assets.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        name = "name_example"  # str | Filter results by name.
        scope = "scope_example"  # str | Filter results by scope.
        project_id = 56  # int | Filter results by project id. if scope filter is project, only assets from the specific project will be included in the response. otherwise, the response will include both project, department, cluster and tenant assets.
        department_id = "1"  # str | Filter using the department id.
        cluster_id = "d73a738f-fab3-430a-8fa3-5241493d7128"  # str | Filter using the Universally Unique Identifier (UUID) of the cluster.
        usage_info = True  # bool | Whether the query should include asset usage information as part of the response.
        comply_to_project = 56  # int | Include workload creation compliance information of an asset, for a given project, as part of the response. To check compliance, you need to provide both project id and workload type.
        comply_to_workload_type = "comply_to_workload_type_example"  # str | Include workload creation compliance information of an asset, for a given workload type, as part of the response. To check compliance, you need to provide both project id and workload type.
        status_info = True  # bool | Whether the query should include asset status information as part of the response.
        asset_ids = "dbf4767e-2fa1-43b0-97a2-7c0cecda180b,550e8400-e29b-41d4-a716-44665544000a"  # str | Filter results by the ids of the assets. Provided value should be a comma separated string of UUIDs.
        comply_to_replica_type = "comply_to_replica_type_example"  # str | Include workload creation compliance information of an asset, for a given replica type, as part of the response. To check compliance, you need to provide both project id and workload type. For distributed, replica type should be provided as well.

        # Make request
        response = self.api.list_pvc_assets()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/asset/datasource/pvc" in kwargs["url"]

        # Verify query parameters
        assert "name=" in kwargs["url"]
        # Verify query parameters
        assert "scope=" in kwargs["url"]
        # Verify query parameters
        assert "projectId=" in kwargs["url"]
        # Verify query parameters
        assert "departmentId=" in kwargs["url"]
        # Verify query parameters
        assert "clusterId=" in kwargs["url"]
        # Verify query parameters
        assert "usageInfo=" in kwargs["url"]
        # Verify query parameters
        assert "complyToProject=" in kwargs["url"]
        # Verify query parameters
        assert "complyToWorkloadType=" in kwargs["url"]
        # Verify query parameters
        assert "statusInfo=" in kwargs["url"]
        # Verify query parameters
        assert "assetIds=" in kwargs["url"]
        # Verify query parameters
        assert "complyToReplicaType=" in kwargs["url"]

        # Verify response
        assert isinstance(response, PVCListResponse)

    def test_list_pvc_assets_error(self):
        """Test error handling for list_pvc_assets"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.list_pvc_assets()
        assert exc_info.value.status == 400

    def test_update_pvc_asset_by_id(self):
        """Test case for update_pvc_asset_by_id

        Update a PVC asset. Use to update the details of a PVC datasource asset by id.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        asset_id = "asset_id_example"  # str | Unique identifier of the asset.
        pvc_update_request = runai.PVCUpdateRequest()  # PVCUpdateRequest |

        # Make request
        response = self.api.update_pvc_asset_by_id(
            asset_id=asset_id,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "PUT"
        assert "/api/v1/asset/datasource/pvc/{AssetId}" in kwargs["url"]

        # Verify body
        assert kwargs["body"] is not None

        # Verify response
        assert isinstance(response, PVCAsset)

    def test_update_pvc_asset_by_id_error(self):
        """Test error handling for update_pvc_asset_by_id"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        asset_id = "asset_id_example"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.update_pvc_asset_by_id(
                asset_id=asset_id,
            )
        assert exc_info.value.status == 400
