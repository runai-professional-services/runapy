# coding: utf-8

"""
Runai API

# Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: 2.2
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.resources_cpu import ResourcesCpu
from runai.models.resources_gpu import ResourcesGpu
from runai.models.resources_memory import ResourcesMemory
from runai.models.resources_node_pool import ResourcesNodePool
from typing import Optional, Set
from typing_extensions import Self


class Resources(BaseModel):
    """
    Pydantic class model representing Resources.

    Parameters:
        ```python
        node_pool: Optional[ResourcesNodePool]
        gpu: ResourcesGpu
        cpu: Optional[ResourcesCpu]
        memory: Optional[ResourcesMemory]
        priority: Optional[str]
        ```
        node_pool: See model ResourcesNodePool for more information.
        gpu: See model ResourcesGpu for more information.
        cpu: See model ResourcesCpu for more information.
        memory: See model ResourcesMemory for more information.
        priority: See model str for more information.
    Example:
        ```python
        Resources(
            node_pool=runai.models.resources_node_pool.Resources_nodePool(
                    id = '22',
                    name = 'default', ),
                        gpu="example",
                        cpu=runai.models.resources_cpu.Resources_cpu(),
                        memory=runai.models.resources_memory.Resources_memory(),
                        priority='Normal'
        )
        ```
    """  # noqa: E501

    node_pool: Optional[ResourcesNodePool] = Field(default=None, alias="nodePool")
    gpu: ResourcesGpu
    cpu: Optional[ResourcesCpu] = None
    memory: Optional[ResourcesMemory] = None
    priority: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["nodePool", "gpu", "cpu", "memory", "priority"]

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
        """Create an instance of Resources from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of node_pool
        if self.node_pool:
            _dict["nodePool"] = self.node_pool.to_dict()
        # override the default output from pydantic by calling `to_dict()` of gpu
        if self.gpu:
            _dict["gpu"] = self.gpu.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cpu
        if self.cpu:
            _dict["cpu"] = self.cpu.to_dict()
        # override the default output from pydantic by calling `to_dict()` of memory
        if self.memory:
            _dict["memory"] = self.memory.to_dict()
        # set to None if node_pool (nullable) is None
        # and model_fields_set contains the field
        if self.node_pool is None and "node_pool" in self.model_fields_set:
            _dict["nodePool"] = None

        # set to None if cpu (nullable) is None
        # and model_fields_set contains the field
        if self.cpu is None and "cpu" in self.model_fields_set:
            _dict["cpu"] = None

        # set to None if memory (nullable) is None
        # and model_fields_set contains the field
        if self.memory is None and "memory" in self.model_fields_set:
            _dict["memory"] = None

        # set to None if priority (nullable) is None
        # and model_fields_set contains the field
        if self.priority is None and "priority" in self.model_fields_set:
            _dict["priority"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Resources from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "nodePool": (
                    ResourcesNodePool.from_dict(obj["nodePool"])
                    if obj.get("nodePool") is not None
                    else None
                ),
                "gpu": (
                    ResourcesGpu.from_dict(obj["gpu"])
                    if obj.get("gpu") is not None
                    else None
                ),
                "cpu": (
                    ResourcesCpu.from_dict(obj["cpu"])
                    if obj.get("cpu") is not None
                    else None
                ),
                "memory": (
                    ResourcesMemory.from_dict(obj["memory"])
                    if obj.get("memory") is not None
                    else None
                ),
                "priority": obj.get("priority"),
            }
        )
        return _obj
