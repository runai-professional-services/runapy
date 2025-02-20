"""
Examples for using the JobsApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import JobsApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = JobsApi(api_client)


def example_get_cluster_jobs_count():
    """
    Example of using get_cluster_jobs_count

    Return the number all Jobs in the cluster. Deprecated - please use api/v1/workloads/count instead

    """
    try:
        # Prepare the request parameters
        uuid = "example_uuid"

        node_id = "example_node_id"

        filter = "example_filter"

        # Make the API call
        api_response = api_instance.get_cluster_jobs_count(
            uuid=uuid,
            node_id=node_id,
            filter=filter,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_cluster_jobs_count: {e}")


def example_get_pods_by_job_id():
    """
    Example of using get_pods_by_job_id

    Get all pods that are associated for a specific job. Deprecated - please use api/v1/workloads/{workloadId}/pods instead

    """
    try:
        # Prepare the request parameters
        job_id = "example_job_id"

        uuid = "example_uuid"

        id = "example_id"

        pod_id = "example_pod_id"

        pod_group_id = "example_pod_group_id"

        node_id = "example_node_id"

        name = "example_name"

        status = "example_status"

        # Make the API call
        api_response = api_instance.get_pods_by_job_id(
            job_id=job_id,
            uuid=uuid,
            id=id,
            pod_id=pod_id,
            pod_group_id=pod_group_id,
            node_id=node_id,
            name=name,
            status=status,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_pods_by_job_id: {e}")


def example_list_jobs():
    """
    Example of using list_jobs

    List all Jobs in the cluster. Deprecated - please use api/v1/workloads instead

    """
    try:
        # Prepare the request parameters
        uuid = "example_uuid"

        node_id = "example_node_id"

        filter = "example_filter"

        sort_by = "example_sort_by"

        sort_direction = "example_sort_direction"

        include_deleted = True

        # Make the API call
        api_response = api_instance.list_jobs(
            uuid=uuid,
            node_id=node_id,
            filter=filter,
            sort_by=sort_by,
            sort_direction=sort_direction,
            var_from=var_from,
            limit=limit,
            include_deleted=include_deleted,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling list_jobs: {e}")
