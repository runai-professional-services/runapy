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

from runai.client import RunaiClient


# Create Run:ai client
client = RunaiClient(
    realm=RELAM,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    runai_base_url=RUNAI_BASE_URL,
    cluster_id=CLUSTER_ID
)


NGC_USER = "$oauthtoken"
NGC_PASSWORD = NGC_API_KEY
NGC_REGISTRY_URL = "nvcr.io"

# Create NVIDIA NGC Docker registry secret to enable pulling the model image from nvcr.io
client.assets.credentials.docker_registry_secret.create(
    name="ngc-secret",
    scope="tenant",
    user=NGC_USER,
    password=NGC_PASSWORD,
    url=NGC_REGISTRY_URL
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
client.assets.pvc.create(
    name="llama-nfs-pvc",
    scope="tenant",
    spec=pvc_spec
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
        "pvc": [{
            "name": "llama-nfs-pvc",
            "existingPvc": True,
            "claimName": "llama-nfs-pvc",
            "path": "/opt/nim/.cache"
        }]
    }
}

# Get first project id in the cluster and assign the workload on it
project_id = client.projects.all(filterBy=f"clusterId=={client.cluster_id}")["projects"][0]["id"]

# Create the inference workload
workload = client.inference.create(
    inference_name="llama31-8b",
    use_given_name_as_prefix=False,
    project_id=project_id,
    cluster_id=client.cluster_id,
    spec=inference_nim_llama_3_1_8b_instruct
)

print(workload)
