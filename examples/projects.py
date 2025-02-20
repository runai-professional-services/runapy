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

# Get all projects in the cluster 'b5ac1569-90f9-4e31-9d17-a484dd036251'
response = client.organizations.projects.get_projects(
    filter_by=["clusterId==b5ac1569-90f9-4e31-9d17-a484dd036251"]
).data
print(response)

# Create a department
response = client.organizations.departments.create_department(
    department_creation_request=models.DepartmentCreationRequest(
        name="department-c",
        resources=[
            models.Resources(
                node_pool=models.ResourcesNodePool(id="100580", name="default"),
                gpu=models.ResourcesGpu(deserved=10, limit=-1, over_quota_weight=2),
            )
        ],
        cluster_id="b5ac1569-90f9-4e31-9d17-a484dd036251",
    )
)
print(response)

# Create a project
response = client.organizations.projects.create_project(
    project_creation_request=models.ProjectCreationRequest(
        name="project-c",
        resources=[
            models.Resources(
                node_pool=models.ResourcesNodePool(id="100580", name="default"),
                gpu=models.ResourcesGpu(deserved=3, limit=-1, over_quota_weight=2),
            )
        ],
        cluster_id="b5ac1569-90f9-4e31-9d17-a484dd036251",
    )
)
print(response)

# Update department resources
response = client.organizations.departments.update_department_resources(
    department_id="4519668",
    resources=[
        models.Resources(
            node_pool=models.ResourcesNodePool(id="100580", name="default"),
            gpu=models.ResourcesGpu(deserved=2, limit=-1, over_quota_weight=2),
        )
    ],
)
print(response)
