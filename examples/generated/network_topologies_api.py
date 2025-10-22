"""
Examples for using the NetworkTopologiesApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import NetworkTopologiesApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = NetworkTopologiesApi(api_client)


def example_create_network_topology():
    """
    Example of using create_network_topology

    Create network topologies
    Creates a network topology object based on the provided specification.
    """
    try:
        # Prepare the request parameters

        # Create example data for NetworkTopologyCreateRequest
        network_topology_create_request = models.NetworkTopologyCreateRequest()

        # Make the API call
        api_response = api_instance.create_network_topology(
            network_topology_create_request=network_topology_create_request,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_network_topology: {e}")


def example_delete_network_topology():
    """
    Example of using delete_network_topology

    Delete network topology by ID.
    Delete an existing network topology by its ID.
    """
    try:
        # Prepare the request parameters
        network_topology_id = "example_network_topology_id"

        # Make the API call
        api_instance.delete_network_topology(
            network_topology_id=network_topology_id,
        )

    except Exception as e:
        print(f"Exception when calling delete_network_topology: {e}")


def example_get_network_topologies():
    """
    Example of using get_network_topologies

    Get network topologies.
    Retrieve a list of network topologies with details.
    """
    try:
        # Prepare the request parameters

        filter_by = ["example_item_1", "example_item_2"]

        # Make the API call
        api_response = api_instance.get_network_topologies(
            filter_by=filter_by,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_network_topologies: {e}")


def example_get_network_topologies_count():
    """
    Example of using get_network_topologies_count

    Count the amount of network topologies in a tenant.
    Retrieve the count of network topologies in a tenant group by selected attributes
    """
    try:
        # Prepare the request parameters

        filter_by = ["example_item_1", "example_item_2"]

        # Make the API call
        api_response = api_instance.get_network_topologies_count(
            filter_by=filter_by,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_network_topologies_count: {e}")


def example_get_network_topology_by_id():
    """
    Example of using get_network_topology_by_id

    Get network topology by id.
    Retrieve network topology details by Universally Unique Identifier (UUID).
    """
    try:
        # Prepare the request parameters
        network_topology_id = "example_network_topology_id"

        # Make the API call
        api_response = api_instance.get_network_topology_by_id(
            network_topology_id=network_topology_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_network_topology_by_id: {e}")
