# coding: utf-8

"""
Test file for RolesApi
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


class TestRolesApi:
    """Test cases for RolesApi"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures"""
        self.configuration = Configuration(
            client_id="test-client",
            client_secret="test-secret",
            runai_base_url="https://test.run.ai",
        )
        self.api_client = ApiClient(self.configuration)
        self.api = RolesApi(self.api_client)

        # Mock the request method
        self.request_patcher = mock.patch.object(self.api_client.rest_client, "request")
        self.mock_request = self.request_patcher.start()
        yield
        self.request_patcher.stop()

    def test_get_role_v1(self):
        """Test case for get_role_v1

        Get a role by id. Retrieve the details of a role by id.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        role_id_path = 32  # int | The id of the role to retrieve

        # Make request
        response = self.api.get_role_v1(
            role_id_path=role_id_path,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/authorization/roles/{roleIdPath}" in kwargs["url"]

        # Verify response
        assert isinstance(response, Role1)

    def test_get_role_v1_error(self):
        """Test error handling for get_role_v1"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        role_id_path = 32

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_role_v1(
                role_id_path=role_id_path,
            )
        assert exc_info.value.status == 400

    def test_get_roles_v1(self):
        """Test case for get_roles_v1

        Get a list of roles. Use to retrieve a list of roles.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Make request
        response = self.api.get_roles_v1()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/authorization/roles" in kwargs["url"]

        # Verify response
        assert isinstance(response, List[Role1])

    def test_get_roles_v1_error(self):
        """Test error handling for get_roles_v1"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_roles_v1()
        assert exc_info.value.status == 400
