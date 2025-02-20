"""
Examples for using the AuditLogsApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import AuditLogsApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = AuditLogsApi(api_client)


def example_download_audit_logs():
    """
    Example of using download_audit_logs

    Download audit logs
    Download audit logs as a file, based on query params filter
    """
    try:
        # Prepare the request parameters

        start = "2024-12-29T12:00:00Z"

        end = "2024-12-29T12:00:00Z"
        file_type = "example_file_type"

        number_of_samples = 42

        filter_by = ["example_item_1", "example_item_2"]

        # Make the API call
        api_instance.download_audit_logs(
            start=start,
            end=end,
            file_type=file_type,
            number_of_samples=number_of_samples,
            filter_by=filter_by,
        )

    except Exception as e:
        print(f"Exception when calling download_audit_logs: {e}")


def example_get_audit_logs():
    """
    Example of using get_audit_logs

    Get audit logs
    Get audit logs based on query params filter
    """
    try:
        # Prepare the request parameters

        start = "2024-12-29T12:00:00Z"

        end = "2024-12-29T12:00:00Z"

        offset = 42

        number_of_samples = 42

        sort_order = "example_sort_order"

        sort_by = "example_sort_by"

        filter_by = ["example_item_1", "example_item_2"]

        # Make the API call
        api_response = api_instance.get_audit_logs(
            start=start,
            end=end,
            offset=offset,
            number_of_samples=number_of_samples,
            sort_order=sort_order,
            sort_by=sort_by,
            filter_by=filter_by,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_audit_logs: {e}")
