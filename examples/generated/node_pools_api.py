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

def example_count_nodepools():
    """
    Example of using count_nodepools
    
    Count nodepools
    Count nodepools
    """
    try:
        # Prepare the request parameters
        
        
        
        filter_by = ["example_item_1", "example_item_2"]
        
        
        
        

        # Make the API call
        api_response = api_instance.count_nodepools(
            filter_by=filter_by,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling count_nodepools: {e}")

def example_create_nodepool():
    """
    Example of using create_nodepool
    
    Create nodepool
    Create nodepool
    """
    try:
        # Prepare the request parameters
        
        # Create example data for NodepoolCreateFields
        nodepool_create_fields = models.NodepoolCreateFields(
            name = 'v100',
            label_key = '0',
            label_value = 'uUUGjjNSwg0_bs9ZayIMrKdgNvb6gvxmP00',
            cluster_id = 'd73a738f-fab3-430a-8fa3-5241493d7128',
            gpu_network_acceleration_label_key = '',
            gpu_network_acceleration_detection = 'Auto',
            gpu_resource_optimization = {reservedGpuMemoryForSwapOperations=10G, nodeLevelSchedulerEnabled=true, cpuSwapMemorySize=10000M, swapEnabled=true},
            scheduling_configuration = {numaAwareScheduling=true, placementStrategy={cpu=spread, gpu=spread}, minGuaranteedRuntime=5d8h40m, timeBasedFairShare={historicalUsageWeight=1.5, windowDuration=2d, decayHalfLife=24h, tumblingWindowStartTime=2025-01-06T08:00Z, enabled=true, windowType=tumbling}, gpuPodsPlacementStrategy={node=, device=}, cpuPodsPlacementStrategy={node=}},
            network_topology_id = '123e4567-e89b-12d3-a456-426614174000'
        )

        # Make the API call
        api_response = api_instance.create_nodepool(
            nodepool_create_fields=nodepool_create_fields,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling create_nodepool: {e}")

def example_delete_nodepool():
    """
    Example of using delete_nodepool
    
    Delete nodepool
    Delete nodepool
    """
    try:
        # Prepare the request parameters
        nodepool_id = "example_nodepool_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.delete_nodepool(
            nodepool_id=nodepool_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling delete_nodepool: {e}")

def example_get_nodepool():
    """
    Example of using get_nodepool
    
    Get nodepool
    Get nodepool
    """
    try:
        # Prepare the request parameters
        nodepool_id = "example_nodepool_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_nodepool(
            nodepool_id=nodepool_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_nodepool: {e}")

def example_get_nodepool_metrics():
    """
    Example of using get_nodepool_metrics
    
    Get the node pool metrics data.
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

def example_get_nodepool_minimal():
    """
    Example of using get_nodepool_minimal
    
    Get nodepool minimal data by ID
    Retrieve essential data for a specific node pool by ID required for common operations (e.g., workload submission)
    """
    try:
        # Prepare the request parameters
        nodepool_id = "example_nodepool_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_nodepool_minimal(
            nodepool_id=nodepool_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_nodepool_minimal: {e}")

def example_get_nodepools():
    """
    Example of using get_nodepools
    
    Get nodepools
    Get nodepools
    """
    try:
        # Prepare the request parameters
        
        
        
        filter_by = ["example_item_1", "example_item_2"]
        
        
        
        
        
        
        
        
        
        
        
        
        sort_order = "example_sort_order"
        
        
        
        
        
        
        
        
        offset = 42
        
        
        
        
        
        
        
        limit = 42
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_nodepools(
            filter_by=filter_by,
            sort_by=sort_by,
            sort_order=sort_order,
            offset=offset,
            limit=limit,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_nodepools: {e}")

def example_get_nodepools_minimal():
    """
    Example of using get_nodepools_minimal
    
    Get nodepools minimal
    Retrieve essential node pool data required for common operations (e.g., workload submission)
    """
    try:
        # Prepare the request parameters
        
        
        
        filter_by = ["example_item_1", "example_item_2"]
        
        
        
        
        
        
        
        
        
        
        
        
        sort_order = "example_sort_order"
        
        
        
        
        
        
        
        
        offset = 42
        
        
        
        
        
        
        
        limit = 42
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.get_nodepools_minimal(
            filter_by=filter_by,
            sort_by=sort_by,
            sort_order=sort_order,
            offset=offset,
            limit=limit,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling get_nodepools_minimal: {e}")

def example_legacy_create_nodepool():
    """
    Example of using legacy_create_nodepool
    
    Create a Node Pool.
    Use to create a node pool in a cluster by Universally Unique Identifier (UUID). Deprecated, please use /api/v1/node-pools instead.
    """
    try:
        # Prepare the request parameters
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        
        
        # Create example data for LegacyNodePoolCreateRequest
        legacy_node_pool_create_request = models.LegacyNodePoolCreateRequest(
            name = 'node-pool-a',
            over_provisioning_ratio = 1,
            label_key = 'node-type',
            label_value = 'type-x',
            placement_strategy = runai.models.legacy_placement_strategy.LegacyPlacementStrategy(
                    cpu = 'spread', 
                    gpu = 'spread', )
        )

        # Make the API call
        api_instance.legacy_create_nodepool(
            cluster_id=cluster_id,
            legacy_node_pool_create_request=legacy_node_pool_create_request,
        )

    except Exception as e:
        print(f"Exception when calling legacy_create_nodepool: {e}")

def example_legacy_delete_nodepool():
    """
    Example of using legacy_delete_nodepool
    
    Delete a Node Pool by id.
    Use to delete a node pool by Universally Unique Identifier (UUID). Deprecated, please use /api/v1/node-pools/{id} instead.
    """
    try:
        # Prepare the request parameters
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        
        nodepool_id = "example_nodepool_id"
        
        
        
        
        
        
        

        # Make the API call
        api_instance.legacy_delete_nodepool(
            cluster_id=cluster_id,
            nodepool_id=nodepool_id,
        )

    except Exception as e:
        print(f"Exception when calling legacy_delete_nodepool: {e}")

def example_legacy_get_nodepools():
    """
    Example of using legacy_get_nodepools
    
    Get the cluster&#39;s Node Pools.
    Retrieve all the node pools with details from the cluster by Universally Unique Identifier (UUID). Deprecated, please use /api/v1/node-pools instead.
    """
    try:
        # Prepare the request parameters
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        

        # Make the API call
        api_response = api_instance.legacy_get_nodepools(
            cluster_id=cluster_id,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling legacy_get_nodepools: {e}")

def example_legacy_update_nodepool():
    """
    Example of using legacy_update_nodepool
    
    Update a Node Pool.
    Use to update the details of a node pool by Universally Unique Identifier (UUID). Deprecated, please use PATCH /api/v1/node-pools/{id} instead.
    """
    try:
        # Prepare the request parameters
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        
        nodepool_id = "example_nodepool_id"
        
        
        
        
        
        
        
        
        # Create example data for LegacyUpdateNodePoolRequest
        legacy_update_node_pool_request = models.LegacyUpdateNodePoolRequest(
            label_key = 'node-type',
            label_value = 'type-x',
            over_provisioning_ratio = 1,
            placement_strategy = runai.models.legacy_placement_strategy.LegacyPlacementStrategy(
                    cpu = 'spread', 
                    gpu = 'spread', )
        )

        # Make the API call
        api_instance.legacy_update_nodepool(
            cluster_id=cluster_id,
            nodepool_id=nodepool_id,
            legacy_update_node_pool_request=legacy_update_node_pool_request,
        )

    except Exception as e:
        print(f"Exception when calling legacy_update_nodepool: {e}")

def example_legacy_update_nodepool_labels():
    """
    Example of using legacy_update_nodepool_labels
    
    Update labels of a Node Pool.
    Use to update the labels of a node pool. Deprecated, please use PATCH /api/v1/node-pools/{id} instead.
    """
    try:
        # Prepare the request parameters
        cluster_id = "example_cluster_id"
        
        
        
        
        
        
        
        nodepool_id = "example_nodepool_id"
        
        
        
        
        
        
        
        
        # Create example data for LegacyNodePoolLabelsRequest
        legacy_node_pool_labels_request = models.LegacyNodePoolLabelsRequest(
            label_key = 'node-type',
            label_value = 'type-x'
        )

        # Make the API call
        api_instance.legacy_update_nodepool_labels(
            cluster_id=cluster_id,
            nodepool_id=nodepool_id,
            legacy_node_pool_labels_request=legacy_node_pool_labels_request,
        )

    except Exception as e:
        print(f"Exception when calling legacy_update_nodepool_labels: {e}")

def example_patch_nodepool():
    """
    Example of using patch_nodepool
    
    Patch nodepool fields
    Update only specific fields of a nodepool
    """
    try:
        # Prepare the request parameters
        nodepool_id = "example_nodepool_id"
        
        
        
        
        
        
        
        
        # Create example data for NodepoolUpdateFields
        nodepool_update_fields = models.NodepoolUpdateFields(
            label_key = '0',
            label_value = 'uUUGjjNSwg0_bs9ZayIMrKdgNvb6gvxmP00',
            gpu_network_acceleration_label_key = '',
            gpu_network_acceleration_detection = 'Auto',
            gpu_resource_optimization = {reservedGpuMemoryForSwapOperations=10G, nodeLevelSchedulerEnabled=true, cpuSwapMemorySize=10000M, swapEnabled=true},
            scheduling_configuration = {numaAwareScheduling=true, placementStrategy={cpu=spread, gpu=spread}, minGuaranteedRuntime=5d8h40m, timeBasedFairShare={historicalUsageWeight=1.5, windowDuration=2d, decayHalfLife=24h, tumblingWindowStartTime=2025-01-06T08:00Z, enabled=true, windowType=tumbling}, gpuPodsPlacementStrategy={node=, device=}, cpuPodsPlacementStrategy={node=}},
            network_topology_id = '123e4567-e89b-12d3-a456-426614174000'
        )

        # Make the API call
        api_response = api_instance.patch_nodepool(
            nodepool_id=nodepool_id,
            nodepool_update_fields=nodepool_update_fields,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling patch_nodepool: {e}")

def example_update_nodepool():
    """
    Example of using update_nodepool
    
    Update nodepool
    Update nodepool
    """
    try:
        # Prepare the request parameters
        nodepool_id = "example_nodepool_id"
        
        
        
        
        
        
        
        
        # Create example data for NodepoolUpdateFields
        nodepool_update_fields = models.NodepoolUpdateFields(
            label_key = '0',
            label_value = 'uUUGjjNSwg0_bs9ZayIMrKdgNvb6gvxmP00',
            gpu_network_acceleration_label_key = '',
            gpu_network_acceleration_detection = 'Auto',
            gpu_resource_optimization = {reservedGpuMemoryForSwapOperations=10G, nodeLevelSchedulerEnabled=true, cpuSwapMemorySize=10000M, swapEnabled=true},
            scheduling_configuration = {numaAwareScheduling=true, placementStrategy={cpu=spread, gpu=spread}, minGuaranteedRuntime=5d8h40m, timeBasedFairShare={historicalUsageWeight=1.5, windowDuration=2d, decayHalfLife=24h, tumblingWindowStartTime=2025-01-06T08:00Z, enabled=true, windowType=tumbling}, gpuPodsPlacementStrategy={node=, device=}, cpuPodsPlacementStrategy={node=}},
            network_topology_id = '123e4567-e89b-12d3-a456-426614174000'
        )

        # Make the API call
        api_response = api_instance.update_nodepool(
            nodepool_id=nodepool_id,
            nodepool_update_fields=nodepool_update_fields,
        )
        print(f"API response: {api_response}")

    except Exception as e:
        print(f"Exception when calling update_nodepool: {e}")

