"""
Examples for using the StorageClassesApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import StorageClassesApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = StorageClassesApi(api_client)


def example_get_storage_classes():
    """
    Example of using get_storage_classes

    Get all storageClasses from a cluster.
    Retrieve a list of storageClass names by Universally Unique Identifier (UUID) of the cluster.
    """
    try:
        # Prepare the request parameters
        uuid = "example_uuid"

        # Make the API call
        api_response = api_instance.get_storage_classes(
            uuid=uuid,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_storage_classes: {e}")
