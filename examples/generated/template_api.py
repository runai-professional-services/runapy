"""
Examples for using the TemplateApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import TemplateApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = TemplateApi(api_client)

def example_create_template():
    """
    Example of using create_template
    
    Create a template.
    Use to create a template.
    """
    try:
        # Prepare the request parameters
        
        # Create example data for WorkloadTemplateCreationRequest
        workload_template_creation_request = models.WorkloadTemplateCreationRequest(
            meta = {"name":"my-asset","scope":"tenant","workloadSupportedTypes":{"workspace":false,"training":false,"inference":false,"distributed":true,"distFramework":"TF"}},
            spec = runai.models.specific_run_creation_fields.SpecificRunCreationFields(
                    assets = runai.models.assets_ids.AssetsIds(
                        environment = '0', 
                        compute = '', 
                        datasources = [
                            runai.models.asset_id_and_kind.AssetIdAndKind(
                                id = '0', 
                                kind = 'compute', 
                                overrides = {containerPath=/container/directory}, )
                            ], 
                        workload_volumes = [
                            ''
                            ], ), 
                    specific_env = {terminationGracePeriodSeconds=20, autoScaling={maxReplicas=1, initialReplicas=0, scaleToZeroRetentionSeconds=1301, metricThresholdPercentage=15.511548, minReplicas=0, activationReplicas=1, scaleDownDelaySeconds=729, initializationTimeoutSeconds=1, thresholdMetric=http_requests_total, concurrencyHardLimit=0, thresholdValue=7}, terminateAfterPreemption=false, backoffLimit=3, parallelism=1, autoDeletionTimeAfterCompletionSeconds=15, annotations=[Ljava.lang.Object;@624b523, completions=1, nodeType=my-node-type, restartPolicy=Always, command=python, runAsUid=500, labels=[Ljava.lang.Object;@50b46e24, args=-x my-script.py, tolerations=[Ljava.lang.Object;@1c30cb85, environmentVariables=[Ljava.lang.Object;@577bf0aa, servingPortAccess={}, runAsGid=30, supplementalGroups=2,3,5,8, allowOverQuota=true, nodePools=["my-node-pool-a","my-node-pool-b"], podAffinity={type=Required, key=key}, connections=[Ljava.lang.Object;@7455dacb}, )
        )

        # Make the API call
        api_response = api_instance.create_template(
            workload_template_creation_request=workload_template_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_template: {e}")

def example_delete_template_by_id():
    """
    Example of using delete_template_by_id
    
    Delete a template.
    Use to delete a template by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.delete_template_by_id(
            asset_id=asset_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling delete_template_by_id: {e}")

def example_get_template_by_id():
    """
    Example of using get_template_by_id
    
    Get a template.
    Retrieve the details of a template by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_template_by_id(
            asset_id=asset_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_template_by_id: {e}")

def example_list_templates():
    """
    Example of using list_templates
    
    List templates.
    Retrieve a list of templates.
    """
    try:
        # Prepare the request parameters
        name = "example_name"
        
        
        
        
        
        
        
        scope = "example_scope"
        
        
        
        
        
        
        
        
        project_id = 42
        
        
        
        
        
        
        department_id = "example_department_id"
        
        
        
        
        
        
        
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        
        distributed_framework = "example_distributed_framework"
        
        
        
        
        
        
        
        
        
        is_distributed = True
        
        
        
        
        
        
        
        is_training = True
        
        
        
        
        
        
        
        is_workspace = True
        
        
        
        
        

        # Make the API call
        api_response = api_instance.list_templates(
            name=name,
            scope=scope,
            project_id=project_id,
            department_id=department_id,
            cluster_id=cluster_id,
            distributed_framework=distributed_framework,
            is_distributed=is_distributed,
            is_training=is_training,
            is_workspace=is_workspace,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_templates: {e}")

def example_update_template():
    """
    Example of using update_template
    
    Update a template.
    Use to update the details of a template by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        
        # Create example data for WorkloadTemplateUpdateRequest
        workload_template_update_request = models.WorkloadTemplateUpdateRequest(
            meta = {"name":"my-asset"},
            spec = runai.models.specific_run_creation_fields.SpecificRunCreationFields(
                    assets = runai.models.assets_ids.AssetsIds(
                        environment = '0', 
                        compute = '', 
                        datasources = [
                            runai.models.asset_id_and_kind.AssetIdAndKind(
                                id = '0', 
                                kind = 'compute', 
                                overrides = {containerPath=/container/directory}, )
                            ], 
                        workload_volumes = [
                            ''
                            ], ), 
                    specific_env = {terminationGracePeriodSeconds=20, autoScaling={maxReplicas=1, initialReplicas=0, scaleToZeroRetentionSeconds=1301, metricThresholdPercentage=15.511548, minReplicas=0, activationReplicas=1, scaleDownDelaySeconds=729, initializationTimeoutSeconds=1, thresholdMetric=http_requests_total, concurrencyHardLimit=0, thresholdValue=7}, terminateAfterPreemption=false, backoffLimit=3, parallelism=1, autoDeletionTimeAfterCompletionSeconds=15, annotations=[Ljava.lang.Object;@624b523, completions=1, nodeType=my-node-type, restartPolicy=Always, command=python, runAsUid=500, labels=[Ljava.lang.Object;@50b46e24, args=-x my-script.py, tolerations=[Ljava.lang.Object;@1c30cb85, environmentVariables=[Ljava.lang.Object;@577bf0aa, servingPortAccess={}, runAsGid=30, supplementalGroups=2,3,5,8, allowOverQuota=true, nodePools=["my-node-pool-a","my-node-pool-b"], podAffinity={type=Required, key=key}, connections=[Ljava.lang.Object;@7455dacb}, )
        )

        # Make the API call
        api_response = api_instance.update_template(
            asset_id=asset_id,
            workload_template_update_request=workload_template_update_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_template: {e}")

