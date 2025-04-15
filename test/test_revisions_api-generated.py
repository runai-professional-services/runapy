# coding: utf-8

"""
Test file for RevisionsApi
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


class TestRevisionsApi:
    """Test cases for RevisionsApi"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures"""
        self.configuration = Configuration(
            client_id="test-client",
            client_secret="test-secret",
            runai_base_url="https://test.run.ai",
        )
        self.api_client = ApiClient(self.configuration)
        self.api = RevisionsApi(self.api_client)

        # Mock the request method
        self.request_patcher = mock.patch.object(self.api_client.rest_client, "request")
        self.mock_request = self.request_patcher.start()
        yield
        self.request_patcher.stop()

    def test_count_inference_workload_revisions(self):
        """Test case for count_inference_workload_revisions

        Get inference workload revisions count. Retrieve the number of an inference workload revisions from a cluster.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        workload_id = "workload_id_example"  # str | The  Universally Unique Identifier (UUID) of the workload.
        deleted = True  # bool | Return only deleted resources when `true`.

        # Make request
        response = self.api.count_inference_workload_revisions(
            workload_id=workload_id,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert (
            "/api/v1/workloads/inferences/{workloadId}/revisions/count" in kwargs["url"]
        )

        # Verify query parameters
        assert "deleted=" in kwargs["url"]

        # Verify response
        assert isinstance(response, CountAccessRules200Response)

    def test_count_inference_workload_revisions_error(self):
        """Test error handling for count_inference_workload_revisions"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        workload_id = "workload_id_example"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.count_inference_workload_revisions(
                workload_id=workload_id,
            )
        assert exc_info.value.status == 400

    def test_get_inference_workload_revisions(self):
        """Test case for get_inference_workload_revisions

        Get inference workload revisions by id. Retrieve the details of inference workload revisions by workload id.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        workload_id = "workload_id_example"  # str | The  Universally Unique Identifier (UUID) of the workload.
        deleted = True  # bool | Return only deleted resources when `true`.

        # Make request
        response = self.api.get_inference_workload_revisions(
            workload_id=workload_id,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/workloads/inferences/{workloadId}/revisions" in kwargs["url"]

        # Verify query parameters
        assert "deleted=" in kwargs["url"]

        # Verify response
        assert isinstance(response, GetInferenceWorkloadRevisions200Response)

    def test_get_inference_workload_revisions_error(self):
        """Test error handling for get_inference_workload_revisions"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        workload_id = "workload_id_example"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_inference_workload_revisions(
                workload_id=workload_id,
            )
        assert exc_info.value.status == 400

    def test_get_revision(self):
        """Test case for get_revision

        Get revision data. Retrieve revision details using a revision id.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        revision_id = "revision_id_example"  # str | The  Universally Unique Identifier (UUID) of the revision.

        # Make request
        response = self.api.get_revision(
            revision_id=revision_id,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/workloads/inferences/revisions/{revisionId}" in kwargs["url"]

        # Verify response
        assert isinstance(response, Revision)

    def test_get_revision_error(self):
        """Test error handling for get_revision"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        revision_id = "revision_id_example"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_revision(
                revision_id=revision_id,
            )
        assert exc_info.value.status == 400
