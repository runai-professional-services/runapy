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

# Create 4 gpu chatbot llm inference workload in 'test' project
## 1. Fetch the projects id given to be used in the workload creation
response = client.organizations.projects.get_projects(filter_by=["name==test"]).data[
    "projects"
][0]
project_id = response["id"]
cluster_id = response["clusterId"]

## 2. Create 4 gpu chatbot llm inference workload
response = client.workloads.inferences.create_inference1(
    inference_creation_request=models.InferenceCreationRequest(
        name="llm-chat",
        projectId=project_id,
        clusterId=cluster_id,
        spec=models.InferenceSpecSpec(
            image="runai.jfrog.io/core-llm/llm-app",
            command="start-notebook.sh",
            environmentVariables=[
                models.EnvironmentVariable(
                    name="RUNAI_MODEL_NAME",
                    value="meta-llama/Llama-3.1-8B-Instruct",
                ),
                models.EnvironmentVariable(
                    name="RUNAI_MODEL_BASE_URL",
                    value="http://chatbot.runai-test.svc.cluster.local",
                ),
                models.EnvironmentVariable(
                    name="RUNAI_MODEL_TOKEN_LIMIT",
                    value="8192",
                ),
                models.EnvironmentVariable(
                    name="RUNAI_MODEL_MAX_LENGTH",
                    value="16384",
                ),
                models.EnvironmentVariable(
                    name="PATH_PREFIX",
                    value="/${RUNAI_PROJECT}/${RUNAI_JOB_NAME}",
                ),
            ],
            autoscaling=models.AutoScaling(
                maxReplicas=2, minReplicas=1, metric="troughput", metricThreshold=100
            ),
            compute=models.ComputeFields(
                gpuDevicesRequest=1,
                gpuPortionRequest=4,
                cpuCoreRequest=2,
                cpuMemoryRequest="200M",
                gpuRequestType=models.GpuRequestType.PORTION,
            ),
            exposedUrls=[
                models.ExposedUrl(
                    container=3000,
                    name="ChatbotUI",
                    tool_name="ChatbotUI",
                    tool_type="chatbot-ui",
                )
            ],
            servingPort=models.ServingPort(
                container=3000, protocol=models.ServingPortProtocol.HTTP
            ),
        ),
    )
)
print(response)
