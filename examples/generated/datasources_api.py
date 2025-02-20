"""
Examples for using the DatasourcesApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import DatasourcesApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = DatasourcesApi(api_client)


def example_list_datasource_assets():
    """
    Example of using list_datasource_assets

    List datasource assets.
    Returns a combined list of data-sources.
    """
    try:
        # Prepare the request parameters
        name = "example_name"

        scope = "example_scope"

        project_id = 42

        department_id = "example_department_id"

        cluster_id = "example_cluster_id"

        usage_info = True

        comply_to_project = 42

        comply_to_workload_type = "example_comply_to_workload_type"

        status_info = True

        asset_ids = "example_asset_ids"

        comply_to_replica_type = "example_comply_to_replica_type"

        # Make the API call
        api_response = api_instance.list_datasource_assets(
            name=name,
            scope=scope,
            project_id=project_id,
            department_id=department_id,
            cluster_id=cluster_id,
            usage_info=usage_info,
            comply_to_project=comply_to_project,
            comply_to_workload_type=comply_to_workload_type,
            status_info=status_info,
            asset_ids=asset_ids,
            comply_to_replica_type=comply_to_replica_type,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_datasource_assets: {e}")
