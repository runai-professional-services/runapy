"""
This script is used to create an inference workload with the Run:AI client using the LLaMA 3.1-8B LLM model from NVIDIA NGC.

Steps performed by the script:

1. Connects to Run:AI using the provided client credentials. Ensure you have at least one existing project.
2. Configures the NVIDIA NGC Docker registry secret to enable pulling the LLaMA 3.1-8B model image.
3. Defines and creates a Persistent Volume Claim (PVC) for model storage with NFS as the backend.
4. Configures the inference workload to run the LLaMA 3.1-8B model, setting CPU, GPU, and memory requirements.
5. Deploys the inference workload with autoscaling on the specified node pool.

Key Details:
- Storage recommendation: 100GB to 500GB, depending on model size.
- Default storage path: `/opt/nim/.cache`.
- Warning: Not using a PVC for storage may result in the node becoming full, leading to a `NodeNotReady` state.
"""

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

NGC_USER = "$oauthtoken"
NGC_PASSWORD = NGC_API_TOKEN  # Replace with NGC API token
NGC_REGISTRY_URL = "nvcr.io"
RUNAI_PROJECT_NAME = "my-project"

## 1. Fetch the projects id given to be used in the workload creation
response = client.organizations.projects.get_projects(
    filter_by=[f"name=={RUNAI_PROJECT_NAME}"]
).data["projects"][0]
project_id = response["id"]
cluster_id = response["clusterId"]

## 2. Create NVIDIA NGC Docker registry secret to enable pulling the model image from nvcr.io
client.workload_assets.credentials.create_docker_registry(
    docker_registry_creation_request=models.DockerRegistryCreationRequest(
        meta=models.AssetCreationRequest(
            name="ngc-registry-secret",
            scope=models.Scope.PROJECT,
            projectId=int(project_id),
        ),
        # Add existing_secret_name if you intend to use existing secret
        spec=models.DockerRegistryCreationSpec(
            user=NGC_USER, password=NGC_PASSWORD, url=NGC_REGISTRY_URL
        ),
    )
)


"""
Storage ideal size 100GB → 500GB - Based on Model
Default NIM location -> /opt/nim/.cache
"""
pvc_spec = {
    "path": "/opt/nim/.cache",
    "existingPvc": False,
    "claimName": "llama-nfs-pvc",
    "readOnly": False,
    "ephemeral": False,
    "claimInfo": {
        "size": "100G",
        "storageClass": "nfs-csi",
        "accessModes": {
            "readWriteOnce": False,
            "readOnlyMany": False,
            "readWriteMany": True,
        },
        "volumeMode": "Filesystem",
    },
}
# Create PVC
client.workload_assets.pvc.create_pvc_asset(
    pvc_creation_request=models.PVCCreationRequest(
        meta=models.AssetCreationRequest(
            name="llama-nfs-pvc", scope=models.Scope.PROJECT, projectId=int(project_id)
        ),
        spec=models.PVCAssetSpec.from_dict(pvc_spec),
    )
)

inference_nim_llama_3_1_8b_instruct = {
    "image": "nvcr.io/nim/meta/llama-3.1-8b-instruct:latest",
    "imagePullPolicy": "Always",
    "nodePools": ["default"],
    "servingPort": {"protocol": "http", "container": 8000},
    "autoscaling": {
        "metric": "concurrency",
        "maxReplicas": 3,
        "minReplicas": 0,
        "metricThreshold": 2,
        "scaleToZeroRetentionSeconds": 1800,
    },
    "compute": {
        "cpuCoreRequest": 0.1,
        "gpuRequestType": "portion",
        "cpuMemoryRequest": "100M",
        "gpuDevicesRequest": 1,
        "gpuPortionRequest": 1,
    },
    "environmentVariables": [
        {"name": "NGC_API_KEY", "value": NGC_PASSWORD},
    ],
    "storage": {
        "pvc": [
            {
                "name": "llama-nfs-pvc",
                "existingPvc": True,
                "claimName": "llama-nfs-pvc3",
                "path": "/opt/nim/.cache",
            }
        ]
    },
}

## 2. Create 4 gpu chatbot llm inference workload
response = client.workloads.inferences.create_inference1(
    inference_creation_request=models.InferenceCreationRequest(
        name="llama-3-1-8b-inference-workload",
        projectId=project_id,
        clusterId=cluster_id,
        spec=models.InferenceSpecSpec.from_dict(inference_nim_llama_3_1_8b_instruct),
    )
)
print(response)
