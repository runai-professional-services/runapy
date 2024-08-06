import abc
import json

from typing import Any, Optional, List, Literal

from . import errors
from . import models


class Controller(abc.ABC):
    def __init__(self, client):
        self.client = client

    def _filter(self, data, **kwargs: Any):
        if kwargs:
            for key, value in kwargs.items():
                data = [x for x in data if x.get(key) == value]
                # Unpack list
                data = data[0]
        return data


class NodePoolController(Controller):
    def __init__(self, client):
        super().__init__(client)

    def all(self) -> List:
        path = f"/v1/k8s/clusters/{self.client.cluster_id}/node-pools"

        return self.client.get(path)

    def get(self, nodepool_name: str):
        node_pools = self.all()
        node_pool = self._filter(node_pools, name=nodepool_name)

        return node_pool

    def node_pool_metrics(self, nodepool_name: str):
        path = f"/v1/k8s/clusters/{self.client.cluster_id}/node-pools/{nodepool_name}"

        return self.client.get(path)

    def create(
        self,
        name: str,
        label_key: str,
        label_value: str,
        placement_strategy: models.PlacementStrategy,
        over_provisioning_ratio: Optional[int] = 1,
    ):
        path = f"/v1/k8s/clusters/{self.client.cluster_id}/node-pools"

        data = {
            "name": name,
            "labelKey": label_key,
            "labelValue": label_value,
            "placementStrategy": placement_strategy,
            "overProvisioningRatio": over_provisioning_ratio,
        }

        node_pool = models.build_model(models.NodePoolCreateRequest, data)
        payload = node_pool.model_dump_json()

        return self.client.post(path, payload)

    def update(self, nodepool_id: int, **kwargs):
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
            options[key] = value

        return self.client.put(path, options)

    def update_labels(self, nodepool_id: int, label_key: str, label_value: str):
        path = f"/v1/k8s/clusters/{self.client.cluster_id}/node-pools/{nodepool_id}/labels"

        options = {"labelKey": label_key, "labelValue": label_value}
        payload = json.dumps(options)

        return self.client.put(path, payload)

    def delete(self, nodepool_id: int):
        path = f"/v1/k8s/clusters/{self.client.cluster_id}/node-pools/{nodepool_id}"

        resp = self.client.delete(path)
        return resp


class ProjectController(Controller):
    def __init__(self, client):
        super().__init__(client)

    def all(self):
        # TODO: Pass query parameters instead of hardcoded filterBy
        path = f"/api/v1/org-unit/projects?filterBy=clusterId=={self.client.cluster_id}"

        resp = self.client.get(path)
        projects = resp["projects"]

        return projects

    def create(
        self,
        name: str,
        resources: List[models.Resources],
        requested_namespace: Optional[str] = None,
        default_node_pools: Optional[List[str]] = None,
        scheduling_rules: Optional[models.SchedulingRules] = None,
        parent_id: Optional[str] = None,
        node_types: Optional[models.NodeTypes] = None,
    ):
        path = "/api/v1/org-unit/projects"

        data = {
            "name": name,
            "resources": resources,
            "clusterId": self.client.cluster_id,
            "requestedNamespace": requested_namespace,
            "defaultNodePools": default_node_pools,
            "schedulingRules": scheduling_rules,
            "parentId": parent_id,
            "nodeTypes": node_types,
        }

        project = models.build_model(model=models.ProjectCreateRequest, data=data)
        payload = project.model_dump_json()

        return self.client.post(path, payload)

    def get(self, project_id: int):
        path = f"/api/v1/org-unit/projects/{project_id}"

        return self.client.get(path)

    def update(
        self,
        project_id: int,
        resources: List[models.Resources],
        default_node_pools: Optional[List[str]] = None,
        node_types: Optional[models.NodeTypes] = None,
        scheduling_rules: Optional[models.SchedulingRules] = None,
    ):
        path = f"/api/v1/org-unit/projects/{project_id}"

        existing_project = self.get(project_id=project_id)

        scheduling_rules = scheduling_rules or existing_project["schedulingRules"] or None
        default_node_pools = default_node_pools or existing_project["defaultNodePools"] or None
        node_types = node_types or existing_project["nodeTypes"]

        data = {
            "resources": resources,
            "schedulingRules": scheduling_rules,
            "defaultNodePools": default_node_pools,
            "nodeTypes": node_types,
        }

        model = models.build_model(model=models.ProjectUpdateRequest, data=data)
        payload = model.model_dump_json()

        return self.client.put(path, payload)

    def delete(self, project_id: int):
        path = f"/api/v1/org-unit/projects/{project_id}"

        return self.client.delete(path)


