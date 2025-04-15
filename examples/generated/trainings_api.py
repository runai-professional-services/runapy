"""
Examples for using the TrainingsApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import TrainingsApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = TrainingsApi(api_client)


def example_create_training1():
    """
    Example of using create_training1

    Create a training.
    Create a training workload using container related fields.
    """
    try:
        # Prepare the request parameters

        # Create example data for TrainingCreationRequest
        training_creation_request = models.TrainingCreationRequest()

        # Make the API call
        api_response = api_instance.create_training1(
            training_creation_request=training_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_training1: {e}")


def example_delete_training():
    """
    Example of using delete_training

    Delete a training.
    Delete a training using a workload id.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        # Make the API call
        api_response = api_instance.delete_training(
            workload_id=workload_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling delete_training: {e}")


def example_get_training():
    """
    Example of using get_training

    Get training data.
    Retrieve training details using a workload id.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        # Make the API call
        api_response = api_instance.get_training(
            workload_id=workload_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_training: {e}")


def example_resume_training():
    """
    Example of using resume_training

    Resume a training.
    Resume a training that was suspended using a workload id.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        # Make the API call
        api_response = api_instance.resume_training(
            workload_id=workload_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling resume_training: {e}")


def example_suspend_training():
    """
    Example of using suspend_training

    Suspend a training.
    Suspend a training from running using a workload id.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        # Make the API call
        api_response = api_instance.suspend_training(
            workload_id=workload_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling suspend_training: {e}")
