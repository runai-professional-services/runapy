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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.job_advanced_data import JobAdvancedData
from runai.models.job_resource_data import JobResourceData
from typing import Optional, Set
from typing_extensions import Self


class JobResourcesDataOvertime(BaseModel):
    """
    Pydantic class model representing JobResourcesDataOvertime.

    Parameters:
        ```python
        gpu: JobResourceData
        gpu_memory: JobResourceData
        cpu: JobResourceData
        cpu_memory: JobResourceData
        advanced: JobAdvancedData
        timestamp: datetime
        ```
        gpu: See model JobResourceData for more information.
        gpu_memory: See model JobResourceData for more information.
        cpu: See model JobResourceData for more information.
        cpu_memory: See model JobResourceData for more information.
        advanced: See model JobAdvancedData for more information.
        timestamp: See model datetime for more information.
    Example:
        ```python
        JobResourcesDataOvertime(
            gpu=runai.models.job_resource_data.JobResourceData(
                    allocated = 2.5,
                    utilization = 0.8, ),
                        gpu_memory=runai.models.job_resource_data.JobResourceData(
                    allocated = 2.5,
                    utilization = 0.8, ),
                        cpu=runai.models.job_resource_data.JobResourceData(
                    allocated = 2.5,
                    utilization = 0.8, ),
                        cpu_memory=runai.models.job_resource_data.JobResourceData(
                    allocated = 2.5,
                    utilization = 0.8, ),
                        advanced=runai.models.job_advanced_data.JobAdvancedData(
                    idle_seconds = 50,
                    gr_engine_active = 1.337,
                    dram_active = 1.337,
                    sm_active = 1.337,
                    sm_occupancy = 1.337,
                    pipe_tensor_active = 1.337,
                    pipe_fp64_active = 1.337,
                    pipe_fp32_active = 1.337,
                    pipe_fp16_active = 1.337,
                    nvlink_tx_bytes = 1.337,
                    nvlink_rx_bytes = 1.337,
                    pcie_tx_bytes = 1.337,
                    pcie_rx_bytes = 1.337, ),
                        timestamp='2023-06-06T12:09:18.211Z'
        )
        ```
    """  # noqa: E501

    gpu: JobResourceData
    gpu_memory: JobResourceData = Field(alias="gpu-memory")
    cpu: JobResourceData
    cpu_memory: JobResourceData = Field(alias="cpu-memory")
    advanced: Optional[JobAdvancedData] = None
    timestamp: datetime
    __properties: ClassVar[List[str]] = [
        "gpu",
        "gpu-memory",
        "cpu",
        "cpu-memory",
        "advanced",
        "timestamp",
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
        """Create an instance of JobResourcesDataOvertime from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of gpu_memory
        if self.gpu_memory:
            _dict["gpu-memory"] = self.gpu_memory.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cpu
        if self.cpu:
            _dict["cpu"] = self.cpu.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cpu_memory
        if self.cpu_memory:
            _dict["cpu-memory"] = self.cpu_memory.to_dict()
        # override the default output from pydantic by calling `to_dict()` of advanced
        if self.advanced:
            _dict["advanced"] = self.advanced.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of JobResourcesDataOvertime from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "gpu": (
                    JobResourceData.from_dict(obj["gpu"])
                    if obj.get("gpu") is not None
                    else None
                ),
                "gpu-memory": (
                    JobResourceData.from_dict(obj["gpu-memory"])
                    if obj.get("gpu-memory") is not None
                    else None
                ),
                "cpu": (
                    JobResourceData.from_dict(obj["cpu"])
                    if obj.get("cpu") is not None
                    else None
                ),
                "cpu-memory": (
                    JobResourceData.from_dict(obj["cpu-memory"])
                    if obj.get("cpu-memory") is not None
                    else None
                ),
                "advanced": (
                    JobAdvancedData.from_dict(obj["advanced"])
                    if obj.get("advanced") is not None
                    else None
                ),
                "timestamp": obj.get("timestamp"),
            }
        )
        return _obj
