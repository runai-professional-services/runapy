import abc
import inspect
import json

from typing import Any, Optional, List, Literal

from . import models
from . import errors


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
        return [
            name
            for name, _ in inspect.getmembers(self, predicate=inspect.ismethod)
            if not name.startswith("_")
            if not name.__contains__("options")
        ]


class TemplateController(Controller):
    def __init__(self, client):
        super().__init__(client)
        self.path = "/api/v1/asset/workload-template"

    def all(self) -> List:

        return self.client.get(self.path)
    
    def create(
        self,
        name: str,
        scope: str,
        assets: dict,
        clusterId: Optional[str] = None,
        specificenv: Optional[dict] = None,
    ):
        """
        assets example:
        "environment": "1f21043c-3a8a-4049-bd62-4c3135545178",
        "compute": "bbe5a6d1-1c63-4448-b534-036514f8b756",
        "datasources": [id: 1, kind: "accessKey"],
        "workloadVolumes": "my-volume"

        specificEnv example:
        "command": "python",
        "args": "-x my-script.py",
        "runAsUid": 500,
        "runAsGid": 30,
        "supplementalGroups": "2,3,5,8",
        "environmentVariables": [
        {}
        ],
        "nodeType": "my-node-type",
        "nodePools": [
        "my-node-pool-a",
        "my-node-pool-b"
        ],
        "podAffinity": {
        "type": "Required",
        "key": "string"
        },
        "terminateAfterPreemption": false,
        "autoDeletionTimeAfterCompletionSeconds": 15,
        "backoffLimit": 3,
        "annotations": [
        {}
        ],
        "labels": [
        {
        "name": "stage",
        "value": "initial-research",
        "exclude": false
        }
        ],
        """
        data = {
            "meta": {
                "name": name,
                "scope": scope,
                "clusterId": clusterId,
            },

            "spec": {
                "assets": assets,
                "specificEnv": specificenv,
            }
        }

        template = models.build_model(models.TemplateCreateRequest, data)
        payload = template.model_dump_json()

        return self.client.post(self.path, payload)

    def get_by_name(self, template_name: str):
        templates = self.all()

        template = next(
            (entry for entry in templates['entries'] 
            if entry['meta']['name'] == template_name),
            None
        )
        
        return template

    def update(
        self,
        asset_id: str,
        name: str,
        assets: dict,
        specificenv: Optional[dict] = None,
    ):
        """
        Used to update an existing template. 

        assets example:
        "environment": "1f21043c-3a8a-4049-bd62-4c3135545178",
        "compute": "bbe5a6d1-1c63-4448-b534-036514f8b756"
        "datasources": [id: 1, kind: "accessKey"]
        "workloadVolumes": "my-volume"

        specificEnv example:
        "command": "python",
        "args": "-x my-script.py",
        "runAsUid": 500,
        "runAsGid": 30,
        "supplementalGroups": "2,3,5,8",
        "environmentVariables": [
            {"name": "HOME",
            "value": "/home/my-folder",
            "secret": {
                "name": "postgress_secret",
                "key": "POSTGRES_PASSWORD"
            },
            "exclude": false}
        ],
        "nodeType": "my-node-type",
        "nodePools": [
        "my-node-pool-a",
        "my-node-pool-b"
        ],
        "podAffinity": {
        "type": "Required",
        "key": "string"
        },
        "terminateAfterPreemption": false,
        "autoDeletionTimeAfterCompletionSeconds": 15,
        "backoffLimit": 3,
        "annotations": [
            {"name": "billing",
            "value": "my-billing-unit",
            "exclude": false}
        ],
        "labels": [
        {
        "name": "stage",
        "value": "initial-research",
        "exclude": false
        }
        ],
        """

        path = f"{self.path}/{asset_id}"

        data = {
            "meta": {
                "name": name,
            },
            "spec": {
                "assets": assets,
                "specificEnv": specificenv,
            }
        }

        template_request = models.build_model(
            model=models.TemplateUpdateRequest, data=data
        )

        payload = template_request.model_dump_json()

        return self.client.put(path, payload)

    def delete(self, asset_id: int):
        path = f"{self.path}/{asset_id}"

        resp = self.client.delete(path)
        return resp
    

