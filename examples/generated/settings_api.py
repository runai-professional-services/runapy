"""
Examples for using the SettingsApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import SettingsApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = SettingsApi(api_client)


def example_get_security_setting_by_key():
    """
    Example of using get_security_setting_by_key

    Get security setting by key

    """
    try:
        # Prepare the request parameters

        # Make the API call
        api_response = api_instance.get_security_setting_by_key(
            key=key,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_security_setting_by_key: {e}")


def example_get_security_settings():
    """
    Example of using get_security_settings

    Get security settings

    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_security_settings()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_security_settings: {e}")


def example_update_security_setting_by_key():
    """
    Example of using update_security_setting_by_key

    Update security setting by key

    """
    try:
        # Prepare the request parameters

        # Create example data for UpdateSecuritySettingByKeyRequest
        update_security_setting_by_key_request = (
            models.UpdateSecuritySettingByKeyRequest()
        )

        # Make the API call
        api_instance.update_security_setting_by_key(
            key=key,
            update_security_setting_by_key_request=update_security_setting_by_key_request,
        )

    except Exception as e:
        print(f"Exception when calling update_security_setting_by_key: {e}")
