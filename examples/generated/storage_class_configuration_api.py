"""
Examples for using the StorageClassConfigurationApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import StorageClassConfigurationApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = StorageClassConfigurationApi(api_client)

def example_create_storage_class_configuration():
    """
    Example of using create_storage_class_configuration
    
    Create storage class configuration
    Creates a new storage class configuration in the NVIDIA Run:ai platform. This endpoint enables administrators to define storage class behavior and customize their usage settings. 
    """
    try:
        # Prepare the request parameters
        
        # Create example data for StorageClassConfigurationCreationRequest
        storage_class_configuration_creation_request = models.StorageClassConfigurationCreationRequest(
            tenant_id = 1001,
            scope_type = 'cluster',
            scope_id = '',
            name = 'Standard',
            permissions = {allowDataSharing=true, allowedForWorkloads=true, allowedForEphemeralVolumes=true, allowedForPersistentVolumes=true, allowedForAssets=true},
            customization = {attributes=[Ljava.lang.Object;@c568f91, claimSize={default=1G, min=1G, max=1G, step=1G, supportedUnits=[Ljava.lang.Object;@5fd43e58}, accessMode={default={readOnlyMany=false, readWriteMany=false, readWriteOnce=true}, supportedValues={readOnlyMany=true, readWriteMany=true, readWriteOnce=true}, required=true}, volumeMode={default=Filesystem, supportedValues={block=true, filesystem=true}, required=true}}
        )

        # Make the API call
        api_response = api_instance.create_storage_class_configuration(
            storage_class_configuration_creation_request=storage_class_configuration_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_storage_class_configuration: {e}")

def example_delete_storage_class_configuration_by_id():
    """
    Example of using delete_storage_class_configuration_by_id
    
    Delete storage class configuration by id
    Deletes a specific storage class configuration by its unique identifier. Use this endpoint to permanently remove configurations that are no longer needed.
    """
    try:
        # Prepare the request parameters
        id = "example_id"
        
        
        
        
        
        
        
        
        tenant_id = 42
        
        
        
        
        
        

        # Make the API call
        api_instance.delete_storage_class_configuration_by_id(
            id=id,
            tenant_id=tenant_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_storage_class_configuration_by_id: {e}")

def example_get_storage_class_configuration_by_id():
    """
    Example of using get_storage_class_configuration_by_id
    
    Get storage class configuration by id
    Retrieves a specific storage class configuration by its unique identifier. Use this endpoint to view detailed information about the configuration, including its permissions and customization options. 
    """
    try:
        # Prepare the request parameters
        id = "example_id"
        
        
        
        
        
        
        
        
        tenant_id = 42
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_storage_class_configuration_by_id(
            id=id,
            tenant_id=tenant_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_storage_class_configuration_by_id: {e}")

def example_list_storage_class_configuration():
    """
    Example of using list_storage_class_configuration
    
    List storage class configurations
    Retrieves a list of storage class configurations defined in the system.
    """
    try:
        # Prepare the request parameters
        
        
        
        filter_by = ["example_item_1", "example_item_2"]
        
        
        
        
        sort_by = "example_sort_by"
        
        
        
        
        
        
        
        sort_order = "example_sort_order"
        
        
        
        
        
        
        
        
        offset = 42
        
        
        
        
        
        
        
        limit = 42
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.list_storage_class_configuration(
            filter_by=filter_by,
            sort_by=sort_by,
            sort_order=sort_order,
            offset=offset,
            limit=limit,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_storage_class_configuration: {e}")

def example_patch_storage_class_configuration_by_id():
    """
    Example of using patch_storage_class_configuration_by_id
    
    Patch storage class configuration by id
    Partially updates an existing storage class configuration by its unique identifier. Use this endpoint to modify specific fields, such as permissions, customization values, or attributes, without replacing the entire configuration.
    """
    try:
        # Prepare the request parameters
        id = "example_id"
        
        
        
        
        
        
        
        
        # Create example data for StorageClassConfigurationPatchRequest
        storage_class_configuration_patch_request = models.StorageClassConfigurationPatchRequest(
            permissions = {allowDataSharing=true, allowedForWorkloads=true, allowedForEphemeralVolumes=true, allowedForPersistentVolumes=true, allowedForAssets=true},
            customization = runai.models.storage_class_configuration_patch_request_customization.StorageClassConfigurationPatchRequest_customization()
        )
        
        tenant_id = 42
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.patch_storage_class_configuration_by_id(
            id=id,
            storage_class_configuration_patch_request=storage_class_configuration_patch_request,
            tenant_id=tenant_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling patch_storage_class_configuration_by_id: {e}")

def example_update_storage_class_configuration_by_id():
    """
    Example of using update_storage_class_configuration_by_id
    
    Update storage class configuration by id
    Updates an existing storage class configuration by its unique identifier. Use this endpoint to fully replace an existing configuration, including permissions and customization settings.
    """
    try:
        # Prepare the request parameters
        id = "example_id"
        
        
        
        
        
        
        
        
        # Create example data for StorageClassConfigurationUpdateRequest
        storage_class_configuration_update_request = models.StorageClassConfigurationUpdateRequest(
            permissions = {allowDataSharing=true, allowedForWorkloads=true, allowedForEphemeralVolumes=true, allowedForPersistentVolumes=true, allowedForAssets=true},
            customization = {attributes=[Ljava.lang.Object;@c568f91, claimSize={default=1G, min=1G, max=1G, step=1G, supportedUnits=[Ljava.lang.Object;@5fd43e58}, accessMode={default={readOnlyMany=false, readWriteMany=false, readWriteOnce=true}, supportedValues={readOnlyMany=true, readWriteMany=true, readWriteOnce=true}, required=true}, volumeMode={default=Filesystem, supportedValues={block=true, filesystem=true}, required=true}}
        )
        
        tenant_id = 42
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.update_storage_class_configuration_by_id(
            id=id,
            storage_class_configuration_update_request=storage_class_configuration_update_request,
            tenant_id=tenant_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_storage_class_configuration_by_id: {e}")