class ComputeController(Controller):
    def __init__(self, client):
        super().__init__(client)
        self.path = "/api/v1/asset/compute"

    def all(self) -> List:
        return self.client.get(self.path)
    
    def get_by_name(self, compute_name: str):
        computes = self.all()

        compute = next(
            (entry for entry in computes['entries'] 
            if entry['meta']['name'] == compute_name),
            None
        )
        
        return compute


class EnvironmentController(Controller):
    def __init__(self, client):
        super().__init__(client)
        self.path = "/api/v1/asset/environment"

    def all(self) -> List:
        return self.client.get(self.path)
    
    def get_by_name(self, environment_name: str):
        environments = self.all()

        environment = next(
            (entry for entry in environments['entries'] 
            if entry['meta']['name'] == environment_name), 
            None
        )
        
        return environment


class NodePoolController(Controller):
    def __init__(self, client):
        super().__init__(client)
        if self.client.cluster_id is None:
            raise errors.RunaiClusterIDNotConfigured()

    def all(self) -> List:
        path = f"/v1/k8s/clusters/{self.client.cluster_id}/node-pools"

        return self.client.get(path)

    def get_by_name(self, nodepool_name: str):
        node_pools = self.all()
        node_pool = self._filter(node_pools, name=nodepool_name)

        return node_pool

    def node_pool_metrics(
        self,
        nodepool_name: str,
        start: str,
        end: str,
        metric_type: Literal[
            "GPU_UTILIZATION",
            "GPU_MEMORY_UTILIZATION",
            "CPU_UTILIZATION",
            "CPU_MEMORY_UTILIZATION",
            "TOTAL_GPU",
            "GPU_QUOTA",
            "ALLOCATED_GPU",
            "AVG_WORKLOAD_WAIT_TIME",
        ],
        number_of_samples: Optional[int] = 20,
    ) -> dict:
        path = f"/api/v1/clusters/{self.client.cluster_id}/nodepools/{nodepool_name}/metrics"

        params = {
            "start": start,
            "end": end,
            "metricType": metric_type,
            "numberOfSamples": number_of_samples,
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
        placement_strategy: dict,
        over_provisioning_ratio: Optional[int] = 1,
    ) -> dict:
        """
        placementStrategy example:
        {"gpu": "binpack", "cpu": "binpack"}
        """
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

    def update(
        self,
        nodepool_id: int,
        labelKey: str,
        labelValue: str,
        placementStrategy: models.ResourcesPlacementStrategy,
        overProvisioningRatio: Optional[int] = 1,
    ) -> dict:
        """
        Used to update node pool fields that are not labels
        For labels, please use update_labels method

        placementStrategy example:
        {"gpu": "binpack", "cpu": "binpack"}
        """
        path = f"/v1/k8s/clusters/{self.client.cluster_id}/node-pools/{nodepool_id}"

        data = {
            "labelKey": labelKey,
            "labelValue": labelValue,
            "placementStrategy": placementStrategy,
            "overProvisioningRatio": overProvisioningRatio,
        }

        node_pool_request = models.build_model(
            model=models.NodePoolUpdateRequest, data=data
        )
        payload = node_pool_request.model_dump_json()

        return self.client.put(path, payload)

    def update_labels(self, nodepool_id: int, label_key: str, label_value: str) -> dict:
        path = (
            f"/v1/k8s/clusters/{self.client.cluster_id}/node-pools/{nodepool_id}/labels"
        )

        labels = models.build_model(
            model=models.NodePoolLabels,
            data={"labelKey": label_key, "labelValue": label_value},
        )

        payload = labels.model_dump_json()

        return self.client.put(path, payload)

    def delete(self, nodepool_id: int):
        path = f"/v1/k8s/clusters/{self.client.cluster_id}/node-pools/{nodepool_id}"

        resp = self.client.delete(path)
        return resp


