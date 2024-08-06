from runapy import RunaiClient

client = RunaiClient(
    realm=REALM,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    runai_base_url=BASE_URL,
    cluster_id=CLUSTER_ID
)  

# Get all departments
print(client.departments.all())

# Create a department
department = (client.departments.create(
    name="new-department",
    resources=[{
        "nodePool": {
            "id": "22",
            "name": "default"
        },
        "gpu": {
            "deserved": 0,
            "limit": 0,
            "overQuotaWeight": 2
        },
        "cpu": None,
        "memory": None
    }]
))
print(department)

# Get department by id
department_id = department["id"]
print(client.departments.get(department_id))

# Delete department
print(client.departments.delete(department_id))

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
            "memory": None
        }
    ]
)