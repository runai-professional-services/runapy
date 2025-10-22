"""
Examples for using the DatavolumesApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import DatavolumesApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = DatavolumesApi(api_client)


def example_count_datavolumes():
    """
    Example of using count_datavolumes

    Count data volumes.
    Retrieve the number of data volumes.
    """
    try:
        # Prepare the request parameters

        usable_in_project_id = "example_usable_in_project_id"

        filter_by = ["example_item_1", "example_item_2"]

        search = "example_search"

        # Make the API call
        api_response = api_instance.count_datavolumes(
            request_type=request_type,
            usable_in_project_id=usable_in_project_id,
            filter_by=filter_by,
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling count_datavolumes: {e}")


def example_create_datavolume():
    """
    Example of using create_datavolume

    Create a datavolume

    """
    try:
        # Prepare the request parameters

        # Create example data for DatavolumeCreationFields
        datavolume_creation_fields = models.DatavolumeCreationFields(
            name="datavolume-a",
            description="Results of experiment X",
            origin_pvc_name="pvc-a",
            project_id="5",
            should_delete_original_volume=False,
            use_original_volume=True,
        )

        # Make the API call
        api_response = api_instance.create_datavolume(
            datavolume_creation_fields=datavolume_creation_fields,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_datavolume: {e}")


def example_datavolume_name_availability():
    """
    Example of using datavolume_name_availability

    Data volumes name availability.
    Checks if a specified data volume name is available under the given scope (e.g., project or department). Returns a 204 No Content response if the name is available, or 409 Conflict if the name is already in use.
    """
    try:
        # Prepare the request parameters
        data_name = "example_data_name"

        cluster_id = "example_cluster_id"

        # Make the API call
        api_instance.datavolume_name_availability(
            data_name=data_name,
            cluster_id=cluster_id,
        )

    except Exception as e:
        print(f"Exception when calling datavolume_name_availability: {e}")


def example_delete_datavolume():
    """
    Example of using delete_datavolume

    Delete datavolume

    """
    try:
        # Prepare the request parameters
        datavolume_id = "example_datavolume_id"

        # Make the API call
        api_response = api_instance.delete_datavolume(
            datavolume_id=datavolume_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling delete_datavolume: {e}")


def example_get_datavolume():
    """
    Example of using get_datavolume

    Get datavolume

    """
    try:
        # Prepare the request parameters
        datavolume_id = "example_datavolume_id"

        # Make the API call
        api_response = api_instance.get_datavolume(
            datavolume_id=datavolume_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_datavolume: {e}")


def example_get_datavolume_shared_scopes():
    """
    Example of using get_datavolume_shared_scopes

    Get the datavolume&#39;s shared scopes

    """
    try:
        # Prepare the request parameters
        datavolume_id = "example_datavolume_id"

        # Make the API call
        api_response = api_instance.get_datavolume_shared_scopes(
            datavolume_id=datavolume_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_datavolume_shared_scopes: {e}")


def example_get_datavolumes():
    """
    Example of using get_datavolumes

    List datavolumes in permitted scopes
    Get requested datavolumes.
    """
    try:
        # Prepare the request parameters

        usable_in_project_id = "example_usable_in_project_id"

        offset = 42

        limit = 42

        sort_by = "example_sort_by"

        sort_order = "example_sort_order"

        filter_by = ["example_item_1", "example_item_2"]

        search = "example_search"

        # Make the API call
        api_response = api_instance.get_datavolumes(
            request_type=request_type,
            usable_in_project_id=usable_in_project_id,
            offset=offset,
            limit=limit,
            sort_by=sort_by,
            sort_order=sort_order,
            filter_by=filter_by,
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_datavolumes: {e}")


def example_patch_datavolume():
    """
    Example of using patch_datavolume

    Patch datavolume

    """
    try:
        # Prepare the request parameters
        datavolume_id = "example_datavolume_id"

        # Create example data for DatavolumePatchFields
        datavolume_patch_fields = models.DatavolumePatchFields(
            description="Results of experiment X"
        )

        # Make the API call
        api_response = api_instance.patch_datavolume(
            datavolume_id=datavolume_id,
            datavolume_patch_fields=datavolume_patch_fields,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling patch_datavolume: {e}")


def example_patch_datavolume_shared_scopes():
    """
    Example of using patch_datavolume_shared_scopes

    Patch the datavolume&#39;s shared scopes

    """
    try:
        # Prepare the request parameters
        datavolume_id = "example_datavolume_id"

        # Create example data for SharedScopesPatchRequest
        shared_scopes_patch_request = models.SharedScopesPatchRequest(
            add=[
                runai.models.shared_scope_base.SharedScopeBase(
                    scope_type="cluster",
                    scope_id="a418ed33-9399-48c0-a890-122cadd13bfd",
                )
            ],
            remove=[
                runai.models.shared_scope_base.SharedScopeBase(
                    scope_type="cluster",
                    scope_id="a418ed33-9399-48c0-a890-122cadd13bfd",
                )
            ],
        )

        # Make the API call
        api_response = api_instance.patch_datavolume_shared_scopes(
            datavolume_id=datavolume_id,
            shared_scopes_patch_request=shared_scopes_patch_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling patch_datavolume_shared_scopes: {e}")
