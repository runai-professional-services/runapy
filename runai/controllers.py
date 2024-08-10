import abc
import json
import inspect

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

    def options(self) -> List[str]:
        """
        Returns a list of all class methods for the current controller.
        """
        return [name for name, _
                in inspect.getmembers(self, predicate=inspect.ismethod) 
                if not name.startswith('_')
                if not name.__contains__("options")]


class NodePoolController(Controller):
    def __init__(self, client):
        super().__init__(client)

    def all(self) -> List:
        path = f"/v1/k8s/clusters/{self.client.cluster_id}/node-pools"

        return self.client.get(path)

    def get_by_name(self, nodepool_name: str):
        node_pools = self.all()
        node_pool = self._filter(node_pools, name=nodepool_name)

        return node_pool

    def node_pool_metrics(self,
                          nodepool_name: str,
                          start: str,
                          end: str,
                          metric_type: Literal["GPU_UTILIZATION",
                                               "GPU_MEMORY_UTILIZATION",
                                               "CPU_UTILIZATION",
                                               "CPU_MEMORY_UTILIZATION",
                                               "TOTAL_GPU", "GPU_QUOTA",
                                               "ALLOCATED_GPU",
                                               "AVG_WORKLOAD_WAIT_TIME"],
                          number_of_samples: Optional[int] = 20
                          ) -> dict:
        path = f"/api/v1/clusters/{self.client.cluster_id}/nodepools/{nodepool_name}/metrics"

        params = {
            "start": start,
            "end": end,
            "metricType": metric_type,
            "numberOfSamples": number_of_samples
            }

        query_params = models.build_query_params(
            query_model=models.NodePoolsQueryParams, params=params
        )

        return self.client.get(path, query_params)

    def create(
        self,
        name: str,
        label_key: str,
        label_value: str,
        placement_strategy: models.ResourcesPlacementStrategy,
        over_provisioning_ratio: Optional[int] = 1,
    ) -> dict:
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

    def update(self, 
               nodepool_id: int,
               labelKey: str,
               labelValue: str,
               placementStrategy: models.ResourcesPlacementStrategy,
               overProvisioningRatio: Optional[int] = 1) -> dict:
        """
        Used to update node pool fields that are not labels
        For labels, please use update_labels method
        """
        path = f"/v1/k8s/clusters/{self.client.cluster_id}/node-pools/{nodepool_id}"

        data = {
            "labelKey": labelKey,
            "labelValue": labelValue,
            "placementStrategy": placementStrategy,
            "overProvisioningRatio": overProvisioningRatio
        }

        node_pool_request = models.build_model(
            model=models.NodePoolUpdateRequest, data=data)
        payload = node_pool_request.model_dump_json()

        return self.client.put(path, payload)

    def update_labels(self,
                      nodepool_id: int,
                      label_key: str,
                      label_value: str) -> dict:
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

    def all(self,
            filterBy: Optional[str] = None,
            sortBy: Optional[Literal["name", "clusterId", "departmentId", "createdAt"]] = None,
            sortOrder: Optional[Literal["asc", "desc"]] = None,
            offset: Optional[int] = None,
            limit: Optional[int] = None
            ) -> List:
        path = "/api/v1/org-unit/projects"

        params = {
            "filterBy": filterBy,
            "sortBy": sortBy,
            "sortOrder": sortOrder,
            "offset": offset,
            "limit": limit

        }

        query_params = models.build_query_params(
            query_model=models.ProjectQueryParams, params=params)

        return self.client.get(path, query_params)

    def create(
        self,
        name: str,
        resources: List[models.Resources],
        requested_namespace: Optional[str] = None,
        default_node_pools: Optional[List[str]] = None,
        scheduling_rules: Optional[models.SchedulingRules] = None,
        parent_id: Optional[str] = None,
        node_types: Optional[models.NodeTypes] = None,
    ) -> dict:
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

    def get(self, project_id: int) -> dict:
        path = f"/api/v1/org-unit/projects/{project_id}"

        return self.client.get(path)

    def update(
        self,
        project_id: int,
        resources: List[models.Resources],
        default_node_pools: Optional[List[str]] = None,
        node_types: Optional[models.NodeTypes] = None,
        scheduling_rules: Optional[models.SchedulingRules] = None,
    ) -> dict:
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

    def all(self,
            filterBy: Optional[str] = None,
            sortBy: Optional[Literal["name", "clusterId", "createdAt"]] = None,
            sortOrder: Optional[Literal["asc", "desc"]] = None,
            offset: Optional[int] = None,
            limit: Optional[int] = None
            ) -> List:
        path = "/api/v1/org-unit/departments"

        params = {
            "filterBy": filterBy,
            "sortBy": sortBy,
            "sortOrder": sortOrder,
            "offset": offset,
            "limit": limit

        }

        query_params = models.build_query_params(
            query_model=models.ProjectQueryParams, params=params)

        return self.client.get(path, query_params)

    def create(self, name: str, resources: models.Resources) -> dict:
        path = "/api/v1/org-unit/departments"

        data = {
            "name": name,
            "resources": resources,
            "clusterId": self.client.cluster_id,
        }
        department = models.build_model(model=models.DepartmentCreateRequest, data=data)
        payload = department.model_dump_json()

        return self.client.post(path, payload)

    def get(self, department_id: int) -> dict:
        path = f"/api/v1/org-unit/departments/{department_id}"

        return self.client.get(path)

    def update_resources(self,
                         department_id: str,
                         resources: List[models.Resources]) -> dict:
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

    def all(self,
            subjectType: Optional[str] = None,
            subjectIds: Optional[List[str]] = None,
            limit: Optional[int] = None,
            offset: Optional[int] = None,
            lastUpdated: Optional[str] = None,
            includeDeleted: Optional[bool] = None,
            clusterId: Optional[str] = None,
            scopeId: Optional[str] = None,
            sortBy: Optional[Literal[
                            "subjectId",
                            "subjectType",
                            "roleId",
                            "scopeId",
                            "scopeType",
                            "roleName",
                            "scopeName",
                            "createdAt",
                            "deletedAt",
                            "createdBy",
                            ]] = None,
            filterBy: Optional[str] = None,
            sortOrder: Optional[Literal["asc", "desc"]] = "asc"
            ) -> List:
        
        path = "/api/v1/authorization/access-rules"
        
        params = {
            "subjectType": subjectType,
            "subjectIds": subjectIds,
            "limit": limit,
            "offset": offset,
            "lastUpdated": lastUpdated,
            "includeDeleted": includeDeleted,
            "clusterId": clusterId,
            "scopeId": scopeId,
            "sortBy": sortBy,
            "filterBy": filterBy,
            "sortOrder": sortOrder
        }

        query_params = models.build_query_params(
            query_model=models.AccessRulesQueryParams, params=params)

        return self.client.get(path, params=query_params)

    def create(self,
               subject_id: str,
               subject_type: Literal["user", "app", "group"],
               role_id: int,
               scope_id: str,
               scope_type: Literal["system", "tenant", "cluster", "department", "project"]
               ) -> dict:

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

    def all(self) -> List:
        path = "/api/v1/authorization/roles"

        return self.client.get(path)

    def get(self, role_id: int) -> dict:
        path = f"/api/v1/authorization/roles/{role_id}"

        return self.client.get(path)

    def get_roles_name_to_id_map(self) -> dict:
        path = "/api/v1/authorization/roles"

        roles = self.client.get(path)

        m = {}
        for role in roles:
            m[role["name"]] = role["id"]

        return m


