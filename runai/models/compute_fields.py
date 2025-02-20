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

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StrictBool,
    StrictFloat,
    StrictInt,
    field_validator,
)
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from runai.models.extended_resource import ExtendedResource
from runai.models.gpu_request_type import GpuRequestType
from runai.models.mig_profile import MigProfile
from typing import Optional, Set
from typing_extensions import Self


class ComputeFields(BaseModel):
    """
    Pydantic class model representing ComputeFields.

    Parameters:
        ```python
        gpu_devices_request: Optional[int]
        gpu_request_type: Optional[GpuRequestType]
        gpu_portion_request: Optional[float]
        gpu_portion_limit: Optional[float]
        gpu_memory_request: Optional[str]
        gpu_memory_limit: Optional[str]
        mig_profile: Optional[MigProfile]
        cpu_core_request: Optional[float]
        cpu_core_limit: Optional[float]
        cpu_memory_request: Optional[str]
        cpu_memory_limit: Optional[str]
        large_shm_request: Optional[bool]
        extended_resources: Optional[List[ExtendedResource]]
        ```
        gpu_devices_request: Requested number of GPU devices. Currently if more than one device is requested, it is not possible to provide values for gpuMemory, gpuPortion or migProfile [deprecated].
        gpu_request_type: See model GpuRequestType for more information.
        gpu_portion_request: Required if and only if gpuRequestType is portion. States the portion of the GPU to allocate for the created workload, per GPU device, between 0 and 1. The default is no allocated GPUs.
        gpu_portion_limit: Limitations on the portion consumed by the workload, per GPU device. The system guarantees The gpuPotionLimit must be no less than the gpuPortionRequest.
        gpu_memory_request: Required if and only if gpuRequestType is memory. States the GPU memory to allocate for the created workload, per GPU device. Note that the workload will not be scheduled unless the system can guarantee this amount of GPU memory to the workload.
        gpu_memory_limit: Limitation on the memory consumed by the workload, per GPU device. The system guarantees The gpuMemoryLimit must be no less than gpuMemoryRequest.
        mig_profile: See model MigProfile for more information.
        cpu_core_request: CPU units to allocate for the created workload (0.5, 1, .etc). The workload will receive at least this amount of CPU. Note that the workload will not be scheduled unless the system can guarantee this amount of CPUs to the workload.
        cpu_core_limit: Limitations on the number of CPUs consumed by the workload (0.5, 1, .etc). The system guarantees that this workload will not be able to consume more than this amount of CPUs.
        cpu_memory_request: The amount of CPU memory to allocate for this workload (1G, 20M, .etc). The workload will receive at least this amount of memory. Note that the workload will not be scheduled unless the system can guarantee this amount of memory to the workload
        cpu_memory_limit: Limitations on the CPU memory to allocate for this workload (1G, 20M, .etc). The system guarantees that this workload will not be able to consume more than this amount of memory. The workload will receive an error when trying to allocate more memory than this limit.
        large_shm_request: A large /dev/shm device to mount into a container running the created workload. An shm is a shared file system mounted on RAM.
        extended_resources: Extended resources and their quantity.
    Example:
        ```python
        ComputeFields(
            gpu_devices_request=1,
                        gpu_request_type='portion',
                        gpu_portion_request=0.5,
                        gpu_portion_limit=0.5,
                        gpu_memory_request='10M',
                        gpu_memory_limit='10M',
                        mig_profile='1g.5gb',
                        cpu_core_request=0.5,
                        cpu_core_limit=2,
                        cpu_memory_request='20M',
                        cpu_memory_limit='30M',
                        large_shm_request=False,
                        extended_resources=[
                    runai.models.extended_resource.ExtendedResource(
                        resource = 'hardware-vendor.example/foo',
                        quantity = '2',
                        exclude = False, )
                    ]
        )
        ```
    """  # noqa: E501

    gpu_devices_request: Optional[StrictInt] = Field(
        default=None,
        description="Requested number of GPU devices. Currently if more than one device is requested, it is not possible to provide values for gpuMemory, gpuPortion or migProfile [deprecated].",
        alias="gpuDevicesRequest",
    )
    gpu_request_type: Optional[GpuRequestType] = Field(
        default=None, alias="gpuRequestType"
    )
    gpu_portion_request: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="Required if and only if gpuRequestType is portion. States the portion of the GPU to allocate for the created workload, per GPU device, between 0 and 1. The default is no allocated GPUs.",
        alias="gpuPortionRequest",
    )
    gpu_portion_limit: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="Limitations on the portion consumed by the workload, per GPU device. The system guarantees The gpuPotionLimit must be no less than the gpuPortionRequest.",
        alias="gpuPortionLimit",
    )
    gpu_memory_request: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None,
        description="Required if and only if gpuRequestType is memory. States the GPU memory to allocate for the created workload, per GPU device. Note that the workload will not be scheduled unless the system can guarantee this amount of GPU memory to the workload.",
        alias="gpuMemoryRequest",
    )
    gpu_memory_limit: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None,
        description="Limitation on the memory consumed by the workload, per GPU device. The system guarantees The gpuMemoryLimit must be no less than gpuMemoryRequest.",
        alias="gpuMemoryLimit",
    )
    mig_profile: Optional[MigProfile] = Field(default=None, alias="migProfile")
    cpu_core_request: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="CPU units to allocate for the created workload (0.5, 1, .etc). The workload will receive at least this amount of CPU. Note that the workload will not be scheduled unless the system can guarantee this amount of CPUs to the workload.",
        alias="cpuCoreRequest",
    )
    cpu_core_limit: Optional[Union[StrictFloat, StrictInt]] = Field(
        default=None,
        description="Limitations on the number of CPUs consumed by the workload (0.5, 1, .etc). The system guarantees that this workload will not be able to consume more than this amount of CPUs.",
        alias="cpuCoreLimit",
    )
    cpu_memory_request: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None,
        description="The amount of CPU memory to allocate for this workload (1G, 20M, .etc). The workload will receive at least this amount of memory. Note that the workload will not be scheduled unless the system can guarantee this amount of memory to the workload",
        alias="cpuMemoryRequest",
    )
    cpu_memory_limit: Optional[Annotated[str, Field(strict=True)]] = Field(
        default=None,
        description="Limitations on the CPU memory to allocate for this workload (1G, 20M, .etc). The system guarantees that this workload will not be able to consume more than this amount of memory. The workload will receive an error when trying to allocate more memory than this limit.",
        alias="cpuMemoryLimit",
    )
    large_shm_request: Optional[StrictBool] = Field(
        default=None,
        description="A large /dev/shm device to mount into a container running the created workload. An shm is a shared file system mounted on RAM.",
        alias="largeShmRequest",
    )
    extended_resources: Optional[List[Optional[ExtendedResource]]] = Field(
        default=None,
        description="Extended resources and their quantity.",
        alias="extendedResources",
    )
    __properties: ClassVar[List[str]] = [
        "gpuDevicesRequest",
        "gpuRequestType",
        "gpuPortionRequest",
        "gpuPortionLimit",
        "gpuMemoryRequest",
        "gpuMemoryLimit",
        "migProfile",
        "cpuCoreRequest",
        "cpuCoreLimit",
        "cpuMemoryRequest",
        "cpuMemoryLimit",
        "largeShmRequest",
        "extendedResources",
    ]

    @field_validator("gpu_memory_request")
    def gpu_memory_request_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([+-]?[0-9.]+)([eEinumkKMGTP]*[-+]?[0-9]*)$", value):
            raise ValueError(
                r"must validate the regular expression /^([+-]?[0-9.]+)([eEinumkKMGTP]*[-+]?[0-9]*)$/"
            )
        return value

    @field_validator("gpu_memory_limit")
    def gpu_memory_limit_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([+-]?[0-9.]+)([eEinumkKMGTP]*[-+]?[0-9]*)$", value):
            raise ValueError(
                r"must validate the regular expression /^([+-]?[0-9.]+)([eEinumkKMGTP]*[-+]?[0-9]*)$/"
            )
        return value

    @field_validator("cpu_memory_request")
    def cpu_memory_request_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^([+-]?[0-9.]+)([eEinumkKMGTP]*[-+]?[0-9]*)$", value):
            raise ValueError(
                r"must validate the regular expression /^([+-]?[0-9.]+)([eEinumkKMGTP]*[-+]?[0-9]*)$/"
            )
        return value

    @field_validator("cpu_memory_limit")
    def cpu_memory_limit_validate_regular_expression(cls, value):
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
        """Create an instance of ComputeFields from a JSON string"""
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
        # set to None if gpu_devices_request (nullable) is None
        # and model_fields_set contains the field
        if (
            self.gpu_devices_request is None
            and "gpu_devices_request" in self.model_fields_set
        ):
            _dict["gpuDevicesRequest"] = None

        # set to None if gpu_request_type (nullable) is None
        # and model_fields_set contains the field
        if (
            self.gpu_request_type is None
            and "gpu_request_type" in self.model_fields_set
        ):
            _dict["gpuRequestType"] = None

        # set to None if gpu_portion_request (nullable) is None
        # and model_fields_set contains the field
        if (
            self.gpu_portion_request is None
            and "gpu_portion_request" in self.model_fields_set
        ):
            _dict["gpuPortionRequest"] = None

        # set to None if gpu_portion_limit (nullable) is None
        # and model_fields_set contains the field
        if (
            self.gpu_portion_limit is None
            and "gpu_portion_limit" in self.model_fields_set
        ):
            _dict["gpuPortionLimit"] = None

        # set to None if gpu_memory_request (nullable) is None
        # and model_fields_set contains the field
        if (
            self.gpu_memory_request is None
            and "gpu_memory_request" in self.model_fields_set
        ):
            _dict["gpuMemoryRequest"] = None

        # set to None if gpu_memory_limit (nullable) is None
        # and model_fields_set contains the field
        if (
            self.gpu_memory_limit is None
            and "gpu_memory_limit" in self.model_fields_set
        ):
            _dict["gpuMemoryLimit"] = None

        # set to None if mig_profile (nullable) is None
        # and model_fields_set contains the field
        if self.mig_profile is None and "mig_profile" in self.model_fields_set:
            _dict["migProfile"] = None

        # set to None if cpu_core_request (nullable) is None
        # and model_fields_set contains the field
        if (
            self.cpu_core_request is None
            and "cpu_core_request" in self.model_fields_set
        ):
            _dict["cpuCoreRequest"] = None

        # set to None if cpu_core_limit (nullable) is None
        # and model_fields_set contains the field
        if self.cpu_core_limit is None and "cpu_core_limit" in self.model_fields_set:
            _dict["cpuCoreLimit"] = None

        # set to None if cpu_memory_request (nullable) is None
        # and model_fields_set contains the field
        if (
            self.cpu_memory_request is None
            and "cpu_memory_request" in self.model_fields_set
        ):
            _dict["cpuMemoryRequest"] = None

        # set to None if cpu_memory_limit (nullable) is None
        # and model_fields_set contains the field
        if (
            self.cpu_memory_limit is None
            and "cpu_memory_limit" in self.model_fields_set
        ):
            _dict["cpuMemoryLimit"] = None

        # set to None if large_shm_request (nullable) is None
        # and model_fields_set contains the field
        if (
            self.large_shm_request is None
            and "large_shm_request" in self.model_fields_set
        ):
            _dict["largeShmRequest"] = None

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
        """Create an instance of ComputeFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "gpuDevicesRequest": obj.get("gpuDevicesRequest"),
                "gpuRequestType": obj.get("gpuRequestType"),
                "gpuPortionRequest": obj.get("gpuPortionRequest"),
                "gpuPortionLimit": obj.get("gpuPortionLimit"),
                "gpuMemoryRequest": obj.get("gpuMemoryRequest"),
                "gpuMemoryLimit": obj.get("gpuMemoryLimit"),
                "migProfile": obj.get("migProfile"),
                "cpuCoreRequest": obj.get("cpuCoreRequest"),
                "cpuCoreLimit": obj.get("cpuCoreLimit"),
                "cpuMemoryRequest": obj.get("cpuMemoryRequest"),
                "cpuMemoryLimit": obj.get("cpuMemoryLimit"),
                "largeShmRequest": obj.get("largeShmRequest"),
                "extendedResources": (
                    [
                        ExtendedResource.from_dict(_item)
                        for _item in obj["extendedResources"]
                    ]
                    if obj.get("extendedResources") is not None
                    else None
                ),
            }
        )
        return _obj
