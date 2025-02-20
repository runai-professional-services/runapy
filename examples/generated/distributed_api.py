"""
Examples for using the DistributedApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import DistributedApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = DistributedApi(api_client)


def example_create_distributed():
    """
    Example of using create_distributed

    Create a distributed training.
    Use to create a distributed training.
    """
    try:
        # Prepare the request parameters

        # Create example data for DistributedCreationRequest
        distributed_creation_request = models.DistributedCreationRequest()

        # Make the API call
        api_response = api_instance.create_distributed(
            distributed_creation_request=distributed_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_distributed: {e}")


def example_delete_distributed():
    """
    Example of using delete_distributed

    Delete a distributed training by id.
    Use to delete a distributed training by workload id.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        # Make the API call
        api_instance.delete_distributed(
            workload_id=workload_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_distributed: {e}")


def example_get_distributed():
    """
    Example of using get_distributed

    Get distributed training&#39;s data. [Experimental]
    Retrieve the details of a distributed training by workload id.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        # Make the API call
        api_response = api_instance.get_distributed(
            workload_id=workload_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_distributed: {e}")
