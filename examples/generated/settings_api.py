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


def example_get_authorization_setting_by_key():
    """
    Example of using get_authorization_setting_by_key

    Get authorization setting by key

    """
    try:
        # Prepare the request parameters

        # Make the API call
        api_response = api_instance.get_authorization_setting_by_key(
            key=key,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_authorization_setting_by_key: {e}")


def example_get_authorization_settings():
    """
    Example of using get_authorization_settings

    Get authorization settings

    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_authorization_settings()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_authorization_settings: {e}")


def example_get_branding_setting_by_key():
    """
    Example of using get_branding_setting_by_key

    Get branding setting by key
    Returns a single branding setting identified by the path key.
    """
    try:
        # Prepare the request parameters

        # Make the API call
        api_response = api_instance.get_branding_setting_by_key(
            key=key,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_branding_setting_by_key: {e}")


def example_get_branding_settings():
    """
    Example of using get_branding_settings

    Get branding settings
    Returns all branding-related settings for the tenant.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_branding_settings()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_branding_settings: {e}")


def example_get_cluster_setting_by_key():
    """
    Example of using get_cluster_setting_by_key

    Get cluster setting by key

    """
    try:
        # Prepare the request parameters

        # Make the API call
        api_response = api_instance.get_cluster_setting_by_key(
            key=key,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_cluster_setting_by_key: {e}")


def example_get_cluster_settings():
    """
    Example of using get_cluster_settings

    Get cluster settings

    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_cluster_settings()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_cluster_settings: {e}")


def example_get_datavolumes_setting_by_key():
    """
    Example of using get_datavolumes_setting_by_key

    Get datavolumes setting by key

    """
    try:
        # Prepare the request parameters

        # Make the API call
        api_response = api_instance.get_datavolumes_setting_by_key(
            key=key,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_datavolumes_setting_by_key: {e}")


def example_get_datavolumes_settings():
    """
    Example of using get_datavolumes_settings

    Get datavolumes settings

    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_datavolumes_settings()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_datavolumes_settings: {e}")


def example_get_node_pool_setting_by_key():
    """
    Example of using get_node_pool_setting_by_key

    Get node pool setting by key

    """
    try:
        # Prepare the request parameters

        # Make the API call
        api_response = api_instance.get_node_pool_setting_by_key(
            key=key,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_node_pool_setting_by_key: {e}")


def example_get_node_pool_settings():
    """
    Example of using get_node_pool_settings

    Get node pool settings

    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_node_pool_settings()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_node_pool_settings: {e}")


def example_get_notifications_setting_by_key():
    """
    Example of using get_notifications_setting_by_key

    Get notifications setting by key
    Returns a single notifications setting identified by the path key.
    """
    try:
        # Prepare the request parameters

        # Make the API call
        api_response = api_instance.get_notifications_setting_by_key(
            key=key,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_notifications_setting_by_key: {e}")


def example_get_notifications_settings():
    """
    Example of using get_notifications_settings

    Get notifications settings
    Returns all notifications-related settings for the tenant.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_notifications_settings()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_notifications_settings: {e}")


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


def example_get_workloads_service_setting_by_key():
    """
    Example of using get_workloads_service_setting_by_key

    Get a workloads setting by key.
    Retrieve the current value of a specific workloads setting by its key.
    """
    try:
        # Prepare the request parameters

        # Make the API call
        api_response = api_instance.get_workloads_service_setting_by_key(
            key=key,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_workloads_service_setting_by_key: {e}")


def example_get_workloads_service_settings():
    """
    Example of using get_workloads_service_settings

    Get all workloads settings.
    Retrieve the current values of all workloads-related settings for the tenant.
    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_workloads_service_settings()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_workloads_service_settings: {e}")


def example_get_workloads_setting_by_key():
    """
    Example of using get_workloads_setting_by_key

    Get workloads setting by key

    """
    try:
        # Prepare the request parameters

        # Make the API call
        api_response = api_instance.get_workloads_setting_by_key(
            key=key,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_workloads_setting_by_key: {e}")


def example_get_workloads_settings():
    """
    Example of using get_workloads_settings

    Get workloads settings

    """
    try:
        # Make the API call with no parameters
        api_response = api_instance.get_workloads_settings()
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_workloads_settings: {e}")


def example_update_authorization_setting_by_key():
    """
    Example of using update_authorization_setting_by_key

    Update authorization setting by key

    """
    try:
        # Prepare the request parameters

        # Create example data for UpdateAuthorizationSettingByKeyRequest
        update_authorization_setting_by_key_request = (
            models.UpdateAuthorizationSettingByKeyRequest(enabled=True)
        )

        # Make the API call
        api_instance.update_authorization_setting_by_key(
            key=key,
            update_authorization_setting_by_key_request=update_authorization_setting_by_key_request,
        )

    except Exception as e:
        print(f"Exception when calling update_authorization_setting_by_key: {e}")


def example_update_branding_setting_by_key():
    """
    Example of using update_branding_setting_by_key

    Update branding setting by key
    Updates a single branding setting identified by the path key.
    """
    try:
        # Prepare the request parameters

        # Create example data for UpdateLogo
        update_logo = models.UpdateLogo(logo="")

        # Make the API call
        api_instance.update_branding_setting_by_key(
            key=key,
            update_logo=update_logo,
        )

    except Exception as e:
        print(f"Exception when calling update_branding_setting_by_key: {e}")


def example_update_cluster_setting_by_key():
    """
    Example of using update_cluster_setting_by_key

    Update cluster setting by key

    """
    try:
        # Prepare the request parameters

        # Create example data for UpdateClusterSettingByKeyRequest
        update_cluster_setting_by_key_request = models.UpdateClusterSettingByKeyRequest(
            enabled=True
        )

        # Make the API call
        api_instance.update_cluster_setting_by_key(
            key=key,
            update_cluster_setting_by_key_request=update_cluster_setting_by_key_request,
        )

    except Exception as e:
        print(f"Exception when calling update_cluster_setting_by_key: {e}")


def example_update_datavolumes_setting_by_key():
    """
    Example of using update_datavolumes_setting_by_key

    Update datavolumes setting by key

    """
    try:
        # Prepare the request parameters

        # Create example data for UpdateDatavolumesSettingByKeyRequest
        update_datavolumes_setting_by_key_request = (
            models.UpdateDatavolumesSettingByKeyRequest(enabled=True)
        )

        # Make the API call
        api_instance.update_datavolumes_setting_by_key(
            key=key,
            update_datavolumes_setting_by_key_request=update_datavolumes_setting_by_key_request,
        )

    except Exception as e:
        print(f"Exception when calling update_datavolumes_setting_by_key: {e}")


def example_update_node_pool_setting_by_key():
    """
    Example of using update_node_pool_setting_by_key

    Update node pool setting by key

    """
    try:
        # Prepare the request parameters

        # Create example data for UpdateNodePoolSettingByKeyRequest
        update_node_pool_setting_by_key_request = (
            models.UpdateNodePoolSettingByKeyRequest(enabled=True)
        )

        # Make the API call
        api_instance.update_node_pool_setting_by_key(
            key=key,
            update_node_pool_setting_by_key_request=update_node_pool_setting_by_key_request,
        )

    except Exception as e:
        print(f"Exception when calling update_node_pool_setting_by_key: {e}")


def example_update_notifications_setting_by_key():
    """
    Example of using update_notifications_setting_by_key

    Update notifications setting by key
    Updates a single notifications setting identified by the path key.
    """
    try:
        # Prepare the request parameters

        # Create example data for UpdateAdminMessage
        update_admin_message = models.UpdateAdminMessage(msg="", enable_dismiss=True)

        # Make the API call
        api_instance.update_notifications_setting_by_key(
            key=key,
            update_admin_message=update_admin_message,
        )

    except Exception as e:
        print(f"Exception when calling update_notifications_setting_by_key: {e}")


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


def example_update_workloads_service_setting_by_key():
    """
    Example of using update_workloads_service_setting_by_key

    Update a workloads setting by key.
    Update the value of a specific workloads setting by its key.
    """
    try:
        # Prepare the request parameters

        # Create example data for UpdateWorkloadsSettingByKeyRequest
        update_workloads_setting_by_key_request = (
            models.UpdateWorkloadsSettingByKeyRequest(enabled=True)
        )

        # Make the API call
        api_response = api_instance.update_workloads_service_setting_by_key(
            key=key,
            update_workloads_setting_by_key_request=update_workloads_setting_by_key_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_workloads_service_setting_by_key: {e}")


def example_update_workloads_setting_by_key():
    """
    Example of using update_workloads_setting_by_key

    Update workloads setting by key

    """
    try:
        # Prepare the request parameters

        # Create example data for YamlSubmissionSetting
        yaml_submission_setting = models.YamlSubmissionSetting(enabled=True)

        # Make the API call
        api_instance.update_workloads_setting_by_key(
            key=key,
            yaml_submission_setting=yaml_submission_setting,
        )

    except Exception as e:
        print(f"Exception when calling update_workloads_setting_by_key: {e}")
