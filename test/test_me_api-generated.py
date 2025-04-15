# coding: utf-8

"""
Test file for MeApi
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


class TestMeApi:
    """Test cases for MeApi"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures"""
        self.configuration = Configuration(
            client_id="test-client",
            client_secret="test-secret",
            runai_base_url="https://test.run.ai",
        )
        self.api_client = ApiClient(self.configuration)
        self.api = MeApi(self.api_client)

        # Mock the request method
        self.request_patcher = mock.patch.object(self.api_client.rest_client, "request")
        self.mock_request = self.request_patcher.start()
        yield
        self.request_patcher.stop()

    def test_count_me_access_rules(self):
        """Test case for count_me_access_rules

        Count the access rules assigned to the requesting user. Use to retrieve the number of access rules assigned to the requesting user.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        search = "test project"  # str | Filter results by a free text search.

        # Make request
        response = self.api.count_me_access_rules()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/authorization/me/access-rules/count" in kwargs["url"]

        # Verify query parameters
        assert "search=" in kwargs["url"]

        # Verify response
        assert isinstance(response, CountAccessRules200Response)

    def test_count_me_access_rules_error(self):
        """Test error handling for count_me_access_rules"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.count_me_access_rules()
        assert exc_info.value.status == 400

    def test_get_me_access_rules(self):
        """Test case for get_me_access_rules

        List the access rules assigned to the requesting user. Retrieve the access rules assigned to the requesting user.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        limit = 50  # int | The maximum number of entries to return.
        offset = 100  # int | The offset of the first item returned in the collection.
        search = "test project"  # str | Filter results by a free text search.

        # Make request
        response = self.api.get_me_access_rules()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/authorization/me/access-rules" in kwargs["url"]

        # Verify query parameters
        assert "limit=" in kwargs["url"]
        # Verify query parameters
        assert "offset=" in kwargs["url"]
        # Verify query parameters
        assert "search=" in kwargs["url"]

        # Verify response
        assert isinstance(response, MeAccessRulesResponse)

    def test_get_me_access_rules_error(self):
        """Test error handling for get_me_access_rules"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_me_access_rules()
        assert exc_info.value.status == 400
