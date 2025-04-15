"""
Examples for using the EnvironmentApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import EnvironmentApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = EnvironmentApi(api_client)

def example_create_environment_asset():
    """
    Example of using create_environment_asset
    
    Create an environment asset.
    Use to create an environment asset.
    """
    try:
        # Prepare the request parameters
        
        # Create example data for EnvironmentCreationRequest
        environment_creation_request = models.EnvironmentCreationRequest(
            meta = {"name":"my-asset","scope":"tenant","workloadSupportedTypes":{"workspace":false,"training":false,"inference":false,"distributed":true,"distFramework":"TF"}},
            spec = {image=python:3.8, imagePullPolicy=Always, stdin=true, capabilities=["CHOWN","KILL"], uidGidSource=fromTheImage, hostNetwork=false, workingDir=/home/myfolder, hostIpc=false, command=python, runAsUid=500, runAsNonRoot=true, readOnlyRootFilesystem=false, args=-x my-script.py, overrideUidGidInWorkspace=false, environmentVariables=[Ljava.lang.Object;@4ac9a1ff, runAsGid=30, tty=true, supplementalGroups=2,3,5,8, createHomeDir=true, probes={readiness={handler={httpGet={path=/, scheme=HTTP, port=15087, host=example.com}}, failureThreshold=1, periodSeconds=1, timeoutSeconds=1, successThreshold=1, initialDelaySeconds=0}}, allowPrivilegeEscalation=false, seccompProfileType=RuntimeDefault, connections=[Ljava.lang.Object;@6c7114db}
        )

        # Make the API call
        api_response = api_instance.create_environment_asset(
            environment_creation_request=environment_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_environment_asset: {e}")

def example_delete_environment_asset_by_id():
    """
    Example of using delete_environment_asset_by_id
    
    Delete an environment asset.
    Use to delete an environment asset by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.delete_environment_asset_by_id(
            asset_id=asset_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling delete_environment_asset_by_id: {e}")

def example_get_environment_asset_by_id():
    """
    Example of using get_environment_asset_by_id
    
    Get an environment asset.
    Use to retrieve the details of environment asset by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        
        
        usage_info = True
        
        
        
        
        
        
        comply_to_project = 42
        
        
        
        
        
        
        comply_to_workload_type = "example_comply_to_workload_type"
        
        
        
        
        
        
        
        comply_to_replica_type = "example_comply_to_replica_type"
        
        
        
        
        
        
        
        
        
        status_info = True
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_environment_asset_by_id(
            asset_id=asset_id,
            usage_info=usage_info,
            comply_to_project=comply_to_project,
            comply_to_workload_type=comply_to_workload_type,
            comply_to_replica_type=comply_to_replica_type,
            status_info=status_info,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_environment_asset_by_id: {e}")

def example_list_environment_assets():
    """
    Example of using list_environment_assets
    
    List environment assets.
    Use to retrieve a list of environment assets.
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
        
        
        
        
        
        
        
        distributed_framework = "example_distributed_framework"
        
        
        
        
        
        
        
        
        
        is_distributed = True
        
        
        
        
        
        
        
        is_training = True
        
        
        
        
        
        
        
        is_workspace = True
        
        
        
        
        
        
        
        is_inference = True
        
        
        
        
        
        comply_to_replica_type = "example_comply_to_replica_type"
        
        
        
        
        
        
        
        
        
        status_info = True
        
        
        
        
        

        # Make the API call
        api_response = api_instance.list_environment_assets(
            name=name,
            scope=scope,
            project_id=project_id,
            department_id=department_id,
            cluster_id=cluster_id,
            usage_info=usage_info,
            comply_to_project=comply_to_project,
            comply_to_workload_type=comply_to_workload_type,
            distributed_framework=distributed_framework,
            is_distributed=is_distributed,
            is_training=is_training,
            is_workspace=is_workspace,
            is_inference=is_inference,
            comply_to_replica_type=comply_to_replica_type,
            status_info=status_info,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_environment_assets: {e}")

def example_update_environment_asset_by_id():
    """
    Example of using update_environment_asset_by_id
    
    Update an environment asset.
    Use to update the details of environment asset by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        
        # Create example data for EnvironmentUpdateRequest
        environment_update_request = models.EnvironmentUpdateRequest(
            meta = {"name":"my-asset"},
            spec = {image=python:3.8, imagePullPolicy=Always, stdin=true, capabilities=["CHOWN","KILL"], uidGidSource=fromTheImage, hostNetwork=false, workingDir=/home/myfolder, hostIpc=false, command=python, runAsUid=500, runAsNonRoot=true, readOnlyRootFilesystem=false, args=-x my-script.py, overrideUidGidInWorkspace=false, environmentVariables=[Ljava.lang.Object;@4ac9a1ff, runAsGid=30, tty=true, supplementalGroups=2,3,5,8, createHomeDir=true, probes={readiness={handler={httpGet={path=/, scheme=HTTP, port=15087, host=example.com}}, failureThreshold=1, periodSeconds=1, timeoutSeconds=1, successThreshold=1, initialDelaySeconds=0}}, allowPrivilegeEscalation=false, seccompProfileType=RuntimeDefault, connections=[Ljava.lang.Object;@6c7114db}
        )

        # Make the API call
        api_response = api_instance.update_environment_asset_by_id(
            asset_id=asset_id,
            environment_update_request=environment_update_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_environment_asset_by_id: {e}")

