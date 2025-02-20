"""
Examples for using the SecretApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import SecretApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = SecretApi(api_client)

def example_create_secret_asset():
    """
    Example of using create_secret_asset
    
    Create a Secret datasource asset.
    Use to create a Secret datasource asset.
    """
    try:
        # Prepare the request parameters
        
        # Create example data for SecretAssetCreationRequest
        secret_asset_creation_request = models.SecretAssetCreationRequest(
            meta = {"name":"my-asset","scope":"tenant","workloadSupportedTypes":{"workspace":false,"training":false,"inference":false,"distributed":true,"distFramework":"TF"}},
            spec = {mountPath=mountPath, credentialAssetId=046b6c7f-0b8a-43b9-b35d-6489e6daee91}
        )

        # Make the API call
        api_response = api_instance.create_secret_asset(
            secret_asset_creation_request=secret_asset_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_secret_asset: {e}")

def example_delete_secret_asset_by_id():
    """
    Example of using delete_secret_asset_by_id
    
    Delete a Secret asset.
    Use to delete a Secret datasource asset by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.delete_secret_asset_by_id(
            asset_id=asset_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling delete_secret_asset_by_id: {e}")

def example_get_secret_asset_by_id():
    """
    Example of using get_secret_asset_by_id
    
    Get a Secret asset.
    Retrieve the details of Secret datasource asset by id.
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
        api_response = api_instance.get_secret_asset_by_id(
            asset_id=asset_id,
            usage_info=usage_info,
            comply_to_project=comply_to_project,
            comply_to_workload_type=comply_to_workload_type,
            status_info=status_info,
            comply_to_replica_type=comply_to_replica_type,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_secret_asset_by_id: {e}")

def example_list_secret_assets():
    """
    Example of using list_secret_assets
    
    List Secret datasource assets.
    Retrieve a list of Secret datasource assets.
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
        api_response = api_instance.list_secret_assets(
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
        print(f"Exception when calling list_secret_assets: {e}")

def example_update_secret_asset_by_id():
    """
    Example of using update_secret_asset_by_id
    
    Update a Secret asset.
    Use to update the details of a Secret datasource asset by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        
        # Create example data for SecretAssetUpdateRequest
        secret_asset_update_request = models.SecretAssetUpdateRequest(
            meta = {"name":"my-asset"}
        )

        # Make the API call
        api_response = api_instance.update_secret_asset_by_id(
            asset_id=asset_id,
            secret_asset_update_request=secret_asset_update_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_secret_asset_by_id: {e}")

