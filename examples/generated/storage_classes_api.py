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

    get a Storage Class/Classes for a given cluster

    """
    try:
        # Prepare the request parameters
        cluster_id = "example_cluster_id"

        name = "example_name"

        include_none = True

        # Make the API call
        api_response = api_instance.get_storage_classes(
            cluster_id=cluster_id,
            name=name,
            include_none=include_none,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_storage_classes: {e}")


def example_v1_get_storage_classes():
    """
    Example of using v1_get_storage_classes

    Get all storageClasses from a cluster.
    this API is used by cluster versions &lt; 2.20
    """
    try:
        # Prepare the request parameters
        uuid = "example_uuid"

        include_none = True

        # Make the API call
        api_response = api_instance.v1_get_storage_classes(
            uuid=uuid,
            include_none=include_none,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling v1_get_storage_classes: {e}")
