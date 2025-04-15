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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.overtime_range_data import OvertimeRangeData
from typing import Optional, Set
from typing_extensions import Self


class OvertimeData(BaseModel):
    """
    Pydantic class model representing OvertimeData.

    Parameters:
        ```python
        range24h_data: Optional[OvertimeRangeData]
        range7d_data: Optional[OvertimeRangeData]
        range30d_data: Optional[OvertimeRangeData]
        ```
        range24h_data: See model OvertimeRangeData for more information.
        range7d_data: See model OvertimeRangeData for more information.
        range30d_data: See model OvertimeRangeData for more information.
    Example:
        ```python
        OvertimeData(
            range24h_data=runai.models.overtime_range_data.OvertimeRangeData(
                    average_gpu_allocation = 10,
                    average_gpu_utilization = 95,
                    updated_at = '2021-08-01T00:00Z', ),
                        range7d_data=runai.models.overtime_range_data.OvertimeRangeData(
                    average_gpu_allocation = 10,
                    average_gpu_utilization = 95,
                    updated_at = '2021-08-01T00:00Z', ),
                        range30d_data=runai.models.overtime_range_data.OvertimeRangeData(
                    average_gpu_allocation = 10,
                    average_gpu_utilization = 95,
                    updated_at = '2021-08-01T00:00Z', )
        )
        ```
    """  # noqa: E501

    range24h_data: Optional[OvertimeRangeData] = Field(
        default=None, alias="range24hData"
    )
    range7d_data: Optional[OvertimeRangeData] = Field(default=None, alias="range7dData")
    range30d_data: Optional[OvertimeRangeData] = Field(
        default=None, alias="range30dData"
    )
    __properties: ClassVar[List[str]] = ["range24hData", "range7dData", "range30dData"]

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
        """Create an instance of OvertimeData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of range24h_data
        if self.range24h_data:
            _dict["range24hData"] = self.range24h_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of range7d_data
        if self.range7d_data:
            _dict["range7dData"] = self.range7d_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of range30d_data
        if self.range30d_data:
            _dict["range30dData"] = self.range30d_data.to_dict()
        # set to None if range24h_data (nullable) is None
        # and model_fields_set contains the field
        if self.range24h_data is None and "range24h_data" in self.model_fields_set:
            _dict["range24hData"] = None

        # set to None if range7d_data (nullable) is None
        # and model_fields_set contains the field
        if self.range7d_data is None and "range7d_data" in self.model_fields_set:
            _dict["range7dData"] = None

        # set to None if range30d_data (nullable) is None
        # and model_fields_set contains the field
        if self.range30d_data is None and "range30d_data" in self.model_fields_set:
            _dict["range30dData"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OvertimeData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "range24hData": (
                    OvertimeRangeData.from_dict(obj["range24hData"])
                    if obj.get("range24hData") is not None
                    else None
                ),
                "range7dData": (
                    OvertimeRangeData.from_dict(obj["range7dData"])
                    if obj.get("range7dData") is not None
                    else None
                ),
                "range30dData": (
                    OvertimeRangeData.from_dict(obj["range30dData"])
                    if obj.get("range30dData") is not None
                    else None
                ),
            }
        )
        return _obj
