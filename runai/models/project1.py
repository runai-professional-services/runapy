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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.project1_current import Project1Current
from runai.models.project1_metadata import Project1Metadata
from runai.models.time_range import TimeRange
from typing import Optional, Set
from typing_extensions import Self


class Project1(BaseModel):
    """
    Pydantic class model representing Project1.

    Parameters:
        ```python
        metadata: Project1Metadata
        current: Project1Current
        time_range: TimeRange
        ```
        metadata: See model Project1Metadata for more information.
        current: See model Project1Current for more information.
        time_range: See model TimeRange for more information.
    Example:
        ```python
        Project1(
            metadata=runai.models.project1_metadata.Project1_metadata(
                    project_id = 1,
                    project_name = 'project-a',
                    department_id = 8,
                    department_name = 'default',
                    cluster_id = '71f69d83-ba66-4822-adf5-55ce55efd210',
                    cluster_name = 'cluster-a', ),
                        current=runai.models.project1_current.Project1_current(
                    resources = [
                        null
                        ], ),
                        time_range=runai.models.time_range.TimeRange(
                    resources = [
                        null
                        ], )
        )
        ```
    """  # noqa: E501

    metadata: Project1Metadata
    current: Project1Current
    time_range: Optional[TimeRange] = Field(default=None, alias="timeRange")
    __properties: ClassVar[List[str]] = ["metadata", "current", "timeRange"]

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
        """Create an instance of Project1 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict["metadata"] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of current
        if self.current:
            _dict["current"] = self.current.to_dict()
        # override the default output from pydantic by calling `to_dict()` of time_range
        if self.time_range:
            _dict["timeRange"] = self.time_range.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Project1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "metadata": (
                    Project1Metadata.from_dict(obj["metadata"])
                    if obj.get("metadata") is not None
                    else None
                ),
                "current": (
                    Project1Current.from_dict(obj["current"])
                    if obj.get("current") is not None
                    else None
                ),
                "timeRange": (
                    TimeRange.from_dict(obj["timeRange"])
                    if obj.get("timeRange") is not None
                    else None
                ),
            }
        )
        return _obj
