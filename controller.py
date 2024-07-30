import abc
import json
from typing import Any, Optional, List, Dict

import errors
import models
from models import build_model

class Controller(abc.ABC):
    def __init__(self, klass, client, instance=None):
        self.klass = klass
        self.client = client
        self.instance = instance

    @abc.abstractmethod
    def all(self):
        pass

    def get(self, id: str):
        try:
            return next(x for x in self.all() if x.id == id)
        except StopIteration:
            raise errors.RunaiNotFoundError
        
    def first(self):
        try:
            return self.all()[0]
        except IndexError:
            raise errors.RunaiNotFoundError

    # def _filter_by_kwargs(self, data, **kwargs: Any):
    #     if kwargs:
    #         for key, value in kwargs.items():
    #             data = [x for x in data if getattr(x, key) == value]
    #     return data

    # def filter(self, **kwargs: Any):
    #     return self._filter_by_kwargs(self.all(), **kwargs)
    def filter(self, data, **kwargs: Any):
        if kwargs:
            for key, value in kwargs.items():
                data = [x for x in data if x.get(key) == value]
                #Unpack list
                data = data[0]
        return data

    @staticmethod
    def factory(klass, client, instance=None):
        try:
            if isinstance(klass, str):
                key = klass
            else:
                key = klass.__name__
                controller = {
                    "Cluster": ClusterController,
                    "Department": DepartmentController,
                    "Project": ProjectController,
                    "NodePool": NodePoolController,
                    # "Roles": RoleController,
                    # "AccessRules": AccessRuleController,
                    # "Users": UserController,
                }[key]
                return controller(klass, client, instance)
        except KeyError:
            errors.RunaiError

class NodePoolController(Controller):
    def all(self) -> List:
        path = f"/v1/k8s/clusters/{self.client.cluster_id}/node-pools"
        
        return self.client._get(path)
    
    def get(self, nodepool_name: str):
        node_pools = self.all()
        node_pool = self.filter(node_pools, name=nodepool_name)

        return node_pool

    def node_pool_metrics(self, nodepool_name: str):
        path = f"/v1/k8s/clusters/{self.client.cluster_id}/node-pools/{nodepool_name}"

        return self.client._get(path)
    
    def create(self, name: str, labelKey: str, labelValue: str, placementStrategy: models.PlacementStrategy, overProvisioningRatio: Optional[int] = 1):
        path = f"/v1/k8s/clusters/{self.client.cluster_id}/node-pools"

        data = {
            "name": name,
            "labelKey": labelKey,
            "labelValue": labelValue,
            "placementStrategy": placementStrategy,
            "overProvisioningRatio": overProvisioningRatio

        }

        node_pool = build_model(models.NodePoolCreateRequest, data)
        payload = node_pool.model_dump_json()
        
        return self.client._post(path, payload)
    
    def update(self,nodepool_id: int, **kwargs):
        """
        Used to update node pool fields that are not labels
        For labels, please use update_labels method
        """
        path = f"/v1/k8s/clusters/{self.client.cluster_id}/node-pools/{nodepool_id}"
        model_fields = [field for field in models.NodePoolRequest.model_fields]
        
        options = {}
        for key, value in kwargs.items():
            if key not in model_fields:
                raise ValueError(f"Field does not exist: {key}")
            options[key]=value
        
        return self.client._put(path, options)
    
    def update_labels(self,nodepool_id: int, labelKey: str, labelValue: str):
        path = f"/v1/k8s/clusters/{self.client.cluster_id}/node-pools/{nodepool_id}/labels"
        options = {
            "labelKey": labelKey,
            "labelValue": labelValue
        }
        payload = json.dumps(options)
        return self.client._put(path, payload)
    
    def delete(self, nodepool_id: int):
        path = f"/v1/k8s/clusters/{self.client.cluster_id}/node-pools/{nodepool_id}"

        resp = self.client._delete(path)
        return resp
    


