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


# Create a training workload in project 'test'
## 1. Fetch the projects id given to be used in the workload creation
response = client.organizations.projects.get_projects(filter_by=["name==test"]).data[
    "projects"
][0]
project_id = response["id"]
cluster_id = response["clusterId"]

## 2. Create 1 gpu training workload with Run:ai quickstart-demo image
response = client.workloads.trainings.create_training1(
    training_creation_request=models.TrainingCreationRequest(
        name="test",
        projectId=project_id,
        clusterId=cluster_id,
        spec=models.TrainingSpecSpec(
            image="gcr.io/run-ai-demo/quickstart-demo",
            compute=models.ComputeFields(
                gpuDevicesRequest=1,
                gpuPortionRequest=1,
                cpuCoreRequest=0.1,
                cpuMemoryRequest="100M",
                gpuRequestType="portion",
            ),
        ),
    )
)
print(response)
