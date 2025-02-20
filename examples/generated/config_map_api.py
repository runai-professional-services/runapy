"""
Examples for using the ConfigMapApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import ConfigMapApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = ConfigMapApi(api_client)

def example_create_config_map_asset():
    """
    Example of using create_config_map_asset
    
    Create a ConfigMap datasource asset.
    Use to create a ConfigMap datasource asset.
    """
    try:
        # Prepare the request parameters
        
        # Create example data for ConfigMapCreationRequest
        config_map_creation_request = models.ConfigMapCreationRequest(
            meta = {"name":"my-asset","scope":"tenant","workloadSupportedTypes":{"workspace":false,"training":false,"inference":false,"distributed":true,"distFramework":"TF"}},
            spec = {mountPath=mountPath, configMap=configMap}
        )

        # Make the API call
        api_response = api_instance.create_config_map_asset(
            config_map_creation_request=config_map_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_config_map_asset: {e}")

def example_delete_config_map_asset_by_id():
    """
    Example of using delete_config_map_asset_by_id
    
    Delete a ConfigMap asset.
    Use to delete a ConfigMap datasource asset by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.delete_config_map_asset_by_id(
            asset_id=asset_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling delete_config_map_asset_by_id: {e}")

def example_get_config_map_asset_by_id():
    """
    Example of using get_config_map_asset_by_id
    
    Get a ConfigMap asset.
    Retrieve the details of ConfigMap datasource asset by id.
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
        api_response = api_instance.get_config_map_asset_by_id(
            asset_id=asset_id,
            usage_info=usage_info,
            comply_to_project=comply_to_project,
            comply_to_workload_type=comply_to_workload_type,
            status_info=status_info,
            comply_to_replica_type=comply_to_replica_type,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_config_map_asset_by_id: {e}")

def example_list_config_map_assets():
    """
    Example of using list_config_map_assets
    
    List ConfigMap datasource assets.
    Retrieve a list of ConfigMap datasource assets.
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
        api_response = api_instance.list_config_map_assets(
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
        print(f"Exception when calling list_config_map_assets: {e}")

def example_update_config_map_asset_by_id():
    """
    Example of using update_config_map_asset_by_id
    
    Update a ConfigMap asset.
    Use to update the details of a ConfigMap datasource asset by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        
        # Create example data for ConfigMapUpdateRequest
        config_map_update_request = models.ConfigMapUpdateRequest(
            meta = {"name":"my-asset"}
        )

        # Make the API call
        api_response = api_instance.update_config_map_asset_by_id(
            asset_id=asset_id,
            config_map_update_request=config_map_update_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_config_map_asset_by_id: {e}")

