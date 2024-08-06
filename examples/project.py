from runai.client import RunaiClient

client = RunaiClient(
    realm=REALM,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    runai_base_url=BASE_URL,
    cluster_id=CLUSTER_ID
)

# Get all projects
print(client.projects.all())

# Create projet with GPU resource only
print(client.projects.create(
    name="latest-project-3",
    resources=[
        {
            "nodePool": {
                "id": "3028",
                "name": "test"
            },
            "gpu": {
                "deserved": 1,
                "limit": 2,
                "overQuotaWeight": 2
            },
            }
    ]
))

# Update project GPU resources only (works same as PATCH)
client.projects.update(
    project_id=4500111,
    resources=[
        {
            "nodePool": {
                "id": "3028",
                "name": "test"
            },
            "gpu": {
                "deserved": 2,
                "limit": 3,
                "overQuotaWeight": 2
            },
            }
    ])

# Delete a project
print(client.projects.delete(4500111))
