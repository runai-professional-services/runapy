"""
Examples for using the RevisionsApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import RevisionsApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = RevisionsApi(api_client)


def example_count_inference_workload_revisions():
    """
    Example of using count_inference_workload_revisions

    Get inference workload revisions count.
    Retrieve the number of an inference workload revisions from a cluster.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        deleted = True

        # Make the API call
        api_response = api_instance.count_inference_workload_revisions(
            workload_id=workload_id,
            deleted=deleted,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling count_inference_workload_revisions: {e}")


def example_get_inference_workload_revisions():
    """
    Example of using get_inference_workload_revisions

    Get inference workload revisions by id.
    Retrieve the details of inference workload revisions by workload id.
    """
    try:
        # Prepare the request parameters
        workload_id = "example_workload_id"

        deleted = True

        # Make the API call
        api_response = api_instance.get_inference_workload_revisions(
            workload_id=workload_id,
            deleted=deleted,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_inference_workload_revisions: {e}")


def example_get_revision():
    """
    Example of using get_revision

    Get revision data.
    Retrieve revision details using a revision id.
    """
    try:
        # Prepare the request parameters
        revision_id = "example_revision_id"

        # Make the API call
        api_response = api_instance.get_revision(
            revision_id=revision_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_revision: {e}")
