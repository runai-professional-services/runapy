# coding: utf-8

"""
Run:ai API

# Introduction  The Run:ai Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: latest
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.workload import Workload
from typing import Optional, Set
from typing_extensions import Self


class GetWorkloads200Response(BaseModel):
    """
    Pydantic class model representing GetWorkloads200Response.

    Parameters:
        ```python
        next: int
        workloads: List[Workload]
        ```
        next: See model int for more information.
        workloads: See model List[Workload] for more information.
    Example:
        ```python
        GetWorkloads200Response(
            next=1,
                        workloads=[
                    runai.models.workload.Workload(
                        tenant_id = 1001,
                        running_pods = 1,
                        phase_updated_at = '2022-06-08T11:28:24.131Z',
                        k8s_phase_updated_at = '2022-06-08T11:28:24.131Z',
                        updated_at = '2022-06-08T11:28:24.131Z',
                        source = 'CLI',
                        deleted_at = '2022-08-12T19:28:24.131Z',
                        type = 'runai-job',
                        name = 'very-important-job',
                        id = '',
                        priority = 50,
                        priority_class_name = 'high-priority',
                        submitted_by = 'researcher@run.ai',
                        cluster_id = '71f69d83-ba66-4822-adf5-55ce55efd210',
                        project_name = 'proj-1',
                        project_id = '1',
                        department_name = 'department-1',
                        department_id = '1',
                        namespace = 'runai-proj-1',
                        created_at = '2022-01-01T03:49:52.531Z',
                        workload_requested_resources = runai.models.workload_request_resources.WorkloadRequestResources(
                            gpu_request_type = 'portion',
                            gpu = runai.models.request_resource_cores.RequestResourceCores(
                                limit = 1.5,
                                request = 1, ),
                            gpu_memory = runai.models.request_resource_quantity.RequestResourceQuantity(
                                limit = '2G',
                                request = '200M', ),
                            cpu = runai.models.request_resource_cores.RequestResourceCores(
                                limit = 1.5,
                                request = 1, ),
                            cpu_memory = runai.models.request_resource_quantity.RequestResourceQuantity(
                                limit = '2G',
                                request = '200M', ),
                            mig_profile = [
                                '1g.5gb'
                                ],
                            extended_resources = [
                                runai.models.workloads_extended_resource.WorkloadsExtendedResource(
                                    resource = 'hardware-vendor.example/foo',
                                    quantity = '2',
                                    exclude = False, )
                                ], ),
                        pods_requested_resources = runai.models.workload_request_resources.WorkloadRequestResources(),
                        allocated_resources = runai.models.workload_allocated_resources.WorkloadAllocatedResources(),
                        actions_support = runai.models.actions_support.ActionsSupport(
                            delete = True,
                            suspend = True, ),
                        phase = 'Creating',
                        conditions = [
                            runai.models.condition1.Condition1(
                                type = 'Ready',
                                status = 'False',
                                message = 'Resource validation failed: ...',
                                reason = 'ErrorConfig',
                                last_transition_time = '2022-01-01T03:49:52.531Z', )
                            ],
                        phase_message = 'Not enough resources in the requested nodepool',
                        k8s_phase = 'Pending',
                        requested_pods = runai.models.requested_pods.RequestedPods(
                            number = 1,
                            min = 2,
                            max = 5,
                            parallelism = 3,
                            completions = 5, ),
                        requested_node_pools = [
                            'default'
                            ],
                        current_node_pools = [
                            'default'
                            ],
                        completed_at = '2022-01-01T03:49:52.531Z',
                        images = [
                            'alpine:latest'
                            ],
                        children_ids = [
                            runai.models.workload_children_ids_inner.Workload_childrenIds_inner(
                                id = '',
                                type = '', )
                            ],
                        urls = [
                            ''
                            ],
                        datasources = [
                            runai.models.datasource.Datasource(
                                type = 'pvc',
                                name = 'my-pvc-datasource-1',
                                id = '', )
                            ],
                        environments = [
                            runai.models.environment.Environment(
                                connections = [
                                    runai.models.connection1.Connection1(
                                        name = 'my-pytorch-env',
                                        tool_type = 'pytorch',
                                        connection_type = 'ExternalUrl',
                                        url = 'http://wandb.com/yourproject',
                                        authorization_type = 'public',
                                        authorized_users = ["user@company.ai","another@company.ai"],
                                        authorized_groups = ["group-a","group-b"],
                                        container_port = 8080, )
                                    ],
                                name = 'pytorch',
                                id = '',
                                replica_type = 'Master', )
                            ],
                        external_connections = [
                            runai.models.connection1.Connection1(
                                name = 'my-pytorch-env',
                                tool_type = 'pytorch',
                                connection_type = 'ExternalUrl',
                                url = 'http://wandb.com/yourproject',
                                authorization_type = 'public',
                                authorized_users = ["user@company.ai","another@company.ai"],
                                authorized_groups = ["group-a","group-b"],
                                container_port = 8080, )
                            ],
                        distributed_framework = 'Pytorch',
                        additional_fields = { },
                        preemptible = True,
                        environment_variables = {
                            'key' : ''
                            },
                        command = 'sleep',
                        arguments = '1000',
                        phase_reason = '',
                        idle_gpus = 3,
                        idle_allocated_gpus = 1, )
                    ]
        )
        ```
    """  # noqa: E501

    next: Optional[StrictInt] = None
    workloads: List[Workload]
    __properties: ClassVar[List[str]] = ["next", "workloads"]

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
        """Create an instance of GetWorkloads200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in workloads (list)
        _items = []
        if self.workloads:
            for _item_workloads in self.workloads:
                if _item_workloads:
                    _items.append(_item_workloads.to_dict())
            _dict["workloads"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetWorkloads200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "next": obj.get("next"),
                "workloads": (
                    [Workload.from_dict(_item) for _item in obj["workloads"]]
                    if obj.get("workloads") is not None
                    else None
                ),
            }
        )
        return _obj