class ProjectController(Controller):
    def __init__(self, client):
        super().__init__(client)
        if self.client.cluster_id is None:
            raise errors.RunaiClusterIDNotConfigured()

    def all(
        self,
        filterBy: Optional[str] = None,
        sortBy: Optional[
            Literal["name", "clusterId", "departmentId", "createdAt"]
        ] = None,
        sortOrder: Optional[Literal["asc", "desc"]] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> List:
        path = "/api/v1/org-unit/projects"

        params = {
            "filterBy": filterBy,
            "sortBy": sortBy,
            "sortOrder": sortOrder,
            "offset": offset,
            "limit": limit,
        }

        query_params = models.build_query_params(
            query_model=models.ProjectQueryParams, params=params
        )

        return self.client.get(path, query_params)

    def create(
        self,
        name: str,
        resources: List[dict],
        requested_namespace: Optional[str] = None,
        default_node_pools: Optional[List[str]] = ["default"],
        scheduling_rules: Optional[dict] = None,
        parent_id: Optional[str] = None,
        node_types: Optional[dict] = None,
    ) -> dict:
        """
        Create a project.
        Fields are matching the API documentation.\n
        Parameters examples:\n
        resources\n
        [{
            "nodePool": {
            "id": "22",
            "name": "default"
        },
            "gpu": {
            "deserved": 1,
            "limit": 2,
            "overQuotaWeight": 2
        },
            "cpu": {
            "deserved": 1,
            "limit": 2,
            "overQuotaWeight": 2
        },
            "memory": {
            "deserved": 1,
            "limit": 2,
            "overQuotaWeight": 2,
            "units": "Mib"
        }]

        scheduling_rules\n
        {"interactiveJobTimeLimitSeconds": 3600,
                            "interactiveJobMaxIdleDurationSeconds": None,
                            "interactiveJobPreemptIdleDurationSeconds": None,
                            "trainingJobTimeLimitSeconds": None,
                            "trainingJobMaxIdleDurationSeconds": None
                            }

        node_types\n
        {"training": ["gpu"], "workspace": ["cpu"]}
        """
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
        resources: List[dict],
        default_node_pools: Optional[List[str]] = None,
        node_types: Optional[dict] = None,
        scheduling_rules: Optional[dict] = None,
    ) -> dict:
        """
        Update a project\n
        Parameters examples:\n
        resources\n
        [{
            "nodePool": {
            "id": "22",
            "name": "default"
        },
            "gpu": {
            "deserved": 1,
            "limit": 2,
            "overQuotaWeight": 2
        },
            "cpu": {
            "deserved": 1,
            "limit": 2,
            "overQuotaWeight": 2
        },
            "memory": {
            "deserved": 1,
            "limit": 2,
            "overQuotaWeight": 2,
            "units": "Mib"
        }]

        scheduling_rules\n
        {"interactiveJobTimeLimitSeconds": 3600,
                            "interactiveJobMaxIdleDurationSeconds": None,
                            "interactiveJobPreemptIdleDurationSeconds": None,
                            "trainingJobTimeLimitSeconds": None,
                            "trainingJobMaxIdleDurationSeconds": None
                            }

        node_types\n
        {"training": ["gpu"], "workspace": ["cpu"]}
        """
        path = f"/api/v1/org-unit/projects/{project_id}"

        data = {
            "resources": resources,
            "schedulingRules": scheduling_rules,
            "defaultNodePools": default_node_pools,
            "nodeTypes": node_types,
        }

        model = models.build_model(model=models.ProjectUpdateRequest, data=data)
        payload = model.model_dump_json()

        return self.client.put(path, payload)
    
    def patch(self,
              project_id: int,
              resources: List[dict]
              ) -> dict:
        path = f"/api/v1/org-unit/projects/{project_id}/resources"

        data = {"resources": resources}

        model = models.build_model(model=models.ProjectUpdateRequest, data=data)
        payload = model.model_dump()["resources"]

        return self.client.patch(path, json.dumps(payload))

    def delete(self, project_id: int):
        path = f"/api/v1/org-unit/projects/{project_id}"

        return self.client.delete(path)


