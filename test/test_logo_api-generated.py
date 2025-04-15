# coding: utf-8

"""
Test file for LogoApi
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


class TestLogoApi:
    """Test cases for LogoApi"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures"""
        self.configuration = Configuration(
            client_id="test-client",
            client_secret="test-secret",
            runai_base_url="https://test.run.ai",
        )
        self.api_client = ApiClient(self.configuration)
        self.api = LogoApi(self.api_client)

        # Mock the request method
        self.request_patcher = mock.patch.object(self.api_client.rest_client, "request")
        self.mock_request = self.request_patcher.start()
        yield
        self.request_patcher.stop()

    def test_get_tenant_logo(self):
        """Test case for get_tenant_logo

        Get tenant logo. (base64) Retrieve the base64 logo file.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Make request
        response = self.api.get_tenant_logo()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/logo" in kwargs["url"]

        # Verify response
        assert isinstance(response, GetTenantLogo200Response)

    def test_get_tenant_logo_error(self):
        """Test error handling for get_tenant_logo"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_tenant_logo()
        assert exc_info.value.status == 400

    def test_upload_tenant_logo(self):
        """Test case for upload_tenant_logo

        Upload logo for tenant. (base64) Use to upload a base64 logo file. Max size 128kb.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({})
        self.mock_request.return_value = mock_response

        # Test parameters
        logo_creation_request = runai.LogoCreationRequest()  # LogoCreationRequest |

        # Make request
        self.api.upload_tenant_logo()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "POST"
        assert "/api/v1/logo" in kwargs["url"]

        # Verify body
        assert kwargs["body"] is not None

    def test_upload_tenant_logo_error(self):
        """Test error handling for upload_tenant_logo"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.upload_tenant_logo()
        assert exc_info.value.status == 400
