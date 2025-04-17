# coding: utf-8

"""
Test file for DatavolumesApi
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


class TestDatavolumesApi:
    """Test cases for DatavolumesApi"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures"""
        self.configuration = Configuration(
            client_id="test-client",
            client_secret="test-secret",
            runai_base_url="https://test.run.ai",
        )
        self.api_client = ApiClient(self.configuration)
        self.api = DatavolumesApi(self.api_client)

        # Mock the request method
        self.request_patcher = mock.patch.object(self.api_client.rest_client, "request")
        self.mock_request = self.request_patcher.start()
        yield
        self.request_patcher.stop()

    def test_count_datavolumes(self):
        """Test case for count_datavolumes

        Count data volumes. Retrieve the number of data volumes.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        request_type = (
            runai.DatavolumeRequestType()
        )  # DatavolumeRequestType | Which datavolumes would be returned in the response. Originated - datavolumes that are originated in the permitted scopes of the caller. UsableInProject - datavolumes that can be used in a specific project; if you use this value, you must also provide the project ID in the \"usableInProjectId\" query param.
        usable_in_project_id = "5"  # str | Only when using \"UsableInProject\" requestType; Filter results for only datavolumes that are shared with - or originated in - the project.
        filter_by = [
            '["name!=some-datavolume-name"]'
        ]  # List[str] | Filter results by a parameter. Use the format field-name operator value. Operators are == Equals, != Not equals, <= Less than or equal, >= Greater than or equal, =@ contains, !@ Does not contains, =^ Starts with and =$ Ends with. Dates are in ISO 8601 timestamp format and available for operators == None, != None, <= and >=.

        # Make request
        response = self.api.count_datavolumes(
            request_type=request_type,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/datavolumes/count" in kwargs["url"]

        # Verify query parameters
        assert "requestType=" in kwargs["url"]
        # Verify query parameters
        assert "usableInProjectId=" in kwargs["url"]
        # Verify query parameters
        assert "filterBy=" in kwargs["url"]

        # Verify response
        assert isinstance(response, CountAccessRules200Response)

    def test_count_datavolumes_error(self):
        """Test error handling for count_datavolumes"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        request_type = runai.DatavolumeRequestType()

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.count_datavolumes(
                request_type=request_type,
            )
        assert exc_info.value.status == 400

    def test_create_datavolume(self):
        """Test case for create_datavolume

        Create a datavolume
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        datavolume_creation_fields = (
            runai.DatavolumeCreationFields()
        )  # DatavolumeCreationFields | The datavolume to create.

        # Make request
        response = self.api.create_datavolume(
            datavolume_creation_fields=datavolume_creation_fields,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "POST"
        assert "/api/v1/datavolumes" in kwargs["url"]

        # Verify body
        assert kwargs["body"] is not None

        # Verify response
        assert isinstance(response, Datavolume)

    def test_create_datavolume_error(self):
        """Test error handling for create_datavolume"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        datavolume_creation_fields = runai.DatavolumeCreationFields()

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.create_datavolume(
                datavolume_creation_fields=datavolume_creation_fields,
            )
        assert exc_info.value.status == 400

    def test_delete_datavolume(self):
        """Test case for delete_datavolume

        Delete datavolume
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        datavolume_id = "71f69d83-ba66-4822-adf5-55ce55efd210"  # str | The id of the datavolume to retrieve

        # Make request
        response = self.api.delete_datavolume(
            datavolume_id=datavolume_id,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "DELETE"
        assert "/api/v1/datavolumes/{datavolumeId}" in kwargs["url"]

        # Verify response
        assert isinstance(response, HttpResponse)

    def test_delete_datavolume_error(self):
        """Test error handling for delete_datavolume"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        datavolume_id = "71f69d83-ba66-4822-adf5-55ce55efd210"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.delete_datavolume(
                datavolume_id=datavolume_id,
            )
        assert exc_info.value.status == 400

    def test_get_datavolume(self):
        """Test case for get_datavolume

        Get datavolume
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        datavolume_id = "71f69d83-ba66-4822-adf5-55ce55efd210"  # str | The id of the datavolume to retrieve

        # Make request
        response = self.api.get_datavolume(
            datavolume_id=datavolume_id,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/datavolumes/{datavolumeId}" in kwargs["url"]

        # Verify response
        assert isinstance(response, Datavolume)

    def test_get_datavolume_error(self):
        """Test error handling for get_datavolume"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        datavolume_id = "71f69d83-ba66-4822-adf5-55ce55efd210"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_datavolume(
                datavolume_id=datavolume_id,
            )
        assert exc_info.value.status == 400

    def test_get_datavolume_shared_scopes(self):
        """Test case for get_datavolume_shared_scopes

        Get the datavolume's shared scopes
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        datavolume_id = "71f69d83-ba66-4822-adf5-55ce55efd210"  # str | The id of the datavolume to retrieve

        # Make request
        response = self.api.get_datavolume_shared_scopes(
            datavolume_id=datavolume_id,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/datavolumes/{datavolumeId}/sharedScopes" in kwargs["url"]

        # Verify response
        assert isinstance(response, List[SharedScope])

    def test_get_datavolume_shared_scopes_error(self):
        """Test error handling for get_datavolume_shared_scopes"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        datavolume_id = "71f69d83-ba66-4822-adf5-55ce55efd210"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_datavolume_shared_scopes(
                datavolume_id=datavolume_id,
            )
        assert exc_info.value.status == 400

    def test_get_datavolumes(self):
        """Test case for get_datavolumes

        List datavolumes in permitted scopes Get requested datavolumes.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        request_type = (
            runai.DatavolumeRequestType()
        )  # DatavolumeRequestType | Which datavolumes would be returned in the response. Originated - datavolumes that are originated in the permitted scopes of the caller. UsableInProject - datavolumes that can be used in a specific project; if you use this value, you must also provide the project ID in the \"usableInProjectId\" query param.
        usable_in_project_id = "5"  # str | Only when using \"UsableInProject\" requestType; Filter results for only datavolumes that are shared with - or originated in - the project.
        offset = 100  # int | The offset of the first item returned in the collection.
        limit = 50  # int | The maximum number of entries to return.
        sort_by = "sort_by_example"  # str | Sort results by a parameters.
        sort_order = asc  # str | Sort results in descending or ascending order.
        filter_by = [
            '["name!=some-datavolume-name"]'
        ]  # List[str] | Filter results by a parameter. Use the format field-name operator value. Operators are == Equals, != Not equals, <= Less than or equal, >= Greater than or equal, =@ contains, !@ Does not contains, =^ Starts with and =$ Ends with. Dates are in ISO 8601 timestamp format and available for operators == None, != None, <= and >=.

        # Make request
        response = self.api.get_datavolumes(
            request_type=request_type,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/datavolumes" in kwargs["url"]

        # Verify query parameters
        assert "requestType=" in kwargs["url"]
        # Verify query parameters
        assert "usableInProjectId=" in kwargs["url"]
        # Verify query parameters
        assert "offset=" in kwargs["url"]
        # Verify query parameters
        assert "limit=" in kwargs["url"]
        # Verify query parameters
        assert "sortBy=" in kwargs["url"]
        # Verify query parameters
        assert "sortOrder=" in kwargs["url"]
        # Verify query parameters
        assert "filterBy=" in kwargs["url"]

        # Verify response
        assert isinstance(response, GetDatavolumes200Response)

    def test_get_datavolumes_error(self):
        """Test error handling for get_datavolumes"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        request_type = runai.DatavolumeRequestType()

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_datavolumes(
                request_type=request_type,
            )
        assert exc_info.value.status == 400

    def test_patch_datavolume(self):
        """Test case for patch_datavolume

        Patch datavolume
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        datavolume_id = "71f69d83-ba66-4822-adf5-55ce55efd210"  # str | The id of the datavolume to retrieve
        datavolume_patch_fields = (
            runai.DatavolumePatchFields()
        )  # DatavolumePatchFields | Datavolume to update.

        # Make request
        response = self.api.patch_datavolume(
            datavolume_id=datavolume_id,
            datavolume_patch_fields=datavolume_patch_fields,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "PATCH"
        assert "/api/v1/datavolumes/{datavolumeId}" in kwargs["url"]

        # Verify body
        assert kwargs["body"] is not None

        # Verify response
        assert isinstance(response, DatavolumeNoSharedScopes)

    def test_patch_datavolume_error(self):
        """Test error handling for patch_datavolume"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        datavolume_id = "71f69d83-ba66-4822-adf5-55ce55efd210"
        datavolume_patch_fields = runai.DatavolumePatchFields()

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.patch_datavolume(
                datavolume_id=datavolume_id,
                datavolume_patch_fields=datavolume_patch_fields,
            )
        assert exc_info.value.status == 400

    def test_patch_datavolume_shared_scopes(self):
        """Test case for patch_datavolume_shared_scopes

        Patch the datavolume's shared scopes
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        datavolume_id = "71f69d83-ba66-4822-adf5-55ce55efd210"  # str | The id of the datavolume to retrieve
        shared_scopes_patch_request = (
            runai.SharedScopesPatchRequest()
        )  # SharedScopesPatchRequest | Requested SharedScopes of the datavolume to patch.

        # Make request
        response = self.api.patch_datavolume_shared_scopes(
            datavolume_id=datavolume_id,
            shared_scopes_patch_request=shared_scopes_patch_request,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "PATCH"
        assert "/api/v1/datavolumes/{datavolumeId}/sharedScopes" in kwargs["url"]

        # Verify body
        assert kwargs["body"] is not None

        # Verify response
        assert isinstance(response, List[SharedScope])

    def test_patch_datavolume_shared_scopes_error(self):
        """Test error handling for patch_datavolume_shared_scopes"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        datavolume_id = "71f69d83-ba66-4822-adf5-55ce55efd210"
        shared_scopes_patch_request = runai.SharedScopesPatchRequest()

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.patch_datavolume_shared_scopes(
                datavolume_id=datavolume_id,
                shared_scopes_patch_request=shared_scopes_patch_request,
            )
        assert exc_info.value.status == 400
