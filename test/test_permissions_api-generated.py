# coding: utf-8

"""
Test file for PermissionsApi
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


class TestPermissionsApi:
    """Test cases for PermissionsApi"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures"""
        self.configuration = Configuration(
            client_id="test-client",
            client_secret="test-secret",
            runai_base_url="https://test.run.ai",
        )
        self.api_client = ApiClient(self.configuration)
        self.api = PermissionsApi(self.api_client)

        # Mock the request method
        self.request_patcher = mock.patch.object(self.api_client.rest_client, "request")
        self.mock_request = self.request_patcher.start()
        yield
        self.request_patcher.stop()

    def test_get_permissions(self):
        """Test case for get_permissions

        Get a summary of user permissions. Retrieve a summary of user permissions.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Make request
        response = self.api.get_permissions()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/authorization/permissions" in kwargs["url"]

        # Verify response
        assert isinstance(response, List[Permission])

    def test_get_permissions_error(self):
        """Test error handling for get_permissions"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_permissions()
        assert exc_info.value.status == 400

    def test_get_permitted_scopes(self):
        """Test case for get_permitted_scopes

        Calculate permitted scopes. Use to calculate user permitted scopes for an action on a resource.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        get_permitted_scopes_request = (
            runai.GetPermittedScopesRequest()
        )  # GetPermittedScopesRequest | The request parameters.

        # Make request
        response = self.api.get_permitted_scopes(
            get_permitted_scopes_request=get_permitted_scopes_request,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "POST"
        assert "/api/v1/authorization/permitted-scopes" in kwargs["url"]

        # Verify body
        assert kwargs["body"] is not None

        # Verify response
        assert isinstance(response, PermittedScopesActions)

    def test_get_permitted_scopes_error(self):
        """Test error handling for get_permitted_scopes"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        get_permitted_scopes_request = runai.GetPermittedScopesRequest()

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_permitted_scopes(
                get_permitted_scopes_request=get_permitted_scopes_request,
            )
        assert exc_info.value.status == 400
