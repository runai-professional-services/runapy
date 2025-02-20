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


# Create a jupyter notebook with 0.5 gpu in 'test' project
## 1. Fetch the projects id given to be used in the workload creation
response = client.organizations.projects.get_projects(filter_by=["name==test"]).data[
    "projects"
][0]
project_id = response["id"]
cluster_id = response["clusterId"]

## 2. Create 0.5 gpu workspace workload with jupyter scipy-notebook image
response = client.workloads.workspaces.create_workspace1(
    workspace_creation_request=models.WorkspaceCreationRequest(
        name="jupyter-workspace",
        projectId=project_id,
        clusterId=cluster_id,
        spec=models.WorkspaceSpecSpec(
            image="jupyter/scipy-notebook",
            command="start-notebook.sh",
            args="--NotebookApp.base_url=/${RUNAI_PROJECT}/${RUNAI_JOB_NAME} --NotebookApp.token=''",
            exposedUrls=[
                models.ExposedUrl(
                    container=8888,
                    tool_type="jupyter-notebook",
                    tool_name="Jupyter",
                    name="Jupyter",
                )
            ],
            compute=models.ComputeFields(
                gpuDevicesRequest=1,
                gpuPortionRequest=0.5,
                cpuCoreRequest=0.1,
                cpuMemoryRequest="100M",
                gpuRequestType="portion",
            ),
        ),
    )
)
print(response)
