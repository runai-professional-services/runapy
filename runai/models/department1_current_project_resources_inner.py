# coding: utf-8

"""
Runai API

# Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: 2.0.0
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from runai.models.resource_data import ResourceData
from typing import Optional, Set
from typing_extensions import Self


class Department1CurrentProjectResourcesInner(BaseModel):
    """
    Pydantic class model representing Department1CurrentProjectResourcesInner.

    Parameters:
        ```python
        number_of_pending_workloads: int
        gpu: ResourceData
        cpu: ResourceData
        memory: ResourceData
        project_name: str
        nodepool_name: str
        ```
        number_of_pending_workloads: See model int for more information.
        gpu: See model ResourceData for more information.
        cpu: See model ResourceData for more information.
        memory: See model ResourceData for more information.
        project_name: See model str for more information.
        nodepool_name: See model str for more information.
    Example:
        ```python
        Department1CurrentProjectResourcesInner(
            number_of_pending_workloads=1,
                        gpu=runai.models.resource_data.ResourceData(
                    quota = 3,
                    allocated = 2.5,
                    utilization = 0.765, ),
                        cpu=runai.models.resource_data.ResourceData(
                    quota = 3,
                    allocated = 2.5,
                    utilization = 0.765, ),
                        memory=runai.models.resource_data.ResourceData(
                    quota = 3,
                    allocated = 2.5,
                    utilization = 0.765, ),
                        project_name='project-a',
                        nodepool_name='nodepoola'
        )
        ```
    """  # noqa: E501

    number_of_pending_workloads: StrictInt = Field(alias="numberOfPendingWorkloads")
    gpu: ResourceData
    cpu: ResourceData
    memory: ResourceData
    project_name: StrictStr = Field(alias="projectName")
    nodepool_name: StrictStr = Field(alias="nodepoolName")
    __properties: ClassVar[List[str]] = [
        "numberOfPendingWorkloads",
        "gpu",
        "cpu",
        "memory",
        "projectName",
        "nodepoolName",
    ]

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
        """Create an instance of Department1CurrentProjectResourcesInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of gpu
        if self.gpu:
            _dict["gpu"] = self.gpu.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cpu
        if self.cpu:
            _dict["cpu"] = self.cpu.to_dict()
        # override the default output from pydantic by calling `to_dict()` of memory
        if self.memory:
            _dict["memory"] = self.memory.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Department1CurrentProjectResourcesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "numberOfPendingWorkloads": obj.get("numberOfPendingWorkloads"),
                "gpu": (
                    ResourceData.from_dict(obj["gpu"])
                    if obj.get("gpu") is not None
                    else None
                ),
                "cpu": (
                    ResourceData.from_dict(obj["cpu"])
                    if obj.get("cpu") is not None
                    else None
                ),
                "memory": (
                    ResourceData.from_dict(obj["memory"])
                    if obj.get("memory") is not None
                    else None
                ),
                "projectName": obj.get("projectName"),
                "nodepoolName": obj.get("nodepoolName"),
            }
        )
        return _obj
