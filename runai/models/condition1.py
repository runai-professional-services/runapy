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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class Condition1(BaseModel):
    """
    Pydantic class model representing Condition1.

    Parameters:
        ```python
        type: str
        status: str
        message: str
        reason: str
        last_transition_time: Optional[datetime]
        ```
        type: The type of the condition, such as Failed or Available. See Types of domain status conditions.
        status: The status of the condition, such as True, False or Unknown.
        message: An optional, human-readable message providing more details about the condition.
        reason: The reason for the Failed condition. Not applicable to other types of condition.
        last_transition_time: A timestamp of when the condition was created or the last time time the condition transitioned from one status to another.
    Example:
        ```python
        Condition1(
            type='Ready',
                        status='False',
                        message='Resource validation failed: ...',
                        reason='ErrorConfig',
                        last_transition_time='2022-01-01T03:49:52.531Z'
        )
        ```
    """  # noqa: E501

    type: StrictStr = Field(
        description="The type of the condition, such as Failed or Available. See Types of domain status conditions."
    )
    status: StrictStr = Field(
        description="The status of the condition, such as True, False or Unknown."
    )
    message: Optional[StrictStr] = Field(
        default=None,
        description="An optional, human-readable message providing more details about the condition.",
    )
    reason: Optional[StrictStr] = Field(
        default=None,
        description="The reason for the Failed condition. Not applicable to other types of condition.",
    )
    last_transition_time: Optional[datetime] = Field(
        default=None,
        description="A timestamp of when the condition was created or the last time time the condition transitioned from one status to another.",
        alias="lastTransitionTime",
    )
    __properties: ClassVar[List[str]] = [
        "type",
        "status",
        "message",
        "reason",
        "lastTransitionTime",
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
        """Create an instance of Condition1 from a JSON string"""
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
        # set to None if last_transition_time (nullable) is None
        # and model_fields_set contains the field
        if (
            self.last_transition_time is None
            and "last_transition_time" in self.model_fields_set
        ):
            _dict["lastTransitionTime"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Condition1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "type": obj.get("type"),
                "status": obj.get("status"),
                "message": obj.get("message"),
                "reason": obj.get("reason"),
                "lastTransitionTime": obj.get("lastTransitionTime"),
            }
        )
        return _obj
