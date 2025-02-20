"""
Examples for using the DeploymentsApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import DeploymentsApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = DeploymentsApi(api_client)


def example_get_deployment():
    """
    Example of using get_deployment

    Get a deployment by id

    """
    try:
        # Prepare the request parameters
        uuid = "example_uuid"

        deployment_id = "example_deployment_id"

        # Make the API call
        api_response = api_instance.get_deployment(
            uuid=uuid,
            deployment_id=deployment_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_deployment: {e}")


def example_get_deployments():
    """
    Example of using get_deployments

    List deployments

    """
    try:
        # Prepare the request parameters
        uuid = "example_uuid"

        # Make the API call
        api_response = api_instance.get_deployments(
            uuid=uuid,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_deployments: {e}")
