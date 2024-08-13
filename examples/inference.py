from runai.client import RunaiClient

# Scroll to the bottom to see the controller methods and implementation

inference_llm_sample_autoscaling_spec = {
        "image": "gcr.io/run-ai-demo/llm",
        "imagePullPolicy": "Always",
        "nodePools": ["default"],
        "annotations": [{"name": "workloadNumber", "value": "1231"}],
        "servingPort": {"protocol": "http", "container": 8000},
        "autoscaling": {
            "metric": "concurrency",
            "maxReplicas": 3,
            "minReplicas": 0,
            "metricThreshold": 2,
            "scaleToZeroRetentionSeconds": 900,
        },
        "compute": {
            "cpuCoreRequest": 0.1,
            "gpuRequestType": "portion",
            "cpuMemoryRequest": "100M",
            "gpuDevicesRequest": 1,
            "gpuPortionRequest": 1,
        },
        "environmentVariables": [
            {"name": "RUNAI_MODEL", "value": "meta-llama/Llama-2-7b-chat-hf"},
            {"name": "HF_TOKEN", "value": "hf_1234567890"},
        ],
    }


client = RunaiClient(
    realm=REALM,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    runai_base_url=BASE_URL,
    cluster_id=CLUSTER_ID
)    

# Create the inference workload
inference = client.workspace.create(
        workspace_name="inference-job1",
        use_given_name_as_prefix=False,
        project_id=PROJECT_ID,
        cluster_id=CLUSTER_ID,
        spec=inference_llm_sample_autoscaling_spec
        )

inference_id = inference["workloadId"]

# Get the inference workload
print(client.inference.get(inference_id=inference_id))

# Delete the inference workload
print(client.inference.delete(inference_id=inference_id))


# Get the metrics of the inference workload
print(client.inference.get_metrics(
    inference_id=inference_id,
    start="2023-06-06T12:09:18.211Z",
    end="2025-06-06T12:09:18.211Z",
    metric_type="THROUGHPUT"
    ))