"""
Examples for using the ComputeApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import ComputeApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = ComputeApi(api_client)

def example_create_compute_asset():
    """
    Example of using create_compute_asset
    
    Create compute asset.
    Use to create a compute asset.
    """
    try:
        # Prepare the request parameters
        
        # Create example data for ComputeCreationRequest
        compute_creation_request = models.ComputeCreationRequest(
            meta = {"name":"my-asset","scope":"tenant","workloadSupportedTypes":{"workspace":false,"training":false,"inference":false,"distributed":true,"distFramework":"TF"}},
            spec = {cpuMemoryLimit=30M, extendedResources=[Ljava.lang.Object;@5b02a984, gpuMemoryRequest=10M, gpuPortionRequest=0.5, gpuMemoryLimit=10M, cpuCoreLimit=2, largeShmRequest=false, cpuCoreRequest=0.5, gpuPortionLimit=0.5, gpuRequestType=portion, cpuMemoryRequest=20M, gpuDevicesRequest=1}
        )

        # Make the API call
        api_response = api_instance.create_compute_asset(
            compute_creation_request=compute_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_compute_asset: {e}")

def example_delete_compute_asset_by_id():
    """
    Example of using delete_compute_asset_by_id
    
    Delete a compute asset.
    Use to delete a compute asset, by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.delete_compute_asset_by_id(
            asset_id=asset_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling delete_compute_asset_by_id: {e}")

def example_get_compute_asset_by_id():
    """
    Example of using get_compute_asset_by_id
    
    Retrieve a compute asset.
    Use to retrieve the details of a compute asset by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        
        
        usage_info = True
        
        
        
        
        
        
        comply_to_project = 42
        
        
        
        
        
        
        comply_to_workload_type = "example_comply_to_workload_type"
        
        
        
        
        
        
        
        comply_to_replica_type = "example_comply_to_replica_type"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_compute_asset_by_id(
            asset_id=asset_id,
            usage_info=usage_info,
            comply_to_project=comply_to_project,
            comply_to_workload_type=comply_to_workload_type,
            comply_to_replica_type=comply_to_replica_type,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_compute_asset_by_id: {e}")

def example_list_compute_assets():
    """
    Example of using list_compute_assets
    
    List compute assets.
    Use to retrieve a list of compute assets.
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
        
        
        
        
        
        
        
        comply_to_replica_type = "example_comply_to_replica_type"
        
        
        
        
        
        
        
        
        
        include_descendants = True
        
        
        
        
        

        # Make the API call
        api_response = api_instance.list_compute_assets(
            name=name,
            scope=scope,
            project_id=project_id,
            department_id=department_id,
            cluster_id=cluster_id,
            usage_info=usage_info,
            comply_to_project=comply_to_project,
            comply_to_workload_type=comply_to_workload_type,
            comply_to_replica_type=comply_to_replica_type,
            include_descendants=include_descendants,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_compute_assets: {e}")

def example_update_compute_asset_by_id():
    """
    Example of using update_compute_asset_by_id
    
    Update a compute asset.
    Use to update the details of a compute asset by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        
        # Create example data for ComputeUpdateRequest
        compute_update_request = models.ComputeUpdateRequest(
            meta = {"name":"my-asset"},
            spec = {cpuMemoryLimit=30M, extendedResources=[Ljava.lang.Object;@5b02a984, gpuMemoryRequest=10M, gpuPortionRequest=0.5, gpuMemoryLimit=10M, cpuCoreLimit=2, largeShmRequest=false, cpuCoreRequest=0.5, gpuPortionLimit=0.5, gpuRequestType=portion, cpuMemoryRequest=20M, gpuDevicesRequest=1}
        )

        # Make the API call
        api_response = api_instance.update_compute_asset_by_id(
            asset_id=asset_id,
            compute_update_request=compute_update_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_compute_asset_by_id: {e}")

