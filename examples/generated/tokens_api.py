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
    Retrieve access token for an application. The application token is retrieved from the authorization server.
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


def example_exchange_code_for_token():
    """
    Example of using exchange_code_for_token

    exchange code for token
    Exchanges an authorization code for an access token. The authorization code is retrieved from the authorization server.
    """
    try:
        # Prepare the request parameters
        redirect_uri = "example_redirect_uri"

        code = "example_code"

        # Make the API call
        api_response = api_instance.exchange_code_for_token(
            redirect_uri=redirect_uri,
            code=code,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling exchange_code_for_token: {e}")


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
        )

        # Make the API call
        api_response = api_instance.grant_token(
            user_agent=user_agent,
            token_request=token_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling grant_token: {e}")


def example_refresh_token():
    """
    Example of using refresh_token

    refresh token
    Refreshes an user tokens. The refresh token is retrieved from the authorization server.
    """
    try:
        # Prepare the request parameters
        refresh_token = "example_refresh_token"

        # Make the API call
        api_response = api_instance.refresh_token(
            refresh_token=refresh_token,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling refresh_token: {e}")
