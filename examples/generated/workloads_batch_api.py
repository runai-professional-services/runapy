"""
Examples for using the WorkloadsBatchApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import WorkloadsBatchApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = WorkloadsBatchApi(api_client)


def example_batch_workloads():
    """
    Example of using batch_workloads

    Workload batch operations.

    """
    try:
        # Prepare the request parameters

        # Create example data for WorkloadBatch
        workload_batch = models.WorkloadBatch(ids=[""], action="delete")

        # Make the API call
        api_response = api_instance.batch_workloads(
            workload_batch=workload_batch,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling batch_workloads: {e}")
