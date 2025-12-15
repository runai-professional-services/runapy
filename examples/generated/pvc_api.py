"""
Examples for using the PVCApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import PVCApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = PVCApi(api_client)

def example_create_pvc_asset():
    """
    Example of using create_pvc_asset
    
    Create a PVC asset.
    Use to create a PVC datasource asset.
    """
    try:
        # Prepare the request parameters
        
        # Create example data for PVCCreationRequest
        pvc_creation_request = models.PVCCreationRequest(
            meta = {"name":"my-asset","scope":"tenant","workloadSupportedTypes":{"workspace":false,"training":false,"inference":false,"distributed":true,"distFramework":"TF"}},
            spec = {path=/container/my-claim, claimName=my-claim, dataSharing=false, claimInfo={storageClass=my-storage-class, addedAttrValues=[Ljava.lang.Object;@7d0cd23c, size=1G, accessModes={readOnlyMany=false, readWriteMany=false, readWriteOnce=true}, volumeMode=Filesystem}, ephemeral=false, readOnly=false, existingPvc=false}
        )

        # Make the API call
        api_response = api_instance.create_pvc_asset(
            pvc_creation_request=pvc_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_pvc_asset: {e}")

def example_delete_pvc_asset_by_id():
    """
    Example of using delete_pvc_asset_by_id
    
    Delete a PVC asset.
    Use to delete a PVC datasource asset by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.delete_pvc_asset_by_id(
            asset_id=asset_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling delete_pvc_asset_by_id: {e}")

def example_get_pvc_asset_by_id():
    """
    Example of using get_pvc_asset_by_id
    
    Get a PVC asset.
    Retrieve the details of a PVC datasource asset by id.
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
        api_response = api_instance.get_pvc_asset_by_id(
            asset_id=asset_id,
            usage_info=usage_info,
            comply_to_project=comply_to_project,
            comply_to_workload_type=comply_to_workload_type,
            status_info=status_info,
            comply_to_replica_type=comply_to_replica_type,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_pvc_asset_by_id: {e}")

def example_get_pvc_history():
    """
    Example of using get_pvc_history
    
    Get the PVC history.
    Retrieve PVC history details, including events, using a PVC id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        
        offset = 42
        
        
        
        
        
        
        
        limit = 42
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_pvc_history(
            asset_id=asset_id,
            offset=offset,
            limit=limit,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_pvc_history: {e}")

def example_list_pvc_assets():
    """
    Example of using list_pvc_assets
    
    List PVC assets.
    Retrieves a list of PVC datasource assets.
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
        api_response = api_instance.list_pvc_assets(
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
        print(f"Exception when calling list_pvc_assets: {e}")

def example_update_pvc_asset_by_id():
    """
    Example of using update_pvc_asset_by_id
    
    Update a PVC asset.
    Use to update the details of a PVC datasource asset by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        
        # Create example data for PVCUpdateRequest
        pvc_update_request = models.PVCUpdateRequest(
            meta = {"name":"my-asset"},
            spec = runai.models.pvc_fields_updatable.PvcFieldsUpdatable(
                    path = '/container/my-claim', )
        )

        # Make the API call
        api_response = api_instance.update_pvc_asset_by_id(
            asset_id=asset_id,
            pvc_update_request=pvc_update_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_pvc_asset_by_id: {e}")

