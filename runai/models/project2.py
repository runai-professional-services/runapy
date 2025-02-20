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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from runai.models.assigned_resources import AssignedResources
from runai.models.jobs_node_affinity import JobsNodeAffinity
from runai.models.node_pool_assigned_resources import NodePoolAssignedResources
from runai.models.project_status1 import ProjectStatus1
from runai.models.resource_permissions import ResourcePermissions
from typing import Optional, Set
from typing_extensions import Self


class Project2(BaseModel):
    """
    Pydantic class model representing Project2.

    Parameters:
        ```python
        deserved_gpus: float
        max_allowed_gpus: float
        gpu_over_quota_weight: float
        default_node_pools: List[str]
        interactive_job_time_limit_secs: float
        interactive_job_max_idle_duration_secs: float
        interactive_preemptible_job_max_idle_duration_secs: float
        training_job_time_limit_secs: float
        training_job_max_idle_duration_secs: float
        node_affinity: JobsNodeAffinity
        permissions: ResourcePermissions
        resources: AssignedResources
        name: str
        node_pools_resources: List[NodePoolAssignedResources]
        namespace: str
        id: int
        department_id: int
        tenant_id: int
        cluster_uuid: str
        department_name: str
        interactive_node_affinity: str
        train_node_affinity: str
        created_at: datetime
        status: ProjectStatus1
        phase: str
        ```
        deserved_gpus: Deprecated. Use &#39;deserved&#39; for the relevant resource type under &#x60;NodePoolResources&#x60;. The project&#39;s deserved GPU allocation in case the cluster has those resources.
        max_allowed_gpus: Deprecated. Instead, use &#x60;maxAllowed&#x60; for the relevant resource type under &#x60;NodePoolResources&#x60;. An upper limit for the amount of GPUs the project can get (Even if over quota is allowed and resources are available).
        gpu_over_quota_weight: Deprecated. Instead, use &#x60;overQuotaWeight&#x60; for the relevant resource type under &#x60;NodePoolResources&#x60;. The priority the project gets for over quota resources.
        default_node_pools: Default node pools list for workload submission for this project if a workload doesn&#39;t specify a node pools list.
        interactive_job_time_limit_secs: A limit (in seconds) for the duration of interactive jobs from this project.
        interactive_job_max_idle_duration_secs: Maximum duration (in seconds) that an interactive job can be idle before being terminated.
        interactive_preemptible_job_max_idle_duration_secs: Maximum duration (in seconds) that an interactive preemptible job can be idle before being terminated.
        training_job_time_limit_secs: A limit (in seconds) for the duration of training jobs from this project. Available only from cluster version 2.12
        training_job_max_idle_duration_secs: Maximum duration (in seconds) that a training job can be idle before being terminated.
        node_affinity: Node affinity configuration for jobs in the project.
        permissions: Deprecated. Instead, use the &#x60;accessRules&#x60; API to add permissions to a specific subject in the project scope.
        resources: Deprecated. Instead, use &#x60;nodePoolsResources&#x60;. Total resources assigned to the Project. Can only be used in PUT/POST when there is a single Node Pool in the system. The resources returned in &#x60;GET&#x60; are the sum of all Node Pool Resources.
        name: Project name.
        node_pools_resources: Resources assigned to this Project per Node Pool.
        namespace: The name of an existing namespace to use for the project in the cluster. Supported only for cluster versions 2.12 or higher.
        id: Project id.
        department_id: ID of the department that owns the project.
        tenant_id: ID of the tenant where the project is located.
        cluster_uuid: ID of the cluster where the project is located.
        department_name: Name of the department where the project is located.
        interactive_node_affinity: See model str for more information.
        train_node_affinity: See model str for more information.
        created_at: Creation date of the project.
        status: See model ProjectStatus1 for more information.
        phase: project&#39;s phase
    Example:
        ```python
        Project2(
            deserved_gpus=3,
                        max_allowed_gpus=5,
                        gpu_over_quota_weight=1,
                        default_node_pools=[default],
                        interactive_job_time_limit_secs=3600,
                        interactive_job_max_idle_duration_secs=3000,
                        interactive_preemptible_job_max_idle_duration_secs=3000,
                        training_job_time_limit_secs=3600,
                        training_job_max_idle_duration_secs=3000,
                        node_affinity=runai.models.jobs_node_affinity.JobsNodeAffinity(
                    train = null,
                    interactive = null, ),
                        permissions=runai.models.resource_permissions.ResourcePermissions(
                    users = [
                        ''
                        ],
                    groups = [
                        ''
                        ],
                    applications = [
                        ''
                        ], ),
                        resources=runai.models.assigned_resources.AssignedResources(
                    id = 1.337,
                    gpu = null,
                    cpu = null,
                    memory = null, ),
                        name='team-a',
                        node_pools_resources=[
                    null
                    ],
                        namespace='ns-proj1',
                        id=5,
                        department_id=2,
                        tenant_id=2,
                        cluster_uuid='71f69d83-ba66-4822-adf5-55ce55efd210',
                        department_name='department-a',
                        interactive_node_affinity='none',
                        train_node_affinity='none',
                        created_at='2021-12-14T16:04:15.099Z',
                        status=runai.models.project_status1.ProjectStatus1(
                    namespace = 'runai-team-a',
                    message = 'NamespaceHandlerFailed',
                    quota_statuses = [
                        runai.models.node_pool_quota_status.NodePoolQuotaStatus(
                            node_pool_name = '',
                            allocated = runai.models.quota_status_resource_list.QuotaStatusResourceList(
                                gpu = 0,
                                cpu = 1000,
                                memory = 1000, ),
                            allocated_non_preemptible = runai.models.quota_status_resource_list.QuotaStatusResourceList(
                                gpu = 0,
                                cpu = 1000,
                                memory = 1000, ),
                            requested = , )
                        ], ),
                        phase='Ready'
        )
        ```
    """  # noqa: E501

    deserved_gpus: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="Deprecated. Use 'deserved' for the relevant resource type under `NodePoolResources`. The project's deserved GPU allocation in case the cluster has those resources.",
        alias="deservedGpus",
    )
    max_allowed_gpus: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="Deprecated. Instead, use `maxAllowed` for the relevant resource type under `NodePoolResources`. An upper limit for the amount of GPUs the project can get (Even if over quota is allowed and resources are available).",
        alias="maxAllowedGpus",
    )
    gpu_over_quota_weight: Optional[
        Union[
            Annotated[float, Field(le=3, strict=True, ge=0)],
            Annotated[int, Field(le=3, strict=True, ge=0)],
        ]
    ] = Field(
        default=None,
        description="Deprecated. Instead, use `overQuotaWeight` for the relevant resource type under `NodePoolResources`. The priority the project gets for over quota resources.",
        alias="gpuOverQuotaWeight",
    )
    default_node_pools: Optional[List[StrictStr]] = Field(
        default=None,
        description="Default node pools list for workload submission for this project if a workload doesn't specify a node pools list.",
        alias="defaultNodePools",
    )
    interactive_job_time_limit_secs: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="A limit (in seconds) for the duration of interactive jobs from this project.",
        alias="interactiveJobTimeLimitSecs",
    )
    interactive_job_max_idle_duration_secs: Optional[Union[StrictFloat, StrictInt]] = (
        Field(
            default=None,
            description="Maximum duration (in seconds) that an interactive job can be idle before being terminated.",
            alias="interactiveJobMaxIdleDurationSecs",
        )
    )
    interactive_preemptible_job_max_idle_duration_secs: Optional[
        Union[StrictFloat, StrictInt]
    ] = Field(
        default=None,
        description="Maximum duration (in seconds) that an interactive preemptible job can be idle before being terminated.",
        alias="interactivePreemptibleJobMaxIdleDurationSecs",
    )
    training_job_time_limit_secs: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="A limit (in seconds) for the duration of training jobs from this project. Available only from cluster version 2.12",
        alias="trainingJobTimeLimitSecs",
    )
    training_job_max_idle_duration_secs: Optional[Union[StrictFloat, StrictInt]] = (
        Field(
            default=None,
            description="Maximum duration (in seconds) that a training job can be idle before being terminated.",
            alias="trainingJobMaxIdleDurationSecs",
        )
    )
    node_affinity: Optional[JobsNodeAffinity] = Field(
        default=None,
        description="Node affinity configuration for jobs in the project.",
        alias="nodeAffinity",
    )
    permissions: Optional[ResourcePermissions] = Field(
        default=None,
        description="Deprecated. Instead, use the `accessRules` API to add permissions to a specific subject in the project scope.",
    )
    resources: Optional[AssignedResources] = Field(
        default=None,
        description="Deprecated. Instead, use `nodePoolsResources`. Total resources assigned to the Project. Can only be used in PUT/POST when there is a single Node Pool in the system. The resources returned in `GET` are the sum of all Node Pool Resources.",
    )
    name: Optional[StrictStr] = Field(default=None, description="Project name.")
    node_pools_resources: Optional[List[NodePoolAssignedResources]] = Field(
        default=None,
        description="Resources assigned to this Project per Node Pool.",
        alias="nodePoolsResources",
    )
    namespace: Optional[StrictStr] = Field(
        default=None,
        description="The name of an existing namespace to use for the project in the cluster. Supported only for cluster versions 2.12 or higher.",
    )
    id: Optional[StrictInt] = Field(default=None, description="Project id.")
    department_id: Optional[StrictInt] = Field(
        default=None,
        description="ID of the department that owns the project.",
        alias="departmentId",
    )
    tenant_id: Optional[StrictInt] = Field(
        default=None,
        description="ID of the tenant where the project is located.",
        alias="tenantId",
    )
    cluster_uuid: Optional[StrictStr] = Field(
        default=None,
        description="ID of the cluster where the project is located.",
        alias="clusterUuid",
    )
    department_name: Optional[StrictStr] = Field(
        default=None,
        description="Name of the department where the project is located.",
        alias="departmentName",
    )
    interactive_node_affinity: Optional[StrictStr] = Field(
        default=None, alias="interactiveNodeAffinity"
    )
    train_node_affinity: Optional[StrictStr] = Field(
        default=None, alias="trainNodeAffinity"
    )
    created_at: Optional[datetime] = Field(
        default=None, description="Creation date of the project.", alias="createdAt"
    )
    status: Optional[ProjectStatus1] = None
    phase: Optional[StrictStr] = Field(default=None, description="project's phase")
    __properties: ClassVar[List[str]] = [
        "deservedGpus",
        "maxAllowedGpus",
        "gpuOverQuotaWeight",
        "defaultNodePools",
        "interactiveJobTimeLimitSecs",
        "interactiveJobMaxIdleDurationSecs",
        "interactivePreemptibleJobMaxIdleDurationSecs",
        "trainingJobTimeLimitSecs",
        "trainingJobMaxIdleDurationSecs",
        "nodeAffinity",
        "permissions",
        "resources",
        "name",
        "nodePoolsResources",
        "namespace",
        "id",
        "departmentId",
        "tenantId",
        "clusterUuid",
        "departmentName",
        "interactiveNodeAffinity",
        "trainNodeAffinity",
        "createdAt",
        "status",
        "phase",
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
        """Create an instance of Project2 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set(
            [
                "id",
            ]
        )

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of node_affinity
        if self.node_affinity:
            _dict["nodeAffinity"] = self.node_affinity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of permissions
        if self.permissions:
            _dict["permissions"] = self.permissions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of resources
        if self.resources:
            _dict["resources"] = self.resources.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in node_pools_resources (list)
        _items = []
        if self.node_pools_resources:
            for _item_node_pools_resources in self.node_pools_resources:
                if _item_node_pools_resources:
                    _items.append(_item_node_pools_resources.to_dict())
            _dict["nodePoolsResources"] = _items
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict["status"] = self.status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Project2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "deservedGpus": obj.get("deservedGpus"),
                "maxAllowedGpus": obj.get("maxAllowedGpus"),
                "gpuOverQuotaWeight": obj.get("gpuOverQuotaWeight"),
                "defaultNodePools": obj.get("defaultNodePools"),
                "interactiveJobTimeLimitSecs": obj.get("interactiveJobTimeLimitSecs"),
                "interactiveJobMaxIdleDurationSecs": obj.get(
                    "interactiveJobMaxIdleDurationSecs"
                ),
                "interactivePreemptibleJobMaxIdleDurationSecs": obj.get(
                    "interactivePreemptibleJobMaxIdleDurationSecs"
                ),
                "trainingJobTimeLimitSecs": obj.get("trainingJobTimeLimitSecs"),
                "trainingJobMaxIdleDurationSecs": obj.get(
                    "trainingJobMaxIdleDurationSecs"
                ),
                "nodeAffinity": (
                    JobsNodeAffinity.from_dict(obj["nodeAffinity"])
                    if obj.get("nodeAffinity") is not None
                    else None
                ),
                "permissions": (
                    ResourcePermissions.from_dict(obj["permissions"])
                    if obj.get("permissions") is not None
                    else None
                ),
                "resources": (
                    AssignedResources.from_dict(obj["resources"])
                    if obj.get("resources") is not None
                    else None
                ),
                "name": obj.get("name"),
                "nodePoolsResources": (
                    [
                        NodePoolAssignedResources.from_dict(_item)
                        for _item in obj["nodePoolsResources"]
                    ]
                    if obj.get("nodePoolsResources") is not None
                    else None
                ),
                "namespace": obj.get("namespace"),
                "id": obj.get("id"),
                "departmentId": obj.get("departmentId"),
                "tenantId": obj.get("tenantId"),
                "clusterUuid": obj.get("clusterUuid"),
                "departmentName": obj.get("departmentName"),
                "interactiveNodeAffinity": obj.get("interactiveNodeAffinity"),
                "trainNodeAffinity": obj.get("trainNodeAffinity"),
                "createdAt": obj.get("createdAt"),
                "status": (
                    ProjectStatus1.from_dict(obj["status"])
                    if obj.get("status") is not None
                    else None
                ),
                "phase": obj.get("phase"),
            }
        )
        return _obj
