"""
Examples for using the RegistryApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import RegistryApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = RegistryApi(api_client)

def example_create_registry():
    """
    Example of using create_registry
    
    Create a registry asset.
    Use to create a registry asset containing a registry base url and credentials.
    """
    try:
        # Prepare the request parameters
        
        # Create example data for RegistryCreationRequest
        registry_creation_request = models.RegistryCreationRequest(
            meta = {"name":"my-asset","scope":"tenant","workloadSupportedTypes":{"workspace":false,"training":false,"inference":false,"distributed":true,"distFramework":"TF"}},
            spec = {password=12345678, credentialKind=password, user=admin, url=https://hub.docker.com/}
        )

        # Make the API call
        api_response = api_instance.create_registry(
            registry_creation_request=registry_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_registry: {e}")

def example_delete_registry():
    """
    Example of using delete_registry
    
    Delete a registry asset.
    Use to delete a registry asset containing registry base url and credentials by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        

        # Make the API call
        api_instance.delete_registry(
            asset_id=asset_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_registry: {e}")

def example_get_registry_by_id():
    """
    Example of using get_registry_by_id
    
    Get a registry.
    Retrieve a registry asset by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_registry_by_id(
            asset_id=asset_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_registry_by_id: {e}")

def example_get_repositories():
    """
    Example of using get_repositories
    
    Get the repositories in the registry.
    Retrieve a list of repositories from a registry asset.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        search_name = "example_search_name"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_repositories(
            asset_id=asset_id,
            search_name=search_name,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_repositories: {e}")

def example_get_repository_tags():
    """
    Example of using get_repository_tags
    
    Get the repositories tags in the registry.
    Retrieve a list of repository tags from a repository asset.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        repository = "example_repository"
        
        
        
        
        
        
        
        search_name = "example_search_name"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_repository_tags(
            asset_id=asset_id,
            repository=repository,
            search_name=search_name,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_repository_tags: {e}")

def example_list_registries():
    """
    Example of using list_registries
    
    Get registries.
    Retrieve a list of registries assets.
    """
    try:
        # Prepare the request parameters
        name = "example_name"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.list_registries(
            name=name,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_registries: {e}")

def example_update_registry():
    """
    Example of using update_registry
    
    Update a registry asset.
    Use to update a registry asset containing registry base url and credentials by id.
    """
    try:
        # Prepare the request parameters
        asset_id = "example_asset_id"
        
        
        
        
        
        
        
        
        # Create example data for RegistryUpdateRequest
        registry_update_request = models.RegistryUpdateRequest(
            meta = {"name":"my-asset"}
        )

        # Make the API call
        api_response = api_instance.update_registry(
            asset_id=asset_id,
            registry_update_request=registry_update_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_registry: {e}")

