from runai.client import RunaiClient

distributed_sample_small_gpu_two_workers_spec = {
        "image": "gcr.io/kubeflow-ci/pytorch-dist-mnist_test:1.0",
        "imagePullPolicy": "Always",
        "nodePools": ["default"],
        "numWorkers": 2,
        "compute": {
            "cpuCoreRequest": 0.1,
            "gpuRequestType": "portion",
            "cpuMemoryRequest": "100M",
            "gpuDevicesRequest": 1,
            "gpuPortionRequest": 0.1,
        },
        "backoffLimit": 18,
        "distributedFramework": "PyTorch",
        "masterSpecSameAsWorker": True,
    }

client = RunaiClient(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    runai_base_url=BASE_URL,
    cluster_id=CLUSTER_ID
)    

# Get project ID by name
filter_by = f"clusterId=={CLUSTER_ID}"
respone = client.projects.all(filterBy=filter_by)

projects_list = respone["projects"]

project_name = "my-project-name"
project_id = None

for project in projects_list:
    if project["name"] == project_name:
        project_id = project["id"]

distributed_workload = client.distributed.create(
        ditributed_training_name="distributed-pytorch-two-gpus",
        use_given_name_as_prefix=False,
        project_id=project_id,
        cluster_id=CLUSTER_ID,
        spec=distributed_sample_small_gpu_two_workers_spec
    )

print(distributed_workload)

distributed_workload_id = distributed_workload["workloadId"]

# Get the workload data
print(client.distributed.get(distributed_workload_id=distributed_workload_id))

# Delete the workload
print(client.distributed.delete(distributed_workload_id=distributed_workload_id))