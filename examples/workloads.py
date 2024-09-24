from runai.client import RunaiClient

client = RunaiClient(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    runai_base_url=BASE_URL,
    cluster_id=CLUSTER_ID
)

print(client.workloads.get_workloads_telemetry(telemetry_type="WORKLOADS_COUNT"))

print(client.workloads.count_workloads(deleted=True))


print(client.workloads.get_workload_metrics(
    workload_id="7202a18e-051d-4362-b6d2-06d94094df6c",
    metric_type="GPU_UTILIZATION",
    start="2023-06-06T12:09:18.211Z",
    end="2025-06-06T12:09:18.211Z"
    ))

print(client.workloads.all(deleted=False))
