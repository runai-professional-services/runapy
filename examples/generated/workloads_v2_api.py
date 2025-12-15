"""
Examples for using the WorkloadsV2Api
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import WorkloadsV2Api
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = WorkloadsV2Api(api_client)


def example_create_workload_v2():
    """
    Example of using create_workload_v2

    Create a workload. [Experimental]
    Submit a workload with metadata and a Kubernetes manifest.
    """
    try:
        # Prepare the request parameters

        # Create example data for WorkloadV2CreateRequest
        workload_v2_create_request = models.WorkloadV2CreateRequest(
            metadata=runai.models.workload_v2_metadata_create_params.WorkloadV2MetadataCreateParams(
                name="my-workload-name",
                use_given_name_as_prefix=True,
                project_id="1",
                cluster_id="71f69d83-ba66-4822-adf5-55ce55efd210",
                priority="jUR,rZ#UM/?R,Fp^l6$ARj",
                category="jUR,rZ#UM/?R,Fp^l6$ARj",
                preemptibility="preemptible",
            ),
            manifest={
                "apiVersion": "apps/v1",
                "kind": "Deployment",
                "metadata": {"name": "my-app"},
                "spec": {
                    "replicas": 1,
                    "selector": {"matchLabels": {"app": "my-app"}},
                    "template": {
                        "metadata": {"labels": {"app": "my-app"}},
                        "spec": {
                            "containers": [{"name": "app", "image": "nginx:latest"}]
                        },
                    },
                },
            },
            manifest_base64_encoded="[B@71ea1fda",
        )

        # Make the API call
        api_response = api_instance.create_workload_v2(
            workload_v2_create_request=workload_v2_create_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_workload_v2: {e}")


def example_delete_workload_v2():
    """
    Example of using delete_workload_v2

    Delete a workload. [Experimental]
    Delete a specific workload by ID
    """
    try:
        # Prepare the request parameters
        workload_v2_id = "example_workload_v2_id"

        # Make the API call
        api_response = api_instance.delete_workload_v2(
            workload_v2_id=workload_v2_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling delete_workload_v2: {e}")


def example_get_workload_v2_by_id():
    """
    Example of using get_workload_v2_by_id

    Get a specific workload. [Experimental]
    Retrieve details of a specific workload by ID
    """
    try:
        # Prepare the request parameters
        workload_v2_id = "example_workload_v2_id"

        # Make the API call
        api_response = api_instance.get_workload_v2_by_id(
            workload_v2_id=workload_v2_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_workload_v2_by_id: {e}")


def example_update_workload_v2():
    """
    Example of using update_workload_v2

    Update workload spec. [Experimental]
    Update the specification of an existing workload.
    """
    try:
        # Prepare the request parameters
        workload_v2_id = "example_workload_v2_id"

        # Create example data for WorkloadV2UpdateRequest
        workload_v2_update_request = models.WorkloadV2UpdateRequest(
            metadata=runai.models.workload_v2_metadata_update_params.WorkloadV2MetadataUpdateParams(
                priority="jUR,rZ#UM/?R,Fp^l6$ARj",
                category="jUR,rZ#UM/?R,Fp^l6$ARj",
            ),
            manifest={
                "apiVersion": "apps/v1",
                "kind": "Deployment",
                "metadata": {"name": "my-app"},
                "spec": {
                    "replicas": 1,
                    "selector": {"matchLabels": {"app": "my-app"}},
                    "template": {
                        "metadata": {"labels": {"app": "my-app"}},
                        "spec": {
                            "containers": [{"name": "app", "image": "nginx:latest"}]
                        },
                    },
                },
            },
            manifest_base64_encoded="[B@71ea1fda",
        )

        # Make the API call
        api_response = api_instance.update_workload_v2(
            workload_v2_id=workload_v2_id,
            workload_v2_update_request=workload_v2_update_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_workload_v2: {e}")
