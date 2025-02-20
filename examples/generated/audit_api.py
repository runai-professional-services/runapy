"""
Examples for using the AuditApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import AuditApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = AuditApi(api_client)


def example_get_audit_logs():
    """
    Example of using get_audit_logs

    Get audit logs.
    Retrieve audit logs using the query parameters.
    """
    try:
        # Prepare the request parameters

        start = "2024-12-29T12:00:00Z"

        end = "2024-12-29T12:00:00Z"
        cluster_uuid = "example_cluster_uuid"

        action = "example_action"

        source_type = "example_source_type"

        source_id = "example_source_id"

        source_name = "example_source_name"

        entity_type = "example_entity_type"

        entity_id = "example_entity_id"

        limit = 42

        offset = 42

        success = "example_success"

        download = "example_download"

        # Make the API call
        api_response = api_instance.get_audit_logs(
            start=start,
            end=end,
            cluster_uuid=cluster_uuid,
            action=action,
            source_type=source_type,
            source_id=source_id,
            source_name=source_name,
            entity_type=entity_type,
            entity_id=entity_id,
            limit=limit,
            offset=offset,
            success=success,
            download=download,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_audit_logs: {e}")
