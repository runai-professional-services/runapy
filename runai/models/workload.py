# coding: utf-8

"""
Runai API

# Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: 2.19
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.actions_support import ActionsSupport
from runai.models.condition1 import Condition1
from runai.models.connection1 import Connection1
from runai.models.datasource import Datasource
from runai.models.environment import Environment
from runai.models.phase import Phase
from runai.models.phase_reason import PhaseReason
from runai.models.requested_pods import RequestedPods
from runai.models.source import Source
from runai.models.workload_allocated_resources import WorkloadAllocatedResources
from runai.models.workload_children_ids_inner import WorkloadChildrenIdsInner
from runai.models.workload_request_resources import WorkloadRequestResources
from typing import Optional, Set
from typing_extensions import Self


class Workload(BaseModel):
    """
    Pydantic class model representing Workload.

    Parameters:
        ```python
        tenant_id: int
        running_pods: int
        phase_updated_at: datetime
        k8s_phase_updated_at: datetime
        updated_at: datetime
        source: Source
        deleted_at: Optional[datetime]
        type: str
        name: str
        id: str
        priority: Optional[int]
        priority_class_name: str
        submitted_by: str
        cluster_id: str
        project_name: str
        project_id: str
        department_name: str
        department_id: str
        namespace: str
        created_at: datetime
        workload_requested_resources: Optional[WorkloadRequestResources]
        pods_requested_resources: Optional[WorkloadRequestResources]
        allocated_resources: Optional[WorkloadAllocatedResources]
        actions_support: ActionsSupport
        phase: Phase
        conditions: List[Condition1]
        phase_message: str
        k8s_phase: str
        requested_pods: RequestedPods
        requested_node_pools: List[str]
        current_node_pools: List[str]
        completed_at: Optional[datetime]
        images: List[str]
        children_ids: List[WorkloadChildrenIdsInner]
        urls: List[str]
        datasources: List[Datasource]
        environments: List[Environment]
        external_connections: List[Connection1]
        distributed_framework: str
        additional_fields: Dict[str, object]
        preemptible: Optional[bool]
        environment_variables: Dict[str, str]
        command: str
        arguments: str
        phase_reason: Optional[PhaseReason]
        ```
        tenant_id: The id of the tenant.
        running_pods: See model int for more information.
        phase_updated_at: See model datetime for more information.
        k8s_phase_updated_at: See model datetime for more information.
        updated_at: See model datetime for more information.
        source: See model Source for more information.
        deleted_at: See model datetime for more information.
        type: See model str for more information.
        name: See model str for more information.
        id: See model str for more information.
        priority: See model int for more information.
        priority_class_name: See model str for more information.
        submitted_by: See model str for more information.
        cluster_id: The id of the cluster.
        project_name: See model str for more information.
        project_id: See model str for more information.
        department_name: See model str for more information.
        department_id: See model str for more information.
        namespace: See model str for more information.
        created_at: See model datetime for more information.
        workload_requested_resources: See model WorkloadRequestResources for more information.
        pods_requested_resources: See model WorkloadRequestResources for more information.
        allocated_resources: See model WorkloadAllocatedResources for more information.
        actions_support: See model ActionsSupport for more information.
        phase: See model Phase for more information.
        conditions: See model List[Condition1] for more information.
        phase_message: See model str for more information.
        k8s_phase: See model str for more information.
        requested_pods: See model RequestedPods for more information.
        requested_node_pools: See model List[str] for more information.
        current_node_pools: See model List[str] for more information.
        completed_at: See model datetime for more information.
        images: See model List[str] for more information.
        children_ids: See model List[WorkloadChildrenIdsInner] for more information.
        urls: See model List[str] for more information.
        datasources: See model List[Datasource] for more information.
        environments: See model List[Environment] for more information.
        external_connections: See model List[Connection1] for more information.
        distributed_framework: See model str for more information.
        additional_fields: See model Dict[str, object] for more information.
        preemptible: See model bool for more information.
        environment_variables: See model Dict[str, str] for more information.
        command: See model str for more information.
        arguments: See model str for more information.
        phase_reason: See model PhaseReason for more information.
    Example:
        ```python
        Workload(
            tenant_id=1001,
                        running_pods=1,
                        phase_updated_at='2022-06-08T11:28:24.131Z',
                        k8s_phase_updated_at='2022-06-08T11:28:24.131Z',
                        updated_at='2022-06-08T11:28:24.131Z',
                        source='CLI',
                        deleted_at='2022-08-12T19:28:24.131Z',
                        type='runai-job',
                        name='very-important-job',
                        id='',
                        priority=50,
                        priority_class_name='high-priority',
                        submitted_by='researcher@run.ai',
                        cluster_id='71f69d83-ba66-4822-adf5-55ce55efd210',
                        project_name='proj-1',
                        project_id='1',
                        department_name='department-1',
                        department_id='1',
                        namespace='runai-proj-1',
                        created_at='2022-01-01T03:49:52.531Z',
                        workload_requested_resources=runai.models.workload_request_resources.WorkloadRequestResources(
                    gpu_request_type = 'portion',
                    gpu = runai.models.request_resource_cores.RequestResourceCores(
                        limit = 1.5,
                        request = 1, ),
                    gpu_memory = runai.models.request_resource_quantity.RequestResourceQuantity(
                        limit = '2G',
                        request = '200M', ),
                    cpu = runai.models.request_resource_cores.RequestResourceCores(
                        limit = 1.5,
                        request = 1, ),
                    cpu_memory = runai.models.request_resource_quantity.RequestResourceQuantity(
                        limit = '2G',
                        request = '200M', ),
                    mig_profile = [
                        '1g.5gb'
                        ],
                    extended_resources = [
                        runai.models.workloads_extended_resource.WorkloadsExtendedResource(
                            resource = 'hardware-vendor.example/foo',
                            quantity = '2',
                            exclude = False, )
                        ], ),
                        pods_requested_resources=runai.models.workload_request_resources.WorkloadRequestResources(
                    gpu_request_type = 'portion',
                    gpu = runai.models.request_resource_cores.RequestResourceCores(
                        limit = 1.5,
                        request = 1, ),
                    gpu_memory = runai.models.request_resource_quantity.RequestResourceQuantity(
                        limit = '2G',
                        request = '200M', ),
                    cpu = runai.models.request_resource_cores.RequestResourceCores(
                        limit = 1.5,
                        request = 1, ),
                    cpu_memory = runai.models.request_resource_quantity.RequestResourceQuantity(
                        limit = '2G',
                        request = '200M', ),
                    mig_profile = [
                        '1g.5gb'
                        ],
                    extended_resources = [
                        runai.models.workloads_extended_resource.WorkloadsExtendedResource(
                            resource = 'hardware-vendor.example/foo',
                            quantity = '2',
                            exclude = False, )
                        ], ),
                        allocated_resources=runai.models.workload_allocated_resources.WorkloadAllocatedResources(
                    gpu = 1.5,
                    mig_profile = [
                        '1g.5gb'
                        ],
                    gpu_memory = '200Mi',
                    cpu = 0.5,
                    cpu_memory = '0B',
                    extended_resources = [
                        runai.models.workloads_extended_resource.WorkloadsExtendedResource(
                            resource = 'hardware-vendor.example/foo',
                            quantity = '2',
                            exclude = False, )
                        ], ),
                        actions_support=runai.models.actions_support.ActionsSupport(
                    delete = True,
                    suspend = True, ),
                        phase='Creating',
                        conditions=[
                    runai.models.condition1.Condition1(
                        type = 'Ready',
                        status = 'False',
                        message = 'Resource validation failed: ...',
                        reason = 'ErrorConfig',
                        last_transition_time = '2022-01-01T03:49:52.531Z', )
                    ],
                        phase_message='Not enough resources in the requested nodepool',
                        k8s_phase='Pending',
                        requested_pods=runai.models.requested_pods.RequestedPods(
                    number = 1,
                    min = 2,
                    max = 5,
                    parallelism = 3,
                    completions = 5, ),
                        requested_node_pools=[
                    'default'
                    ],
                        current_node_pools=[
                    'default'
                    ],
                        completed_at='2022-01-01T03:49:52.531Z',
                        images=[
                    'alpine:latest'
                    ],
                        children_ids=[
                    runai.models.workload_children_ids_inner.Workload_childrenIds_inner(
                        id = '',
                        type = '', )
                    ],
                        urls=[
                    ''
                    ],
                        datasources=[
                    runai.models.datasource.Datasource(
                        type = 'pvc',
                        name = 'my-pvc-datasource-1',
                        id = '', )
                    ],
                        environments=[
                    runai.models.environment.Environment(
                        connections = [
                            runai.models.connection1.Connection1(
                                name = 'my-pytorch-env',
                                tool_type = 'pytorch',
                                connection_type = 'ExternalUrl',
                                url = 'http://wandb.com/yourproject',
                                authorized_users = ["user@company.ai","another@company.ai"],
                                authorized_groups = ["group-a","group-b"],
                                container_port = 8080, )
                            ],
                        name = 'pytorch',
                        id = '',
                        replica_type = 'Master', )
                    ],
                        external_connections=[
                    runai.models.connection1.Connection1(
                        name = 'my-pytorch-env',
                        tool_type = 'pytorch',
                        connection_type = 'ExternalUrl',
                        url = 'http://wandb.com/yourproject',
                        authorized_users = ["user@company.ai","another@company.ai"],
                        authorized_groups = ["group-a","group-b"],
                        container_port = 8080, )
                    ],
                        distributed_framework='Pytorch',
                        additional_fields={ },
                        preemptible=True,
                        environment_variables={
                    'key' : ''
                    },
                        command='sleep',
                        arguments='1000',
                        phase_reason='NonPreemptibleOverQuota'
        )
        ```
    """  # noqa: E501

    tenant_id: StrictInt = Field(description="The id of the tenant.", alias="tenantId")
    running_pods: StrictInt = Field(alias="runningPods")
    phase_updated_at: datetime = Field(alias="phaseUpdatedAt")
    k8s_phase_updated_at: datetime = Field(alias="k8sPhaseUpdatedAt")
    updated_at: datetime = Field(alias="updatedAt")
    source: Source
    deleted_at: Optional[datetime] = Field(alias="deletedAt")
    type: StrictStr
    name: StrictStr
    id: StrictStr
    priority: Optional[StrictInt]
    priority_class_name: StrictStr = Field(alias="priorityClassName")
    submitted_by: Optional[StrictStr] = Field(default=None, alias="submittedBy")
    cluster_id: StrictStr = Field(
        description="The id of the cluster.", alias="clusterId"
    )
    project_name: StrictStr = Field(alias="projectName")
    project_id: StrictStr = Field(alias="projectId")
    department_name: StrictStr = Field(alias="departmentName")
    department_id: StrictStr = Field(alias="departmentId")
    namespace: StrictStr
    created_at: datetime = Field(alias="createdAt")
    workload_requested_resources: Optional[WorkloadRequestResources] = Field(
        default=None, alias="workloadRequestedResources"
    )
    pods_requested_resources: Optional[WorkloadRequestResources] = Field(
        default=None, alias="podsRequestedResources"
    )
    allocated_resources: Optional[WorkloadAllocatedResources] = Field(
        default=None, alias="allocatedResources"
    )
    actions_support: Optional[ActionsSupport] = Field(
        default=None, alias="actionsSupport"
    )
    phase: Phase
    conditions: List[Condition1]
    phase_message: Optional[StrictStr] = Field(default=None, alias="phaseMessage")
    k8s_phase: StrictStr = Field(alias="k8sPhase")
    requested_pods: Optional[RequestedPods] = Field(default=None, alias="requestedPods")
    requested_node_pools: Optional[List[StrictStr]] = Field(
        default=None, alias="requestedNodePools"
    )
    current_node_pools: Optional[List[StrictStr]] = Field(
        default=None, alias="currentNodePools"
    )
    completed_at: Optional[datetime] = Field(default=None, alias="completedAt")
    images: Optional[List[StrictStr]] = None
    children_ids: Optional[List[WorkloadChildrenIdsInner]] = Field(
        default=None, alias="childrenIds"
    )
    urls: Optional[List[StrictStr]] = None
    datasources: Optional[List[Datasource]] = None
    environments: Optional[List[Environment]] = None
    external_connections: Optional[List[Connection1]] = Field(
        default=None, alias="externalConnections"
    )
    distributed_framework: Optional[StrictStr] = Field(
        default=None, alias="distributedFramework"
    )
    additional_fields: Optional[Dict[str, Any]] = Field(
        default=None, alias="additionalFields"
    )
    preemptible: Optional[StrictBool] = None
    environment_variables: Optional[Dict[str, StrictStr]] = Field(
        default=None, alias="environmentVariables"
    )
    command: Optional[StrictStr] = None
    arguments: Optional[StrictStr] = None
    phase_reason: Optional[PhaseReason] = Field(default=None, alias="phaseReason")
    __properties: ClassVar[List[str]] = [
        "tenantId",
        "runningPods",
        "phaseUpdatedAt",
        "k8sPhaseUpdatedAt",
        "updatedAt",
        "source",
        "deletedAt",
        "type",
        "name",
        "id",
        "priority",
        "priorityClassName",
        "submittedBy",
        "clusterId",
        "projectName",
        "projectId",
        "departmentName",
        "departmentId",
        "namespace",
        "createdAt",
        "workloadRequestedResources",
        "podsRequestedResources",
        "allocatedResources",
        "actionsSupport",
        "phase",
        "conditions",
        "phaseMessage",
        "k8sPhase",
        "requestedPods",
        "requestedNodePools",
        "currentNodePools",
        "completedAt",
        "images",
        "childrenIds",
        "urls",
        "datasources",
        "environments",
        "externalConnections",
        "distributedFramework",
        "additionalFields",
        "preemptible",
        "environmentVariables",
        "command",
        "arguments",
        "phaseReason",
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
        """Create an instance of Workload from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of workload_requested_resources
        if self.workload_requested_resources:
            _dict["workloadRequestedResources"] = (
                self.workload_requested_resources.to_dict()
            )
        # override the default output from pydantic by calling `to_dict()` of pods_requested_resources
        if self.pods_requested_resources:
            _dict["podsRequestedResources"] = self.pods_requested_resources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of allocated_resources
        if self.allocated_resources:
            _dict["allocatedResources"] = self.allocated_resources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of actions_support
        if self.actions_support:
            _dict["actionsSupport"] = self.actions_support.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in conditions (list)
        _items = []
        if self.conditions:
            for _item_conditions in self.conditions:
                if _item_conditions:
                    _items.append(_item_conditions.to_dict())
            _dict["conditions"] = _items
        # override the default output from pydantic by calling `to_dict()` of requested_pods
        if self.requested_pods:
            _dict["requestedPods"] = self.requested_pods.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in children_ids (list)
        _items = []
        if self.children_ids:
            for _item_children_ids in self.children_ids:
                if _item_children_ids:
                    _items.append(_item_children_ids.to_dict())
            _dict["childrenIds"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in datasources (list)
        _items = []
        if self.datasources:
            for _item_datasources in self.datasources:
                if _item_datasources:
                    _items.append(_item_datasources.to_dict())
            _dict["datasources"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in environments (list)
        _items = []
        if self.environments:
            for _item_environments in self.environments:
                if _item_environments:
                    _items.append(_item_environments.to_dict())
            _dict["environments"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in external_connections (list)
        _items = []
        if self.external_connections:
            for _item_external_connections in self.external_connections:
                if _item_external_connections:
                    _items.append(_item_external_connections.to_dict())
            _dict["externalConnections"] = _items
        # set to None if deleted_at (nullable) is None
        # and model_fields_set contains the field
        if self.deleted_at is None and "deleted_at" in self.model_fields_set:
            _dict["deletedAt"] = None

        # set to None if priority (nullable) is None
        # and model_fields_set contains the field
        if self.priority is None and "priority" in self.model_fields_set:
            _dict["priority"] = None

        # set to None if workload_requested_resources (nullable) is None
        # and model_fields_set contains the field
        if (
            self.workload_requested_resources is None
            and "workload_requested_resources" in self.model_fields_set
        ):
            _dict["workloadRequestedResources"] = None

        # set to None if pods_requested_resources (nullable) is None
        # and model_fields_set contains the field
        if (
            self.pods_requested_resources is None
            and "pods_requested_resources" in self.model_fields_set
        ):
            _dict["podsRequestedResources"] = None

        # set to None if allocated_resources (nullable) is None
        # and model_fields_set contains the field
        if (
            self.allocated_resources is None
            and "allocated_resources" in self.model_fields_set
        ):
            _dict["allocatedResources"] = None

        # set to None if completed_at (nullable) is None
        # and model_fields_set contains the field
        if self.completed_at is None and "completed_at" in self.model_fields_set:
            _dict["completedAt"] = None

        # set to None if preemptible (nullable) is None
        # and model_fields_set contains the field
        if self.preemptible is None and "preemptible" in self.model_fields_set:
            _dict["preemptible"] = None

        # set to None if phase_reason (nullable) is None
        # and model_fields_set contains the field
        if self.phase_reason is None and "phase_reason" in self.model_fields_set:
            _dict["phaseReason"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Workload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "tenantId": obj.get("tenantId"),
                "runningPods": obj.get("runningPods"),
                "phaseUpdatedAt": obj.get("phaseUpdatedAt"),
                "k8sPhaseUpdatedAt": obj.get("k8sPhaseUpdatedAt"),
                "updatedAt": obj.get("updatedAt"),
                "source": obj.get("source"),
                "deletedAt": obj.get("deletedAt"),
                "type": obj.get("type"),
                "name": obj.get("name"),
                "id": obj.get("id"),
                "priority": obj.get("priority"),
                "priorityClassName": obj.get("priorityClassName"),
                "submittedBy": obj.get("submittedBy"),
                "clusterId": obj.get("clusterId"),
                "projectName": obj.get("projectName"),
                "projectId": obj.get("projectId"),
                "departmentName": obj.get("departmentName"),
                "departmentId": obj.get("departmentId"),
                "namespace": obj.get("namespace"),
                "createdAt": obj.get("createdAt"),
                "workloadRequestedResources": (
                    WorkloadRequestResources.from_dict(
                        obj["workloadRequestedResources"]
                    )
                    if obj.get("workloadRequestedResources") is not None
                    else None
                ),
                "podsRequestedResources": (
                    WorkloadRequestResources.from_dict(obj["podsRequestedResources"])
                    if obj.get("podsRequestedResources") is not None
                    else None
                ),
                "allocatedResources": (
                    WorkloadAllocatedResources.from_dict(obj["allocatedResources"])
                    if obj.get("allocatedResources") is not None
                    else None
                ),
                "actionsSupport": (
                    ActionsSupport.from_dict(obj["actionsSupport"])
                    if obj.get("actionsSupport") is not None
                    else None
                ),
                "phase": obj.get("phase"),
                "conditions": (
                    [Condition1.from_dict(_item) for _item in obj["conditions"]]
                    if obj.get("conditions") is not None
                    else None
                ),
                "phaseMessage": obj.get("phaseMessage"),
                "k8sPhase": obj.get("k8sPhase"),
                "requestedPods": (
                    RequestedPods.from_dict(obj["requestedPods"])
                    if obj.get("requestedPods") is not None
                    else None
                ),
                "requestedNodePools": obj.get("requestedNodePools"),
                "currentNodePools": obj.get("currentNodePools"),
                "completedAt": obj.get("completedAt"),
                "images": obj.get("images"),
                "childrenIds": (
                    [
                        WorkloadChildrenIdsInner.from_dict(_item)
                        for _item in obj["childrenIds"]
                    ]
                    if obj.get("childrenIds") is not None
                    else None
                ),
                "urls": obj.get("urls"),
                "datasources": (
                    [Datasource.from_dict(_item) for _item in obj["datasources"]]
                    if obj.get("datasources") is not None
                    else None
                ),
                "environments": (
                    [Environment.from_dict(_item) for _item in obj["environments"]]
                    if obj.get("environments") is not None
                    else None
                ),
                "externalConnections": (
                    [
                        Connection1.from_dict(_item)
                        for _item in obj["externalConnections"]
                    ]
                    if obj.get("externalConnections") is not None
                    else None
                ),
                "distributedFramework": obj.get("distributedFramework"),
                "additionalFields": obj.get("additionalFields"),
                "preemptible": obj.get("preemptible"),
                "environmentVariables": obj.get("environmentVariables"),
                "command": obj.get("command"),
                "arguments": obj.get("arguments"),
                "phaseReason": obj.get("phaseReason"),
            }
        )
        return _obj
