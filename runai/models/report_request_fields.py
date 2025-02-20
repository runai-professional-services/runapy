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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from runai.models.report_group_by_options import ReportGroupByOptions
from typing import Optional, Set
from typing_extensions import Self


class ReportRequestFields(BaseModel):
    """
    Pydantic class model representing ReportRequestFields.

    Parameters:
        ```python
        name: str
        description: str
        start: datetime
        end: datetime
        group_by: Optional[ReportGroupByOptions]
        filter_by: List[str]
        ```
        name: See model str for more information.
        description: See model str for more information.
        start: timestamp from when to fetch data in UTC
        end: timestamp until when to fetch data in UTC
        group_by: See model ReportGroupByOptions for more information.
        filter_by: Filter results by a parameter. Use the format field-name &#x3D;&#x3D; value. - Default: []
    Example:
        ```python
        ReportRequestFields(
            name='2023 GPU report',
                        description='This report shows the GPU usage of all projects in the organization',
                        start='2023-06-07T09:09:18.211Z',
                        end='2023-06-07T12:09:18.211Z',
                        group_by='Nodepool',
                        filter_by=["projectName==some-name"]
        )
        ```
    """  # noqa: E501

    name: StrictStr
    description: Optional[StrictStr] = None
    start: datetime = Field(description="timestamp from when to fetch data in UTC")
    end: datetime = Field(description="timestamp until when to fetch data in UTC")
    group_by: Optional[ReportGroupByOptions] = Field(default=None, alias="groupBy")
    filter_by: Optional[List[Annotated[str, Field(strict=True)]]] = Field(
        default=None,
        description="Filter results by a parameter. Use the format field-name == value.",
        alias="filterBy",
    )
    __properties: ClassVar[List[str]] = [
        "name",
        "description",
        "start",
        "end",
        "groupBy",
        "filterBy",
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
        """Create an instance of ReportRequestFields from a JSON string"""
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
        # set to None if group_by (nullable) is None
        # and model_fields_set contains the field
        if self.group_by is None and "group_by" in self.model_fields_set:
            _dict["groupBy"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReportRequestFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "name": obj.get("name"),
                "description": obj.get("description"),
                "start": obj.get("start"),
                "end": obj.get("end"),
                "groupBy": obj.get("groupBy"),
                "filterBy": obj.get("filterBy"),
            }
        )
        return _obj