class UsersController(Controller):
    def __init__(self, client):
        super().__init__(client)

    def all(self):
        raise errors.RunaiNotImplementedError

    def create(self, email: str, to_reset_password: bool = False) -> dict:
        path = "/api/v1/users"

        data = {"email": email, "resetPassword": to_reset_password}
        user = models.build_model(model=models.UserCreateRequest, data=data)

        payload = user.model_dump_json()

        return self.client.post(path, payload)


class ClusterController(Controller):
    def __init__(self, client):
        super().__init__(client)

    def all(self, verbosity: Literal["full", "metadata"] = "full") -> List:
        path = f"/api/v1/clusters?verbosity={verbosity}"

        params = {
            "verbosity": verbosity
        }

        query_params = models.build_query_params(
            query_model=models.ClusterQueryParams, params=params)

        return self.client.get(path, params=query_params)

    def get(self,
            cluster_id: str,
            verbosity: Literal["full", "metadata"] = "full") -> dict:
        path = f"/api/v1/clusters/{cluster_id}"

        params = {
            "verbosity": verbosity
        }

        query_params = models.build_query_params(
            query_model=models.ClusterQueryParams, params=params)

        return self.client.get(path, params=query_params)

    def update(self):
        raise errors.RunaiNotImplementedError

    def delete(self):
        raise errors.RunaiNotImplementedError
