"""
Examples for using the TokensApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import TokensApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = TokensApi(api_client)


def example_grant_token():
    """
    Example of using grant_token

    Create an access token v1
    Create tokens using the &#x60;grant_type&#x60; parameter. This endpoint is deprecated. Use &#x60;/api/v2/token&#x60; instead.
    """
    try:
        # Prepare the request parameters

        # Create example data for TokenRequest
        token_request = models.TokenRequest(
            grant_type="client_credentials",
            code="",
            redirect_uri="",
            refresh_token="",
            username="",
            password="",
            client_id="",
            client_secret="",
            external_token="",
            code_verifier="",
        )

        # Make the API call
        api_response = api_instance.grant_token(
            token_request=token_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling grant_token: {e}")


def example_grant_token_v2():
    """
    Example of using grant_token_v2

    Create an access token v2
    Use this endpoint to obtain an access token. Compliant with standard OAuth2 protocol and supports the common OAuth2 grant types.
    """
    try:
        # Prepare the request parameters
        grant_type = "example_grant_type"

        client_id = "example_client_id"

        client_secret = "example_client_secret"

        username = "example_username"

        password = "example_password"

        external_token = "example_external_token"

        # Make the API call
        api_response = api_instance.grant_token_v2(
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            username=username,
            password=password,
            external_token=external_token,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling grant_token_v2: {e}")
