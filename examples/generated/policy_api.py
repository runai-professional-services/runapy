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

        # Make the API call
        api_instance.delete_distributed_policy(
            scope=scope,
            department_id=department_id,
            project_id=project_id,
            cluster_id=cluster_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_distributed_policy: {e}")


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

        # Make the API call
        api_instance.delete_inference_policy(
            scope=scope,
            department_id=department_id,
            project_id=project_id,
            cluster_id=cluster_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_inference_policy: {e}")


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

        # Make the API call
        api_instance.delete_training_policy(
            scope=scope,
            department_id=department_id,
            project_id=project_id,
            cluster_id=cluster_id,
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

        # Make the API call
        api_instance.delete_workspace_policy(
            scope=scope,
            department_id=department_id,
            project_id=project_id,
            cluster_id=cluster_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_workspace_policy: {e}")


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


def example_get_training_policy_v2():
    """
    Example of using get_training_policy_v2

    Get a training policy.
    Retrieve the details of an training policy for a given organizational unit.
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

        # Make the API call
        api_response = api_instance.list_policies(
            workload_type=workload_type,
            scope=scope,
            department_id=department_id,
            project_id=project_id,
            cluster_id=cluster_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_policies: {e}")


def example_overwrite_distributed_policy_v2():
    """
    Example of using overwrite_distributed_policy_v2

    Overwrite a distributed policy.
    Use to apply a distributed policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters

        validate_only = True

        # Create example data for DistributedPolicyOverwriteRequestV2
        distributed_policy_overwrite_request_v2 = models.DistributedPolicyOverwriteRequestV2(
            meta=runai.models.policy_creation_fields.PolicyCreationFields(
                scope="system",
                project_id=1,
                department_id="2",
                cluster_id="71f69d83-ba66-4822-adf5-55ce55efd210",
                name="my-policy",
            ),
            policy=runai.models.distributed_policy_defaults_and_rules_v2.DistributedPolicyDefaultsAndRulesV2(
                defaults=runai.models.distributed_policy_defaults_v2.DistributedPolicyDefaultsV2(
                    worker=runai.models.distributed_policy_defaults_v2_worker.DistributedPolicyDefaultsV2_worker(),
                    master=runai.models.replica_defaults_v2.ReplicaDefaultsV2(),
                ),
                rules=runai.models.distributed_policy_rules_v2.DistributedPolicyRulesV2(),
                imposed_assets=runai.models.distributed_imposed_assets.DistributedImposedAssets(),
            ),
        )

        # Make the API call
        api_response = api_instance.overwrite_distributed_policy_v2(
            validate_only=validate_only,
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

        # Create example data for InferencePolicyOverwriteRequestV2
        inference_policy_overwrite_request_v2 = models.InferencePolicyOverwriteRequestV2(
            meta=runai.models.policy_creation_fields.PolicyCreationFields(
                scope="system",
                project_id=1,
                department_id="2",
                cluster_id="71f69d83-ba66-4822-adf5-55ce55efd210",
                name="my-policy",
            ),
            policy=runai.models.inference_policy_defaults_and_rules_v2.InferencePolicyDefaultsAndRulesV2(
                defaults=runai.models.inference_policy_defaults_and_rules_v2_defaults.InferencePolicyDefaultsAndRulesV2_defaults(),
                rules=runai.models.rules.rules(),
                imposed_assets=[""],
            ),
        )

        # Make the API call
        api_response = api_instance.overwrite_inference_policy_v2(
            validate_only=validate_only,
            inference_policy_overwrite_request_v2=inference_policy_overwrite_request_v2,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling overwrite_inference_policy_v2: {e}")


def example_overwrite_training_policy_v2():
    """
    Example of using overwrite_training_policy_v2

    Overwrite a training policy.
    Use to apply a training policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters

        validate_only = True

        # Create example data for TrainingPolicyOverwriteRequestV2
        training_policy_overwrite_request_v2 = models.TrainingPolicyOverwriteRequestV2(
            meta=runai.models.policy_creation_fields.PolicyCreationFields(
                scope="system",
                project_id=1,
                department_id="2",
                cluster_id="71f69d83-ba66-4822-adf5-55ce55efd210",
                name="my-policy",
            ),
            policy=runai.models.training_policy_defaults_and_rules_v2.TrainingPolicyDefaultsAndRulesV2(
                defaults=runai.models.training_policy_defaults_and_rules_v2_defaults.TrainingPolicyDefaultsAndRulesV2_defaults(),
                rules=runai.models.rules.rules(),
                imposed_assets=[""],
            ),
        )

        # Make the API call
        api_response = api_instance.overwrite_training_policy_v2(
            validate_only=validate_only,
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

        # Create example data for WorkspacePolicyOverwriteRequestV2
        workspace_policy_overwrite_request_v2 = models.WorkspacePolicyOverwriteRequestV2(
            meta=runai.models.policy_creation_fields.PolicyCreationFields(
                scope="system",
                project_id=1,
                department_id="2",
                cluster_id="71f69d83-ba66-4822-adf5-55ce55efd210",
                name="my-policy",
            ),
            policy=runai.models.workspace_policy_defaults_and_rules_v2.WorkspacePolicyDefaultsAndRulesV2(
                defaults=runai.models.workspace_policy_defaults_and_rules_v2_defaults.WorkspacePolicyDefaultsAndRulesV2_defaults(),
                rules=runai.models.rules.rules(),
                imposed_assets=[""],
            ),
        )

        # Make the API call
        api_response = api_instance.overwrite_workspace_policy_v2(
            validate_only=validate_only,
            workspace_policy_overwrite_request_v2=workspace_policy_overwrite_request_v2,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling overwrite_workspace_policy_v2: {e}")


def example_update_distributed_policy_v2():
    """
    Example of using update_distributed_policy_v2

    Update a distributed policy.
    Use to apply changes to distributed policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters

        validate_only = True

        # Create example data for DistributedPolicyChangeRequestV2
        distributed_policy_change_request_v2 = models.DistributedPolicyChangeRequestV2(
            meta=runai.models.policy_creation_fields.PolicyCreationFields(
                scope="system",
                project_id=1,
                department_id="2",
                cluster_id="71f69d83-ba66-4822-adf5-55ce55efd210",
                name="my-policy",
            ),
            policy=runai.models.distributed_policy_defaults_and_rules_v2.DistributedPolicyDefaultsAndRulesV2(
                defaults=runai.models.distributed_policy_defaults_v2.DistributedPolicyDefaultsV2(
                    worker=runai.models.distributed_policy_defaults_v2_worker.DistributedPolicyDefaultsV2_worker(),
                    master=runai.models.replica_defaults_v2.ReplicaDefaultsV2(),
                ),
                rules=runai.models.distributed_policy_rules_v2.DistributedPolicyRulesV2(),
                imposed_assets=runai.models.distributed_imposed_assets.DistributedImposedAssets(),
            ),
            reset=["master.security.runAsGpu", "worker.compute.gpu"],
        )

        # Make the API call
        api_response = api_instance.update_distributed_policy_v2(
            validate_only=validate_only,
            distributed_policy_change_request_v2=distributed_policy_change_request_v2,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_distributed_policy_v2: {e}")


def example_update_inference_policy_v2():
    """
    Example of using update_inference_policy_v2

    Update an inference policy.
    Use to apply changes to inference policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters

        validate_only = True

        # Create example data for InferencePolicyChangeRequestV2
        inference_policy_change_request_v2 = models.InferencePolicyChangeRequestV2(
            meta=runai.models.policy_creation_fields.PolicyCreationFields(
                scope="system",
                project_id=1,
                department_id="2",
                cluster_id="71f69d83-ba66-4822-adf5-55ce55efd210",
                name="my-policy",
            ),
            policy=runai.models.inference_policy_defaults_and_rules_v2.InferencePolicyDefaultsAndRulesV2(
                defaults=runai.models.inference_policy_defaults_and_rules_v2_defaults.InferencePolicyDefaultsAndRulesV2_defaults(),
                rules=runai.models.rules.rules(),
                imposed_assets=[""],
            ),
            reset=["master.security.runAsGpu", "worker.compute.gpu"],
        )

        # Make the API call
        api_response = api_instance.update_inference_policy_v2(
            validate_only=validate_only,
            inference_policy_change_request_v2=inference_policy_change_request_v2,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_inference_policy_v2: {e}")


def example_update_training_policy_v2():
    """
    Example of using update_training_policy_v2

    Update a training policy.
    Use to apply changes to training policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters

        validate_only = True

        # Create example data for TrainingPolicyChangeRequestV2
        training_policy_change_request_v2 = models.TrainingPolicyChangeRequestV2(
            meta=runai.models.policy_creation_fields.PolicyCreationFields(
                scope="system",
                project_id=1,
                department_id="2",
                cluster_id="71f69d83-ba66-4822-adf5-55ce55efd210",
                name="my-policy",
            ),
            policy=runai.models.training_policy_defaults_and_rules_v2.TrainingPolicyDefaultsAndRulesV2(
                defaults=runai.models.training_policy_defaults_and_rules_v2_defaults.TrainingPolicyDefaultsAndRulesV2_defaults(),
                rules=runai.models.rules.rules(),
                imposed_assets=[""],
            ),
            reset=["master.security.runAsGpu", "worker.compute.gpu"],
        )

        # Make the API call
        api_response = api_instance.update_training_policy_v2(
            validate_only=validate_only,
            training_policy_change_request_v2=training_policy_change_request_v2,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_training_policy_v2: {e}")


def example_update_workspace_policy_v2():
    """
    Example of using update_workspace_policy_v2

    Update a workspace policy.
    Use to apply changes to workspace policy for a given organizational unit.
    """
    try:
        # Prepare the request parameters

        validate_only = True

        # Create example data for WorkspacePolicyChangeRequestV2
        workspace_policy_change_request_v2 = models.WorkspacePolicyChangeRequestV2(
            meta=runai.models.policy_creation_fields.PolicyCreationFields(
                scope="system",
                project_id=1,
                department_id="2",
                cluster_id="71f69d83-ba66-4822-adf5-55ce55efd210",
                name="my-policy",
            ),
            policy=runai.models.workspace_policy_defaults_and_rules_v2.WorkspacePolicyDefaultsAndRulesV2(
                defaults=runai.models.workspace_policy_defaults_and_rules_v2_defaults.WorkspacePolicyDefaultsAndRulesV2_defaults(),
                rules=runai.models.rules.rules(),
                imposed_assets=[""],
            ),
            reset=["master.security.runAsGpu", "worker.compute.gpu"],
        )

        # Make the API call
        api_response = api_instance.update_workspace_policy_v2(
            validate_only=validate_only,
            workspace_policy_change_request_v2=workspace_policy_change_request_v2,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_workspace_policy_v2: {e}")
