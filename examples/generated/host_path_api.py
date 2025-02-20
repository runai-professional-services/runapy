"""
Examples for using the HostPathApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import HostPathApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = HostPathApi(api_client)

def example_create_host_path():
    """
    Example of using create_host_path
    
    Create a host path asset.
    Use to create a hostPath datasource asset.
    """
    try:
        # Prepare the request parameters
        
        # Create example data for HostPathCreationRequest
        host_path_creation_request = models.HostPathCreationRequest(
            meta = {"name":"my-asset","scope":"tenant","workloadSupportedTypes":{"workspace":false,"training":false,"inference":false,"distributed":true,"distFramework":"TF"}},
            spec = {path=/container/directory, mountPath=/local/directory, mountPropagation=None, readOnly=true}
        )

        # Make the API call
        api_response = api_instance.create_host_path(
            host_path_creation_request=host_path_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_host_path: {e}")

def example_delete_host_path_by_id():
    """
    Example of using delete_host_path_by_id
    
    Delete a hostPath asset.
    Use to delete a hostPath datasource asset by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.delete_host_path_by_id(
            asset_id=asset_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling delete_host_path_by_id: {e}")

def example_get_host_path_by_id():
    """
    Example of using get_host_path_by_id
    
    Get a hostPath asset.
    Use to retrieve the details of a hostPath datasource by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        
        
        usage_info = True
        
        
        
        
        
        
        comply_to_project = 42
        
        
        
        
        
        
        comply_to_workload_type = "example_comply_to_workload_type"
        
        
        
        
        
        
        
        comply_to_replica_type = "example_comply_to_replica_type"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_host_path_by_id(
            asset_id=asset_id,
            usage_info=usage_info,
            comply_to_project=comply_to_project,
            comply_to_workload_type=comply_to_workload_type,
            comply_to_replica_type=comply_to_replica_type,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_host_path_by_id: {e}")

def example_list_host_path_assets():
    """
    Example of using list_host_path_assets
    
    List host path assets.
    Retrieve a list of hostPath datasource assets.
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
        api_response = api_instance.list_host_path_assets(
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
        print(f"Exception when calling list_host_path_assets: {e}")

def example_update_host_path_by_id():
    """
    Example of using update_host_path_by_id
    
    Update a hostPath asset.
    Use to update the details of a hostPath datasource by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        
        # Create example data for HostPathUpdateRequest
        host_path_update_request = models.HostPathUpdateRequest(
            meta = {"name":"my-asset"},
            spec = {path=/container/directory, mountPath=/local/directory, mountPropagation=None, readOnly=true}
        )

        # Make the API call
        api_response = api_instance.update_host_path_by_id(
            asset_id=asset_id,
            host_path_update_request=host_path_update_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_host_path_by_id: {e}")

