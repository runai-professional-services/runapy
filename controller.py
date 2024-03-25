import abc
from typing import Any

import errors

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

    def _filter_by_kwargs(self, data, **kwargs: Any):
        if kwargs:
            for key, value in kwargs.items():
                data = [x for x in data if getattr(x, key) == value]
        return data

    def filter(self, **kwargs: Any):
        return self._filter_by_kwargs(self.all(), **kwargs)

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
                }[key]
                return controller(klass, client, instance)
        except KeyError:
            errors.RunaiError

class NodePoolController(Controller):
    def all(self):
        cluster_id = "b1575f57-676a-4a75-a133-641fc6e7c896"
        path = f"/v1/k8s/clusters/{cluster_id}/node_pools"

        return self.client._get(path)

    def all_metrics(self):
        path = "/v1/k8s/clusters"

        return self.client._get(path)

    def get(self, department_id: str):
        cluster_id = "b1575f57-676a-4a75-a133-641fc6e7c896"
        path = f"/v1/k8s/clusters/{cluster_id}/departments/{department_id}"

        return self.client._get(path)
        #TODO: Add error catch and parameter validation
    
    def update(self, id: str):
        return errors.RunaiNotImplementedError
    
    def delete(self, id: str):
        return errors.RunaiNotImplementedError
    


class ProjectController(Controller):
    def all(self, cluster_id=None):
        # Project endpoint is being called directly by the RunaiClient
        if cluster_id:
            client = self.client
            department_id = None
        # Called by parent client Department 
        if not cluster_id:
            if self.client.__class__.__name__ == "Department":
                department_id = self.client.id
                cluster_id = self.client.clusterUuid
                client = self.client.client

        path = f"/v1/k8s/clusters/{cluster_id}/projects"
        resp = client._get(path)

        projects = []
        for project_data in resp:
            if department_id is not None:
                p_id = project_data["departmentId"]
                if project_data["departmentId"] == department_id:
                    projects.append(self.klass.from_dict(project_data))
            else:
                projects.append(self.klass.from_dict(project_data))

        for project in projects:
            project.client = client
        
        return projects

    def all_metrics(self):
        path = "/v1/k8s/clusters"

        return self.client._get(path)
    
    def create(self, data: object):
        path = f"v1/k8s/clusters/{cluster_id}/projects"
        cluster_id = "b1575f57-676a-4a75-a133-641fc6e7c896"
        return self.client._post(path, data)

    def get(self, project_id: int):
        # Project endpoint is being called directly by the RunaiClient
        # if project_id:
        #     client = self.client
        #     department_id = None
        # Called by parent client Department 
        if self.client.__class__.__name__ == "Department":
            cluster_id = self.client.clusterUuid
            client = self.client.client

        path = f"/v1/k8s/clusters/{cluster_id}/projects"
        cluster_id = "b1575f57-676a-4a75-a133-641fc6e7c896"        

        return client._get(path)
        #TODO: Add error catch and parameter validation
    
    def update(self, id: str):
        return errors.RunaiNotImplementedError
    
    def delete(self, id: str):
        return errors.RunaiNotImplementedError

class DepartmentController(Controller):
    def all(self):
        path = f"/v1/k8s/clusters/{self.client.uuid}/departments"
        client = self.client.client

        resp = client._get(path)
        departments = []
        print(resp)

        for department_data in resp:
            print(F"DEPARTMENT DATA: {department_data}")
            departments.append(self.klass.from_dict(department_data))
        for department in departments:
            department.client = client
        
        return departments

    def all_metrics(self):
        path = "/v1/k8s/clusters"

        return self.client._get(path)

    def get(self, department_id: str):
        cluster_id = "b1575f57-676a-4a75-a133-641fc6e7c896"
        path = f"/v1/k8s/clusters/{cluster_id}/departments/{department_id}"

        return self.client._get(path)
        #TODO: Add error catch and parameter validation
    
    def update(self, id: str):
        return errors.RunaiNotImplementedError
    
    def delete(self, id: str):
        return errors.RunaiNotImplementedError

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
        #TODO: Add error catch and parameter validation
    
    def update(self):
        return errors.RunaiNotImplementedError
    
    def delete(self):
        return errors.RunaiNotImplementedError