"""
Examples for using the DistributedInferencesApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import DistributedInferencesApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = DistributedInferencesApi(api_client)


def example_create_distributed_inference():
    """
    Example of using create_distributed_inference

    Create a distributed inference. [Experimental]
    Create a distributed inference using container related fields.
    """
    try:
        # Prepare the request parameters

        # Create example data for DistributedInferenceCreationRequest
        distributed_inference_creation_request = (
            models.DistributedInferenceCreationRequest()
        )

        # Make the API call
        api_response = api_instance.create_distributed_inference(
            distributed_inference_creation_request=distributed_inference_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_distributed_inference: {e}")


def example_delete_distributed_inference():
    """
    Example of using delete_distributed_inference

    Delete a distributed inference.
    Delete a distributed inference using a workload id.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        # Make the API call
        api_response = api_instance.delete_distributed_inference(
            workload_id=workload_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling delete_distributed_inference: {e}")


def example_get_distributed_inference():
    """
    Example of using get_distributed_inference

    Get a distributed inference data.
    Retrieve a distributed inference details using a workload id.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        # Make the API call
        api_response = api_instance.get_distributed_inference(
            workload_id=workload_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_distributed_inference: {e}")


def example_update_distributed_inference_spec():
    """
    Example of using update_distributed_inference_spec

    Update distributed inference spec.
    Update the specification of an existing distributed inference workload.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        # Create example data for UpdateRequest
        update_request = models.UpdateRequest()

        # Make the API call
        api_response = api_instance.update_distributed_inference_spec(
            workload_id=workload_id,
            update_request=update_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_distributed_inference_spec: {e}")
