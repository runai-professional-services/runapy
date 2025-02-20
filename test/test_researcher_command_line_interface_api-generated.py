# coding: utf-8

"""
Test file for ResearcherCommandLineInterfaceApi
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


class TestResearcherCommandLineInterfaceApi:
    """Test cases for ResearcherCommandLineInterfaceApi"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures"""
        self.configuration = Configuration(
            client_id="test-client",
            client_secret="test-secret",
            runai_base_url="https://test.run.ai",
        )
        self.api_client = ApiClient(self.configuration)
        self.api = ResearcherCommandLineInterfaceApi(self.api_client)

        # Mock the request method
        self.request_patcher = mock.patch.object(self.api_client.rest_client, "request")
        self.mock_request = self.request_patcher.start()
        yield
        self.request_patcher.stop()

    def test_get_binary(self):
        """Test case for get_binary

        Download RunAI Researcher command line binary This endpoint returns a binary file that run the Run:AI CLI.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        operating_system = "linux"  # str | The operating system name.
        architecture = "arm64"  # str | The architecture type.

        # Make request
        response = self.api.get_binary(
            operating_system=operating_system,
            architecture=architecture,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert (
            "/api/v1/cli-exposer/dist/{operatingSystem}/{architecture}/runai"
            in kwargs["url"]
        )

        # Verify response
        assert isinstance(response, bytearray)

    def test_get_binary_error(self):
        """Test error handling for get_binary"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        operating_system = "linux"
        architecture = "arm64"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_binary(
                operating_system=operating_system,
                architecture=architecture,
            )
        assert exc_info.value.status == 400

    def test_get_installer_linux(self):
        """Test case for get_installer_linux

        Download Linux installer script This endpoint returns a Linux script that can be used to install the Run:AI CLI.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Make request
        response = self.api.get_installer_linux()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/cli-exposer/installer/linux" in kwargs["url"]

        # Verify response
        assert isinstance(response, str)

    def test_get_installer_linux_error(self):
        """Test error handling for get_installer_linux"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_installer_linux()
        assert exc_info.value.status == 400

    def test_get_installer_linux_commands(self):
        """Test case for get_installer_linux_commands

        Get Linux installer script commands This endpoint returns a linux script commands that can be used to install the Run:AI CLI.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Make request
        response = self.api.get_installer_linux_commands()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/cli-exposer/installer/linux/commands" in kwargs["url"]

        # Verify response
        assert isinstance(response, Command)

    def test_get_installer_linux_commands_error(self):
        """Test error handling for get_installer_linux_commands"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_installer_linux_commands()
        assert exc_info.value.status == 400

    def test_get_installer_mac(self):
        """Test case for get_installer_mac

        Download Mac installer script This endpoint returns a Mac script that can be used to install the Run:AI CLI.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Make request
        response = self.api.get_installer_mac()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/cli-exposer/installer/mac" in kwargs["url"]

        # Verify response
        assert isinstance(response, str)

    def test_get_installer_mac_error(self):
        """Test error handling for get_installer_mac"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_installer_mac()
        assert exc_info.value.status == 400

    def test_get_installer_mac_commands(self):
        """Test case for get_installer_mac_commands

        Get Mac installer script commands This endpoint returns a Mac script commands that can be used to install the Run:AI CLI.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Make request
        response = self.api.get_installer_mac_commands()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/cli-exposer/installer/mac/commands" in kwargs["url"]

        # Verify response
        assert isinstance(response, Command)

    def test_get_installer_mac_commands_error(self):
        """Test error handling for get_installer_mac_commands"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_installer_mac_commands()
        assert exc_info.value.status == 400

    def test_get_installer_unix(self):
        """Test case for get_installer_unix

        Download Unix installer script This endpoint returns a unix script that can be used to install the Run:AI CLI.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Make request
        response = self.api.get_installer_unix()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/cli-exposer/installer/unix" in kwargs["url"]

        # Verify response
        assert isinstance(response, str)

    def test_get_installer_unix_error(self):
        """Test error handling for get_installer_unix"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_installer_unix()
        assert exc_info.value.status == 400

    def test_get_installer_unix_commands(self):
        """Test case for get_installer_unix_commands

        Get Unix installer script commands This endpoint returns a unix script commands that can be used to install the Run:AI CLI.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Make request
        response = self.api.get_installer_unix_commands()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/cli-exposer/installer/unix/commands" in kwargs["url"]

        # Verify response
        assert isinstance(response, Command)

    def test_get_installer_unix_commands_error(self):
        """Test error handling for get_installer_unix_commands"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_installer_unix_commands()
        assert exc_info.value.status == 400

    def test_get_installer_windows_commands(self):
        """Test case for get_installer_windows_commands

        Get Windows MSI installer script commands This endpoint returns a windows script commands that can be used to install the Run:AI CLI.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Make request
        response = self.api.get_installer_windows_commands()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/cli-exposer/installer/windows/commands" in kwargs["url"]

        # Verify response
        assert isinstance(response, Command)

    def test_get_installer_windows_commands_error(self):
        """Test error handling for get_installer_windows_commands"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_installer_windows_commands()
        assert exc_info.value.status == 400

    def test_get_manual_document(self):
        """Test case for get_manual_document

        Get CLI document by name This endpoint returns a document of help for the Run:AI CLI.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        document_name = "runai.md"  # str | The manual document name.

        # Make request
        response = self.api.get_manual_document(
            document_name=document_name,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/cli-exposer/docs/{documentName}" in kwargs["url"]

        # Verify response
        assert isinstance(response, str)

    def test_get_manual_document_error(self):
        """Test error handling for get_manual_document"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        document_name = "runai.md"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_manual_document(
                document_name=document_name,
            )
        assert exc_info.value.status == 400
