from runai.client import RunaiClient

# Scroll to the bottom to see the controller methods and implementation

jupyter_sample_half_gpu_spec = {
        "command": "start-notebook.sh",
        "args": "--NotebookApp.base_url=/${RUNAI_PROJECT}/${RUNAI_JOB_NAME} --NotebookApp.token=''",
        "image": "gcr.io/run-ai-demo/jupyter-demo",
        "imagePullPolicy": "Always",
        "nodePools": ["default"],
        "compute": {
            "gpuDevicesRequest": 1,
            "gpuRequestType": "portion",
            "gpuPortionRequest": 0.5,
        },
        "security": {
            "seccompProfileType": "RuntimeDefault",
        },
        "backoffLimit": 6,
        "exposedUrls": [
            {"container": 8888, "toolType": "jupyter-notebook", "toolName": "Jupyter"}
        ],
        "priorityClass": "build",
    }

tensorboard_sample_cpu_only_spec = {
        "command": "tensorboard",
        "args": "--logdir ./ --host 0.0.0.0 --path_prefix /${RUNAI_PROJECT}/${RUNAI_JOB_NAME}",
        "image": "tensorflow/tensorflow:latest",
        "imagePullPolicy": "Always",
        "nodePools": ["default"],
        "compute": {
            "cpuCoreRequest": 0.1,
            "cpuMemoryRequest": "100M",
            "gpuDevicesRequest": 0,
        },
        "backoffLimit": 6,
        "exposedUrls": [
            {"container": 6006, "toolType": "tensorboard", "toolName": "TensorBoard"}
        ],
        "priorityClass": "build",
    }

tensorboard_sample_one_gpu_pvc_spec = {
        "command": "tensorboard",
        "args": "--logdir ./ --host 0.0.0.0 --path_prefix /${RUNAI_PROJECT}/${RUNAI_JOB_NAME}",
        "image": "tensorflow/tensorflow:latest",
        "imagePullPolicy": "Always",
        "nodePools": ["default"],
        "compute": {
            "cpuCoreRequest": 0.1,
            "gpuRequestType": "portion",
            "cpuMemoryRequest": "100M",
            "gpuDevicesRequest": 1,
            "gpuPortionRequest": 1,
        },
        "storage": {
            "pvc": [
                {
                    "path": "/tmp",
                    "readOnly": False,
                    "claimName": "pvc-1-project-h15je",
                    "existingPvc": True,
                }
            ]
        },
        "backoffLimit": 6,
        "exposedUrls": [
            {"container": 6006, "toolType": "tensorboard", "toolName": "TensorBoard"}
        ],
        "priorityClass": "build",
    }

chatui_sample_generic_secret_spec = {
        "image": "gcr.io/run-ai-demo/llm:app",
        "imagePullPolicy": "Always",
        "nodePools": ["default"],
        "compute": {
            "cpuCoreRequest": 0.1,
            "cpuMemoryRequest": "100M",
            "gpuDevicesRequest": 0,
        },
        "storage": {
            "secretVolume": [
                {"secret": "genericsecret-generic-secret", "mountPath": "/tmp/"}
            ]
        },
        "backoffLimit": 6,
        "exposedUrls": [
            {"toolName": "ChatbotUI", "toolType": "chatbot-ui", "container": 3000}
        ],
        "environmentVariables": [
            {"name": "RUNAI_MODEL_NAME", "value": "MODEL_NAME_HERE"},
            {
                "name": "RUNAI_MODEL_BASE_URL",
                "value": "http://WORKLOAD.runai-PROJECT.svc",
            },
            {"name": "RUNAI_MODEL_MAX_LENGTH", "value": "4096"},
            {"name": "RUNAI_MODEL_TOKEN_LIMIT", "value": "2048"},
            {"name": "PATH_PREFIX", "value": "/${RUNAI_PROJECT}/${RUNAI_JOB_NAME}"},
        ],
        "priorityClass": "build",
    }

client = RunaiClient(
    realm=REALM,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    runai_base_url=BASE_URL,
    cluster_id=CLUSTER_ID
)    

# First, get the project ID of the relevant project
# If alraedy known, skip this step

filter_by = f"clusterId=={CLUSTER_ID}"
respone = client.projects.all(filterBy=filter_by)

projects_list = respone["projects"]

project_name = "my-project-name"
project_id = None

for project in projects_list:
    if project["name"] == project_name:
        project_id = project["id"]

# Switch the spec with one of the following examples above, or create your own spec
# It is recommened to switch the workload_name to imply on the used spec
# Visit https://app.run.ai/api/docs to see all options under the spec

workspace = client.workspace.create(
        workspace_name="jupyter-workspace",
        use_given_name_as_prefix=False,
        project_id=project_id,
        cluster_id=CLUSTER_ID,
        spec=jupyter_sample_half_gpu_spec
    )

print(workspace)

workspace_id = workspace["workloadId"]

# Get a workspace
print(client.workspace.get(workspace_id=workspace_id))

# Suspend a workspace
print(client.workspace.suspend(workspace_id=workspace_id))

# Resume a workspace
print(client.workspace.resume(workspace_id=workspace_id))
