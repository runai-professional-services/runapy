"""
Examples for using the PolicyApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import PolicyApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = PolicyApi(api_client)

def example_apply_gvk_policy():
    """
    Example of using apply_gvk_policy
    
    Replace a policy. [experimental]
    Replace an existing policy&#39;s rules and description.
    """
    try:
        # Prepare the request parameters
        policy_id = "example_policy_id"
        
        
        
        
        
        
        
        
        # Create example data for UpdateGvkPolicyReq
        update_gvk_policy_req = models.UpdateGvkPolicyReq(
        )

        # Make the API call
        api_response = api_instance.apply_gvk_policy(
            policy_id=policy_id,
            update_gvk_policy_req=update_gvk_policy_req,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling apply_gvk_policy: {e}")

def example_create_gvk_policy():
    """
    Example of using create_gvk_policy
    
    Create a policy. [experimental]
    Create a policy for a specific workload type based on the provided specification.
    """
    try:
        # Prepare the request parameters
        
        # Create example data for CreateGvkPolicyReq
        create_gvk_policy_req = models.CreateGvkPolicyReq(
        )

        # Make the API call
        api_response = api_instance.create_gvk_policy(
            create_gvk_policy_req=create_gvk_policy_req,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_gvk_policy: {e}")

def example_delete_distributed_inference_policy():
    """
    Example of using delete_distributed_inference_policy
    
    Delete a distributed inference policy.
    Use to delete a distributed inference policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters
        scope = "example_scope"
        
        
        
        
        
        
        
        department_id = "example_department_id"
        
        
        
        
        
        
        
        project_id = "example_project_id"
        
        
        
        
        
        
        
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        
        
        
        approve_cluster_deletion = True
        
        
        
        
        

        # Make the API call
        api_instance.delete_distributed_inference_policy(
            scope=scope,
            department_id=department_id,
            project_id=project_id,
            cluster_id=cluster_id,
            approve_cluster_deletion=approve_cluster_deletion,
        )

    except Exception as e:
        print(f"Exception when calling delete_distributed_inference_policy: {e}")

def example_delete_distributed_policy():
    """
    Example of using delete_distributed_policy
    
    Delete a distributed policy.
    Use to delete a distributed policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters
        scope = "example_scope"
        
        
        
        
        
        
        
        department_id = "example_department_id"
        
        
        
        
        
        
        
        project_id = "example_project_id"
        
        
        
        
        
        
        
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        
        
        
        approve_cluster_deletion = True
        
        
        
        
        

        # Make the API call
        api_instance.delete_distributed_policy(
            scope=scope,
            department_id=department_id,
            project_id=project_id,
            cluster_id=cluster_id,
            approve_cluster_deletion=approve_cluster_deletion,
        )

    except Exception as e:
        print(f"Exception when calling delete_distributed_policy: {e}")

def example_delete_gvk_policy():
    """
    Example of using delete_gvk_policy
    
    Delete a policy. [experimental]
    Delete an existing policy and all of its rules.
    """
    try:
        # Prepare the request parameters
        policy_id = "example_policy_id"
        
        
        
        
        
        
        

        # Make the API call
        api_instance.delete_gvk_policy(
            policy_id=policy_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_gvk_policy: {e}")

def example_delete_gvk_policy_rules():
    """
    Example of using delete_gvk_policy_rules
    
    Delete rules from a policy. [experimental]
    Delete one or more rules from an existing policy by reference.
    """
    try:
        # Prepare the request parameters
        policy_id = "example_policy_id"
        
        
        
        
        
        
        
        
        # Create example data for DeleteGvkPolicyRulesReq
        delete_gvk_policy_rules_req = models.DeleteGvkPolicyRulesReq(
        )

        # Make the API call
        api_response = api_instance.delete_gvk_policy_rules(
            policy_id=policy_id,
            delete_gvk_policy_rules_req=delete_gvk_policy_rules_req,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling delete_gvk_policy_rules: {e}")

def example_delete_inference_policy():
    """
    Example of using delete_inference_policy
    
    Delete an inference policy.
    Use to delete an inference policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters
        scope = "example_scope"
        
        
        
        
        
        
        
        department_id = "example_department_id"
        
        
        
        
        
        
        
        project_id = "example_project_id"
        
        
        
        
        
        
        
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        
        
        
        approve_cluster_deletion = True
        
        
        
        
        

        # Make the API call
        api_instance.delete_inference_policy(
            scope=scope,
            department_id=department_id,
            project_id=project_id,
            cluster_id=cluster_id,
            approve_cluster_deletion=approve_cluster_deletion,
        )

    except Exception as e:
        print(f"Exception when calling delete_inference_policy: {e}")

def example_delete_nim_service_policy():
    """
    Example of using delete_nim_service_policy
    
    Delete NVIDIA NIM service policy.
    Use to delete NVIDIA NIM service policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters
        scope = "example_scope"
        
        
        
        
        
        
        
        department_id = "example_department_id"
        
        
        
        
        
        
        
        project_id = "example_project_id"
        
        
        
        
        
        
        
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        

        # Make the API call
        api_instance.delete_nim_service_policy(
            scope=scope,
            department_id=department_id,
            project_id=project_id,
            cluster_id=cluster_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_nim_service_policy: {e}")

def example_delete_training_policy():
    """
    Example of using delete_training_policy
    
    Delete a training policy.
    Use to delete a training policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters
        scope = "example_scope"
        
        
        
        
        
        
        
        department_id = "example_department_id"
        
        
        
        
        
        
        
        project_id = "example_project_id"
        
        
        
        
        
        
        
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        
        
        
        approve_cluster_deletion = True
        
        
        
        
        

        # Make the API call
        api_instance.delete_training_policy(
            scope=scope,
            department_id=department_id,
            project_id=project_id,
            cluster_id=cluster_id,
            approve_cluster_deletion=approve_cluster_deletion,
        )

    except Exception as e:
        print(f"Exception when calling delete_training_policy: {e}")