class ProjectController(Controller):
    def all(self):
        # TODO: Pass query parameters instead of hardcoded filterBy
        path = f"/api/v1/org-unit/projects?filterBy=clusterId=={self.client.cluster_id}"
        # path = f"/v1/k8s/clusters/{self.client.cluster_id}/projects"
        resp = self.client._get(path)

        projects = resp["projects"]
        # projects = []
        # for project_data in resp:
        #     projects.append(self.klass.from_dict(project_data))

        # for project in projects:
        #     project.client = self.client
        
        return projects

    def test(self):
        path = "/api/v1/org-unit/node-type"
        return self.client._get(path)

    def all_metrics(self):
        path = "/v1/k8s/clusters"

        return self.client._get(path)
    
    def create(self, 
               name: str, 
               requestedNamespace: str, 
               nodeTypes:models.NodeTypes,
               resources:models.Resources,
               parentId:Optional[str],
               defaultNodePools:Optional[List[str]],
               schedulingRules:Optional[models.SchedulingRules]
               ):
        path = f"v1/k8s/clusters/{self.client.cluster_id}/projects"

        payload={}
        return self.client._post(path, payload)

    def get(self, project_id: int):
        # Project endpoint is being called directly by the RunaiClient
        # if project_id:
        #     client = self.client
        #     department_id = None
        # Called by parent client Department 
        if self.client.__class__.__name__ == "Department":
            cluster_id = self.client.clusterUuid
            client = self.client.client

        path = f"/v1/k8s/clusters/{cluster_id}/projects/{project_id}"      

        return client._get(path)
        #TODO: Add error catch and parameter validation
    
    def update(self, id: str):
        return errors.RunaiNotImplementedError
    
    def delete(self, id: str):
        return errors.RunaiNotImplementedError

class DepartmentController(Controller):
    def all(self):
        # path = f"/v1/k8s/clusters/{self.client.uuid}/departments"
        # TODO: Pass query parameters instead of hardcoded filterBy
        path = f"/api/v1/org-unit/departments?filterBy=clusterId=={self.client.cluster_id}"
        client = self.client

        resp = client._get(path)

        departments = resp["departments"]
        # departments = []
        # for department_data in resp:
        #     departments.append(self.klass.from_dict(department_data))
        # for department in departments:
        #     department.client = client
        
        return departments

    def all_metrics(self):
        path = "/v1/k8s/clusters"

        return self.client._get(path)

    def create(self, name: str, resources:models.Resources):
        path = f"/api/v1/org-unit/departments"
        data = {
            "name": name,
            "resources": resources,
            "clusterId": self.client.cluster_id
        }
        department = build_model(models.DepartmentCreateRequest, data=data)
        payload = department.model_dump_json()

        return self.client._post(path, payload)

    def get(self, department_id: int):
        path = f"/api/v1/org-unit/departments/{department_id}"

        return self.client._get(path)
    
    def update_resources(self, department_id: str,  resources: List[models.Resources]):
        path = f"/api/v1/org-unit/departments/{department_id}/resources"

        payload = []
        for resource in resources:
            resource = build_model(models.Resources, resource)
            payload.append(resource.model_dump())
        
        return self.client._put(path, payload)
    
    def delete(self, department_id: int):
        path = f"/api/v1/org-unit/departments/{department_id}"
        return self.client._delete(path)

# class UserController(Controller):
#     def all(self):
#         path = "/api/v1/users"

#         resp = self.client._get(path)

#         users = []
#         for data in resp:
#             users.append({"id": data["id"], "username": data["username"]})
#         return users

# class RoleController(Controller):
#     def all(self):
#         path = "/api/v1/authorization/roles"

#         resp = self.client._get(path)

#         return resp

# class AccessRuleController(Controller):
#     def all(self):
#         path = "/api/v1/authorization/access-rules"

#         resp = self.client._get(path)

#         return resp
    
#     def create(self):
#         path = "/api/v1/authorization/access-rules"



class ClusterController(Controller):
    def all(self):
        path = "/v1/k8s/clusters"

        resp = self.client._get(path)

        clusters = []        
        for cluster_data in resp:
            clusters.append(self.klass.from_dict(cluster_data))
        for cluster in clusters:
            cluster.client = self.client
        return clusters
    
    def get(self, id: str):
        path = f"/v1/k8s/clusters/{id}"

        return self.client._get(path)
    
    def update(self):
        return errors.RunaiNotImplementedError
    
    def delete(self):
        return errors.RunaiNotImplementedError