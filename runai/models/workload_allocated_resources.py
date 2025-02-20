# coding: utf-8

"""
    Runai API

    # Introduction  The Run:AI Control-Plane API reference is a guide that provides an easy-to-use programming interface for adding various tasks to your application, including workload submission, resource management, and administrative operations.  Run:ai APIs are accessed using *bearer tokens*. To obtain a token, you need to create an **Application** through the Run:ai user interface. To create an application, in your UI, go to `Settings & Tools`, `Application` and create a new Application.  After you have created a new application, you will need to assign it access rules. To assign access rules to the application, see [Create access rules](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#create-or-delete-rules). Make sure you assign the correct rules to your application. Use the [Roles](https://docs.run.ai/latest/admin/runai-setup/access-control/rbac/?h=create+delete+app#roles) to assign the correct access rules.  To get your access token, follow the instructions in [Request a token](https://docs.run.ai/latest/developer/rest-auth/#request-an-api-token). 

    The version of the OpenAPI document: 2.18
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictFloat,
    StrictInt,
    field_validator,
)
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from runai.models.mig_profile import MigProfile
from runai.models.workloads_extended_resource import WorkloadsExtendedResource
from typing import Optional, Set
from typing_extensions import Self


class WorkloadAllocatedResources(BaseModel):
    """
    Pydantic class model representing WorkloadAllocatedResources.

    Parameters:
        ```python
        gpu: Optional[float]
        mig_profile: Optional[List[MigProfile]]
        gpu_memory: Optional[str]
        cpu: Optional[float]
        cpu_memory: Optional[str]
        extended_resources: Optional[List[WorkloadsExtendedResource]]
        ```
        gpu: Required if and only if gpuRequestType is portion. States the number of GPUs allocated for the created workload. The default is no allocated GPUs.
        mig_profile: See model List[MigProfile] for more information.
        gpu_memory: See model str for more information.
        cpu: States the amount of CPU cores used by the workload running.
        cpu_memory: See model str for more information.
        extended_resources: Set of extended resources with their quantity
    Example:
        ```python
        WorkloadAllocatedResources(
            gpu=1.5,
                        mig_profile=[
                    '1g.5gb'
                    ],
                        gpu_memory='200Mi',
                        cpu=0.5,
                        cpu_memory='0B',
                        extended_resources=[
                    runai.models.workloads_extended_resource.WorkloadsExtendedResource(
                        resource = 'hardware-vendor.example/foo',
                        quantity = '2',
                        exclude = False, )
                    ]
        )
        ```
    """  # noqa: E501

    gpu: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="Required if and only if gpuRequestType is portion. States the number of GPUs allocated for the created workload. The default is no allocated GPUs.",
    )
    mig_profile: Optional[List[Optional[MigProfile]]] = Field(
        default=None, alias="migProfile"
    )
    gpu_memory: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, alias="gpuMemory"
    )
    cpu: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="States the amount of CPU cores used by the workload running.",
    )
    cpu_memory: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None, alias="cpuMemory"
    )
    extended_resources: Optional[List[Optional[WorkloadsExtendedResource]]] = Field(
        default=None,
        description="Set of extended resources with their quantity",
        alias="extendedResources",
    )
    __properties: ClassVar[List[str]] = [
        "gpu",
        "migProfile",
        "gpuMemory",
        "cpu",
        "cpuMemory",
        "extendedResources",
    ]

    @field_validator("gpu_memory")
    def gpu_memory_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([+-]?[0-9.]+)([eEinumkKMGTP]*[-+]?[0-9]*)$", value):
            raise ValueError(
                r"must validate the regular expression /^([+-]?[0-9.]+)([eEinumkKMGTP]*[-+]?[0-9]*)$/"
            )
        return value

    @field_validator("cpu_memory")
    def cpu_memory_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([+-]?[0-9.]+)([eEinumkKMGTP]*[-+]?[0-9]*)$", value):
            raise ValueError(
                r"must validate the regular expression /^([+-]?[0-9.]+)([eEinumkKMGTP]*[-+]?[0-9]*)$/"
            )
        return value

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
        """Create an instance of WorkloadAllocatedResources from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in extended_resources (list)
        _items = []
        if self.extended_resources:
            for _item_extended_resources in self.extended_resources:
                if _item_extended_resources:
                    _items.append(_item_extended_resources.to_dict())
            _dict["extendedResources"] = _items
        # set to None if gpu (nullable) is None
        # and model_fields_set contains the field
        if self.gpu is None and "gpu" in self.model_fields_set:
            _dict["gpu"] = None

        # set to None if mig_profile (nullable) is None
        # and model_fields_set contains the field
        if self.mig_profile is None and "mig_profile" in self.model_fields_set:
            _dict["migProfile"] = None

        # set to None if gpu_memory (nullable) is None
        # and model_fields_set contains the field
        if self.gpu_memory is None and "gpu_memory" in self.model_fields_set:
            _dict["gpuMemory"] = None

        # set to None if cpu (nullable) is None
        # and model_fields_set contains the field
        if self.cpu is None and "cpu" in self.model_fields_set:
            _dict["cpu"] = None

        # set to None if cpu_memory (nullable) is None
        # and model_fields_set contains the field
        if self.cpu_memory is None and "cpu_memory" in self.model_fields_set:
            _dict["cpuMemory"] = None

        # set to None if extended_resources (nullable) is None
        # and model_fields_set contains the field
        if (
            self.extended_resources is None
            and "extended_resources" in self.model_fields_set
        ):
            _dict["extendedResources"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WorkloadAllocatedResources from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "gpu": obj.get("gpu"),
                "migProfile": obj.get("migProfile"),
                "gpuMemory": obj.get("gpuMemory"),
                "cpu": obj.get("cpu"),
                "cpuMemory": obj.get("cpuMemory"),
                "extendedResources": (
                    [
                        WorkloadsExtendedResource.from_dict(_item)
                        for _item in obj["extendedResources"]
                    ]
                    if obj.get("extendedResources") is not None
                    else None
                ),
            }
        )
        return _obj