def example_delete_workspace_policy():
    """
    Example of using delete_workspace_policy
    
    Delete a workspace policy.
    Use to delete a workspace policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters
        scope = "example_scope"
        
        
        
        
        
        
        
        department_id = "example_department_id"
        
        
        
        
        
        
        
        project_id = "example_project_id"
        
        
        
        
        
        
        
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        
        
        
        approve_cluster_deletion = True
        
        
        
        
        

        # Make the API call
        api_instance.delete_workspace_policy(
            scope=scope,
            department_id=department_id,
            project_id=project_id,
            cluster_id=cluster_id,
            approve_cluster_deletion=approve_cluster_deletion,
        )

    except Exception as e:
        print(f"Exception when calling delete_workspace_policy: {e}")

def example_get_distributed_inference_policy_v2():
    """
    Example of using get_distributed_inference_policy_v2
    
    Get a distributed inference policy.
    Retrieve the details of a distributed inference policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters
        scope = "example_scope"
        
        
        
        
        
        
        
        department_id = "example_department_id"
        
        
        
        
        
        
        
        project_id = "example_project_id"
        
        
        
        
        
        
        
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_distributed_inference_policy_v2(
            scope=scope,
            department_id=department_id,
            project_id=project_id,
            cluster_id=cluster_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_distributed_inference_policy_v2: {e}")

def example_get_distributed_policy_v2():
    """
    Example of using get_distributed_policy_v2
    
    Get a distributed policy.
    Retrieve the details of a distributed policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters
        scope = "example_scope"
        
        
        
        
        
        
        
        department_id = "example_department_id"
        
        
        
        
        
        
        
        project_id = "example_project_id"
        
        
        
        
        
        
        
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_distributed_policy_v2(
            scope=scope,
            department_id=department_id,
            project_id=project_id,
            cluster_id=cluster_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_distributed_policy_v2: {e}")

def example_get_effective_policy():
    """
    Example of using get_effective_policy
    
    Get the effective policy by type and scope. The effective policy is a combination of the policy provided for the given scope (if exist) and the effective policies of its parent scopes.
    
    """
    try:
        # Prepare the request parameters
        
        # Create example data for WorkloadTypeAndScope
        workload_type_and_scope = models.WorkloadTypeAndScope(
            workload_type = runai.models.gvk.GVK(
                    group = 'apps', 
                    version = 'v1', 
                    kind = 'Deployment', ),
            scope = 'system',
            cluster_id = '71f69d83-ba66-4822-adf5-55ce55efd210',
            department_id = '2',
            project_id = '1'
        )

        # Make the API call
        api_response = api_instance.get_effective_policy(
            workload_type_and_scope=workload_type_and_scope,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_effective_policy: {e}")

def example_get_gvk_policy():
    """
    Example of using get_gvk_policy
    
    Get a policy. [experimental]
    Retrieve policy details by id, including both the declared rules and the effective rules.
    """
    try:
        # Prepare the request parameters
        policy_id = "example_policy_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_gvk_policy(
            policy_id=policy_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_gvk_policy: {e}")

def example_get_inference_policy_v2():
    """
    Example of using get_inference_policy_v2
    
    Get an inference policy.
    Retrieve the details of an inference policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters
        scope = "example_scope"
        
        
        
        
        
        
        
        department_id = "example_department_id"
        
        
        
        
        
        
        
        project_id = "example_project_id"
        
        
        
        
        
        
        
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_inference_policy_v2(
            scope=scope,
            department_id=department_id,
            project_id=project_id,
            cluster_id=cluster_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_inference_policy_v2: {e}")

def example_get_mapping_field_info():
    """
    Example of using get_mapping_field_info
    
    Get mapping field info. [experimental]
    Retrieve the detailed breakdown for one or more field references in a workload type&#39;s mapping.
    """
    try:
        # Prepare the request parameters
        
        # Create example data for GetMappingFieldInfoReq
        get_mapping_field_info_req = models.GetMappingFieldInfoReq(
            workload_type = runai.models.gvk.GVK(
                    group = 'apps', 
                    version = 'v1', 
                    kind = 'Deployment', ),
            fields_ref = [
                    runai.models.breakdown_field_ref.BreakdownFieldRef(
                        field_name = null, 
                        spec_selector = '', 
                        item_selector = '', )
                    ]
        )

        # Make the API call
        api_response = api_instance.get_mapping_field_info(
            get_mapping_field_info_req=get_mapping_field_info_req,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_mapping_field_info: {e}")

def example_get_mapping_minimal():
    """
    Example of using get_mapping_minimal
    
    Get minimal mapping info. [experimental]
    Retrieve the names and descriptions of fields, spec selectors, and item selectors for a workload type, without the full JQ expressions.
    """
    try:
        # Prepare the request parameters
        
        # Create example data for GetMappingMinimalInfoReq
        get_mapping_minimal_info_req = models.GetMappingMinimalInfoReq(
            workload_type = runai.models.gvk.GVK(
                    group = 'apps', 
                    version = 'v1', 
                    kind = 'Deployment', )
        )

        # Make the API call
        api_response = api_instance.get_mapping_minimal(
            get_mapping_minimal_info_req=get_mapping_minimal_info_req,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_mapping_minimal: {e}")

def example_get_nim_service_policy():
    """
    Example of using get_nim_service_policy
    
    Get NVIDIA NIM service policy.
    Retrieve the details of NVIDIA NIM service policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters
        scope = "example_scope"
        
        
        
        
        
        
        
        department_id = "example_department_id"
        
        
        
        
        
        
        
        project_id = "example_project_id"
        
        
        
        
        
        
        
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_nim_service_policy(
            scope=scope,
            department_id=department_id,
            project_id=project_id,
            cluster_id=cluster_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_nim_service_policy: {e}")

def example_get_training_policy_v2():
    """
    Example of using get_training_policy_v2
    
    Get a training policy.
    Retrieve the details of a training policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters
        scope = "example_scope"
        
        
        
        
        
        
        
        department_id = "example_department_id"
        
        
        
        
        
        
        
        project_id = "example_project_id"
        
        
        
        
        
        
        
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_training_policy_v2(
            scope=scope,
            department_id=department_id,
            project_id=project_id,
            cluster_id=cluster_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_training_policy_v2: {e}")

def example_get_workspace_policy_v2():
    """
    Example of using get_workspace_policy_v2
    
    Get a workspace policy.
    Retrieve the details of a workspace policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters
        scope = "example_scope"
        
        
        
        
        
        
        
        department_id = "example_department_id"
        
        
        
        
        
        
        
        project_id = "example_project_id"
        
        
        
        
        
        
        
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_workspace_policy_v2(
            scope=scope,
            department_id=department_id,
            project_id=project_id,
            cluster_id=cluster_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_workspace_policy_v2: {e}")

def example_list_gvk_policies():
    """
    Example of using list_gvk_policies
    
    List policies. [experimental]
    Retrieve a list of policies with their details, optionally filtered, sorted, and paginated.
    """
    try:
        # Prepare the request parameters
        
        
        
        filter_by = ["example_item_1", "example_item_2"]
        
        
        
        
        sort_by = "example_sort_by"
        
        
        
        
        
        
        
        
        offset = 42
        
        
        
        
        
        
        
        limit = 42
        
        
        
        
        
        
        sort_order = "example_sort_order"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.list_gvk_policies(
            filter_by=filter_by,
            sort_by=sort_by,
            offset=offset,
            limit=limit,
            sort_order=sort_order,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_gvk_policies: {e}")

def example_list_policies():
    """
    Example of using list_policies
    
    List policies
    Retrieve a list of all the applied policies.
    """
    try:
        # Prepare the request parameters
        workload_type = "example_workload_type"
        
        
        
        
        
        
        
        scope = "example_scope"
        
        
        
        
        
        
        
        department_id = "example_department_id"
        
        
        
        
        
        
        
        project_id = "example_project_id"
        
        
        
        
        
        
        
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        
        
        
        include_fallback_policies = True
        
        
        
        
        

        # Make the API call
        api_response = api_instance.list_policies(
            workload_type=workload_type,
            scope=scope,
            department_id=department_id,
            project_id=project_id,
            cluster_id=cluster_id,
            include_fallback_policies=include_fallback_policies,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_policies: {e}")

def example_overwrite_distributed_inference_policy_v2():
    """
    Example of using overwrite_distributed_inference_policy_v2
    
    Overwrite a distributed inference policy.
    Use to apply a distributed inference policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters
        
        
        validate_only = True
        
        
        
        
        
        
        
        approve_cluster_deletion = True
        
        
        
        
        
        
        # Create example data for DistributedInferencePolicyOverwriteRequestV2
        distributed_inference_policy_overwrite_request_v2 = models.DistributedInferencePolicyOverwriteRequestV2(
            meta = runai.models.policy_creation_fields.PolicyCreationFields(
                    scope = 'system', 
                    project_id = 1, 
                    department_id = '2', 
                    cluster_id = '71f69d83-ba66-4822-adf5-55ce55efd210', 
                    name = 'my-policy', ),
            policy = runai.models.distributed_inference_policy_defaults_and_rules_v2.DistributedInferencePolicyDefaultsAndRulesV2(
                    defaults = runai.models.defaults.defaults(), 
                    rules = runai.models.rules.rules(), 
                    imposed_assets = runai.models.distributed_inference_imposed_assets.DistributedInferenceImposedAssets(
                        leader = [
                            ''
                            ], 
                        worker = [
                            ''
                            ], ), 
                    status = {validation={errorMessage=errorMessage}}, )
        )

        # Make the API call
        api_response = api_instance.overwrite_distributed_inference_policy_v2(
            validate_only=validate_only,
            approve_cluster_deletion=approve_cluster_deletion,
            distributed_inference_policy_overwrite_request_v2=distributed_inference_policy_overwrite_request_v2,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling overwrite_distributed_inference_policy_v2: {e}")

def example_overwrite_distributed_policy_v2():
    """
    Example of using overwrite_distributed_policy_v2
    
    Overwrite a distributed policy.
    Use to apply a distributed policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters
        
        
        validate_only = True
        
        
        
        
        
        
        
        approve_cluster_deletion = True
        
        
        
        
        
        
        # Create example data for DistributedPolicyOverwriteRequestV2
        distributed_policy_overwrite_request_v2 = models.DistributedPolicyOverwriteRequestV2(
            meta = runai.models.policy_creation_fields.PolicyCreationFields(
                    scope = 'system', 
                    project_id = 1, 
                    department_id = '2', 
                    cluster_id = '71f69d83-ba66-4822-adf5-55ce55efd210', 
                    name = 'my-policy', ),
            policy = runai.models.distributed_policy_defaults_and_rules_v2.DistributedPolicyDefaultsAndRulesV2(
                    defaults = runai.models.distributed_policy_defaults_v2.DistributedPolicyDefaultsV2(
                        master = runai.models.replica_defaults_v2.ReplicaDefaultsV2(
                            annotations = runai.models.annotations_defaults.AnnotationsDefaults(
                                instances = [
                                    {name=billing, exclude=false, value=my-billing-unit}
                                    ], ), 
                            args = '-x my-script.py', 
                            auto_deletion_time_after_completion_seconds = 15, 
                            backoff_limit = 3, 
                            category = 'jUR,rZ#UM/?R,Fp^l6$ARj', 
                            command = 'python', 
                            compute = runai.models.superset_defaults_all_of_compute.SupersetDefaultsAllOfCompute(
                                cpu_core_limit = 2, 
                                cpu_core_request = 0.5, 
                                cpu_memory_limit = '30M', 
                                cpu_memory_request = '20M', 
                                extended_resources = runai.models.extended_resources_defaults.ExtendedResourcesDefaults(
                                    attributes = {quantity=2, resource=hardware-vendor.example/foo, exclude=false}, 
                                    instances = [
                                        {quantity=2, resource=hardware-vendor.example/foo, exclude=false}
                                        ], ), 
                                gpu_devices_request = 1, 
                                gpu_memory_limit = '10M', 
                                gpu_memory_request = '10M', 
                                gpu_portion_limit = 0.5, 
                                gpu_portion_request = 0.5, 
                                gpu_request_type = 'portion', 
                                large_shm_request = False, ), 
                            create_home_dir = True, 
                            environment_variables = runai.models.environment_variables_defaults.EnvironmentVariablesDefaults(
                                instances = [
                                    runai.models.environment_variable.EnvironmentVariable(
                                        name = 'HOME', 
                                        value = '/home/my-folder', 
                                        secret = runai.models.environment_variable_secret.EnvironmentVariableSecret(
                                            name = 'postgress_secret', 
                                            key = 'POSTGRES_PASSWORD', ), 
                                        config_map = {name=my-config-map, key=MY_POSTGRES_SCHEMA}, 
                                        pod_field_ref = {path=metadata.name}, 
                                        user_credential = runai.models.environment_variable_user_credential.EnvironmentVariableUserCredential(
                                            name = 'my_postgres_user_and_password', 
                                            key = 'POSTGRES_PASSWORD', ), 
                                        exclude = False, 
                                        description = 'Home directory of the user.', )
                                    ], ), 
                            exposed_urls = runai.models.exposed_urls_defaults.ExposedUrlsDefaults(
                                instances = [
                                    runai.models.exposed_url.ExposedUrl(
                                        container = 8080, 
                                        url = 'https://my-url.com', 
                                        authorization_type = 'authenticatedUsers', 
                                        authorized_users = ["user-a","user-b"], 
                                        authorized_groups = ["group-a","group-b"], 
                                        tool_type = 'jupyter', 
                                        tool_name = 'my-pytorch', 
                                        name = 'url-instance-a', 
                                        exclude = False, )
                                    ], ), 
                            image = 'python:3.8', 
                            image_pull_policy = 'Always', 
                            image_pull_secrets = runai.models.image_pull_secrets_defaults.ImagePullSecretsDefaults(), 
                            labels = runai.models.labels_defaults.LabelsDefaults(), 
                            node_affinity_required = {nodeSelectorTerms=[Ljava.lang.Object;@659caab3}, 
                            node_pools = ["my-node-pool-a","my-node-pool-b"], 
                            node_type = 'my-node-type', 
                            pod_affinity = {type=Required, key=key}, 
                            ports = runai.models.ports_defaults.PortsDefaults(), 
                            preemptibility = 'preemptible', 
                            priority_class = 'jUR,rZ#UM/?R,Fp^l6$ARj', 
                            probes = {readiness={handler={httpGet={path=/, scheme=HTTP, port=15087, host=example.com}}, failureThreshold=1, periodSeconds=1, timeoutSeconds=1, successThreshold=1, initialDelaySeconds=0}}, 
                            related_urls = runai.models.related_urls_defaults.RelatedUrlsDefaults(), 
                            restart_policy = 'Always', 
                            security = runai.models.superset_defaults_all_of_security.SupersetDefaultsAllOfSecurity(
                                allow_privilege_escalation = False, 
                                capabilities = ["CHOWN","KILL"], 
                                host_ipc = False, 
                                host_network = False, 
                                read_only_root_filesystem = False, 
                                run_as_gid = 30, 
                                run_as_non_root = True, 
                                run_as_uid = 500, 
                                seccomp_profile_type = 'RuntimeDefault', 
                                supplemental_groups = '2,3,5,8', 
                                uid_gid_source = 'fromTheImage', ), 
                            stdin = True, 
                            storage = runai.models.superset_defaults_all_of_storage.SupersetDefaults_allOf_storage(
                                config_map_volume = runai.models.config_maps_defaults.ConfigMapsDefaults(), 
                                data_volume = runai.models.data_volumes_defaults.DataVolumesDefaults(), 
                                empty_dir_volume = runai.models.empty_dirs_defaults.EmptyDirsDefaults(), 
                                git = runai.models.gits_defaults.GitsDefaults(), 
                                host_path = runai.models.host_paths_defaults.HostPathsDefaults(), 
                                nfs = runai.models.nfss_defaults.NfssDefaults(), 
                                pvc = runai.models.pvcs_defaults.PvcsDefaults(), 
                                s3 = runai.models.s3s_defaults.S3sDefaults(), 
                                secret_volume = runai.models.secrets_defaults.SecretsDefaults(), ), 
                            terminate_after_preemption = False, 
                            termination_grace_period_seconds = 20, 
                            tolerations = runai.models.tolerations_defaults.TolerationsDefaults(), 
                            tty = True, 
                            working_dir = '/home/myfolder', ), 
                        worker = runai.models.distributed_policy_defaults_v2_worker.DistributedPolicyDefaultsV2_worker(), ), 
                    rules = runai.models.distributed_policy_rules_v2.DistributedPolicyRulesV2(), 
                    imposed_assets = runai.models.distributed_imposed_assets.DistributedImposedAssets(), 
                    status = {validation={errorMessage=errorMessage}}, )
        )

        # Make the API call
        api_response = api_instance.overwrite_distributed_policy_v2(
            validate_only=validate_only,
            approve_cluster_deletion=approve_cluster_deletion,
            distributed_policy_overwrite_request_v2=distributed_policy_overwrite_request_v2,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling overwrite_distributed_policy_v2: {e}")

def example_overwrite_inference_policy_v2():
    """
    Example of using overwrite_inference_policy_v2
    
    Overwrite an inference policy.
    Use to apply an inference policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters
        
        
        validate_only = True
        
        
        
        
        
        
        
        approve_cluster_deletion = True
        
        
        
        
        
        
        # Create example data for InferencePolicyOverwriteRequestV2
        inference_policy_overwrite_request_v2 = models.InferencePolicyOverwriteRequestV2(
            meta = runai.models.policy_creation_fields.PolicyCreationFields(
                    scope = 'system', 
                    project_id = 1, 
                    department_id = '2', 
                    cluster_id = '71f69d83-ba66-4822-adf5-55ce55efd210', 
                    name = 'my-policy', ),
            policy = runai.models.inference_policy_defaults_and_rules_v2.InferencePolicyDefaultsAndRulesV2(
                    defaults = runai.models.defaults.defaults(), 
                    rules = runai.models.rules.rules(), 
                    imposed_assets = [
                        ''
                        ], 
                    status = {validation={errorMessage=errorMessage}}, )
        )

        # Make the API call
        api_response = api_instance.overwrite_inference_policy_v2(
            validate_only=validate_only,
            approve_cluster_deletion=approve_cluster_deletion,
            inference_policy_overwrite_request_v2=inference_policy_overwrite_request_v2,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling overwrite_inference_policy_v2: {e}")

def example_overwrite_nim_service_policy():
    """
    Example of using overwrite_nim_service_policy
    
    Overwrite NVIDIA NIM service policy.
    Use to apply NVIDIA NIM service policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters
        
        
        validate_only = True
        
        
        
        
        
        
        # Create example data for NimServicePolicyOverwriteRequest
        nim_service_policy_overwrite_request = models.NimServicePolicyOverwriteRequest(
            meta = runai.models.policy_creation_fields.PolicyCreationFields(
                    scope = 'system', 
                    project_id = 1, 
                    department_id = '2', 
                    cluster_id = '71f69d83-ba66-4822-adf5-55ce55efd210', 
                    name = 'my-policy', ),
            policy = runai.models.nim_service_policy_defaults_and_rules.NimServicePolicyDefaultsAndRules(
                    defaults = runai.models.defaults.defaults(), 
                    rules = runai.models.rules.rules(), 
                    status = {validation={errorMessage=errorMessage}}, )
        )

        # Make the API call
        api_response = api_instance.overwrite_nim_service_policy(
            validate_only=validate_only,
            nim_service_policy_overwrite_request=nim_service_policy_overwrite_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling overwrite_nim_service_policy: {e}")

def example_overwrite_training_policy_v2():
    """
    Example of using overwrite_training_policy_v2
    
    Overwrite a training policy.
    Use to apply a training policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters
        
        
        validate_only = True
        
        
        
        
        
        
        
        approve_cluster_deletion = True
        
        
        
        
        
        
        # Create example data for TrainingPolicyOverwriteRequestV2
        training_policy_overwrite_request_v2 = models.TrainingPolicyOverwriteRequestV2(
            meta = runai.models.policy_creation_fields.PolicyCreationFields(
                    scope = 'system', 
                    project_id = 1, 
                    department_id = '2', 
                    cluster_id = '71f69d83-ba66-4822-adf5-55ce55efd210', 
                    name = 'my-policy', ),
            policy = runai.models.training_policy_defaults_and_rules_v2.TrainingPolicyDefaultsAndRulesV2(
                    defaults = runai.models.defaults.defaults(), 
                    rules = runai.models.rules.rules(), 
                    imposed_assets = [
                        ''
                        ], 
                    status = runai.models.policy_validation_status.PolicyValidationStatus(
                        validation = {errorMessage=errorMessage}, ), )
        )

        # Make the API call
        api_response = api_instance.overwrite_training_policy_v2(
            validate_only=validate_only,
            approve_cluster_deletion=approve_cluster_deletion,
            training_policy_overwrite_request_v2=training_policy_overwrite_request_v2,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling overwrite_training_policy_v2: {e}")

def example_overwrite_workspace_policy_v2():
    """
    Example of using overwrite_workspace_policy_v2
    
    Overwrite a workspace policy.
    Ue to apply a workspace policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters
        
        
        validate_only = True
        
        
        
        
        
        
        
        approve_cluster_deletion = True
        
        
        
        
        
        
        # Create example data for WorkspacePolicyOverwriteRequestV2
        workspace_policy_overwrite_request_v2 = models.WorkspacePolicyOverwriteRequestV2(
            meta = runai.models.policy_creation_fields.PolicyCreationFields(
                    scope = 'system', 
                    project_id = 1, 
                    department_id = '2', 
                    cluster_id = '71f69d83-ba66-4822-adf5-55ce55efd210', 
                    name = 'my-policy', ),
            policy = runai.models.workspace_policy_defaults_and_rules_v2.WorkspacePolicyDefaultsAndRulesV2(
                    defaults = runai.models.defaults.defaults(), 
                    rules = runai.models.rules.rules(), 
                    imposed_assets = [
                        ''
                        ], 
                    status = {validation={errorMessage=errorMessage}}, )
        )

        # Make the API call
        api_response = api_instance.overwrite_workspace_policy_v2(
            validate_only=validate_only,
            approve_cluster_deletion=approve_cluster_deletion,
            workspace_policy_overwrite_request_v2=workspace_policy_overwrite_request_v2,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling overwrite_workspace_policy_v2: {e}")

def example_patch_gvk_policy():
    """
    Example of using patch_gvk_policy
    
    Patch a policy. [experimental]
    Merge rules into an existing policy, keyed by rule identity.
    """
    try:
        # Prepare the request parameters
        policy_id = "example_policy_id"
        
        
        
        
        
        
        
        
        # Create example data for UpdateGvkPolicyReq
        update_gvk_policy_req = models.UpdateGvkPolicyReq(
        )

        # Make the API call
        api_response = api_instance.patch_gvk_policy(
            policy_id=policy_id,
            update_gvk_policy_req=update_gvk_policy_req,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling patch_gvk_policy: {e}")

def example_update_distributed_inference_policy_v2():
    """
    Example of using update_distributed_inference_policy_v2
    
    Update a distributed inference policy.
    Use to apply changes to a distributed inference policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters
        
        
        validate_only = True
        
        
        
        
        
        
        
        approve_cluster_deletion = True
        
        
        
        
        
        
        # Create example data for DistributedInferencePolicyChangeRequestV2
        distributed_inference_policy_change_request_v2 = models.DistributedInferencePolicyChangeRequestV2(
            meta = runai.models.policy_creation_fields.PolicyCreationFields(
                    scope = 'system', 
                    project_id = 1, 
                    department_id = '2', 
                    cluster_id = '71f69d83-ba66-4822-adf5-55ce55efd210', 
                    name = 'my-policy', ),
            policy = runai.models.distributed_inference_policy_defaults_and_rules_v2.DistributedInferencePolicyDefaultsAndRulesV2(
                    defaults = runai.models.defaults.defaults(), 
                    rules = runai.models.rules.rules(), 
                    imposed_assets = runai.models.distributed_inference_imposed_assets.DistributedInferenceImposedAssets(
                        leader = [
                            ''
                            ], 
                        worker = [
                            ''
                            ], ), 
                    status = {validation={errorMessage=errorMessage}}, ),
            reset = ["master.security.runAsGpu","worker.compute.gpu"]
        )

        # Make the API call
        api_response = api_instance.update_distributed_inference_policy_v2(
            validate_only=validate_only,
            approve_cluster_deletion=approve_cluster_deletion,
            distributed_inference_policy_change_request_v2=distributed_inference_policy_change_request_v2,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_distributed_inference_policy_v2: {e}")

def example_update_distributed_policy_v2():
    """
    Example of using update_distributed_policy_v2
    
    Update a distributed policy.
    Use to apply changes to a distributed policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters
        
        
        validate_only = True
        
        
        
        
        
        
        
        approve_cluster_deletion = True
        
        
        
        
        
        
        # Create example data for DistributedPolicyChangeRequestV2
        distributed_policy_change_request_v2 = models.DistributedPolicyChangeRequestV2(
            meta = runai.models.policy_creation_fields.PolicyCreationFields(
                    scope = 'system', 
                    project_id = 1, 
                    department_id = '2', 
                    cluster_id = '71f69d83-ba66-4822-adf5-55ce55efd210', 
                    name = 'my-policy', ),
            policy = runai.models.distributed_policy_defaults_and_rules_v2.DistributedPolicyDefaultsAndRulesV2(
                    defaults = runai.models.distributed_policy_defaults_v2.DistributedPolicyDefaultsV2(
                        master = runai.models.replica_defaults_v2.ReplicaDefaultsV2(
                            annotations = runai.models.annotations_defaults.AnnotationsDefaults(
                                instances = [
                                    {name=billing, exclude=false, value=my-billing-unit}
                                    ], ), 
                            args = '-x my-script.py', 
                            auto_deletion_time_after_completion_seconds = 15, 
                            backoff_limit = 3, 
                            category = 'jUR,rZ#UM/?R,Fp^l6$ARj', 
                            command = 'python', 
                            compute = runai.models.superset_defaults_all_of_compute.SupersetDefaultsAllOfCompute(
                                cpu_core_limit = 2, 
                                cpu_core_request = 0.5, 
                                cpu_memory_limit = '30M', 
                                cpu_memory_request = '20M', 
                                extended_resources = runai.models.extended_resources_defaults.ExtendedResourcesDefaults(
                                    attributes = {quantity=2, resource=hardware-vendor.example/foo, exclude=false}, 
                                    instances = [
                                        {quantity=2, resource=hardware-vendor.example/foo, exclude=false}
                                        ], ), 
                                gpu_devices_request = 1, 
                                gpu_memory_limit = '10M', 
                                gpu_memory_request = '10M', 
                                gpu_portion_limit = 0.5, 
                                gpu_portion_request = 0.5, 
                                gpu_request_type = 'portion', 
                                large_shm_request = False, ), 
                            create_home_dir = True, 
                            environment_variables = runai.models.environment_variables_defaults.EnvironmentVariablesDefaults(
                                instances = [
                                    runai.models.environment_variable.EnvironmentVariable(
                                        name = 'HOME', 
                                        value = '/home/my-folder', 
                                        secret = runai.models.environment_variable_secret.EnvironmentVariableSecret(
                                            name = 'postgress_secret', 
                                            key = 'POSTGRES_PASSWORD', ), 
                                        config_map = {name=my-config-map, key=MY_POSTGRES_SCHEMA}, 
                                        pod_field_ref = {path=metadata.name}, 
                                        user_credential = runai.models.environment_variable_user_credential.EnvironmentVariableUserCredential(
                                            name = 'my_postgres_user_and_password', 
                                            key = 'POSTGRES_PASSWORD', ), 
                                        exclude = False, 
                                        description = 'Home directory of the user.', )
                                    ], ), 
                            exposed_urls = runai.models.exposed_urls_defaults.ExposedUrlsDefaults(
                                instances = [
                                    runai.models.exposed_url.ExposedUrl(
                                        container = 8080, 
                                        url = 'https://my-url.com', 
                                        authorization_type = 'authenticatedUsers', 
                                        authorized_users = ["user-a","user-b"], 
                                        authorized_groups = ["group-a","group-b"], 
                                        tool_type = 'jupyter', 
                                        tool_name = 'my-pytorch', 
                                        name = 'url-instance-a', 
                                        exclude = False, )
                                    ], ), 
                            image = 'python:3.8', 
                            image_pull_policy = 'Always', 
                            image_pull_secrets = runai.models.image_pull_secrets_defaults.ImagePullSecretsDefaults(), 
                            labels = runai.models.labels_defaults.LabelsDefaults(), 
                            node_affinity_required = {nodeSelectorTerms=[Ljava.lang.Object;@659caab3}, 
                            node_pools = ["my-node-pool-a","my-node-pool-b"], 
                            node_type = 'my-node-type', 
                            pod_affinity = {type=Required, key=key}, 
                            ports = runai.models.ports_defaults.PortsDefaults(), 
                            preemptibility = 'preemptible', 
                            priority_class = 'jUR,rZ#UM/?R,Fp^l6$ARj', 
                            probes = {readiness={handler={httpGet={path=/, scheme=HTTP, port=15087, host=example.com}}, failureThreshold=1, periodSeconds=1, timeoutSeconds=1, successThreshold=1, initialDelaySeconds=0}}, 
                            related_urls = runai.models.related_urls_defaults.RelatedUrlsDefaults(), 
                            restart_policy = 'Always', 
                            security = runai.models.superset_defaults_all_of_security.SupersetDefaultsAllOfSecurity(
                                allow_privilege_escalation = False, 
                                capabilities = ["CHOWN","KILL"], 
                                host_ipc = False, 
                                host_network = False, 
                                read_only_root_filesystem = False, 
                                run_as_gid = 30, 
                                run_as_non_root = True, 
                                run_as_uid = 500, 
                                seccomp_profile_type = 'RuntimeDefault', 
                                supplemental_groups = '2,3,5,8', 
                                uid_gid_source = 'fromTheImage', ), 
                            stdin = True, 
                            storage = runai.models.superset_defaults_all_of_storage.SupersetDefaults_allOf_storage(
                                config_map_volume = runai.models.config_maps_defaults.ConfigMapsDefaults(), 
                                data_volume = runai.models.data_volumes_defaults.DataVolumesDefaults(), 
                                empty_dir_volume = runai.models.empty_dirs_defaults.EmptyDirsDefaults(), 
                                git = runai.models.gits_defaults.GitsDefaults(), 
                                host_path = runai.models.host_paths_defaults.HostPathsDefaults(), 
                                nfs = runai.models.nfss_defaults.NfssDefaults(), 
                                pvc = runai.models.pvcs_defaults.PvcsDefaults(), 
                                s3 = runai.models.s3s_defaults.S3sDefaults(), 
                                secret_volume = runai.models.secrets_defaults.SecretsDefaults(), ), 
                            terminate_after_preemption = False, 
                            termination_grace_period_seconds = 20, 
                            tolerations = runai.models.tolerations_defaults.TolerationsDefaults(), 
                            tty = True, 
                            working_dir = '/home/myfolder', ), 
                        worker = runai.models.distributed_policy_defaults_v2_worker.DistributedPolicyDefaultsV2_worker(), ), 
                    rules = runai.models.distributed_policy_rules_v2.DistributedPolicyRulesV2(), 
                    imposed_assets = runai.models.distributed_imposed_assets.DistributedImposedAssets(), 
                    status = {validation={errorMessage=errorMessage}}, ),
            reset = ["master.security.runAsGpu","worker.compute.gpu"]
        )

        # Make the API call
        api_response = api_instance.update_distributed_policy_v2(
            validate_only=validate_only,
            approve_cluster_deletion=approve_cluster_deletion,
            distributed_policy_change_request_v2=distributed_policy_change_request_v2,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_distributed_policy_v2: {e}")

def example_update_inference_policy_v2():
    """
    Example of using update_inference_policy_v2
    
    Update an inference policy.
    Use to apply changes to an inference policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters
        
        
        validate_only = True
        
        
        
        
        
        
        
        approve_cluster_deletion = True
        
        
        
        
        
        
        # Create example data for InferencePolicyChangeRequestV2
        inference_policy_change_request_v2 = models.InferencePolicyChangeRequestV2(
            meta = runai.models.policy_creation_fields.PolicyCreationFields(
                    scope = 'system', 
                    project_id = 1, 
                    department_id = '2', 
                    cluster_id = '71f69d83-ba66-4822-adf5-55ce55efd210', 
                    name = 'my-policy', ),
            policy = runai.models.inference_policy_defaults_and_rules_v2.InferencePolicyDefaultsAndRulesV2(
                    defaults = runai.models.defaults.defaults(), 
                    rules = runai.models.rules.rules(), 
                    imposed_assets = [
                        ''
                        ], 
                    status = {validation={errorMessage=errorMessage}}, ),
            reset = ["master.security.runAsGpu","worker.compute.gpu"]
        )

        # Make the API call
        api_response = api_instance.update_inference_policy_v2(
            validate_only=validate_only,
            approve_cluster_deletion=approve_cluster_deletion,
            inference_policy_change_request_v2=inference_policy_change_request_v2,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_inference_policy_v2: {e}")

def example_update_nim_service_policy():
    """
    Example of using update_nim_service_policy
    
    Update NVIDIA NIM service policy.
    Use to apply changes to NVIDIA NIM service policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters
        
        
        validate_only = True
        
        
        
        
        
        
        # Create example data for NimServicePolicyChangeRequest
        nim_service_policy_change_request = models.NimServicePolicyChangeRequest(
            meta = runai.models.policy_creation_fields.PolicyCreationFields(
                    scope = 'system', 
                    project_id = 1, 
                    department_id = '2', 
                    cluster_id = '71f69d83-ba66-4822-adf5-55ce55efd210', 
                    name = 'my-policy', ),
            policy = runai.models.nim_service_policy_defaults_and_rules.NimServicePolicyDefaultsAndRules(
                    defaults = runai.models.defaults.defaults(), 
                    rules = runai.models.rules.rules(), 
                    status = {validation={errorMessage=errorMessage}}, ),
            reset = ["master.security.runAsGpu","worker.compute.gpu"]
        )

        # Make the API call
        api_response = api_instance.update_nim_service_policy(
            validate_only=validate_only,
            nim_service_policy_change_request=nim_service_policy_change_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_nim_service_policy: {e}")

def example_update_training_policy_v2():
    """
    Example of using update_training_policy_v2
    
    Update a training policy.
    Use to apply changes to a training policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters
        
        
        validate_only = True
        
        
        
        
        
        
        
        approve_cluster_deletion = True
        
        
        
        
        
        
        # Create example data for TrainingPolicyChangeRequestV2
        training_policy_change_request_v2 = models.TrainingPolicyChangeRequestV2(
            meta = runai.models.policy_creation_fields.PolicyCreationFields(
                    scope = 'system', 
                    project_id = 1, 
                    department_id = '2', 
                    cluster_id = '71f69d83-ba66-4822-adf5-55ce55efd210', 
                    name = 'my-policy', ),
            policy = runai.models.training_policy_defaults_and_rules_v2.TrainingPolicyDefaultsAndRulesV2(
                    defaults = runai.models.defaults.defaults(), 
                    rules = runai.models.rules.rules(), 
                    imposed_assets = [
                        ''
                        ], 
                    status = runai.models.policy_validation_status.PolicyValidationStatus(
                        validation = {errorMessage=errorMessage}, ), ),
            reset = ["master.security.runAsGpu","worker.compute.gpu"]
        )

        # Make the API call
        api_response = api_instance.update_training_policy_v2(
            validate_only=validate_only,
            approve_cluster_deletion=approve_cluster_deletion,
            training_policy_change_request_v2=training_policy_change_request_v2,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_training_policy_v2: {e}")

def example_update_workspace_policy_v2():
    """
    Example of using update_workspace_policy_v2
    
    Update a workspace policy.
    Use to apply changes to a workspace policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters
        
        
        validate_only = True
        
        
        
        
        
        
        
        approve_cluster_deletion = True
        
        
        
        
        
        
        # Create example data for WorkspacePolicyChangeRequestV2
        workspace_policy_change_request_v2 = models.WorkspacePolicyChangeRequestV2(
            meta = runai.models.policy_creation_fields.PolicyCreationFields(
                    scope = 'system', 
                    project_id = 1, 
                    department_id = '2', 
                    cluster_id = '71f69d83-ba66-4822-adf5-55ce55efd210', 
                    name = 'my-policy', ),
            policy = runai.models.workspace_policy_defaults_and_rules_v2.WorkspacePolicyDefaultsAndRulesV2(
                    defaults = runai.models.defaults.defaults(), 
                    rules = runai.models.rules.rules(), 
                    imposed_assets = [
                        ''
                        ], 
                    status = {validation={errorMessage=errorMessage}}, ),
            reset = ["master.security.runAsGpu","worker.compute.gpu"]
        )

        # Make the API call
        api_response = api_instance.update_workspace_policy_v2(
            validate_only=validate_only,
            approve_cluster_deletion=approve_cluster_deletion,
            workspace_policy_change_request_v2=workspace_policy_change_request_v2,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_workspace_policy_v2: {e}")

