"""
Examples for using the WorkloadTemplatesApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import WorkloadTemplatesApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = WorkloadTemplatesApi(api_client)


def example_count_templates():
    """
    Example of using count_templates

    Count templates. [Experimental]
    Get the total number of templates.
    """
    try:
        # Prepare the request parameters

        filter_by = ["example_item_1", "example_item_2"]

        search = "example_search"

        # Make the API call
        api_response = api_instance.count_templates(
            filter_by=filter_by,
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling count_templates: {e}")


def example_create_distributed_template():
    """
    Example of using create_distributed_template

    Create a new distributed training template. [Experimental]
    Create a new distributed training template.
    """
    try:
        # Prepare the request parameters

        # Create example data for DistributedTemplateCreationRequest
        distributed_template_creation_request = (
            models.DistributedTemplateCreationRequest()
        )

        # Make the API call
        api_response = api_instance.create_distributed_template(
            distributed_template_creation_request=distributed_template_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_distributed_template: {e}")


def example_create_training_template():
    """
    Example of using create_training_template

    Create a new training template. [Experimental]
    Create a new training template.
    """
    try:
        # Prepare the request parameters

        # Create example data for TrainingTemplateCreationRequest
        training_template_creation_request = models.TrainingTemplateCreationRequest()

        # Make the API call
        api_response = api_instance.create_training_template(
            training_template_creation_request=training_template_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_training_template: {e}")


def example_create_workspace_template():
    """
    Example of using create_workspace_template

    Create a new workspace template. [Experimental]
    Create a new workspace template.
    """
    try:
        # Prepare the request parameters

        # Create example data for WorkspaceTemplateCreationRequest
        workspace_template_creation_request = models.WorkspaceTemplateCreationRequest()

        # Make the API call
        api_response = api_instance.create_workspace_template(
            workspace_template_creation_request=workspace_template_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_workspace_template: {e}")


def example_delete_distributed_template():
    """
    Example of using delete_distributed_template

    Delete a distributed training template by ID. [Experimental]
    Delete a distributed training template by ID.
    """
    try:
        # Prepare the request parameters
        template_id = "example_template_id"

        # Make the API call
        api_instance.delete_distributed_template(
            template_id=template_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_distributed_template: {e}")


def example_delete_training_template():
    """
    Example of using delete_training_template

    Delete a training template by ID. [Experimental]
    Delete a training template by ID.
    """
    try:
        # Prepare the request parameters
        template_id = "example_template_id"

        # Make the API call
        api_instance.delete_training_template(
            template_id=template_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_training_template: {e}")


def example_delete_workspace_template():
    """
    Example of using delete_workspace_template

    Delete a workspace template by ID. [Experimental]
    Delete a workspace template by ID.
    """
    try:
        # Prepare the request parameters
        template_id = "example_template_id"

        # Make the API call
        api_instance.delete_workspace_template(
            template_id=template_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_workspace_template: {e}")


def example_get_distributed_template():
    """
    Example of using get_distributed_template

    Get a specific distributed training template by ID. [Experimental]
    Get a specific distributed training template by ID.
    """
    try:
        # Prepare the request parameters
        template_id = "example_template_id"

        # Make the API call
        api_response = api_instance.get_distributed_template(
            template_id=template_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_distributed_template: {e}")


def example_get_template_by_id1():
    """
    Example of using get_template_by_id1

    Get a template, any type. [Experimental]
    Retrieve the details of a template using its id.
    """
    try:
        # Prepare the request parameters
        template_id = "example_template_id"

        # Make the API call
        api_response = api_instance.get_template_by_id1(
            template_id=template_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_template_by_id1: {e}")


def example_get_training_template():
    """
    Example of using get_training_template

    Retrieve a specific training template by ID. [Experimental]
    Retrieve a specific training template by ID.
    """
    try:
        # Prepare the request parameters
        template_id = "example_template_id"

        # Make the API call
        api_response = api_instance.get_training_template(
            template_id=template_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_training_template: {e}")


def example_get_workspace_template():
    """
    Example of using get_workspace_template

    Retrieve a specific workspace template by ID. [Experimental]
    Retrieve a specific workspace template by ID.
    """
    try:
        # Prepare the request parameters
        template_id = "example_template_id"

        # Make the API call
        api_response = api_instance.get_workspace_template(
            template_id=template_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_workspace_template: {e}")


def example_list_distributed_templates():
    """
    Example of using list_distributed_templates

    List all distributed training templates. [Experimental]
    List all distributed training templates.
    """
    try:
        # Prepare the request parameters

        offset = 42

        limit = 42

        sort_order = "example_sort_order"

        sort_by = "example_sort_by"

        filter_by = ["example_item_1", "example_item_2"]

        search = "example_search"

        # Make the API call
        api_response = api_instance.list_distributed_templates(
            offset=offset,
            limit=limit,
            sort_order=sort_order,
            sort_by=sort_by,
            filter_by=filter_by,
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_distributed_templates: {e}")


def example_list_templates1():
    """
    Example of using list_templates1

    List templates. [Experimental]
    Retrieve all available templates.
    """
    try:
        # Prepare the request parameters

        offset = 42

        limit = 42

        sort_order = "example_sort_order"

        sort_by = "example_sort_by"

        filter_by = ["example_item_1", "example_item_2"]

        search = "example_search"

        # Make the API call
        api_response = api_instance.list_templates1(
            offset=offset,
            limit=limit,
            sort_order=sort_order,
            sort_by=sort_by,
            filter_by=filter_by,
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_templates1: {e}")


def example_list_training_templates():
    """
    Example of using list_training_templates

    List all training templates. [Experimental]
    List all training templates.
    """
    try:
        # Prepare the request parameters

        offset = 42

        limit = 42

        sort_order = "example_sort_order"

        sort_by = "example_sort_by"

        filter_by = ["example_item_1", "example_item_2"]

        search = "example_search"

        # Make the API call
        api_response = api_instance.list_training_templates(
            offset=offset,
            limit=limit,
            sort_order=sort_order,
            sort_by=sort_by,
            filter_by=filter_by,
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_training_templates: {e}")


def example_list_workspace_templates():
    """
    Example of using list_workspace_templates

    List all workspace templates. [Experimental]
    List all workspace templates.
    """
    try:
        # Prepare the request parameters

        offset = 42

        limit = 42

        sort_order = "example_sort_order"

        sort_by = "example_sort_by"

        filter_by = ["example_item_1", "example_item_2"]

        search = "example_search"

        # Make the API call
        api_response = api_instance.list_workspace_templates(
            offset=offset,
            limit=limit,
            sort_order=sort_order,
            sort_by=sort_by,
            filter_by=filter_by,
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_workspace_templates: {e}")


def example_patch_distributed_template():
    """
    Example of using patch_distributed_template

    Patch a distributed training template by ID. [Experimental]
    Patch a distributed training template by ID.
    """
    try:
        # Prepare the request parameters
        template_id = "example_template_id"

        # Create example data for DistributedTemplatePatchRequest
        distributed_template_patch_request = models.DistributedTemplatePatchRequest()

        # Make the API call
        api_response = api_instance.patch_distributed_template(
            template_id=template_id,
            distributed_template_patch_request=distributed_template_patch_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling patch_distributed_template: {e}")


def example_patch_training_template():
    """
    Example of using patch_training_template

    Patch a training template by ID. [Experimental]
    Patch a training template by ID.
    """
    try:
        # Prepare the request parameters
        template_id = "example_template_id"

        # Create example data for TrainingTemplatePatchRequest
        training_template_patch_request = models.TrainingTemplatePatchRequest()

        # Make the API call
        api_response = api_instance.patch_training_template(
            template_id=template_id,
            training_template_patch_request=training_template_patch_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling patch_training_template: {e}")


def example_patch_workspace_template():
    """
    Example of using patch_workspace_template

    Patch a workspace template by ID. [Experimental]
    Patch a workspace template by ID.
    """
    try:
        # Prepare the request parameters
        template_id = "example_template_id"

        # Create example data for WorkspaceTemplatePatchRequest
        workspace_template_patch_request = models.WorkspaceTemplatePatchRequest()

        # Make the API call
        api_response = api_instance.patch_workspace_template(
            template_id=template_id,
            workspace_template_patch_request=workspace_template_patch_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling patch_workspace_template: {e}")


def example_update_distributed_template():
    """
    Example of using update_distributed_template

    Update a distributed training template by ID. [Experimental]
    Update a distributed training template by ID.
    """
    try:
        # Prepare the request parameters
        template_id = "example_template_id"

        # Create example data for DistributedTemplateUpdateRequest
        distributed_template_update_request = models.DistributedTemplateUpdateRequest()

        # Make the API call
        api_response = api_instance.update_distributed_template(
            template_id=template_id,
            distributed_template_update_request=distributed_template_update_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_distributed_template: {e}")


def example_update_training_template():
    """
    Example of using update_training_template

    Update a training template by ID. [Experimental]
    Update a training template by ID.
    """
    try:
        # Prepare the request parameters
        template_id = "example_template_id"

        # Create example data for TrainingTemplateUpdateRequest
        training_template_update_request = models.TrainingTemplateUpdateRequest()

        # Make the API call
        api_response = api_instance.update_training_template(
            template_id=template_id,
            training_template_update_request=training_template_update_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_training_template: {e}")


def example_update_workspace_template():
    """
    Example of using update_workspace_template

    Update a workspace template by ID. [Experimental]
    Update a workspace template by ID.
    """
    try:
        # Prepare the request parameters
        template_id = "example_template_id"

        # Create example data for WorkspaceTemplateUpdateRequest
        workspace_template_update_request = models.WorkspaceTemplateUpdateRequest()

        # Make the API call
        api_response = api_instance.update_workspace_template(
            template_id=template_id,
            workspace_template_update_request=workspace_template_update_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_workspace_template: {e}")
