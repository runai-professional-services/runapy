from typing import Optional, List, Literal, Type, Any

import pydantic
from pydantic import BaseModel, ValidationError


class PlacementStrategy(BaseModel):
    cpu: Literal["spread", "binpack"]
    gpu: Literal["spread", "binpack"]


class NodePool(BaseModel):
    id: int
    name: str
    labelKey: str
    labelValue: str
    placementStrategy: PlacementStrategy
    overProvisioningRatio: Optional[int] = 1


class NodePoolCreateRequest(BaseModel):
    name: str
    labelKey: str
    labelValue: str
    placementStrategy: PlacementStrategy
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
    Object:
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
    parentId: Optional[str] = None  # TODO: change to uuid type


class DepartmentCreateRequest(BaseModel):
    name: str
    clusterId: str
    resources: List[Resources]

# @dataclass
# class Authorization(BaseModel):
#     @property
#     def users(self) -> Controller:
#         return Controller.factory("Users", self)


class Cluster(BaseModel):
    tenantId: int
    uuid: str
    name: str
    domain: str
    # description: str # TODO: Remove field as it causes an error
    version: str
    createdAt: str
    # connected: bool # TODO: Remove field as it causes an error
    status: object


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
        raise ValueError(f"Failed to build payload: {e}")
