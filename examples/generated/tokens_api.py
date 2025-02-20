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

    Create an application token.
    Use to create application tokens. Select a token using the &#x60;grant_type&#x60; parameter.
    """
    try:
        # Prepare the request parameters
        user_agent = "example_user_agent"

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
        )

        # Make the API call
        api_response = api_instance.grant_token(
            user_agent=user_agent,
            token_request=token_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling grant_token: {e}")
