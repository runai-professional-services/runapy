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


def example_app_token():
    """
    Example of using app_token

    get application token
    Retrieve access token for an application. The application token is retrieved from the authorization server. This endpoint is deprecated.  Use /api/v1/token with the grantType parameter set to app_token instead, with AppID and appSecret set accordingly to get an application token
    """
    try:
        # Prepare the request parameters

        # Create example data for AppTokenRequest
        app_token_request = models.AppTokenRequest(id="", name="", secret="")

        # Make the API call
        api_response = api_instance.app_token(
            app_token_request=app_token_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling app_token: {e}")


def example_grant_token():
    """
    Example of using grant_token

    Create an access token v1
    Create tokens using the &#x60;grant_type&#x60; parameter.
    """
    try:
        # Prepare the request parameters

        # Create example data for TokenRequest
        token_request = models.TokenRequest(
            grant_type="app_token",
            app_id="",
            app_secret="",
            code="",
            redirect_uri="",
            refresh_token="",
            username="",
            password="",
            client_id="",
            client_secret="",
            external_token="",
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

        refresh_token = "example_refresh_token"

        code = "example_code"

        redirect_uri = "example_redirect_uri"

        # Make the API call
        api_response = api_instance.grant_token_v2(
            grant_type=grant_type,
            client_id=client_id,
            client_secret=client_secret,
            username=username,
            password=password,
            refresh_token=refresh_token,
            code=code,
            redirect_uri=redirect_uri,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling grant_token_v2: {e}")
