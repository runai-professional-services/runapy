"""
Examples for using the NodesApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import NodesApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = NodesApi(api_client)


def example_get_node_telemetry():
    """
    Example of using get_node_telemetry

    Get node telemetry data.
    Retrieve node telemetry data for use in analysis applications.
    """
    try:
        # Prepare the request parameters

        cluster_id = "example_cluster_id"

        nodepool_name = "example_nodepool_name"

        group_by = ["example_item_1", "example_item_2"]

        # Make the API call
        api_response = api_instance.get_node_telemetry(
            telemetry_type=telemetry_type,
            cluster_id=cluster_id,
            nodepool_name=nodepool_name,
            group_by=group_by,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_node_telemetry: {e}")


def example_get_nodes():
    """
    Example of using get_nodes

    Get a list of nodes.
    Retrieve a list of nodes from the Kubernetes cluster.
    """
    try:
        # Prepare the request parameters
        cluster_uuid = "example_cluster_uuid"

        node_name = "example_node_name"

        # Make the API call
        api_response = api_instance.get_nodes(
            cluster_uuid=cluster_uuid,
            node_name=node_name,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_nodes: {e}")
