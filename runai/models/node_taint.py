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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class NodeTaint(BaseModel):
    """
    Pydantic class model representing NodeTaint.

    Parameters:
        ```python
        key: str
        value: str
        effect: str
        ```
        key: The taint key to be applied to a node.
        value: The taint value corresponding to the taint key.
        effect: The effect of the taint on pods that do not tolerate the taint.
    Example:
        ```python
        NodeTaint(
            key='foo',
                        value='bar',
                        effect='NoSchedule'
        )
        ```
    """  # noqa: E501

    key: StrictStr = Field(description="The taint key to be applied to a node.")
    value: Optional[StrictStr] = Field(
        default=None, description="The taint value corresponding to the taint key."
    )
    effect: StrictStr = Field(
        description="The effect of the taint on pods that do not tolerate the taint."
    )
    __properties: ClassVar[List[str]] = ["key", "value", "effect"]

    @field_validator("effect")
    def effect_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(["NoSchedule", "PreferNoSchedule", "NoExecute"]):
            raise ValueError(
                "must be one of enum values ('NoSchedule', 'PreferNoSchedule', 'NoExecute')"
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
        """Create an instance of NodeTaint from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NodeTaint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "key": obj.get("key"),
                "value": obj.get("value"),
                "effect": obj.get("effect"),
            }
        )
        return _obj
