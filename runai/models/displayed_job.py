# coding: utf-8

"""
Run:ai API

# Introduction  The Run:ai Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: latest
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictFloat,
    StrictInt,
    StrictStr,
)
from typing import Any, ClassVar, Dict, List, Optional, Union
from runai.models.pod import Pod
from typing import Optional, Set
from typing_extensions import Self


class DisplayedJob(BaseModel):
    """
    Pydantic class model representing DisplayedJob.

    Parameters:
        ```python
        job_id: str
        pod_group_id: str
        job_name: str
        job_type: str
        cluster_id: str
        status: str
        image_name: str
        user: str
        project: str
        node_id: str
        creation_time: str
        completion_time: str
        total_runtime: str
        total_wait_time: str
        pending: float
        running: float
        parallelism: float
        completions: float
        failed: float
        succeeded: float
        current_allocated_gpus: float
        current_allocated_gpus_memory: float
        current_requested_gpus: float
        total_requested_gpus: float
        requested_gpus_per_pod_group: float
        requested_gpus_memory_per_pod_group: float
        parent_workload_name: str
        total_requested_memory: float
        total_requested_cpu: float
        total_limit_cpu: float
        total_limit_memory: float
        workload_kind: float
        latest_pod: Pod
        cli_command: str
        requested_mig_devices: str
        dynamic_data: object
        exists_in_cluster: bool
        is_jupyter: bool
        job_url: str
        node_pool: str
        ```
        job_id: Unique identifier of the job.
        pod_group_id: Unique identifier of the pod group.
        job_name: The name of the job.
        job_type: See model str for more information.
        cluster_id: Unique identifier of the cluster.
        status: See model str for more information.
        image_name: The name of the image executed by the pod.
        user: The owner of the job.
        project: The project that the pod group belongs to.
        node_id: Unique identifier of the node.
        creation_time: Creation time of the job.
        completion_time: Completion time of the job.
        total_runtime: See model str for more information.
        total_wait_time: See model str for more information.
        pending: See model float for more information.
        running: See model float for more information.
        parallelism: See model float for more information.
        completions: See model float for more information.
        failed: See model float for more information.
        succeeded: See model float for more information.
        current_allocated_gpus: See model float for more information.
        current_allocated_gpus_memory: See model float for more information.
        current_requested_gpus: See model float for more information.
        total_requested_gpus: See model float for more information.
        requested_gpus_per_pod_group: See model float for more information.
        requested_gpus_memory_per_pod_group: See model float for more information.
        parent_workload_name: See model str for more information.
        total_requested_memory: See model float for more information.
        total_requested_cpu: See model float for more information.
        total_limit_cpu: See model float for more information.
        total_limit_memory: See model float for more information.
        workload_kind: Specifies the kind of k8s resource that owns the pod group.
        latest_pod: See model Pod for more information.
        cli_command: See model str for more information.
        requested_mig_devices: See model str for more information.
        dynamic_data: See model object for more information.
        exists_in_cluster: See model bool for more information.
        is_jupyter: If true, it indicates that the pod group runs jupyter notebook. - Default: False
        job_url: See model str for more information.
        node_pool: The node pool of the job.
    Example:
        ```python
        DisplayedJob(
            job_id='',
                        pod_group_id='',
                        job_name='job-0',
                        job_type='',
                        cluster_id='',
                        status='',
                        image_name='tensorflow',
                        user='',
                        project='',
                        node_id='',
                        creation_time='',
                        completion_time='',
                        total_runtime='',
                        total_wait_time='',
                        pending=1.337,
                        running=1.337,
                        parallelism=1.337,
                        completions=1.337,
                        failed=1.337,
                        succeeded=1.337,
                        current_allocated_gpus=1.337,
                        current_allocated_gpus_memory=1.337,
                        current_requested_gpus=1.337,
                        total_requested_gpus=1.337,
                        requested_gpus_per_pod_group=1.337,
                        requested_gpus_memory_per_pod_group=1.337,
                        parent_workload_name='',
                        total_requested_memory=1.337,
                        total_requested_cpu=1.337,
                        total_limit_cpu=1.337,
                        total_limit_memory=1.337,
                        workload_kind=1.337,
                        latest_pod=runai.models.pod.Pod(
                    pod_id = '',
                    job_id = '',
                    pod_group_id = '',
                    cluster_uuid = '',
                    pod_name = '',
                    image_name = '',
                    node_id = '',
                    phase = '',
                    status = '',
                    created = 56,
                    completed = 56,
                    started = 56,
                    last_updated = 56,
                    dynamic_data = runai.models.dynamic_data.dynamicData(),
                    exists_in_cluster = True,
                    resource_request = {
                        'key' : 1.337
                        },
                    resource_allocation = {
                        'key' : 1.337
                        },
                    node_pool = '',
                    namespace = '', ),
                        cli_command='',
                        requested_mig_devices='',
                        dynamic_data=None,
                        exists_in_cluster=True,
                        is_jupyter=True,
                        job_url='',
                        node_pool=''
        )
        ```
    """  # noqa: E501

    job_id: Optional[StrictStr] = Field(
        default=None, description="Unique identifier of the job.", alias="JobId"
    )
    pod_group_id: Optional[StrictStr] = Field(
        default=None,
        description="Unique identifier of the pod group.",
        alias="podGroupId",
    )
    job_name: Optional[StrictStr] = Field(
        default=None, description="The name of the job.", alias="jobName"
    )
    job_type: Optional[StrictStr] = Field(default=None, alias="jobType")
    cluster_id: Optional[StrictStr] = Field(
        default=None, description="Unique identifier of the cluster.", alias="clusterId"
    )
    status: Optional[StrictStr] = None
    image_name: Optional[StrictStr] = Field(
        default=None,
        description="The name of the image executed by the pod.",
        alias="imageName",
    )
    user: Optional[StrictStr] = Field(default=None, description="The owner of the job.")
    project: Optional[StrictStr] = Field(
        default=None, description="The project that the pod group belongs to."
    )
    node_id: Optional[StrictStr] = Field(
        default=None, description="Unique identifier of the node.", alias="nodeId"
    )
    creation_time: Optional[StrictStr] = Field(
        default=None, description="Creation time of the job.", alias="creationTime"
    )
    completion_time: Optional[StrictStr] = Field(
        default=None, description="Completion time of the job.", alias="completionTime"
    )
    total_runtime: Optional[StrictStr] = Field(default=None, alias="totalRuntime")
    total_wait_time: Optional[StrictStr] = Field(default=None, alias="totalWaitTime")
    pending: Optional[Union[StrictFloat, StrictInt]] = None
    running: Optional[Union[StrictFloat, StrictInt]] = None
    parallelism: Optional[Union[StrictFloat, StrictInt]] = None
    completions: Optional[Union[StrictFloat, StrictInt]] = None
    failed: Optional[Union[StrictFloat, StrictInt]] = None
    succeeded: Optional[Union[StrictFloat, StrictInt]] = None
    current_allocated_gpus: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, alias="currentAllocatedGPUs"
    )
    current_allocated_gpus_memory: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, alias="currentAllocatedGPUsMemory"
    )
    current_requested_gpus: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, alias="currentRequestedGPUs"
    )
    total_requested_gpus: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, alias="totalRequestedGPUs"
    )
    requested_gpus_per_pod_group: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, alias="requestedGPUsPerPodGroup"
    )
    requested_gpus_memory_per_pod_group: Optional[Union[StrictFloat, StrictInt]] = (
        Field(default=None, alias="requestedGPUsMemoryPerPodGroup")
    )
    parent_workload_name: Optional[StrictStr] = Field(
        default=None, alias="parentWorkloadName"
    )
    total_requested_memory: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, alias="totalRequestedMemory"
    )
    total_requested_cpu: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, alias="totalRequestedCPU"
    )
    total_limit_cpu: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, alias="totalLimitCPU"
    )
    total_limit_memory: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None, alias="totalLimitMemory"
    )
    workload_kind: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="Specifies the kind of k8s resource that owns the pod group.",
        alias="workloadKind",
    )
    latest_pod: Optional[Pod] = Field(default=None, alias="latestPod")
    cli_command: Optional[StrictStr] = Field(default=None, alias="cliCommand")
    requested_mig_devices: Optional[StrictStr] = Field(
        default=None, alias="requestedMigDevices"
    )
    dynamic_data: Optional[Dict[str, Any]] = Field(default=None, alias="dynamicData")
    exists_in_cluster: Optional[StrictBool] = Field(
        default=None, alias="existsInCluster"
    )
    is_jupyter: Optional[StrictBool] = Field(
        default=False,
        description="If true, it indicates that the pod group runs jupyter notebook.",
        alias="isJupyter",
    )
    job_url: Optional[StrictStr] = Field(default=None, alias="jobUrl")
    node_pool: Optional[StrictStr] = Field(
        default=None, description="The node pool of the job.", alias="nodePool"
    )
    __properties: ClassVar[List[str]] = [
        "JobId",
        "podGroupId",
        "jobName",
        "jobType",
        "clusterId",
        "status",
        "imageName",
        "user",
        "project",
        "nodeId",
        "creationTime",
        "completionTime",
        "totalRuntime",
        "totalWaitTime",
        "pending",
        "running",
        "parallelism",
        "completions",
        "failed",
        "succeeded",
        "currentAllocatedGPUs",
        "currentAllocatedGPUsMemory",
        "currentRequestedGPUs",
        "totalRequestedGPUs",
        "requestedGPUsPerPodGroup",
        "requestedGPUsMemoryPerPodGroup",
        "parentWorkloadName",
        "totalRequestedMemory",
        "totalRequestedCPU",
        "totalLimitCPU",
        "totalLimitMemory",
        "workloadKind",
        "latestPod",
        "cliCommand",
        "requestedMigDevices",
        "dynamicData",
        "existsInCluster",
        "isJupyter",
        "jobUrl",
        "nodePool",
    ]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DisplayedJob from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of latest_pod
        if self.latest_pod:
            _dict["latestPod"] = self.latest_pod.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DisplayedJob from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "JobId": obj.get("JobId"),
                "podGroupId": obj.get("podGroupId"),
                "jobName": obj.get("jobName"),
                "jobType": obj.get("jobType"),
                "clusterId": obj.get("clusterId"),
                "status": obj.get("status"),
                "imageName": obj.get("imageName"),
                "user": obj.get("user"),
                "project": obj.get("project"),
                "nodeId": obj.get("nodeId"),
                "creationTime": obj.get("creationTime"),
                "completionTime": obj.get("completionTime"),
                "totalRuntime": obj.get("totalRuntime"),
                "totalWaitTime": obj.get("totalWaitTime"),
                "pending": obj.get("pending"),
                "running": obj.get("running"),
                "parallelism": obj.get("parallelism"),
                "completions": obj.get("completions"),
                "failed": obj.get("failed"),
                "succeeded": obj.get("succeeded"),
                "currentAllocatedGPUs": obj.get("currentAllocatedGPUs"),
                "currentAllocatedGPUsMemory": obj.get("currentAllocatedGPUsMemory"),
                "currentRequestedGPUs": obj.get("currentRequestedGPUs"),
                "totalRequestedGPUs": obj.get("totalRequestedGPUs"),
                "requestedGPUsPerPodGroup": obj.get("requestedGPUsPerPodGroup"),
                "requestedGPUsMemoryPerPodGroup": obj.get(
                    "requestedGPUsMemoryPerPodGroup"
                ),
                "parentWorkloadName": obj.get("parentWorkloadName"),
                "totalRequestedMemory": obj.get("totalRequestedMemory"),
                "totalRequestedCPU": obj.get("totalRequestedCPU"),
                "totalLimitCPU": obj.get("totalLimitCPU"),
                "totalLimitMemory": obj.get("totalLimitMemory"),
                "workloadKind": obj.get("workloadKind"),
                "latestPod": (
                    Pod.from_dict(obj["latestPod"])
                    if obj.get("latestPod") is not None
                    else None
                ),
                "cliCommand": obj.get("cliCommand"),
                "requestedMigDevices": obj.get("requestedMigDevices"),
                "dynamicData": obj.get("dynamicData"),
                "existsInCluster": obj.get("existsInCluster"),
                "isJupyter": (
                    obj.get("isJupyter") if obj.get("isJupyter") is not None else False
                ),
                "jobUrl": obj.get("jobUrl"),
                "nodePool": obj.get("nodePool"),
            }
        )
        return _obj
