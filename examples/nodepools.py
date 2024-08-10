from runai.client import RunaiClient

client = RunaiClient(
    realm=REALM,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    runai_base_url=BASE_URL,
    cluster_id=CLUSTER_ID
)    

# Get all nodepools
print(client.node_pools.all())

# Create nodepool
print(client.node_pools.create(
    name="test3",
    label_key="newTestLabel",
    label_value="someValue",
    placement_strategy={"cpu": "spread", "gpu": "spread"}
    ))

# Get single nodepool by name
node_pool = client.node_pools.get_by_name(nodepool_name="test3")
print(node_pool)

# Update nodepool labels
print(client.node_pools.update_labels(nodepool_id=node_pool["id"], labelKey="new-type", labelValue="new"))

# Update nodepool labels, resources strategy or both
print(client.node_pools.update(
    nodepool_id=3028,
    labelKey="testLabelNew",
    labelValue="someValue",
    placementStrategy={
         "gpu": "spread",
         "cpu": "spread"
      },
))

# Get nodepool metrics
print(client.node_pools.node_pool_metrics(
    nodepool_name="test",
    start="2023-06-06T12:09:18.211Z",
    end="2025-06-06T12:09:18.211Z",
    metric_type="GPU_UTILIZATION"
))