class DepartmentController(Controller):
    def __init__(self, client):
        super().__init__(client)
        if self.client.cluster_id is None:
            raise errors.RunaiClusterIDNotConfigured()

    def all(
        self,
        filterBy: Optional[str] = None,
        sortBy: Optional[Literal["name", "clusterId", "createdAt"]] = None,
        sortOrder: Optional[Literal["asc", "desc"]] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> List:
        path = "/api/v1/org-unit/departments"

        params = {
            "filterBy": filterBy,
            "sortBy": sortBy,
            "sortOrder": sortOrder,
            "offset": offset,
            "limit": limit,
        }

        query_params = models.build_query_params(
            query_model=models.DepartmentQueryParams, params=params
        )

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

    def update_resources(
        self, department_id: str, resources: List[models.Resources]
    ) -> dict:
        path = f"/api/v1/org-unit/departments/{department_id}/resources"

        payload = []
        for resource in resources:
            resource = models.build_model(models.Resources, resource)
            payload.append(resource.model_dump())

        return self.client.put(path, payload)
    
    def patch(self,
              department_id: int,
              resources: List[dict]
              ) -> dict:
        path = f"/api/v1/org-unit/departments/{department_id}/resources"

        data = {"resources": resources}

        model = models.build_model(model=models.DepartmentUpdateRequest, data=data)
        payload = model.model_dump()["resources"]

        return self.client.patch(path, json.dumps(payload))

    def delete(self, department_id: int):
        path = f"/api/v1/org-unit/departments/{department_id}"

        return self.client.delete(path)


class AccessRulesController(Controller):
    def __init__(self, client):
        super().__init__(client)

    def all(
        self,
        subjectType: Optional[str] = None,
        subjectIds: Optional[List[str]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        lastUpdated: Optional[str] = None,
        includeDeleted: Optional[bool] = None,
        clusterId: Optional[str] = None,
        scopeId: Optional[str] = None,
        sortBy: Optional[
            Literal[
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
            ]
        ] = None,
        filterBy: Optional[str] = None,
        sortOrder: Optional[Literal["asc", "desc"]] = "asc",
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
            "sortOrder": sortOrder,
        }

        query_params = models.build_query_params(
            query_model=models.AccessRulesQueryParams, params=params
        )

        return self.client.get(path, params=query_params)

    def create(
        self,
        subject_id: str,
        subject_type: Literal["user", "app", "group"],
        role_id: int,
        scope_id: str,
        scope_type: Literal["system", "tenant", "cluster", "department", "project"],
    ) -> dict:

        path = "/api/v1/authorization/access-rules"

        data = {
            "subjectId": subject_id,
            "subjectType": subject_type,
            "roleId": role_id,
            "scopeId": scope_id,
            "scopeType": scope_type,
            "clusterId": self.client.cluster_id,
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

        params = {"verbosity": verbosity}

        query_params = models.build_query_params(
            query_model=models.ClusterQueryParams, params=params
        )

        return self.client.get(path, params=query_params)

    def get(
        self, cluster_id: str, verbosity: Literal["full", "metadata"] = "full"
    ) -> dict:
        path = f"/api/v1/clusters/{cluster_id}"

        params = {"verbosity": verbosity}

        query_params = models.build_query_params(
            query_model=models.ClusterQueryParams, params=params
        )

        return self.client.get(path, params=query_params)


class WorkloadsController(Controller):
    def __init__(self, client):
        super().__init__(client)

    def all(
        self,
        deleted: Optional[bool] = False,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        last_updated: Optional[str] = None,
        sort_by: Optional[
            Literal[
                "type",
                "name",
                "clusterId",
                "projectId",
                "projectName",
                "departmentId",
                "departmentName",
                "createdAt",
                "deletedAt",
                "submittedBy",
                "phase",
                "completedAt",
                "nodepool",
                "allocatedGPU",
            ]
        ] = None,
        filter_by: Optional[str] = None,
        sort_order: Optional[Literal["asc", "desc"]] = "asc",
    ):
        """Retrieve a list of active workloads with details.

        deleted - Return only deleted resources when true.
        """
        path = "/api/v1/workloads"

        params = {
            "deleted": deleted,
            "limit": limit,
            "offset": offset,
            "lastUpdated": last_updated,
            "sortBy": sort_by,
            "filterBy": filter_by,
            "sortOrder": sort_order,
        }
        query_params = models.build_query_params(
            query_model=models.WorkloadsGetAllQueryParams, params=params
        )

        return self.client.get(path, query_params)

    def get_workload(self, workload_id: str):
        path = f"/api/v1/workloads/{workload_id}"

        return self.client.get(path)

    def count_workloads(self, deleted: bool, filter_by: Optional[str] = None):
        path = "/api/v1/workloads/count"

        params = {"deleted": deleted, "filterBy": filter_by}

        query_params = models.build_query_params(
            query_model=models.WorkloadsCountQueryParams, params=params
        )

        return self.client.get(path, query_params)

    def get_workloads_telemetry(
        self,
        telemetry_type: Literal["WORKLOADS_COUNT", "GPU_ALLOCATION"],
        group_by: Optional[
            List[
                Literal[
                    "ClusterId",
                    "DepartmentId",
                    "ProjectId",
                    "Type",
                    "CurrentNodepools",
                    "Phase",
                ]
            ]
        ] = None,
        node_pool_name: Optional[str] = None,
        department_id: Optional[str] = None,
        cluster_id: Optional[str] = None,
    ):
        path = "/api/v1/workloads/telemetry"

        params = {
            "telemetryType": telemetry_type,
            "groupBy": group_by,
            "nodePoolName": node_pool_name,
            "departmentId": department_id,
            "clusterId": cluster_id,
        }

        query_params = models.build_query_params(
            query_model=models.WorkloadsTelemetryQueryParams, params=params
        )

        return self.client.get(path, query_params)

    def get_workload_metrics(
        self,
        workload_id: str,
        start: str,
        end: str,
        metric_type: List[Literal[
            "GPU_MEMORY_REQUEST_BYTES",
            "CPU_USAGE_CORES",
            "CPU_REQUEST_CORES",
            "CPU_LIMIT_CORES",
            "CPU_MEMORY_USAGE_BYTES",
            "CPU_MEMORY_REQUEST_BYTES",
            "CPU_MEMORY_LIMIT_BYTES",
            "POD_COUNT",
            "RUNNING_POD_COUNT",
            "GPU_ALLOCATION",
        ]],
        number_of_samples: Optional[int] = 20,
    ):
        path = f"/api/v1/workloads/{workload_id}/metrics"

        params = {
            "workloadId": workload_id,
            "start": start,
            "end": end,
            "metricType": metric_type,
            "numberOfSamples": number_of_samples,
        }
        query_params = models.build_query_params(
            query_model=models.WorkloadMetricsQueryParams, params=params
        )

        return self.client.get(path, query_params)


class WorkspaceController(Controller):
    def __init__(self, client):
        super().__init__(client)
        if self.client.cluster_id is None:
            raise errors.RunaiClusterIDNotConfigured()

    def create(
        self,
        workspace_name: str,
        use_given_name_as_prefix: bool,
        project_id: str,
        cluster_id: str,
        spec: dict,
    ):
        path = "/api/v1/workloads/workspaces"

        data = {
            "name": workspace_name,
            "usGivenNameAsPrefix": use_given_name_as_prefix,
            "projectId": project_id,
            "clusterId": cluster_id,
            "spec": spec,
        }

        workspace = models.build_model(model=models.WorkspaceCreateRequest, data=data)

        payload = workspace.model_dump_json()

        return self.client.post(path, payload)

    def delete(self, workspace_id: int):
        path = f"/api/v1/workloads/workspaces/{workspace_id}"

        return self.client.delete(path)

    def get(self, workspace_id: int):
        path = f"/api/v1/workloads/workspaces/{workspace_id}"

        return self.client.get(path)

    def suspend(self, workspace_id: int):
        path = f"/api/v1/workloads/workspaces/{workspace_id}/suspend"

        return self.client.post(path, {})

    def resume(self, workspace_id: int):
        path = f"/api/v1/workloads/workspaces/{workspace_id}/resume"

        return self.client.post(path, {})


class TrainingController(Controller):
    def __init__(self, client):
        super().__init__(client)
        if self.client.cluster_id is None:
            raise errors.RunaiClusterIDNotConfigured()

    def create(
        self,
        training_name: str,
        use_given_name_as_prefix: bool,
        project_id: str,
        cluster_id: str,
        spec: dict,
    ):
        path = "/api/v1/workloads/trainings"

        data = {
            "name": training_name,
            "usGivenNameAsPrefix": use_given_name_as_prefix,
            "projectId": project_id,
            "clusterId": cluster_id,
            "spec": spec,
        }

        training = models.build_model(model=models.TrainingCreateRequest, data=data)
        payload = training.model_dump_json()

        return self.client.post(path, payload)

    def delete(self, training_id: str):
        path = f"/api/v1/workloads/trainings/{training_id}"

        return self.client.delete(path)

    def get(self, training_id: str):
        path = f"/api/v1/workloads/trainings/{training_id}"

        return self.client.get(path)

    def suspend(self, training_id: str):
        path = f"/api/v1/workloads/trainings/{training_id}/suspend"

        return self.client.post(path, {})

    def resume(self, training_id: str):
        path = f"/api/v1/workloads/trainings/{training_id}/resume"

        return self.client.post(path, {})


class InferenceController(Controller):
    def __init__(self, client):
        super().__init__(client)
        if self.client.cluster_id is None:
            raise errors.RunaiClusterIDNotConfigured()

    def create(
        self,
        inference_name: str,
        use_given_name_as_prefix: bool,
        project_id: str,
        cluster_id: str,
        spec: dict,
    ):
        path = "/api/v1/workloads/inferences"

        data = {
            "name": inference_name,
            "usGivenNameAsPrefix": use_given_name_as_prefix,
            "projectId": project_id,
            "clusterId": cluster_id,
            "spec": spec,
        }

        inference = models.build_model(model=models.InferenceCreateRequest, data=data)
        payload = inference.model_dump_json(exclude_none=True)

        return self.client.post(path, payload)

    def delete(self, inference_id: str):
        path = f"/api/v1/workloads/inferences/{inference_id}"

        return self.client.delete(path)

    def get(self, inference_id: str):
        path = f"/api/v1/workloads/inferences/{inference_id}"

        return self.client.get(path)

    def get_metrics(
        self,
        inference_id: str,
        start: str,
        end: str,
        metric_type: Literal["THROUGHPUT", "LATENCY"],
        number_of_samples: Optional[int] = 20,
    ):
        path = f"/api/v1/workloads/inferences/{inference_id}/metrics"

        params = {
            "start": start,
            "end": end,
            "metricType": metric_type,
            "numberOfSamples": number_of_samples,
        }

        query_params = models.build_query_params(
            query_model=models.InferenceWorkloadQueryParams, params=params
        )
        return self.client.get(path, query_params)

    def get_pod_metrics(
        self,
        inference_id: str,
        pod_id: str,
        start: str,
        end: str,
        metric_type: Literal["THROUGHPUT", "LATENCY"],
        number_of_samples: Optional[int] = 20,
    ):
        path = f"/api/v1/workloads/inferences/{inference_id}/pods/{pod_id}/metrics"

        params = {
            "start": start,
            "end": end,
            "metricType": metric_type,
            "numberOfSamples": number_of_samples,
        }

        query_params = models.build_query_params(
            query_model=models.InferenceWorkloadQueryParams, params=params
        )
        return self.client.get(path, query_params)


class DistributedController(Controller):
    def __init__(self, client):
        super().__init__(client)
        if self.client.cluster_id is None:
            raise errors.RunaiClusterIDNotConfigured()

    def create(
        self,
        ditributed_training_name: str,
        use_given_name_as_prefix: bool,
        project_id: str,
        cluster_id: str,
        spec: dict,
        master_spec_same_as_worker: Optional[bool] = True,
        master_spec: Optional[dict] = None,
    ):
        path = "/api/v1/workloads/distributed"

        if master_spec_same_as_worker and master_spec is not None:
            raise errors.RunaiClientError(
                err=ValueError,
                message="Cannot use masterSpec if masterSpecSameAsWorker set to true\n Either disable the flag or remove masterSpec",
            )

        data = {
            "name": ditributed_training_name,
            "usGivenNameAsPrefix": use_given_name_as_prefix,
            "projectId": project_id,
            "clusterId": cluster_id,
            "spec": spec,
            "masterSpecSameAsWorker": master_spec_same_as_worker,
            "masterSpec": master_spec,
        }

        distributed = models.build_model(
            model=models.DistributedCreateRequest, data=data
        )
        payload = distributed.model_dump_json()

        return self.client.post(path, payload)

    def get(self, ditributed_workload_id: str):
        path = f"/api/v1/workloads/distributed/{ditributed_workload_id}"

        return self.client.get(path)

    def delete(self, ditributed_workload_id: str):
        path = f"/api/v1/workloads/distributed/{ditributed_workload_id}"

        return self.client.delete(path)
