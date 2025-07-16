"""
Examples for using the OrgUnitApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import OrgUnitApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = OrgUnitApi(api_client)


def example_get_priorities():
    """
    Example of using get_priorities

    Get priorities
    Get priorities
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_priorities()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_priorities: {e}")
