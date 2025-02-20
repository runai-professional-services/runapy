"""
Examples for using the TenantApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import TenantApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = TenantApi(api_client)


def example_get_tenant_settings():
    """
    Example of using get_tenant_settings

    Get all tenant settings.
    Retrieve all tenant settings.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_tenant_settings()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_tenant_settings: {e}")


def example_get_tenant_settings_by_key():
    """
    Example of using get_tenant_settings_by_key

    Get a tenant setting by key.
    Retrieve a specific tenant setting by key.
    """
    try:
        # Prepare the request parameters
        setting_key = "example_setting_key"

        # Make the API call
        api_response = api_instance.get_tenant_settings_by_key(
            setting_key=setting_key,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_tenant_settings_by_key: {e}")


def example_logo():
    """
    Example of using logo

    Get tenant logo.
    Get tennant logo
    """
    try:
        # Prepare the request parameters

        tenant_id = 42

        # Make the API call
        api_response = api_instance.logo(
            tenant_id=tenant_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling logo: {e}")


def example_update_tenant_setting():
    """
    Example of using update_tenant_setting

    Update a tenant setting.
    Use to update tenant settings.
    """
    try:
        # Prepare the request parameters

        # Create example data for TenantSettingCreationRequest
        tenant_setting_creation_request = models.TenantSettingCreationRequest(
            key="department.use", value=true
        )

        # Make the API call
        api_response = api_instance.update_tenant_setting(
            tenant_setting_creation_request=tenant_setting_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_tenant_setting: {e}")


def example_upload_tenant_logo():
    """
    Example of using upload_tenant_logo

    Upload a tenant logo.
    Upload tenant logo file. Max size of 128kb.
    """
    try:
        # Prepare the request parameters

        tenant_id = 42

        # Create example data for Logo200Response
        logo200_response = models.Logo200Response(logo="")

        # Make the API call
        api_instance.upload_tenant_logo(
            tenant_id=tenant_id,
            logo200_response=logo200_response,
        )

    except Exception as e:
        print(f"Exception when calling upload_tenant_logo: {e}")
