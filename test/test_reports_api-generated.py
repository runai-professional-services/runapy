# coding: utf-8

"""
Test file for ReportsApi
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


class TestReportsApi:
    """Test cases for ReportsApi"""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup test fixtures"""
        self.configuration = Configuration(
            client_id="test-client",
            client_secret="test-secret",
            runai_base_url="https://test.run.ai",
        )
        self.api_client = ApiClient(self.configuration)
        self.api = ReportsApi(self.api_client)

        # Mock the request method
        self.request_patcher = mock.patch.object(self.api_client.rest_client, "request")
        self.mock_request = self.request_patcher.start()
        yield
        self.request_patcher.stop()

    def test_are_reports_available(self):
        """Test case for are_reports_available

        Reports availability
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Make request
        response = self.api.are_reports_available()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/org-unit/reports/availability" in kwargs["url"]

        # Verify response
        assert isinstance(response, AreReportsAvailable200Response)

    def test_are_reports_available_error(self):
        """Test error handling for are_reports_available"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.are_reports_available()
        assert exc_info.value.status == 400

    def test_count_reports(self):
        """Test case for count_reports

        Count reports
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        filter_by = [
            '["name!=some-name"]'
        ]  # List[str] | Filter results by a parameter. Use the format field-name operator value. Operators are == Equals, != Not equals, <= Less than or equal, >= Greater than or equal, =@ contains, !@ Does not contains, =^ Starts with and =$ Ends with. Dates are in ISO 8601 timestamp format and available for operators == None, != None, <= and >=.
        search = "test project"  # str | Filter results by a free text search.

        # Make request
        response = self.api.count_reports()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/org-unit/reports/count" in kwargs["url"]

        # Verify query parameters
        assert "filterBy=" in kwargs["url"]
        # Verify query parameters
        assert "search=" in kwargs["url"]

        # Verify response
        assert isinstance(response, CountResponse)

    def test_count_reports_error(self):
        """Test error handling for count_reports"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.count_reports()
        assert exc_info.value.status == 400

    def test_create_report(self):
        """Test case for create_report

        Create a new report request.
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        report_request_fields = (
            runai.ReportRequestFields()
        )  # ReportRequestFields | Report to create.

        # Make request
        response = self.api.create_report(
            report_request_fields=report_request_fields,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "POST"
        assert "/api/v1/org-unit/reports" in kwargs["url"]

        # Verify body
        assert kwargs["body"] is not None

        # Verify response
        assert isinstance(response, Report)

    def test_create_report_error(self):
        """Test error handling for create_report"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        report_request_fields = runai.ReportRequestFields()

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.create_report(
                report_request_fields=report_request_fields,
            )
        assert exc_info.value.status == 400

    def test_delete_report_by_id(self):
        """Test case for delete_report_by_id

        Delete report
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({})
        self.mock_request.return_value = mock_response

        # Test parameters
        report_id = "575c19e8-c7c3-45b0-8290-2f47397a8383"  # str | The report id

        # Make request
        self.api.delete_report_by_id(
            report_id=report_id,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "DELETE"
        assert "/api/v1/org-unit/reports/{reportId}" in kwargs["url"]

    def test_delete_report_by_id_error(self):
        """Test error handling for delete_report_by_id"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        report_id = "575c19e8-c7c3-45b0-8290-2f47397a8383"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.delete_report_by_id(
                report_id=report_id,
            )
        assert exc_info.value.status == 400

    def test_download_report_by_id(self):
        """Test case for download_report_by_id

        Download report
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({})
        self.mock_request.return_value = mock_response

        # Test parameters
        report_id = "575c19e8-c7c3-45b0-8290-2f47397a8383"  # str | The report id

        # Make request
        self.api.download_report_by_id(
            report_id=report_id,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/org-unit/reports/{reportId}/file" in kwargs["url"]

    def test_download_report_by_id_error(self):
        """Test error handling for download_report_by_id"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        report_id = "575c19e8-c7c3-45b0-8290-2f47397a8383"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.download_report_by_id(
                report_id=report_id,
            )
        assert exc_info.value.status == 400

    def test_get_report_by_id(self):
        """Test case for get_report_by_id

        Get report
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        report_id = "575c19e8-c7c3-45b0-8290-2f47397a8383"  # str | The report id

        # Make request
        response = self.api.get_report_by_id(
            report_id=report_id,
        )

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/org-unit/reports/{reportId}" in kwargs["url"]

        # Verify response
        assert isinstance(response, Report)

    def test_get_report_by_id_error(self):
        """Test error handling for get_report_by_id"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters
        report_id = "575c19e8-c7c3-45b0-8290-2f47397a8383"

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.get_report_by_id(
                report_id=report_id,
            )
        assert exc_info.value.status == 400

    def test_list_reports(self):
        """Test case for list_reports

        List reports
        """
        # Mock response
        mock_response = mock.Mock()
        mock_response.status = 200
        mock_response.read.return_value = json.dumps({"data": {}})
        self.mock_request.return_value = mock_response

        # Test parameters
        filter_by = [
            '["name!=some-name"]'
        ]  # List[str] | Filter results by a parameter. Use the format field-name operator value. Operators are == Equals, != Not equals, <= Less than or equal, >= Greater than or equal, =@ contains, !@ Does not contains, =^ Starts with and =$ Ends with. Dates are in ISO 8601 timestamp format and available for operators == None, != None, <= and >=.
        sort_by = (
            runai.ReportFilterAndSortFields()
        )  # ReportFilterAndSortFields | Sort results by a parameters.
        sort_order = asc  # str | Sort results in descending or ascending order.
        offset = 100  # int | The offset of the first item returned in the collection.
        limit = 50  # int | The maximum number of entries to return.
        search = "test project"  # str | Filter results by a free text search.

        # Make request
        response = self.api.list_reports()

        # Verify request was made
        assert self.mock_request.called
        args, kwargs = self.mock_request.call_args

        # Verify request method and URL
        assert kwargs["method"] == "GET"
        assert "/api/v1/org-unit/reports" in kwargs["url"]

        # Verify query parameters
        assert "filterBy=" in kwargs["url"]
        # Verify query parameters
        assert "sortBy=" in kwargs["url"]
        # Verify query parameters
        assert "sortOrder=" in kwargs["url"]
        # Verify query parameters
        assert "offset=" in kwargs["url"]
        # Verify query parameters
        assert "limit=" in kwargs["url"]
        # Verify query parameters
        assert "search=" in kwargs["url"]

        # Verify response
        assert isinstance(response, ListReports200Response)

    def test_list_reports_error(self):
        """Test error handling for list_reports"""
        # Mock error response
        mock_response = mock.Mock()
        mock_response.status = 400
        mock_response.read.return_value = json.dumps({"message": "Error message"})
        self.mock_request.return_value = mock_response

        # Test parameters

        # Verify error handling
        with pytest.raises(ApiException) as exc_info:
            self.api.list_reports()
        assert exc_info.value.status == 400
