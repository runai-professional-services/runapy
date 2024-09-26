from runai.client import RunaiClient

client = RunaiClient(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    runai_base_url=BASE_URL,
    cluster_id=CLUSTER_ID
)  

# Get all departments
print(client.departments.all())

default_node_pool = "default"
nodepool = client.node_pools.get_by_name(nodepool_name=default_node_pool)

# Create a department
department = client.departments.create(
    name="new-department",
    resources=[{
        "nodePool": {
            "id": str(nodepool["id"]),
            "name": default_node_pool,
        },
        "gpu": {
            "deserved": 0,
            "limit": 0,
            "overQuotaWeight": 2
        },
        "cpu": None,
        "memory": None
    }])
print(department)

# Get department by id
department_id = department["id"]
client.departments.get(department_id)

# Delete department
client.departments.delete(department_id)

# Update department
department = client.departments.update_resources(
    department_id=4500007,
    resources=[
        {
            "nodePool": {
                "id": "2917",
                "name": "default"
            },
            "gpu": {
                "deserved": 6,
                "limit": 6,
                "overQuotaWeight": 2
            },
            "cpu": None,
            "memory": None,
        }
    ]
)

# Create department with unlimited cpu and memory resources on the default nodepool

default_node_pool = "default"
nodepool = client.node_pools.get_by_name(nodepool_name=default_node_pool)

client.departments.create(
    name="department-with-unlimited-cpu-and-memory",
    resources=[{
        "nodePool": {
            "id": str(nodepool["id"]),
            "name": default_node_pool
        },
        "gpu": {
            "deserved": 1,
            "limit": 5,
        },
        "cpu": {
            "deserved": None,
            "limit": -1,
        },
        "memory": {
            "deserved": None,
            "limit": -1,
            "units": "Mib",
        }
    }]
)