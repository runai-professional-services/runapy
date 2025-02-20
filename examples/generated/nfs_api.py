"""
Examples for using the NFSApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import NFSApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = NFSApi(api_client)

def example_create_nfs_asset():
    """
    Example of using create_nfs_asset
    
    Create an NFS asset.
    Use to create an NFS datasource asset.
    """
    try:
        # Prepare the request parameters
        
        # Create example data for NFSCreationRequest
        nfs_creation_request = models.NFSCreationRequest(
            meta = {"name":"my-asset","scope":"tenant","workloadSupportedTypes":{"workspace":false,"training":false,"inference":false,"distributed":true,"distFramework":"TF"}},
            spec = {path=/container/nfs, server=my.nfs.com, mountPath=/local/nfs, readOnly=true}
        )

        # Make the API call
        api_response = api_instance.create_nfs_asset(
            nfs_creation_request=nfs_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_nfs_asset: {e}")

def example_delete_nfs_asset_by_id():
    """
    Example of using delete_nfs_asset_by_id
    
    Delete an NFS asset.
    Use to delete an NFS datasource asset by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.delete_nfs_asset_by_id(
            asset_id=asset_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling delete_nfs_asset_by_id: {e}")

def example_get_nfs_asset_by_id():
    """
    Example of using get_nfs_asset_by_id
    
    Get an NFS asset.
    Use to retrieve the details of NFS datasource asset by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        
        
        usage_info = True
        
        
        
        
        
        
        comply_to_project = 42
        
        
        
        
        
        
        comply_to_workload_type = "example_comply_to_workload_type"
        
        
        
        
        
        
        
        comply_to_replica_type = "example_comply_to_replica_type"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_nfs_asset_by_id(
            asset_id=asset_id,
            usage_info=usage_info,
            comply_to_project=comply_to_project,
            comply_to_workload_type=comply_to_workload_type,
            comply_to_replica_type=comply_to_replica_type,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_nfs_asset_by_id: {e}")

def example_list_nfs_assets():
    """
    Example of using list_nfs_assets
    
    List NFS assets.
    Retrieve a list of NFS datasource assets.
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
        
        
        
        
        
        
        
        asset_ids = "example_asset_ids"
        
        
        
        
        
        
        
        comply_to_replica_type = "example_comply_to_replica_type"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.list_nfs_assets(
            name=name,
            scope=scope,
            project_id=project_id,
            department_id=department_id,
            cluster_id=cluster_id,
            usage_info=usage_info,
            comply_to_project=comply_to_project,
            comply_to_workload_type=comply_to_workload_type,
            asset_ids=asset_ids,
            comply_to_replica_type=comply_to_replica_type,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_nfs_assets: {e}")

def example_update_nfs_asset_by_id():
    """
    Example of using update_nfs_asset_by_id
    
    Update an NFS asset.
    Use to update the details of NFS datasource asset by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        
        # Create example data for NFSUpdateRequest
        nfs_update_request = models.NFSUpdateRequest(
            meta = {"name":"my-asset"},
            spec = {path=/container/nfs, server=my.nfs.com, mountPath=/local/nfs, readOnly=true}
        )

        # Make the API call
        api_response = api_instance.update_nfs_asset_by_id(
            asset_id=asset_id,
            nfs_update_request=nfs_update_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_nfs_asset_by_id: {e}")

