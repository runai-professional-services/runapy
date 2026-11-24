"""
Examples for using the AIApplicationsAPIApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import AIApplicationsAPIApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = AIApplicationsAPIApi(api_client)

def example_count_applications():
    """
    Example of using count_applications
    
    Count AI applications. [Experimental]
    Get the total number of AI applications.
    """
    try:
        # Prepare the request parameters
        
        
        
        filter_by = ["example_item_1", "example_item_2"]
        
        
        
        
        search = "example_search"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.count_applications(
            filter_by=filter_by,
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling count_applications: {e}")

def example_create_application1():
    """
    Example of using create_application1
    
    Create AI application.
    Create AI application.
    """
    try:
        # Prepare the request parameters
        
        # Create example data for AIApplicationCreationRequest
        ai_application_creation_request = models.AIApplicationCreationRequest(
            cluster_id = '71f69d83-ba66-4822-adf5-55ce55efd210',
            project_id = '1',
            name = 'a1c2v7s6djuy1zmetozkhdomha1bae37b8ocvx8o53ow2eg7p6qw9qklp6l4y010fogx',
            spec = {auth={assetId=046b6c7f-0b8a-43b9-b35d-6489e6daee91}, values={key=}, chartRef={chartName=redis, chartVersion=17.3.17, repo=https://charts.bitnami.com/bitnami, chartURL=https://helm.ngc.nvidia.com/nvidia/blueprint/charts/nvidia-blueprint-rag-v2.3.0.tgz}, valuesBase64=valuesBase64}
        )

        # Make the API call
        api_response = api_instance.create_application1(
            ai_application_creation_request=ai_application_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_application1: {e}")

def example_delete_application():
    """
    Example of using delete_application
    
    Delete AI application.
    Delete AI application.
    """
    try:
        # Prepare the request parameters
        ai_application_id = "example_ai_application_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.delete_application(
            ai_application_id=ai_application_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling delete_application: {e}")

def example_get_application():
    """
    Example of using get_application
    
    Get AI application. [Experimental]
    Get AI application.
    """
    try:
        # Prepare the request parameters
        ai_application_id = "example_ai_application_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_application(
            ai_application_id=ai_application_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_application: {e}")

def example_list_applications():
    """
    Example of using list_applications
    
    List AI applications. [Experimental]
    List AI applications.
    """
    try:
        # Prepare the request parameters
        
        
        
        
        
        
        
        
        
        offset = 42
        
        
        
        
        
        
        
        limit = 42
        
        
        
        
        
        
        sort_order = "example_sort_order"
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        filter_by = ["example_item_1", "example_item_2"]
        
        
        
        
        search = "example_search"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.list_applications(
            verbosity=verbosity,
            offset=offset,
            limit=limit,
            sort_order=sort_order,
            sort_by=sort_by,
            filter_by=filter_by,
            search=search,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_applications: {e}")

