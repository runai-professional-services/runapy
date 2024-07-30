import datetime

from typing import Optional, List, Literal

import pydantic
from pydantic import BaseModel
from dataclasses import dataclass, field
from dataclasses_json import DataClassJsonMixin

@dataclass
class PlacementStrategy:
    cpu: Literal["spread","binpack"]
    gpu: Literal["spread","binpack"]

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

@dataclass
class NodeTypes(BaseModel):
    """
    training : List[str]
    workspace: List[str]
    """
    training: List[str]
    workspace: List[str]
    
@dataclass
class SchedulingRules(BaseModel):
    interactiveJobTimeLimitSecs: Optional[int] = None
    interactiveJobMaxIdleDurationSecs: Optional[int] = None
    interactivePreemptibleJobMaxIdleDurationSecs: Optional[int] = None
    trainingJobTimeLimitSecs: Optional[int] = None
    trainingJobMaxIdleDurationSecs: Optional[int] = None

@dataclass
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
    nodePool:
    gpu: str
    """
    nodePool: NodePoolIdentifier
    gpu: Resource
    cpu: Optional[Resource]
    memory: Optional[Memory]

@dataclass
class ProjectRequest(BaseModel):
    name: str
    clusterId: str #TODO: change to uuid type
    requestedNamespace: str
    nodeTypes: NodeTypes
    resources: List[Resources]
    parentId: Optional[str] #TODO: change to uuid type
    defaultNodePools: Optional[List[str]]
    schedulingRules: Optional[SchedulingRules]

@dataclass
class Project(DataClassJsonMixin):
    id: int
    name: str
    interactiveJobTimeLimitSecs: Optional[int] = None
    interactiveJobMaxIdleDurationSecs: Optional[int] = None
    interactivePreemptibleJobMaxIdleDurationSecs: Optional[int] = None
    trainingJobTimeLimitSecs: Optional[int] = None
    trainingJobMaxIdleDurationSecs: Optional[int] = None
    permissions: Optional[object] = None
    # nodeAffinity: Optional[object]
    # nodePoolsResources: list[object]
    # defaultNodePools: list[object]
    
    # Metadata
    # tenantId: Optional[int]
    # departmentId: Optional[int]
    # departmentName: Optional[str]
    # clusterUuid: Optional[str]
    # createdAt: Optional[str]
    # status: Optional[object]

    @property
    def all(self):
        pass
    
    @property
    def get(self):
        pass

    def delete(self) -> bool:
        path = ""

        return bool(self.client.delete(path))
    
    def create(self) -> object:
        return
    
    def edit(self) -> object:
        return self
    
    # def change_quota(self, quota: int) -> bool:
    #     path = ""

    #     return bool(self.client.put(path, quota))

class DepartmentCreateRequest(BaseModel):
    name: str
    clusterId: str
    resources: List[Resources]


@dataclass
class AggregatedResources:
    nodePool: NodePool
    gpu: Resource
    cpu: Resource
    memory: Resource

@dataclass
class OLDDepartmentCreateRequest:
    name: str
    clusterId: str
    resources: List[AggregatedResources]

@dataclass
class DepartmentStatus:
    allocated: Resource
    allocatedNonPreemptible: Resource
    requested: Resource
    nodePoolName: str
    nodePoolId: str

@dataclass
class QuotaStatus:
    allocated: Resource
    allocatedNonPreemptible: Resource
    requested: Resource

@dataclass
class Department(DataClassJsonMixin):
    # id: int
    # name: str
    # clusterUuid: str
    # tenantId: int
    # createdAt: str
    # nodePoolsResources: Optional[list[object]] # TODO: Convert to proper node pool object
    # projects: Optional[list[Project]] #TODO: Convert to computed field
    id: int
    name: str
    clusterId: str
    createdAt: datetime.datetime
    updatedAt: datetime.datetime
    createdBy: str
    updatedBy: str
    resources: List[AggregatedResources]
    children: List['Department'] = field(default_factory=list)
    projectsAggregatedResources: List[AggregatedResources] = field(default_factory=list)
    status: Optional[DepartmentStatus] = None
    
    # @property
    # def all_metrics(self):
    #     path = "/v1/k8s/departments"

    #     return self.client.get(path)
    
    # @property
    # def get(self, id: str):
    #     path = f"/v1/k8s/departments/{id}"

    #     return self.client.get(path)
    #     #TODO: Add error catch and parameter validation
    
    # @property
    # def get_metrics(self, id: str):
    #     path = f"/v1/k8s/departments/{id}"

    #     return self.client.get(path)
    #     #TODO: Add error catch and parameter validation
    
    # # TODO: Create method should be on DepartmentController and not on existing object
    # @property
    # def create(self, id: str):
    #     return errors.RunaiNotImplementedError
    
    # @property
    # def update(self, id: str):
    #     return errors.RunaiNotImplementedError
    
    # @property
    # def delete(self, id: str):
    #     return errors.RunaiNotImplementedError
    
    # # TODO: The code currently crashes as the projects nodePoolsResources are not returned to departments.all()
    # # TODO: Need to build the projects list when calling departments
    # @property
    # def projects(self) -> Controller:
    #     return Controller.factory(Project, self)
    
    # @projects.setter
    # def projects(self, projects) -> list[Controller]:
    #     projects_list = []
    #     for project in projects:
    #          project_controller = Controller.factory(klass=Project, client=self, instance=project)
    #          print(f"PROJECT_CONTROLLER: {dir(project_controller)}")
    #          print(f"PROJECT_CONTROLLER: {project_controller.client.projects.get(project.id)}")
    #          print(f"PROJECT_CONTROLLER: {dir(project_controller.all())}")
    #          project_controller.instance = project_controller.get(project_controller.client.id)
    #          projects_list.append(project_controller)
    #     return projects_list


# @dataclass
# class Authorization(DataClassJsonMixin):
#     @property
#     def users(self) -> Controller:
#         return Controller.factory("Users", self)

@dataclass
class Cluster(DataClassJsonMixin):
    tenantId: int
    uuid: str
    name: str
    domain: str
    # description: str # TODO: Remove field as it causes an error
    version: str
    createdAt: str
    # connected: bool # TODO: Remove field as it causes an error
    status: object


def build_model(model: BaseModel, data: dict) -> BaseModel:
    try:
        built_model = model(**data)
        return built_model
    except pydantic.ValidationError as e:
        raise ValueError(f"Failed to build payload: {e}")