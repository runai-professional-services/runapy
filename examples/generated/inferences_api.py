"""
Examples for using the InferencesApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import InferencesApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = InferencesApi(api_client)


def example_create_inference1():
    """
    Example of using create_inference1

    Create an inference.
    Create an inference using container related fields.
    """
    try:
        # Prepare the request parameters

        # Create example data for InferenceCreationRequest
        inference_creation_request = models.InferenceCreationRequest()

        # Make the API call
        api_response = api_instance.create_inference1(
            inference_creation_request=inference_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_inference1: {e}")


def example_delete_inference():
    """
    Example of using delete_inference

    Delete an inference.
    Delete an inference using a workload id.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        # Make the API call
        api_instance.delete_inference(
            workload_id=workload_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_inference: {e}")


def example_get_inference():
    """
    Example of using get_inference

    Get inference data.
    Retrieve inference details using a workload id.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        # Make the API call
        api_response = api_instance.get_inference(
            workload_id=workload_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_inference: {e}")


def example_get_inference_workload_metrics():
    """
    Example of using get_inference_workload_metrics

    Get inference metrics data.
    Retrieve inference metrics data by id. Supported from control-plane version 2.18 or later.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        metric_type = ["example_item_1", "example_item_2"]

        start = "2024-12-29T12:00:00Z"

        end = "2024-12-29T12:00:00Z"

        number_of_samples = 42

        # Make the API call
        api_response = api_instance.get_inference_workload_metrics(
            workload_id=workload_id,
            metric_type=metric_type,
            start=start,
            end=end,
            number_of_samples=number_of_samples,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_inference_workload_metrics: {e}")


def example_get_inference_workload_pod_metrics():
    """
    Example of using get_inference_workload_pod_metrics

    Get inference pod&#39;s metrics data.
    Retrieve inference metrics pod&#39;s data by workload and pod id. Supported from control-plane version 2.18 or later.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        pod_id = "example_pod_id"

        metric_type = ["example_item_1", "example_item_2"]

        start = "2024-12-29T12:00:00Z"

        end = "2024-12-29T12:00:00Z"

        number_of_samples = 42

        # Make the API call
        api_response = api_instance.get_inference_workload_pod_metrics(
            workload_id=workload_id,
            pod_id=pod_id,
            metric_type=metric_type,
            start=start,
            end=end,
            number_of_samples=number_of_samples,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_inference_workload_pod_metrics: {e}")


def example_update_inference_spec():
    """
    Example of using update_inference_spec

    Update inference spec. [Experimental]
    Update the specification of an existing inference workload.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        # Create example data for InferenceUpdateRequest
        inference_update_request = models.InferenceUpdateRequest()

        # Make the API call
        api_response = api_instance.update_inference_spec(
            workload_id=workload_id,
            inference_update_request=inference_update_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_inference_spec: {e}")
