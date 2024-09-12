"""
Basic example on how to use the metrics API endpoint

####### Important#######
This endpoint is experimental and is due to future changes
########################

The script uses two Run:ai API endpoints:
- list workloads -  list all workloads in the cluster/project/department
- workload metrics - get metrics and measurements data for the workload

Documentation for the endpoints and parameter options can be found here:
- list workloads - https://api-docs.run.ai/2.18/tag/Workloads#operation/get_workloads
- workload metrics - https://api-docs.run.ai/2.18/tag/Workloads#operation/get_workload_metrics

For optimal measurements, select a short start<->end time range and set the num_of_samples to high number (1000)

"""

import datetime
from runai.client import RunaiClient

client = RunaiClient(
    realm=REALM,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    runai_base_url=BASE_URL,
    cluster_id=CLUSTER_ID
)

start_date = "2024-09-12T01:00:00.000Z"
end_date = datetime.datetime.now(datetime.timezone.utc).isoformat().replace("+00:00", "Z")

print(f"Start date: {start_date}")
print(f"End date: {end_date}")
if __name__ == "__main__":
    workloads = client.workloads.all(deleted=False, filter_by=f"clusterId=={client.cluster_id}")['workloads']
    for workload in workloads:
        workload_id = workload["id"]
        print(f"Workload ID: {workload_id}")
        print(client.workloads.get_workload_metrics(workload_id=workload["id"],
                                                    start=start_date,
                                                    end=end_date,
                                                    number_of_samples=1000,
                                                    metric_type="GPU_UTILIZATION"))
