from runai.client import RunaiClient

# Scroll to the bottom to see the controller methods and implementation
# It is recommened to switch the workload_name to imply on the used spec
# Visit https://app.run.ai/api/docs to see all options under the spec

tensorboard_jupyter_training_sample_two_gpu_spec = {
        "image": "gcr.io/run-ai-demo/jupyter-tensorboard",
        "labels": [{"name": "MY_TRAINING_NUMBER", "value": "10241"}],
        "imagePullPolicy": "Always",
        "nodePools": ["default"],
        "compute": {
            "cpuCoreRequest": 0.2,
            "cpuMemoryRequest": "200M",
            "gpuDevicesRequest": 2,
        },
        "backoffLimit": 6,
        "exposedUrls": [
            {"toolName": "Jupyter", "toolType": "jupyter-notebook", "container": 8888},
            {"toolName": "TensorBoard", "toolType": "tensorboard", "container": 6006},
        ],
        "environmentVariables": [{"name": "LOG_DIR", "value": "./"}],
        "priorityClass": "train",
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

training = client.training.create(
        training_name="training-tensor-jupyter-two-gpus",
        use_given_name_as_prefix=False,
        project_id=project_id,
        cluster_id=CLUSTER_ID,
        spec=tensorboard_jupyter_training_sample_two_gpu_spec
        )

print(training)

training_id = training["workloadId"]

# Get a training
print(client.training.get(training_id=training_id))

# Suspend a training
print(client.training.suspend(training_id=training_id))

# Resume a training
print(client.training.resume(training_id=training_id))