"""
Examples for using the S3Api
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import S3Api
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = S3Api(api_client)


def example_create_s3_asset():
    """
    Example of using create_s3_asset

    Create an S3 asset.
    Use to create an S3 compatible datasource asset.
    """
    try:
        # Prepare the request parameters

        # Create example data for S3CreationRequest
        s3_creation_request = models.S3CreationRequest(
            meta={
                "name": "my-asset",
                "scope": "tenant",
                "workloadSupportedTypes": {
                    "workspace": false,
                    "training": false,
                    "inference": false,
                    "distributed": true,
                    "distFramework": "TF",
                },
            },
            spec=None,
        )

        # Make the API call
        api_response = api_instance.create_s3_asset(
            s3_creation_request=s3_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_s3_asset: {e}")


def example_delete_s3_asset_by_id():
    """
    Example of using delete_s3_asset_by_id

    Delete an S3 asset.
    Use to delete an S3 compatible datasource asset by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"

        # Make the API call
        api_response = api_instance.delete_s3_asset_by_id(
            asset_id=asset_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling delete_s3_asset_by_id: {e}")


def example_get_s3_asset_by_id():
    """
    Example of using get_s3_asset_by_id

    Get an S3 asset.
    Retrieve the details of S3 compatible datasource asset by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"

        usage_info = True

        comply_to_project = 42

        comply_to_workload_type = "example_comply_to_workload_type"

        status_info = True

        comply_to_replica_type = "example_comply_to_replica_type"

        # Make the API call
        api_response = api_instance.get_s3_asset_by_id(
            asset_id=asset_id,
            usage_info=usage_info,
            comply_to_project=comply_to_project,
            comply_to_workload_type=comply_to_workload_type,
            status_info=status_info,
            comply_to_replica_type=comply_to_replica_type,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_s3_asset_by_id: {e}")


def example_list_s3_assets():
    """
    Example of using list_s3_assets

    List S3 assets.
    Retrieve a list of S3 compatible datasource assets.
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
        api_response = api_instance.list_s3_assets(
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
        print(f"Exception when calling list_s3_assets: {e}")


def example_update_s3_asset_by_id():
    """
    Example of using update_s3_asset_by_id

    Update an S3 asset.
    Use to update the details of an S3 compatible datasource asset by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"

        # Create example data for S3UpdateRequest
        s3_update_request = models.S3UpdateRequest(meta={"name": "my-asset"}, spec=None)

        # Make the API call
        api_response = api_instance.update_s3_asset_by_id(
            asset_id=asset_id,
            s3_update_request=s3_update_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_s3_asset_by_id: {e}")
