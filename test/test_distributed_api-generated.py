# coding: utf-8

"""
Test file for DistributedApi
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


class TestDistributedApi:
    """Test cases for DistributedApi"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures"""
        self.configuration = Configuration(
            client_id="test-client",
            client_secret="test-secret",
            runai_base_url="https://test.run.ai",
        )
        self.api_client = ApiClient(self.configuration)
        self.api = DistributedApi(self.api_client)

        # Mock the request method
        self.request_patcher = mock.patch.object(self.api_client.rest_client, "request")
        self.mock_request = self.request_patcher.start()
        yield
        self.request_patcher.stop()

    def test_create_distributed(self):
        """Test case for create_distributed

        Create a distributed training. Use to create a distributed training.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        distributed_creation_request = (
            runai.DistributedCreationRequest()
        )  # DistributedCreationRequest |

        # Make request
        response = self.api.create_distributed()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "POST"
        assert "/api/v1/workloads/distributed" in kwargs["url"]

        # Verify body
        assert kwargs["body"] is not None

        # Verify response
        assert isinstance(response, DistributedWorkload)

    def test_create_distributed_error(self):
        """Test error handling for create_distributed"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.create_distributed()
        assert exc_info.value.status == 400

    def test_delete_distributed(self):
        """Test case for delete_distributed

        Delete a distributed training by id. Use to delete a distributed training by workload id.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        workload_id = "workload_id_example"  # str | The  Universally Unique Identifier (UUID) of the workload.

        # Make request
        response = self.api.delete_distributed(
            workload_id=workload_id,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "DELETE"
        assert "/api/v1/workloads/distributed/{workloadId}" in kwargs["url"]

        # Verify response
        assert isinstance(response, HttpResponse)

    def test_delete_distributed_error(self):
        """Test error handling for delete_distributed"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        workload_id = "workload_id_example"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.delete_distributed(
                workload_id=workload_id,
            )
        assert exc_info.value.status == 400

    def test_get_distributed(self):
        """Test case for get_distributed

        Get distributed training's data. [Experimental] Retrieve the details of a distributed training by workload id.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        workload_id = "workload_id_example"  # str | The  Universally Unique Identifier (UUID) of the workload.

        # Make request
        response = self.api.get_distributed(
            workload_id=workload_id,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/workloads/distributed/{workloadId}" in kwargs["url"]

        # Verify response
        assert isinstance(response, DistributedWorkload)

    def test_get_distributed_error(self):
        """Test error handling for get_distributed"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        workload_id = "workload_id_example"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_distributed(
                workload_id=workload_id,
            )
        assert exc_info.value.status == 400

    def test_resume_distributed(self):
        """Test case for resume_distributed

        Resume a distributed training. Resume a distributed training that was suspended using a workload id.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        workload_id = "workload_id_example"  # str | The  Universally Unique Identifier (UUID) of the workload.

        # Make request
        response = self.api.resume_distributed(
            workload_id=workload_id,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "POST"
        assert "/api/v1/workloads/distributed/{workloadId}/resume" in kwargs["url"]

        # Verify response
        assert isinstance(response, HttpResponse)

    def test_resume_distributed_error(self):
        """Test error handling for resume_distributed"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        workload_id = "workload_id_example"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.resume_distributed(
                workload_id=workload_id,
            )
        assert exc_info.value.status == 400

    def test_suspend_distributed(self):
        """Test case for suspend_distributed

        Suspend a distributed training. Suspend a distributed training from running using a workload id.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        workload_id = "workload_id_example"  # str | The  Universally Unique Identifier (UUID) of the workload.

        # Make request
        response = self.api.suspend_distributed(
            workload_id=workload_id,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "POST"
        assert "/api/v1/workloads/distributed/{workloadId}/suspend" in kwargs["url"]

        # Verify response
        assert isinstance(response, HttpResponse)

    def test_suspend_distributed_error(self):
        """Test error handling for suspend_distributed"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        workload_id = "workload_id_example"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.suspend_distributed(
                workload_id=workload_id,
            )
        assert exc_info.value.status == 400
