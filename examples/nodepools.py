from runapy import RunaiClient

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
node_pool = client.node_pools.get(nodepool_name="test3")
print(node_pool)

# Update nodepool
print(client.node_pools.update_labels(nodepool_id=node_pool["id"], labelKey="new-type", labelValue="new"))