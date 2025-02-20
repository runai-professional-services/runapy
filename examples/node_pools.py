# Create a node pool
from runai.configuration import Configuration
from runai.api_client import ApiClient
from runai.runai_client import RunaiClient

from runai import models

configuration = Configuration(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    runai_base_url="https://org.run.ai",
)

api_client = ApiClient(configuration)
client = RunaiClient(api_client)

# Create a node pool
response = client.organizations.node_pools.create_nodepool(
    nodepool_create_fields=models.NodepoolCreateFields(
        name="a100",
        labelKey="node-pool-type",
        labelValue="a100",
        clusterId="bf71b092-8e48-4653-8824-c88242de3ad5",
    )
)
print(response)


# Get all nodespools in the cluster 'bf71b092-8e48-4653-8824-c88242de3ad5'
response = client.organizations.node_pools.get_nodepools(
    filter_by=["clusterId==bf71b092-8e48-4653-8824-c88242de3ad5"]
).data
print(response)


# Update node pool placement Strategy

## 1. Get nodepool id by node pool name
node_pool = client.organizations.node_pools.get_nodepools(
    filter_by=["name==a100"]
).data["nodepools"][0]
node_pool_id = node_pool["id"]

## 2. Update placement strategy using update_nodepool with node_pool_id
response = client.organizations.node_pools.patch_nodepool(
    nodepool_id=node_pool_id,
    nodepool_update_fields=models.NodepoolUpdateFields(
        placementStrategy=models.NodepoolCreateFieldsPlacementStrategy(
            cpu=models.PlacementStrategy(models.PlacementStrategy.BINPACK),
            gpu=models.PlacementStrategy(models.PlacementStrategy.BINPACK),
        )
    ),
)
print(response)


# Delete nodepool
response = client.organizations.node_pools.delete_nodepool(nodepool_id=node_pool_id)
print(response)


# Get nodepool metrics
response = client.organizations.node_pools.get_nodepool_metrics(
    cluster_uuid="bf71b092-8e48-4653-8824-c88242de3ad5",
    nodepool_name="a100",
    start="2025-02-10T12:09:18.211Z",
    end="2025-02-11T12:09:18.211Z",
    metric_type=[
        models.MetricsType(models.MetricsType.GPU_UTILIZATION),
        models.MetricsType(models.MetricsType.GPU_MEMORY_UTILIZATION),
        models.MetricsType(models.MetricsType.CPU_UTILIZATION),
        models.MetricsType(models.MetricsType.CPU_MEMORY_UTILIZATION),
        models.MetricsType(models.MetricsType.AVG_WORKLOAD_WAIT_TIME),
        models.MetricsType(models.MetricsType.ALLOCATED_GPU),
        models.MetricsType(models.MetricsType.GPU_QUOTA),
        models.MetricsType(models.MetricsType.TOTAL_GPU_NODES),
    ],
)
print(response)
