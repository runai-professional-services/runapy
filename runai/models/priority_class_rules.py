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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from runai.models.priority_class_options_options_inner import (
    PriorityClassOptionsOptionsInner,
)
from runai.models.source_of_rule import SourceOfRule
from typing import Optional, Set
from typing_extensions import Self


class PriorityClassRules(BaseModel):
    """
    Pydantic class model representing PriorityClassRules.

    Parameters:
        ```python
        source_of_rule: Optional[SourceOfRule]
        required: Optional[bool]
        can_edit: Optional[bool]
        options: Optional[List[PriorityClassOptionsOptionsInner]]
        ```
        source_of_rule: See model SourceOfRule for more information.
        required: Whether the field is mandatory, default to false.
        can_edit: Whether the value of the field is editable, default to true
        options: See model List[PriorityClassOptionsOptionsInner] for more information.
    Example:
        ```python
        PriorityClassRules(
            source_of_rule={"scope":"project","projectId":3},
                        required=True,
                        can_edit=True,
                        options=[
                    runai.models.priority_class_options_options_inner.PriorityClassOptions_options_inner(
                        value = 'build',
                        displayed = '', )
                    ]
        )
        ```
    """  # noqa: E501

    source_of_rule: Optional[SourceOfRule] = Field(default=None, alias="sourceOfRule")
    required: Optional[StrictBool] = Field(
        default=None, description="Whether the field is mandatory, default to false."
    )
    can_edit: Optional[StrictBool] = Field(
        default=None,
        description="Whether the value of the field is editable, default to true",
        alias="canEdit",
    )
    options: Optional[List[PriorityClassOptionsOptionsInner]] = None
    __properties: ClassVar[List[str]] = [
        "sourceOfRule",
        "required",
        "canEdit",
        "options",
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
        """Create an instance of PriorityClassRules from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of source_of_rule
        if self.source_of_rule:
            _dict["sourceOfRule"] = self.source_of_rule.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in options (list)
        _items = []
        if self.options:
            for _item_options in self.options:
                if _item_options:
                    _items.append(_item_options.to_dict())
            _dict["options"] = _items
        # set to None if source_of_rule (nullable) is None
        # and model_fields_set contains the field
        if self.source_of_rule is None and "source_of_rule" in self.model_fields_set:
            _dict["sourceOfRule"] = None

        # set to None if required (nullable) is None
        # and model_fields_set contains the field
        if self.required is None and "required" in self.model_fields_set:
            _dict["required"] = None

        # set to None if can_edit (nullable) is None
        # and model_fields_set contains the field
        if self.can_edit is None and "can_edit" in self.model_fields_set:
            _dict["canEdit"] = None

        # set to None if options (nullable) is None
        # and model_fields_set contains the field
        if self.options is None and "options" in self.model_fields_set:
            _dict["options"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PriorityClassRules from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "sourceOfRule": (
                    SourceOfRule.from_dict(obj["sourceOfRule"])
                    if obj.get("sourceOfRule") is not None
                    else None
                ),
                "required": obj.get("required"),
                "canEdit": obj.get("canEdit"),
                "options": (
                    [
                        PriorityClassOptionsOptionsInner.from_dict(_item)
                        for _item in obj["options"]
                    ]
                    if obj.get("options") is not None
                    else None
                ),
            }
        )
        return _obj
