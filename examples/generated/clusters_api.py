"""
Examples for using the ClustersApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import ClustersApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = ClustersApi(api_client)


def example_create_cluster():
    """
    Example of using create_cluster

    Create a cluster.
    Use to create a Kubernetes cluster.
    """
    try:
        # Prepare the request parameters

        # Create example data for ClusterCreationRequest
        cluster_creation_request = models.ClusterCreationRequest(
            name="", domain="", version=""
        )

        # Make the API call
        api_response = api_instance.create_cluster(
            cluster_creation_request=cluster_creation_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_cluster: {e}")


def example_delete_cluster():
    """
    Example of using delete_cluster

    Delete a cluster by id.
    Use to delete a cluster by Universally Unique Identifier (UUID).  Will return 202 for success if this api was called on a cluster that its version is &gt;&#x3D;2.20,  and force query param is false or not provided. Will return 204 for success if force query param is true, or if cluster is in a version &lt; 2.20
    """
    try:
        # Prepare the request parameters
        cluster_uuid = "example_cluster_uuid"

        force = True

        # Make the API call
        api_response = api_instance.delete_cluster(
            cluster_uuid=cluster_uuid,
            force=force,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling delete_cluster: {e}")


def example_get_cluster_by_uuid():
    """
    Example of using get_cluster_by_uuid

    Get cluster by id.
    Retrieve cluster details by Universally Unique Identifier (UUID).
    """
    try:
        # Prepare the request parameters
        cluster_uuid = "example_cluster_uuid"

        verbosity = "example_verbosity"

        # Make the API call
        api_response = api_instance.get_cluster_by_uuid(
            cluster_uuid=cluster_uuid,
            verbosity=verbosity,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_cluster_by_uuid: {e}")


def example_get_cluster_install_info_by_uuid():
    """
    Example of using get_cluster_install_info_by_uuid

    Retrieve the installation instructions of a cluster by ID.
    Use to retrieve installation instruction for a cluster by Universally Unique Identifier (UUID).  Supports clusters version 2.15 or above.
    """
    try:
        # Prepare the request parameters
        cluster_uuid = "example_cluster_uuid"

        version = "example_version"

        remote_cluster_url = "example_remote_cluster_url"

        # Make the API call
        api_response = api_instance.get_cluster_install_info_by_uuid(
            cluster_uuid=cluster_uuid,
            version=version,
            remote_cluster_url=remote_cluster_url,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_cluster_install_info_by_uuid: {e}")


def example_get_cluster_metrics():
    """
    Example of using get_cluster_metrics

    Get the cluster metrics data.
    Retrieve the metrics data for a Kubernetes cluster by Universally Unique Identifier (UUID).
    """
    try:
        # Prepare the request parameters
        cluster_uuid = "example_cluster_uuid"

        start = "2024-12-29T12:00:00Z"

        end = "2024-12-29T12:00:00Z"

        metric_type = ["example_item_1", "example_item_2"]

        number_of_samples = 42

        group_by = "example_group_by"

        nodepool_name = "example_nodepool_name"

        # Make the API call
        api_response = api_instance.get_cluster_metrics(
            cluster_uuid=cluster_uuid,
            start=start,
            end=end,
            metric_type=metric_type,
            number_of_samples=number_of_samples,
            group_by=group_by,
            nodepool_name=nodepool_name,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_cluster_metrics: {e}")


def example_get_cluster_minimal_data_by_id():
    """
    Example of using get_cluster_minimal_data_by_id

    Get cluster minimal data by id
    Retrieve essential data for a specific cluster by ID required for common operations (e.g., workload submission)
    """
    try:
        # Prepare the request parameters
        cluster_uuid = "example_cluster_uuid"

        # Make the API call
        api_response = api_instance.get_cluster_minimal_data_by_id(
            cluster_uuid=cluster_uuid,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_cluster_minimal_data_by_id: {e}")


def example_get_clusters():
    """
    Example of using get_clusters

    Get a list of clusters.
    Retrieve a list of clusters with details.
    """
    try:
        # Prepare the request parameters
        verbosity = "example_verbosity"

        include_requested_for_delete = True

        # Make the API call
        api_response = api_instance.get_clusters(
            verbosity=verbosity,
            include_requested_for_delete=include_requested_for_delete,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_clusters: {e}")


def example_get_clusters_minimal_data():
    """
    Example of using get_clusters_minimal_data

    Get clusters minimal data
    Retrieve essential cluster data required for common operations (e.g., workload submission)
    """
    try:
        # Prepare the request parameters

        filter_by = ["example_item_1", "example_item_2"]

        offset = 42

        limit = 42

        # Make the API call
        api_response = api_instance.get_clusters_minimal_data(
            filter_by=filter_by,
            offset=offset,
            limit=limit,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_clusters_minimal_data: {e}")


def example_update_cluster():
    """
    Example of using update_cluster

    Update a cluster by id.
    Use to update the details of a Kubernetes cluster by Universally Unique Identifier (UUID).
    """
    try:
        # Prepare the request parameters
        cluster_uuid = "example_cluster_uuid"

        # Create example data for ClusterUpdateRequest
        cluster_update_request = models.ClusterUpdateRequest(name="")

        # Make the API call
        api_instance.update_cluster(
            cluster_uuid=cluster_uuid,
            cluster_update_request=cluster_update_request,
        )

    except Exception as e:
        print(f"Exception when calling update_cluster: {e}")
