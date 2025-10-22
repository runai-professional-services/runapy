"""
Examples for using the CredentialsApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import CredentialsApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = CredentialsApi(api_client)

def example_create_access_key():
    """
    Example of using create_access_key
    
    Create an access key.
    Use to create an S3-compatible access key credential.
    """
    try:
        # Prepare the request parameters
        
        # Create example data for AccessKeyCreationRequest
        access_key_creation_request = models.AccessKeyCreationRequest(
            meta = {"name":"my-asset","scope":"tenant","workloadSupportedTypes":{"workspace":false,"training":false,"inference":false,"distributed":true,"distFramework":"TF"}},
            spec = runai.models.access_key_creation_spec.AccessKeyCreationSpec(
                    existing_secret_name = '0', 
                    access_key_id = '0', 
                    secret_access_key = '0', )
        )

        # Make the API call
        api_response = api_instance.create_access_key(
            access_key_creation_request=access_key_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_access_key: {e}")

def example_create_docker_registry():
    """
    Example of using create_docker_registry
    
    Create a docker registry credential.
    Use to create a docker registry credential containing userid, password and url.
    """
    try:
        # Prepare the request parameters
        
        # Create example data for DockerRegistryCreationRequest
        docker_registry_creation_request = models.DockerRegistryCreationRequest(
            meta = {"name":"my-asset","scope":"tenant","workloadSupportedTypes":{"workspace":false,"training":false,"inference":false,"distributed":true,"distFramework":"TF"}},
            spec = runai.models.docker_registry_creation_spec.DockerRegistryCreationSpec(
                    existing_secret_name = '0', 
                    user = '0', 
                    password = '0', 
                    url = '0', )
        )

        # Make the API call
        api_response = api_instance.create_docker_registry(
            docker_registry_creation_request=docker_registry_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_docker_registry: {e}")

def example_create_generic_secret():
    """
    Example of using create_generic_secret
    
    Create a generic-secret.
    Use to create a generic-secret asset.
    """
    try:
        # Prepare the request parameters
        
        # Create example data for GenericSecretCreationRequest
        generic_secret_creation_request = models.GenericSecretCreationRequest(
            meta = {"name":"my-asset","scope":"tenant","workloadSupportedTypes":{"workspace":false,"training":false,"inference":false,"distributed":true,"distFramework":"TF"}},
            spec = runai.models.generic_secret_creation_spec.GenericSecretCreationSpec(
                    existing_secret_name = '0', 
                    key_value_pairs = [
                        {value=my-secret, key=secret-key}
                        ], )
        )

        # Make the API call
        api_response = api_instance.create_generic_secret(
            generic_secret_creation_request=generic_secret_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_generic_secret: {e}")

def example_create_ngc_api_key():
    """
    Example of using create_ngc_api_key
    
    Create a ngc-api-key.
    Use to create a ngc-api-key asset.
    """
    try:
        # Prepare the request parameters
        
        # Create example data for NgcApiKeyCreationRequest
        ngc_api_key_creation_request = models.NgcApiKeyCreationRequest(
            meta = {"name":"my-asset","scope":"tenant","workloadSupportedTypes":{"workspace":false,"training":false,"inference":false,"distributed":true,"distFramework":"TF"}},
            spec = runai.models.ngc_api_key_creation_spec.NgcApiKeyCreationSpec(
                    ngc_api_key = 'C0', )
        )

        # Make the API call
        api_response = api_instance.create_ngc_api_key(
            ngc_api_key_creation_request=ngc_api_key_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_ngc_api_key: {e}")

def example_create_password():
    """
    Example of using create_password
    
    Create a userid / password credential.
    Use to create a userid / password credential.
    """
    try:
        # Prepare the request parameters
        
        # Create example data for PasswordCreationRequest
        password_creation_request = models.PasswordCreationRequest(
            meta = {"name":"my-asset","scope":"tenant","workloadSupportedTypes":{"workspace":false,"training":false,"inference":false,"distributed":true,"distFramework":"TF"}},
            spec = runai.models.password_creation_spec.PasswordCreationSpec(
                    existing_secret_name = '0', 
                    user = '0', 
                    password = '0', )
        )

        # Make the API call
        api_response = api_instance.create_password(
            password_creation_request=password_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_password: {e}")

def example_delete_access_key():
    """
    Example of using delete_access_key
    
    Delete an access key.
    Use to delete an S3-compatible access key credential by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.delete_access_key(
            asset_id=asset_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling delete_access_key: {e}")

def example_delete_docker_registry():
    """
    Example of using delete_docker_registry
    
    Delete a docker registry credential.
    Use to deletes a docker registry credential by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.delete_docker_registry(
            asset_id=asset_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling delete_docker_registry: {e}")

def example_delete_generic_secret():
    """
    Example of using delete_generic_secret
    
    Delete a generic-secret.
    Use to delete a generic-secret asset, by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        

        # Make the API call
        api_instance.delete_generic_secret(
            asset_id=asset_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_generic_secret: {e}")

def example_delete_ngc_api_key():
    """
    Example of using delete_ngc_api_key
    
    Delete a ngc-api-key.
    Use to delete a ngc-api-key asset, by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        

        # Make the API call
        api_instance.delete_ngc_api_key(
            asset_id=asset_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_ngc_api_key: {e}")

def example_delete_password():
    """
    Example of using delete_password
    
    Delete a password asset.
    Udse to delete a password credential by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.delete_password(
            asset_id=asset_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling delete_password: {e}")

def example_get_access_key_by_id():
    """
    Example of using get_access_key_by_id
    
    Get an access key.
    Use to retrieve the details of an S3-compatible access key credential by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        
        
        usage_info = True
        
        
        
        
        
        
        
        status_info = True
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_access_key_by_id(
            asset_id=asset_id,
            usage_info=usage_info,
            status_info=status_info,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_access_key_by_id: {e}")

def example_get_docker_registry_by_id():
    """
    Example of using get_docker_registry_by_id
    
    Get a docker registry credential.
    Use to retrieve the details of a docker registry credential by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        
        
        usage_info = True
        
        
        
        
        
        
        
        status_info = True
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_docker_registry_by_id(
            asset_id=asset_id,
            usage_info=usage_info,
            status_info=status_info,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_docker_registry_by_id: {e}")

def example_get_generic_secret_by_id():
    """
    Example of using get_generic_secret_by_id
    
    Get a generic-secret.
    Returns the details of a generic-secret asset, by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        
        
        usage_info = True
        
        
        
        
        
        
        
        status_info = True
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_generic_secret_by_id(
            asset_id=asset_id,
            usage_info=usage_info,
            status_info=status_info,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_generic_secret_by_id: {e}")

def example_get_ngc_api_key_by_id():
    """
    Example of using get_ngc_api_key_by_id
    
    Get a ngc-api-key.
    Returns the details of a ngc-api-key asset, by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        
        
        usage_info = True
        
        
        
        
        
        
        
        status_info = True
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_ngc_api_key_by_id(
            asset_id=asset_id,
            usage_info=usage_info,
            status_info=status_info,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_ngc_api_key_by_id: {e}")

def example_get_password_by_id():
    """
    Example of using get_password_by_id
    
    Get a userid / password credential.
    Use to retrieve the details of a userid / password credential asset by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        
        
        usage_info = True
        
        
        
        
        
        
        
        status_info = True
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_password_by_id(
            asset_id=asset_id,
            usage_info=usage_info,
            status_info=status_info,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_password_by_id: {e}")

def example_list_access_keys():
    """
    Example of using list_access_keys
    
    List access keys.
    Use to retrieve a list of S3-compatible access key credentials.
    """
    try:
        # Prepare the request parameters
        name = "example_name"
        
        
        
        
        
        
        
        scope = "example_scope"
        
        
        
        
        
        
        
        
        project_id = 42
        
        
        
        
        
        
        department_id = "example_department_id"
        
        
        
        
        
        
        
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        
        
        
        usage_info = True
        
        
        
        
        
        
        
        status_info = True
        
        
        
        
        

        # Make the API call
        api_response = api_instance.list_access_keys(
            name=name,
            scope=scope,
            project_id=project_id,
            department_id=department_id,
            cluster_id=cluster_id,
            usage_info=usage_info,
            status_info=status_info,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_access_keys: {e}")

def example_list_credentials_assets():
    """
    Example of using list_credentials_assets
    
    List credentials.
    Use to retrieve a list of all existing credentials.
    """
    try:
        # Prepare the request parameters
        name = "example_name"
        
        
        
        
        
        
        
        scope = "example_scope"
        
        
        
        
        
        
        
        
        project_id = 42
        
        
        
        
        
        
        department_id = "example_department_id"
        
        
        
        
        
        
        
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        
        
        
        usage_info = True
        
        
        
        
        
        
        
        status_info = True
        
        
        
        
        

        # Make the API call
        api_response = api_instance.list_credentials_assets(
            name=name,
            scope=scope,
            project_id=project_id,
            department_id=department_id,
            cluster_id=cluster_id,
            usage_info=usage_info,
            status_info=status_info,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_credentials_assets: {e}")

def example_list_docker_registries():
    """
    Example of using list_docker_registries
    
    List docker registry credentials.
    Use to retrieve a list of docker registry credentials.
    """
    try:
        # Prepare the request parameters
        name = "example_name"
        
        
        
        
        
        
        
        scope = "example_scope"
        
        
        
        
        
        
        
        
        project_id = 42
        
        
        
        
        
        
        department_id = "example_department_id"
        
        
        
        
        
        
        
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        
        
        
        usage_info = True
        
        
        
        
        
        
        
        status_info = True
        
        
        
        
        

        # Make the API call
        api_response = api_instance.list_docker_registries(
            name=name,
            scope=scope,
            project_id=project_id,
            department_id=department_id,
            cluster_id=cluster_id,
            usage_info=usage_info,
            status_info=status_info,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_docker_registries: {e}")

def example_list_generic_secret():
    """
    Example of using list_generic_secret
    
    List generic-secrets.
    Retrieve a list of generic-secret assets.
    """
    try:
        # Prepare the request parameters
        name = "example_name"
        
        
        
        
        
        
        
        scope = "example_scope"
        
        
        
        
        
        
        
        
        project_id = 42
        
        
        
        
        
        
        department_id = "example_department_id"
        
        
        
        
        
        
        
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        
        
        
        usage_info = True
        
        
        
        
        
        
        
        status_info = True
        
        
        
        
        

        # Make the API call
        api_response = api_instance.list_generic_secret(
            name=name,
            scope=scope,
            project_id=project_id,
            department_id=department_id,
            cluster_id=cluster_id,
            usage_info=usage_info,
            status_info=status_info,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_generic_secret: {e}")

def example_list_ngc_api_key():
    """
    Example of using list_ngc_api_key
    
    List ngc-api-keys.
    Retrieve a list of ngcApiKey assets.
    """
    try:
        # Prepare the request parameters
        name = "example_name"
        
        
        
        
        
        
        
        scope = "example_scope"
        
        
        
        
        
        
        
        
        project_id = 42
        
        
        
        
        
        
        department_id = "example_department_id"
        
        
        
        
        
        
        
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        
        
        
        usage_info = True
        
        
        
        
        
        
        
        status_info = True
        
        
        
        
        

        # Make the API call
        api_response = api_instance.list_ngc_api_key(
            name=name,
            scope=scope,
            project_id=project_id,
            department_id=department_id,
            cluster_id=cluster_id,
            usage_info=usage_info,
            status_info=status_info,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_ngc_api_key: {e}")

def example_list_passwords():
    """
    Example of using list_passwords
    
    List password credentials.
    Use to retrieve a list of password credentials.
    """
    try:
        # Prepare the request parameters
        name = "example_name"
        
        
        
        
        
        
        
        scope = "example_scope"
        
        
        
        
        
        
        
        
        project_id = 42
        
        
        
        
        
        
        department_id = "example_department_id"
        
        
        
        
        
        
        
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        
        
        
        usage_info = True
        
        
        
        
        
        
        
        status_info = True
        
        
        
        
        

        # Make the API call
        api_response = api_instance.list_passwords(
            name=name,
            scope=scope,
            project_id=project_id,
            department_id=department_id,
            cluster_id=cluster_id,
            usage_info=usage_info,
            status_info=status_info,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_passwords: {e}")

def example_update_access_key():
    """
    Example of using update_access_key
    
    Update an access key.
    Use to update the details of an S3-compatible access key credential by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        
        # Create example data for AccessKeyUpdateRequest
        access_key_update_request = models.AccessKeyUpdateRequest(
            meta = {"description":"my-credentials"}
        )

        # Make the API call
        api_response = api_instance.update_access_key(
            asset_id=asset_id,
            access_key_update_request=access_key_update_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_access_key: {e}")

def example_update_docker_registry():
    """
    Example of using update_docker_registry
    
    Update a docker registry credential.
    Use to updates the details of a docker registry credentials by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        
        # Create example data for DockerRegistryUpdateRequest
        docker_registry_update_request = models.DockerRegistryUpdateRequest(
            meta = {"description":"my-credentials"}
        )

        # Make the API call
        api_response = api_instance.update_docker_registry(
            asset_id=asset_id,
            docker_registry_update_request=docker_registry_update_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_docker_registry: {e}")

def example_update_generic_secret():
    """
    Example of using update_generic_secret
    
    Update a generic-secret.
    Updates the details of a generic-secret asset, by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        
        # Create example data for GenericSecretUpdateRequest
        generic_secret_update_request = models.GenericSecretUpdateRequest(
            meta = {"description":"my-credentials"}
        )

        # Make the API call
        api_response = api_instance.update_generic_secret(
            asset_id=asset_id,
            generic_secret_update_request=generic_secret_update_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_generic_secret: {e}")

def example_update_ngc_api_key():
    """
    Example of using update_ngc_api_key
    
    Update a ngc-api-key.
    Updates the details of a ngc-api-key asset, by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        
        # Create example data for NgcApiKeyUpdateRequest
        ngc_api_key_update_request = models.NgcApiKeyUpdateRequest(
            meta = {"description":"my-credentials"}
        )

        # Make the API call
        api_response = api_instance.update_ngc_api_key(
            asset_id=asset_id,
            ngc_api_key_update_request=ngc_api_key_update_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_ngc_api_key: {e}")

def example_update_password():
    """
    Example of using update_password
    
    Update a password credential.
    Use to Update the details of a password credential by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        
        # Create example data for PasswordUpdateRequest
        password_update_request = models.PasswordUpdateRequest(
            meta = {"description":"my-credentials"}
        )

        # Make the API call
        api_response = api_instance.update_password(
            asset_id=asset_id,
            password_update_request=password_update_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_password: {e}")

