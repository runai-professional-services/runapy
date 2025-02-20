# coding: utf-8

"""
Runai API

# Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token).

The version of the OpenAPI document: 2.19
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from runai.models.resource_v1_response import ResourceV1Response
from typing import Optional, Set
from typing_extensions import Self


class AssignedResourcesV1Response(BaseModel):
    """
    Pydantic class model representing AssignedResourcesV1Response.

    Parameters:
        ```python
        id: float
        gpu: ResourceV1Response
        cpu: ResourceV1Response
        memory: ResourceV1Response
        ```
        id: See model float for more information.
        gpu: GPU number assigned
        cpu: CPU Millicores assigned. Supported only if &#39;CPU Resources Quota&#39; feature flag is enabled.
        memory: CPU Memory Mib assigned. Supported only if &#39;CPU Resources Quota&#39; feature flag is enabled.
    Example:
        ```python
        AssignedResourcesV1Response(
            id=1.337,
                        gpu=runai.models.resource_v1_response.ResourceV1Response(
                    deserved = 0,
                    max_allowed = 1000,
                    over_quota_weight = 2, ),
                        cpu=runai.models.resource_v1_response.ResourceV1Response(
                    deserved = 0,
                    max_allowed = 1000,
                    over_quota_weight = 2, ),
                        memory=runai.models.resource_v1_response.ResourceV1Response(
                    deserved = 0,
                    max_allowed = 1000,
                    over_quota_weight = 2, )
        )
        ```
    """  # noqa: E501

    id: Optional[Union[StrictFloat, StrictInt]] = None
    gpu: ResourceV1Response = Field(description="GPU number assigned")
    cpu: ResourceV1Response = Field(
        description="CPU Millicores assigned. Supported only if 'CPU Resources Quota' feature flag is enabled."
    )
    memory: ResourceV1Response = Field(
        description="CPU Memory Mib assigned. Supported only if 'CPU Resources Quota' feature flag is enabled."
    )
    __properties: ClassVar[List[str]] = ["id", "gpu", "cpu", "memory"]

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
        """Create an instance of AssignedResourcesV1Response from a JSON string"""
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
        """Create an instance of AssignedResourcesV1Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "id": obj.get("id"),
                "gpu": (
                    ResourceV1Response.from_dict(obj["gpu"])
                    if obj.get("gpu") is not None
                    else None
                ),
                "cpu": (
                    ResourceV1Response.from_dict(obj["cpu"])
                    if obj.get("cpu") is not None
                    else None
                ),
                "memory": (
                    ResourceV1Response.from_dict(obj["memory"])
                    if obj.get("memory") is not None
                    else None
                ),
            }
        )
        return _obj
