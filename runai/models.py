from typing import Optional, List, Literal
from enum import StrEnum

import pydantic
from pydantic import BaseModel

from . import errors


class ResourcesPlacementStrategy(BaseModel):
    cpu: Literal["spread", "binpack"]
    gpu: Literal["spread", "binpack"]


class NodePoolLabels(BaseModel):
    labelKey: str
    labelValue: str


class NodePool(BaseModel):
    id: int
    name: str
    labelKey: str
    labelValue: str
    placementStrategy: ResourcesPlacementStrategy
    overProvisioningRatio: Optional[int] = 1


class NodePoolUpdateRequest(BaseModel):
    labelKey: str
    labelValue: str
    placementStrategy: ResourcesPlacementStrategy
    overProvisioningRatio: Optional[int] = 1


class NodePoolCreateRequest(BaseModel):
    name: str
    labelKey: str
    labelValue: str
    placementStrategy: ResourcesPlacementStrategy
    overProvisioningRatio: Optional[int] = 1


class Resource(BaseModel):
    deserved: int
    limit: int
    overQuotaWeight: int


class Memory(Resource):
    units: Literal["Mib", "MB", "GB"]


class NodeTypes(BaseModel):
    """
    training : Optional[List[str]]
    workspace: Optional[List[str]]
    """
    training: Optional[List[str]] = None
    workspace: Optional[List[str]] = None


class SchedulingRules(BaseModel):
    """
    Scheduling rules to be applied on all workloads within the project

    interactiveJobTimeLimitSeconds: Optional[int] = None
    interactiveJobMaxIdleDurationSeconds: Optional[int] = None
    interactiveJobPreemptIdleDurationSeconds: Optional[int] = None
    trainingJobTimeLimitSeconds: Optional[int] = None
    trainingJobMaxIdleDurationSeconds: Optional[int] = None
    """
    interactiveJobTimeLimitSeconds: Optional[int] = None
    interactiveJobMaxIdleDurationSeconds: Optional[int] = None
    interactiveJobPreemptIdleDurationSeconds: Optional[int] = None
    trainingJobTimeLimitSeconds: Optional[int] = None
    trainingJobMaxIdleDurationSeconds: Optional[int] = None


class NodePoolIdentifier(BaseModel):
    id: str
    name: str


class Resources(BaseModel):
    """
    Set the gpu, cpu, and memory resources for a given nodepool.
    CPU/Memory may not work if your organization does not permit assiging these resources

    "nodePool": {
        id: str
        name: str
    },
    "gpu": {
        deserved: int
        limit: int
        overQuotaWeight: int
    },
    "cpu": {
        "deserved": int,
        "limit": int,
        "overQuotaWeight": int
    },
        "memory": {
            "deserved": int,
            "limit": int,
            "overQuotaWeight": int,
            "units": "Mib" or "GB" or "MB,
    }

    Example:
    {
        {
            "nodePool": {
            "id": 22,
            "name": "default"
        },
            "gpu": {
            "deserved": 1000,
            "limit": 0,
            "overQuotaWeight": 2
        },
            "cpu": {
            "deserved": 1000,
            "limit": 0,
            "overQuotaWeight": 2
        },
            "memory": {
            "deserved": 1000,
            "limit": 0,
            "overQuotaWeight": 2,
            "units": "Mib"
        }
}
    }
    """
    nodePool: NodePoolIdentifier
    gpu: Resource
    cpu: Optional[Resource] = None
    memory: Optional[Memory] = None


class ProjectUpdateRequest(BaseModel):
    resources: List[Resources]
    nodeTypes: Optional[NodeTypes] = None
    defaultNodePools: Optional[List[str]] = None
    schedulingRules: Optional[SchedulingRules] = None


class ProjectCreateRequest(BaseModel):
    name: str
    clusterId: str
    resources: List[Resources]
    nodeTypes: Optional[NodeTypes] = None
    defaultNodePools: Optional[List[str]] = None
    schedulingRules: Optional[SchedulingRules] = None
    requestedNamespace: Optional[str] = None
    parentId: Optional[str] = None


class DepartmentCreateRequest(BaseModel):
    name: str
    clusterId: str
    resources: List[Resources]


class UserCreateRequest(BaseModel):
    email: str
    resetPassword: Optional[bool] = False


class AccessRule(BaseModel):
    subjectId: str
    subjectType: Literal["user", "app", "group"]
    roleId: int
    scopeId: str
    scopeType: Literal["system", "tenant", "cluster", "department", "project"]
    clusterId: str


def build_model(model: BaseModel, data: dict) -> BaseModel:
    try:
        built_model = model(**data)
        return built_model
    except pydantic.ValidationError as e:
        raise errors.RunaiBuildModelError(err=e)


class SortOrderEnum(StrEnum):
    asc = "asc"
    desc = "desc"


class ProjectSortByEnum(StrEnum):
    name = "name"
    clusterId = "clusterId"
    departmentId = "departmentId"
    createdAt = "createdAt"


class ProjectQueryParams(BaseModel):
    filterBy: Optional[str] = None
    sortBy: Optional[ProjectSortByEnum] = None
    sortOrder: Optional[Literal["asc", "desc"]] = None
    offset: Optional[int] = None
    limit: Optional[int] = None


class DepartmentSortByEnum(StrEnum):
    name = "name"
    clusterId = "clusterId"
    createdAt = "createdAt"


class DepartmentQueryParams(BaseModel):
    filterBy: Optional[str] = None
    sortBy: Optional[Literal["name", "clusterId", "createdAt"]] = None
    sortOrder: Optional[Literal["asc", "desc"]] = None
    offset: Optional[int] = None
    limit: Optional[int] = None


class NodePoolsQueryParams(BaseModel):
    start: str
    end: str
    metricType: Literal["GPU_UTILIZATION", "GPU_MEMORY_UTILIZATION", "CPU_UTILIZATION", "CPU_MEMORY_UTILIZATION", "TOTAL_GPU", "GPU_QUOTA", "ALLOCATED_GPU", "AVG_WORKLOAD_WAIT_TIME"]
    numberOfSamples: Optional[int] = 20


class AccessRulesSortByEnum(StrEnum):
    subjectId = "subjectId"
    subjectType = "subjectType"
    roleId = "roleId"
    scopeId = "scopeId"
    scopeType = "scopeType"
    roleName = "roleName"
    scopeName = "scopeName"
    createdAt = "createdAt"
    deletedAt = "deletedAt"
    createdBy = "createdBy"


class AccessRulesQueryParams(BaseModel):
    subjectType: Optional[str] = None
    subjectIds: Optional[List[str]] = None
    limit: Optional[int] = None
    offset: Optional[int] = None
    lastUpdated: Optional[str] = None
    includeDeleted: Optional[bool] = None
    clusterId: Optional[str] = None
    scopeId: Optional[str] = None
    filterBy: Optional[str] = None
    sortBy: Optional[AccessRulesSortByEnum] = None
    sortOrder: Optional[SortOrderEnum] = "asc"


class ClusterQueryParams(BaseModel):
    verbosity: Optional[Literal["full", "metadata"]] = "full"


def build_query_params(query_model: BaseModel, params: dict) -> BaseModel:
    try:
        built_model = query_model(**params)
        return built_model
    except pydantic.ValidationError as e:
        raise errors.RunaiQueryParamsError(err=e)
