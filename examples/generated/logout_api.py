"""
Examples for using the LogoutApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import LogoutApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = LogoutApi(api_client)


def example_logout():
    """
    Example of using logout

    Logout

    """
    try:
        # Make the API call with no parameters
        api_instance.logout()

    except Exception as e:
        print(f"Exception when calling logout: {e}")