class DepartmentController(Controller):
    def __init__(self, client):
        super().__init__(client)

    def all(self):
        # path = f"/v1/k8s/clusters/{self.client.uuid}/departments"
        # TODO: Pass query parameters instead of hardcoded filterBy
        path = (
            f"/api/v1/org-unit/departments?filterBy=clusterId=={self.client.cluster_id}"
        )

        resp = self.client.get(path)
        departments = resp["departments"]

        return departments

    def all_metrics(self):
        path = "/v1/k8s/clusters"

        return self.client.get(path)

    def create(self, name: str, resources: models.Resources):
        path = "/api/v1/org-unit/departments"

        data = {
            "name": name,
            "resources": resources,
            "clusterId": self.client.cluster_id,
        }
        department = models.build_model(model=models.DepartmentCreateRequest, data=data)
        payload = department.model_dump_json()

        return self.client.post(path, payload)

    def get(self, department_id: int):
        path = f"/api/v1/org-unit/departments/{department_id}"

        return self.client.get(path)

    def update_resources(self, department_id: str, resources: List[models.Resources]):
        path = f"/api/v1/org-unit/departments/{department_id}/resources"

        payload = []
        for resource in resources:
            resource = models.build_model(models.Resources, resource)
            payload.append(resource.model_dump())

        return self.client.put(path, payload)

    def delete(self, department_id: int):
        path = f"/api/v1/org-unit/departments/{department_id}"

        return self.client.delete(path)


class AccessRulesController(Controller):
    def __init__(self, client):
        super().__init__(client)

    def all(self):
        path = "/api/v1/authorization/access-rules"

        return self.client.get(path)

    def create(self,
               subject_id: str,
               subject_type: Literal["user", "app", "group"],
               role_id: int,
               scope_id: str,
               scope_type: Literal["system", "tenant", "cluster", "department", "project"]
               ):
        path = "/api/v1/authorization/access-rules"

        data = {
                "subjectId": subject_id,
                "subjectType": subject_type,
                "roleId": role_id,
                "scopeId": scope_id,
                "scopeType": scope_type,
                "clusterId": self.client.cluster_id
                }
        access_rule = models.build_model(models.AccessRule, data)
        payload = access_rule.model_dump_json()

        return self.client.post(path, payload)


class RolesController(Controller):
    def __init__(self, client):
        super().__init__(client)

    def all(self):
        path = "/api/v1/authorization/roles"

        return self.client.get(path)

    def get(self, role_id: int):
        path = f"/api/v1/authorization/roles/{role_id}"

        return self.client.get(path)

    def get_roles_name_to_id_map(self) -> dict:
        path = "/api/v1/authorization/roles"

        roles = self.client.get(path)

        m = {}
        for role in roles:
            m[role["name"]] = role["id"]

        return m


class ClusterController(Controller):
    def __init__(self, client):
        super().__init__(client)

    def all(self):
        path = "/v1/k8s/clusters"

        resp = self.client.get(path)

        clusters = []
        for cluster_data in resp:
            clusters.append(self.klass.from_dict(cluster_data))
        for cluster in clusters:
            cluster.client = self.client
        return clusters

    def get(self, id: str):
        path = f"/v1/k8s/clusters/{id}"

        return self.client.get(path)

    def update(self):
        return errors.RunaiNotImplementedError

    def delete(self):
        return errors.RunaiNotImplementedError
