"""
Examples for using the NodePoolsApi
"""

from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.api import NodePoolsApi
from runai import models

# Configure API key authorization
configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
api_instance = NodePoolsApi(api_client)

def example_create_node_pool():
    """
    Example of using create_node_pool
    
    Create a Node Pool.
    Use to create a node pool in a cluster by Universally Unique Identifier (UUID).
    """
    try:
        # Prepare the request parameters
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        
        
        # Create example data for NodePoolCreateRequest
        node_pool_create_request = models.NodePoolCreateRequest(
            name = 'node-pool-a',
            over_provisioning_ratio = 1,
            label_key = 'node-type',
            label_value = 'type-x',
            placement_strategy = {cpu=spread, gpu=binpack}
        )

        # Make the API call
        api_instance.create_node_pool(
            cluster_id=cluster_id,
            node_pool_create_request=node_pool_create_request,
        )

    except Exception as e:
        print(f"Exception when calling create_node_pool: {e}")

def example_delete_node_pool():
    """
    Example of using delete_node_pool
    
    Delete a Node Pool by id.§
    Use to delete a node pool by Universally Unique Identifier (UUID).
    """
    try:
        # Prepare the request parameters
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        
        
        id = 42
        
        
        
        
        
        

        # Make the API call
        api_instance.delete_node_pool(
            cluster_id=cluster_id,
            id=id,
        )

    except Exception as e:
        print(f"Exception when calling delete_node_pool: {e}")

def example_get_node_pools():
    """
    Example of using get_node_pools
    
    Get the cluster&#39;s Node Pools.
    Retrieve all the node pools with details from the cluster by Universally Unique Identifier (UUID).
    """
    try:
        # Prepare the request parameters
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_node_pools(
            cluster_id=cluster_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_node_pools: {e}")

def example_get_nodepool_metrics():
    """
    Example of using get_nodepool_metrics
    
    Get the node pool metrics data. [Experimental]
    Retrieve the node pool metrics data by Universally Unique Identifier (UUID).
    """
    try:
        # Prepare the request parameters
        cluster_uuid = "example_cluster_uuid"
        
        
        
        
        
        
        
        nodepool_name = "example_nodepool_name"
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        start = "2024-12-29T12:00:00Z"
        
        
        
        
        
        
        
        end = "2024-12-29T12:00:00Z"
        
        
        
        metric_type = ["example_item_1", "example_item_2"]
        
        
        
        
        
        number_of_samples = 42
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_nodepool_metrics(
            cluster_uuid=cluster_uuid,
            nodepool_name=nodepool_name,
            start=start,
            end=end,
            metric_type=metric_type,
            number_of_samples=number_of_samples,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_nodepool_metrics: {e}")

def example_update_node_pool():
    """
    Example of using update_node_pool
    
    Update a Node Pool.
    Use to update the details of a node pool by Universally Unique Identifier (UUID).
    """
    try:
        # Prepare the request parameters
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        
        
        id = 42
        
        
        
        
        
        
        
        # Create example data for UpdateNodePoolRequest
        update_node_pool_request = models.UpdateNodePoolRequest(
            label_key = 'node-type',
            label_value = 'type-x',
            over_provisioning_ratio = 1,
            placement_strategy = {cpu=spread, gpu=binpack}
        )

        # Make the API call
        api_instance.update_node_pool(
            cluster_id=cluster_id,
            id=id,
            update_node_pool_request=update_node_pool_request,
        )

    except Exception as e:
        print(f"Exception when calling update_node_pool: {e}")

def example_update_node_pool_labels():
    """
    Example of using update_node_pool_labels
    
    Update labels of a Node Pool.
    Use to update the labels of a node pool.
    """
    try:
        # Prepare the request parameters
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        
        
        id = 42
        
        
        
        
        
        
        
        # Create example data for NodePoolLabelsRequest
        node_pool_labels_request = models.NodePoolLabelsRequest(
            label_key = 'node-type',
            label_value = 'type-x'
        )

        # Make the API call
        api_instance.update_node_pool_labels(
            cluster_id=cluster_id,
            id=id,
            node_pool_labels_request=node_pool_labels_request,
        )

    except Exception as e:
        print(f"Exception when calling update_node_pool_labels: {e}")

