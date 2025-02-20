"""
Examples for using the ReportsApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import ReportsApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = ReportsApi(api_client)


def example_are_reports_available():
    """
    Example of using are_reports_available

    Reports availability

    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.are_reports_available()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling are_reports_available: {e}")


def example_count_reports():
    """
    Example of using count_reports

    Count reports

    """
    try:
        # Prepare the request parameters

        filter_by = ["example_item_1", "example_item_2"]

        search = "example_search"

        # Make the API call
        api_response = api_instance.count_reports(
            filter_by=filter_by,
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling count_reports: {e}")


def example_create_report():
    """
    Example of using create_report

    Create a new report request.

    """
    try:
        # Prepare the request parameters

        # Create example data for ReportRequestFields
        report_request_fields = models.ReportRequestFields(
            name="2023 GPU report",
            description="This report shows the GPU usage of all projects in the organization",
            start="2023-06-07T09:09:18.211Z",
            end="2023-06-07T12:09:18.211Z",
            group_by="Nodepool",
            filter_by=["projectName==some-name"],
        )

        # Make the API call
        api_response = api_instance.create_report(
            report_request_fields=report_request_fields,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_report: {e}")


def example_delete_report_by_id():
    """
    Example of using delete_report_by_id

    Delete report

    """
    try:
        # Prepare the request parameters
        report_id = "example_report_id"

        # Make the API call
        api_instance.delete_report_by_id(
            report_id=report_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_report_by_id: {e}")


def example_download_report_by_id():
    """
    Example of using download_report_by_id

    Download report

    """
    try:
        # Prepare the request parameters
        report_id = "example_report_id"

        # Make the API call
        api_instance.download_report_by_id(
            report_id=report_id,
        )

    except Exception as e:
        print(f"Exception when calling download_report_by_id: {e}")


def example_get_report_by_id():
    """
    Example of using get_report_by_id

    Get report

    """
    try:
        # Prepare the request parameters
        report_id = "example_report_id"

        # Make the API call
        api_response = api_instance.get_report_by_id(
            report_id=report_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_report_by_id: {e}")


def example_list_reports():
    """
    Example of using list_reports

    List reports

    """
    try:
        # Prepare the request parameters

        filter_by = ["example_item_1", "example_item_2"]

        sort_order = "example_sort_order"

        offset = 42

        limit = 42

        search = "example_search"

        # Make the API call
        api_response = api_instance.list_reports(
            filter_by=filter_by,
            sort_by=sort_by,
            sort_order=sort_order,
            offset=offset,
            limit=limit,
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_reports: {e}")
