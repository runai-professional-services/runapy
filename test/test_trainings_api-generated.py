# coding: utf-8

"""
Test file for TrainingsApi
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


class TestTrainingsApi:
    """Test cases for TrainingsApi"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures"""
        self.configuration = Configuration(
            client_id="test-client",
            client_secret="test-secret",
            runai_base_url="https://test.run.ai",
        )
        self.api_client = ApiClient(self.configuration)
        self.api = TrainingsApi(self.api_client)

        # Mock the request method
        self.request_patcher = mock.patch.object(self.api_client.rest_client, "request")
        self.mock_request = self.request_patcher.start()
        yield
        self.request_patcher.stop()

    def test_create_training1(self):
        """Test case for create_training1

        Create a training. Create a training workload using container related fields.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        training_creation_request = (
            runai.TrainingCreationRequest()
        )  # TrainingCreationRequest |

        # Make request
        response = self.api.create_training1()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "POST"
        assert "/api/v1/workloads/trainings" in kwargs["url"]

        # Verify body
        assert kwargs["body"] is not None

        # Verify response
        assert isinstance(response, Training1)

    def test_create_training1_error(self):
        """Test error handling for create_training1"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.create_training1()
        assert exc_info.value.status == 400

    def test_delete_training(self):
        """Test case for delete_training

        Delete a training. Delete a training using a workload id.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        workload_id = "workload_id_example"  # str | The  Universally Unique Identifier (UUID) of the workload.

        # Make request
        response = self.api.delete_training(
            workload_id=workload_id,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "DELETE"
        assert "/api/v1/workloads/trainings/{workloadId}" in kwargs["url"]

        # Verify response
        assert isinstance(response, HttpResponse)

    def test_delete_training_error(self):
        """Test error handling for delete_training"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        workload_id = "workload_id_example"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.delete_training(
                workload_id=workload_id,
            )
        assert exc_info.value.status == 400

    def test_get_training(self):
        """Test case for get_training

        Get training data. Retrieve training details using a workload id.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        workload_id = "workload_id_example"  # str | The  Universally Unique Identifier (UUID) of the workload.

        # Make request
        response = self.api.get_training(
            workload_id=workload_id,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/workloads/trainings/{workloadId}" in kwargs["url"]

        # Verify response
        assert isinstance(response, Training1)

    def test_get_training_error(self):
        """Test error handling for get_training"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        workload_id = "workload_id_example"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_training(
                workload_id=workload_id,
            )
        assert exc_info.value.status == 400

    def test_resume_training(self):
        """Test case for resume_training

        Resume a training. Resume a training that was suspended using a workload id.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        workload_id = "workload_id_example"  # str | The  Universally Unique Identifier (UUID) of the workload.

        # Make request
        response = self.api.resume_training(
            workload_id=workload_id,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "POST"
        assert "/api/v1/workloads/trainings/{workloadId}/resume" in kwargs["url"]

        # Verify response
        assert isinstance(response, HttpResponse)

    def test_resume_training_error(self):
        """Test error handling for resume_training"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        workload_id = "workload_id_example"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.resume_training(
                workload_id=workload_id,
            )
        assert exc_info.value.status == 400

    def test_suspend_training(self):
        """Test case for suspend_training

        Suspend a training. Suspend a training from running using a workload id.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        workload_id = "workload_id_example"  # str | The  Universally Unique Identifier (UUID) of the workload.

        # Make request
        response = self.api.suspend_training(
            workload_id=workload_id,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "POST"
        assert "/api/v1/workloads/trainings/{workloadId}/suspend" in kwargs["url"]

        # Verify response
        assert isinstance(response, HttpResponse)

    def test_suspend_training_error(self):
        """Test error handling for suspend_training"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        workload_id = "workload_id_example"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.suspend_training(
                workload_id=workload_id,
            )
        assert exc_info.value.status == 400
