"""
Examples for using the LogoApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import LogoApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = LogoApi(api_client)


def example_get_tenant_logo():
    """
    Example of using get_tenant_logo

    Get tenant logo. (base64)
    Retrieve the base64 logo file.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_tenant_logo()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_tenant_logo: {e}")


def example_upload_tenant_logo():
    """
    Example of using upload_tenant_logo

    Upload logo for tenant. (base64)
    Use to upload a base64 logo file. Max size 128kb.
    """
    try:
        # Prepare the request parameters

        # Create example data for LogoCreationRequest
        logo_creation_request = models.LogoCreationRequest(logo="")

        # Make the API call
        api_instance.upload_tenant_logo(
            logo_creation_request=logo_creation_request,
        )

    except Exception as e:
        print(f"Exception when calling upload_tenant_logo: {e}")
