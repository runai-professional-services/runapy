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
            start=datetime.datetime.strptime(
                "2013-10-20 19:20:30.00", "%Y-%m-%d %H:%M:%S.%f"
            ),
            end=datetime.datetime.strptime(
                "2013-10-20 19:20:30.00", "%Y-%m-%d %H:%M:%S.%f"
            ),
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
