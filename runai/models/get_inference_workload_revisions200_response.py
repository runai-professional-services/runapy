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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from runai.models.revision import Revision
from typing import Optional, Set
from typing_extensions import Self


class GetInferenceWorkloadRevisions200Response(BaseModel):
    """
    Pydantic class model representing GetInferenceWorkloadRevisions200Response.

    Parameters:
        ```python
        revisions: List[Revision]
        ```
        revisions: See model List[Revision] for more information.
    Example:
        ```python
        GetInferenceWorkloadRevisions200Response(
            revisions=[
                    runai.models.revision.Revision(
                        type = 'runai-revision',
                        name = 'very-important-job',
                        id = '',
                        workload_id = '',
                        tenant_id = 1001,
                        cluster_id = '71f69d83-ba66-4822-adf5-55ce55efd210',
                        project_id = '1',
                        department_id = '2',
                        created_at = '2022-01-01T03:49:52.531Z',
                        deleted_at = '2022-08-12T19:28:24.131Z',
                        revision_requested_resources = runai.models.workload_request_resources.WorkloadRequestResources(
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
                        requested_pods = runai.models.requested_pods.RequestedPods(
                            number = 1,
                            min = 2,
                            max = 5,
                            parallelism = 3,
                            completions = 5, ),
                        requested_node_pools = [
                            'default'
                            ],
                        allocated_resources = runai.models.workload_allocated_resources.WorkloadAllocatedResources(),
                        current_node_pools = [
                            'default'
                            ],
                        running_pods = 1,
                        images = [
                            'alpine:latest'
                            ],
                        environment_variables = {
                            'key' : ''
                            },
                        command = 'sleep',
                        arguments = '1000',
                        children_ids = [
                            runai.models.workload_children_ids_inner.Workload_childrenIds_inner(
                                id = '',
                                type = '', )
                            ],
                        conditions = [
                            runai.models.condition1.Condition1(
                                type = 'Ready',
                                status = 'False',
                                message = 'Resource validation failed: ...',
                                reason = 'ErrorConfig',
                                last_transition_time = '2022-01-01T03:49:52.531Z', )
                            ],
                        phase = 'Creating',
                        phase_message = 'Not enough resources in the requested nodepool',
                        phase_updated_at = '2022-06-08T11:28:24.131Z',
                        additional_fields = { }, )
                    ]
        )
        ```
    """  # noqa: E501

    revisions: List[Revision]
    __properties: ClassVar[List[str]] = ["revisions"]

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
        """Create an instance of GetInferenceWorkloadRevisions200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in revisions (list)
        _items = []
        if self.revisions:
            for _item_revisions in self.revisions:
                if _item_revisions:
                    _items.append(_item_revisions.to_dict())
            _dict["revisions"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetInferenceWorkloadRevisions200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "revisions": (
                    [Revision.from_dict(_item) for _item in obj["revisions"]]
                    if obj.get("revisions") is not None
                    else None
                )
            }
        )
        return _obj
