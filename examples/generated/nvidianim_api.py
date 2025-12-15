"""
Examples for using the NVIDIANIMApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import NVIDIANIMApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = NVIDIANIMApi(api_client)


def example_create_nim_service():
    """
    Example of using create_nim_service

    Create a NVIDIA NIM service. [Experimental]
    Create a NVIDIA NIM service
    """
    try:
        # Prepare the request parameters

        # Create example data for NimServiceCreateRequest
        nim_service_create_request = models.NimServiceCreateRequest(
            metadata=runai.models.nim_service_metadata_create_params.NIMServiceMetadataCreateParams(
                name="my-workload-name",
                use_given_name_as_prefix=True,
                project_id="1",
            ),
            spec=None,
        )

        # Make the API call
        api_response = api_instance.create_nim_service(
            nim_service_create_request=nim_service_create_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_nim_service: {e}")


def example_get_nim_service_by_id():
    """
    Example of using get_nim_service_by_id

    Get a NVIDIA NIM service. [Experimental]
    Retrieve details of a specific NVIDIA NIM service, by id
    """
    try:
        # Prepare the request parameters
        workload_v2_id = "example_workload_v2_id"

        # Make the API call
        api_response = api_instance.get_nim_service_by_id(
            workload_v2_id=workload_v2_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_nim_service_by_id: {e}")


def example_update_nim_service_spec():
    """
    Example of using update_nim_service_spec

    Update NVIDIA NIM service spec. [Experimental]
    Update the specification of an existing NVIDIA NIM service.
    """
    try:
        # Prepare the request parameters
        workload_v2_id = "example_workload_v2_id"

        # Create example data for NimServiceUpdateRequest
        nim_service_update_request = models.NimServiceUpdateRequest(spec=None)

        # Make the API call
        api_response = api_instance.update_nim_service_spec(
            workload_v2_id=workload_v2_id,
            nim_service_update_request=nim_service_update_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_nim_service_spec: {e}")
