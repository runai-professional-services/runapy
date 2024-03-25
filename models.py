from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin
from typing import Optional

import errors
from controller import *

    
@dataclass
class NodePool(DataClassJsonMixin):
    
    @property
    def all(self):
        pass

@dataclass
class Project(DataClassJsonMixin):
    id: int
    name: str
    # nodePoolsResources: list[object]

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

    # def move(self, department_id: int) -> bool:
    #     path = ""

    #     return bool(self.client.move(path, department_id))
    
    # def change_quota(self, quota: int) -> bool:
    #     path = ""

    #     return bool(self.client.put(path, quota))


@dataclass
class Department(DataClassJsonMixin):
    id: int
    name: str
    clusterUuid: str
    tenantId: int
    createdAt: str
    nodePoolsResources: Optional[list[object]] # TODO: Convert to proper node pool object
    projects: Optional[list[Project]]
    
    @property
    def all_metrics(self):
        path = "/v1/k8s/departments"

        return self.client.get(path)
    
    @property
    def get(self, id: str):
        path = f"/v1/k8s/departments/{id}"

        return self.client.get(path)
        #TODO: Add error catch and parameter validation
    
    @property
    def get_metrics(self, id: str):
        path = f"/v1/k8s/departments/{id}"

        return self.client.get(path)
        #TODO: Add error catch and parameter validation
    
    # TODO: Create method should be on DepartmentController and not on existing object
    @property
    def create(self, id: str):
        return errors.RunaiNotImplementedError
    
    @property
    def update(self, id: str):
        return errors.RunaiNotImplementedError
    
    @property
    def delete(self, id: str):
        return errors.RunaiNotImplementedError
    
    # TODO: The code currently crashes as the projects nodePoolsResources are not returned to departments.all()
    # TODO: Need to build the projects list when calling departments
    @property
    def projects(self) -> Controller:
        return Controller.factory(Project, self)
    
    @projects.setter
    def projects(self, projects) -> list[Controller]:
        p = []
        for project in projects:
             p.append(Controller.factory(klass=Project, client=self, instance=project))
        return p

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
    
    @property
    def departments(self) -> Controller:
        return Controller.factory(Department, self)