"""
Examples for using the GitApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import GitApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = GitApi(api_client)

def example_create_git_asset():
    """
    Example of using create_git_asset
    
    Create a Git asset.
    Use to create a a Git datasource asset.
    """
    try:
        # Prepare the request parameters
        
        # Create example data for GitCreationRequest
        git_creation_request = models.GitCreationRequest(
            meta = {"name":"my-asset","scope":"tenant","workloadSupportedTypes":{"workspace":false,"training":false,"inference":false,"distributed":true,"distFramework":"TF"}},
            spec = {path=/container/my-repository, repository=https://github.com/my-git/my-repo, branch=main, passwordAssetId=046b6c7f-0b8a-43b9-b35d-6489e6daee91, revision=revision}
        )

        # Make the API call
        api_response = api_instance.create_git_asset(
            git_creation_request=git_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_git_asset: {e}")

def example_delete_git_asset_by_id():
    """
    Example of using delete_git_asset_by_id
    
    Delete a Git asset.
    Use to delete a Git datasource asset by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.delete_git_asset_by_id(
            asset_id=asset_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling delete_git_asset_by_id: {e}")

def example_get_git_asset_by_id():
    """
    Example of using get_git_asset_by_id
    
    Get a Git asset.
    Use to retrieve the details of a Git datasource asset by id.
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
        api_response = api_instance.get_git_asset_by_id(
            asset_id=asset_id,
            usage_info=usage_info,
            comply_to_project=comply_to_project,
            comply_to_workload_type=comply_to_workload_type,
            status_info=status_info,
            comply_to_replica_type=comply_to_replica_type,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_git_asset_by_id: {e}")

def example_list_git_assets():
    """
    Example of using list_git_assets
    
    List Git assets.
    Retrieve a list of Git datasource assets.
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
        api_response = api_instance.list_git_assets(
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
        print(f"Exception when calling list_git_assets: {e}")

def example_update_git_asset_by_id():
    """
    Example of using update_git_asset_by_id
    
    Update a Git asset.
    Use to update the details of Git datasource asset by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        
        # Create example data for GitUpdateRequest
        git_update_request = models.GitUpdateRequest(
            meta = {"name":"my-asset"},
            spec = {path=/container/my-repository, repository=https://github.com/my-git/my-repo, branch=main, passwordAssetId=046b6c7f-0b8a-43b9-b35d-6489e6daee91, revision=revision}
        )

        # Make the API call
        api_response = api_instance.update_git_asset_by_id(
            asset_id=asset_id,
            git_update_request=git_update_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_git_asset_by_id: {e}")

